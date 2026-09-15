from brown.evals.metrics.new_user_intent import word_count


def test_em_dash_joined_words_are_split_but_hyphen_compounds_are_not() -> None:
    text = "mindset—questioning everything, and action-at-a-distance stayed one word."
    assert word_count.compute_prose_word_count(text) == 8


def test_stray_punctuation_after_citation_is_not_counted() -> None:
    text = "...of models [[12]](http://x). It is designed..."
    assert word_count.compute_prose_word_count(text) == 5


def test_table_title_is_prose_but_table_rows_are_excluded() -> None:
    text = "Table 1: Decision matrix comparing X and Y\n| Col1 | Col2 |\n|---|---|\n| a | b |\nMore prose after."
    assert word_count.compute_prose_word_count(text) == 11


def test_image_caption_line_is_excluded() -> None:
    text = "Some prose before.\nImage 1: A caption describing the diagram (Source: url)\nMore prose after."
    assert word_count.compute_prose_word_count(text) == 6


def test_fenced_code_and_mermaid_blocks_are_excluded() -> None:
    text = "Prose before.\n```mermaid\ngraph TD\nA-->B\n```\nProse after."
    assert word_count.compute_prose_word_count(text) == 4


def test_untitled_introduction_before_first_h2() -> None:
    article = "# My Title\n\nIntro prose here, two sentences.\n\n## Section One\nBody one.\n\n## References\nref junk"
    sections = word_count.split_into_sections(article)
    assert [title for title, _ in sections] == ["Introduction", "Section One"]
    assert dict(sections)["Introduction"] == "Intro prose here, two sentences."


def test_explicit_introduction_h2_merges_pre_h2_lead_image() -> None:
    article = "# My Title\n\n![lead image](url.png)\n\n## Introduction\nReal intro prose.\n\n## Section Two\nBody two."
    sections = word_count.split_into_sections(article)
    assert [title for title, _ in sections] == ["Introduction", "Section Two"]
    assert "Real intro prose." in dict(sections)["Introduction"]
    assert "lead image" in dict(sections)["Introduction"]


def test_references_section_is_always_excluded() -> None:
    article = "## Section One\nBody one.\n\n## References\n- [1] Some source"
    titles = [title for title, _ in word_count.split_into_sections(article)]
    assert titles == ["Section One"]
