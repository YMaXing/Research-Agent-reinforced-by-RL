"""
Shared fixtures and fake LLM helpers for mcp_server unit tests.

Design notes
------------
* Real LLM calls are expensive and non-deterministic, so every call to
  ``get_chat_model`` is replaced by a *fake* model that returns a fixed,
  pre-configured response.

* ``FakeStructuredModel`` mimics a LangChain model that has had
  ``.with_structured_output(GeneratedQueries)`` applied – its ``ainvoke``
  returns a ``GeneratedQueries`` Pydantic object directly.

* ``RecordingModel`` is the same but also stores the prompt text so that
  tests can assert on what was sent to the (fake) LLM.

* ``FakePlainModel`` mimics an unstructured chat model – its ``ainvoke``
  returns an object with a ``.content`` attribute (like LangChain's
  ``AIMessage``), which is used by the deduplication handler.

Path setup
----------
``mcp_server/`` is inserted into ``sys.path`` so that ``src.*`` packages
are importable without installing the package in editable mode.

``dedup_new_queries_tool.py`` contains a bare (non-relative) import::

    from generate_next_queries_tool import write_queries_to_file

As a work-around we register a mock module under the bare name
``generate_next_queries_tool`` *before* any test file imports the dedup
tool.  Tests that care about file-writing behaviour can either patch that
symbol explicitly or (more commonly) rely on the return-dict assertions
since ``write_queries_to_file`` is exercised independently in
``test_query_helpers.py``.

Required dev dependencies (add to your venv / pyproject.toml):
    pytest>=8
    pytest-asyncio>=0.23
"""

import json
import sys
from pathlib import Path
from typing import Any, List, Tuple
from unittest.mock import MagicMock

import pytest

# ---------------------------------------------------------------------------
# sys.path – must happen before any src.* imports
# ---------------------------------------------------------------------------
_MSERVER_ROOT = Path(__file__).resolve().parent.parent  # .../mcp_server/
if str(_MSERVER_ROOT) not in sys.path:
    sys.path.insert(0, str(_MSERVER_ROOT))

# ---------------------------------------------------------------------------
# Work-around for the bare import in dedup_new_queries_tool.py.
# Register a stub module BEFORE any test file imports the dedup tool so that
#   `from generate_next_queries_tool import write_queries_to_file`
# resolves without error.  Tests that also need the real function can patch
# at the call-site level.
# ---------------------------------------------------------------------------
_mock_gnqt_module = MagicMock()
sys.modules.setdefault("generate_next_queries_tool", _mock_gnqt_module)

# ---------------------------------------------------------------------------
# Package imports (safe now that sys.path is set up)
# ---------------------------------------------------------------------------
from src.models.query_models import GeneratedQueries, QueryAndReason  # noqa: E402

# ---------------------------------------------------------------------------
# Canonical fake query data reused across several test modules
# ---------------------------------------------------------------------------
FAKE_QUERIES_5: List[Tuple[str, str]] = [
    ("What is RAG?", "Covers retrieval basics"),
    ("How does dense retrieval work?", "Technical deep dive"),
    ("What are RAG limitations?", "Critical analysis"),
    ("How does RAG compare to fine-tuning?", "Comparative analysis"),
    ("What are production RAG challenges?", "Real-world perspective"),
]


# ---------------------------------------------------------------------------
# Fake model helpers
# ---------------------------------------------------------------------------

class FakeAIMessage:
    """Minimal stand-in for LangChain's ``AIMessage`` (has ``.content``)."""

    def __init__(self, content: str) -> None:
        self.content = content


class FakeStructuredModel:
    """
    Simulates ``get_chat_model(model_id, GeneratedQueries)`` – a model that
    has been wrapped with ``with_structured_output`` so its ``ainvoke``
    returns a ``GeneratedQueries`` object directly.
    """

    def __init__(self, queries: List[Tuple[str, str]]) -> None:
        self._queries = queries

    def _build_response(self) -> GeneratedQueries:
        return GeneratedQueries(
            queries=[QueryAndReason(question=q, reason=r) for q, r in self._queries]
        )

    async def ainvoke(self, prompt: Any, **kwargs: Any) -> GeneratedQueries:
        return self._build_response()

    def invoke(self, prompt: Any, **kwargs: Any) -> GeneratedQueries:
        return self._build_response()


class RecordingModel:
    """
    Like ``FakeStructuredModel`` but records the last prompt string sent to
    it, enabling assertions on prompt content (e.g. depth/breadth ratios).
    """

    def __init__(self, queries: List[Tuple[str, str]]) -> None:
        self._queries = queries
        self.last_prompt: str = ""

    def _build_response(self) -> GeneratedQueries:
        return GeneratedQueries(
            queries=[QueryAndReason(question=q, reason=r) for q, r in self._queries]
        )

    async def ainvoke(self, prompt: Any, **kwargs: Any) -> GeneratedQueries:
        self.last_prompt = str(prompt)
        return self._build_response()

    def invoke(self, prompt: Any, **kwargs: Any) -> GeneratedQueries:
        self.last_prompt = str(prompt)
        return self._build_response()


class FakePlainModel:
    """
    Simulates ``get_chat_model(model_id)`` without a schema – its
    ``ainvoke`` returns a ``FakeAIMessage`` whose ``.content`` is whatever
    JSON string was supplied at construction time.
    """

    def __init__(self, content: str) -> None:
        self._content = content

    async def ainvoke(self, prompt: Any, **kwargs: Any) -> FakeAIMessage:
        return FakeAIMessage(self._content)

    def invoke(self, prompt: Any, **kwargs: Any) -> FakeAIMessage:
        return FakeAIMessage(self._content)


# ---------------------------------------------------------------------------
# pytest fixtures
# ---------------------------------------------------------------------------

@pytest.fixture
def tmp_research_dir(tmp_path: Path) -> Path:
    """
    A minimal research directory containing ``article_guideline.md``.
    Most tools require this file to exist.
    """
    (tmp_path / "article_guideline.md").write_text(
        "# RAG Systems\n\nExplain retrieval-augmented generation architectures.",
        encoding="utf-8",
    )
    return tmp_path


@pytest.fixture
def fake_structured_model() -> FakeStructuredModel:
    """Returns all 5 fake queries."""
    return FakeStructuredModel(FAKE_QUERIES_5)


@pytest.fixture
def fake_structured_model_few() -> FakeStructuredModel:
    """Returns only 2 queries – fewer than the default ``n_queries=5``."""
    return FakeStructuredModel(FAKE_QUERIES_5[:2])


@pytest.fixture
def fake_plain_model_factory():
    """
    Factory fixture: call it with a JSON string to get a ``FakePlainModel``::

        model = fake_plain_model_factory('{"kept_queries": [...]}')
    """
    def _factory(content: str) -> FakePlainModel:
        return FakePlainModel(content)

    return _factory
