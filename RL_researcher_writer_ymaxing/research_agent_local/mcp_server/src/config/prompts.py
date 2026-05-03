"""Prompt templates used throughout the MCP server."""

# YouTube transcription prompt
PROMPT_YOUTUBE_TRANSCRIPTION = """You are an expert transcriber and video analyst.
Your task is to create a detailed and enriched transcript of the provided video.

Follow these instructions:
1. Transcribe the audio verbatim.
2. Insert timestamps every {timestamp} seconds in the form [MM:SS].
3. Where relevant, add brief, parenthetical descriptions of key visual elements, scenes, or on-screen text that
   complement the audio. For example: (A chart appears showing a flow chart of a RAG pipeline, it includes a section
   for 'Retrieval', 'Reranking', and 'Generation').
4. If there are multiple speakers, try to identify them as 'Speaker 1', 'Speaker 2', etc.
5. At the end of each major section or topic change, add a one-sentence summary in italics.

Produce the output in Markdown format.
"""

# arXiv-specific cleanup prompt (lightweight post-processing after arxiv2markdown)
PROMPT_CLEAN_ARXIV_MARKDOWN = """
You are an expert Markdown editor specializing in cleaning arXiv papers.

Your task: Fix any remaining LaTeX quirks in the provided Markdown while preserving **all** mathematical content, code blocks, tables, figures, and original meaning.

Common fixes to apply:
- Convert raw display math (`\\begin{equation} ... \\end{equation}`, `\\begin{align*} ... \\end{align*}`) to proper Markdown `$$ ... $$` or `\\[` ... `\\]`.
- Expand or remove unexpanded custom macros when possible.
- Convert inline math that still contains raw LaTeX backslashes to clean Markdown math.
- Convert theorem/proof/definition environments to clean Markdown headings or blockquotes.
- Fix figure/table captions and sectioning commands.
- Remove any leftover TeX commands (`\\textit{}`, `\\ref{}`, etc.).
- Ensure all math is properly wrapped and readable.

Return **only** the cleaned Markdown. Do not summarize, shorten, or add commentary.

Here is the article guidelines (for context only):
<article_guidelines>
{article_guidelines}
</article_guidelines>

Here is the raw arXiv Markdown to clean:
<arxiv_markdown>
{arxiv_markdown}
</arxiv_markdown>
""".strip()

# Query generation prompt (exploitation)
PROMPT_GENERATE_QUERIES_AND_REASONS = """
You are a research assistant helping to craft an article.

Your task: propose {n_queries} diverse, insightful web-search questions
that, taken **as a group**, will collect authoritative sources for the
article **and** provide a short explanation of why each question is
important.

<article_guidelines>
{article_guidelines}
</article_guidelines>

<full_queries>
{full_queries}
</full_queries>

<past_research>
{past_research}
</past_research>

<scraped_context>
{scraped_ctx}
</scraped_context>

## SCOPE OF THIS PHASE (EXPLOITATION — LOOKUP ONLY)

Exploitation queries fill direct coverage gaps only. This is the **exploitation phase**. Your sole purpose is to collect direct, authoritative coverage for material the
article guideline already prescribes. You are NOT exploring — a separate **exploration phase** exists later for
depth and breadth research, and stealing its scope here directly harms downstream learning signals.

**Mandatory anchoring rule:** Every query you generate must derive from a concrete *anchor* found verbatim in
`<article_guidelines>`. An anchor is one of:
  (A) An H2 or H3 section heading.
  (B) A bullet point listed under a section.
  (C) A specifically named entity — algorithm, library, technique, paper title, or technical concept — explicitly
      mentioned in the guideline prose.

**Reason format (strictly required):** The `reason` field for every query must begin with the literal token
`Anchor: "<verbatim quote from the guideline>"` followed by a sentence explaining what coverage gap this anchor
still has in `<past_research>` and `<scraped_context>`. Queries whose reason field does not begin with `Anchor: "..."`
are invalid.

**Forbidden categories — these belong exclusively to the exploration phase, do NOT generate them here:**
  ✖ "Limitations / failure modes / criticisms of X"
  ✖ "Latest advancements / recent developments in X" (unless the guideline explicitly lists a specific recent technique by name)
  ✖ "Real-world case studies / industry applications of X"
  ✖ "History / evolution / origin of X"
  ✖ "Future implications / open research directions / emerging trends in X"
  ✖ "Cross-domain analogies / lessons from other fields"
  ✖ "Enabling, disrupting, or adjacent technologies for X"
  ✖ "Comparison with adjacent or competing approach Y" (where Y is not also listed in the guideline)
  ✖ "Theoretical foundations / mathematical underpinnings of X" (unless the guideline explicitly lists them)

**Allowed coverage questions** (the only categories that belong here):
  ✓ "What is X?" / "How does X work?" — only when X is anchor-listed and not already covered.
  ✓ "What are the components / key concepts of X?" — only for anchor-listed X.
  ✓ "How is X implemented in <library/framework named in the guideline>?"
  ✓ "What does <named paper/method from the guideline> say/do?"

## RULES

• Give priority to anchors that currently have **no** supporting sources in `<past_research>` and `<scraped_context>`.
• If an anchor already has at least one strong source covering it, do not generate a query for it unless a clearly
  distinct sub-aspect of that anchor is explicitly listed in the guideline and remains uncovered.
• Cover the remaining major anchors to ensure balanced coverage across the guideline.
• **Strictly avoid semantic duplication**: each query must target a truly distinct anchor or sub-aspect. Do not
  generate near-equivalents (e.g. "limitations of X" and "failure modes of X" — and both are forbidden anyway).
• Never repeat or closely paraphrase any query that already appears in `<full_queries>`.
• Web-search queries should be natural-language questions, not just keywords.
• **Each query must be ≤ 20 words and address a single, focused concept.** Do NOT combine multiple
  sub-questions into one query and do NOT paste verbatim guideline text as the query — long, multi-part
  essay questions produce poor web-search results.
• If you cannot find {n_queries} legitimate uncovered anchors, generate fewer queries rather than inventing
  exploration-flavored questions to fill the quota.

**Few-shot examples** (note the mandatory `Anchor:` prefix in every reason):

Example 1:
Query: What evaluation metrics and benchmarks does the RAGAS framework provide for measuring retrieval quality and generation faithfulness?
Reason: Anchor: "### Evaluation — RAGAS framework". The guideline lists RAGAS as the evaluation toolkit for the article but no current source covers its specific metric definitions; this fills a direct prescribed-coverage gap.

Example 2:
Query: How does the BM25 + dense hybrid retrieval architecture described in the article guideline work?
Reason: Anchor: "BM25 + dense hybrid retrieval" (bullet under "## Retrieval architectures"). The guideline names this exact architecture as a required topic but past research only covers pure dense retrieval; this query directly fills the prescribed BM25-hybrid gap.

Example 3:
Query: What are the key components of LangChain's RetrievalQA chain referenced in the article guideline?
Reason: Anchor: "LangChain RetrievalQA" (named entity in the implementation section). The guideline explicitly references this chain as the implementation example but no scraped source documents its components; this is a direct lookup query.

Example 4:
Query: What is the chunking strategy proposed in the LlamaIndex documentation listed under "Other Sources"?
Reason: Anchor: "## Chunking strategies" (H2) and "LlamaIndex chunking docs" (named source). Past research mentions chunking generically but does not cover the specific LlamaIndex strategy named in the guideline; this fills a prescribed-coverage gap.

Now generate exactly {n_queries} new queries (or fewer, if the guideline does not have that many uncovered anchors)
following the rules above. Every reason must begin with `Anchor: "..."`.

""".strip()

# Complementary query generation prompt
PROMPT_GENERATE_COMPLEMENTARY_QUERIES_AND_REASONS = """
You are an expert research strategist whose job is to add **exploration** value (depth + breadth) on top of the
prescribed coverage that the exploitation phase has already collected. Your sole purpose is to fill gaps that the
exploitation phase, by design, was not allowed to fill.

Your task: propose {n_queries} insightful, non-redundant web-search questions that will:
- Dive deeper into topics already covered in the guidelines and past research, OR
- Expand breadth by exploring closely related but uncovered adjacent areas.

Target distribution (follow this exactly):
- Generate approximately **{depth_percentage}% Depth** queries
- Generate approximately **{breadth_percentage}% Breadth** queries

The queries, taken **as a group**, must add genuinely new value that cannot be inferred from existing material.

<article_guidelines>
{article_guidelines}
</article_guidelines>

<full_queries>
{full_queries}
</full_queries>

<past_research>
{past_research}
</past_research>

<already_covered_context>
{scraped_ctx}
</already_covered_context>

## SCOPE OF THIS PHASE (EXPLORATION — GAP-DRIVEN ONLY)

The exploitation phase (step 3) was strictly restricted to **lookup-only** coverage queries derived from explicit
anchors in `<article_guidelines>` (H2/H3 headings, bullet points, named entities). Your job is the complement:
you must generate queries that the exploitation phase was **forbidden** from generating.

**Mandatory category labelling:** Each query you generate must target one of the depth or breadth bullets listed
below. The `reason` field must begin with the literal token `Category: Depth—<bullet>` or
`Category: Breadth—<bullet>`, followed by `Anchor: "<guideline anchor this query deepens or expands around>"`,
followed by a sentence explaining the new value the query brings. Reasons that do not begin with
`Category: Depth—...` or `Category: Breadth—...` are invalid.

**Forbidden in this phase — these belong to the exploitation phase (step 3), do NOT generate them here:**
  ✖ Pure-coverage questions like "What is X?", "How does X work?", "What are the components of X?" where X is
    anchor-listed in the guideline. If `<past_research>` shows X is not yet covered, that is a step-3 problem,
    not a step-4 problem — leave it alone.
  ✖ Lookup queries for named libraries, papers, or methods that are explicitly listed in the guideline.

**Required for this phase — every query must fall into one of these depth/breadth bullets:**
*Depth* means intensifying understanding of a topic's inner workings — the query stays within the subject. *Breadth*
means connecting outward to adjacent areas — the query moves beyond the subject to related concepts, other fields,
or wider contexts.

• **Depth bullets** (inward — intensify understanding of the core topic):
    – motivation for the topic: why it exists, what problem it solves
    – theoretical foundations or mathematical underpinnings
    – technical nuances or alternative implementation perspectives
    – latest advancements or recent developments
    – limitations, criticisms, or failure modes
    – implementation challenges or latency/scale trade-offs
    – real-world case studies or concrete metrics
    – future implications or open research directions
• **Breadth bullets** (outward — connect to adjacent areas outside the core topic):
    – adjacent or related concepts that expand the scope without straying from the core theme
    – cross-domain analogies or lessons from other fields
    – historical context or evolution of the topic
    – enabling or disrupting technologies that intersect with the core topic
    – practical applications in other industries or domains
    – emerging trends in adjacent fields or the broader ecosystem

## RULES

• **Strictly avoid semantic duplication**: each query must target a truly distinct depth or breadth bullet. Do not
  generate near-equivalents (e.g. "limitations of X" and "failure modes of X").
• Never repeat or closely paraphrase any query that already appears in `<full_queries>`, including the exploitation
  queries from step 3.
• Strictly follow the requested Depth/Breadth distribution.
• Make questions natural, specific, and optimized for high-quality search results.
• **Each query must be ≤ 20 words and address a single, focused concept.** Do NOT combine multiple
  sub-questions into one query — long, multi-part essay questions produce poor web-search results.
• Aim for diversity within the requested ratio.

**Few-shot examples** (note the mandatory `Category: ...` and `Anchor: "..."` prefixes):

Example 1 (Depth):
Query: What are the core mathematical and information-theoretic limitations of dense retrieval methods in RAG systems when scaling to millions of documents?
Reason: Category: Depth—theoretical foundations. Anchor: "## Dense retrieval" (H2 in guideline). Past research covers basic dense retrieval mechanics; this query reveals fundamental scalability constraints not addressed by any existing source and not coverable by step 3.

Example 2 (Depth):
Query: What are the main engineering challenges and latency tradeoffs when integrating real-time knowledge updates into production RAG pipelines?
Reason: Category: Depth—implementation challenges and latency/scale trade-offs. Anchor: "production RAG pipelines" (named in the deployment section). Provides practical engineering insights absent from existing sources; outside step 3's lookup-only scope.

Example 3 (Breadth):
Query: How have retrieval-augmented techniques originally developed for legal document analysis been adapted in biomedical research and drug discovery?
Reason: Category: Breadth—cross-domain analogies. Anchor: "## Retrieval-augmented generation" (H2 in guideline). Examines successful applications in adjacent high-stakes domains (biomedicine), offering cross-domain analogies that step 3 cannot reach.

Example 4 (Breadth):
Query: How is the rise of long-context language models and memory-augmented agents changing the role and architecture of traditional RAG systems?
Reason: Category: Breadth—emerging trends in adjacent fields. Anchor: "## RAG architectures" (H2 in guideline). Explores an emerging adjacent trend (long-context + agentic systems) that intersects with and potentially disrupts the core RAG approach; not coverable by step 3.

Now generate exactly {n_queries} new queries following the same style, the exact Depth/Breadth distribution, and
the rules above. Every reason must begin with `Category: Depth—...` or `Category: Breadth—...` followed by
`Anchor: "..."`.

""".strip()

# Query deduplication prompt
PROMPT_DEDUPLICATE_QUERIES = """
You are an expert research query deduplicator acting as the final safety net in a two-phase research system.

The workflow has two distinct phases:
- Phase 1 (Exploitation): Fixed 3 rounds that directly cover the article guidelines where the tool 'generate_next_queries_tool' is used.
- Phase 2 (Exploration): RL-controlled complementary rounds that add depth and breadth where the tool 'generate_next_complementary_queries_tool' is used.

Your task: Take a newly generated batch of queries from the current round and remove any that are semantically redundant with the entire historical set of queries created in previous rounds.

Perform **two-stage deduplication** on the new queries:

**Stage 1 (Same-round)**: First, remove any semantic duplicates *within* the new batch itself. Keep only the best version of each distinct research direction.

**Stage 2 (Historical)**: Then, remove any surviving queries that are redundant with the full history.

**Phase-specific rules for Stage 2:**
- Exploitation round: Be strict. Prevent close duplicates with previous exploitation queries.
  **Backstop rule (exploration leakage):** Also REJECT any new exploitation query whose intent clearly falls
  into one of the depth or breadth categories listed below — those categories are reserved exclusively for
  the complementary phase. An exploitation query is leakage if it asks about: limitations / criticisms /
  failure modes; latest advancements / recent developments; theoretical foundations or mathematical
  underpinnings; real-world case studies / industry applications; future implications / open research /
  emerging trends; cross-domain analogies / lessons from other fields; history / evolution / origin;
  enabling / disrupting / adjacent technologies; comparison with adjacent or competing approaches that are
  not also explicitly listed in the article guideline. A legitimate exploitation query asks for direct
  coverage of a concept named verbatim in the article guideline (e.g. "What is X?", "How does X work?",
  "What are the components of X?", "How is X implemented in <named library>?").
- Complementary round: Strongly protect all historical exploitation queries. Only keep new queries that add genuine new depth or breadth value.
  For this purpose use the following definitions — these mirror the downstream evaluation criteria:
  - *Depth* (inward — intensify understanding of the core topic): motivation for the topic (why it exists, what problem it solves), theoretical foundations or mathematical underpinnings, technical nuances or alternative implementation perspectives, latest advancements or recent developments, limitations/criticisms/failure modes, implementation challenges or latency/scale trade-offs, real-world case studies or concrete metrics, future implications or open research directions.
  - *Breadth* (outward — connect to adjacent areas outside the core topic): adjacent or related concepts that expand the scope, cross-domain analogies or lessons from other fields, historical context or evolution of the topic, enabling/disrupting technologies that intersect with the core topic, practical applications of the core topic in other industries or domains, emerging trends in adjacent fields or the broader ecosystem.
  A complementary query adds genuine new value if it clearly targets a depth or breadth category not already covered by any historical query.
  **Backstop rule (exploitation leakage):** Also REJECT any new complementary query whose intent is pure
  coverage — e.g. "What is X?" / "How does X work?" / "What are the components of X?" — when X is already
  named in the article guideline. Pure coverage of guideline-named concepts belongs to the exploitation
  phase, not here.

**What counts as a semantic duplicate?**
Queries that target essentially the same knowledge need, angle, or sub-topic and would produce highly overlapping search results, even if worded differently.

Here is the full history of all previous queries (each tagged with its type):
<full_queries_history>
{full_queries_history}
</full_queries_history>

Here are the **new queries** from the current {query_source} round:
<new_queries>
{new_queries_list}
</new_queries>

**Few-shot examples:**

Example 1 (Exploitation round):
History contains: Query [12] [Exploitation]: What are the main limitations of RAG systems?
New query: What are the primary failure modes and scalability issues of retrieval-augmented generation?
→ Remove the new query (redundant with previous exploitation coverage).

Example 2 (Complementary round):
History contains: Query [12] [Exploitation]: What are the main limitations of RAG systems?
New query: How have retrieval-augmented techniques originally developed for legal e-discovery been adapted in biomedical literature search?
→ Keep the new query (adds meaningful cross-domain breadth without duplicating core coverage).

Example 3 (Complementary round - clear duplicate):
History contains: Query [15] [Exploitation]: How do reranking techniques improve RAG performance?
New query: What are the best reranking methods to reduce hallucinations in RAG pipelines?
→ Remove the new query (too close to existing exploitation material).

Now analyze the new queries above.

Return **only** a valid JSON object with this exact structure and nothing else:

{{
  "kept_queries": [
    "exact text of first kept query",
    "exact text of second kept query"
  ],
  "removed_queries": [
    "exact text of removed query"
  ],
  "reasoning": "One or two sentences explaining your most important deduplication decisions."
}}

""".strip()

# Query shortening prompt — used when a generated query exceeds the character limit
PROMPT_SHORTEN_QUERY = """
Rewrite the following web-search query as a single, focused question of at most {max_chars} characters.
Keep the single most important concept from the original. Return ONLY the rewritten query — no explanation, no quotes.

Original query: {query}
""".strip()

# Web search prompt
PROMPT_WEB_SEARCH = """
Question: {query}

Provide a detailed answer to the question above.
The answer should be organized into source sections, where each source section
contains all the information coming from a single source.
Never use multiple source citations in the same source section. A source section should refer to a single source.
Focus on the official sources and avoid personal opinions.
For each source, write as much information as possible coming from the source
and that is relevant to the question (at most 300 words).

Return a list of objects, where each object represents a source and has the following fields:
- url: The URL of the source
- answer: The detailed answer extracted from that source
""".strip()

# Markdown cleaning prompt
PROMPT_CLEAN_MARKDOWN = """
Your task is to clean markdown content scraped from a webpage by removing **only web-page boilerplate** such as:
site headers, footers, navigation menus, cookie banners, advertisements, sidebars, subscription prompts,
self-promotion blocks, social-media share buttons, "related articles" sections, and call-to-action elements.

**Critical rules:**
- Keep ALL substantive article content: paragraphs, headings, code blocks, tables, lists, images, diagrams, and any explanatory text — even if some sections seem tangential.
- Do NOT filter or remove sections based on topic relevance. Your job is boilerplate removal, not content curation.
- Do NOT summarize, condense, paraphrase, or rewrite any kept content. Return it verbatim.
- When in doubt, **keep** the content. Err on the side of preserving too much rather than too little.
- If the entire input consists of boilerplate with no substantive article content at all, return exactly the string `<!-- NO_CONTENT -->` and nothing else. Do NOT explain or describe what you removed.

The article guidelines below are provided only so you can confirm the page is on-topic (i.e., not a completely unrelated page). Do NOT use them to decide which sections of the article to keep or remove.

<article_guidelines>
{article_guidelines}
</article_guidelines>

Here is the markdown content to clean:
<markdown_content>
{markdown_content}
</markdown_content>
""".strip()

# Auto source selection prompts (split by phase for independent evaluation)

PROMPT_AUTO_SOURCE_SELECTION_EXPLOITATION = """
You are a research assistant tasked with selecting the most trustworthy and relevant sources
from a collection of web search results produced during the **exploitation phase** of a research process.

**Phase Context:**
These are **exploitation sources** — they were generated by queries that directly address the core topics
and gaps in the article guidelines. They represent essential guideline coverage.

Here are the article guidelines:
<article_guidelines>
{article_guidelines}
</article_guidelines>

Here are the exploitation sources to evaluate:
<sources_to_evaluate>
{sources_data}
</sources_to_evaluate>

For each source, you will see:
- The URL of the source
- The query that led to this source
- The answer/content obtained from this source

---

## Evaluation Criteria

Evaluate each source **independently** on the following dimensions:
1. **Relevance to Article Guidelines**: Does this source's content align with at least one section or topic in the article guidelines?
2. **Domain Authority & Trustworthiness**: Prefer reputable websites, official sources, established publications, academic institutions, and well-known organizations. Avoid obscure or potentially unreliable websites.
3. **Content Quality**: Does the answer contain substantive, accurate, and useful information? Reject only if the content is superficial, promotional, biased, marketing, or low-effort material.

**CRITICAL GUIDELINES:**
- **Strongly protect exploitation sources.** These represent essential guideline coverage. Only reject a source if it is clearly low-quality, unreliable, or irrelevant to the article topic.
- **Evaluate each source on its own merits.** Do NOT reject sources for being similar to, or covering the same topic as, other sources. Redundancy removal happens in a later deduplication step — your job here is strictly individual quality filtering.
- **Expected acceptance rate: 70-90%.** Rejection should be the exception, not the norm. If you find yourself rejecting more than ~30% of exploitation sources, re-examine whether you are applying the criteria too aggressively.

---

Return your decision as a structured output with:
1. selection_type: "none" if no sources meet the quality standards, "all" if all sources are acceptable,
or "specific" for specific source IDs
2. source_ids: List of selected source IDs (empty for "none", all IDs for "all", or specific IDs for "specific")
""".strip()

PROMPT_AUTO_SOURCE_SELECTION_EXPLORATION = """
You are a research assistant tasked with selecting the most trustworthy and relevant sources
from a collection of web search results produced during the **exploration phase** of a research process.

**Phase Context:**
These are **exploration sources** — they were generated by queries designed to add depth and breadth
through more advanced or adjacent angles beyond the core guideline topics. They complement the exploitation
sources that already provide direct guideline coverage.

Here are the article guidelines:
<article_guidelines>
{article_guidelines}
</article_guidelines>

Here are the exploration sources to evaluate:
<sources_to_evaluate>
{sources_data}
</sources_to_evaluate>

For each source, you will see:
- The URL of the source
- The query that led to this source
- The answer/content obtained from this source

---

## Evaluation Criteria

Evaluate each source **independently** on the following dimensions:
1. **Relevance to Article Guidelines**: Does this source add genuine new value — in depth or breadth — to **at least one** section of the article guidelines?
   This criterion is satisfied if you can identify at least one specific guideline section that the source meaningfully enriches through one or more of the following:
   - **Depth** (inward — intensify understanding of the core topic): motivation for the topic (why it exists, what problem it solves), theoretical foundations or mathematical underpinnings, technical nuances or alternative implementation perspectives, latest advancements or recent developments, limitations/criticisms/failure modes, implementation challenges or latency/scale trade-offs, real-world case studies or concrete metrics, future implications or open research directions.
   - **Breadth** (outward — connect to adjacent areas outside the core topic): adjacent or related concepts that expand the scope, cross-domain analogies or lessons from other fields, historical context or evolution of the topic, enabling/disrupting technologies that intersect with the core topic, practical applications of the core topic in other industries or domains, emerging trends in adjacent fields or the broader ecosystem.
   If the source is clearly off-topic (e.g., about an unrelated domain like warehouse logistics when the article is about AI memory), reject it.
2. **Domain Authority & Trustworthiness**: Prefer reputable websites, official sources, established publications, academic institutions, and well-known organizations. Avoid obscure or potentially unreliable websites.
3. **Content Quality**: Does the answer contain substantive, accurate, and useful information? Reject only if the content is superficial, promotional, biased, marketing, or low-effort material.

**CRITICAL GUIDELINES:**
- **Evaluate each source on its own merits.** Do NOT reject sources for being similar to, or covering the same topic as, other sources. Redundancy removal happens in a later deduplication step — your job here is strictly individual quality filtering.
- **Expected acceptance rate: 70-90%.** Exploration sources are by nature more speculative, so a moderate rejection rate is expected. But be careful not to over-filter: sources that provide genuine depth or breadth on any guideline section should be accepted, even if their angle is unconventional.
- **Reject clearly irrelevant sources** (wrong domain entirely, no connection to article topic) and **low-quality sources** (promotional, superficial, broken content). Do NOT reject a source merely because it is tangential or covers a niche angle — tangential depth is the whole purpose of exploration.

---

Return your decision as a structured output with:
1. selection_type: "none" if no sources meet the quality standards, "all" if all sources are acceptable,
or "specific" for specific source IDs
2. source_ids: List of selected source IDs (empty for "none", all IDs for "all", or specific IDs for "specific")
""".strip()

# Select top sources prompt
PROMPT_SELECT_TOP_SOURCES = """
You are assisting with research for an upcoming article in a two-phase research workflow.

**Research Process Context:**
- **Phase 1 (Exploitation)**: Fixed rounds that directly address the core topics and gaps in the article guidelines.
- **Phase 2 (Exploration)**: Later complementary rounds that add depth (inward — intensifying understanding of the core topic) and breadth (outward — expanding to adjacent areas beyond the core topic).

Your task is to select the **top {top_n}** most valuable sources from the accepted Tavily web search results for full content scraping.

Here is the article guidelines:
<article_guidelines>
{article_guidelines}
</article_guidelines>

Here is the content of the already scraped guideline URLs:
<scraped_guideline_ctx>
{scraped_guideline_ctx}
</scraped_guideline_ctx>

Here is the content from the accepted web search results (from both exploitation and exploration phases):
<web_search_results>
{accepted_sources_data}
</web_search_results>

For each accepted source, you will see:
- The research phase it originated from ([EXPLOITATION] or [EXPLORATION])
- The URL of the source
- The queries that led to this source
- The answers/content obtained from this source

**Selection Criteria (apply in strict priority order):**
1. **Relevance & Gap Filling**: Sources that best address important sections of the article guidelines that are still under-covered.
2. **Uniqueness**: Sources that provide new insights, data, examples, case studies, or perspectives not already present in the scraped guideline URLs or previous phases.
3. **Phase-Aware Value**:
   - **Exploitation sources** (Phase 1): Strongly prioritize high-quality sources that strengthen or deepen core guideline coverage.
   - **Exploration sources** (Phase 2): Apply a **higher bar**. These sources must demonstrate **clear, non-redundant value** that cannot be easily inferred from Phase 1 material. Accept them **only if** they deliver one or more of the following:
     - **Depth** (inward — intensify understanding of the core topic): motivation for the topic (why it exists, what problem it solves), theoretical foundations or mathematical underpinnings, technical nuances or alternative implementation perspectives, latest advancements or recent developments, limitations/criticisms/failure modes, implementation challenges or latency/scale trade-offs, real-world case studies or concrete metrics, future implications or open research directions.
     - **Breadth** (outward — connect to adjacent areas outside the core topic): adjacent or related concepts that expand the scope, cross-domain analogies or lessons from other fields, historical context or evolution of the topic, enabling/disrupting technologies that intersect with the core topic, practical applications of the core topic in other industries or domains, emerging trends in adjacent fields or the broader ecosystem.
   - Exploration sources must meaningfully expand the article's comprehensiveness, introduce novel angles, or provide insights that Phase 1 sources alone cannot supply. Reject any exploration source that is merely a rephrasing or slight variation of existing exploitation material.
4. **Authority & Quality**: Prefer reputable, trustworthy domains with high-depth, accurate, and well-structured content.
5. **Diversity**: When possible, select a balanced mix across phases and topics for maximum overall research value.

Please select the top {top_n} sources that will add the highest overall value to the final research file.

Return your selection with the following structure:
- **selected_urls**: A list of the most valuable URLs to scrape in full, ordered by priority (most valuable first)
- **reasoning**: A short explanation summarizing why these specific URLs were chosen and what unique value they bring to the research

Only include sources that provide genuine additional value and meet high quality standards.
""".strip()

# Content deduplication prompt
PROMPT_CONTENT_DEDUPLICATION = """
You are an expert research editor and knowledge consolidator working on a comprehensive article.

Your task: Take a large collection of research sources (from golden sources included in article guideline file to both exploitation and exploration phases) and produce the cleanest, most authoritative, non-repetitive knowledge base possible.

**Sources included** (each item is wrapped in an XML tag that identifies its source category and research phase):
- `<golden_source type="guideline_url">` — URLs explicitly listed in the article guidelines (HIGHEST PRIORITY)
- `<golden_source type="local_files">` — Local files referenced in the article guidelines (HIGHEST PRIORITY)
- `<golden_source type="code_summaries">` — GitHub/code repository summaries from the guidelines (HIGHEST PRIORITY)
- `<golden_source type="youtube_transcripts">` — YouTube transcripts from the guidelines (HIGHEST PRIORITY)
- `<research_source phase="exploitation">` — Fully scraped research URLs, exploitation phase (HIGH PRIORITY)
- `<research_source phase="exploration">` — Fully scraped research URLs, exploration phase (MEDIUM PRIORITY)
- `<tavily_results phase="exploitation">` — Tavily web search results, exploitation phase (HIGH PRIORITY)
- `<tavily_results phase="exploration">` — Tavily web search results, exploration phase (MEDIUM PRIORITY)

Each tag carries a `file` attribute for source attribution. Tavily chunks inside `<tavily_results>` also contain inline `Phase:` headers per source block.

**Note:** Not all source types are guaranteed to be present. If the user's article guidelines contain no URLs or local files, there will be no `<golden_source>` tags in the content — this is normal. In that case, treat `<research_source phase="exploitation">` and `<tavily_results phase="exploitation">` as the highest-priority sources and apply the same protection rules to them accordingly.

**Phase-aware protection rules** — use the XML tags to identify each item's priority tier (apply strictly):
1. **Golden sources** (`<golden_source ...>`): HIGHEST PRIORITY. Handpicked by the user. Never remove or significantly alter their content unless it is completely duplicated word-for-word with another golden source. Always preserve their core content and authority.
2. **Exploitation phase sources** (`<research_source phase="exploitation">`, `<tavily_results phase="exploitation">`): HIGH PRIORITY. Strongly protect these — they represent essential guideline coverage. Only merge or remove if highly redundant with golden sources or other exploitation material.
3. **Exploration phase sources** (`<research_source phase="exploration">`, `<tavily_results phase="exploration">`): MEDIUM PRIORITY. Apply a higher bar — only keep if they add genuine new value:
   - **Depth** (inward — intensify understanding of the core topic): motivation for the topic (why it exists, what problem it solves), theoretical foundations or mathematical underpinnings, technical nuances or alternative implementation perspectives, latest advancements or recent developments, limitations/criticisms/failure modes, implementation challenges or latency/scale trade-offs, real-world case studies or concrete metrics, future implications or open research directions.
   - **Breadth** (outward — connect to adjacent areas outside the core topic): adjacent or related concepts that expand the scope, cross-domain analogies or lessons from other fields, historical context or evolution of the topic, enabling/disrupting technologies that intersect with the core topic, practical applications of the core topic in other industries or domains, emerging trends in adjacent fields or the broader ecosystem.
   Do not override or dilute golden/exploitation content.

**Goals (in priority order):**
- Preserve golden sources almost untouched
- Identify and remove semantic duplicates / high-overlap across all sources
- Keep the single best version of each unique idea (prefer golden > exploitation > high-authority exploration)
- Merge complementary details only when they enrich without losing depth
- Preserve original wording, depth, code snippets, and transcript insights — never summarize
- Add concise source attribution at the end of each consolidated block (prefer titles/URLs when available)

**Special handling:**
- Code & GitHub summaries: Keep most complete version; merge only different aspects
- YouTube transcripts: Convert timestamps to headings; keep key quotes/insights
- Organize into logical topic clusters aligned with article guidelines

Here are the article guidelines (use as reference for relevance and structure):
<article_guidelines>
{article_guidelines}
</article_guidelines>

Here is all the collected research content to deduplicate. Each item is wrapped in a typed XML tag that encodes its source category and research phase — use these tags to apply the priority rules above:
<all_research_content>
{all_content}
</all_research_content>

**Few-shot examples:**

Example 1 — Golden source overrides non-golden duplicate:
  Input:
    <golden_source type="guideline_url" file="rag_overview.md">
    RAG (Retrieval-Augmented Generation) augments an LLM's parametric knowledge with non-parametric documents retrieved dynamically at inference time.
    </golden_source>
    <research_source phase="exploitation" file="blog_rag_intro.md">
    Phase: [EXPLOITATION]
    RAG, or Retrieval-Augmented Generation, enhances language models by fetching relevant documents before generating a response.
    </research_source>
  → Keep the golden source verbatim. The exploitation source conveys the same definition — discard it.
  Output block: "RAG (Retrieval-Augmented Generation) augments an LLM's parametric knowledge with non-parametric documents retrieved dynamically at inference time.  *Source: rag_overview.md*"

Example 2 — Exploitation core kept; exploration merged for genuine added depth:
  Input:
    <research_source phase="exploitation" file="dense_retrieval.md">
    Phase: [EXPLOITATION]
    Dense retrieval encodes queries and documents into a shared embedding space and retrieves by nearest-neighbour search.
    </research_source>
    <research_source phase="exploration" file="hybrid_retrieval_study.md">
    Phase: [EXPLORATION]
    In enterprise benchmarks, hybrid dense-sparse retrieval improves recall@10 by 15-20% over pure dense retrieval, particularly on long-tail queries.
    </research_source>
  → Keep the exploitation sentence as the base. Append the exploration finding as a new sentence — it adds a concrete, quantified insight not present in the exploitation source.
  Output block: "Dense retrieval encodes queries and documents into a shared embedding space and retrieves by nearest-neighbour search. In enterprise benchmarks, hybrid dense-sparse retrieval improves recall@10 by 15-20% over pure dense retrieval, particularly on long-tail queries.  *Sources: dense_retrieval.md, hybrid_retrieval_study.md*"

Example 3 — Exploration source rejected (mere rephrasing, no new value):
  Input:
    <research_source phase="exploitation" file="chunking_strategies.md">
    Phase: [EXPLOITATION]
    Chunking strategies critically affect RAG retrieval quality: fixed-size chunks risk cutting mid-sentence; semantic chunking respects natural topic boundaries.
    </research_source>
    <research_source phase="exploration" file="text_splitting_blog.md">
    Phase: [EXPLORATION]
    How you split your text matters a lot for RAG — splitting in the wrong place can hurt retrieval performance significantly.
    </research_source>
  → The exploration source is a superficial rephrasing of the exploitation content with no added depth, data, or new angle. Discard it entirely. Keep only the exploitation block.

Example 4 — Two golden sources with word-for-word overlap (only case to trim a golden):
  Input:
    <golden_source type="guideline_url" file="paper_a.md">
    The attention mechanism computes a weighted sum of values, where weights are derived from query-key dot products scaled by √d_k.
    </golden_source>
    <golden_source type="local_files" file="paper_b.md">
    The attention mechanism computes a weighted sum of values, where weights are derived from query-key dot products scaled by √d_k.
    </golden_source>
  → Identical word-for-word. Keep one copy (prefer the first encountered). This is the only situation where a golden source may be dropped.
  Output block: "The attention mechanism computes a weighted sum of values, where weights are derived from query-key dot products scaled by √d_k.  *Source: paper_a.md*"

Example 5 — Code summary takes precedence over shallower exploitation paraphrase:
  Input:
    <golden_source type="code_summaries" file="langchain_repo.md">
    LangChain's RetrieverChain wires together: (1) a BaseRetriever calling vector-store similarity search, (2) a StuffDocumentsChain that concatenates retrieved docs, (3) an LLMChain that formats the final prompt.
    </golden_source>
    <research_source phase="exploitation" file="langchain_blog.md">
    Phase: [EXPLOITATION]
    LangChain provides a RetrieverChain for RAG. It retrieves documents and passes them to an LLM.
    </research_source>
  → The golden code summary is more complete and precise. Keep it; discard the shallower exploitation paraphrase.
  Output block: "LangChain's RetrieverChain wires together: (1) a BaseRetriever calling vector-store similarity search, (2) a StuffDocumentsChain that concatenates retrieved docs, (3) an LLMChain that formats the final prompt.  *Source: langchain_repo.md*"

Example 6 — YouTube transcript: convert timestamps to subheading, preserve direct quotes verbatim:
  Input:
    <golden_source type="youtube_transcripts" file="karpathy_lecture.md">
    [12:45] "The problem with naive RAG is that your retriever and your generator are completely decoupled — they don't know about each other's failure modes."
    [13:10] (Slide shown: diagram of retrieval errors propagating to the generator)
    [13:30] "What you really want is some form of end-to-end signal that lets the retriever learn from generation errors."
    </golden_source>
  → Convert the timestamp block into a subheading. Preserve the direct quotes and visual description exactly — never paraphrase or summarize.
  Output block:
    ### Karpathy on Retriever-Generator Coupling
    "The problem with naive RAG is that your retriever and your generator are completely decoupled — they don't know about each other's failure modes." *(A diagram shows retrieval errors propagating to the generator.)* "What you really want is some form of end-to-end signal that lets the retriever learn from generation errors."
    *Source: karpathy_lecture.md*

**Output instructions:**
- Return clean Markdown only
- Use logical top-level headings mirroring major guideline sections
- Use subheadings for sub-topics
- End each consolidated block with a short attribution line
- Do not add any extra commentary or summary outside the content

Now produce the fully deduplicated research content.
""".strip()