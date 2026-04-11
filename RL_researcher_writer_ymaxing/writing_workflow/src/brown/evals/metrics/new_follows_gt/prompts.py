"""Prompt templates and examples for the FollowsGT evaluation metric.

This module contains the system prompt template used
for evaluating how well generated articles follow ground truth content across
six dimensions (core_content, flow, structure, depth_enhancement,
breadth_enhancement, core_preservation).
"""

from pathlib import Path

from brown.evals.metrics.base import CriterionScore, SectionCriteriaScores

from .types import (
    FollowsGTArticleScores,
    FollowsGTCriteriaScores,
    FollowsGTMetricExample,
    FollowsGTMetricFewShotExamples,
)

SYSTEM_PROMPT = """You are an expert in Natural Language Processing (NLP) evaluation metrics, specifically trained to 
assess answer quality in responses provided by large language models (LLMs). 

Your task is to evaluate the quality of a generated article by another LLM relative to 
an expected article output across six criteria: core_content, flow, structure, 
depth_enhancement, breadth_enhancement, and core_preservation.

## INSTRUCTIONS 

1. You must analyze the given expected article (<expected_output>) and generated article (<generated_output>) 
to determine the most relevant evaluation.
2. Since the generated output is an answer from another LLM, you will use the expected output as the reference 
standard to compare and evaluate the quality of the generated output.
3. Both the generated and expected outputs are in Markdown format.
4. Instead of comparing the outputs as a whole, you will divide the outputs into sections and compare each section 
individually. 
5. You will always use the expected output as the reference point to extract the sections of interest during the
evaluation. If there is no perfect match between the expected and generated section names, first try to infer
the corresponding section based on the similarity of section names and their respective content. If you conclude that 
the expected output contains a section that the generated output lacks, you will assign a score of 0 to the missing 
section in the generated output.
6. Sections are divided by H2 headers, marked as "##" in Markdown. You will use these headers as 
separators. Anything between two H2 headers constitutes a section. The only valid exception to this rule is the first 
section, the introduction, which sometimes appears between the title and the first H2 header. You will never include 
the title or subtitle as part of the first section.
7. The prompt automatically detects whether the <expected_output> contains multiple H2 sections or is a single paragraph/block.
   - If the expected_output is a single paragraph/block (no H2 headers), use SINGLE-PARAGRAPH MODE.
   - If the expected_output contains multiple H2 headers, use MULTI-SECTION MODE.
   - Throughout the criteria below, some sub-points are tagged with **[USE ONLY IN MULTI-SECTION MODE]**. This tag is a conditional marker:
     • If you are in MULTI-SECTION MODE, apply the tagged sub-point as part of the criterion.
     • If you are in SINGLE-PARAGRAPH MODE, skip the tagged sub-point entirely — it does not apply.
     • Sub-points with no tag always apply in both modes.
8. When comparing each individual section of the expected output to the generated output, you will assign a binary 
score for multiple criteria: 0 or 1, where 0 indicates a non-match and 1 indicates a perfect match, for each of the six criteria. Each 
criterion is completely independent of the others, meaning that a score of 0 in one criterion does not affect the score of 
another criterion. 
9. You must compute binary scores for each section based on the following criteria:
   1. **CoreContent:** Evaluate whether the generated section covers the same content as the expected section:
      - Focus ONLY on evaluating that the substance of the content is the same between the expected and generated section. By content, we 
    mean core subjects, topics, research, ideas, key points or arguments. For example, if both sections discuss the
    fundamentals of RAG, it's valid. But, if the expected section discusses advanced RAG topics, while the generated section
    discusses basic RAG topics, it's invalid. 
      - In this criterion, we are not interested in the order, structure, layout, or any other aspect related to the flow of
    ideas, structure or mechanics. For example, if there are missing or additional ideas discussed it's still valid, as
    long as the substance of the content between the expected and generated section is the same.
      - If the expected section relies on a specific non-trivial named example or artifact — such as a named code class, 
    dataset, algorithm, or API — that plays a central role in illustrating the main idea of the section (not merely mentioned 
    in passing or indirectly implied), using a different named example or artifact in the generated section is a content 
    mismatch. Non-trivial means the example is the primary vehicle through which the section's core concept is demonstrated. 
    For example, if the expected section uses a `DocumentMetadata` Pydantic class as the central implementation example to 
    showcase how Pydantic structured outputs work, but the generated section instead uses a `RedditThread` class for the same 
    purpose, this is a content mismatch and scores 0, even if the general technique or teaching is otherwise similar.
      - The scope of the generated section must match the scope of the expected section. If the expected section discusses 
    a topic broadly (e.g., "deep research AI assistant systems"), a generated section that narrows the focus to a specific 
    subdomain or instance of that topic (e.g., a "financial AI assistant") constitutes a scope mismatch and scores 0, even 
    though the subdomain is technically a subset of the broader topic. The generated section must cover the same breadth of 
    scope as the expected section.
   2.**Flow:** Evaluate whether the generated section follows the same order of ideas as the expected section, such as 
   the flow of:
      - [USE ONLY IN MULTI-SECTION MODE] Main ideas covered starting with the beginning, until the end of the section. With special 
      emphasis on the beginning and end of the section as they reflect the transition between the previous and next sections
      - Internal transitions between the main points within the section. We expect a smooth flow of ideas, 
      without any abrupt jumps or breaks.
      - Placement of notes, images, tables, code blocks, or any other media elements within the generated section, 
      relative to the expected section. 
      - We don't expect a perfect one on one match between the paragraphs and sentences between the expected and generated section.
      However, we expect the same ideas and concepts to be discussed in the same way, order, and storyline.
      - Assign a score of 0 if anything is missing from the generated section relative to the expected section, such as missing
      topics, ideas, or media.
      - Accepted differences between the expected and generated section:    
         - Addtional complementary ideas in the generated section that enrich the content in depth and/or breadth without breaking the flow 
         of the main ideas in the expected section. For example, if the expected section introduces RAG and its main components, while the 
         generated section also includes additional relevant information about the latest advancements in RAG, it's valid. 
         - Mismatching media numbering is accepted. For example, if in the expected section we have a figure with the number 3 and
         in the generated section we have a figure with the number 4, it's valid. It will be invalid, only if the figure would be
         missing altogether.
         - Mismatching or missing emojis. For example, if the expected section has a 💡 emoji, while the generated section has 
         a 🔑 emoji, it's valid. Also, if the emoji is missing altogether from the generated section, it's valid.
         - Mismatching source reference numbers. For example, if the expected section refers a source with the number 3, 
         while the generated section refers a source with the number 7, it's valid. It will be invalid, only if the generated
         section misses the source altogether. 
         - Different placement of the source in the generated section. For example, if the expected section has the source
         at the end of a sentence within the paragraph, while the generated section has it at the end of the paragraph, it's valid. 
         It will be invalid, only if the generated section would be missing altogether.
         - Mismatching number of source references. For example, if the expected section has 3 source references, while the 
         generated section has 2 source references, it's valid. It will be invalid, only if the generated section would have 
         misses the references altogether. For example if the expected section has 3 source references, while the generated 
         section has 0 source references, it's invalid.
         - Having reference numbers in the generated section, while having none in the expected section. For example, if the 
         expected section has 0 reference numbers, while the generated section has 3 reference number, it's valid. It will be 
         invalid, only the other way around, where the expected section has 3 reference numbers, while the generated section has 0. 
   3. **Structure:** Evaluate whether the generated section follows the same structure as the expected section. By 
   structure, we mean:
      - [USE ONLY IN MULTI-SECTION MODE] H3/H4/H5/H6 sub-heading structure and formatting
      - Mismatches in headers formatting and presence. For example, if the expected section doesn't have a header,
      while the generated section has one, it's invalid. It's valid only if there is a one on one match between the headers
      formatting and presence.
      - Paragraph length and structure patterns
      - Use of bulleted lists, numbered lists, callouts, notes, or other layout elements
      - Division of the section when guiding readers through code blocks or diagrams
      - Use of bolding, italicizing, quotes, backticks, or other formatting elements
      - Formatting of citation references across sentences
      - Formatting of images, tables, and Mermaid diagrams and their corresponding citations. If they are missing from
      the generated section, we consider it valid for this criterion, as we are interested ONLY in formatting, which we
      cannot verify when elements are absent. For this criterion, missing elements from the generated sections are 
      considered valid. They are invalid only if present in both sections but formatted differently.
      - Formatting of notes and code blocks
      - Number formatting conventions
   4. **DepthEnhancement:** Evaluate whether the section contains valuable *depth* additions that originated from the exploration 
        phase of the research agent.
      - Depth additions must be one or more of the following (taken directly from the complementary-query definition):
        • theoretical foundations or mathematical underpinnings
        • technical nuances or alternative implementation perspectives
        • latest developments or recent advancements
        • limitations, criticisms, or failure modes
        • implementation challenges, latency/scale trade-offs, or engineering realities
        • real-world case studies with concrete metrics or outcomes
        • future implications or open research directions
      - The addition must be relevant to the main topic/theme of the ground truth section and must enrich the content without 
        contradicting any ground truth facts.
      - Score 1 if at least one such high-quality depth element is present and meaningfully integrated.
      - Score 0 if no depth addition exists, the addition is shallow/superficial, or it is irrelevant to the ground truth section.
   5. **BreadthEnhancement:** Evaluate whether the section contains valuable *breadth* additions that originated from the exploration
         phase of the research agent.
      - Breadth additions must be one or more of the following (taken directly from the complementary-query definition):
        • adjacent or related concepts that expand the scope without straying from the core theme
        • cross-domain analogies or lessons from other fields
        • historical context or evolution of the topic
        • enabling/disrupting technologies that intersect with the core topic
        • practical applications in other industries or real-world scenarios
        • emerging trends connected to the main topic
      - The addition must be relevant to the main topic/theme of the ground truth section and must expand the article usefully.
      - Score 1 if at least one such high-quality breadth element is present and meaningfully integrated.
      - Score 0 if no breadth addition exists, the addition is off-topic, or it is merely tangential marketing fluff.
   6. **CorePreservation:** Evaluate whether the exploration additions (depth or breadth) preserve the ground truth core.
      - The ground truth core (main ideas, storyline, key examples, emphasis, and logical weight) must remain the dominant focus
        of the section.
      - Exploration material may support or enrich the core but must never dilute, overshadow, bury, or shift the primary narrative 
        away from the ground truth.
      - Score 1 if the ground truth core is still clearly the primary narrative and any exploration additions are in service of it.
      - Score 0 if the added material crowds out, repeats excessively, or changes the emphasis of the original ground truth core content.
10. Along with the binary scores, you will provide a brief and concise explanation containing the reasoning behind 
the score for each criterion. The score will be used to debug and monitor the evaluation process. Therefore, it is
important to provide thorough reasoning for the score. Since we provide binary scores, the reasoning should always 
contain what is good and what is problematic about the generated section, regardless of the score. For example, if the 
score is 0, the reasoning should also contain what is good about the generated section, such as "both sections 
follow the same flow of ideas," and what is problematic, such as "the generated section contains an additional 
paragraph on AI Evals that is not present in the expected section." When scoring depth_enhancement or breadth_enhancement, 
explicitly state which specific type of addition (from the lists above) was present or missing.
11.Important rules when comparing the content of sections:
      - Focus on substance, not superficial formatting differences
      - When comparing **media**, you only care about the placement of the media, not the content of the media. 
      Since media can take many forms such as Mermaid diagrams, tables, images, or URLs, you will completely ignore the 
      content of the media and only check whether the media is present in the correct place in the section, has 
      the appropriate citation, and proper numbering.

## CHAIN OF THOUGHT

**Understanding Input:**
1.1. Read, understand, and compare each section of the expected output and generated output.
1.2. Determine if the ground truth article is a single section/paragraph/block. If yes, use SINGLE-PARAGRAPH MODE; 
    if not, use MULTI-SECTION MODE.
1.3. In the case of MULTI-SECTION MODE, split the expected output into sections using H2 headers as separators; 
    in the case of SINGLE-PARAGRAPH MODE, use the entire block as a single section.

**Splitting into Sections:**
2.1. Using the expected output as the reference point, compare each section of the expected and generated 
outputs individually and assign a binary score of 0 or 1, where 0 indicates a mismatch and 1 indicates a perfect match.
2.2. Always use the expected output as the reference point to extract the sections of interest. 
2.3. When computing the score for an individual section, you will iterate through each section of the expected output, 
find its associated section in the generated output, and compute all six criteria using the mode-specific rules above 
for that section in isolation, ignoring all other sections. 

**Assigning Scores to Each Section:**
3.1. Based on all sections of the expected output, assign a binary score of either 0 or 1 
for all evaluation criteria listed in the instructions:
   - **1:** The generated section matches the expected section perfectly on the given criterion.
   - **0:** The generated section does not match the expected section on the given criterion.
If a required section is missing from the generated output, assign 0 to all six criteria.
3.2. Justify why you assigned a score of 0 or 1 with a brief explanation that highlights the reasoning behind the score
based on the given criterion.

## WHAT TO AVOID

- Do not provide scores using the generated output as the reference point to divide into sections. You must always 
use the expected output as the reference point to divide into sections.
- Do not let other sections influence the score of a section. The score of each section must be determined in complete 
isolation from any other section.
- Do not overlap requirements between different criteria. For example, in the content criterion, as are not interested in the flow 
of ideas, if the ideas are in different order, or something is missing, it's still valid. However, that is an important
aspect of the flow criterion, which will be invalid. Another two examples are that flow differences must not affect 
the core_content score, and that
a strong depth addition must not affect the core_preservation score unless it actually dilutes the core.

## FEW-SHOT EXAMPLES

Here are few-shot examples demonstrating how to compute the scores for each section and criterion:
<few-shot-examples>
{examples}
</few-shot-examples>

## INPUTS

<generated_output>
{output}
</generated_output>

<expected_output>
{expected_output}
</expected_output>

Think through your answer step by step, and provide the requested evaluation.
"""

EXAMPLES_DIR = Path(__file__).parent / "examples"
DEFAULT_FEW_SHOT_EXAMPLES = FollowsGTMetricFewShotExamples(
    examples=[
        # ── Lesson 4: Structured Outputs ────────────────────────────
        FollowsGTMetricExample.from_markdown(
            output_file=EXAMPLES_DIR / "04_structured_outputs" / "article_generated.md",
            expected_output_file=EXAMPLES_DIR / "04_structured_outputs" / "article_ground_truth.md",
            scores=FollowsGTArticleScores(
                sections=[
                    SectionCriteriaScores(
                        title="Introduction",
                        scores=FollowsGTCriteriaScores(
                            core_content=CriterionScore(
                                score=1,
                                reason=(
                                    "Both sections cover the same core subjects and ideas, discussing the purpose "
                                    "of structured outputs as a bridge between LLMs (Software 3.0) and traditional "
                                    "applications (Software 1.0). The generated section includes an additional "
                                    "paragraph on the historical evolution of data formats, but the substance of "
                                    "the content remains the same."
                                ),
                            ),
                            flow=CriterionScore(
                                score=0,
                                reason=(
                                    "The generated section lacks the first sentence, which in the expected output "
                                    "serves as a smooth transition from the previous lessons into the article. "
                                    "Also, it misses the diagram present in the expected output, labeled as Figure 1. "
                                    "The additional paragraph about data format history does not break the flow of "
                                    "the main ideas and is an accepted complementary addition."
                                ),
                            ),
                            structure=CriterionScore(
                                score=1,
                                reason="Both sections use the same paragraph length patterns.",
                            ),
                            depth_enhancement=CriterionScore(
                                score=0,
                                reason=(
                                    "No depth additions are present in the generated section. The content closely "
                                    "follows the ground truth without adding theoretical foundations, technical "
                                    "nuances, real-world case studies, or any other qualifying depth element."
                                ),
                            ),
                            breadth_enhancement=CriterionScore(
                                score=1,
                                reason=(
                                    "The generated section includes a paragraph tracing the evolution of structured "
                                    "data formats from XML in the late 1990s through JSON and YAML to the current "
                                    "Pydantic era. This qualifies as 'historical context or evolution of the topic' "
                                    "and is meaningfully integrated into the narrative about why structured outputs "
                                    "matter for LLMs."
                                ),
                            ),
                            core_preservation=CriterionScore(
                                score=1,
                                reason=(
                                    "The ground truth core — introducing structured outputs as the bridge between "
                                    "LLMs and traditional applications — remains the clearly dominant narrative. "
                                    "The historical context paragraph is a brief addition that supports the core "
                                    "argument without diluting or shifting the emphasis."
                                ),
                            ),
                        ),
                    ),
                    SectionCriteriaScores(
                        title="Why Structured Outputs Are Critical",
                        scores=FollowsGTCriteriaScores(
                            core_content=CriterionScore(
                                score=1,
                                reason=(
                                    "Both sections cover the same reasons why structured outputs are critical, "
                                    "including ease of parsing, data validation with Pydantic, and common use "
                                    "cases like entity extraction for knowledge graphs. The generated section "
                                    "has an additional paragraph on GraphRAG, but the substance of the core "
                                    "content about why structured outputs matter is the same."
                                ),
                            ),
                            flow=CriterionScore(
                                score=0,
                                reason=(
                                    "Follows a similar logical flow, starting with the importance, detailing "
                                    "benefits, discussing use cases, and concluding with a diagram. However, the "
                                    "generated section contains an additional paragraph on GraphRAG that disrupts "
                                    "the flow between the diagram and the closing sentence. Additionally, it omits "
                                    "the last transition sentence setting up the three implementation approaches."
                                ),
                            ),
                            structure=CriterionScore(
                                score=1,
                                reason=(
                                    "Both sections use the same paragraph length patterns and have the same usage "
                                    "pattern for backticks and citation references across sentences. Also, the figures "
                                    "and their corresponding citations use the same formatting rules."
                                ),
                            ),
                            depth_enhancement=CriterionScore(
                                score=0,
                                reason=(
                                    "The GraphRAG paragraph is irrelevant to the section's topic about why "
                                    "structured outputs are critical. It does not provide depth on structured "
                                    "outputs (no theoretical foundations, limitations, or implementation "
                                    "challenges related to structured outputs). It is an off-topic addition "
                                    "about a different technology."
                                ),
                            ),
                            breadth_enhancement=CriterionScore(
                                score=0,
                                reason=(
                                    "The GraphRAG paragraph is off-topic and does not expand the scope of "
                                    "'why structured outputs are critical' in a useful way. It discusses a "
                                    "completely different technology (graph-based RAG) rather than providing "
                                    "adjacent concepts, cross-domain analogies, or historical context related "
                                    "to structured outputs."
                                ),
                            ),
                            core_preservation=CriterionScore(
                                score=0,
                                reason=(
                                    "The GraphRAG paragraph adds substantial irrelevant material that shifts "
                                    "focus away from the ground truth's emphasis on structured outputs' benefits. "
                                    "It crowds out the core narrative by inserting an entire paragraph about "
                                    "knowledge graph traversal and semantic relationships, which are unrelated "
                                    "to the section's purpose of explaining why structured outputs are critical."
                                ),
                            ),
                        ),
                    ),
                    SectionCriteriaScores(
                        title="Implementing Structured Outputs From Scratch Using JSON",
                        scores=FollowsGTCriteriaScores(
                            core_content=CriterionScore(
                                score=1,
                                reason=(
                                    "Both sections provide a step-by-step guide on implementing structured outputs "
                                    "using JSON from scratch, covering client setup, document definition, prompt "
                                    "crafting, and parsing."
                                ),
                            ),
                            flow=CriterionScore(
                                score=0,
                                reason=("The generated section omits the Note callout box present in the expected output."),
                            ),
                            structure=CriterionScore(
                                score=0,
                                reason=(
                                    "Both sections use the same paragraph length, number formatting, numbered lists "
                                    "and division of code blocks patterns. However, the generated section incorrectly "
                                    "formats the JSON code block under point 4), where it misses the closing ```. "
                                    "Also, in the last section, where it outputs the final JSON structure, it doesn't "
                                    "enclose the JSON into Python backticks as expected: ```python <content> ```"
                                ),
                            ),
                            depth_enhancement=CriterionScore(
                                score=1,
                                reason=(
                                    "The generated section includes a paragraph about failure modes of manual JSON "
                                    "parsing, noting that LLMs frequently produce trailing commas, invalid comments, "
                                    "and unescaped characters, with concrete data showing ~12%% of LLM-generated "
                                    "JSON outputs contain syntax errors. This qualifies as 'limitations, criticisms, "
                                    "or failure modes' and is directly relevant to the section's topic of manual "
                                    "JSON-based structured outputs."
                                ),
                            ),
                            breadth_enhancement=CriterionScore(
                                score=0,
                                reason=(
                                    "No breadth additions are present. The section focuses on the JSON "
                                    "implementation without adding adjacent concepts, cross-domain analogies, "
                                    "historical context, or applications in other industries."
                                ),
                            ),
                            core_preservation=CriterionScore(
                                score=1,
                                reason=(
                                    "The depth addition about JSON failure modes is naturally integrated at the "
                                    "end of the section and serves the core narrative about implementing structured "
                                    "outputs from scratch. The ground truth core — the step-by-step JSON guide — "
                                    "remains the clearly dominant focus."
                                ),
                            ),
                        ),
                    ),
                    SectionCriteriaScores(
                        title="Implementing Structured Outputs From Scratch Using Pydantic",
                        scores=FollowsGTCriteriaScores(
                            core_content=CriterionScore(
                                score=0,
                                reason=(
                                    "Both sections accurately explain the benefits of Pydantic for structured outputs, "
                                    "demonstrate defining models, generating schemas, and validating responses, and "
                                    "compare it with other Python types. Still, the generated section uses different "
                                    "code examples, using a RedditThread Pydantic Python class instead of the expected "
                                    "DocumentMetadata class, which does not comply with the expected example specially "
                                    "required in the ground truth article."
                                ),
                            ),
                            flow=CriterionScore(
                                score=1,
                                reason=(
                                    "Even though the sections use different code examples, the flow of ideas is "
                                    "the same: introducing Pydantic, demonstrating its implementation through "
                                    "numbered steps with code, and concluding with a comparison to other data "
                                    "validation methods. The additional paragraph about Pydantic v2 is a "
                                    "complementary depth addition that does not break the main flow."
                                ),
                            ),
                            structure=CriterionScore(
                                score=1,
                                reason=(
                                    "Both sections maintain a similar structure: introductory paragraphs, "
                                    "numbered steps with code blocks, and a concluding comparison. The formatting "
                                    "of Python code and JSON blocks is the same. Also, backticks and citation "
                                    "references follow the same pattern."
                                ),
                            ),
                            depth_enhancement=CriterionScore(
                                score=1,
                                reason=(
                                    "The generated section includes a paragraph about Pydantic v2's major "
                                    "architectural overhaul, noting the Rust-based validation core that achieved "
                                    "5-50x performance improvements. This qualifies as both 'latest developments "
                                    "or recent advancements' and 'technical nuances or alternative implementation "
                                    "perspectives' and is directly relevant to the Pydantic section."
                                ),
                            ),
                            breadth_enhancement=CriterionScore(
                                score=0,
                                reason=(
                                    "No breadth additions are present. The section stays focused on Pydantic "
                                    "without adding adjacent concepts, historical context, cross-domain analogies, "
                                    "or applications in other industries."
                                ),
                            ),
                            core_preservation=CriterionScore(
                                score=1,
                                reason=(
                                    "The Pydantic v2 paragraph is directly relevant and well-integrated as a "
                                    "closing note to the section. The ground truth core — teaching how to use "
                                    "Pydantic for structured outputs with step-by-step code — remains the "
                                    "clearly dominant narrative throughout the section."
                                ),
                            ),
                        ),
                    ),
                    SectionCriteriaScores(
                        title="Implementing Structured Outputs Using Gemini and Pydantic",
                        scores=FollowsGTCriteriaScores(
                            core_content=CriterionScore(
                                score=1,
                                reason=(
                                    "Both sections accurately describe the native implementation of structured "
                                    "outputs using the Gemini API and Pydantic."
                                ),
                            ),
                            flow=CriterionScore(
                                score=0,
                                reason=(
                                    "Both sections follow a similar logical flow, introducing native API support "
                                    "and then demonstrating its implementation through steps with code. However, "
                                    "the generated section misses the first sentence used to transition from the "
                                    "previous section, and also misses points 3) and 4) from the code walkthrough "
                                    "numbered list."
                                ),
                            ),
                            structure=CriterionScore(
                                score=0,
                                reason=(
                                    "In both sections, the use of citation references and backticks is the same. "
                                    "Also, the structure of the introductory paragraph, division of code blocks "
                                    "and conclusion follow the same pattern. However, the generated section uses a "
                                    "bulleted list to divide the code blocks instead of a numbered list as expected."
                                ),
                            ),
                            depth_enhancement=CriterionScore(
                                score=0,
                                reason=(
                                    "No depth additions related to Gemini's structured output implementation are "
                                    "present. The competitor API comparison is a breadth addition, not depth."
                                ),
                            ),
                            breadth_enhancement=CriterionScore(
                                score=1,
                                reason=(
                                    "The generated section includes an extensive paragraph comparing how other "
                                    "providers (OpenAI, Anthropic, Cohere, Mistral, and open-source tools like "
                                    "Outlines and Instructor) implement structured outputs, including constrained "
                                    "decoding and grammar-based generation with CFGs. This qualifies as 'adjacent "
                                    "or related concepts that expand the scope without straying from the core theme' "
                                    "and 'enabling/disrupting technologies that intersect with the core topic.'"
                                ),
                            ),
                            core_preservation=CriterionScore(
                                score=0,
                                reason=(
                                    "The extensive comparison with competitor APIs overwhelms the section, which "
                                    "in the ground truth is specifically focused on demonstrating Gemini's native "
                                    "structured output capabilities. The competitor paragraph is longer than the "
                                    "entire Gemini-specific content and shifts the section's emphasis from a "
                                    "hands-on Gemini tutorial to a general industry comparison, diluting the "
                                    "ground truth's focused narrative."
                                ),
                            ),
                        ),
                    ),
                    SectionCriteriaScores(
                        title="Structured Outputs Are Everywhere",
                        scores=FollowsGTCriteriaScores(
                            core_content=CriterionScore(
                                score=1,
                                reason=(
                                    "Both sections serve as a conclusion, summarizing the importance of structured "
                                    "outputs as a fundamental pattern in AI engineering."
                                ),
                            ),
                            flow=CriterionScore(
                                score=0,
                                reason=(
                                    "Both sections follow a similar flow, summarizing the key takeaway. However, the "
                                    "generated section omits the final sentences that set the scene for future lessons "
                                    "in the course."
                                ),
                            ),
                            structure=CriterionScore(
                                score=0,
                                reason=(
                                    "Both sections use the same paragraph length patterns. However, the number "
                                    "formatting of the citation reference from the first paragraph misses the "
                                    "square brackets."
                                ),
                            ),
                            depth_enhancement=CriterionScore(
                                score=0,
                                reason=(
                                    "No depth additions are present. The section is a brief conclusion without "
                                    "any additional theoretical foundations, technical nuances, or real-world "
                                    "case studies."
                                ),
                            ),
                            breadth_enhancement=CriterionScore(
                                score=0,
                                reason=(
                                    "No breadth additions are present. The section does not include adjacent "
                                    "concepts, cross-domain analogies, historical context, or applications in "
                                    "other industries."
                                ),
                            ),
                            core_preservation=CriterionScore(
                                score=1,
                                reason=(
                                    "No exploration material was added, so the ground truth core — summarizing "
                                    "structured outputs as a fundamental pattern — remains fully intact."
                                ),
                            ),
                        ),
                    ),
                    SectionCriteriaScores(
                        title="References",
                        scores=FollowsGTCriteriaScores(
                            core_content=CriterionScore(
                                score=1,
                                reason="Both sections contain a list of references, similar in purpose.",
                            ),
                            flow=CriterionScore(
                                score=1,
                                reason=("Both sections follow the same flow for referencing the sources, as a numbered list from 1 to n."),
                            ),
                            structure=CriterionScore(
                                score=1,
                                reason=(
                                    "Both sections use the same pattern to structure the references, as a "
                                    "bulleted list, where each element is structured as "
                                    "[<reference_number>] [<reference_name>](<reference_url>)"
                                ),
                            ),
                            depth_enhancement=CriterionScore(
                                score=0,
                                reason=("Not applicable for a references section. No depth additions present."),
                            ),
                            breadth_enhancement=CriterionScore(
                                score=0,
                                reason=("Not applicable for a references section. No breadth additions present."),
                            ),
                            core_preservation=CriterionScore(
                                score=1,
                                reason=(
                                    "The references section serves its purpose without modification. No exploration material was added."
                                ),
                            ),
                        ),
                    ),
                ]
            ),
        ),
        # ── Lesson 7: Planning and Reasoning ────────────────────────
        FollowsGTMetricExample.from_markdown(
            output_file=EXAMPLES_DIR / "07_reasoning_planning" / "article_generated.md",
            expected_output_file=EXAMPLES_DIR / "07_reasoning_planning" / "article_ground_truth.md",
            scores=FollowsGTArticleScores(
                sections=[
                    SectionCriteriaScores(
                        title="Introduction",
                        scores=FollowsGTCriteriaScores(
                            core_content=CriterionScore(
                                score=1,
                                reason=(
                                    "Covers the same core subjects and ideas, discussing the limitations of standard "
                                    "LLMs and the need for planning and reasoning in AI agents."
                                ),
                            ),
                            flow=CriterionScore(
                                score=0,
                                reason=(
                                    "Both sections set the scene of the lesson, discussing the 'why' behind the need "
                                    "for planning and reasoning in AI agents. However, the generated introduction "
                                    "omits the sentences that talk about the previous lessons and anchor the lesson "
                                    "within the course. The historical context paragraph about STRIPS and SHRDLU is "
                                    "an accepted complementary breadth addition that does not break the main flow."
                                ),
                            ),
                            structure=CriterionScore(
                                score=0,
                                reason=(
                                    "The generated output uses an H2 header 'Why Your Agent Needs to Think Before "
                                    "It Acts' as a title for the introduction, while the expected section does not "
                                    "have any headers."
                                ),
                            ),
                            depth_enhancement=CriterionScore(
                                score=0,
                                reason=(
                                    "No depth additions are present. The historical context about STRIPS and SHRDLU "
                                    "is a breadth addition (historical context), not depth. No theoretical "
                                    "foundations, technical nuances, or real-world case studies were added."
                                ),
                            ),
                            breadth_enhancement=CriterionScore(
                                score=1,
                                reason=(
                                    "The generated section includes a paragraph about the historical roots of AI "
                                    "planning, tracing it from early symbolic AI systems like STRIPS (1971) and "
                                    "SHRDLU (1970) to the current LLM-based neural paradigm. This qualifies as "
                                    "'historical context or evolution of the topic' and is meaningfully integrated "
                                    "into the introduction's argument about why planning matters."
                                ),
                            ),
                            core_preservation=CriterionScore(
                                score=1,
                                reason=(
                                    "The ground truth core — introducing the need for planning and reasoning in "
                                    "AI agents — remains the clearly dominant narrative. The historical context "
                                    "paragraph is a brief, supporting addition that enriches without overwhelming."
                                ),
                            ),
                        ),
                    ),
                    SectionCriteriaScores(
                        title="What a Non-Reasoning Model Does And Why It Fails on Complex Tasks",
                        scores=FollowsGTCriteriaScores(
                            core_content=CriterionScore(
                                score=1,
                                reason=(
                                    "Accurately covers the core subject of why non-reasoning models fail on complex "
                                    "tasks, using the same 'Technical Research Assistant Agent' example and discussing "
                                    "similar failure points."
                                ),
                            ),
                            flow=CriterionScore(
                                score=1,
                                reason=(
                                    "Follows a similar order of ideas, starting with the example, explaining the "
                                    "failure, and then discussing the need for reasoning. The benchmark data "
                                    "paragraph is a complementary depth addition that does not break the main flow."
                                ),
                            ),
                            structure=CriterionScore(
                                score=1,
                                reason=(
                                    "Both sections have similar paragraph length patterns and use of images and "
                                    "their corresponding citations."
                                ),
                            ),
                            depth_enhancement=CriterionScore(
                                score=1,
                                reason=(
                                    "The generated section includes concrete benchmark data showing that "
                                    "non-reasoning models achieve only 23%% success rate on tasks with more "
                                    "than five sequential steps vs 67%% for reasoning-augmented agents, with "
                                    "near-zero recovery rates on error recovery tasks. This qualifies as "
                                    "'real-world case studies with concrete metrics or outcomes' and is directly "
                                    "relevant to the section's argument about non-reasoning model failures."
                                ),
                            ),
                            breadth_enhancement=CriterionScore(
                                score=0,
                                reason=(
                                    "No breadth additions are present. The section stays focused on explaining "
                                    "why non-reasoning models fail without adding adjacent concepts, historical "
                                    "context, or cross-domain analogies."
                                ),
                            ),
                            core_preservation=CriterionScore(
                                score=1,
                                reason=(
                                    "The benchmark data supports and reinforces the core argument about why "
                                    "non-reasoning models fail. The ground truth core — demonstrating failure "
                                    "through the research assistant example — remains the dominant narrative."
                                ),
                            ),
                        ),
                    ),
                    SectionCriteriaScores(
                        title='Teaching Models to "Think": Chain-of-Thought and Its Limits',
                        scores=FollowsGTCriteriaScores(
                            core_content=CriterionScore(
                                score=0,
                                reason=(
                                    "The generated section begins with the expected topic on the Chain-of-Thought "
                                    "concept, but in the second paragraph, it shifts entirely to discussing "
                                    "Retrieval-Augmented Generation (RAG), which is a completely different topic "
                                    "from the expected section's content about CoT's practical limitations, "
                                    "the single-pass problem, and the need for separating thinking from acting."
                                ),
                            ),
                            flow=CriterionScore(
                                score=0,
                                reason=(
                                    "Both sections start by introducing CoT, but then the generated section "
                                    "diverges to RAG, which is an entirely different topic, completely departing "
                                    "from the expected flow. The expected section proceeds from CoT introduction "
                                    "to its limitations, a diagram, a Note callout, and the need for separation "
                                    "— all of which are missing."
                                ),
                            ),
                            structure=CriterionScore(
                                score=0,
                                reason=(
                                    "The generated section uses the same citation strategy and number formatting, "
                                    "but the paragraphs are much longer than expected. Also, the generated section "
                                    "lacks the diagram and the 'Note' callout box."
                                ),
                            ),
                            depth_enhancement=CriterionScore(
                                score=0,
                                reason=(
                                    "The RAG content is irrelevant to the section's topic about Chain-of-Thought "
                                    "and its limits. While the RAG paragraphs contain technical detail (embedding "
                                    "models, NDCG scores, hallucination rates), none of this qualifies as depth "
                                    "enrichment for CoT because it is about a completely different technology. "
                                    "No depth additions relevant to CoT are present."
                                ),
                            ),
                            breadth_enhancement=CriterionScore(
                                score=0,
                                reason=(
                                    "The RAG content is off-topic and does not expand the scope of 'Chain-of-Thought "
                                    "and its limits' in a useful way. It discusses an unrelated technology rather "
                                    "than providing adjacent concepts, cross-domain analogies, or historical context "
                                    "related to CoT prompting."
                                ),
                            ),
                            core_preservation=CriterionScore(
                                score=0,
                                reason=(
                                    "The RAG paragraphs completely overwhelm and replace the expected CoT content. "
                                    "The ground truth core — explaining CoT's limitations, the single-pass problem, "
                                    "and the need for separating thinking from acting — is almost entirely absent. "
                                    "The added material shifts the section's narrative from CoT to RAG."
                                ),
                            ),
                        ),
                    ),
                    SectionCriteriaScores(
                        title="Separating Planning from Answering: Foundations of ReAct and Plan-and-Execute",
                        scores=FollowsGTCriteriaScores(
                            core_content=CriterionScore(
                                score=1,
                                reason=(
                                    "Accurately describes the core idea of separating planning from answering and "
                                    "introduces ReAct and Plan-and-Execute as the two dominant strategies."
                                ),
                            ),
                            flow=CriterionScore(
                                score=0,
                                reason=(
                                    "Both sections follow the same logical progression, starting with the core idea "
                                    "of separation and then introducing the two patterns. However, the last sentence "
                                    "from the generated section is very abrupt, being a poor transition to the next "
                                    "section."
                                ),
                            ),
                            structure=CriterionScore(
                                score=0,
                                reason=(
                                    "The generated section maintains a similar paragraph length, number formatting, "
                                    "and citation strategy. However, it covers the ReAct and Plan-and-Execute "
                                    "topics within a paragraph instead of a bullet list with the names of the "
                                    "algorithms being bolded."
                                ),
                            ),
                            depth_enhancement=CriterionScore(
                                score=0,
                                reason=(
                                    "No meaningful depth additions are present. The generated section describes "
                                    "benefits of the separation (control, iterative loops, different handling of "
                                    "outputs) but these are the same points covered in the ground truth, not "
                                    "additional depth. No theoretical foundations, concrete metrics, implementation "
                                    "challenges, or real-world case studies beyond the ground truth are provided."
                                ),
                            ),
                            breadth_enhancement=CriterionScore(
                                score=0,
                                reason=(
                                    "No breadth additions are present. The section stays focused on the same "
                                    "concepts as the ground truth without adding adjacent concepts, historical "
                                    "context, or cross-domain analogies."
                                ),
                            ),
                            core_preservation=CriterionScore(
                                score=1,
                                reason=(
                                    "No exploration material was added that could dilute the core. The ground "
                                    "truth's narrative about the separation principle and the two patterns remains "
                                    "fully intact as the dominant focus."
                                ),
                            ),
                        ),
                    ),
                    SectionCriteriaScores(
                        title="ReAct in Depth: The Loop of Thought, Action, and Observation",
                        scores=FollowsGTCriteriaScores(
                            core_content=CriterionScore(
                                score=1,
                                reason=(
                                    "Both sections provide the same detailed explanation of the ReAct framework, "
                                    "its iterative Thought-Action-Observation loop, and a step-by-step example "
                                    "using the research assistant agent."
                                ),
                            ),
                            flow=CriterionScore(
                                score=0,
                                reason=(
                                    "Both sections begin with the same flow, introducing ReAct, explaining its "
                                    "loop, and presenting the diagram. However, the generated section places the "
                                    "advantages and disadvantages of ReAct before the hands-on example, instead "
                                    "of after it as in the expected output."
                                ),
                            ),
                            structure=CriterionScore(
                                score=0,
                                reason=(
                                    "The generated section employs a similar strategy to format the diagram's "
                                    "citation and references. However, in the expected section, the example is "
                                    "formatted as a numbered list, while in the generated section, it is formatted "
                                    "as a bulleted list. Also, the generated section added backticks around the "
                                    "text from Action 1, 2, 3, and 4, while the expected section does not."
                                ),
                            ),
                            depth_enhancement=CriterionScore(
                                score=1,
                                reason=(
                                    "The generated section includes specific benchmark data from the ReAct paper, "
                                    "noting 8-14%% accuracy improvements on HotpotQA and FEVER benchmarks, and "
                                    "that humans rated ReAct's reasoning traces as 1.4x more trustworthy than "
                                    "CoT-only baselines. This qualifies as 'real-world case studies with concrete "
                                    "metrics or outcomes' and is directly relevant to understanding ReAct's value."
                                ),
                            ),
                            breadth_enhancement=CriterionScore(
                                score=1,
                                reason=(
                                    "The generated section draws a cross-domain analogy between ReAct's "
                                    "Thought-Action-Observation loop and the OODA loop (Observe-Orient-Decide-Act) "
                                    "from military strategy, developed by John Boyd in the 1970s. This qualifies "
                                    "as 'cross-domain analogies or lessons from other fields' and meaningfully "
                                    "enriches the reader's understanding by connecting AI agent design to "
                                    "established decision-making theory."
                                ),
                            ),
                            core_preservation=CriterionScore(
                                score=1,
                                reason=(
                                    "Both the benchmark data and the OODA analogy are concise additions placed "
                                    "after the main example. The ground truth core — explaining the ReAct loop "
                                    "and demonstrating it through the step-by-step research assistant example — "
                                    "remains the clearly dominant narrative throughout the section."
                                ),
                            ),
                        ),
                    ),
                    SectionCriteriaScores(
                        title="Plan-and-Execute in Depth: Structure and Predictability",
                        scores=FollowsGTCriteriaScores(
                            core_content=CriterionScore(
                                score=1,
                                reason=(
                                    "Accurately explains the Plan-and-Execute pattern, its two phases "
                                    "(Planning and Execution), and its benefits for predictable tasks."
                                ),
                            ),
                            flow=CriterionScore(
                                score=0,
                                reason=(
                                    "Both sections follow a similar logical flow, introducing the pattern, "
                                    "explaining its efficiency, and then detailing the planning and execution "
                                    "phases with an example. However, the Plan-and-Execute diagram was expected "
                                    "before the Planning Phase section, and instead it is placed within the "
                                    "numbered list of the Planning Phase section."
                                ),
                            ),
                            structure=CriterionScore(
                                score=0,
                                reason=(
                                    "The generated section employs a similar strategy for the diagram's citation, "
                                    "number formatting, references, and the bulleted list. However, it formats "
                                    "the planning and execution phases as bolded text instead of as H3 headers."
                                ),
                            ),
                            depth_enhancement=CriterionScore(
                                score=0,
                                reason=(
                                    "No depth additions beyond the ground truth content are present. The section "
                                    "covers the same concepts without adding theoretical foundations, concrete "
                                    "metrics, or implementation challenges."
                                ),
                            ),
                            breadth_enhancement=CriterionScore(
                                score=1,
                                reason=(
                                    "The generated section includes a paragraph about practical applications of "
                                    "Plan-and-Execute in diverse industries: healthcare clinical trial management, "
                                    "legal discovery document review, and supply chain optimization. This qualifies "
                                    "as 'practical applications in other industries or real-world scenarios' and "
                                    "meaningfully expands the reader's understanding of where this pattern applies."
                                ),
                            ),
                            core_preservation=CriterionScore(
                                score=1,
                                reason=(
                                    "The industry applications paragraph is a concise addition placed after the "
                                    "main pros/cons discussion. The ground truth core — explaining the two-phase "
                                    "pattern with the planning and execution phases — remains the clearly dominant "
                                    "narrative throughout the section."
                                ),
                            ),
                        ),
                    ),
                    SectionCriteriaScores(
                        title="Pros and Cons: ReAct vs. Plan-and-Execute",
                        scores=FollowsGTCriteriaScores(
                            core_content=CriterionScore(
                                score=0,
                                reason="The generated output completely omits this section.",
                            ),
                            flow=CriterionScore(
                                score=0,
                                reason="The generated output completely omits this section.",
                            ),
                            structure=CriterionScore(
                                score=0,
                                reason="The generated output completely omits this section.",
                            ),
                            depth_enhancement=CriterionScore(
                                score=0,
                                reason="The generated output completely omits this section.",
                            ),
                            breadth_enhancement=CriterionScore(
                                score=0,
                                reason="The generated output completely omits this section.",
                            ),
                            core_preservation=CriterionScore(
                                score=0,
                                reason="The generated output completely omits this section.",
                            ),
                        ),
                    ),
                    SectionCriteriaScores(
                        title="Deep Research AI Assistant Systems",
                        scores=FollowsGTCriteriaScores(
                            core_content=CriterionScore(
                                score=0,
                                reason=(
                                    "Both sections discuss how ReAct and Plan-and-Execute patterns are applied in "
                                    "real-world settings, but the expected output uses a deep research system as "
                                    "an example, while the generated one uses a financial assistant as the example, "
                                    "which is just a specific type of deep research systems and thus unduly narrows the "
                                    "focus of the section to a specific domain (finance) rather than discussing deep "
                                    "research systems more broadly as in the expected output."
                                ),
                            ),
                            flow=CriterionScore(
                                score=0,
                                reason=(
                                    "Both sections follow a similar progression: introducing real-world systems, "
                                    "explaining how they apply the patterns, and discussing hybrid approaches. "
                                    "However, the generated section completely misses the expected Mermaid diagram "
                                    "at the end of the section."
                                ),
                            ),
                            structure=CriterionScore(
                                score=1,
                                reason=(
                                    "Both sections have similar paragraph length patterns, number formatting, and "
                                    "citation patterns. The diagram is missing from the generated section, but for "
                                    "the structure criterion, missing elements are considered valid since we can "
                                    "only evaluate formatting when elements are present in both."
                                ),
                            ),
                            depth_enhancement=CriterionScore(
                                score=1,
                                reason=(
                                    "The generated section includes an extensive paragraph about financial "
                                    "sector-specific implementation constraints: MiFID II and SEC Rule 17a-4 "
                                    "regulatory requirements, Bloomberg/Reuters data feed integration processing "
                                    "250,000+ updates/second, T+2 settlement lifecycles via DTCC, and Basel III "
                                    "VaR computations using Monte Carlo simulations. This qualifies as "
                                    "'implementation challenges, latency/scale trade-offs, or engineering "
                                    "realities' and 'real-world case studies with concrete metrics or outcomes.'"
                                ),
                            ),
                            breadth_enhancement=CriterionScore(
                                score=0,
                                reason=(
                                    "No breadth additions are present. The financial implementation details "
                                    "are depth-oriented (specific technical constraints and metrics), not "
                                    "breadth-oriented (no adjacent concepts, cross-domain analogies, or "
                                    "historical context)."
                                ),
                            ),
                            core_preservation=CriterionScore(
                                score=0,
                                reason=(
                                    "The extensive financial implementation paragraph overwhelms the section's "
                                    "core message. The ground truth focuses on how the theoretical patterns "
                                    "(ReAct and Plan-and-Execute) power real-world deep research systems, with "
                                    "the emphasis on the patterns themselves. The generated section shifts the "
                                    "emphasis to domain-specific financial constraints (regulatory compliance, "
                                    "settlement lifecycles, VaR computations), burying the original narrative "
                                    "about pattern application under dense financial engineering detail."
                                ),
                            ),
                        ),
                    ),
                    SectionCriteriaScores(
                        title=('Reasoning Models: How LLMs\' "Reasoning and Planning" are Being Internalized in LLMs'),
                        scores=FollowsGTCriteriaScores(
                            core_content=CriterionScore(
                                score=0,
                                reason="The generated section is completely empty.",
                            ),
                            flow=CriterionScore(
                                score=0,
                                reason="The generated section is completely empty.",
                            ),
                            structure=CriterionScore(
                                score=0,
                                reason="The generated section is completely empty.",
                            ),
                            depth_enhancement=CriterionScore(
                                score=0,
                                reason="The generated section is completely empty.",
                            ),
                            breadth_enhancement=CriterionScore(
                                score=0,
                                reason="The generated section is completely empty.",
                            ),
                            core_preservation=CriterionScore(
                                score=0,
                                reason="The generated section is completely empty.",
                            ),
                        ),
                    ),
                    SectionCriteriaScores(
                        title="Conclusion",
                        scores=FollowsGTCriteriaScores(
                            core_content=CriterionScore(
                                score=1,
                                reason=(
                                    "In both sections, the conclusion summarizes the key takeaways of the article, "
                                    "including the importance of planning and reasoning, and the two foundational "
                                    "patterns (ReAct and Plan-and-Execute)."
                                ),
                            ),
                            flow=CriterionScore(
                                score=1,
                                reason=(
                                    "Follows a similar flow, reiterating the main points within the lesson "
                                    "and setting the scene for future lessons."
                                ),
                            ),
                            structure=CriterionScore(
                                score=1,
                                reason=("Both sections have similar paragraph length, number formatting, and citation patterns."),
                            ),
                            depth_enhancement=CriterionScore(
                                score=0,
                                reason=(
                                    "No depth additions are present in the generated conclusion. The tangential "
                                    "sentence about 'greatest human leaders' is not a depth addition — it "
                                    "contains no theoretical foundations, technical nuances, concrete metrics, "
                                    "or real-world case studies."
                                ),
                            ),
                            breadth_enhancement=CriterionScore(
                                score=0,
                                reason=(
                                    "The generated section contains a sentence comparing AI reasoning patterns "
                                    "to human leadership ('Just as the greatest human leaders...'). While this "
                                    "superficially resembles a cross-domain analogy, it is merely tangential "
                                    "marketing fluff that does not meaningfully expand understanding or connect "
                                    "to a concrete cross-domain lesson. It lacks substance and specificity."
                                ),
                            ),
                            core_preservation=CriterionScore(
                                score=1,
                                reason=(
                                    "The tangential sentence does not overwhelm or dilute the core conclusion. "
                                    "The ground truth core — summarizing the key patterns and looking ahead to "
                                    "future lessons — remains the clearly dominant narrative. The fluff sentence "
                                    "is a single addition that does not shift the emphasis."
                                ),
                            ),
                        ),
                    ),
                    SectionCriteriaScores(
                        title="References",
                        scores=FollowsGTCriteriaScores(
                            core_content=CriterionScore(
                                score=1,
                                reason="Both sections contain a list of citations, similar in purpose.",
                            ),
                            flow=CriterionScore(
                                score=1,
                                reason=("Both sections follow the same flow for referencing the sources, as a numbered list from 1 to n."),
                            ),
                            structure=CriterionScore(
                                score=0,
                                reason=(
                                    "Both sections use a bulleted list to enumerate the citations, but the "
                                    "use of parentheses is not the same. The generated article outputs the "
                                    "references as `- [<number>] <reference_name>(<url>)` instead of "
                                    "`- [[<number>]](<url>) <article_name>`."
                                ),
                            ),
                            depth_enhancement=CriterionScore(
                                score=0,
                                reason=("Not applicable for a references section. No depth additions present."),
                            ),
                            breadth_enhancement=CriterionScore(
                                score=0,
                                reason=("Not applicable for a references section. No breadth additions present."),
                            ),
                            core_preservation=CriterionScore(
                                score=1,
                                reason=(
                                    "The references section serves its purpose without modification. No exploration material was added."
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
    output: str,
    expected_output: str,
    few_shot_examples: FollowsGTMetricFewShotExamples,
) -> str:
    """Generate the evaluation prompt for the ground_truth metric.

    This function formats the system prompt with the provided generated output, expected output,
    and few-shot examples to create a comprehensive prompt for the language model evaluation.

    Args:
        output: The generated article content to be evaluated.
        expected_output: The expected article content for comparison.
        few_shot_examples: An instance of FollowsGTMetricFewShotExamples containing examples
         to guide the language model's evaluation.

    Returns:
        The complete formatted prompt string ready for LLM invocation.
    """
    # Path("context.md").write_text(few_shot_examples.to_context())
    return SYSTEM_PROMPT.format(
        examples=few_shot_examples.to_context(),
        output=output,
        expected_output=expected_output,
    )
