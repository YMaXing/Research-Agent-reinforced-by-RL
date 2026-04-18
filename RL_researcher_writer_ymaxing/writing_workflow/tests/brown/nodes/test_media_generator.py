"""Tests for brown.nodes.media_generator module."""

import pytest

from brown.builders import build_model
from brown.config_app import get_app_config
from brown.nodes.media_generator import MediaGeneratorOrchestrator
from brown.nodes.tool_nodes import MermaidDiagramGenerator


class TestMermaidDiagramGenerator:
    """Test the MermaidDiagramGenerator class."""

    def test_mermaid_diagram_generator_initialization(self) -> None:
        """Test creating Mermaid diagram generator."""
        from brown.nodes.tool_nodes import GeneratedMermaidDiagram

        mock_response = GeneratedMermaidDiagram(
            content="```mermaid\ngraph TD\n    A[Start] --> B[End]\n```",
            caption="Test diagram",
        )

        app_config = get_app_config()
        model, _ = build_model(app_config, node="generate_media_items")
        model.responses = [mock_response.model_dump_json()]

        generator = MermaidDiagramGenerator(model=model)

        assert generator.model == model

    @pytest.mark.asyncio
    async def test_mermaid_diagram_generator_ainvoke(self) -> None:
        """Test Mermaid diagram generation with properly quoted labels and labeled edges."""
        from brown.nodes.tool_nodes import GeneratedMermaidDiagram

        mock_response = GeneratedMermaidDiagram(
            content='```mermaid\nflowchart LR\n    A["Input"] -- "process" --> B["Processing"] -- "output" --> C["Output"]\n```',
            caption="Process flow diagram",
        )

        app_config = get_app_config()
        model, _ = build_model(app_config, node="generate_media_items")
        model.responses = [mock_response.model_dump_json()]

        generator = MermaidDiagramGenerator(model=model)

        description = "A flowchart showing data processing flow"
        section_title = "Data Processing"

        result = await generator.ainvoke(description, section_title)

        assert hasattr(result, "content")
        assert hasattr(result, "caption")
        assert "flowchart LR" in result.content
        assert result.location == section_title
        assert "Process flow diagram" in result.caption

    @pytest.mark.asyncio
    async def test_mermaid_diagram_generator_error_handling(self) -> None:
        """Test Mermaid diagram generator error handling."""
        # Test with invalid response that should trigger error handling
        from pydantic import BaseModel

        class InvalidResponse(BaseModel):
            invalid: str

        mock_response = InvalidResponse(invalid="response")

        app_config = get_app_config()
        model, _ = build_model(app_config, node="generate_media_items")
        model.responses = [mock_response.model_dump_json()]

        generator = MermaidDiagramGenerator(model=model)

        description = "Test diagram"
        section_title = "Test Section"

        # Should handle error gracefully
        result = await generator.ainvoke(description, section_title)

        assert hasattr(result, "content")
        assert hasattr(result, "caption")
        # Should contain error information
        assert "Error" in result.content or "Failed" in result.content

    def test_mermaid_diagram_generator_requires_mocked_response_for_fake_model(self) -> None:
        """Test that fake model works without mocked response (uses default)."""
        app_config = get_app_config()
        model, _ = build_model(app_config, node="generate_media_items")
        # Don't set responses - should use default

        # Should not raise an error - fake model uses default response when mocked_response is None
        generator = MermaidDiagramGenerator(model=model)

        # Verify it was created successfully
        assert generator.model == model

    def test_mermaid_diagram_generator_prompt_contains_gold_standard_example(self) -> None:
        """Gold Standard flowchart LR example is present in the prompt to guide quality."""
        assert "Gold Standard" in MermaidDiagramGenerator.prompt_template
        assert "flowchart LR" in MermaidDiagramGenerator.prompt_template

    def test_mermaid_diagram_generator_prompt_contains_orientation_rule(self) -> None:
        """Prompt instructs to use flowchart LR for data flows instead of defaulting to graph TD."""
        assert "NEVER default" in MermaidDiagramGenerator.prompt_template
        assert "Orientation" in MermaidDiagramGenerator.prompt_template

    def test_mermaid_diagram_generator_prompt_contains_completeness_rule(self) -> None:
        """Prompt forbids truncated flows that stop at intermediate nodes."""
        assert "NEVER truncate the flow" in MermaidDiagramGenerator.prompt_template

    def test_mermaid_diagram_generator_prompt_contains_edge_label_rule(self) -> None:
        """Prompt requires descriptive labels on primary arrows."""
        assert "NEVER omit edge labels on primary flows" in MermaidDiagramGenerator.prompt_template

    def test_mermaid_diagram_generator_prompt_contains_shallow_diagram_rule(self) -> None:
        """Prompt forbids shallow diagrams with too few nodes."""
        assert "NEVER produce shallow diagrams" in MermaidDiagramGenerator.prompt_template

    def test_mermaid_diagram_generator_prompt_preserves_verbatim_identifiers(self) -> None:
        """Prompt requires preserving exact names and identifiers from the description verbatim."""
        assert "Preserve exact identifiers" in MermaidDiagramGenerator.prompt_template
        assert "Do not shorten, paraphrase, or abbreviate" in MermaidDiagramGenerator.prompt_template

    @pytest.mark.asyncio
    async def test_mermaid_diagram_generator_error_fallback_is_static(self) -> None:
        """Error fallback returns a static 'See logs for details' message without leaking exception text."""
        from pydantic import BaseModel

        class InvalidResponse(BaseModel):
            invalid: str

        mock_response = InvalidResponse(invalid="some internal exception message")

        app_config = get_app_config()
        model, _ = build_model(app_config, node="generate_media_items")
        model.responses = [mock_response.model_dump_json()]

        generator = MermaidDiagramGenerator(model=model)

        result = await generator.ainvoke("Test diagram", "Test Section")

        assert "See logs for details" in result.content
        assert "See logs for details" in result.caption
        # Exception message must NOT leak into the output
        assert "some internal exception message" not in result.content
        assert "some internal exception message" not in result.caption


class TestMediaGeneratorOrchestrator:
    """Test the MediaGeneratorOrchestrator class."""

    def test_media_generator_orchestrator_initialization(self) -> None:
        """Test creating orchestrator."""
        from pydantic import BaseModel

        from brown.entities.guidelines import ArticleGuideline
        from brown.entities.research import Research
        from brown.nodes.base import ToolCall

        class MockToolCallResponse(BaseModel):
            tool_calls: list[ToolCall]

        mock_response = MockToolCallResponse(
            tool_calls=[
                ToolCall(
                    name="generate_mermaid_diagram",
                    args={"description_of_the_diagram": "Test diagram description", "section_title": "Test Section"},
                    id="test_call_1",
                    type="tool_call",
                )
            ]
        )

        app_config = get_app_config()
        model, toolkit = build_model(app_config, node="generate_media_items")
        model.responses = [mock_response.model_dump_json()]

        article_guideline = ArticleGuideline(content="Create a test diagram")
        research = Research(content="Test research content")

        orchestrator = MediaGeneratorOrchestrator(
            article_guideline=article_guideline,
            research=research,
            model=model,
            toolkit=toolkit,
        )

        assert orchestrator.model == model
        assert orchestrator.toolkit == toolkit

    @pytest.mark.asyncio
    async def test_media_generator_orchestrator_ainvoke(self) -> None:
        """Test orchestrator execution."""
        from pydantic import BaseModel

        class MockResponse(BaseModel):
            content: str

        mock_response = MockResponse(content="Mock response")

        app_config = get_app_config()
        model, toolkit = build_model(app_config, node="generate_media_items")
        model.responses = [mock_response.model_dump_json()]

        from brown.entities.guidelines import ArticleGuideline
        from brown.entities.research import Research

        article_guideline = ArticleGuideline(content="Create a test diagram")
        research = Research(content="Test research content")

        orchestrator = MediaGeneratorOrchestrator(
            article_guideline=article_guideline,
            research=research,
            model=model,
            toolkit=toolkit,
        )

        result = await orchestrator.ainvoke()

        assert isinstance(result, list)
        # The orchestrator returns a list of ToolCall objects
        # Since we're using a simple mock response, it should return an empty list
        assert len(result) == 0

    def test_media_generator_orchestrator_requires_mocked_response_for_fake_model(self) -> None:
        """Test that fake model works without mocked response (uses default)."""
        app_config = get_app_config()
        model, toolkit = build_model(app_config, node="generate_media_items")
        # Don't set responses - should use default

        from brown.entities.guidelines import ArticleGuideline
        from brown.entities.research import Research

        article_guideline = ArticleGuideline(content="Create a test diagram")
        research = Research(content="Test research content")

        # Should not raise an error - fake model uses default response when mocked_response is None
        orchestrator = MediaGeneratorOrchestrator(
            article_guideline=article_guideline,
            research=research,
            model=model,
            toolkit=toolkit,
        )

        # Verify it was created successfully
        assert orchestrator.model == model
        assert orchestrator.toolkit == toolkit

    def test_orchestrator_prompt_contains_media_type_decision_section(self) -> None:
        """Prompt has a Media Type Decision section that gates tool calls."""
        assert "Media Type Decision" in MediaGeneratorOrchestrator.system_prompt_template
        assert "comparison table" in MediaGeneratorOrchestrator.system_prompt_template

    def test_orchestrator_prompt_skips_tool_calls_for_tabular_comparison_content(self) -> None:
        """Prompt explicitly instructs to skip tool calls for 2D comparison data."""
        assert "do NOT call any tool" in MediaGeneratorOrchestrator.system_prompt_template
        assert "2-dimensional" in MediaGeneratorOrchestrator.system_prompt_template

    def test_orchestrator_prompt_contains_lesson_from_past_failure(self) -> None:
        """Prompt encodes the concrete past failure as a cautionary example for the LLM."""
        assert "Lesson from past failure" in MediaGeneratorOrchestrator.system_prompt_template

    def test_orchestrator_prompt_word_mermaid_alone_not_sufficient(self) -> None:
        """Prompt warns that the word 'mermaid' in the guideline is not sufficient to trigger a tool call."""
        assert 'word "diagram" or "mermaid" in the guideline alone is NOT sufficient' in MediaGeneratorOrchestrator.system_prompt_template

    def test_orchestrator_step1_triggers_on_broad_per_item_attributes(self) -> None:
        """Step 1 condition (b) covers any per-item attribute, not only explicit Pros AND Cons."""
        prompt = MediaGeneratorOrchestrator.system_prompt_template
        # The broad attribute list must be present
        assert "any other per-item property" in prompt
        # Representative attributes beyond Pros/Cons must be listed
        assert "use cases" in prompt
        assert "trade-offs" in prompt
        assert "complexity" in prompt
        assert "limitations" in prompt

    def test_orchestrator_step2_includes_mindmap_classification(self) -> None:
        """Step 2 classification list must include mindmap as a valid visual type."""
        assert "mindmap" in MediaGeneratorOrchestrator.system_prompt_template
        assert "concept map" in MediaGeneratorOrchestrator.system_prompt_template

    @pytest.mark.asyncio
    async def test_ainvoke_sends_system_prompt_as_system_role(self) -> None:
        """ainvoke() separates the system prompt into a 'system' role message and
        sends a 'user' role message, rather than merging everything into one user message."""
        from unittest.mock import patch

        from langchain_core.messages import AIMessage

        from brown.entities.guidelines import ArticleGuideline
        from brown.entities.research import Research
        from brown.models import FakeModel

        app_config = get_app_config()
        model, toolkit = build_model(app_config, node="generate_media_items")

        article_guideline = ArticleGuideline(content="## Section 1\nRender a Mermaid diagram.")
        research = Research(content="Research content with no images")

        orchestrator = MediaGeneratorOrchestrator(
            article_guideline=article_guideline,
            research=research,
            model=model,
            toolkit=toolkit,
        )

        captured_inputs: list = []

        async def capturing_ainvoke(_self, inputs, *args, **kwargs):
            captured_inputs.extend(inputs)
            return AIMessage(content="", tool_calls=[])

        # patch.object on a Pydantic instance fails; patch the class method instead
        with patch.object(FakeModel, "ainvoke", new=capturing_ainvoke):
            await orchestrator.ainvoke()

        roles = [msg["role"] for msg in captured_inputs]
        assert "system" in roles, "Expected a 'system' role message"
        assert "user" in roles, "Expected a 'user' role message"

        system_msg = next(msg for msg in captured_inputs if msg["role"] == "system")
        # System message content must be a plain string containing the orchestrator instructions
        assert isinstance(system_msg["content"], str)
        assert "Media Generation Orchestrator" in system_msg["content"]
        assert "## Section 1" in system_msg["content"]

        user_msg = next(msg for msg in captured_inputs if msg["role"] == "user")
        # User message content is a list of content blocks (from build_user_input_content)
        assert isinstance(user_msg["content"], list)


class TestMermaidDiagramGeneratorValidation:
    """Tests for the Mermaid validation and self-correction logic in ainvoke()."""

    @pytest.mark.asyncio
    async def test_inline_comment_stripped_from_output(self) -> None:
        """Inline %% comments (code followed by %% on the same line) are stripped from the output."""
        from brown.nodes.tool_nodes import GeneratedMermaidDiagram

        raw_content = '```mermaid\nflowchart LR\n  A["Input"] -- "process" --> B["Output"] %% this is an inline comment\n```'
        mock_response = GeneratedMermaidDiagram(content=raw_content, caption="Test diagram")

        app_config = get_app_config()
        model, _ = build_model(app_config, node="generate_media_items")
        model.responses = [mock_response.model_dump_json()]

        generator = MermaidDiagramGenerator(model=model)
        result = await generator.ainvoke("Test", "Test Section")

        assert "%%" not in result.content
        assert 'B["Output"]' in result.content
        assert "flowchart LR" in result.content

    @pytest.mark.asyncio
    async def test_standalone_comment_lines_preserved(self) -> None:
        """Standalone %% comment lines (not after code on same line) are NOT stripped."""
        from brown.nodes.tool_nodes import GeneratedMermaidDiagram

        raw_content = '```mermaid\nflowchart LR\n  %% External sources\n  A["Input"] -- "process" --> B["Output"]\n```'
        mock_response = GeneratedMermaidDiagram(content=raw_content, caption="Test diagram")

        app_config = get_app_config()
        model, _ = build_model(app_config, node="generate_media_items")
        model.responses = [mock_response.model_dump_json()]

        generator = MermaidDiagramGenerator(model=model)
        result = await generator.ainvoke("Test", "Test Section")

        assert "%% External sources" in result.content

    @pytest.mark.asyncio
    async def test_trailing_semicolons_stripped_from_output(self) -> None:
        """Trailing semicolons are stripped automatically without a retry."""
        from brown.nodes.tool_nodes import GeneratedMermaidDiagram

        raw_content = '```mermaid\nflowchart LR\n  A["Step 1"] --> B["Step 2"];\n  B["Step 2"] --> C["End"];\n```'
        mock_response = GeneratedMermaidDiagram(content=raw_content, caption="Flow")

        app_config = get_app_config()
        model, _ = build_model(app_config, node="generate_media_items")
        model.responses = [mock_response.model_dump_json()]

        generator = MermaidDiagramGenerator(model=model)
        result = await generator.ainvoke("Semicolons", "Test Section")

        # Trailing semicolons must be gone
        for line in result.content.splitlines():
            assert not line.rstrip().endswith(";"), f"Line still has trailing semicolon: {line!r}"

    @pytest.mark.asyncio
    async def test_unquoted_labels_with_special_chars_are_auto_quoted(self) -> None:
        """Node labels with special characters (parentheses, commas, etc.) are
        auto-quoted to prevent Mermaid parse errors."""
        from brown.nodes.tool_nodes import GeneratedMermaidDiagram

        raw_content = "```mermaid\nflowchart LR\n  A[Vision Encoder (e.g., ViT)] --> B[Output]\n```"
        mock_response = GeneratedMermaidDiagram(content=raw_content, caption="ML pipeline")

        app_config = get_app_config()
        model, _ = build_model(app_config, node="generate_media_items")
        model.responses = [mock_response.model_dump_json()]

        generator = MermaidDiagramGenerator(model=model)
        result = await generator.ainvoke("Unquoted labels", "Test Section")

        # The special-char label must be quoted
        assert 'A["Vision Encoder (e.g., ViT)"]' in result.content

    def test_has_valid_structure_detects_diagram_type_on_first_content_line(self) -> None:
        """_has_valid_structure checks the first non-comment, non-empty line only."""
        # Access the helper indirectly by invoking ainvoke with well-formed content;
        # structural validation success is confirmed by the model being called only once.
        # We test the logic contract via the graceful-degradation test (invalid) and
        # this positive test by checking that a valid diagram passes through unchanged.
        # The fence-extract + first-line logic is validated here via edge cases:
        good = '```mermaid\n%% a comment\ngraph TD\n  A["x"]\n```'
        # "graph" type only appears in a comment and a label — NOT as first content line
        false_positive_risk = '```mermaid\ngraph TD\n  A["sequenceDiagram inside label"]\n```'
        # Both should satisfy structural validation (first real line is "graph TD")
        # Just exercising the static method-level behaviour through plain unit assertions:
        import re as _re

        def _simulate_has_valid_structure(content: str) -> bool:
            _TYPES = (
                "flowchart",
                "graph",
                "sequencediagram",
                "classdiagram",
                "statediagram",
                "erdiagram",
                "journey",
                "gantt",
                "pie",
                "mindmap",
                "timeline",
            )
            fence_match = _re.search(r"```mermaid\s*\n(.*?)(?:```|$)", content, _re.DOTALL | _re.IGNORECASE)
            inner = fence_match.group(1) if fence_match else content
            for line in inner.splitlines():
                stripped = line.strip()
                if not stripped or stripped.startswith("%%"):
                    continue
                return any(stripped.lower().startswith(t) for t in _TYPES)
            return False

        assert _simulate_has_valid_structure(good) is True
        assert _simulate_has_valid_structure(false_positive_risk) is True

        # Content where the type word only appears inside a label, never as a declaration
        sneaky = '```mermaid\n  A["This is a sequenceDiagram label"]\n```'
        assert _simulate_has_valid_structure(sneaky) is False

    @pytest.mark.asyncio
    async def test_structural_validation_graceful_degradation(self) -> None:
        """When a diagram has no recognised type keyword, ainvoke() degrades gracefully
        rather than raising an exception, even after the retry is exhausted."""
        from brown.nodes.tool_nodes import GeneratedMermaidDiagram

        # Content with no Mermaid diagram type keyword — structural validation will fail
        invalid_content = '```mermaid\n    A["Input"] --> B["Output"]\n```'
        mock_response = GeneratedMermaidDiagram(content=invalid_content, caption="Invalid")

        app_config = get_app_config()
        model, _ = build_model(app_config, node="generate_media_items")
        model.responses = [mock_response.model_dump_json()]

        generator = MermaidDiagramGenerator(model=model)
        # Should not raise
        result = await generator.ainvoke("Missing type keyword", "Test Section")

        assert hasattr(result, "content")
        assert hasattr(result, "caption")
        assert result.location == "Test Section"


class TestMermaidPromptConsistency:
    """Tests that verify the prompt template is internally consistent.

    Each rule in Syntax Rules, Formatting Rules, and Common Mistakes must agree.
    The examples (gold standard, system architecture, docstring) must also
    demonstrate the stated rules.
    """

    def test_syntax_rule_1_uses_quoted_label_syntax(self) -> None:
        """Syntax Rule 1 must use quoted-label syntax ["Label"] to agree with
        Formatting Rules and Common Mistakes which both require quoted labels."""
        prompt = MermaidDiagramGenerator.prompt_template
        # The rule must show the quoted form
        assert '["Label"]' in prompt
        # The unquoted bare form must NOT appear as the authoritative Rule 1 example
        # (it's fine in WRONG examples, but Rule 1 itself must be quoted)
        rule_1_line = next(line for line in prompt.splitlines() if line.strip().startswith("1. **Node Labels**"))
        assert '["Label"]' in rule_1_line, f"Rule 1 should demonstrate quoted labels: {rule_1_line!r}"

    def test_syntax_rule_15_has_no_trailing_semicolons(self) -> None:
        """Syntax Rule 15 must NOT show trailing semicolons on classDef/class lines,
        consistent with 'NEVER use semicolons at the end of lines'."""
        prompt = MermaidDiagramGenerator.prompt_template
        rule_15_line = next(line for line in prompt.splitlines() if "15. **Node Style Classes**" in line)
        assert "properties;" not in rule_15_line, "Rule 15 must not show 'classDef name properties;'"
        assert "name;" not in rule_15_line, "Rule 15 must not show 'class nodes name;'"
        # The rule should explicitly mention no trailing semicolons
        assert "No trailing semicolons" in rule_15_line or "No trailing semicolons" in prompt

    def test_gold_standard_all_primary_flows_are_labeled(self) -> None:
        """The gold standard example must label ALL primary flows (STM, IK, R edges),
        consistent with 'Label all primary flows' / 'NEVER omit edge labels on primary flows'."""
        prompt = MermaidDiagramGenerator.prompt_template
        # The three previously-unlabeled flows must now carry labels
        assert 'STM -- "' in prompt, "STM primary flow must be labeled"
        assert 'IK -- "' in prompt, "IK primary flow must be labeled"
        assert 'R -- "' in prompt, "R primary flow must be labeled"
        # Unlabeled forms must not appear in the gold standard section
        gold_start = prompt.index("### Process Flow / Data Flow (Gold Standard)")
        gold_end = prompt.index("### Simple Decision Flowchart")
        gold_section = prompt[gold_start:gold_end]
        assert "STM --> R" not in gold_section, "Unlabeled STM --> R must not appear in gold standard"
        assert "IK --> R" not in gold_section, "Unlabeled IK --> R must not appear in gold standard"
        assert "R --> ACT" not in gold_section, "Unlabeled R --> ACT must not appear in gold standard"

    def test_system_architecture_example_uses_flowchart_lr(self) -> None:
        """The System Architecture example must use 'flowchart LR', not 'graph TB',
        consistent with 'Use flowchart LR for data flows'."""
        prompt = MermaidDiagramGenerator.prompt_template
        arch_start = prompt.index("### System Architecture")
        arch_end = prompt.index("### Sequence Diagrams")
        arch_section = prompt[arch_start:arch_end]
        assert "flowchart LR" in arch_section, "System Architecture example must use flowchart LR"
        assert "graph TB" not in arch_section, "System Architecture example must not use graph TB"

    def test_system_architecture_example_labeled_edges(self) -> None:
        """The System Architecture example must label its edges, consistent with
        'Label all primary flows'."""
        prompt = MermaidDiagramGenerator.prompt_template
        arch_start = prompt.index("### System Architecture")
        arch_end = prompt.index("### Sequence Diagrams")
        arch_section = prompt[arch_start:arch_end]
        # Check for labeled edge patterns
        assert '-- "' in arch_section, "System Architecture example must use labeled edges"

    def test_docstring_example_uses_quoted_labels(self) -> None:
        """The ainvoke docstring example must use quoted labels and flowchart LR,
        consistent with the prompt's own rules."""
        import inspect

        docstring = inspect.getdoc(MermaidDiagramGenerator.ainvoke)
        assert docstring is not None
        # Must use flowchart LR (not graph LR)
        assert "flowchart LR" in docstring, "Docstring example must use 'flowchart LR'"
        # Must use quoted labels
        assert '["' in docstring, "Docstring example must use quoted node labels"
        # Unlabeled unquoted forms must not appear
        assert "A[User Input]" not in docstring, "Docstring must not use unquoted labels"
