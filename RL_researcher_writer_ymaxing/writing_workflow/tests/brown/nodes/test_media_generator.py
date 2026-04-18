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
        """Test Mermaid diagram generation."""
        from brown.nodes.tool_nodes import GeneratedMermaidDiagram

        mock_response = GeneratedMermaidDiagram(
            content="```mermaid\ngraph LR\n    A[Input] --> B[Process] --> C[Output]\n```",
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
        assert "graph LR" in result.content
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
