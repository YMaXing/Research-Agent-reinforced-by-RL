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
from a collection of web search results.

Your task is to evaluate each source based on:
1. **Domain Authority & Trustworthiness**: Prefer reputable websites, official sources, established publications,
academic institutions, and well-known organizations. Avoid obscure or potentially unreliable websites.
2. **Content Quality**: Evaluate the quality and relevance of the answers obtained from each source.
3. **Relevance to Article Guidelines**: How well each source's content aligns with the provided article guidelines.

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

**Selection Criteria:**
- ACCEPT sources from trustworthy domains (e.g., .edu, .gov, established news sites,
official documentation, reputable organizations)
- ACCEPT sources with high-quality, relevant content that directly supports the article guidelines
- REJECT sources from obscure, untrustworthy, or potentially biased websites
- REJECT sources with low-quality, irrelevant, or superficial content
- REJECT sources that seem to be marketing materials, advertisements, or self-promotional content

Return your decision as a structured output with:
1. selection_type: "none" if no sources meet the quality standards, "all" if all sources are acceptable,
or "specific" for specific source IDs
2. source_ids: List of selected source IDs (empty for "none", all IDs for "all", or specific IDs for "specific")
""".strip()

# Select top sources prompt
PROMPT_SELECT_TOP_SOURCES = """
You are assisting with research for an upcoming article.

Here is the article guidelines:
<article_guidelines>
{article_guidelines}
</article_guidelines>

Here is the content of the already scraped guideline URLs:
<scraped_guideline_ctx>
{scraped_guideline_ctx}
</scraped_guideline_ctx>

Here is the content from the web search results:
<web_search_results>
{accepted_sources_data}
</web_search_results>

Your task is to select the most relevant and trustworthy sources from the web search results.
You should consider:
1. **Relevance**: How well each source addresses the article guidelines
2. **Authority**: The credibility and reputation of the source
3. **Quality**: The depth and accuracy of the information provided
4. **Uniqueness**: Sources that provide unique insights not covered by the scraped guideline URLs

Please select the top {top_n} sources that would be most valuable for the article research.

Return your selection with the following structure:
- **selected_urls**: A list of the most valuable URLs to scrape in full, ordered by priority
- **reasoning**: A short explanation summarizing why these specific URLs were chosen and their value to the research

Only include sources that provide genuine value and meet high quality standards.
""".strip()
