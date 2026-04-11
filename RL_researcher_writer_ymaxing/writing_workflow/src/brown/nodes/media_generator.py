from typing import cast

from langchain_core.language_models import BaseChatModel
from langchain_core.messages import AIMessage
from langchain_core.runnables import Runnable
from loguru import logger

from brown.config_app import get_app_config
from brown.entities.guidelines import ArticleGuideline
from brown.entities.research import Research
from brown.models import FakeModel

from .base import Node, ToolCall, Toolkit

app_config = get_app_config()


class MediaGeneratorOrchestrator(Node):
    system_prompt_template = """You are a Media Generation Orchestrator responsible for analyzing article 
guidelines and research to identify what media items need to be generated for the article.

Your task is to:
1. Carefully analyze the article guideline and research content provided
2. Identify ALL explicit requests for media items (diagrams, charts, visual illustrations, etc.)
3. For each identified media requirement, call the appropriate tool to generate the media item
4. Provide clear, detailed descriptions for each media item based on the guideline requirements and research context

## Analysis Guidelines

**Look for these explicit indicators in the article guideline:**
- Direct mentions: "Render a Mermaid diagram", "Draw a diagram", "Create a visual", "Illustrate with", etc.
- Visual requirements: "diagram visually explaining", "chart showing", "figure depicting", "visual representation"
- Process flows: descriptions of workflows, architectures, data flows, or system interactions
- Structural elements: hierarchies, relationships, or step-by-step processes

**Key places to look:**
- Section requirements and descriptions  
- Specific instructions mentioning visual elements
- Architecture or system descriptions
- Process flows or workflows

## Media Type Decision

Before calling any tool, you must decide whether the requested visual is a **diagram** (call a tool)
or a **comparison table** (do NOT call any tool — leave it for the writer).

**Produce a Markdown table (skip all tools) when the guideline's visualization request involves:**
- A structured comparison of N options or approaches across multiple named attributes
  (e.g., pros, cons, use cases, complexity, trade-offs, features).
  Examples of guideline phrasings that signal a table despite using the word "diagram" or "visual":
  - "visualize / diagram the three approaches" where each approach has explicit pros/cons listed
  - "compare N methods", "summarize the trade-offs", "show the pros and cons of each"
  - "create a summary / overview table of ..."
- The underlying data is inherently 2-dimensional: N rows (items) x M columns (attributes).
  Such data is always clearer as a table than as a graph with nodes and edges.

**Lesson from past failure:** A guideline that said "Provide a mermaid diagram to visualize the
three approaches" (for a section comparing Raw Strings vs. Structured Entities vs. Knowledge
Graph, each with their own Pros/Cons/Use-cases) was incorrectly routed to MermaidDiagramGenerator.
The result was an inferior graph with nested subgraphs reproducing tabular data. The correct output
was a Markdown table (as in the ground truth). When content is a 2D comparison matrix, do not
call any tool — the writer will produce the table inline.

**Produce a Mermaid diagram (call MermaidDiagramGenerator) when the guideline involves:**
- Flows where information or control moves through a sequence of steps or components
- Architectures showing how systems, modules, or layers are connected (e.g., memory layers → retrieval pipeline → reasoning → action)
  retrieval pipeline → reasoning → action)
- Hierarchies or taxonomies (parent→child relationships)
- Decision trees / flowcharts (yes/no branches)
- Interaction sequences between participants
- State transitions
- Entity-relationship structures and class/inheritance diagrams
- Mind maps of concept relationships

## Tool Usage Instructions

You will call multiple tools to generate the media items. You will use the tool that is most appropriate for the media item you are 
generating.

For each identified media requirement:

**When to use MermaidDiagramGenerator:**
- Explicit requests that describe a flow, architecture, hierarchy, sequence, or state machine
  (see "Produce a Mermaid diagram" criteria above)
- Note: the word "diagram" or "mermaid" in the guideline alone is NOT sufficient — first check
  whether the content is 2D tabular comparison data. If it is, skip the tool call entirely.

**Ordering Requirements:**
Call tools in the same order that diagram requests appear in the guideline. Diagrams are
order-sensitive — each is tied to a specific section, and the order determines how they are
referenced in the article.

**Description Requirements:**
When calling tools, provide detailed descriptions that include:
- The specific purpose and context from the article guideline
- Key components that should be included based on the research
- The type of diagram most appropriate (flowchart, sequence, architecture, etc.)
- Specific elements, relationships, or flows to highlight
- Any terminology or technical details from the research
- The exact names, labels, class names, and artifact identifiers mentioned in the guideline.
  Do not substitute equivalent-sounding alternatives (e.g., if the guideline specifies
  `DocumentMetadata`, use that exact name in the description, not a paraphrase).

## Example Analysis Process

1. **Scan the guideline** for phrases like:
   - "Render a Mermaid diagram of..."
   - "Draw a diagram showing..."
   - "Illustrate the architecture..."
   - "Visual representation of..."

2. **For each found requirement:**
   - Extract the specific context and purpose
   - Identify what should be visualized
   - Determine the most appropriate diagram type
   - Craft a detailed description incorporating research insights

3. **Call the appropriate tool** with the comprehensive description

## Input Context

Here is the article guideline:
{article_guideline}

Here is the research:
{research}

## Your Response

Analyze the provided article guideline and research, then call the appropriate tools for each 
identified media item requirement. Each tool call should include a detailed description that ensures 
the generated media item will be relevant, accurate, and valuable for the article's educational goals.

If no explicit media requirements are found in the guideline, respond with: 
"No explicit media item requirements found in the article guideline."
"""

    def __init__(
        self,
        article_guideline: ArticleGuideline,
        research: Research,
        model: Runnable,
        toolkit: Toolkit,
    ) -> None:
        self.article_guideline = article_guideline
        self.research = research

        super().__init__(model, toolkit)

    def _extend_model(self, model: Runnable) -> Runnable:
        model = cast(BaseChatModel, super()._extend_model(model))
        model = model.bind_tools(self.toolkit.get_tools(), tool_choice="auto")

        return model

    async def ainvoke(self) -> list[ToolCall]:
        system_prompt = self.system_prompt_template.format(
            article_guideline=self.article_guideline.to_context(),
            research=self.research.to_context(),
        )
        user_input_content = self.build_user_input_content(inputs=[system_prompt], image_urls=self.research.image_urls)
        inputs = [
            {
                "role": "user",
                "content": user_input_content,
            }
        ]
        response = await self.model.ainvoke(inputs)

        if isinstance(response, AIMessage) and response.tool_calls:
            jobs = cast(list[ToolCall], response.tool_calls)
        else:
            logger.warning(f"No tool calls found in the response. Instead found response of type `{type(response)}`.")
            jobs = []

        return jobs

    def _set_default_model_mocked_responses(self, model: FakeModel) -> FakeModel:
        model.responses = []

        return model
