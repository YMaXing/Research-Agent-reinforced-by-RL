from typing import cast

from langchain_core.language_models import BaseChatModel
from langchain_core.runnables import Runnable
from loguru import logger
from pydantic import BaseModel, Field

from brown.config_app import get_app_config
from brown.entities.exceptions import InvalidOutputTypeException
from brown.entities.media_items import MermaidDiagram
from brown.models import FakeModel

from .base import ToolNode

app_config = get_app_config()


class GeneratedMermaidDiagram(BaseModel):
    content: str = Field(description="The Mermaid diagram code formatted in Markdown format as: ```mermaid\n[diagram content here]\n```")
    caption: str = Field(description="The caption, as a short description of the diagram.")


class MermaidDiagramGenerator(ToolNode):
    prompt_template = """
You are a specialized agent that creates clean, readable Mermaid diagrams from text descriptions.

## Task
Generate a valid Mermaid diagram based on this description:
<description_of_the_diagram>
{description_of_the_diagram}
</description_of_the_diagram>

## Output Format
Return ONLY the Mermaid code block in this exact format:
```mermaid
[diagram content here]
```

## Diagram Types & Examples

### Process Flow / Data Flow (Gold Standard)
Use `flowchart LR` for left-to-right data flows and pipelines. Include ALL major actors
end-to-end — never stop at an intermediate node. Group related components with subgraphs.
Use edge labels to describe the nature of each relationship. Use dotted arrows (`-.->`) for
indirect or supporting relationships. Use `classDef`/`class` to visually differentiate node
groups. Use `%%` comments to annotate sections. Use `<br/>` for multi-line labels.
```mermaid
flowchart LR
  %% External sources
  subgraph Sources["External Sources"]
    DB["Knowledge Base<br/>(Vector DB)"]
    API["External APIs"]
  end

  %% Agent memory
  subgraph Memory["Agent Memory"]
    LTM["Long-Term Memory<br/>(Persistent Storage)"]
    STM["Short-Term Memory<br/>(Context Window)"]
    IK["Internal Knowledge<br/>(Model Weights)"]
  end

  %% Reasoning and output
  subgraph Execution["Reasoning & Action"]
    R["Reasoning Process"]
    ACT["Output / Action<br/>(response or tool call)"]
  end

  %% Primary data flows
  DB -- "ingest" --> LTM
  API -- "fetch" --> LTM
  LTM -- "retrieve" --> STM
  STM --> R
  IK --> R
  R --> ACT

  %% Indirect / supporting relationships
  IK -. "guides retrieval" .-> LTM

  %% Visual grouping
  classDef store stroke-dasharray: 3 3;
  classDef exec stroke-width:2;
  class LTM,STM,IK store;
  class R,ACT exec;
```


### Simple Decision Flowchart
```mermaid
graph TD
    A["Start"] --> B{{"Decision"}}
    B -->|"Yes"| C["Action 1"]
    B -->|"No"| D["Action 2"]
    C --> E["End"]
    D --> E
```

### State Diagrams
```mermaid
stateDiagram-v2
    [*] --> Idle
    Idle --> Processing : "start"
    Processing --> Complete : "finish"
    Complete --> [*]
```

### System Architecture
```mermaid
graph TB
    subgraph "Frontend"
        UI["User Interface"]
    end
    subgraph "Backend"
        API["API Gateway"]
        DB[("Database")]
    end
    UI --> API
    API --> DB
```

### Sequence Diagrams
```mermaid
sequenceDiagram
    participant User
    participant System
    participant Database
    
    User->>System: "Request"
    System->>Database: "Query"
    Database-->>System: "Result"
    System-->>User: "Response"
```

### Mindmaps
```mermaid
mindmap
  root("AI System")
    ("Data Layer")
      ("Raw Data")
      ("Processed Data")
      ("Vector Database")
    ("Model Layer")
      ("LLM")
      ("Embedding Model")
      ("Fine-tuned Model")
    ("Application Layer")
      ("API Gateway")
      ("User Interface")
      ("Authentication")
```

### Tables and relationships between them
```mermaid
erDiagram
    USER {{
        string user_id
        string name
        string email
    }}
    PROJECT {{
        string project_id
        string title
        string description
    }}
    TASK {{
        string task_id
        string title
        string status
    }}
    
    USER ||--o{{ PROJECT : "owns"
    PROJECT ||--o{{ TASK : "contains"
    USER ||--o{{ TASK : "assigned_to"
```

### Class Diagrams
```mermaid
classDiagram
    class BaseModel {{
        +str model_name
        +dict config
        +load_model()
        +predict(input) dict
    }}
    
    class LLMModel {{
        +str tokenizer_path
        +int max_tokens
        +generate_text(prompt) str
        +fine_tune(dataset)
    }}
    
    class EmbeddingModel {{
        +int embedding_dim
        +str architecture
        +encode(text) array
        +similarity(vec1, vec2) float
    }}
    
    BaseModel <|-- LLMModel
    BaseModel <|-- EmbeddingModel
    LLMModel --> EmbeddingModel : "uses"
```

## Syntax Rules
1. **Node Labels**: Use square brackets `[Label]` for rectangular nodes
2. **Decisions**: Use curly braces `{{Decision}}` for diamond shapes  
3. **Databases**: Use `[(Label)]` for cylindrical database shapes
4. **Circles**: Use `((Label))` for circular nodes
5. **Arrows**: Use `-->` for solid arrows, `-.->` for dotted arrows
6. **Labels on Arrows**: Use `-->|Label|` or `-- "label" -->` for labeled connections
7. **Subgraphs**: Use `subgraph "Title"` and `end` to group elements
8. **Comments**: Use `%%` for comments that annotate diagram sections
9. **ERD Entities**: Use `ENTITY_NAME {{ field_type field_name }}` format
10. **ERD Relationships**: Use `||--o{{`, `||--||`, `}}o--||` for different cardinalities
11. **Class Definitions**: Use `class ClassName {{ +type attribute +method() }}` format
12. **Class Relationships**: Use `<|--` (inheritance), `-->` (association), `--*` (composition)
13. **Multi-line Labels**: Use `<br/>` inside labels for a second line of context: `A["Long-Term Memory<br/>(External DB)"]`
14. **Named-edge Arrows**: Prefer `-- "label" -->` over `-->|"label"|` in flowcharts for readability
15. **Node Style Classes**: Use `classDef name properties;` at the bottom to define visual groups, 
    then `class node1,node2 name;` to apply — differentiates related nodes visually

## Formatting Rules
**ALWAYS wrap node labels in double quotes `"..."` to prevent parsing errors:**

**WRONG** (causes parse errors):
```mermaid
graph TD
    A[Vision Encoder (e.g., ViT)] --> B[Output];
```

**CORRECT** (always use quotes):
```mermaid
graph TD
    A["Vision Encoder (e.g., ViT)"] --> B["Output"]
```

**Key formatting requirements:**
- **Always use double quotes** around ALL node labels: `A["Label"]`
- **Never use semicolons** at the end of lines (they're optional and can cause issues)
- **Quote any label** containing: parentheses `()`, commas `,`, periods `.`, colons `:`, or spaces
- **Quote subgraph titles** as well: `subgraph "Title"`

## Styling Guidelines
- **Use default colors only** - do not add color specifications or custom styling
- Do not use `fill:`, `stroke:`, `color:` or any CSS styling properties
- Keep diagrams clean and professional with standard Mermaid appearance
- Focus on structure and clarity, not visual customization

## Key Guidelines
- **Orientation:** Use `flowchart LR` for data flows, pipelines, and processes where information
  moves through stages (most technical diagrams). Use `graph TD` only for vertical hierarchies,
  decision trees, or top-down classification structures. Never default to `graph TD` for flow diagrams.
- **Completeness:** Always include the complete end-to-end flow. If the diagram shows a memory or
  data system, include not just the storage components but also what the data feeds into (reasoning)
  and what that produces (action/output/response). A diagram that stops at an intermediate node is
  incomplete.
- **Subgraph grouping:** Group logically related nodes using `subgraph "Title"` blocks whenever
  2+ nodes belong to the same layer, tier, or category.
- **Edge labels:** Add descriptive labels on arrows to explain the relationship type
  (e.g., `-- "retrieve" -->`, `-- "summarize" -->`, `-- "triggers" -->`). Label all primary flows.
- **Visual differentiation:** Use `classDef` and `class` to distinguish major categories of nodes
  (e.g., storage nodes vs. execution nodes vs. external sources).
- **Multi-line labels:** Use `<br/>` when a label's technical type or role adds important context:
  `A["Long-Term Memory<br/>(External DB)"]`.
- **Indirect relationships:** Use `-.->` with an edge label for supporting, enabling, or indirect
  relationships that are not primary data flows.
- **Comments:** Use `%%` comment lines to label sections of the diagram code.
- Keep node labels concise — avoid special characters outside of quoted strings.
- Choose the appropriate diagram type for the concept being illustrated.

## Common Mistakes to Avoid
- **NEVER use unquoted labels** — always wrap in double quotes: `A["Label"]`
- **NEVER use semicolons** at the end of lines (causes parsing issues)
- **NEVER put parentheses `()` in unquoted labels** — parser treats them as shape tokens
- **NEVER truncate the flow** — a memory/pipeline diagram without a final "Reasoning" and
  "Output/Action" node is incomplete; always follow data to its endpoint
- **NEVER default `graph TD` for data flows** — use `flowchart LR` when information moves
  horizontally through a pipeline or system
- **NEVER omit edge labels on primary flows** — unlabeled arrows leave the diagram semantically
  ambiguous; the reader cannot tell what the relationship means
- **NEVER produce shallow diagrams** — a diagram with only 3–4 nodes for a system with 7+
  meaningful components misses key relationships and provides little value
- Don't create overly complex diagrams with too many connections
- Avoid extremely long labels that break the visual flow
- **Never use custom colors or styling** — stick to Mermaid's default appearance

Generate a clean, professional diagram that clearly illustrates the described concept using only default Mermaid 
styling. Remember: ALWAYS use double quotes around ALL labels and NEVER use semicolons.
"""

    def _extend_model(self, model: Runnable) -> Runnable:
        model = cast(BaseChatModel, super()._extend_model(model))
        model = model.with_structured_output(GeneratedMermaidDiagram, include_raw=False)

        return model

    async def ainvoke(self, description_of_the_diagram: str, section_title: str) -> MermaidDiagram:
        """Specialized tool to generate a mermaid diagram from a text description. This tool uses a specialized LLM to
        convert a natural language description into a mermaid diagram.

        Use this tool when you need to generate a mermaid diagram to explain a concept. Don't confuse mermaid diagrams,
        or diagrams in general, with media data, such as images, videos, audio, etc. Diagrams are rendered dynamically
        customized for each article, while media data are static data added as URLs from external sources.
        This tool is used explicitly to dynamically generate diagrams, not to add media data.

        Args:
            description_of_the_diagram: Natural language description of the diagram to generate.
            section_title: Title of the section that the diagram is for.

        Returns:
            The generated mermaid diagram code in Markdown format.

        Raises:
            Exception: If diagram generation fails.

        Examples:
        >>> description = "A flowchart showing data flowing from user input to database"
        >>> diagram = await generate_mermaid_diagram(description)
        >>> print(diagram)
        ```mermaid
        graph LR
            A[User Input] --> B[Processing]
            B --> C[(Database)]
        ```
        """

        try:
            response = await self.model.ainvoke(
                [
                    {
                        "role": "user",
                        "content": self.prompt_template.format(
                            description_of_the_diagram=description_of_the_diagram,
                        ),
                    }
                ]
            )

        except Exception as e:
            logger.exception(f"Failed to generate Mermaid diagram: {e}")

            return MermaidDiagram(
                location=section_title,
                content=f'```mermaid\ngraph TD\n    A["Error: Failed to generate diagram"]\n    A --> B["{str(e)}"]\n```',
                caption=f"Error: Failed to generate diagram: {str(e)}",
            )

        if not isinstance(response, GeneratedMermaidDiagram):
            raise InvalidOutputTypeException(GeneratedMermaidDiagram, type(response))

        return MermaidDiagram(
            location=section_title,
            content=response.content,
            caption=response.caption,
        )

    def _set_default_model_mocked_responses(self, model: FakeModel) -> FakeModel:
        model.responses = [
            MermaidDiagram(
                location="Mock Section Title",
                content="```mermaid\ngraph TD\n    A[Mock Diagram]\n```",
                caption="Mock Caption",
            ).model_dump_json()
        ]

        return model
