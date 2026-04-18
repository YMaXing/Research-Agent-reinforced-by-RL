import asyncio
import re
from pathlib import Path
from typing import TypedDict, cast

from langchain_core.runnables import RunnableConfig
from langgraph.checkpoint.base import BaseCheckpointSaver
from langgraph.config import get_stream_writer
from langgraph.func import entrypoint, task
from langgraph.types import RetryPolicy

from brown.base import Loader
from brown.builders import build_article_renderer, build_loaders, build_model
from brown.config_app import get_app_config
from brown.entities.articles import Article, ArticleExamples
from brown.entities.guidelines import ArticleGuideline
from brown.entities.media_items import MediaItem, MediaItems
from brown.entities.profiles import ArticleProfiles
from brown.entities.research import Research
from brown.entities.reviews import ArticleReviews
from brown.nodes.article_reviewer import ArticleReviewer
from brown.nodes.article_writer import ArticleWriter
from brown.nodes.media_generator import MediaGeneratorOrchestrator
from brown.workflows.types import WorkflowProgress

app_config = get_app_config()

retry_policy = RetryPolicy(max_attempts=3, retry_on=Exception)


def build_generate_article_workflow(checkpointer: BaseCheckpointSaver):
    """Create a generate article workflow with optional checkpointer.

    Args:
        checkpointer: Optional checkpointer to use. If None, workflow runs without persistence.

    Returns:
        Configured workflow entrypoint
    """

    return entrypoint(checkpointer=checkpointer)(_generate_article_workflow)


class GenerateArticleInput(TypedDict):
    dir_path: Path


async def _generate_article_workflow(inputs: GenerateArticleInput, config: RunnableConfig) -> str:
    dir_path = inputs["dir_path"]
    dir_path.mkdir(parents=True, exist_ok=True)

    writer = get_stream_writer()

    writer(WorkflowProgress(progress=0, message="Loading context").model_dump(mode="json"))
    context = {}
    loaders = build_loaders(app_config)
    for context_name in ["article_guideline", "research", "profiles", "examples", "exploration_examples"]:
        loader = cast(Loader, loaders[context_name])
        context[context_name] = loader.load(working_uri=dir_path)
    writer(WorkflowProgress(progress=2, message="Loaded context").model_dump(mode="json"))

    writer(WorkflowProgress(progress=3, message="Genererating media items").model_dump(mode="json"))
    media_items = await generate_media_items(context["article_guideline"], context["research"])
    writer(WorkflowProgress(progress=10, message="Generated media items").model_dump(mode="json"))

    writer(WorkflowProgress(progress=15, message="Writing article").model_dump(mode="json"))
    article = await write_article(context["article_guideline"], context["research"], context["profiles"], media_items, context["examples"])
    writer(WorkflowProgress(progress=20, message="Written raw article").model_dump(mode="json"))

    if context["research"].has_exploration_sources:
        writer(WorkflowProgress(progress=22, message="Integrating exploration sources").model_dump(mode="json"))
        article = await integrate_exploration(
            article, context["article_guideline"], context["research"], context["profiles"], media_items, context["exploration_examples"]
        )
        writer(WorkflowProgress(progress=24, message="Integrated exploration sources").model_dump(mode="json"))

    article_path = dir_path / app_config.context.build_article_uri(0)
    article_renderer = build_article_renderer(app_config)
    article_renderer.render(article, output_uri=article_path)
    writer(WorkflowProgress(progress=25, message=f"Rendered raw article to `{article_path}`").model_dump(mode="json"))

    # Distribute progress evenly from 25 to 100 across review/edit/render steps
    steps_per_iteration = 3  # review, edit, render
    total_steps = max(1, app_config.num_reviews * steps_per_iteration)
    step_size = 75 / total_steps  # remaining percentage after 25
    for i in range(1, app_config.num_reviews + 1):
        base_step_index = (i - 1) * steps_per_iteration

        # Review step
        p_review = int(25 + step_size * (base_step_index + 1))
        p_review = min(p_review, 99)
        writer(
            WorkflowProgress(progress=p_review, message=f"Rewiewing article [Iteration {i} / {app_config.num_reviews}]").model_dump(
                mode="json"
            )
        )
        reviews = await generate_reviews(article, context["article_guideline"], context["profiles"], context["research"], media_items)
        writer(WorkflowProgress(progress=p_review, message="Generated reviews").model_dump(mode="json"))

        # Edit step
        p_edit = int(25 + step_size * (base_step_index + 2))
        p_edit = min(p_edit, 99)
        writer(WorkflowProgress(progress=p_edit, message="Editing article").model_dump(mode="json"))
        article = await edit_based_on_reviews(
            context["article_guideline"],
            context["research"],
            context["profiles"],
            media_items,
            context["examples"],
            reviews,
        )
        writer(WorkflowProgress(progress=p_edit, message="Edited article").model_dump(mode="json"))

        # Render step
        p_render = int(25 + step_size * (base_step_index + 3))
        p_render = min(p_render, 99)
        article_path = dir_path / app_config.context.build_article_uri(i)
        article_renderer.render(article, output_uri=article_path)
        writer(WorkflowProgress(progress=p_render, message=f"Rendered article to `{article_path}`").model_dump(mode="json"))

    article_path = dir_path / app_config.context.article_uri
    article_renderer.render(article, output_uri=article_path)
    writer(WorkflowProgress(progress=100, message=f"Final article rendered to `{article_path}`").model_dump(mode="json"))

    return f"Final article rendered to`{article_path}`."


def _is_comparison_matrix_section(section_text: str) -> bool:
    """Check whether a guideline section describes a comparison matrix.

    A comparison matrix is identified when a section compares N items each with
    multiple per-item attributes. Two independent signals are checked:

    1. **Explicit Pros/Cons** — multiple "Pros:" / "Cons:" (or close synonyms) labelled
       per-item. If both counts are >= 2, the section is tabular data.

    2. **Broad per-item attributes** — when the section has >= 2 distinct multi-attribute
       markers (trade-offs, use cases, complexity, performance, when-to-use, etc.) even
       without explicit Pros/Cons labels. This matches the orchestrator prompt's definition
       which covers any per-item property, not only Pros/Cons.
    """
    pros_count = len(re.findall(r"(?i)\bpros?\b\s*:", section_text))
    cons_count = len(re.findall(r"(?i)\bcons?\b\s*:", section_text))
    if pros_count >= 2 and cons_count >= 2:
        return True

    # Broader attribute markers: trade-offs, use cases, complexity, performance, limitations,
    # advantages, disadvantages, when to use — each appearing >= 2 times signals tabular data.
    broad_markers = [
        r"(?i)\btrade-?offs?\b\s*:",
        r"(?i)\buse[\s-]cases?\b\s*:",
        r"(?i)\bcomplexity\b\s*:",
        r"(?i)\bperformance\b\s*:",
        r"(?i)\blimitations?\b\s*:",
        r"(?i)\badvantages?\b\s*:",
        r"(?i)\bdisadvantages?\b\s*:",
        r"(?i)\bwhen[\s-]to[\s-]use\b\s*:",
    ]
    marker_hits = sum(1 for pattern in broad_markers if len(re.findall(pattern, section_text)) >= 2)
    return marker_hits >= 2


def _is_comparison_matrix_description(description: str) -> bool:
    """Return True if the tool-call description asks for a Pros/Cons comparison diagram.

    Any description that explicitly mentions BOTH a pros-like term AND a cons-like
    term is describing 2-D tabular data.  Such content must be rendered as a
    Markdown table by the article writer — never as a Mermaid diagram.
    """
    d = description.lower()
    has_pros = bool(re.search(r"\bpros?\b|\badvantages?\b|\bstrengths?\b|\bbenefits?\b", d))
    has_cons = bool(re.search(r"\bcons?\b|\bdisadvantages?\b|\bdrawbacks?\b|\blimitations?\b|\bweaknesses?\b", d))
    return has_pros and has_cons


def _extract_section_text(guideline: str, section_title: str) -> str | None:
    """Extract the text of the guideline section whose heading best matches *section_title*.

    Returns the raw text between the matching heading and the next heading of
    the same or higher level, or None if no match is found.
    """
    # Normalise for comparison
    title_lower = section_title.lower().strip()
    # Split guideline into (heading, body) pairs
    heading_pattern = re.compile(r"^(#{1,6})\s+(.+)$", re.MULTILINE)
    headings = list(heading_pattern.finditer(guideline))
    for idx, m in enumerate(headings):
        heading_text = m.group(2).strip()
        # Fuzzy: check if the section_title is a substring of the heading (or vice-versa)
        if title_lower in heading_text.lower() or heading_text.lower() in title_lower:
            start = m.end()
            if idx + 1 < len(headings):
                end = headings[idx + 1].start()
            else:
                end = len(guideline)
            return guideline[start:end]
    return None


def _filter_comparison_matrix_tool_calls(
    jobs: list[dict],
    guideline_content: str,
    writer,
) -> list[dict]:
    """Remove mermaid tool calls whose target section is a comparison matrix.

    Detection uses two independent checks — the first match wins:

    1. **Description-based (primary):** If the orchestrator's description for
       the diagram mentions both "pros" (or synonym) AND "cons" (or synonym),
       the call is for 2-D tabular data.  Block it unconditionally.

    2. **Section-content-based (secondary):** If the tool provides a
       section_title that can be matched against a guideline heading, and
       that section contains ≥ 2 "Pros:" / "Cons:" pairs, block it.

    When a call is blocked the article writer's existing fallback produces a
    Markdown table for that section automatically.
    """
    filtered: list[dict] = []
    for job in jobs:
        args = job.get("args", {})
        description = args.get("description_of_the_diagram", "")
        section_title = args.get("section_title", "")

        # --- Primary check: description mentions pros AND cons ---
        if _is_comparison_matrix_description(description):
            writer(
                f"  ⛔ Filtered out mermaid tool call for section '{section_title}' — "
                f"comparison matrix detected in description (pros + cons language); "
                f"article writer will produce a Markdown table instead."
            )
            continue

        # --- Secondary check: guideline section content has pros/cons structure ---
        if section_title:
            section_text = _extract_section_text(guideline_content, section_title)
            if section_text and _is_comparison_matrix_section(section_text):
                writer(
                    f"  ⛔ Filtered out mermaid tool call for section '{section_title}' — "
                    f"comparison matrix detected in guideline section content; "
                    f"article writer will produce a Markdown table instead."
                )
                continue

        filtered.append(job)
    return filtered


# Broad set of comparison-attribute patterns mirroring _is_comparison_matrix_section.
# Two or more distinct hits in a diagram's content flag it as comparison-matrix content.
_COMPARISON_ATTRIBUTE_PATTERNS: tuple[str, ...] = (
    r"\bpros?\b",
    r"\bcons?\b",
    r"\badvantages?\b",
    r"\bdisadvantages?\b",
    r"\bdrawbacks?\b",
    r"\btrade-?offs?\b",
    r"\buse[\s-]cases?\b",
    r"\bcomplexity\b",
    r"\bperformance\b",
    r"\blimitations?\b",
    r"\bwhen[\s-]to[\s-]use\b",
    r"\bbenefits?\b",
    r"\bstrengths?\b",
    r"\bweaknesses?\b",
)


def _filter_comparison_matrix_media_items(
    media_items: list[MediaItem],
    writer,
) -> list[MediaItem]:
    """Post-generation safety net: drop any MermaidDiagram whose content
    renders comparison-matrix (per-item attribute) data.

    If the pre-flight filter was bypassed (e.g. section_title mismatch) and
    a MermaidDiagram was generated anyway, this check inspects the actual
    diagram content.  A diagram that mentions two or more distinct comparison
    attributes — such as Pros/Cons, trade-offs, limitations, use cases,
    complexity, performance, etc. — is considered comparison-matrix content
    and must not be inserted into the article; the article writer will produce
    a Markdown table instead.

    The broad attribute list mirrors ``_is_comparison_matrix_section`` so that
    pre-flight detection and post-generation filtering use consistent criteria.
    """
    from brown.entities.media_items import MermaidDiagram  # local import to avoid circular

    filtered: list[MediaItem] = []
    for item in media_items:
        if isinstance(item, MermaidDiagram):
            content_lower = item.content.lower()
            attribute_hits = sum(1 for pattern in _COMPARISON_ATTRIBUTE_PATTERNS if re.search(pattern, content_lower))
            if attribute_hits >= 2:
                writer(
                    f"  ⛔ Dropped already-generated MermaidDiagram for location '{item.location}' — "
                    f"its content contains {attribute_hits} distinct comparison attributes "
                    f"(comparison matrix); article writer will produce a Markdown table instead."
                )
                continue
        filtered.append(item)
    return filtered


@task(retry_policy=retry_policy)
async def generate_media_items(article_guideline: ArticleGuideline, research: Research) -> MediaItems:
    writer = get_stream_writer()

    model, toolkit = build_model(app_config, node="generate_media_items")
    media_generator_orchestrator = MediaGeneratorOrchestrator(
        article_guideline=article_guideline,
        research=research,
        model=model,
        toolkit=toolkit,
    )
    media_items_to_generate_jobs = await media_generator_orchestrator.ainvoke()

    # Code-level filter: drop mermaid tool calls for sections whose guideline content
    # is a comparison matrix (multiple items each with explicit Pros and Cons).
    # The article writer will automatically produce a Markdown table for these sections.
    media_items_to_generate_jobs = _filter_comparison_matrix_tool_calls(media_items_to_generate_jobs, article_guideline.content, writer)

    writer(f"Found {len(media_items_to_generate_jobs)} media items to generate using the following tool configurations:")
    for i, job in enumerate(media_items_to_generate_jobs):
        writer(f"  • Tool {i + 1}: {job['name']} - {job.get('args', {}).get('description_of_the_diagram', 'No description')}")

    coroutines = []
    for media_item_to_generate_job in media_items_to_generate_jobs:
        tool_name = media_item_to_generate_job["name"]
        tool = media_generator_orchestrator.toolkit.get_tool_by_name(tool_name)
        if tool is None:
            writer(f"⚠️ Warning: Unknown tool '{tool_name}', skipping...")
            continue
        coroutine = tool.ainvoke(media_item_to_generate_job["args"])
        coroutines.append(coroutine)

    writer(f"Executing {len(coroutines)} media item generation jobs in parallel.")
    media_items: list[MediaItem] = await asyncio.gather(*coroutines)
    writer(f"Generated {len(media_items)} media items.")

    # Post-generation safety net: drop any MermaidDiagram whose content contains
    # Pros/Cons labels — meaning the pre-flight filter was bypassed but the
    # generated diagram is still comparison-matrix content.
    media_items = _filter_comparison_matrix_media_items(list(media_items), writer)

    return MediaItems.build(media_items)


@task(retry_policy=retry_policy)
async def write_article(
    article_guideline: ArticleGuideline,
    research: Research,
    article_profiles: ArticleProfiles,
    media_items: MediaItems,
    article_examples: ArticleExamples,
) -> Article:
    model, _ = build_model(app_config, node="write_article")
    article_writer = ArticleWriter(
        article_guideline=article_guideline,
        research=research,
        article_profiles=article_profiles,
        media_items=media_items,
        article_examples=article_examples,
        model=model,
    )
    article = await article_writer.ainvoke()

    return cast(Article, article)


@task(retry_policy=retry_policy)
async def integrate_exploration(
    core_article: Article,
    article_guideline: ArticleGuideline,
    research: Research,
    article_profiles: ArticleProfiles,
    media_items: MediaItems,
    exploration_examples: ArticleExamples,
) -> Article:
    model, _ = build_model(app_config, node="integrate_exploration")
    article_writer = ArticleWriter(
        article_guideline=article_guideline,
        research=research,
        article_profiles=article_profiles,
        media_items=media_items,
        article_examples=ArticleExamples(examples=[]),
        exploration_examples=exploration_examples,
        model=model,
    )
    article = await article_writer.ainvoke_exploration_integration(core_article)

    return article


@task(retry_policy=retry_policy)
async def generate_reviews(
    article: Article, article_guideline: ArticleGuideline, article_profiles: ArticleProfiles, research: Research, media_items: MediaItems
) -> ArticleReviews:
    model, _ = build_model(app_config, node="review_article")
    article_reviewer = ArticleReviewer(
        to_review=article,
        article_guideline=article_guideline,
        article_profiles=article_profiles,
        research=research,
        media_items=media_items,
        model=model,
    )
    reviews = await article_reviewer.ainvoke()

    return cast(ArticleReviews, reviews)


@task(retry_policy=retry_policy)
async def edit_based_on_reviews(
    article_guideline: ArticleGuideline,
    research: Research,
    article_profiles: ArticleProfiles,
    media_items: MediaItems,
    article_examples: ArticleExamples,
    reviews: ArticleReviews,
) -> Article:
    model, _ = build_model(app_config, node="edit_article")
    article_writer = ArticleWriter(
        article_guideline=article_guideline,
        research=research,
        article_profiles=article_profiles,
        media_items=media_items,
        article_examples=article_examples,
        model=model,
        reviews=reviews,
    )
    article = await article_writer.ainvoke()

    return cast(Article, article)
