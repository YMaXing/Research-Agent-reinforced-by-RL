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
an expected article output across five criteria: core_content, flow, structure,
    depth_enhancement, and breadth_enhancement.

## INSTRUCTIONS 

1. You must analyze the given expected article (<expected_output>) and generated article (<generated_output>) 
to determine the most relevant evaluation.
2. Since the generated output is an answer from another LLM, you will use the expected output as the reference 
standard to compare and evaluate the quality of the generated output.
3. Both the generated and expected outputs are in Markdown format.
4. Instead of comparing the outputs as a whole, you will divide the outputs into sections and compare each section 
individually. 
5. You will always use the expected output as the reference point to extract the sections of interest during the
evaluation. Before evaluating any criteria, you MUST complete a one-time section-resolution pass:
   a. For each H2 section in the expected output, find its counterpart in the generated output:
      i. First look for a section with an identical or similar H2 title.
      ii. If no title match, search for a section whose content clearly covers the same topic and main points.
   b. Record each mapping (e.g., "Expected 'Practical Example' → Generated 'Here is an example'") or mark it
      MISSING if no counterpart can be found anywhere in the generated output.
   c. Apply this mapping consistently for all five criteria evaluation. If you established a content-based match in
      step (ii), that section is NOT missing — use the identified generated section for all criteria.
   d. Only mark a section MISSING if, after both title and content searches, no corresponding content exists anywhere
      in the generated output.
   A different section title alone never makes a section missing. A section is missing only when there is truly
   no content covering that topic anywhere in the generated output.
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
score for multiple criteria: 0 or 1, where 0 indicates a non-match and 1 indicates a perfect match, for each of the five criteria. Each 
criterion is completely independent of the others, meaning that a score of 0 in one criterion does not affect the score of 
another criterion. 
9. You must compute binary scores for each section based on the following criteria:
   1. **CoreContent:** Evaluate whether the generated section covers all the expected content with the correct topical identity:
      - All expected ideas, topics, key points, and arguments from the expected section must be present in the generated section.
    Score 0 if any substantive idea present in the expected section is absent from the generated section.
    Additional ideas in the generated section (depth/breadth additions or supporting narratives) are perfectly fine — completeness
    only checks for omissions, not additions.
      - The substance of the content must match: by content, we mean core subjects, topics, research, ideas, key points or
    arguments. For example, if both sections discuss the fundamentals of RAG, it's valid. But, if the expected section discusses
    advanced RAG topics, while the generated section discusses basic RAG topics, it's invalid.
      - In this criterion, we are not interested in the order, structure, layout, or any other aspect related to the flow of
    ideas, structure or mechanics. Ideas discussed in a different order are still valid for this criterion.
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
    though the subdomain is technically a subset of the broader topic. The generated section must cover the same
    scope as the expected section.
      - **CoreContent is strictly about the presence of ideas, not their formatting.** Sub-heading presence or absence
    (H3/H4 headers), numbered vs. unnumbered lists, paragraph count, indentation, or any other formatting differences
    are NOT content issues — they belong exclusively to Structure (criterion 3). For example, if the expected section
    presents four strategies under four H3 sub-headers while the generated section discusses the same four strategies
    as four plain paragraphs, CoreContent must score 1 if the substantive content of each strategy is present,
    regardless of the formatting difference.
      - **Sub-section content is matched by substance, not by label.** When evaluating CoreContent for a mapped
    section, do NOT look for H3/H4 sub-heading titles to verify sub-section presence. Instead, look for the IDEAS
    and concepts that each expected sub-section covers and check whether those ideas appear anywhere within the
    generated section — as inline text, a diagram caption, a mermaid block, or any other form. An expected sub-section
    titled "Core Components of a ReAct AI Agent" is PRESENT if the generated section discusses those components
    (LLM reasoning, tools, memory) anywhere, even without using that heading title.
      - **Media absence never scores CoreContent=0.** The absence of an image, diagram, or mermaid block from the
    generated section is strictly a Flow failure. A section that covers all expected textual ideas but omits an
    expected figure scores CoreContent=1 and Flow=0, never CoreContent=0. Never cite "missing diagram" or
    "missing image" as a reason for CoreContent=0.
      - **An idea buried to the point of unrecognizability counts as absent.** If a non-qualifying addition (see
    criteria 4/5) is so extensive that an expected idea is never actually stated in a form a reader would recognize
    as covering that point — not merely surrounded by other content, but effectively unstated — treat it as MISSING
    and score CoreContent=0. This is different from an idea that IS clearly stated but sits inside a confusing or
    disrupted narrative; that latter case is a Flow concern, not CoreContent — see the "Flow Precision Tests"
    section (Test 2) for the full three-way boundary between CoreContent, Flow, and neither.
   2. **Flow:** Evaluate whether the ideas present in the generated section follow the same order as the expected
      section, with smooth transitions and media elements correctly placed:
      - [USE ONLY IN MULTI-SECTION MODE] **Reordering is a coherence test, not a sequence-matching test.** The
      default expectation is that the generated section follows the same progression as the expected section. A
      generated section that instead presents the same ideas in a genuinely different order is NOT automatically a
      Flow failure — apply Test 1 ("Reordering Coherence Test") from the "## Flow Precision Tests" section (search
      for that exact heading) before scoring: order differences only fail Flow when the alternate order actually
      disrupts the reader's ability to follow the argument, not merely because it diverges from the expected
      section's chosen sequence. With special emphasis on the beginning and end of the section as they reflect the
      transition between the previous and next sections. Specifically, look at the last paragraph of the expected section and ask:
      does the expected section end with closing transition sentences that explicitly bridge to the next section (e.g., "Now that
      we understand X, let's look at Y")? If yes, check whether the generated section also ends with such a closing transition.
      Missing closing transition sentence(s) that are present in the expected section but absent from the generated section score 0.
      - Internal transitions between the main points within the section. We expect a smooth flow of ideas, 
      without any abrupt jumps or breaks.
      - Placement of notes, images, tables, code blocks, or any other media elements within the generated section, 
      relative to the expected section. 
      - We don't expect a perfect one on one match between the paragraphs and sentences between the expected and generated section.
      However, we expect the same ideas and concepts to be discussed in the same way, order, and storyline.
      - When the section contains complementary additions interspersed with expected ideas, use the following filtering procedure:
      mentally identify the expected ideas and the additions separately. Evaluate the relative order of the expected ideas by stepping over
      the additions. Then check that transitions between consecutive expected ideas — skipping over any additions that appear between
      them — are smooth. Additions may have their own local lead-in and lead-out sentences connecting them to neighboring expected
      ideas; these are acceptable and do not affect the Flow score, as long as the expected ideas still appear in their expected
      relative sequence.
      - Assign a score of 0 for any of the following: a reordering of ideas that fails Test 1 ("Reordering Coherence Test") in
      the "## Flow Precision Tests" section, transition sentences (internal or cross-section closings) present in the expected section are 
      absent from the generated section, or media elements are missing or misplaced. Do not score Flow=0 for missing topics or ideas —
      that is exclusively handled by CoreContent. However, if the absence of an expected idea leaves a bridgeless gap in the
      narrative — an abrupt transition between the surrounding ideas that are present — that transition failure is a legitimate
      Flow=0 reason, as it is a narrative continuity failure distinct from the content absence captured by CoreContent.
      See the accepted differences below for items that do not count as flow failures.
      - Accepted differences between the expected and generated section:    
         - Additional complementary ideas in the generated section that enrich the content via depth or breadth
           additions (as defined in criteria 4 and 5) without breaking the flow of the main ideas in the expected
           section. For example, if the expected section introduces RAG and its main components, while the generated
           section also includes additional relevant information about the latest advancements in RAG, it's valid.
           Additions that fail both depth_enhancement and breadth_enhancement are not qualifying complementary
           additions and are not covered by this rule.
           **Whether a large non-qualifying addition is a problem, and for which criterion, is governed by Test 2
           ("Three-Way Crowding Boundary") in the "## Flow Precision Tests" section — never by a length/proportion
           calculation.** Sheer length alone, with every expected idea still recognizable and the narrative still
           easy to follow, is not a Flow failure (nor a CoreContent failure — see Test 2 for the full three-way split).
         - Supporting narrative additions — including anecdotes, motivating examples, or real-world stories used to
           illustrate or ground a concept from the expected section — placed anywhere within the section (before,
           after, or between expected section ideas) are accepted, provided all expected section ideas remain present
           in the same relative order and the addition does not replace or crowd out any expected section idea.
         - Mismatching media numbering is accepted. For example, if in the expected section we have a figure with the number 3 and
         in the generated section we have a figure with the number 4, it's valid. It will be invalid, only if the figure would be
         missing altogether.
         - Media format substitution is accepted. A Mermaid diagram block (` ```mermaid ... ``` `) in the generated section is
         considered equivalent to and satisfies the placement requirement of a static image reference (e.g., `![Figure N](url)`)
         in the expected section, and vice versa. Both are valid forms of visual media and are interchangeable for the purposes
         of this criterion. A media placement failure only occurs when no visual element of any kind (neither a static image nor
         a Mermaid diagram nor any other media form) is present at a position where the expected section places one.
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
      formatting and presence. The article-level H1 title is excluded from this check — it is the article title, not a
      section sub-header, and its presence or absence does not affect the Structure score.
      - Paragraph length and structure patterns. When the section contains accepted additions (supporting narratives,
      depth or breadth enhancements, or any other interspersed content), apply the same filtering procedure as Flow:
      evaluate the paragraph length and structure patterns of the ground truth ideas only, stepping over the additions.
      Differences in total paragraph count or length caused solely by accepted additions are not a structure failure.
      - Use of bulleted lists, numbered lists, callouts, notes, or other layout elements
      - Division of the section when guiding readers through code blocks or diagrams
      - Use of bolding, italicizing, quotes, backticks, or other formatting elements
      - Formatting of citation references across sentences
      - Formatting of images, tables, and Mermaid diagrams and their corresponding citations. If they are missing from
      the generated section, we consider it valid for this criterion, as we are interested ONLY in formatting, which we
      cannot verify when elements are absent. For this criterion, missing elements from the generated sections are 
      considered valid. They are invalid only if present in both sections but formatted differently.
      Similarly, extra media elements (images, tables, Mermaid diagrams, or any other artifacts) that appear in the 
      generated section but are absent from the expected section are also not a structure failure — they are additions, 
      not substitutions or restructuring. Structure only evaluates how elements are formatted when they are present in 
      both sections, not whether the generated section introduces extra media artifacts.
      - Formatting of notes and code blocks
      - Number formatting conventions
      - **The `## References` section is excluded from this criterion** — differences in how reference entries
      are formatted in the terminal references list never count as a structure failure.

   > **Shared principle for criteria 4 and 5 (DepthEnhancement and BreadthEnhancement):** *Depth* means intensifying
   > understanding of the core topic — the addition stays within the same subject but reveals more of its inner workings,
   > limits, or advanced nuances. *Breadth* means connecting outward to adjacent areas — the addition moves beyond the core
   > subject to related concepts, other fields, or wider contexts that illuminate it from the outside. These are independent
   > criteria: a section can score 1 on depth, breadth, both, or neither. An *addition* is content present in the generated
   > section that goes beyond what the expected section covers. The *core topic* is always the topic of the expected section,
   > regardless of whether the generated section drifts to a different subject.
   >
   > **The numeric score stays binary (0/1) as before, but the reason field must ALSO report every distinct qualifying
   > instance found, not just whether at least one exists.** A single-instance and a six-instance section both still
   > score 1 — the binary score is a downstream aggregation input, not where instance count is captured — but the reason
   > text is what preserves the richer signal for later analysis. Do not stop enumerating once one instance qualifies;
   > continue evaluating every remaining candidate addition in the section and report on all of them.
   >
   > **⚠ MANDATORY LOOKUP before counting any candidate instance:** apply Test 1 (dual-qualification), Test 2
   > (instance-boundary/clustering), and Test 3 (quality floor) from the **"## Depth/Breadth Precision Tests"**
   > section further below in this prompt — search for that exact heading text. Do not rely on the one-line summary
   > above; that section has the full rules and worked examples required to apply them correctly.

   4. **DepthEnhancement:** Evaluate whether the section contains valuable additions that go deeper into the core topic itself.
      - **Depth additions** (inward — intensify understanding of the core topic itself) include one or more of the following:
        • motivation for the core topic — why it exists, what problem it solves, or what need it addresses
        • theoretical foundations or mathematical underpinnings
        • technical nuances or alternative implementation perspectives
        • latest advancements or recent developments in the core topic itself
        • limitations, criticisms, or failure modes of the core topic
        • implementation challenges, latency/scale trade-offs, or engineering realities
        • real-world case studies or concrete metrics about the core topic's performance, behavior, or direct application
        • future implications or open research directions for the core topic
      - The addition must be relevant to the main topic/theme of the ground truth section and must not contradict any ground
        truth facts.
      - Score 1 if at least one depth element passes both the quality check and the source attribution gate below.
      - Score 0 if no depth element passes both checks — whether because no enhancements are present,
        all are shallow/superficial/off-topic/irrelevant, or none can be traced to an exploration source.
      - **Source attribution gate — always active, evaluated per instance:** Assess each candidate depth
        enhancement instance independently. An instance qualifies only when it both (a) satisfies the
        quality criteria above and (b) its content is traceable to at least one exploration-phase source
        listed in `<exploration_sources>`. The section scores 1 if at least one instance qualifies;
        unqualified instances do not lower the score — only a total absence of qualifying instances
        yields 0. When `<exploration_sources>` says "Not provided" (no exploration sources were gathered),
        condition (b) can never be met, so the section scores 0 regardless of content quality. When
        `<exploration_sources>` contains a list of sources, verify traceability for each instance
        individually — an instance without a matching exploration source does not qualify, but other
        instances in the same section may still do so.
      - **Count every qualifying instance and classify each one's quality tier — do not stop at the first.**
        A "distinct instance" is a separate addition (typically its own sentence or paragraph, often under a
        different subheading) rather than a second sentence elaborating on the same single point. Classify
        each qualifying instance as:
        • **strong** — a substantive, specific addition: concrete metrics/data, a named study/algorithm/limitation,
          a quantified trade-off, or a detailed mechanism explanation that meaningfully deepens understanding
          beyond a passing mention.
        • **standard** — a valid, source-attributed addition that clears the quality bar above but is comparatively
          brief, generic, or a single-sentence mention without much elaboration.
   5. **BreadthEnhancement:** Evaluate whether the section contains valuable additions that expand outward to areas adjacent
      to the core topic.
      - **Breadth additions** (outward — connect to adjacent areas outside the core topic) include one or more of the following:
        • adjacent or related concepts that expand the scope without straying from the core theme
        • cross-domain analogies or lessons from other fields
        • historical context or evolution of the topic
        • enabling/disrupting technologies that intersect with the core topic
        • practical applications of the core topic in other industries or domains beyond the section's primary scope
        • emerging trends in adjacent fields or the broader ecosystem surrounding the topic
      - The addition must be relevant to the main topic/theme of the ground truth section and must not contradict any ground
        truth facts.
      - Score 1 if at least one breadth element passes both the quality check and the source attribution gate below.
      - Score 0 if no breadth element passes both checks — whether because no enhancements are present,
        all are shallow/superficial/off-topic/irrelevant, or none can be traced to an exploration source.
      - **Source attribution gate — always active, evaluated per instance:** Assess each candidate breadth
        enhancement instance independently. An instance qualifies only when it both (a) satisfies the
        quality criteria above and (b) its content is traceable to at least one exploration-phase source
        listed in `<exploration_sources>`. The section scores 1 if at least one instance qualifies;
        unqualified instances do not lower the score — only a total absence of qualifying instances
        yields 0. When `<exploration_sources>` says "Not provided" (no exploration sources were gathered),
        condition (b) can never be met, so the section scores 0 regardless of content quality. When
        `<exploration_sources>` contains a list of sources, verify traceability for each instance
        individually — an instance without a matching exploration source does not qualify, but other
        instances in the same section may still do so.
      - **Count every qualifying instance and classify each one's quality tier — do not stop at the first.**
        Use the same "distinct instance" definition and **strong**/**standard** quality rubric as DepthEnhancement
        above (a separate addition, not a second sentence on the same point; strong = substantive/specific/
        quantified/named; standard = valid but brief or generic).
10. Along with the binary scores, you will provide a brief and concise explanation containing the reasoning behind 
the score for each criterion. The score will be used to debug and monitor the evaluation process. Therefore, it is
important to provide thorough reasoning for the score. Since we provide binary scores, the reasoning should always 
contain what is good and what is problematic about the generated section, regardless of the score. For example, if the 
score is 0, the reasoning should also contain what is good about the generated section, such as "both sections 
follow the same flow of ideas," and what is problematic, such as "the generated section contains an additional 
paragraph on AI Evals that is not present in the expected section." When scoring depth_enhancement and breadth_enhancement,
for each criterion name the specific bullet(s) from the respective list that were present or absent, and briefly explain
why the addition qualifies or does not qualify. The reason field for depth_enhancement and breadth_enhancement must always 
address the source attribution gate on a per-instance basis: when `<exploration_sources>` says "Not provided", explicitly state that no
exploration sources were gathered and therefore the score is 0. When `<exploration_sources>` contains a
list of sources, evaluate each candidate instance and state whether it qualifies (citing the matching URL,
e.g. "Instance traces to https://arxiv.org/abs/2310.09298 — empirical JSON error-rate study") or does not
(stating no matching source was found). If at least one instance qualifies, the score is 1; if none
qualify, the score is 0.
   **Mandatory structured tag for depth_enhancement and breadth_enhancement only:** immediately after the
   `**{{score}}:**` marker and before the prose explanation, insert a bracketed tag reporting every qualifying
   instance found and its quality tier, in this exact format:
   `[instances=N; quality=tier1,tier2,...]` — where N is the **true total count** of qualifying instances (do not
   artificially cap it; report the real number even if it is large), and the quality list gives the **strong**/
   **standard** tier for up to the first 5 instances, **ordered strongest-first (all "strong" entries before any
   "standard" entries)**, not in the order they were discussed in the prose. This matters when N > 5: only the
   first 5 listed tiers are ever used downstream, so if a strong instance is not among the first 5 in the list,
   its value is lost — always rank strong before standard so no genuinely stronger instance is dropped in favor
   of a weaker one that merely happened to be discussed earlier. When N = 0, the tag is simply `[instances=0]`
   with no quality list. This tag is required on every depth_enhancement/breadth_enhancement entry regardless of
   score, including score-0 entries (which are always `[instances=0]`).
   *Examples:* a section with one strong depth addition and no others: `**1:** [instances=1; quality=strong] ...`.
   A section with three qualifying breadth additions — two strong, one standard — found while continuing to
   evaluate every candidate rather than stopping at the first: `**1:** [instances=3; quality=strong,strong,standard] ...`.
   A section with seven qualifying depth additions (four strong, three standard): list the four strong tiers
   first, then only enough standard tiers to fill the 5-slot list: `**1:** [instances=7; quality=strong,strong,strong,strong,standard] ...`.
   A section with no qualifying depth additions: `**0:** [instances=0] ...`.
11. Important rules when comparing the content of sections:
      - Focus on substance, not superficial formatting differences
      - When comparing **media**, you only care about the placement of the media, not the content of the media. 
      Since media can take many forms such as Mermaid diagrams, tables, images, or URLs, you will completely ignore the 
      content of the media and only check whether the media is present in the correct place in the section, has 
      the appropriate citation, and proper numbering.
      - **Mermaid diagrams are equivalent to static images.** A Mermaid diagram block (` ```mermaid ... ``` `) in
      the generated section is a valid substitute for a static image reference (`![Figure N](url)`) in the expected
      section at the same position. Never treat a Mermaid diagram as a "missing figure" — it is a present visual
      element. A media element is missing only when no visual of any kind (no static image, no Mermaid diagram, no table,
      no other media form) appears where the expected section places one.

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
2.3. **Pre-evaluation section mapping (do this BEFORE any criterion evaluation):** For each section in the
expected output, locate its counterpart in the generated output using the two-pass search from instruction 5
(title match first, then content match). Record the mapping for every expected section (MAPPED or MISSING).
Commit to this mapping for all subsequent criterion evaluations — do not re-evaluate section presence separately
for each criterion.
2.4. When computing the score for an individual section, iterate through each mapped expected section, use
its pre-resolved generated counterpart, and compute all five criteria in complete isolation from all other sections.

**Assigning Scores to Each Section:**
3.1. For each section and criterion, write your reasoning first: explain what matches, what differs,
and what conclusion you reach. Do NOT write the score yet.
If a required section is missing from the generated output, state that explicitly and conclude 0 for all five criteria.
**For Flow specifically:** before concluding that a reordering or a large addition is a failure, locate the
"## Flow Precision Tests" section (search for that exact heading) and apply Test 1 (reordering coherence) and
Test 2 (three-way crowding boundary) — do not conclude Flow=0 from a bare "different order" or "long addition"
observation alone.
3.2. Based solely on the conclusion you stated in 3.1, derive the binary score:
   - Score **1** if your reasoning concluded the section satisfies the criterion.
   - Score **0** if your reasoning concluded the section violates or fails the criterion.
   The score must be the mechanical output of your stated conclusion — not a separate judgment.
3.3. **[Mandatory self-check]** After assigning all scores, for each section-criterion pair, read
your 3.1 reasoning and your 3.2 score together. Verify: does the score match the conclusion you
wrote? If you wrote that the section preserves flow / contains all ideas / has no structural issues
but scored 0, correct to 1. If you wrote that something is missing or violated but scored 1,
correct to 0. Never leave a score that contradicts your own written conclusion.
3.4. **[Always mandatory]** For every candidate depth/breadth addition in a section, work through this checklist
before it counts toward either score. **Before starting, locate the "## Depth/Breadth Precision Tests" section
(search for that exact heading) — steps (a)/(b)/(c) below are one-line summaries; the full rules and worked
examples live there as Test 1, Test 2, and Test 3 respectively:**
   a. **Dual / depth-only / breadth-only** (Test 1) — apply the dual-qualification test: does it deepen THIS section's own
      mechanism, explain a genuinely distinct outside mechanism, or both (only when the outside mechanism is used
      to illuminate/contrast/connect back to this section's own mechanism)?
   b. **Instance boundary** (Test 2) — apply the clustering test against every other candidate already identified in this
      section: merge only if it answers the same underlying question as one already counted; otherwise keep separate,
      even if it shares a source, paragraph, or lead-in sentence with another candidate.
   c. **Quality floor** (Test 3) — apply the too-shallow-to-count test: exclude entirely (not as "standard") any candidate
      that only rephrases its source's own generic summary without adding a checkable fact, name, number, or mechanism.
   d. **Source attribution** — if `<exploration_sources>` says "Not provided", revise
      depth_enhancement/breadth_enhancement to 0 immediately for the whole section — no instance can ever be traced
      when no exploration sources exist. Otherwise, evaluate each surviving candidate's traceability: it qualifies
      when its content is consistent with at least one listed source.
   Only candidates surviving all four checks count as qualifying instances. Keep the score at 1 as long as at least
   one instance qualifies across the whole section; score 0 only when none do.
3.5. **[Always mandatory]** For every depth_enhancement and breadth_enhancement entry (score 0 or 1),
finalize the `[instances=N; quality=...]` tag required by instruction 10: count every instance that
survived the 3.4 checklist (not just the first), classify each as strong/standard per the
rubric in criteria 4/5, order the quality list strongest-first (all "strong" before any "standard",
per instruction 10), and place the tag immediately after the score marker. A score-0 entry is always
`[instances=0]`; a score-1 entry always has N ≥ 1 with a matching quality list. Also name, in the reasoning
prose, any candidate excluded at steps 3.4(b)/(c) and why — merged or too-shallow exclusions must be
auditable, never silent.

## WHAT TO AVOID

- Do not provide scores using the generated output as the reference point to divide into sections. You must always 
use the expected output as the reference point to divide into sections.
- Do not let other sections influence the score of a section. The score and reasoning for each section must be
based SOLELY on the content of that specific section in both the expected and generated outputs. Never cite the
absence or presence of a different section as evidence when scoring a given section. For example, if section
"Practical Example" is missing, that cannot be cited as a reason to lower the score of section "Key Strategies".
Each section must stand entirely on its own.
- Do not overlap requirements between different criteria. CoreContent and Flow are complementary but non-overlapping: CoreContent
asks whether all expected ideas are present with the correct topical identity, while Flow asks whether the ideas that are present
follow the expected order with smooth transitions. A missing idea scores CoreContent=0 but must not independently cause Flow=0
for the same absence — Flow=0 only when the ordering, transitions, or media placement are wrong. Conversely,
ideas in a different order or with missing transitions score Flow=0 but must not affect the CoreContent score.
Similarly, a strong depth or breadth addition must not affect the core_preservation score unless it actually
dilutes the core. A non-qualifying addition that scores 0 on both depth_enhancement and breadth_enhancement
must not trigger CorePreservation=0 — CorePreservation only evaluates qualifying depth or breadth additions.
**A large non-qualifying addition is never scored by a length/proportion calculation.** Resolve it via Test 2
("Three-Way Crowding Boundary") in the "## Flow Precision Tests" section: an idea buried to unrecognizability is
CoreContent=0; an idea that's present but the addition disrupts the surrounding narrative is Flow=0; sheer length
with nothing missing and nothing disrupted is neither.
- **Media absence is a Flow failure, never a CoreContent failure.** Never assign CoreContent=0 because an image,
diagram, or mermaid block is absent. The presence or absence of visual media belongs exclusively to the Flow
criterion (media placement). A generated section that covers all expected ideas textually but omits an expected
figure is: CoreContent=1, Flow=0. Cite "missing image" or "missing diagram" only in Flow reasoning, never in
CoreContent reasoning.
- **Do not cascade CoreContent failures into other criteria.** A section scoring CoreContent=0 does not
automatically lower Flow, Structure, or CorePreservation. Each criterion is evaluated independently. In
particular, CorePreservation is never affected by CoreContent — if depth_enhancement=0 and breadth_enhancement=0
for a section, CorePreservation=1 by default regardless of the CoreContent score.
- **Your score must be consistent with your reasoning.** Before finalizing a score for a section and criterion,
re-read your reasoning for that entry. If your reasoning concludes that requirements are satisfied or no failure
exists, you MUST assign score **1**. If your reasoning concludes that a requirement is violated or a key element
is missing, you MUST assign score **0**. A score that contradicts the explicit conclusion of your own reasoning
is always a fatal error. Never write that an idea is present and then score 0; never write that flow is
preserved and then score 0; never conclude compliance and assign 0. The score reflects your conclusion.

## Depth/Breadth Precision Tests

Apply these three tests, in order, to every candidate depth/breadth addition before it counts as a qualifying
instance for DepthEnhancement or BreadthEnhancement. Each example below states the article context first, then
the exact passage, then the verdict — read the context before the quote, since whether a passage is even an
"addition" (as opposed to something the expected section already covers) depends on it.

### Test 1: Dual-Qualification Test

**Rule:** Depth and breadth test different things about what a passage explains, not "how deep" vs. "how wide"
readings of the same content. A passage explains either (i) the section's OWN core mechanism, or (ii) a genuinely
distinct field, model, method, or tradition not otherwise used in this section. Score **depth** only for (i) —
elaborating, requantifying, or further testing the section's own mechanism, even via an extended explanation.
Score **breadth** for (ii) — naming and explaining a genuinely distinct adjacent mechanism, even briefly. An
addition qualifies for **both** (dual) only when explaining the distinct outside mechanism (ii) is explicitly
used to illuminate, contrast with, or connect back to the section's own mechanism (i) — not merely mentioned
side-by-side with it.

**Example — breadth-only, not dual:**
- *Context:* a lesson article on implementing structured outputs. One section teaches building a JSON schema
  manually and injecting it into a prompt; a later, separate section teaches the Gemini API's own native
  structured-output feature.
- *Passage, in the manual-schema section:* "...This is similar to the technique used internally by APIs like
  Gemini and OpenAI to enforce a specific output format. This enforcement often relies on grammar-based decoding,
  which constrains the model's token generation to ensure the output is syntactically correct and adheres to the
  schema."
- *Verdict:* **breadth-only** here. Grammar-based decoding is a genuinely distinct method, correctly named — but
  this section's own mechanism (manual schema generation + prompt injection) is not what's being explained, so no
  depth credit.
- *Contrast — the identical concept, depth instead:* the Gemini section later says "...This is often done through
  grammar-based decoding, where the API restricts the model to only generate tokens that conform to the provided
  schema, offering a mathematical guarantee of a valid output structure." Same mechanism, but here it IS the tool
  this section teaches, so this instance is **depth**, not breadth.

**Example — dual:**
- *Context:* a popular-science article on the "dark dimension" cosmology proposal, which explains gravity's
  weakness via one extra micron-scale spatial dimension.
- *Passage:* "...This idea is related to a broader class of 'braneworld' cosmology models, where our
  four-dimensional universe is a membrane, or 'brane,' existing within a higher-dimensional space. In these
  scenarios, the presence of extra dimensions can modify gravitational interactions on large scales, potentially
  explaining the observed acceleration of the universe without a traditional dark energy component. The dark
  dimension proposal extends these concepts by linking the size of a specific extra dimension directly to the
  observed dark energy density, providing a mechanism for how a 4D cosmology can emerge from a higher-dimensional
  setup."
- *Verdict:* **dual** — names a genuinely distinct framework (braneworld models) AND explicitly uses it to
  illuminate the section's own mechanism (contrasting/connecting braneworld's gravity modification to the
  dark-dimension proposal's own). Score both depth and breadth from this one instance.

### Test 2: Instance-Boundary (Clustering) Test

**Rule:** Merge two candidate passages into a single instance only when the second is substantively restating,
rephrasing, or lightly qualifying the SAME underlying claim as the first — i.e., they answer the same question.
Keep them as separate instances whenever they answer genuinely different questions, even if they share a source,
sit in the same paragraph, or are introduced by one common lead-in sentence. Proximity, shared sourcing, and a
shared organizational lead-in are never, by themselves, sufficient reasons to merge.

**Example — merge:**
- *Context:* the same dark-dimension article, discussing a 2025 paper's consistency check against observational
  data.
- *Passage:* "...found this scenario was consistent with DESI data, including higher-order checks against its
  Lyman-alpha forest measurements combined with cosmic microwave background observations."
- *Verdict:* **one instance.** The Lyman-alpha clause qualifies the same DESI-consistency claim within the same
  sentence; it is not a distinct claim.

**Example — keep separate, despite a shared lead-in and adjacency:**
- *Context:* the same article, describing ongoing experimental tests of the theory.
- *Passage:* "Other tests are also being pursued. Physicists are looking for deviations from gravity at the micron
  scale, with experiments at the University of Washington and in Austria pushing the limits of measurement.
  Furthermore, primordial fluctuations could generate a stochastic background of gravitational waves, and a dark
  dimension could modify their signals in ways detectable by future observatories."
- *Verdict:* **two instances.** Both sentences share one lead-in and sit back-to-back, but one answers "how do we
  test this in the lab" and the other "how would this show up in gravitational-wave data" — genuinely different
  detection channels.

**Example — keep separate, despite one umbrella framing sentence:**
- *Context:* a lesson article's pros/cons table comparing the ReAct agent pattern's strengths and weaknesses.
- *Passage:* the table lists, among its rows, "**Grounded Reasoning:** By incorporating external observations,
  ReAct reduces the risk of hallucination compared to pure CoT reasoning" (a pro) alongside a cluster of distinct
  failure-mode cons ("Long-Horizon Drift," "Brittle Error Recovery," "No Consequence Awareness," "Thought-Action
  Divergence").
- *Verdict:* **keep all separate.** Despite sharing one table and one introductory framing sentence, the pro
  answers "why does this approach work" and each con answers a distinct "how does this approach fail" question —
  different underlying questions, not the same claim from two angles. Do not merge the pro into the cons cluster,
  or the distinct cons into each other.

### Test 3: Quality Floor

**Rule:** Below "standard" is a third, unlabeled tier: **too-shallow-to-count**. An addition belongs here —
excluded entirely from `[instances=N]`, not counted as "standard" — when it is essentially a rephrasing of its
cited source's own generic summary sentence, contributing no fact, name, number, mechanism, or nuance beyond what
the surrounding text already conveys. Test: *would a reader who skipped this sentence have missed any concrete,
checkable content?* If no, exclude it. A competent paraphrase can still read as fluent, specific-sounding prose
while adding zero real content — do not let fluency alone clear the floor.

**Example — too-shallow-to-count:**
- *Context:* the same dark-dimension article, closing with a forward-looking statement about future tests.
- *Cited source says:* "Future experimental tests at the interface of cosmology, particle physics, and
  gravitational phenomenology are poised to probe core predictions."
- *Generated text says:* "Future tests at the intersection of cosmology, particle physics, and gravitational wave
  astronomy are also poised to probe the theory's core predictions."
- *Verdict:* **excluded.** Swap a few words and it's the source's own meta-summary line with the serial numbers
  filed off — no named experiment, technique, or fact is added, regardless of citation validity.

**Reporting requirement:** always name excluded shallow candidates in the reasoning prose (not the `[instances=N]`
tag) — state what was found and why it didn't clear the floor, so the exclusion is auditable rather than silent.

## Flow Precision Tests

Apply these two tests whenever a candidate Flow failure involves reordering or a large addition. As with the
Depth/Breadth tests, read each example's context before its passage — the point is judging coherence and
recognizability, not sequence-matching or length.

### Test 1: Reordering Coherence Test

**Rule:** A generated section presenting the expected section's ideas in a different order from the expected
section is NOT automatically a Flow failure. Reordering only fails Flow when the alternate order actually
disrupts the reader's ability to follow the argument — an idea depends on a later idea not yet explained, a
transition no longer makes sense given the new sequence, or the reasoning becomes circular as a result of the
swap. A different-but-complete alternate structuring — one a reader could follow smoothly, with each idea's
prerequisites already established — is not a Flow failure merely because it diverges from the expected section's
chosen order.

**Example — full inversion, still coherent:**
- *Context:* a popular-science article on the dark-dimension proposal. The expected section opens with the
  implication ("if dark energy and dark matter interact, they may share a common origin"), then moves to the
  string-theory framework, the mechanism, and the predictions/tests.
- *Passage:* the generated section instead opens directly with the framework ("The dark dimension proposal
  originates not from cosmology but from fundamental constraints in string theory known as the 'Swampland'
  criteria..."), then the mechanism, then the predictions and tests, and only in its closing sentence states "As
  Obied remarked, if dark energy and dark matter do interact, it could mean they have a common origin."
- *Verdict:* **coherent, not a Flow failure.** This is the entire logical direction reversed — implication-first
  vs. framework-first — not one point nudged out of place, yet it remains a complete, forward-running argument
  (framework → mechanism → predictions → tests → therefore shared origin) traversed in the opposite direction
  from the expected section. This is close to the most dramatic reordering that still passes; use it to calibrate
  how far "coherent" can stretch before it becomes disruptive.

**Example — different reasoning path to the same destination:**
- *Context:* the same article. The expected section's intermediate reasoning is: dark energy varies → dark
  matter mass may also vary → propose a shared dark-dimension link.
- *Passage:* the generated section instead applies the Swampland Distance Conjecture to dark energy's tiny value,
  states this "leads to a surprising prediction," and only in the next paragraph reveals the prediction (a large
  extra spatial dimension must exist) — never explicitly stating the expected section's own intermediate claim
  that dark matter mass may also vary over time.
- *Verdict:* **coherent, not a Flow failure.** The destination and the dependency structure the expected section
  relies on (tiny dark energy value → some consequence follows → shared geometric origin) are both preserved,
  just reached via a more mechanistically explicit, differently-sequenced route.

**Example — small-scale reposition:**
- *Context:* the same article's "Dark Interactions" section, discussing a QCD-inspired dark-sector model by
  Khoury, Lin, and Trodden.
- *Passage:* the generated section moves this point out of its expected position (immediately after the 2005
  Khoury model) and groups it instead with other, thematically related content later in the section.
- *Verdict:* **coherent, not a Flow failure.** Shows the same test applies whether the reordering is one
  paragraph or the whole section's argument direction — small repositioning for thematic grouping is not
  disruptive.

**Known gap in this few-shot set:** every reordering instance examined for this article, once the coherence test
above was applied properly, turned out to pass. There is currently no verified real example of a reordering that
correctly fails this test. Treat the rule statement above (prerequisite-before-dependent violations, transitions
that stop making sense, circular reasoning) as the operative definition of a genuine failure until a real negative
example is available — do not assume reordering is effectively always acceptable just because this set has no
counter-example.

### Test 2: Three-Way Crowding Boundary (CoreContent vs. Flow vs. Neither)

**Rule:** When a non-qualifying addition (depth_enhancement=0 AND breadth_enhancement=0) is large relative to the
expected section, resolve "is this a problem, and for which criterion" with this test, never a length/proportion
calculation:
1. If the addition buries an expected idea so completely that a reader would not recognize it as present —
   effectively unstated despite being technically present as text — treat it as missing: this is a
   **CoreContent=0** failure, not Flow.
2. If the expected idea IS recognizable/present, but the addition disrupts the narrative around it — breaking
   transitions, creating confusing jumps, making the argument hard to follow — this is a **Flow=0** failure. This
   is the same family as the bridgeless-gap rule above, just triggered by an insertion instead of an omission.
3. If neither is true — the addition is simply long, every expected idea is still clearly present, and the
   narrative is still easy to follow — this is **neither** a CoreContent nor a Flow failure. Sheer length alone is
   out of scope for this metric.

**Example — CoreContent (idea buried to unrecognizability):**
- *Context:* an article recasting the dark-dimension proposal as an extended metaphor for AI system design. The
  expected section's mechanism is: gravitons carry gravitational force, leak into the extra dimension, acquire
  mass, and their effects are felt in our four dimensions.
- *Passage:* "Here is how the analogy maps to AI engineering. The 'gravitons' are the fundamental units of
  information and reasoning within an LLM's latent space. The 'dark dimension' is a new, explicit architectural
  layer in our AI system... When we design our system, we allow information from the LLM's latent space to
  'leak' into this new layer... becoming 'dark gravitons.'" No sentence anywhere in the section states the actual
  physics mechanism independent of the AI metaphor.
- *Verdict:* **CoreContent=0**, on the reasoning that the underlying physics idea is never actually stated in its
  own right — only translated. This is a genuinely close call: an equally defensible reading could fold this into
  Flow instead (the idea is arguably "present" in heavily paraphrased form, and it is the presentation that
  disrupts recognition rather than the idea being purely absent). Flag this ambiguity explicitly in the reasoning
  rather than resolving it silently either way.

**Example — neither (long, but nothing missing, nothing disrupted):**
- *Context:* the same dark-dimension article, a different generation with ten separate depth-enhancement
  additions across the section.
- *Passage:* the section runs approximately 16% over its word-count target, driven by ten distinct, genuinely
  substantive, source-attributed additions — yet every expected idea remains independently stated (including
  both of the physicist's direct quotes and all required mechanisms), and the section's ideas remain in the same
  relative order as the expected section throughout.
- *Verdict:* **neither** a CoreContent nor a Flow failure. This pairs with the CoreContent example above to show
  the same surface feature ("a lot of extra content") splitting into different outcomes depending on whether
  anything required actually goes missing, gets buried to the point of disruption, or neither — here it is
  neither, and the length itself is out of scope for this metric.

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

<exploration_sources>
{exploration_sources}
</exploration_sources>

Think through your answer step by step, and provide the requested evaluation.
"""

EXAMPLES_DIR = Path(__file__).parent / "examples"

_LESSON_04_EXPLORATION_SOURCES = """\
The following sources were retrieved during the exploration phase (step 4: gap-driven research \
beyond the article guideline scope). Depth and breadth additions score 1 only if the addition's \
content is traceable to one or more of these sources.

- https://increment.com/apis/interoperability-data-exchange-formats/ \u2014 Historical evolution of \
structured data interchange formats from XML (1998) through JSON (2001) and YAML to modern \
schema-validated APIs using Python type annotations and Pydantic
- https://arxiv.org/abs/2310.09298 \u2014 Empirical study of LLM-generated JSON output reliability: \
approximately 12% of outputs from frontier models contain syntax errors including trailing commas, \
invalid comments, and unescaped special characters
- https://docs.pydantic.dev/blog/pydantic-v2-final/ \u2014 Pydantic v2 architectural overhaul: \
Rust-based core-validator achieves 5\u201350x performance improvements over v1 Python implementation; \
key API changes and migration guidance
- https://blog.outlines.ai/constrained-structured-generation \u2014 Grammar-based structured generation \
using context-free grammars; comparison of OpenAI, Anthropic, Cohere, Mistral native structured \
output APIs; Instructor library for schema-constrained LLM extraction
- https://microsoft.github.io/graphrag/overview \u2014 GraphRAG: combining knowledge graph construction \
with vector retrieval for multi-hop reasoning across document collections\
"""

_LESSON_07_EXPLORATION_SOURCES = """\
The following sources were retrieved during the exploration phase (step 4: gap-driven research \
beyond the article guideline scope). Depth and breadth additions score 1 only if the addition's \
content is traceable to one or more of these sources.

- https://en.wikipedia.org/wiki/History_of_artificial_intelligence \u2014 AI planning history: STRIPS \
automated planner (1971, Stanford AI Lab) and SHRDLU natural-language parser (1970, Winograd); \
transition from symbolic AI to connectionist and neural approaches
- https://arxiv.org/abs/2309.15402 \u2014 Multi-step task benchmark: reasoning-augmented agents achieve \
67% success on tasks with more than five sequential steps vs 23% for standard LLMs; near-zero \
error-recovery rates for non-augmented models
- https://arxiv.org/abs/2210.03629 \u2014 ReAct (Yao et al. 2022): HotpotQA and FEVER benchmark results \
showing 8\u201314% accuracy improvements; human preference study rating ReAct reasoning traces 1.4x \
more trustworthy than CoT-only baselines
- https://en.wikipedia.org/wiki/OODA_loop \u2014 OODA loop (Observe-Orient-Decide-Act) decision-making \
cycle developed by military strategist John Boyd in the 1970s; applications in competitive \
strategy, crisis management, and autonomous decision-making
- https://hbr.org/2024/ai-workflow-automation-enterprise \u2014 Case studies of AI plan-and-execute \
workflows applied to healthcare clinical trial management, legal discovery document review, and \
supply chain and logistics optimization
- https://www.finextra.com/newsarticle/ai-regulated-financial-systems \u2014 AI in regulated financial \
environments: MiFID II and SEC Rule 17a-4 compliance; Bloomberg and Reuters data feed integration \
processing 250,000+ updates per second; T+2 settlement via DTCC; Basel III Value-at-Risk using \
Monte Carlo simulations\
"""

DEFAULT_FEW_SHOT_EXAMPLES = FollowsGTMetricFewShotExamples(
    examples=[
        # ── Lesson 4: Structured Outputs ────────────────────────────
        FollowsGTMetricExample.from_markdown(
            output_file=EXAMPLES_DIR / "04_structured_outputs" / "article_generated.md",
            expected_output_file=EXAMPLES_DIR / "04_structured_outputs" / "article_ground_truth.md",
            exploration_sources=_LESSON_04_EXPLORATION_SOURCES,
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
                                    "[instances=0] No depth additions present. The historical evolution paragraph provides "
                                    "external narrative context rather than intensifying understanding of "
                                    "structured outputs' inner workings — no theoretical foundations, technical "
                                    "nuances, limitations, or real-world case studies about structured outputs "
                                    "are present."
                                ),
                            ),
                            breadth_enhancement=CriterionScore(
                                score=1,
                                reason=(
                                    "[instances=1; quality=standard] A breadth addition is present: the generated "
                                    "section includes a paragraph tracing the evolution of structured data formats "
                                    "from XML in the late 1990s "
                                    "through JSON and YAML to the current Pydantic era, qualifying as 'historical "
                                    "context or evolution of the topic' and meaningfully integrated into the "
                                    "narrative about why structured outputs matter for LLMs."
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
                                    "benefits, discussing use cases, and concluding with a diagram. Stepping over "
                                    "the off-topic GraphRAG addition, the GT ideas — importance, benefits, use "
                                    "cases, diagram, and closing transition — are still evaluated in sequence. "
                                    "The section scores 0 because the last transition sentence setting up the "
                                    "three implementation approaches is absent from the generated section, which "
                                    "is a legitimate narrative continuity failure."
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
                                    "[instances=0] No depth additions present. The GraphRAG paragraph does not go deeper into "
                                    "structured outputs — it provides no theoretical foundations, limitations, or "
                                    "implementation challenges related to structured outputs. It is an off-topic "
                                    "addition about a different technology."
                                ),
                            ),
                            breadth_enhancement=CriterionScore(
                                score=0,
                                reason=(
                                    "[instances=0] No breadth additions present. The GraphRAG paragraph does not expand outward "
                                    "to adjacent concepts, cross-domain analogies, or historical context related "
                                    "to structured outputs. It is an off-topic addition about a different "
                                    "technology that does not illuminate structured outputs from the outside."
                                ),
                            ),
                            core_preservation=CriterionScore(
                                score=1,
                                reason=(
                                    "Both depth_enhancement and breadth_enhancement scored 0, meaning no depth "
                                    "or breadth additions were identified. CorePreservation scores 1 by default "
                                    "since there are no qualifying additions to evaluate. The off-topic GraphRAG "
                                    "paragraph is not a qualifying addition, so CorePreservation does not apply "
                                    "to it. Applying the three-way crowding test: every expected idea in this "
                                    "section remains clearly stated and in order despite the addition, so it "
                                    "triggers neither CoreContent=0 nor Flow=0 either -- it is simply an "
                                    "off-topic addition, not a crowding problem."
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
                                    "[instances=1; quality=strong] A depth addition is present: the generated section includes a paragraph "
                                    "about failure modes of manual JSON parsing, noting that LLMs frequently "
                                    "produce trailing commas, invalid comments, and unescaped characters, with "
                                    "concrete data showing ~12%% of LLM-generated JSON outputs contain syntax "
                                    "errors. This qualifies as 'limitations, criticisms, or failure modes of "
                                    "the core topic' and is directly relevant to the section's topic. Classified as "
                                    "strong: a concrete, quantified failure-rate statistic, not just a generic mention."
                                ),
                            ),
                            breadth_enhancement=CriterionScore(
                                score=0,
                                reason=(
                                    "[instances=0] No breadth additions present. The failure modes paragraph stays within the "
                                    "core topic of manual JSON parsing rather than expanding outward — no adjacent "
                                    "concepts, cross-domain analogies, historical context, or applications in "
                                    "other industries are present."
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
                                    "[instances=1; quality=strong] A depth addition is present: the generated section includes a paragraph "
                                    "about Pydantic v2's major architectural overhaul, noting the Rust-based "
                                    "validation core that achieved 5-50x performance improvements. This qualifies "
                                    "as 'latest advancements or recent developments in the core topic itself' and "
                                    "'technical nuances or alternative implementation perspectives', directly "
                                    "relevant to the Pydantic section. Classified as strong: a specific, quantified "
                                    "performance-improvement claim, not just a generic mention of a new version."
                                ),
                            ),
                            breadth_enhancement=CriterionScore(
                                score=0,
                                reason=(
                                    "[instances=0] No breadth additions present. The Pydantic v2 paragraph deepens understanding "
                                    "of Pydantic itself rather than expanding outward — no adjacent concepts, "
                                    "historical context, cross-domain analogies, or applications in other "
                                    "industries are present."
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
                                score=0,
                                reason=(
                                    "The generated section covers the introduction and the first two steps of the "
                                    "code walkthrough, but omits steps 3 and 4 of the numbered implementation "
                                    "walkthrough present in the expected section. These are substantive ideas that "
                                    "are absent from the generated section."
                                ),
                            ),
                            flow=CriterionScore(
                                score=0,
                                reason=(
                                    "Both sections follow a similar logical flow, introducing native API support "
                                    "and then demonstrating its implementation through steps with code. Stepping "
                                    "over the competitor comparison breadth addition, the expected GT sequence is: "
                                    "intro → step 1 → step 2 → step 3 → step 4 → conclusion. However, the "
                                    "generated section misses the opening transition sentence from the previous "
                                    "section, and since steps 3 and 4 are absent, the walkthrough jumps abruptly "
                                    "from step 2 to the conclusion — a narrative continuity failure caused by "
                                    "the bridgeless gap left by the missing steps."
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
                                    "[instances=0] No depth additions present. The provider comparison paragraph expands outward "
                                    "to other tools rather than going deeper into Gemini's structured output "
                                    "implementation — no theoretical foundations, limitations, or concrete metrics "
                                    "about Gemini's own implementation specifically are present."
                                ),
                            ),
                            breadth_enhancement=CriterionScore(
                                score=1,
                                reason=(
                                    "[instances=1; quality=strong] A breadth addition is present: the generated "
                                    "section includes an extensive paragraph comparing how other providers "
                                    "(OpenAI, Anthropic, Cohere, Mistral, "
                                    "and open-source tools like Outlines and Instructor) implement structured "
                                    "outputs, including constrained decoding and grammar-based generation with "
                                    "CFGs. This qualifies as 'adjacent or related concepts that expand the scope "
                                    "without straying from the core theme' and 'enabling/disrupting technologies "
                                    "that intersect with the core topic'. Classified as one strong, comprehensive "
                                    "instance covering several named alternatives rather than a brief mention."
                                ),
                            ),
                            core_preservation=CriterionScore(
                                score=0,
                                reason=(
                                    "core_content=0 and flow=0 for this section are not themselves the reason for "
                                    "this score (a missing/misordered idea never justifies core_preservation=0 on "
                                    "its own) -- but the qualifying breadth addition itself causes a "
                                    "topical-identity shift: a reader asked to summarize this section in one "
                                    "sentence would describe it as a survey of how competing providers (OpenAI, "
                                    "Anthropic, Cohere, Mistral) implement structured outputs, not as a hands-on "
                                    "walkthrough of Gemini's native capability, which is the ground truth's actual "
                                    "subject. The competitor survey has effectively become what the section is "
                                    "about, displacing rather than supporting the Gemini-specific narrative it was "
                                    "meant to enrich."
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
                                    "[instances=0] No depth additions present. The section is a brief conclusion without any "
                                    "theoretical foundations, technical nuances, real-world case studies, or "
                                    "other qualifying depth elements."
                                ),
                            ),
                            breadth_enhancement=CriterionScore(
                                score=0,
                                reason=(
                                    "[instances=0] No breadth additions present. The section is a brief conclusion without any "
                                    "adjacent concepts, cross-domain analogies, historical context, or "
                                    "applications in other industries."
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
                                    "The ## References section is excluded from structure evaluation. "
                                    "Reference entry format differences never count as a structure failure."
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
            exploration_sources=_LESSON_07_EXPLORATION_SOURCES,
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
                                    "[instances=0] No depth additions present. The historical roots paragraph provides external "
                                    "narrative context rather than intensifying understanding of current LLM "
                                    "planning mechanisms — no theoretical foundations, technical nuances, or "
                                    "real-world case studies about planning and reasoning in LLMs are present."
                                ),
                            ),
                            breadth_enhancement=CriterionScore(
                                score=1,
                                reason=(
                                    "[instances=1; quality=standard] A breadth addition is present: the generated "
                                    "section includes a paragraph about the historical roots of AI planning, "
                                    "tracing it from early symbolic AI "
                                    "systems like STRIPS (1971) and SHRDLU (1970) to the current LLM-based neural "
                                    "paradigm. This qualifies as 'historical context or evolution of the topic' "
                                    "and is meaningfully integrated into the introduction's argument about why "
                                    "planning matters."
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
                                    "Stepping over the benchmark data depth addition, the GT ideas — introducing "
                                    "the research assistant example, explaining the failure, and discussing the "
                                    "need for reasoning — follow the expected relative sequence with smooth "
                                    "transitions. The benchmark data paragraph has its own lead-in connecting "
                                    "it naturally to the surrounding failure analysis, and does not disrupt the "
                                    "GT idea ordering."
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
                                    "[instances=1; quality=strong] A depth addition is present: the generated section includes concrete "
                                    "benchmark data showing that non-reasoning models achieve only 23%% success "
                                    "rate on tasks with more than five sequential steps vs 67%% for "
                                    "reasoning-augmented agents, with near-zero recovery rates on error recovery "
                                    "tasks. This qualifies as 'real-world case studies or concrete metrics about "
                                    "the core topic's performance, behavior, or direct application' and is "
                                    "directly relevant to the section's argument about non-reasoning model failures. "
                                    "Classified as strong: specific, quantified benchmark figures, not a vague claim."
                                ),
                            ),
                            breadth_enhancement=CriterionScore(
                                score=0,
                                reason=(
                                    "[instances=0] No breadth additions present. The benchmark data reinforces the core "
                                    "argument about non-reasoning model failures rather than expanding outward — "
                                    "no adjacent concepts, historical context, or cross-domain analogies present."
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
                                    "Retrieval-Augmented Generation (RAG). As a result, the expected section's "
                                    "core content — CoT's practical limitations, the single-pass problem, and the "
                                    "need for separating thinking from acting — is entirely absent from the "
                                    "generated section."
                                ),
                            ),
                            flow=CriterionScore(
                                score=0,
                                reason=(
                                    "Both sections start by introducing CoT, but the generated section then "
                                    "transitions to RAG rather than following the expected order of ideas. After "
                                    "the CoT introduction, the expected section proceeds to limitations, a "
                                    "diagram, a Note callout, and the separation-of-concerns argument; the "
                                    "generated section instead departs to RAG with no transition toward those "
                                    "expected subsequent ideas. The diagram and Note callout also constitute a "
                                    "media placement failure."
                                ),
                            ),
                            structure=CriterionScore(
                                score=0,
                                reason=(
                                    "The generated section uses the same citation strategy and number formatting. "
                                    "Stepping over the off-topic RAG addition, the GT ideas use the expected "
                                    "paragraph length patterns, so the longer total length is not a structure "
                                    "failure. The missing diagram is also valid for this criterion — missing "
                                    "elements cannot be evaluated for formatting. However, the 'Note' callout "
                                    "box present in the expected section is absent from the generated section, "
                                    "which is a missing layout element and a legitimate structure failure."
                                ),
                            ),
                            depth_enhancement=CriterionScore(
                                score=0,
                                reason=(
                                    "[instances=0] No depth additions present. The RAG paragraphs contain technical detail "
                                    "(embedding models, NDCG scores, hallucination rates) but none qualifies as "
                                    "depth enrichment for CoT — the content is about a completely different "
                                    "technology and does not deepen understanding of CoT's workings or limitations."
                                ),
                            ),
                            breadth_enhancement=CriterionScore(
                                score=0,
                                reason=(
                                    "[instances=0] No breadth additions present. The RAG content does not expand outward from "
                                    "CoT to adjacent concepts — it is an entirely off-topic diversion rather than "
                                    "a related concept, cross-domain analogy, or historical context connected to "
                                    "CoT prompting."
                                ),
                            ),
                            core_preservation=CriterionScore(
                                score=1,
                                reason=(
                                    "Both depth_enhancement and breadth_enhancement scored 0, meaning no depth "
                                    "or breadth additions were identified in this section. Since there are no "
                                    "depth or breadth additions to evaluate, the ground truth core is preserved "
                                    "by default. The off-topic RAG diversion is already penalized by the "
                                    "Flow and CoreContent criteria."
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
                                    "[instances=0] No depth additions present. The generated section describes benefits of the "
                                    "separation (control, iterative loops, different handling of outputs) but "
                                    "these are the same points covered in the ground truth, not additional depth "
                                    "enrichment — no theoretical foundations, concrete metrics, or implementation "
                                    "challenges beyond the ground truth are present."
                                ),
                            ),
                            breadth_enhancement=CriterionScore(
                                score=0,
                                reason=(
                                    "[instances=0] No breadth additions present. No adjacent concepts, historical context, or "
                                    "cross-domain analogies are added beyond what is already in the ground truth."
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
                                    "[instances=1; quality=strong] A depth addition is present: the generated section includes specific "
                                    "benchmark data from the ReAct paper, noting 8-14%% accuracy improvements "
                                    "on HotpotQA and FEVER benchmarks, and that humans rated ReAct's reasoning "
                                    "traces as 1.4x more trustworthy than CoT-only baselines. This qualifies as "
                                    "'real-world case studies or concrete metrics about the core topic's "
                                    "performance, behavior, or direct application'. Classified as strong: named "
                                    "benchmarks with quantified results, not a generic claim."
                                ),
                            ),
                            breadth_enhancement=CriterionScore(
                                score=1,
                                reason=(
                                    "[instances=1; quality=strong] A breadth addition is present: the generated "
                                    "section draws a cross-domain analogy between ReAct's Thought-Action-Observation "
                                    "loop and the OODA loop "
                                    "(Observe-Orient-Decide-Act) from military strategy, developed by John Boyd "
                                    "in the 1970s. This qualifies as 'cross-domain analogies or lessons from "
                                    "other fields' and meaningfully illuminates the ReAct loop from an external "
                                    "perspective. Classified as strong: a specific, well-attributed named framework, "
                                    "not a vague comparison."
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
                                    "[instances=0] No depth additions present. The industry applications paragraph expands "
                                    "outward to other domains rather than deepening understanding of the "
                                    "Plan-and-Execute pattern itself — no theoretical foundations, concrete "
                                    "metrics, or implementation challenges beyond the ground truth are present."
                                ),
                            ),
                            breadth_enhancement=CriterionScore(
                                score=1,
                                reason=(
                                    "[instances=1; quality=strong] A breadth addition is present: the generated "
                                    "section includes a paragraph about practical applications of Plan-and-Execute in diverse industries: "
                                    "healthcare clinical trial management, legal discovery document review, and "
                                    "supply chain optimization. This qualifies as 'practical applications of the "
                                    "core topic in other industries or domains beyond the section's primary scope' "
                                    "and meaningfully expands the reader's understanding of where this pattern applies. "
                                    "Classified as strong: three specific, named industry applications in one addition."
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
                                    "[instances=1; quality=strong] A depth addition is present: the generated "
                                    "section includes an extensive paragraph about financial sector-specific "
                                    "implementation constraints: MiFID II "
                                    "and SEC Rule 17a-4 regulatory requirements, Bloomberg/Reuters data feed "
                                    "integration processing 250,000+ updates/second, T+2 settlement lifecycles via "
                                    "DTCC, and Basel III VaR computations using Monte Carlo simulations. This "
                                    "qualifies as 'implementation challenges, latency/scale trade-offs, or "
                                    "engineering realities' and 'real-world case studies or concrete metrics about "
                                    "the core topic's performance, behavior, or direct application'. Classified as "
                                    "strong: multiple named, quantified regulatory/technical facts bundled into one "
                                    "rich addition."
                                ),
                            ),
                            breadth_enhancement=CriterionScore(
                                score=0,
                                reason=(
                                    "[instances=0] No breadth additions present. The financial implementation details deepen "
                                    "the core topic rather than expanding outward — they do not introduce adjacent "
                                    "concepts, cross-domain analogies, or historical context beyond the section's "
                                    "subject matter."
                                ),
                            ),
                            core_preservation=CriterionScore(
                                score=0,
                                reason=(
                                    "The qualifying depth addition causes a topical-identity shift: the ground "
                                    "truth's core_content is about how the theoretical patterns (ReAct and "
                                    "Plan-and-Execute) power real-world deep research systems, with the patterns "
                                    "themselves as the subject. A reader summarizing this section in one sentence "
                                    "would instead describe it as being about financial-sector regulatory and "
                                    "engineering constraints (MiFID II/SEC compliance, settlement lifecycles, VaR "
                                    "computations) -- the financial detail has become the section's de facto "
                                    "subject rather than illustrating the patterns' application to it."
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
                                    "[instances=0] No depth additions present. The tangential sentence about 'greatest human "
                                    "leaders' contains no theoretical foundations, technical nuances, or concrete "
                                    "metrics that would deepen understanding of the core topic."
                                ),
                            ),
                            breadth_enhancement=CriterionScore(
                                score=0,
                                reason=(
                                    "[instances=0] No breadth additions present. The tangential sentence superficially resembles "
                                    "a cross-domain analogy but is too vague and lacking in substance or "
                                    "specificity to qualify as a meaningful breadth addition."
                                ),
                            ),
                            core_preservation=CriterionScore(
                                score=1,
                                reason=(
                                    "Both depth_enhancement and breadth_enhancement scored 0, meaning no depth "
                                    "or breadth additions were identified in this section. Since there are no "
                                    "depth or breadth additions to evaluate, the ground truth core is preserved "
                                    "by default."
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
                                score=1,
                                reason=(
                                    "The ## References section is excluded from structure evaluation. "
                                    "Reference entry format differences never count as a structure failure."
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
    exploration_sources: str | None = None,
) -> str:
    """Generate the first-pass evaluation prompt for the FollowsGT metric.

    Evaluates five independent criteria (core_content, flow, structure,
    depth_enhancement, breadth_enhancement). CorePreservation is excluded from
    this prompt and evaluated separately via get_core_preservation_prompt.

    Args:
        output: The generated article content to be evaluated.
        expected_output: The expected article content for comparison.
        few_shot_examples: An instance of FollowsGTMetricFewShotExamples containing examples
         to guide the language model's evaluation.
        exploration_sources: Optional formatted string listing the exploration-phase sources
            for this episode. When provided, the judge applies source-attribution checks for
            DepthEnhancement and BreadthEnhancement. When None, falls back to standard
            criteria (backward compatible).

    Returns:
        The complete formatted prompt string ready for the first LLM call.
    """
    _exploration_sources = (
        exploration_sources
        if exploration_sources
        else (
            "Not provided. No exploration-phase sources were gathered for this episode, so the source "
            "attribution gate can never be satisfied: score depth_enhancement and breadth_enhancement as "
            "0 for every section regardless of content quality. Do not apply standard (non-gated) criteria."
        )
    )
    return SYSTEM_PROMPT.format(
        examples=few_shot_examples.to_context(),
        output=output,
        expected_output=expected_output,
        exploration_sources=_exploration_sources,
    )


# ── Second-pass prompt for CorePreservation ──────────────────────────────────

CORE_PRESERVATION_PROMPT = """You are an expert in NLP evaluation metrics.

## Task

You are evaluating the **CorePreservation** criterion for each section of a generated article.

You have access to:
1. The generated article and the expected (ground-truth) article.
2. The **already-determined** `core_content`, `flow`, `depth_enhancement`, and `breadth_enhancement` scores
   for each section, produced by a prior evaluation pass.

Your sole task is to evaluate `core_preservation` for each section by building on those scores.

## CorePreservation Definition

CorePreservation evaluates whether the depth or breadth additions **already identified** in the
prior pass preserve the ground truth core. This criterion applies exclusively to content that was
identified as a depth or breadth addition in those scores — it does not evaluate any other
additions present in the generated section (those are handled by the Flow criterion).

- **Mandatory default rule:** If both `depth_enhancement` AND `breadth_enhancement` scored **0** for
  a section, there are no exploration additions to evaluate; assign a score of **1** by default.
- **CorePreservation is NOT a measure of addition length, density, or proportion.** Do not compute or
  cite word counts, percentages, or relative lengths as justification for any score — that style of
  reasoning is explicitly wrong for this criterion, even for a borderline call.
- **The already-determined `core_content` and `flow` scores are your primary anchor, not a re-litigation
  target:** if `core_content=1` (no expected idea is missing) and `flow`'s scoring is not about a gap
  caused by this addition (i.e. the expected ideas are confirmed present and in a coherent order), that is
  normally sufficient on its own for `core_preservation=1`, regardless of how much surrounding material the
  addition adds. Do not layer a separate density judgment on top of an already-confirmed intact core.
- **Reserve `core_preservation=0` for a narrower, qualitative failure: a topical-identity shift.** This is
  the case where, despite the expected ideas remaining technically present and ordered, the depth/breadth
  addition(s) cause a reader to describe the section's central subject differently than the ground truth's
  — the addition has effectively become what the section is about, not merely additional material alongside
  the core. Ask: *if a reader summarized this section in one sentence, would that summary center on the
  ground-truth topic, or on the added material?* If the ground-truth topic would still anchor the summary,
  score 1 no matter how much surrounding text the addition occupies. If the added material would take over
  the summary, score 0 — but justify it by naming what the section now reads as being about, never by citing
  length, word count, or percentage.
- Anecdotes, motivating examples, or real-world stories identified as depth or breadth additions are
  inherently illustrative and do not by themselves constitute a topical-identity shift, provided they do not
  introduce a competing primary subject that a reader would name instead of the ground truth's.

## Important Rules

- A non-qualifying addition that scores 0 on both `depth_enhancement` and `breadth_enhancement` must
  **never** trigger CorePreservation=0. CorePreservation only evaluates qualifying depth or breadth
  additions. A large non-qualifying addition is resolved by the pass-1 grader's three-way test (CoreContent vs.
  Flow vs. neither, per "## Flow Precision Tests" Test 2), never by CorePreservation.
- **CoreContent absence must never, by itself, justify CorePreservation=0.** A missing expected idea is a
  distinct failure already captured by CoreContent; do not double-penalize it here. Used correctly,
  `core_content`/`flow` only ever push CorePreservation TOWARD 1 (as the anchor described above) — they are
  never cited as the reason for a 0. If `depth_enhancement=0` AND `breadth_enhancement=0` for a section, the
  mandatory default rule applies: CorePreservation=1, regardless of the core_content score.
- Evaluate each section independently of all other sections.

## FEW-SHOT EXAMPLES

Here are few-shot examples demonstrating correct CorePreservation evaluation. Each example shows
the already-determined core_content/flow/depth/breadth scores, the articles, and the expected
CorePreservation judgment:
<few-shot-examples>
{examples}
</few-shot-examples>

## Already-Determined Scores

The following `core_content`, `flow`, `depth_enhancement`, and `breadth_enhancement` scores were
determined in the prior pass. Use them as your starting point — **do not re-evaluate** those criteria.

{section_scores}

## Generated Article

<generated_output>
{output}
</generated_output>

## Expected Article

<expected_output>
{expected_output}
</expected_output>

## Instructions

For each section listed above, evaluate `core_preservation` using the scores
provided. Return exactly **one entry per section, in the same order** as listed above.
"""


def _build_section_scores_context(article_scores: FollowsGTArticleScores) -> str:
    """Format the per-section core_content/flow/depth/breadth scores as context for the second-pass prompt."""
    lines: list[str] = []
    for section in article_scores.sections:
        cc = section.scores.core_content
        fl = section.scores.flow
        d = section.scores.depth_enhancement
        b = section.scores.breadth_enhancement
        lines.append(f'Section: "{section.title}"')
        lines.append(f'  core_content:        score={cc.score}, reason="{cc.reason}"')
        lines.append(f'  flow:                score={fl.score}, reason="{fl.reason}"')
        lines.append(f'  depth_enhancement:   score={d.score}, reason="{d.reason}"')
        lines.append(f'  breadth_enhancement: score={b.score}, reason="{b.reason}"')
        lines.append("")
    return "\n".join(lines)


def get_core_preservation_prompt(
    output: str,
    expected_output: str,
    article_scores: FollowsGTArticleScores,
    few_shot_examples: FollowsGTMetricFewShotExamples = DEFAULT_FEW_SHOT_EXAMPLES,
) -> str:
    """Generate the second-pass prompt for evaluating CorePreservation.

    This prompt provides the already-determined core_content, flow, depth_enhancement, and
    breadth_enhancement scores for each section as explicit context, so the LLM can evaluate
    core_preservation while building on those scores rather than re-deriving whether ideas are
    present/ordered from the raw articles. Few-shot examples calibrate the LLM by demonstrating
    correct CorePreservation judgments alongside the scores that motivated them.

    Args:
        output: The generated article content.
        expected_output: The expected (ground-truth) article content.
        article_scores: The pass-1 article scores containing core_content, flow, depth_enhancement,
            and breadth_enhancement scores for each section.
        few_shot_examples: Few-shot examples to embed in the prompt. Defaults to
            DEFAULT_FEW_SHOT_EXAMPLES, which contains the same examples used in
            pass-1 (each includes core_preservation scores in addition to the
            five pass-1 criteria).

    Returns:
        The complete formatted prompt string for the second LLM call.
    """
    return CORE_PRESERVATION_PROMPT.format(
        examples=few_shot_examples.to_core_preservation_context(),
        section_scores=_build_section_scores_context(article_scores),
        output=output,
        expected_output=expected_output,
    )
