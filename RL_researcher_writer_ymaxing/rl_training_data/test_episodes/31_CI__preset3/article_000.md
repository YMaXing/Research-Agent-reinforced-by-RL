# How to Build a Continuous Integration Pipeline for AI Agents

In our recent lessons, we have covered agent observability with Opik, built offline evaluation datasets, and explored the evaluation-driven development framework. These tools give you the visibility and metrics needed to understand your agent's behavior. Now, it is time to shift our focus to Continuous Integration (CI): the automated infrastructure that keeps your codebase maintainable and prevents regressions from reaching production. This is the engineering discipline that separates fragile prototypes from reliable, production-ready AI systems.

## What is Continuous Integration?

Continuous Integration (CI) is the practice of frequently merging code changes from multiple developers into a central repository. After each merge, an automated build and test sequence runs to detect integration issues early. This process prevents the classic "it works on my machine" problem by ensuring that all code is validated in a clean, consistent environment [[43]](https://www.atlassian.com/continuous-delivery/continuous-integration).

However, CI for AI agents is fundamentally different from traditional software CI. Traditional CI focuses on deterministic logic, where a given input always produces the same output. Checks typically include compiling code, running linters for style, and executing unit tests that assert exact outcomes [[45]](https://gatling.io/blog/ci-cd-best-practices). The fundamental shift for AI systems is from code correctness to behavioral correctness as the CI standard [[Galileo]](https://galileo.ai/blog/continuous-integration-ci-ai-fundamentals). AI agents operate in a world of non-determinism. Their behavior is shaped by probabilistic LLM responses, rapidly evolving prompts, and external data, all of which can introduce variability that breaks traditional testing assumptions [[1]](https://galileo.ai/blog/continuous-integration-ci-ai-fundamentals), [[2]](https://www.guild.ai/glossary/non-deterministic-systems).

Without a CI pipeline tailored for AI agents, teams often fall into three common failure modes.

1.  **Inconsistent code formatting across the team.** When team members use different formatters or apply styles manually, the codebase becomes a mess of conflicting conventions. This leads to cluttered pull requests where meaningful logic changes are buried under trivial style adjustments, wasting valuable code review time.
2.  **Skipped pre-commit checks, leading to CI failures.** Under pressure to ship features quickly, developers might forget to run local tests or linters before pushing code. Without automated enforcement, these manual quality gates are easily bypassed, leading to broken builds and a main branch that is frequently in a failed state.
3.  **Non-deterministic tests that call real LLM APIs.** Writing tests that call live LLM APIs is a recipe for disaster. These tests are slow, expensive, and "flaky"—they can pass or fail unpredictably due to the non-deterministic nature of LLMs, even with the temperature set to 0. This unreliability erodes trust in the test suite and slows the entire team down. These tests also miss the most insidious, agent-specific failures, such as tool misuse, context loss, or cascading errors in multi-agent systems [[53]](https://latitude.so/blog/ai-agent-failure-detection-guide), [[56]](https://nimblebrain.ai/why-ai-fails/agent-governance/agent-failure-modes).

To address these challenges, we use a three-tier CI model that balances cost, speed, and reliability.

*   **Tier 1: Formatting and Linting (Always Run).** These checks are extremely fast, taking only seconds to run, and are free since they do not involve any API calls. They catch syntactic issues and enforce a consistent coding style across the entire project. This tier is identical to what you would find in a traditional software CI pipeline.
*   **Tier 2: Unit and Integration Tests (Always Run).** This tier verifies the deterministic parts of your agent, such as data parsing, schema validation, and workflow routing. Crucially, all LLM calls are mocked, meaning we replace them with fake, predictable responses. This ensures that tests are fast (typically under a minute), reliable, and free of API costs.
*   **Tier 3: AI Evaluations (Manual/Release).** This tier is unique to AI systems. It involves running your agent against a curated dataset of inputs to measure its semantic quality on metrics like helpfulness, accuracy, or instruction-following. These evaluations make real LLM calls, making them slow and expensive. We run them selectively, either manually before a major release or after a significant change to a core prompt.![A three-tier CI model for AI agents, showing the flow from commit checks to PR tests and finally to manual/release AI evaluations, with each tier distinctly colored.](https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/6bf41859-7dd2-4a23-9a88-55720f54114e/image/w=1920,quality=90,fit=scale-down)

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

Pre-commit hooks are automated checks that run on your local machine every time you make a commit [[25]](https://pre-commit.com). They act as the first line of defense, providing immediate feedback and preventing poorly formatted or broken code from ever entering your shared repository. This local enforcement is a powerful way to maintain code quality without relying solely on a remote CI server [[22]](https://blog.gitguardian.com/automated-guard-rails-for-vibe-coding).

The `pre-commit` framework manages these hooks through a simple, declarative YAML file. You define the checks you want to run in a `.pre-commit-config.yaml` file, and the framework handles the installation and execution of the necessary tools. Hooks are typically references to external repositories, which means you can easily leverage community-maintained tools for popular linters and formatters.

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

The daily workflow is straightforward: you make your code changes, stage them with `git add`, and then run `git commit`. If any hooks fail, you review the errors, fix them (often automatically), re-stage the modified files, and commit again. Pre-commit hooks often rely on fast tools like Ruff to do the actual work. Next, we will examine Ruff in depth and show how to configure it.

## Ruff: Fast Python Linting and Formatting

Ruff is an extremely fast Python linter and formatter written in Rust. It serves as a consolidated replacement for a whole suite of older tools like Black, isort, Flake8, and pydocstyle, often delivering sub-second performance even on large codebases [[28]](https://docs.astral.sh/ruff). This speed makes it ideal for both local pre-commit hooks and CI pipelines.

It is important to distinguish between formatting and linting:

*   **Formatting** automatically rewrites your code to follow a consistent and opinionated style. It handles things like line length, indentation, and quote style, eliminating debates over minor stylistic preferences.
*   **Linting** analyzes your code for potential bugs, violations of best practices, and other quality issues. This includes flagging unused variables, missing imports, or unnecessarily complex code.

### Brown’s Ruff Configuration

Ruff is configured in the `[tool.ruff]` section of our `pyproject.toml` file. This centralizes the configuration for both the linter and the formatter.

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
4.  The file is now perfectly formatted.
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
2.  Running the linter reveals all the issues.
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

Ruff's ability to consolidate over ten legacy linters into a single, fast binary eliminates version conflicts and dramatically reduces CI execution times. Once these formatting and linting guardrails are in place, we can turn our attention to verifying the deterministic logic inside the agent nodes, which is the role of unit tests.

## Unit Tests for Agent Repos

The core challenge in testing AI agents is the non-determinism of LLMs. Making real API calls in your tests makes them slow, expensive, and flaky, as identical prompts can yield different outputs or even hit rate limits [[2]](https://www.guild.ai/glossary/non-deterministic-systems). This unpredictability makes it impossible to write reliable assertions.

Unit tests solve this problem by focusing on the deterministic logic within your agent. This includes verifying components that do not require live LLM calls, such as [[30]](https://www.guild.ai/glossary/unit-testing-ai-agents):

*   **Parsing and rendering:** Does your markdown loader correctly extract articles and guidelines?
*   **Schema validation:** Does your Pydantic model reject invalid data structures?
*   **Routing decisions:** Given a specific state, does your agent's workflow route to the correct node?
*   **Utilities:** Do helper functions for text cleaning or URL extraction work as expected?

### Unit Tests vs. Integration Tests

In traditional software engineering, **unit tests** verify individual functions or classes in isolation, while **integration tests** check that multiple components work together correctly. With AI agents, this distinction can become blurry. A single agent node often combines several responsibilities, such as prompt templating, structured output parsing, and routing logic.

We take a pragmatic approach: if a test runs quickly, uses mocked dependencies to avoid network calls, and verifies deterministic logic, we consider it a unit test. This allows us to test meaningful chunks of our agent's behavior without getting bogged down in strict definitions.

To isolate our tests from the non-deterministic LLM, we use a technique called mocking. The most effective strategy for AI agents is response injection, where we provide a fake model with a pre-scripted list of responses. This gives us full control over the LLM's output in a test environment.

<aside>
💡
Another option to mock LLM calls in tests is HTTP mocking, where you intercept API requests and return canned responses using libraries like `responses` or `httpretty`. Some teams prefer fixture-based mocking with `pytest` fixtures and `unittest.mock.patch` to replace LLM calls with fixed outputs. There is also record and replay, which captures real API responses once using tools like `VCR.py` and then replays them in subsequent test runs [[64]](https://agiflow.io/blog/effective-practices-for-mocking-llm-responses-during-the-software-development-lifecycle).
</aside>

### Our Implementation: The FakeModel Pattern

In our Brown agent, we implement response injection using a `FakeModel` class that is compatible with LangChain’s interface. This pattern consists of three parts:

1.  **Configuration specifies the fake model:** The `debug.yaml` configuration at `lessons/writing_workflow/configs/debug.yaml` sets all nodes to use `model_id: “fake”`.
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

An instance of the `FakeModel` class takes a list of pre-scripted responses in its constructor. When its `ainvoke()` method is called, it returns the next response from the list and consumes it. This design ensures that all unit tests run with a fake model by default, and individual tests can inject specific, predictable responses when needed.

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

The test first defines a mock JSON response. It then builds a fake model and injects the mock response into it. Finally, it instantiates the `ArticleWriter` node with the fake model and asserts that the output is correct. This pattern keeps our tests fast, deterministic, and free.

### Running Brown’s Tests

To run the entire test suite for Brown, you can use the `make tests` command from the `writing_workflow/` directory.

```bash
# From the writing_workflow directory
make tests
```

This command runs `CONFIG_FILE=configs/debug.yaml uv run pytest`. The `CONFIG_FILE` environment variable ensures that all tests use the `debug.yaml` configuration, which specifies the use of fake models and prevents any real LLM API calls.

Local tests and hooks provide fast feedback, but true enforcement at the repository level requires automated CI workflows that run on every pull request.

## CI Workflows: Automated Enforcement

GitHub Actions is our CI platform of choice for both the Brown and Nova agents. It allows us to define automated workflows that trigger on events like pull requests or pushes to the main branch. These workflows run in isolated environments, support matrix builds for testing across different platforms, and can execute jobs in parallel to provide fast feedback [[14]](https://kinde.com/learn/ai-for-software-engineering/ai-devops/ci-cd-for-evals-running-prompt-and-agent-regression-tests-in-github-actions).

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

Each job runs on an `ubuntu-latest` virtual machine provided by GitHub and is completely isolated. The `qa` job focuses on code quality. It checks out the code, installs `uv`, sets up the Python environment based on the `.python-version` file, and installs all project dependencies, including development tools, with `uv sync --dev`. It then runs `ruff format --check` to verify code formatting and `ruff check` to lint for quality issues.

The `tests` job follows a similar setup but installs only the production dependencies with `uv sync`. It then runs the test suite using `CONFIG_FILE=configs/debug.yaml uv run pytest`. This ensures that all tests execute with our fake model configuration, preventing any real LLM API calls and keeping the CI pipeline fast, deterministic, and free.

### Setting Up GitHub Actions for Your Repository

To enable this workflow, you need to create the `.github/workflows/` directory at the root of your repository. Inside this directory, create a file named `ci.yml` and paste the configuration above. You will also need a `.python-version` file in your project root specifying the Python version (e.g., `3.12`) and a `configs/debug.yaml` file that configures your agents to use fake models for testing.

Once you commit and push this file, the workflow becomes active. You do not need to configure anything in the GitHub UI for this basic setup, though you will need to add secrets for more advanced workflows, like those involving API keys for evaluations.

### Running the Pipeline and Observing Results

The pipeline runs automatically when its trigger conditions are met. When you open a pull request, the workflow executes and reports its status directly on the PR page, blocking merges if any checks fail.

You can also trigger the workflow manually. In your GitHub repository, go to the "Actions" tab, select the "CI" workflow, and click the "Run workflow" button. This is useful for re-running failed checks or testing a fix without creating a new commit. During a run, you can click on each job (`qa` and `tests`) to view the live output of its steps. If a step fails, its output is expanded and highlighted in red, making it easy to spot the problem.

### Interpreting CI Results and Fixing Issues

When the CI pipeline runs, each job will either succeed (green checkmark) or fail (red X). If the `qa` job fails, the logs will show exactly which files have formatting or linting issues. You can fix these locally by running `make format-fix` or `make lint-fix` from the `writing_workflow/` directory, then committing and pushing the changes.

If the `tests` job fails, the `pytest` output will show a detailed traceback for the failed test. This helps you identify whether the issue is a logic error, an incorrect mock response, or a missing dependency. You can debug the failure locally by running `make tests`.

A critical principle of our CI setup is that it runs the exact same commands as our local `make` targets. This alignment eliminates "it works on my machine" problems. If your checks pass locally, they will pass in CI.

### Trying It Out

The best way to understand CI is to see it in action. Try introducing a deliberate formatting error, commit it, and open a pull request. Watch the `qa` job fail and inspect the logs. Then, run `make format-fix` locally, commit the corrected code, and push again. The CI pipeline will re-run automatically and pass. This hands-on experience will solidify your understanding of the automated feedback loop.

The first two tiers of our CI model run on every commit, but ensuring semantic quality requires a more expensive third tier. This is where AI evaluations enter the picture as selective regression tests.

## AI Evaluations as Regression Tests

AI evaluations are essential for catching semantic quality regressions, such as a decline in helpfulness or an increase in hallucinations, which deterministic unit tests cannot detect [[14]](https://kinde.com/learn/ai-for-software-engineering/ai-devops/ci-cd-for-evals-running-prompt-and-agent-regression-tests-in-github-actions). This practice, often called "golden flow validation," involves benchmarking every build against a representative set of interactions and known failure modes [[Galileo]](https://galileo.ai/blog/continuous-integration-ci-ai-fundamentals). These evaluations form the third tier of our CI model, a quality gate unique to AI systems.

### Why AI Evals Are Unique to AI Systems

AI evaluations are treated as a special, Tier 3 gate because they are expensive. Each run involves real LLM calls, which incur both latency and monetary costs. Development and testing often occur at low volumes where per-call costs seem negligible, but production scale can lead to massive cost overruns [[57]](https://www.digitalapplied.com/blog/88-percent-ai-agents-never-reach-production-failure-framework). For example, a single evaluation run with 20 conversations can cost around $0.64 with a frontier model [[58]](https://developers.redhat.com/articles/2026/05/18/ci-cd-delivery-agentic-ai). Running this on every commit would quickly become impractical. Therefore, we run these evaluations selectively.

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

This workflow differs from our main CI pipeline in a few key ways:

1.  The `workflow_dispatch` trigger ensures it only runs when manually initiated from the GitHub Actions tab. This is our primary safeguard against accidental, costly runs.
2.  It uses a production configuration (`configs/production.yaml`), which means it calls real LLM models instead of our fake ones.
3.  The `LLM_API_KEY` is securely passed to the environment from GitHub Secrets. You can configure these in your repository settings under **Settings → Secrets and variables → Actions**.

To trigger this workflow, you navigate to the "Actions" tab in your repository, select "AI Evaluations," click "Run workflow," choose your branch, and confirm. The results and logs will be available in the Actions interface.

The frequency of running these evaluations depends on your project's maturity:

*   **Early development:** Run evaluations manually on a weekly basis or after major architectural changes to track progress.
*   **Active development:** Run them before merging significant feature branches to catch any regressions you may have introduced. Some teams adopt a two-part strategy: running a small set of critical evaluations on every pull request and a more comprehensive suite nightly [[58]](https://developers.redhat.com/articles/2026/05/18/ci-cd-delivery-agentic-ai).
*   **Mature product:** Integrate them into your formal release process to ensure that production quality never degrades. A best practice is to automatically convert production failures into new evaluation cases, continuously hardening your test suite [[60]](https://www.braintrust.dev/articles/best-ai-evaluation-tools-2026).

With all three tiers of our CI model understood, we can now assemble them into a cohesive daily development workflow.

## Daily Development Workflow

With these CI tools and workflows in place, your daily development process becomes a streamlined, quality-driven cycle.

1.  **Write code** and corresponding unit tests for any new deterministic logic.
2.  **Run quick checks** locally as you work using `make lint-check` and `make format-check`.
3.  **Run tests** after implementing a logical change with `make tests`.
4.  **Commit your changes.** The pre-commit hooks will run automatically, catching any last-minute issues.
5.  **Push and open a pull request.** The main CI workflow will run automatically, providing a final validation gate.
6.  **Before a release, run AI evaluations** manually from the GitHub Actions tab to confirm there are no semantic quality regressions.

This workflow provides feedback in seconds for most commits, catching issues at the earliest possible stage and ensuring that your AI agent remains robust and maintainable.

## Conclusion

The three-tier CI model is a pragmatic adaptation of traditional software engineering practices to the unique challenges of building AI agents. By separating fast, deterministic checks from slow, expensive evaluations, we can maintain high development velocity without sacrificing quality. The upfront investment in setting up pre-commit hooks, configuring Ruff, implementing the `FakeModel` pattern, and defining GitHub Actions workflows pays off by catching regressions before they impact your users.

This CI pipeline is the foundational step that moves your project from a fragile prototype to a reliable, maintainable system that can be scaled across a team. It works when you treat behavior, not just code, as the release artifact [[Galileo]](https://galileo.ai/blog/continuous-integration-ci-ai-fundamentals). In our upcoming lessons, we will build directly on these practices as we explore full CI/CD integration, production monitoring, and cost optimization strategies.

## References

- [1] [Continuous Integration (CI) for AI Fundamentals](https://galileo.ai/blog/continuous-integration-ci-ai-fundamentals)
- [2] [Non-Deterministic Systems](https://www.guild.ai/glossary/non-deterministic-systems)
- [9] [Effective Practices for Mocking LLM Responses During the Software Development Lifecycle](https://agiflow.io/blog/effective-practices-for-mocking-llm-responses-during-the-software-development-lifecycle)
- [11] [FakeLLM](https://langchain-contrib.readthedocs.io/en/latest/llms/fake.html)
- [13] [Fake Chat Models](https://docs.langchain.com/oss/javascript/integrations/chat/fake)
- [14] [CI/CD for Evals: Running prompt and agent regression tests in GitHub Actions](https://kinde.com/learn/ai-for-software-engineering/ai-devops/ci-cd-for-evals-running-prompt-and-agent-regression-tests-in-github-actions)
- [15] [Best AI Evals Tools for CI/CD in 2025](https://www.braintrust.dev/articles/best-ai-evals-tools-cicd-2025)
- [17] [What is AI Regression Testing?](https://testgrid.io/blog/what-is-ai-regression-testing)
- [18] [A practical guide to integrating AI evals into your CI/CD pipeline](https://dev.to/kuldeep_paul/a-practical-guide-to-integrating-ai-evals-into-your-cicd-pipeline-3mlb)
- [19] [How to use workflow_dispatch in GitHub Actions](https://graphite.com/guides/github-actions-workflow-dispatch)
- [20] [Manually running a workflow](https://docs.github.com/actions/managing-workflow-runs/manually-running-a-workflow)
- [21] [Run AI Agent Evals using GitHub Actions](https://learn.microsoft.com/en-us/azure/foundry/how-to/evaluation-github-action)
- [22] [Automated Guard Rails for Vibe Coding](https://blog.gitguardian.com/automated-guard-rails-for-vibe-coding)
- [23] [Local Guardrails for Secrets Security](https://blog.gitguardian.com/local-guardrails-for-secrets-security)
- [24] [pre-commit-hooks](https://github.com/pre-commit/pre-commit-hooks)
- [25] [pre-commit](https://pre-commit.com/)
- [26] [Git Hooks](https://www.atlassian.com/git/tutorials/git-hooks)
- [27] [Ruff FAQ](https://docs.astral.sh/ruff/faq)
- [28] [Ruff](https://docs.astral.sh/ruff)
- [29] [ruff](https://github.com/astral-sh/ruff)
- [30] [Unit Testing (AI Agents)](https://www.guild.ai/glossary/unit-testing-ai-agents)
- [31] [Testing AI Agents in 2025: A Guide to Frameworks and Best Practices](https://oneuptime.com/blog/post/2026-01-30-agent-testing/view)
- [32] [The 4 Best Frameworks to Test Non-Deterministic AI Agents](https://datagrid.com/blog/4-frameworks-test-non-deterministic-ai-agents)
- [33] [An Empirical Study of Testing Practices in Open Source AI Agent Frameworks and Agentic Applications](https://arxiv.org/html/2509.19185v1)
- [34] [A Guide to Unit Testing AI Systems](https://galileo.ai/blog/unit-testing-ai-systems)
- [43] [What is continuous integration?](https://www.atlassian.com/continuous-delivery/continuous-integration)
- [44] [What is CI/CD?](https://octopus.com/devops/ci-cd)
- [45] [CI/CD Best Practices for 2025](https://gatling.io/blog/ci-cd-best-practices)
- [46] [What is continuous integration?](https://www.ibm.com/think/topics/continuous-integration)
- [47] [CI/CD Best Practices for Data Projects: Validation and Testing](https://www.sunnydata.ai/blog/cicd-best-practices-data-projects-validation-testing)
- [48] [AI Maturity Assessment Framework: A Guide to Enterprise AI Readiness](https://www.ness.com/blog/ai-maturity-assessment-framework)
- [49] [MITRE AI Maturity Model and Organizational Assessment Tool Guide](https://www.mitre.org/news-insights/publication/mitre-ai-maturity-model-and-organizational-assessment-tool-guide)
- [50] [Assess Your AI Maturity](https://www.infotech.com/research/ss/assess-your-ai-maturity)
- [51] [The AI Maturity Model in 2025](https://sema4.ai/blog/ai-maturity-model-2026)
- [52] [OWASP AI Maturity Assessment (AIMA)](https://owasp.org/www-project-ai-maturity-assessment)
- [53] [AI Agent Failure Detection Guide](https://latitude.so/blog/ai-agent-failure-detection-guide)
- [56] [Agent Failure Modes](https://nimblebrain.ai/why-ai-fails/agent-governance/agent-failure-modes)
- [57] [88 Percent of AI Agents Never Reach Production: A Failure Framework](https://www.digitalapplied.com/blog/88-percent-ai-agents-never-reach-production-failure-framework)
- [58] [CI/CD for delivery of agentic AI](https://developers.redhat.com/articles/2026/05/18/ci-cd-delivery-agentic-ai)
- [60] [Best AI Evaluation Tools for CI/CD in 2026](https://www.braintrust.dev/articles/best-ai-evaluation-tools-2026)
- [64] [Effective Practices for Mocking LLM Responses During the Software Development Lifecycle](https://agiflow.io/blog/effective-practices-for-mocking-llm-responses-during-the-software-development-lifecycle)
- [Integration with GitHub Actions, uv docs](https://docs.astral.sh/uv/guides/integration/github/)
- [Integration with pre-commit, uv docs](https://docs.astral.sh/uv/guides/integration/pre-commit/)
- [Lesson 31: Continuous Integration (CI) for AI Engineering](https://colab.research.google.com/github/louisfb01/agent-course-notebooks/blob/main/notebooks/lesson_31_notebook.ipynb#scrollTo=b30eba1a)
- [LLM evaluation for CI/CD pipelines](https://www.deepchecks.com/llm-evaluation/ci-cd-pipelines/)
- [Testing](https://docs.langchain.com/oss/python/langchain/test)
- [pyproject.toml explained](https://betterstack.com/community/guides/scaling-python/pyproject-explained/)
- [Unit testing best practices: 13 ways to improve your tests](https://brightsec.com/blog/unit-testing-best-practices/)
- [How to run jobs in parallel with GitHub Actions](https://dev.to/cicube/how-to-run-jobs-in-parallel-with-github-actions-4png)
- [pytest documentation](https://docs.pytest.org/)
- [Why Python developers should switch to uv](https://devcenter.upsun.com/posts/why-python-developers-should-switch-to-uv/)
- [How to Build a Continuous Integration Pipeline for AI Agents](https://galileo.ai/blog/continuous-integration-ci-ai-fundamentals)