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

Guidelines for the set of queries:
• Give priority to sections/topics from the article guidelines that currently lack supporting sources in <past_research> and <scraped_context>.
• Cover any remaining major sections to ensure balanced coverage.
• **Strictly avoid semantic duplication**: each query must target a truly distinct aspect. Do not generate near-equivalents (e.g. "limitations of X" and "failure modes of X").
• Never repeat or closely paraphrase any query that already appears in <full_queries>.
• The web search queries should be natural language questions, not just keywords.

**Few-shot examples:**

Example 1:
Query: What are the most widely accepted evaluation metrics and benchmarks for measuring retrieval quality and generation faithfulness in modern RAG systems?
Reason: This directly fills a major missing section in the article guidelines on evaluation, providing authoritative sources for quantitative assessment that are currently absent from past research.

Example 2:
Query: How do hybrid sparse-dense retrieval architectures improve recall-precision tradeoffs compared to pure dense retrieval in RAG pipelines?
Reason: This targets an important remaining architectural component in the guidelines, ensuring balanced coverage of advanced retrieval strategies not yet addressed in existing material.

Example 3:
Query: What are the primary data privacy and compliance challenges when deploying enterprise-scale RAG systems that access sensitive internal documents?
Reason: This addresses a critical gap in the guidelines regarding production deployment considerations, supplying trustworthy sources on regulatory and security aspects.

Example 4:
Query: How do advanced reranking techniques (such as cross-encoders or LLM-based rerankers) integrate into RAG pipelines to reduce hallucination rates?
Reason: This covers a distinct optimization technique from the guidelines that is currently underrepresented, offering high-quality sources on a specific performance improvement vector.

Now generate exactly {n_queries} new queries following the same style and the rules above.

""".strip()

# Complementary query generation prompt
PROMPT_GENERATE_COMPLEMENTARY_QUERIES_AND_REASONS = """
You are an expert research strategist whose job is to balance **exploitation** (filling direct gaps) with **exploration** (depth + breadth) to make the final article truly comprehensive.

Your task: propose {n_queries} insightful, non-redundant web-search questions that will:
- Dive deeper into topics already covered in the guidelines and past research, OR
- Expand breadth by exploring closely related but uncovered adjacent areas.

Target distribution (follow this exactly):
- Generate approximately **{depth_percentage}% Depth** queries
- Generate approximately **{breadth_percentage}% Breadth** queries

The queries, taken **as a group**, should add genuinely new value that cannot be easily inferred from existing material.

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

**Exploration strategies** (respect the {depth_percentage}% / {breadth_percentage}% distribution above):
• **Depth**: theoretical foundations, technical nuances, alternative perspectives, latest developments, limitations/criticisms, implementation challenges, real-world case studies, future implications.
• **Breadth**: adjacent concepts, cross-domain analogies, historical context, enabling/disrupting technologies, practical applications in other fields, emerging trends connected to the core topic.

**Rules**:
• **Strictly avoid semantic duplication**: each query must target a truly distinct aspect. Do not generate near-equivalents (e.g. "limitations of X" and "failure modes of X").
• Never repeat or closely paraphrase any query that already appears in <full_queries>.
• Strictly follow the requested Depth/Breadth distribution.
• Make questions natural, specific, and optimized for high-quality search results.
• Aim for diversity within the requested ratio.

For each query, provide a short reason that explicitly states:
- whether it is primarily **Depth** or **Breadth**
- exactly what new value it brings to the article.

**Few-shot examples:**

Example 1 (Depth):
Query: What are the core mathematical and information-theoretic limitations of dense retrieval methods in RAG systems when scaling to millions of documents?
Reason: **Depth** - This explores fundamental theoretical constraints of the core retrieval mechanism, revealing scalability bottlenecks not covered in basic guideline discussions.

Example 2 (Depth):
Query: What are the main engineering challenges and latency tradeoffs when integrating real-time knowledge updates into production RAG pipelines?
Reason: **Depth** - This targets practical implementation difficulties and system-level tradeoffs of the core topic, providing actionable insights for real-world deployment.

Example 3 (Breadth):
Query: How have retrieval-augmented techniques originally developed for legal document analysis been adapted and applied in biomedical research and drug discovery?
Reason: **Breadth** - This examines successful applications in adjacent high-stakes domains (biomedicine), offering powerful cross-domain analogies and lessons.

Example 4 (Breadth):
Query: How is the rise of long-context language models and memory-augmented agents changing the role and architecture of traditional RAG systems?
Reason: **Breadth** - This explores an emerging adjacent trend (long-context + agentic systems) and how it intersects with and potentially disrupts core RAG approaches.

Now generate exactly {n_queries} new queries following the same style, the exact Depth/Breadth distribution, and the rules above.

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
- Complementary round: Strongly protect all historical exploitation queries. Only keep new queries that add genuine new depth or breadth value.

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

Example 3 (Complementary round – clear duplicate):
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
Your task is to clean markdown content scraped from a webpage by *only removing* all irrelevant sections such as
headers, footers, navigation bars, advertisements, sidebars, self-promotion, call-to-actions, etc.
Focus on keeping only the core textual content (and code content if there are code sections) that is pertinent to
the article guidelines provided below.
Return *only* the cleaned markdown.
Do not summarize or rewrite the original content. This task is only about *removing* irrelevant content.
Good content should be kept as is, do not touch it.

Here are the article guidelines:
<article_guidelines>
{article_guidelines}
</article_guidelines>

Here is the markdown content to clean:
<markdown_content>
{markdown_content}
</markdown_content>
""".strip()

# Auto source selection prompt
PROMPT_AUTO_SOURCE_SELECTION = """
You are a research assistant tasked with automatically selecting the most trustworthy and relevant sources
from a collection of web search results generated across multiple rounds of a two-phase research process.

**Research Process Context:**
- **Phase 1 (Exploitation)**: Fixed rounds that directly address the core topics and gaps in the article guidelines.
- **Phase 2 (Exploration)**: Later complementary rounds that add depth and breadth through more advanced or adjacent angles.

Your task is to evaluate each source based on:
1. **Domain Authority & Trustworthiness**: Prefer reputable websites, official sources, established publications, academic institutions, and well-known organizations. Avoid obscure or potentially unreliable websites.
2. **Content Quality**: Evaluate the depth, accuracy, and usefulness of the answers obtained from each source.
3. **Relevance to Article Guidelines**: How well each source's content aligns with the provided article guidelines.
4. **Query Origin & Phase Value**: Whether the source came from an exploitation query (core coverage) or a complementary exploration query (depth/breadth).

Here are the article guidelines:
<article_guidelines>
{article_guidelines}
</article_guidelines>

Here are the sources to evaluate:
<sources_to_evaluate>
{sources_data}
</sources_to_evaluate>

For each source, you will see:
- The URL of the source
- The queries that led to this source
- The answers/content obtained from this source

Please analyze each source and determine which ones should be ACCEPTED or REJECTED.

**Selection Criteria (apply in strict priority order):**
- **Strongly protect exploitation sources**: These represent essential guideline coverage. Only reject them if they are clearly low-quality, unreliable, or irrelevant.
- **Higher bar for exploration sources**: Accept complementary sources only if they add genuine new value (theoretical foundations, deeper technical insights, limitations/criticisms, real-world case studies, cross-domain analogies, emerging trends, or important breadth not covered in Phase 1).
- **Trustworthiness**: Prefer sources from high-authority domains (.edu, .gov, established publications, official documentation, reputable organizations).
- **Content Quality**: Accept high-quality, detailed, relevant content. Reject superficial, promotional, biased, marketing, or low-effort material.

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
- **Phase 2 (Exploration)**: Later complementary rounds that add depth (technical nuances, limitations, criticisms, implementation challenges, future implications) and breadth (adjacent concepts, cross-domain analogies, emerging trends, practical applications in other fields).

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

**Selection Criteria (apply in strict priority order):**
1. **Relevance & Gap Filling**: Sources that best address important sections of the article guidelines that are still under-covered.
2. **Uniqueness**: Sources that provide new insights, data, examples, case studies, or perspectives not already present in the scraped guideline URLs or previous phases.
3. **Phase-Aware Value**:
   - **Exploitation sources** (Phase 1): Strongly prioritize high-quality sources that strengthen or deepen core guideline coverage.
   - **Exploration sources** (Phase 2): Apply a **higher bar**. These sources must demonstrate **clear, non-redundant value** that cannot be easily inferred from Phase 1 material. Accept them **only if** they deliver one or more of the following:
     - **Depth** (vertical drilling into the core topic): theoretical foundations, technical nuances, alternative perspectives, latest developments, limitations/criticisms, implementation challenges, real-world case studies, or future implications.
     - **Breadth** (horizontal expansion): adjacent concepts, cross-domain analogies, historical context, enabling/disrupting technologies, practical applications in other fields, or emerging trends connected to the core topic.
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

Your task: Take a large collection of research sources (from both exploitation and exploration phases) and produce the cleanest, most authoritative, non-repetitive knowledge base possible.

**Sources included:**
- Filtered Tavily results (high-quality selected sources)
- Golden sources explicitly mentioned in the article guidelines (stored in URLS_FROM_GUIDELINES_FOLDER)
- Other guideline URLs
- Fully scraped research URLs
- GitHub code repository summaries
- YouTube video transcripts

**Phase-aware protection rules (apply the priority order strictly):**
1. **Golden sources** (from URLS_FROM_GUIDELINES_FOLDER): HIGHEST PRIORITY, These are handpicked by the user and have the highest priority. Never remove or significantly alter content from these sources unless it is completely duplicated word-for-word with another golden source. Always preserve their core content and authority.
2. **Exploitation phase sources** (Phase 1): HIGH PRIORITY, Strongly protect these — they represent essential guideline coverage. Only merge or remove if highly redundant with golden sources or other exploitation material.
3. **Exploration phase sources** (Phase 2): MEDIUM PRIORITY, Higher bar — only keep if they add genuine new value (depth: theoretical foundations, technical nuances, limitations/criticisms, real-world case studies, future implications; breadth: adjacent concepts, cross-domain analogies, emerging trends, applications in other fields). Do not override or dilute golden/exploitation content.

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

Here is all the collected research content to deduplicate:
<all_research_content>
{all_content}
</all_research_content>

**Few-shot examples:**

Example 1 (Golden source protection):
Golden source says: "RAG is defined as retrieval-augmented generation..."
Another source repeats almost the same sentence → Keep the golden version only and discard the duplicate.

Example 2 (Merging complementary):
Exploitation source: "Dense retrieval uses embeddings..."
Exploration source: "In practice, hybrid dense-sparse retrieval improves recall by 15–20% in enterprise settings"
→ Merge into one enriched paragraph, attribute both sources.

**Output instructions:**
- Return clean Markdown only
- Use logical top-level headings mirroring major guideline sections
- Use subheadings for sub-topics
- End each consolidated block with a short attribution line
- Do not add any extra commentary or summary outside the content

Now produce the fully deduplicated research content.
""".strip()