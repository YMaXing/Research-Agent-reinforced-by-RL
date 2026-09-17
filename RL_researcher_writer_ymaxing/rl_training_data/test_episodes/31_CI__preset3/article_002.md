# How to Build a Continuous Integration Pipeline for AI Agents

In previous lessons, we covered agent observability and evaluation-driven development, giving you the visibility to understand agent behavior. We now shift to Continuous Integration (CI): the automated infrastructure that keeps your codebase maintainable and prevents regressions from reaching production. This discipline separates fragile prototypes from production-ready AI systems. With the problem clear, we will define CI in an AI context and introduce the three-tier model that solves these issues.

## What is Continuous Integration?

Continuous Integration (CI) is the practice of frequently merging code changes from multiple developers into a central repository. After each merge, an automated build and test sequence runs to detect integration issues early. This process prevents the classic "it works on my machine" problem by ensuring that all code is validated in a clean, consistent environment [[1]](https://www.atlassian.com/continuous-delivery/continuous-integration).

However, CI for AI agents is fundamentally different from traditional software CI. Traditional CI focuses on deterministic logic, where a given input always produces the same output. Checks typically include compiling code, running linters for style, and executing unit tests that assert exact outcomes [[2]](https://gatling.io/blog/ci-cd-best-practices). CI pipelines built for deterministic software assume that the same input produces the same output, that tests can assert exact matches, and that a passing build means a working system. Autonomous agents violate every one of those assumptions [[3]](https://galileo.ai/blog/continuous-integration-ci-ai-fundamentals). The fundamental shift for AI systems is from code correctness to behavioral correctness as the CI standard. AI agents operate in a world of non-determinism. Their behavior is shaped by probabilistic LLM responses, rapidly evolving prompts, and external data, all of which can introduce variability that breaks traditional testing assumptions [[3]](https://galileo.ai/blog/continuous-integration-ci-ai-fundamentals), [[4]](https://www.guild.ai/glossary/non-deterministic-systems).

Without a CI pipeline tailored for AI agents, teams often fall into three common failure modes.

### Inconsistent Code Formatting

When team members use different formatters or apply styles manually, the codebase becomes a mess of conflicting conventions. This leads to cluttered pull requests where meaningful logic changes are buried under trivial style adjustments, wasting valuable code review time.

### Skipped Local Checks

Under pressure to ship features quickly, developers might forget to run local tests or linters before pushing code. Without automated enforcement, these manual quality gates are easily bypassed, leading to broken builds and a main branch that is frequently in a failed state.

### Non-Deterministic Tests

Writing tests that call live LLM APIs is a source of frequent problems. These tests are slow, expensive, and "flaky." They can pass or fail unpredictably due to the non-deterministic nature of LLMs, even with the temperature set to 0. This unreliability erodes trust in the test suite and slows the entire team down. These tests also miss the most insidious, agent-specific failures, such as tool misuse, context loss, or cascading errors in multi-agent systems [[5]](https://latitude.so/blog/ai-agent-failure-detection-guide), [[6]](https://nimblebrain.ai/why-ai-fails/agent-governance/agent-failure-modes).

To address these challenges, we use a three-tier CI model that balances cost, speed, and reliability.

### Tier 1: Formatting and Linting (Always Run)

These checks are extremely fast, taking only seconds to run, and are free since they do not involve any API calls. They catch syntactic issues and enforce a consistent coding style across the entire project. This tier is identical to what you would find in a traditional software CI pipeline.

### Tier 2: Unit and Integration Tests (Always Run)

This tier verifies the deterministic parts of your agent, such as data parsing, schema validation, and workflow routing. Crucially, all LLM calls are mocked, meaning we replace them with fake, predictable responses. This ensures that tests are fast (typically under a minute), reliable, and free of API costs.

### Tier 3: AI Evaluations (Manual/Release)

This tier is unique to AI systems. It involves running your agent against a curated dataset of inputs to measure its semantic quality on metrics like helpfulness, accuracy, or instruction-following. These evaluations make real LLM calls, making them slow and expensive. We run them selectively, either manually before a major release or after a significant change to a core prompt.![A three-tier CI model for AI agents, showing the flow from commit checks to PR tests and finally to manual/release AI evaluations, with each tier distinctly colored.](https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/6bf41859-7dd2-4a23-9a88-55720f54114e/image/w=1920,quality=90,fit=scale-down)

Image 1: A three-tier CI model for AI agents, showing the flow from commit checks to PR tests and finally to manual/release AI evaluations, with each tier distinctly colored.

This lesson focuses on the CI essentials for building production-ready AI agents. We will not cover comprehensive DevOps topics like Kubernetes or Terraform. Instead, we will teach you the practical, daily techniques that move your agent from a prototype to a maintainable system.

We will cover:

*   Setting up pre-commit hooks to enforce code quality automatically.
*   Configuring Ruff for linting and formatting.
*   Writing unit tests for deterministic agent code with mocked LLM responses.
*   Building a CI pipeline that runs automatically on every change.
*   Using AI evaluations as selective regression tests in CI.

This lesson includes a hands-on notebook where you will practice running formatting checks, linting, and tests on Brown, our writing agent. With the three-tier model established, the fastest feedback comes from running the first tier locally before you even commit code. This is where pre-commit hooks come in.

## Pre-commit Hooks: Automated Local Guardrails

Pre-commit hooks are automated checks that run on your local machine every time you make a commit [[7]](https://pre-commit.com/). They act as the first line of defense, providing immediate feedback and preventing poorly formatted or broken code from ever entering your shared repository. This local enforcement is a powerful way to maintain code quality without relying solely on a remote CI server [[8]](https://blog.gitguardian.com/automated-guard-rails-for-vibe-coding).

The `pre-commit` framework manages these hooks through a simple, declarative YAML file. You define the checks you want to run in a `.pre-commit-config.yaml` file, and the framework handles the installation and execution of the necessary tools. Hooks are typically references to external repositories, which means you can easily leverage community-maintained tools for popular linters and formatters. The framework also creates isolated environments for each hook, so you can use a linter written in Ruby on a Python project without any manual setup.

### Brown’s Pre-commit Configuration

<aside>
💡
You can experiment with the code for this lesson in this [Colab](https://colab.research.google.com/github/louisfb01/agent-course-notebooks/blob/main/notebooks/lesson_31_notebook.ipynb#scrollTo=b30eba1a). Alternatively, you can find the code for this lesson in the notebook for Lesson 31 of the course GitHub repository.
</aside>

In our Brown writing agent, the `.pre-commit-config.yaml` file defines a set of hooks to validate configurations, format files, and lint our Python code.

```yaml
fail_fast: false
repos:
  - repo: https://github.com/abravalheri/validate-pyproject
    rev: v0.24.1
    hooks:
      - id: validate-pyproject
  - repo: https://github.com/pre-commit/mirrors-prettier
    rev: v3.1.0
    hooks:
      - id: prettier
        types_or: [yaml, json5]
  - repo: https://github.com/astral-sh/ruff-pre-commit
    # Ruff version.
    rev: v0.14.6
    hooks:
      # Run the linter.
      - id: ruff-check
        args: [--fix, --exit-non-zero-on-fix]
      # Run the formatter.
      - id: ruff-format
```

Let's walk through each hook:

*   **`validate-pyproject`**: This tool validates that your `pyproject.toml` file is structurally correct according to PEP standards. A malformed `pyproject.toml` can break your entire build and dependency management process, so this check is a simple but important safeguard.
*   **`prettier`**: A popular code formatter that we use to ensure our configuration files, like YAML and JSON, have a consistent style. This keeps our project's configuration readable and reduces merge conflicts caused by stylistic differences.
*   **`ruff-check` and `ruff-format`**: These hooks run Ruff, a modern Python linter and formatter that we will explore in the next section. The `--fix` argument automatically corrects any fixable issues, and `--exit-non-zero-on-fix` ensures the hook fails even after auto-fixing. This forces you to review the changes made by the tool, stage them, and commit again. As recommended by Ruff’s authors, `ruff-check` runs before `ruff-format`.

### Setting Up Pre-commit

In the `lessons/writing_workflow` repo, or any repository where you have configured your `.pre-commit-config.yaml` file, you can set up pre-commit hooks with these commands.

```bash
# Install dependencies (includes pre-commit)
uv sync --dev

# Install the Git hooks
pre-commit install
```

The `pre-commit install` command creates a Git hook at `.git/hooks/pre-commit`. Now, every time you run `git commit`, these hooks will execute automatically. You can also run them manually on all files at any time.

```bash
# Run all hooks on all files
make pre-commit
```

The daily workflow is straightforward: you make your code changes, stage them with `git add`, and then run `git commit`. If any hooks fail, you review the errors, fix them (often automatically), re-stage the modified files, and commit again. This tight feedback loop is what makes pre-commit so effective. Pre-commit hooks often rely on fast tools like Ruff to do the actual work. Next, we will examine Ruff in depth and show how to configure it.

## Ruff: Fast Python Linting and Formatting

Ruff is an extremely fast Python linter and formatter written in Rust. It serves as a consolidated replacement for a whole suite of older tools like Black, isort, Flake8, and pydocstyle, often delivering sub-second performance even on large codebases [[9]](https://docs.astral.sh/ruff). This speed makes it ideal for both local pre-commit hooks and CI pipelines, as it provides near-instantaneous feedback. By combining more than ten legacy tools into a single binary, Ruff also eliminates the version conflicts and dependency headaches that plagued older Python tooling setups.

It is important to distinguish between formatting and linting:

*   **Formatting** automatically rewrites your code to follow a consistent and opinionated style. It handles things like line length, indentation, and quote style, eliminating debates over minor stylistic preferences.
*   **Linting** analyzes your code for potential bugs, violations of best practices, and other quality issues. This includes flagging unused variables, missing imports, or unnecessarily complex code.

### Brown’s Ruff Configuration

Ruff is configured in the `[tool.ruff]` section of our `pyproject.toml` file. This centralizes the configuration for both the linter and the formatter, which is a key benefit of modern Python tooling [[10]](https://betterstack.com/community/guides/scaling-python/pyproject-explained/).

```toml
[tool.ruff]
target-version = "py312"
line-length = 140

[tool.ruff.lint]
select = [
    "F",    # Pyflakes
    "E",    # pycodestyle errors
    "I",    # isort
]

[tool.ruff.lint.isort]
known-first-party = ["src", "tests"]
```

Here is what each key does:

*   `target-version = "py312"` tells Ruff to enforce rules compatible with Python 3.12 syntax.
*   `line-length = 140` sets the maximum line length, a common formatting rule.
*   `select = ["F", "E", "I"]` enables specific rule sets. `F` (Pyflakes) catches common bugs like undefined names, `E` (pycodestyle) enforces PEP 8 style guidelines, and `I` (isort) organizes and formats imports.
*   `known-first-party = ["src", "tests"]` helps isort correctly group our project's internal imports separately from third-party libraries.

To make running these checks easier, our `Makefile` provides several convenience commands.

```makefile
# --- Tests & QA ---

tests: # Run tests.
	CONFIG_FILE=configs/debug.yaml uv run pytest

pre-commit: # Run pre-commit hooks.
	uv run pre-commit run --all-files

format-fix: # Auto-format Python code using ruff formatter.
	uv run ruff format $(QA_FOLDERS)

lint-fix: # Auto-fix linting issues using ruff linter.
	uv run ruff check --fix $(QA_FOLDERS)

format-check: # Check code formatting without making changes using ruff formatter.
	uv run ruff format --check $(QA_FOLDERS) 

lint-check: # Check code for linting issues without fixing them using ruff linter.
	uv run ruff check $(QA_FOLDERS)
```

Each target uses `uv run` to execute commands within the project’s virtual environment. This is managed automatically by `uv` and does not require manual activation. You can run these from the `writing_workflow/` directory to check or fix your code before committing.

### Hands-On Example: Fixing Formatting Issues

Let's see Ruff's formatter in action.

1.  First, we create a Python file with several formatting issues.
    ```bash
    # Create a Python file with various formatting issues
    cat > test_formatting.py << 'EOF'
    # This file has formatting issues
    def  badly_formatted_function(x,y,z):
        result=x+y+z
        my_list=[1,2,3,4,5,6,7,8,9,10]
        my_dict={"key1":"value1","key2":"value2","key3":"value3"}
        if result>10:
            print("Result is greater than 10")
        else:
            print("Result is 10 or less")
        return result
    
    class   BadlyFormattedClass:
        def __init__(self,name,age):
            self.name=name
            self.age=age
        def get_info(self):
            return f"{self.name} is {self.age} years old"
    EOF
    
    echo "Created test_formatting.py"
    ```
    It outputs:
    ```text
    Created test_formatting.py
    ```
2.  Next, we run the format checker. The `--check` flag tells Ruff to report issues without modifying the file.
    ```bash
    uv run ruff format --check test_formatting.py
    ```
    It outputs:
    ```text
    Would reformat: test_formatting.py
    1 file would be reformatted
    ```
3.  Now, we fix the issues automatically by running the command without the `--check` flag.
    ```bash
    uv run ruff format test_formatting.py
    ```
    It outputs:
    ```text
    1 file reformatted
    ```
4.  The file is now perfectly formatted, with consistent spacing and structure.
    ```bash
    cat test_formatting.py
    ```
    It outputs:
    ```text
    # This file has formatting issues
    def badly_formatted_function(x, y, z):
        result = x + y + z
        my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        my_dict = {"key1": "value1", "key2": "value2", "key3": "value3"}
        if result > 10:
            print("Result is greater than 10")
        else:
            print("Result is 10 or less")
        return result
    
    
    class BadlyFormattedClass:
        def __init__(self, name, age):
            self.name = name
            self.age = age
    
        def get_info(self):
            return f"{self.name} is {self.age} years old"
    ```

### Hands-On Example: Fixing Linting Issues

Now let's try the linter.

1.  We create a file with several linting errors, including unused imports and an undefined variable.
    ```bash
    cat > test_linting.py << 'EOF'
    import os
    import sys
    import json # Unused import
    
    def calculate_sum(numbers):
        """Calculate sum of numbers."""
        total = 0
        for num in numbers:
            total = total + num
        return total
    
    def process_data(data):
        """Process some data."""
        result = calculate_sum(data)
        print(f"Result: {result}")
        _ = os.getcwd()  # Use os
        _ = sys.argv[0]  # Use sys
        undefined_variable = some_undefined_function()  # Using undefined name
        return result
    
    import sys # Duplicate import
    EOF
    
    echo "Created test_linting.py"
    ```
    It outputs:
    ```text
    Created test_linting.py
    ```
2.  Running the linter reveals all the issues, from unused imports to undefined names.
    ```bash
    uv run ruff check test_linting.py
    ```
    It outputs:
    ```text
    I001 [*] Import block is un-sorted or un-formatted
     --> test_linting.py:1:1
      |
    1 | / import os
    2 | | import sys
    3 | | import json # Unused import
      | |___________^
    4 |
    5 |   def calculate_sum(numbers):
      |
    help: Organize imports
    
    F401 [*] `json` imported but unused
     --> test_linting.py:3:8
      |
    1 | import os
    2 | import sys
    3 | import json # Unused import
      |        ^^^^
    4 |
    5 | def calculate_sum(numbers):
      |
    help: Remove unused import: `json`
    
    F841 Local variable `undefined_variable` is assigned to but never used
      --> test_linting.py:18:5
       |
    16 |     _ = os.getcwd()  # Use os
    17 |     _ = sys.argv[0]  # Use sys
    18 |     undefined_variable = some_undefined_function()  # Using undefined name
       |     ^^^^^^^^^^^^^^^^^^
    19 |     return result
       |
    help: Remove assignment to unused variable `undefined_variable`
    
    F821 Undefined name `some_undefined_function`
      --> test_linting.py:18:26
       |
    16 |     _ = os.getcwd()  # Use os
    17 |     _ = sys.argv[0]  # Use sys
    18 |     undefined_variable = some_undefined_function()  # Using undefined name
       |                          ^^^^^^^^^^^^^^^^^^^^^^^
    19 |     return result
       |
    
    E402 Module level import not at top of file
      --> test_linting.py:21:1
       |
    19 |     return result
    20 |
    21 | import sys # Duplicate import
       | ^^^^^^^^^^
       |
    
    I001 [*] Import block is un-sorted or un-formatted
      --> test_linting.py:21:1
       |
    19 |     return result
    20 |
    21 | import sys # Duplicate import
       | ^^^^^^^^^^
       |
    help: Organize imports
    
    F811 [*] Redefinition of unused `sys` from line 2
      --> test_linting.py:21:8
       |
    19 |     return result
    20 |
    21 | import sys # Duplicate import
       |        ^^^ `sys` redefined here
       |
      ::: test_linting.py:2:8
       |
     1 | import os
     2 | import sys
       |        --- previous definition of `sys` here
     3 | import json # Unused import
       |
    help: Remove definition: `sys`
    
    Found 7 errors.
    [*] 4 fixable with the `--fix` option (1 hidden fix can be enabled with the `--unsafe-fixes` option).
    ```
3.  Using the `--fix` flag, Ruff automatically corrects the import-related issues.
    ```bash
    uv run ruff check --fix test_linting.py
    ```
    It outputs:
    ```text
    F841 Local variable `undefined_variable` is assigned to but never used
      --> test_linting.py:18:5
       |
    16 |     _ = os.getcwd()  # Use os
    17 |     _ = sys.argv[0]  # Use sys
    18 |     undefined_variable = some_undefined_function()  # Using undefined name
       |     ^^^^^^^^^^^^^^^^^^
    19 |     return result
       |
    help: Remove assignment to unused variable `undefined_variable`
    
    F821 Undefined name `some_undefined_function`
      --> test_linting.py:18:26
       |
    16 |     _ = os.getcwd()  # Use os
    17 |     _ = sys.argv[0]  # Use sys
    18 |     undefined_variable = some_undefined_function()  # Using undefined name
       |                          ^^^^^^^^^^^^^^^^^^^^^^^
    19 |     return result
       |
    
    Found 5 errors (3 fixed, 2 remaining).
    No fixes available (1 hidden fix can be enabled with the `--unsafe-fixes` option).
    ```
4.  The file now has cleaned-up imports, but the logical error (the undefined function) remains, requiring manual intervention.
    ```bash
    cat test_linting.py
    ```
    It outputs:
    ```text
    import os
    import sys
    
    
    def calculate_sum(numbers):
        """Calculate sum of numbers."""
        total = 0
        for num in numbers:
            total = total + num
        return total
    
    def process_data(data):
        """Process some data."""
        result = calculate_sum(data)
        print(f"Result: {result}")
        _ = os.getcwd()  # Use os
        _ = sys.argv[0]  # Use sys
        undefined_variable = some_undefined_function()  # Using undefined name
        return result
    ```

Once these formatting and linting guardrails are in place, we can turn our attention to verifying the deterministic logic inside the agent nodes, which is the role of unit tests.

## Unit Tests for Agent Repos

The core challenge in testing AI agents is the non-determinism of LLMs. Making real API calls in your tests makes them slow, expensive, and flaky, as identical prompts can yield different outputs or even hit rate limits [[4]](https://www.guild.ai/glossary/non-deterministic-systems). This unpredictability makes it impossible to write reliable assertions.

Unit tests solve this problem by focusing on the deterministic logic within your agent. This includes verifying components that do not require live LLM calls, such as [[11]](https://www.guild.ai/glossary/unit-testing-ai-agents):

*   **Parsing and rendering:** Does your markdown loader correctly extract articles and guidelines?
*   **Schema validation:** Does your Pydantic model reject invalid data structures?
*   **Routing decisions:** Given a specific state, does your agent's workflow route to the correct node?
*   **Utilities:** Do helper functions for text cleaning or URL extraction work as expected?

### Unit Tests vs. Integration Tests

In traditional software engineering, **unit tests** verify individual functions or classes in isolation, while **integration tests** check that multiple components work together correctly. With AI agents, this distinction can become blurry. A single agent node often combines several responsibilities, such as prompt templating, structured output parsing, and routing logic. This complexity means that even a "unit" test for a single node might feel like a small integration test.

We take a pragmatic approach: if a test runs quickly, uses mocked dependencies to avoid network calls, and verifies deterministic logic, we consider it a unit test [[12]](https://docs.langchain.com/oss/python/langchain/test). This allows us to test meaningful chunks of our agent's behavior without getting bogged down in strict definitions. The key is that agent tests should be deterministic by mocking the LLM layer while testing everything else with real implementations [[13]](https://oneuptime.com/blog/post/2026-01-30-agent-testing/view).

To isolate our tests from the non-deterministic LLM, we use a technique called mocking. The most effective strategy for AI agents is response injection, where we provide a fake model with a pre-scripted list of responses. This gives us full control over the LLM's output in a test environment.

<aside>
💡
Another option to mock LLM calls in tests is HTTP mocking, where you intercept API requests and return canned responses using libraries like `responses` or `httpretty`. Some teams prefer fixture-based mocking with `pytest` fixtures and `unittest.mock.patch` to replace LLM calls with fixed outputs. There is also record and replay, which captures real API responses once using tools like `VCR.py` and then replays them in subsequent test runs [[14]](https://agiflow.io/blog/effective-practices-for-mocking-llm-responses-during-the-software-development-lifecycle).
</aside>

### Our Implementation: The FakeModel Pattern

In our Brown agent, we implement response injection using a `FakeModel` class that is compatible with LangChain’s interface. This pattern consists of three parts:

1.  **Configuration specifies the fake model:** The `debug.yaml` configuration at `lessons/writing_workflow/configs/debug.yaml` sets all nodes to use `model_id: “fake`”.
2.  **Model factory returns FakeModel:** The model builder in `src/brown/models/get_model.py` checks the configuration and returns an instance of our `FakeModel` class.
3.  **Tests inject specific responses:** The `FakeModel` in `src/brown/models/fake_model.py` extends LangChain’s `FakeListChatModel` and allows tests to inject a list of responses to be returned sequentially.

Here is the implementation of our `FakeModel` class.

```python
class FakeModel(FakeListChatModel):
    def __init__(self, responses: list[str]) -> None:
        super().__init__(responses=responses)

        self._structured_output_type: Type[Any] | None = None
        self._include_raw: bool = False

    ...

    async def ainvoke(self, inputs, *args, **kwargs) -> Any:
        if len(self.responses) == 0:
            return []

        if self._structured_output_type is not None:
            # For structured output, we need to handle the mocked response directly
            # without going through the parent's ainvoke method which creates AIMessage
            response_content = self.responses[0]

            if isinstance(response_content, dict):
                structured_response = self._structured_output_type(**response_content)
            elif isinstance(response_content, str):
                try:
                    data = json.loads(response_content)
                    structured_response = self._structured_output_type(**data)
                except Exception:
                    logger.warning(f"Failed to parse response as JSON: {response_content}")
                    raise ValueError(f"Failed to parse response as JSON: {response_content}")
            else:
                raise NotImplementedError(f"Unsupported response type: {type(response_content)}")

            if self._include_raw:
                # For raw output, we still need to create a proper AIMessage
                from langchain_core.messages import AIMessage

                raw_message = AIMessage(content=response_content)
                return {
                    "parsed": structured_response,
                    "raw": raw_message,
                }
            else:
                return structured_response

        # For non-structured output, use the parent's implementation
        response = await super().ainvoke(inputs, *args, **kwargs)
        return response
```

An instance of the `FakeModel` class takes a list of pre-scripted responses in its constructor. When its `ainvoke()` method is called, it returns the next response from the list and consumes it. The implementation is slightly more complex to handle both regular and structured outputs, but the core idea remains simple. This design ensures that all unit tests run with a fake model by default, and individual tests can inject specific, predictable responses when needed.

### Example: Testing Nodes with Mocked Responses

When testing nodes that call LLMs, you can mock the responses to ensure deterministic behavior. Here is an example test from `lessons/writing_workflow/tests/brown/nodes/test_article_writer.py`.

```python
@pytest.mark.asyncio
async def test_article_writer_ainvoke_success(
    # ... pytest fixtures for mock data
) -> None:
    """Test article generation with mocked response."""
    mock_response = '{"content": "# Generated Article..."}'

    app_config = get_app_config()
    model, _ = build_model(app_config, node="write_article")
    model.responses = [mock_response]

    writer = ArticleWriter(
        # ... inject dependencies
        model=model,
    )

    result = await writer.ainvoke()

    assert isinstance(result, Article)
    assert "# Generated Article" in result.content
```

The test first defines a mock JSON response. It then builds a fake model and injects the mock response into it. Finally, it instantiates the `ArticleWriter` node with the fake model and asserts that the output is correct. This pattern keeps our tests fast, deterministic, and free, giving us confidence that our agent's logic is correct without the flakiness of actual LLM calls.

### Running Brown’s Tests

To run the entire test suite for Brown, you can use the `make tests` command from the `writing_workflow/` directory.

```bash
# From the writing_workflow directory
make tests
```

This command runs `CONFIG_FILE=configs/debug.yaml uv run pytest`. The `CONFIG_FILE` environment variable ensures that all tests use the `debug.yaml` configuration, which specifies the use of fake models and prevents any real LLM API calls.

Local tests and hooks provide fast feedback, but true enforcement at the repository level requires automated CI workflows that run on every pull request.

## CI Workflows: Automated Enforcement

GitHub Actions is our CI platform of choice for both the Brown and Nova agents. It allows us to define automated workflows that trigger on events like pull requests or pushes to the main branch. These workflows run in isolated environments, support matrix builds for testing across different platforms, and can execute jobs in parallel to provide fast feedback [[15]](https://dev.to/cicube/how-to-run-jobs-in-parallel-with-github-actions-4png).

### Our Complete CI Configuration

Our entire CI configuration is defined in a single file at `.github/workflows/ci.yml`.

```yaml
name: CI
on:
  pull_request:
    branches: [main, dev]
  push:
    branches: [main]

env:
  QA_FOLDERS: "src/brown src/nova scripts/ tests/"

jobs:
  qa:
    runs-on: ubuntu-latest
    steps:
      - name: 🛎️ Checkout
        uses: actions/checkout@v4

      - name: 📦 Install uv
        uses: astral-sh/setup-uv@v4

      - name: 🐍 Set up Python
        uses: actions/setup-python@v5
        with:
          python-version-file: ".python-version"

      - name: 🦾 Install the project
        run: |
          uv sync --dev

      - name: 💅 Format Check
        run: |
          uv run ruff format --check $QA_FOLDERS

      - name: 🔎 Lint Check
        run: uv run ruff check $QA_FOLDERS

  tests:
    runs-on: ubuntu-latest
    steps:
      - name: 🛎️ Checkout
        uses: actions/checkout@v4

      - name: 📦 Install uv
        uses: astral-sh/setup-uv@v4

      - name: 🐍 Set up Python
        uses: actions/setup-python@v5
        with:
          python-version-file: ".python-version"

      - name: 🦾 Install the project
        run: |
          uv sync

      - name: 🧪 Run tests
        run: |
          CONFIG_FILE=configs/debug.yaml uv run pytest
```

This configuration specifies that the workflow should run on any pull request targeting the `main` or `dev` branches, as well as on any direct pushes to `main`. This ensures every code change is validated. The `QA_FOLDERS` environment variable lists all directories to be checked, allowing us to use the same CI setup for both agents in our monorepo.

### Understanding the Job Structure

The workflow defines two independent jobs, `qa` and `tests`, that run in parallel. This separation provides clearer and faster feedback. If a formatting check fails, you immediately see "QA job failed" without having to wait for the entire test suite to run.

Each job runs on an `ubuntu-latest` virtual machine provided by GitHub and is completely isolated. The `qa` job focuses on code quality. It checks out the code using `actions/checkout@v4`, then installs `uv` using `astral-sh/setup-uv@v4`. The Python setup step uses `actions/setup-python@v5` and reads the Python version from your `.python-version` file, ensuring consistency between local development and CI. After syncing dependencies with `uv sync --dev` (which includes development dependencies needed for formatting and linting), it runs two checks. The format check uses `uv run ruff format --check` to verify that all code follows consistent formatting rules without modifying any files. The lint check uses `uv run ruff check` to detect code quality issues, unused imports, and potential bugs.

The `tests` job follows a similar setup but installs only the production dependencies with `uv sync`. It then runs the test suite using `CONFIG_FILE=configs/debug.yaml uv run pytest`. This ensures that all tests execute with our fake model configuration, preventing any real LLM API calls and keeping the CI pipeline fast, deterministic, and free.

### Setting Up GitHub Actions for Your Repository

To enable this CI workflow in your repository, you need to create the workflow file in the correct location. GitHub Actions looks for workflow files in the `.github/workflows/` directory at the root of your repository.

First, create the directory structure if it does not already exist. From your repository root, run `mkdir -p .github/workflows`. Then create the file `.github/workflows/ci.yml` and paste the complete configuration shown above. Make sure your repository has a `.python-version` file at the root that specifies which Python version to use, such as `3.12`. You should also ensure that `configs/debug.yaml` exists and configures your agents to use fake models for testing.

Once you commit and push this file to GitHub, the workflow becomes active immediately. You do not need to configure anything in the GitHub UI for basic workflows, though you will need to add secrets for more advanced scenarios, such as API keys for evaluation workflows.

### Running the Pipeline and Observing Results

The pipeline runs automatically whenever its trigger conditions are met. When you push a commit directly to the `main` branch, GitHub Actions executes the workflow within seconds. When you open a pull request targeting `main` or `dev`, the workflow runs automatically and reports its status on the pull request page.

You can also trigger the workflow manually to test changes or re-run failed checks. Navigate to your repository on GitHub and click the “Actions” tab at the top. You will see a list of all your workflows. Click on “CI” to view all runs of this workflow. In the top right corner, you will see a “Run workflow” button. Click it, select the branch you want to run the workflow on, and click the green “Run workflow” button. This is particularly useful when you want to verify that a fix works without creating a new commit or pull request.

To monitor a workflow run, click any run in the list to view its details. The interface shows both jobs (`qa` and `tests`) with their current status. You can click each job to view the output of its individual steps. If a step fails, its output is expanded automatically and highlighted in red, making it easy to identify the problem. The format and lint checks show exactly which files have issues and what needs to be fixed.

### Interpreting CI Results and Fixing Issues

When the CI pipeline runs, it produces one of three outcomes for each job: success (green checkmark), failure (red X), or in progress (yellow dot). GitHub also displays the overall status on your pull request, preventing merges when checks fail.

If the `qa` job fails due to formatting, the output shows which files would be reformatted and exactly what changes Ruff would make to them. You can fix this locally by running `make format-fix` from the `writing_workflow/` directory, then committing and pushing the formatted code. If the `qa` job fails on linting, the output lists each violation with its file location, line number, and error code. Many of these can be auto-fixed by running `make lint-fix` locally.

If the `tests` job fails, the pytest output shows which test failed and why. The traceback helps you identify the issue, whether it is a logic error, an incorrect mock response, or a missing dependency. You should fix the underlying issue, verify the fix by running `make tests` locally, then push your changes.

A critical principle is that CI should run the exact same commands you run locally. The `qa` job executes `uv run ruff format --check` and `uv run ruff check`, which are identical to the targets your Makefile runs. The `tests` job runs `CONFIG_FILE=configs/debug.yaml uv run pytest`, which is exactly what `make tests` does. This eliminates “works on my machine” problems. If tests pass locally with `make tests`, they will pass in CI, and if they fail in CI, you can reproduce the failure locally by running the same command.

### Trying It Out

The best way to understand how CI works is to intentionally trigger a failure and observe the results. Try introducing a formatting violation by creating a file with inconsistent spacing, committing it, and pushing to a branch. Open a pull request and watch the `qa` job fail with clear output showing what needs to be fixed. Then run `make format-fix` locally, commit the corrected code, and push again. The CI pipeline will re-run automatically, and this time the checks will pass.

You can also experiment with the manual trigger feature. Go to the Actions tab, run the workflow on your current branch, and observe how the jobs execute. This hands-on experience will make the abstract concept of CI concrete and help you develop confidence in the system.

The first two tiers run on every commit, but semantic quality requires a more expensive third tier. This is where AI evaluations enter as selective regression tests.

## AI Evaluations as Regression Tests

AI evaluations are essential for catching semantic quality regressions, such as a decline in helpfulness or an increase in hallucinations, which deterministic unit tests cannot detect [[12]](https://kinde.com/learn/ai-for-software-engineering/ai-devops/ci-cd-for-evals-running-prompt-and-agent-regression-tests-in-github-actions). This practice, often called "golden flow validation," involves benchmarking every build against a representative set of interactions and known failure modes [[3]](https://galileo.ai/blog/continuous-integration-ci-ai-fundamentals). These evaluations form the third tier of our CI model, a quality gate unique to AI systems.

### Why AI Evals Are Unique to AI Systems

AI evaluations are treated as a special, Tier 3 gate because they are expensive. Each run involves real LLM calls, which incur both latency and monetary costs. For example, running an evaluation on a 500-example dataset where each run consumes about 500 tokens would total 250,000 tokens. At a rate of $0.01 per 1,000 tokens, a single full run would cost roughly $2.50. Running this on every commit would quickly become impractical [[13]](https://www.digitalapplied.com/blog/88-percent-ai-agents-never-reach-production-failure-framework). Therefore, we run these evaluations selectively.

### Manual-Trigger CI Workflow for AI Evals

To control costs and run evaluations deliberately, we use a separate GitHub Actions workflow that is triggered manually. This workflow, defined in `.github/workflows/eval.yml`, is never run automatically on commits or pull requests.

```yaml
name: AI Evaluations

on:
  workflow_dispatch:  # Manual trigger only

jobs:
  evaluate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: astral-sh/setup-uv@v4
      - uses: actions/setup-python@v5
        with:
          python-version-file: ".python-version"
      - run: uv sync
      - name: Run evaluations
        env:
          LLM_API_KEY: ${{ secrets.LLM_API_KEY }}
        run: |
          # Replace with your actual evaluation script from previous lessons
          # Example: CONFIG_FILE=./configs/production.yaml python -m scripts.run_eval
          CONFIG_FILE=./configs/production.yaml python -m scripts.run_eval
```

This workflow differs from our main CI pipeline because the `workflow_dispatch` trigger ensures it only runs when manually initiated from the GitHub Actions tab, preventing expensive API calls on every commit. It also uses a production configuration (`configs/production.yaml`) to call real LLM models, unlike our tests which use fake models. The `LLM_API_KEY` is securely passed from GitHub Secrets, which you can configure in your repository settings. The evaluation command itself points to the script that runs your agent against a dataset and computes quality metrics, using frameworks like Opik or LangSmith.

To trigger this workflow, you navigate to the "Actions" tab, select "AI Evaluations," click "Run workflow," choose your branch, and confirm. The results and logs will be available in the Actions interface.

The frequency of running these evaluations depends on your project's maturity:

*   **Early development:** Run evaluations manually on a weekly basis or after major architectural changes to track progress.
*   **Active development:** Run them before merging significant feature branches to catch any regressions you may have introduced. Some teams adopt a two-part strategy: running a small set of critical evaluations on every pull request and a more comprehensive suite nightly [[14]](https://developers.redhat.com/articles/2026/05/18/ci-cd-delivery-agentic-ai).
*   **Mature product:** Integrate them into your formal release process to ensure that production quality never degrades. A best practice is to automatically convert production failures into new evaluation cases, continuously hardening your test suite [[15]](https://www.braintrust.dev/articles/best-ai-evaluation-tools-2026).

With all three tiers of our CI model understood, we can now assemble them into a cohesive daily development workflow.

## Daily Development Workflow

With these tools in place, your daily development workflow becomes a streamlined, quality-driven cycle. You start by writing code and its corresponding unit tests. As you work, you can periodically run quick local checks like `make lint-check` and `make format-check`. After making any logic changes, you run the full test suite with `make tests`. Once you are ready, you commit your changes, and the pre-commit hooks run automatically as a final local check. When you push your code and open a pull request, the main CI workflow runs, enforcing all checks remotely. Finally, before a major release, you manually trigger the AI evaluation workflow to ensure there are no semantic quality regressions. This workflow takes seconds for most commits and catches issues early.

We have now covered the full spectrum from theory to daily practice; the conclusion ties everything together.

## Conclusion

The three-tier CI model adapts traditional software practices to the unique realities of LLM-powered agents. The upfront investment in hooks, mocked tests, and selective evaluations pays off by catching regressions before they impact users. This CI pipeline is the foundational step that moves you from fragile prototypes toward reliable, production-scale agents. Future lessons will build on this, covering automated deployment and production monitoring.

## References

- [1] [What is continuous integration?](https://www.atlassian.com/continuous-delivery/continuous-integration)
- [2] [CI/CD Best Practices for 2025](https://gatling.io/blog/ci-cd-best-practices)
- [3] [How to Build a Continuous Integration Pipeline for AI Agents](https://galileo.ai/blog/continuous-integration-ci-ai-fundamentals)
- [4] [Non-Deterministic Systems](https://www.guild.ai/glossary/non-deterministic-systems)
- [5] [AI Agent Failure Detection Guide](https://latitude.so/blog/ai-agent-failure-detection-guide)
- [6] [Agent Failure Modes](https://nimblebrain.ai/why-ai-fails/agent-governance/agent-failure-modes)
- [7] [pre-commit](https://pre-commit.com/)
- [8] [Automated Guard Rails for Vibe Coding](https://blog.gitguardian.com/automated-guard-rails-for-vibe-coding)
- [9] [Ruff](https://docs.astral.sh/ruff)
- [10] [pyproject.toml explained](https://betterstack.com/community/guides/scaling-python/pyproject-explained/)
- [11] [Unit Testing (AI Agents)](https://www.guild.ai/glossary/unit-testing-ai-agents)
- [12] [CI/CD for AI Evals: Running Prompt and Agent Regression Tests in GitHub Actions](https://kinde.com/learn/ai-for-software-engineering/ai-devops/ci-cd-for-evals-running-prompt-and-agent-regression-tests-in-github-actions)
- [13] [88 Percent of AI Agents Never Reach Production: A Failure Framework](https://www.digitalapplied.com/blog/88-percent-ai-agents-never-reach-production-failure-framework)
- [14] [CI/CD for delivery of agentic AI](https://developers.redhat.com/articles/2026/05/18/ci-cd-delivery-agentic-ai)
- [15] [Best AI Evaluation Tools for CI/CD in 2026](https://www.braintrust.dev/articles/best-ai-evaluation-tools-2026)
</article>