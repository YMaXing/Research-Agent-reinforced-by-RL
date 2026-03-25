"""Unit tests for src/app/notebook_handler.py.

Tests the ``NotebookToMarkdownConverter`` class using synthetic notebook
structures built with ``nbformat`` — no real notebook files needed.
"""

import pytest
import nbformat

from src.app.notebook_handler import NotebookToMarkdownConverter


def _make_notebook(cells=None, title=None):
    """Build a minimal notebook dict accepted by nbformat."""
    nb = nbformat.v4.new_notebook()
    if title:
        nb.metadata["title"] = title
    if cells:
        nb.cells = cells
    return nb


def _make_md_cell(source: str):
    return nbformat.v4.new_markdown_cell(source)


def _make_code_cell(source: str, outputs=None):
    cell = nbformat.v4.new_code_cell(source)
    if outputs:
        cell.outputs = outputs
    return cell


def _make_stream_output(text: str):
    return nbformat.v4.new_output(output_type="stream", name="stdout", text=text)


def _make_display_output(text_plain: str):
    return nbformat.v4.new_output(output_type="display_data", data={"text/plain": text_plain})


def _make_error_output(ename="ValueError", evalue="bad"):
    return nbformat.v4.new_output(output_type="error", ename=ename, evalue=evalue, traceback=["Traceback ..."])


# ---------------------------------------------------------------------------
# NotebookToMarkdownConverter basic conversion
# ---------------------------------------------------------------------------


class TestNotebookToMarkdownConverter:
    def test_empty_notebook(self, tmp_path):
        nb = _make_notebook()
        nb_path = tmp_path / "empty.ipynb"
        nbformat.write(nb, str(nb_path))

        converter = NotebookToMarkdownConverter()
        md = converter.convert_notebook_to_string(nb_path)
        # Should produce something (even if just newlines)
        assert isinstance(md, str)

    def test_markdown_cell_preserved(self, tmp_path):
        nb = _make_notebook(cells=[_make_md_cell("## Hello World")])
        nb_path = tmp_path / "md.ipynb"
        nbformat.write(nb, str(nb_path))

        converter = NotebookToMarkdownConverter()
        md = converter.convert_notebook_to_string(nb_path)
        assert "## Hello World" in md

    def test_code_cell_wrapped_in_fence(self, tmp_path):
        nb = _make_notebook(cells=[_make_code_cell("print('hi')")])
        nb_path = tmp_path / "code.ipynb"
        nbformat.write(nb, str(nb_path))

        converter = NotebookToMarkdownConverter()
        md = converter.convert_notebook_to_string(nb_path)
        assert "```python" in md
        assert "print('hi')" in md
        assert "```" in md

    def test_stream_output_included(self, tmp_path):
        cell = _make_code_cell("print('ok')", outputs=[_make_stream_output("ok\n")])
        nb = _make_notebook(cells=[cell])
        nb_path = tmp_path / "stream.ipynb"
        nbformat.write(nb, str(nb_path))

        converter = NotebookToMarkdownConverter(include_outputs=True)
        md = converter.convert_notebook_to_string(nb_path)
        assert "**Output:**" in md
        assert "ok" in md

    def test_outputs_excluded_when_disabled(self, tmp_path):
        cell = _make_code_cell("x = 1", outputs=[_make_stream_output("1\n")])
        nb = _make_notebook(cells=[cell])
        nb_path = tmp_path / "no_out.ipynb"
        nbformat.write(nb, str(nb_path))

        converter = NotebookToMarkdownConverter(include_outputs=False)
        md = converter.convert_notebook_to_string(nb_path)
        assert "**Output:**" not in md

    def test_error_output_included(self, tmp_path):
        cell = _make_code_cell("1/0", outputs=[_make_error_output("ZeroDivisionError", "division by zero")])
        nb = _make_notebook(cells=[cell])
        nb_path = tmp_path / "err.ipynb"
        nbformat.write(nb, str(nb_path))

        converter = NotebookToMarkdownConverter(include_outputs=True)
        md = converter.convert_notebook_to_string(nb_path)
        assert "**Error:**" in md
        assert "ZeroDivisionError" in md

    def test_title_from_metadata(self, tmp_path):
        nb = _make_notebook(cells=[_make_md_cell("body")], title="My Notebook")
        nb_path = tmp_path / "titled.ipynb"
        nbformat.write(nb, str(nb_path))

        converter = NotebookToMarkdownConverter()
        md = converter.convert_notebook_to_string(nb_path)
        assert "# My Notebook" in md

    def test_metadata_comments_when_enabled(self, tmp_path):
        nb = _make_notebook(cells=[_make_md_cell("body")])
        nb_path = tmp_path / "meta.ipynb"
        nbformat.write(nb, str(nb_path))

        converter = NotebookToMarkdownConverter(include_metadata=True)
        md = converter.convert_notebook_to_string(nb_path)
        assert "<!-- Cell" in md

    def test_file_not_found_raises(self, tmp_path):
        converter = NotebookToMarkdownConverter()
        with pytest.raises(FileNotFoundError):
            converter.convert_notebook_to_string(tmp_path / "nope.ipynb")

    def test_invalid_notebook_raises_value_error(self, tmp_path):
        bad_file = tmp_path / "bad.ipynb"
        bad_file.write_text("NOT JSON", encoding="utf-8")
        converter = NotebookToMarkdownConverter()
        with pytest.raises(ValueError):
            converter.convert_notebook_to_string(bad_file)


# ---------------------------------------------------------------------------
# _clip_text (internal helper, accessed via instance)
# ---------------------------------------------------------------------------


class TestClipText:
    def test_short_text_unchanged(self):
        converter = NotebookToMarkdownConverter()
        assert converter._clip_text("hello", max_length=100) == "hello"

    def test_long_text_clipped(self):
        converter = NotebookToMarkdownConverter()
        result = converter._clip_text("a" * 100, max_length=20)
        assert len(result) == 20
        assert result.endswith("...")
