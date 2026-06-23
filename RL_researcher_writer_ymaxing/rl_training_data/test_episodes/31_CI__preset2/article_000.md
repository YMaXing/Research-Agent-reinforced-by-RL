# Continuous Integration for AI Agents

In our last few lessons, we built a foundation for production-grade AI engineering. We used Opik for observability, created datasets for offline evaluation, and adopted an evaluation-driven development framework. These practices give you the visibility and quality signals needed to iterate safely. Now, it is time to shift our focus to Continuous Integration (CI): the automated infrastructure that keeps your codebase maintainable and prevents regressions from reaching production.

With the problem and failure modes clear, we will now define what Continuous Integration means in an AI context and introduce a three-tier model that solves these issues.

## What is Continuous Integration?

Continuous Integration (CI) is the practice of frequently merging code changes from multiple developers into a central repository. Each merge triggers an automated build and test sequence that catches integration issues early, preventing the classic "it works on my machine" problem [[1]](https://www.atlassian.com/continuous-delivery/continuous-integration). In traditional software, CI pipelines focus on deterministic logic: they compile code, run static analysis, and execute unit tests that assert exact, predictable outcomes. The standard is code correctness.

However, building AI agents introduces challenges that traditional CI was not designed for. The fundamental shift is from code correctness to behavioral correctness as the CI standard [[2]](https://galileo.ai/blog/continuous-integration-ci-ai-fundamentals). The non-determinism of LLMs means the same input can produce different outputs, making exact-match tests unreliable [[3]](https://www.guild.ai/glossary/non-deterministic-systems). Rapid prompt iteration can silently break functionality that worked yesterday. Furthermore, the high cost of API calls makes running a full test suite on every commit impractical. Without a CI strategy tailored for AI, teams often face three common failure modes.

1.  **Inconsistent code formatting across the team.** When team members use different formatters or apply styles manually, the codebase becomes cluttered with inconsistent spacing, line breaks, and import orders. This "style drift" adds noise to code reviews, forcing reviewers to spend time on trivial formatting nitpicks instead of focusing on logic and architecture.

2.  **Skipped pre-commit checks, leading to CI failures.** Under pressure to ship quickly, developers might forget or intentionally skip manual quality checks before pushing code. This leads to failures in the central CI pipeline, wasting time and blocking other developers. Without automated enforcement, quality gates become suggestions rather than requirements.

3.  **Non-deterministic tests that call real LLM APIs.** Teams that try to run tests against live LLM APIs quickly discover their test suites are slow, expensive, and flaky. A test might pass one minute and fail the next due to model variability, network latency, or rate-limiting errors. This unreliability erodes trust in the test suite and slows down the entire team [[4]](https://agiflow.io/blog/effective-practices-for-mocking-llm-responses-during-the-software-development-lifecycle).

To solve these problems, we need a CI model calibrated by cost and speed. We use a three-tier approach that provides fast, cheap feedback for most changes while reserving expensive checks for when they matter most.

*   **Tier 1: Formatting and Linting (Always Run).** These checks are fast (taking seconds) and cheap (no API calls). They catch syntactic issues and enforce style consistency. This tier is identical to traditional CI.
*   **Tier 2: Unit and Integration Tests (Always Run).** These verify deterministic logic, such as parsing, schema validation, and routing, without calling external APIs. By mocking LLM responses, tests run quickly (under a minute) and reliably.
*   **Tier 3: AI Evaluations (Manual/Release).** This tier is unique to AI systems. It involves expensive, LLM-based quality checks that use real API calls to evaluate agent quality on a curated dataset. We run these selectively before major releases or after significant prompt changes.![A three-tier CI model for AI agents, showing the flow from commit checks to PR tests and finally to manual/release AI evaluations, with each tier distinctly colored.](https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/6bf41859-7dd2-4a23-9a88-55720f54114e/image/w=1920,quality=90,fit=scale-down)

Image 1: A three-tier CI model for AI agents, showing the flow from commit checks to PR tests and finally to manual/release AI evaluations, with each tier distinctly colored.

The AI evaluations in Tier 3, which we built in previous lessons using our offline datasets and Opik traces, serve as a powerful regression test. They are uniquely suited to catch semantic quality regressions that traditional unit tests structurally cannot detect [[5]](https://kinde.com/learn/ai-for-software-engineering/ai-devops/ci-cd-for-evals-running-prompt-and-agent-regression-tests-in-github-actions).

This lesson covers the CI essentials for building production-ready AI agents. We focus on practical techniques you will use daily: automated quality checks, testing with mocked LLMs, and structuring CI pipelines around cost constraints. We will not cover comprehensive DevOps topics like Kubernetes or Terraform. Instead, we will show you how to effectively move from prototype to production-ready agents.

We will cover:
*   Setting up pre-commit hooks to enforce code quality automatically.
*   Configuring Ruff for linting and formatting.
*   Writing unit tests for deterministic agent code with mocked LLM responses.
*   Building a CI pipeline that runs automatically on every change.
*   Using AI evaluations as selective regression tests in CI.

This lesson includes a hands-on notebook where you will practice running formatting checks, linting, and tests on Brown, our writing agent. With the three-tier model established, the fastest feedback comes from running the first tier locally before you even commit code. This is where pre-commit hooks come in.

## Pre-commit Hooks: Automated Local Guardrails

Pre-commit hooks are Git-based local guardrails that run automatically every time you commit, delivering immediate feedback and preventing bad code from ever reaching the shared repository [[6]](https://pre-commit.com/). They are your first line of defense for maintaining code quality.

The **pre-commit** framework manages these hooks using a declarative YAML configuration [[6]](https://pre-commit.com/). You define the hooks you want to use in a `.pre-commit-config.yaml` file, and the framework handles their installation and execution. These hooks often reference external repositories, allowing the community to maintain up-to-date versions for popular tools.

### Brown’s Pre-commit Configuration

<aside>
💡
You can experiment with the code for this lesson in this [Colab](https://colab.research.google.com/github/louisfb01/agent-course-notebooks/blob/main/notebooks/lesson_31_notebook.ipynb#scrollTo=b30eba1a). Alternatively, you can find the code for this lesson in the notebook for Lesson 31 of the course GitHub repository.
</aside>

Let's look at the configuration used in our Brown writing agent.

```bash
!cat .pre-commit-config.yaml
```

It outputs:

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
    # Ruff version. Keep in sync with the CI workflows (.github/workflows/*.yml).
    rev: v0.14.6
    hooks:
      # Run the linter.
      - id: ruff-check
        args: [--fix, --exit-non-zero-on-fix]
      # Run the formatter.
      - id: ruff-format
```

This configuration defines three types of hooks:

*   **`validate-pyproject`**: This tool validates that your `pyproject.toml` file is structurally correct according to PEP standards. A malformed file can break your entire project, so this check is essential.
*   **`prettier`**: A popular code formatter we use for configuration files like `.github/workflows/ci.yml`. Consistent formatting makes these files readable and reduces merge conflicts.
*   **`ruff-check` and `ruff-format`**: These hooks run Ruff, a modern Python linter and formatter. The `--fix` argument automatically fixes issues, and `--exit-non-zero-on-fix` ensures the hook fails even after auto-fixing, forcing you to review and re-stage the changes. As recommended by Ruff’s authors, the `ruff-check` hook runs before `ruff-format`.

### Setting Up Pre-commit

In the `lessons/writing_workflow` repo, or any repo where you have configured your `.pre-commit-config.yaml` file, you can set up pre-commit hooks with these commands.

```bash
# Install dependencies (includes pre-commit)
uv sync --dev

# Install the Git hooks
pre-commit install
```

The `pre-commit install` command creates a Git hook at `.git/hooks/pre-commit`. Now, every time you run `git commit`, pre-commit runs automatically. You can also run the hooks manually on all files in the repository.

```bash
# Run all hooks on all files
make pre-commit
```

The workflow is simple: make your code changes, stage them with `git add`, and run `git commit`. If any hooks fail, you review the errors, fix them (often automatically), re-stage the files, and commit again. This tight feedback loop keeps the codebase clean from the start.

Pre-commit hooks often rely on fast tools like Ruff to do the actual work. Next, we will examine Ruff in depth and show how to configure and run it both locally and in CI.

## Ruff: Fast Python Linting and Formatting

Ruff is a high-speed Python linter and formatter written in Rust. It replaces a suite of older tools like Black, isort, and Flake8 with a single, consolidated binary, delivering sub-second performance even on large codebases [[7]](https://docs.astral.sh/ruff). This speed makes it ideal for running in pre-commit hooks and CI pipelines, where fast feedback is critical.

It is important to distinguish between formatting and linting, as Ruff handles both.

*   **Formatting** automatically rewrites your code to follow consistent style rules, such as indentation, line breaks, and quote style. It is opinionated and designed to be run without manual intervention.
*   **Linting** analyzes your code for potential bugs, suspicious patterns, and violations of best practices, such as unused variables or missing imports.

### Brown’s Ruff Configuration

Ruff is configured in the `pyproject.toml` file. Here is the configuration for our Brown agent.

```bash
!grep -A 20 "\[tool.ruff\]" pyproject.toml
```

It outputs:

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

[tool.pytest.ini_options]
pythonpath = ["src"]
markers = [
    "integration: end-to-end workflow tests (mocked LLMs, no network). Select with `-m integration` or skip with `-m 'not integration'`.",
]
```

Here is what each key does:
*   `target-version = "py312"` tells Ruff to apply rules compatible with Python 3.12 syntax.
*   `line-length = 140` sets the maximum line length.
*   `select = ["F", "E", "I"]` enables rule sets for catching common bugs (Pyflakes), enforcing PEP 8 style (pycodestyle), and organizing imports (isort) [[8]](https://github.com/astral-sh/ruff).
*   `known-first-party = ["src", "tests"]` tells isort how to group project-specific imports separately from third-party libraries.

We also use a `Makefile` to provide convenient shortcuts for running Ruff commands.

```bash
!sed -n '/# --- Tests & QA ---/,$p' Makefile | tail -n +2
```

It outputs:

```makefile
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

Each target uses `uv run` to execute commands within the project’s virtual environment, which is managed automatically and does not require manual activation. You can run these from the `writing_workflow/` directory to check or fix your code before committing.

### Hands-On Example: Fixing Formatting Issues

Let's see Ruff's formatter in action. We will create a Python file with several formatting issues.

```bash
%%bash

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

Now, we check the formatting without making any changes using the `--check` flag.

```bash
!uv run ruff format --check test_formatting.py
```

It outputs:

```text
Would reformat:  test_formatting.py
1 file would be reformatted
```

As expected, Ruff reports that the file would be reformatted. To fix it automatically, we run the command without the `--check` flag.

```bash
!uv run ruff format test_formatting.py
```

It outputs:

```text
1 file reformatted
```

If we inspect the file, we see that Ruff has fixed all the spacing issues, creating clean, consistently styled code.

```bash
!cat test_formatting.py
```

It outputs:

```python
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

Next, let's practice with the linter. We create a file with several common issues, including unused imports, duplicate imports, and undefined variables.

```bash
%%bash

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

When we run the linter, it reports multiple errors, including `F401` (unused import), `F811` (redefinition of import), and `F821` (undefined name).

```bash
!uv run ruff check test_linting.py
```

It outputs:

```text
Found 7 errors.
[ *] 4 fixable with the `--fix` option (1 hidden fix can be enabled with the `--unsafe-fixes` option).
```

Now, let's try to fix them automatically.

```bash
!uv run ruff check --fix test_linting.py
```

It outputs:

```text
Found 5 errors (3 fixed, 2 remaining).
No fixes available (1 hidden fix can be enabled with the `--unsafe-fixes` option).
```

Ruff automatically removes the unused `json` import and the duplicate `sys` import. However, it cannot fix the `F821` error because using an undefined function is a logic error that requires manual intervention.

```bash
!cat test_linting.py
```

It outputs:

```python
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

Once formatting and linting guardrails are in place, our attention turns to verifying the deterministic logic inside your agent nodes. This is the role of unit tests.

## Unit Tests for Agent Repos

The core challenge of testing AI agents is the non-determinism of LLMs. Making real API calls in tests is a recipe for failure: tests become slow, expensive, and flaky because identical prompts can produce different outputs or hit rate limits [[2]](https://galileo.ai/blog/continuous-integration-ci-ai-fundamentals). This unpredictability makes it impossible to write reliable assertions.

The solution is to isolate your deterministic code from the non-deterministic LLM. Unit tests should verify the logic you control, such as data processing, schema validation, and routing decisions, without making any live API calls [[9]](https://www.guild.ai/glossary/unit-testing-ai-agents). This includes:

*   **Parsing and rendering:** Does your markdown loader extract articles correctly?
*   **Schema validation:** Does your Pydantic model reject invalid data?
*   **Routing decisions:** Given a specific state, does your workflow route to the correct node?
*   **Utilities:** Do helper functions for URL extraction or text cleaning work as expected?

### Unit Tests vs. Integration Tests

In traditional software, a **unit test** verifies a small, isolated piece of code, like a single function, in memory. An **integration test** verifies that multiple components work together correctly, often involving network calls or database connections.

When testing AI agents, these boundaries blur. A single agent node often combines prompt templating, structured output parsing, and routing logic into one functional unit. We follow a pragmatic approach: if a test runs quickly with mocked dependencies and verifies deterministic logic, we consider it a unit test, regardless of how many internal components it touches.

To achieve this, we use mocking strategies to replace the live LLM with a predictable substitute. For our Brown agent, we use response injection, where we provide a fake model class with pre-scripted responses. This gives us a good balance of simplicity and control.

<aside>
💡
Another option to mock LLM calls in tests is HTTP mocking, where you intercept API requests and return canned responses using libraries like `responses` or `httpretty`. Some teams prefer fixture-based mocking with `pytest` fixtures and `unittest.mock.patch` to replace LLM calls with fixed outputs. There's also record and replay, which captures real API responses once and then replays them in tests using tools like VCR.py.
</aside>

### Our Implementation: The FakeModel Pattern

In our Brown agent, we implement response injection with a `FakeModel` class that is compatible with LangChain’s interface. This pattern has three parts.

1.  **Configuration specifies the fake model:** The `debug.yaml` configuration at `lessons/writing_workflow/configs/debug.yaml` sets all nodes to use `model_id: "fake"`.
2.  **Model factory returns FakeModel:** The model builder in `src/brown/models/get_model.py` returns a `FakeModel` instance when the configuration specifies it.
3.  **Tests inject specific responses:** The `FakeModel` in `src/brown/models/fake_model.py` extends LangChain’s `FakeListChatModel` and allows tests to inject a list of responses.

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

An instance of the `FakeModel` class takes a list of pre-scripted responses in its constructor. When `ainvoke()` is called, it returns the first response from the list and consumes it. This design ensures that unit tests can run with a fake model by default, and individual tests can inject specific responses when needed.

### Example: Testing Nodes with Mocked Responses

For nodes that call LLMs, you mock the responses. Here is an example test from `lessons/writing_workflow/tests/brown/nodes/test_article_writer.py` that demonstrates the recipe for writing these tests.

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

The test first creates a mock JSON response. It then builds a fake model and injects the response into it. Finally, it instantiates the `ArticleWriter` node with that fake model and asserts that the output is correct. This pattern keeps our tests fast, deterministic, and free.

### Running Brown’s Tests

To run Brown’s test suite, you can use the command defined in the `Makefile`.

```bash
# From the writing_workflow directory
make tests
```

This command runs `CONFIG_FILE=configs/debug.yaml uv run pytest`. The `debug.yaml` configuration ensures that all tests use the fake models and never call real LLMs, keeping the entire suite fast and reliable.

Local tests and hooks give you fast feedback, but enforcement at the repository level requires automated CI workflows that run on every pull request.

## CI Workflows: Automated Enforcement

GitHub Actions is the CI platform we use for both our Brown and Nova agents. It integrates seamlessly with GitHub repositories and requires minimal setup. Workflows trigger automatically on events like pull requests or pushes, run jobs in isolated environments, and support matrix builds for testing across multiple platforms. This allows us to get fast, reliable feedback on every change [[10]](https://docs.github.com/actions/get-started/quickstart).

### Our Complete CI Configuration

Our entire CI configuration lives in a single workflow file at `.github/workflows/ci.yml`.

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

This configuration defines when the workflow runs and what checks it performs. The `on` section specifies that the workflow triggers on pull requests to the `main` and `dev` branches, as well as on direct pushes to `main`. This ensures every code change is validated before it can be merged.

The `env` section defines an environment variable `QA_FOLDERS` that lists all the directories we want to check. Notice it includes both `src/brown` and `src/nova`, allowing us to use the same CI configuration for both agents in a monorepo structure.

### Understanding the Job Structure

The workflow defines two independent jobs that run in parallel: `qa` and `tests`. Splitting them provides clear, fast feedback. If formatting fails, you immediately see “QA job failed” without waiting for tests to complete. This parallel execution saves time and makes it easier to identify which category of checks failed.

Each job runs on `ubuntu-latest`, a virtual machine provided by GitHub. The jobs are completely isolated, which means they can run simultaneously without interference.

The `qa` job focuses on code quality checks that don’t require running the application. It starts by checking out your code with `actions/checkout@v4`, then installs `uv` using `astral-sh/setup-uv@v4`. The Python setup step uses `actions/setup-python@v5` and reads the Python version from your `.python-version` file, ensuring consistency between local development and CI. After syncing dependencies with `uv sync --dev` (which includes development tools needed for formatting and linting), it runs two checks. The format check uses `uv run ruff format --check` to verify that all code follows consistent formatting rules without modifying any files. The lint check uses `uv run ruff check` to detect code quality issues, unused imports, and potential bugs.

The `tests` job follows a similar setup process. It runs `uv sync` without the `--dev` flag since tests do not require development tools like formatters. The test step uses `CONFIG_FILE=configs/debug.yaml` to ensure tests run with the fake model configuration, preventing any real LLM API calls during CI. This keeps tests fast, deterministic, and free.

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

AI evaluations are critical for catching semantic quality regressions, such as a drop in helpfulness or an increase in hallucinations, that deterministic unit tests cannot detect [[11]](https://www.braintrust.dev/articles/best-ai-evals-tools-cicd-2025). They form the third and most specialized tier of our CI model.

### Why AI Evals Are Unique to AI Systems

Evaluations are unique to AI systems because they involve real LLM calls, which incur significant latency and cost. For example, running an evaluation on a 500-example dataset where each run costs $0.01 in tokens would amount to $5 per full run. Running this on every commit would quickly become prohibitively expensive. This cost is why we treat AI evals as a Tier 3 gate, though low-latency evaluation models are emerging to make some checks practical for the main CI loop [[2]](https://galileo.ai/blog/continuous-integration-ci-ai-fundamentals).

### Manual-Trigger CI Workflow for AI Evals

To manage costs and avoid accidental runs, we use a manual-only `workflow_dispatch` trigger for our evaluation pipeline. This ensures the workflow only runs when a developer deliberately triggers it. Here is an illustrative example of what this workflow, located at `.github/workflows/eval.yml`, might look like.

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

This workflow differs from our main CI pipeline in several key ways:

1.  The `workflow_dispatch` trigger means it never runs automatically. You must manually trigger it from the Actions tab in GitHub, which prevents expensive API calls from running on every commit.
2.  The workflow uses a production configuration (`configs/production.yaml`) instead of the debug configuration. This ensures evaluations use real LLM models rather than fake ones.
3.  The `LLM_API_KEY` environment variable pulls from GitHub Secrets, which you configure in your repository settings under **Settings → Secrets and variables → Actions**. This keeps API keys secure and out of your codebase.

The evaluation command (`python -m scripts.run_eval`) should point to your evaluation script that loads your dataset, runs your agent, and computes metrics using a framework like Opik or LangSmith.

To trigger this workflow, navigate to the Actions tab, select “**AI Evaluations**” from the list, click “**Run workflow**,” choose your branch, and confirm. The results, including logs with metrics and any failures, will be available in the Actions interface.

The frequency of these runs depends on your project’s maturity.

*   **Early development:** Run manually to measure progress weekly or after major changes.
*   **Active development:** Run before merging significant changes to catch regressions.
*   **Mature product:** Run as part of your release process, converting production incidents into new eval cases to create a feedback loop that continuously improves your regression suite [[2]](https://galileo.ai/blog/continuous-integration-ci-ai-fundamentals).

With all three tiers understood, we can now assemble them into a cohesive daily development workflow.

## Daily Development Workflow

With these tools in place, a typical daily workflow looks like this:

1.  **Write code** and corresponding tests.
2.  **Run quick checks** periodically: `make lint-check` and `make format-check`.
3.  **Run tests** after changing logic: `make tests`.
4.  **Commit your changes.** Pre-commit hooks will run automatically.
5.  **Push and open a pull request.** CI runs automatically, enforcing all checks.
6.  **Before releasing, run AI evaluations** manually to check for quality regressions.

This workflow takes seconds for most commits and catches issues early, keeping velocity high while protecting quality. We have now covered the full spectrum from theory to daily practice, so let's conclude by tying everything together.

## Conclusion

The three-tier CI model is a pragmatic adaptation of traditional software practices to the unique realities of LLM-powered systems: non-determinism, prompt volatility, and cost constraints. The upfront investment in setting up pre-commit hooks, configuring Ruff, implementing `FakeModel` patterns, and building selective evaluation workflows pays off by catching regressions before your customers experience a drop in quality. This CI framework is the foundational engineering step that moves you from fragile prototypes toward reliable, maintainable, team-scale production agents.

In future lessons, we will build directly on these practices as we cover full CI/CD integration, production monitoring, and cost optimization strategies.

## References

- [1] Atlassian. (n.d.). *Continuous Integration*. [https://www.atlassian.com/continuous-delivery/continuous-integration](https://www.atlassian.com/continuous-delivery/continuous-integration)
- [2] Galileo. (n.d.). *How to Build a Continuous Integration Pipeline for AI Agents*. [https://galileo.ai/blog/continuous-integration-ci-ai-fundamentals](https://galileo.ai/blog/continuous-integration-ci-ai-fundamentals)
- [3] Guild.ai. (2026, February 23). *Non-Deterministic Systems*. [https://www.guild.ai/glossary/non-deterministic-systems](https://www.guild.ai/glossary/non-deterministic-systems)
- [4] Agiflow. (n.d.). *Effective Practices for Mocking LLM Responses During the Software Development Lifecycle*. [https://agiflow.io/blog/effective-practices-for-mocking-llm-responses-during-the-software-development-lifecycle](https://agiflow.io/blog/effective-practices-for-mocking-llm-responses-during-the-software-development-lifecycle)
- [5] Kinde. (n.d.). *CI/CD for Evals: Running Prompt and Agent Regression Tests in GitHub Actions*. [https://kinde.com/learn/ai-for-software-engineering/ai-devops/ci-cd-for-evals-running-prompt-and-agent-regression-tests-in-github-actions](https://kinde.com/learn/ai-for-software-engineering/ai-devops/ci-cd-for-evals-running-prompt-and-agent-regression-tests-in-github-actions)
- [6] pre-commit. (n.d.). *pre-commit*. [https://pre-commit.com/](https://pre-commit.com/)
- [7] Astral. (n.d.). *Ruff*. [https://docs.astral.sh/ruff/](https://docs.astral.sh/ruff/)
- [8] GitHub. (n.d.). *astral-sh/ruff-pre-commit*. [https://github.com/astral-sh/ruff-pre-commit](https://github.com/astral-sh/ruff-pre-commit)
- [9] Guild.ai. (n.d.). *Unit Testing AI Agents*. [https://www.guild.ai/glossary/unit-testing-ai-agents](https://www.guild.ai/glossary/unit-testing-ai-agents)
- [10] GitHub Docs. (n.d.). *Quickstart for GitHub Actions*. [https://docs.github.com/actions/get-started/quickstart](https://docs.github.com/actions/get-started/quickstart)
- [11] Braintrust. (n.d.). *Best AI Eval Tools for CI/CD Pipelines (2026 Review)*. [https://www.braintrust.dev/articles/best-ai-evals-tools-cicd-2025](https://www.braintrust.dev/articles/best-ai-evals-tools-cicd-2025)
- [12] Astral. (n.d.). *Ruff Linter*. [https://docs.astral.sh/ruff/linter/](https://docs.astral.sh/ruff/linter/)
- [13] Astral. (n.d.). *Integration with GitHub Actions*. [https://docs.astral.sh/uv/guides/integration/github/](https://docs.astral.sh/uv/guides/integration/github/)
- [14] Astral. (n.d.). *Integration with pre-commit*. [https://docs.astral.sh/uv/guides/integration/pre-commit/](https://docs.astral.sh/uv/guides/integration/pre-commit/)
- [15] GitHub Docs. (n.d.). *GitHub Actions documentation*. [https://docs.github.com/en/actions](https://docs.github.com/en/actions)
- [16] Deepchecks. (n.d.). *LLM evaluation for CI/CD pipelines*. [https://www.deepchecks.com/llm-evaluation/ci-cd-pipelines/](https://www.deepchecks.com/llm-evaluation/ci-cd-pipelines/)
- [17] LangChain. (n.d.). *Testing*. [https://docs.langchain.com/oss/python/langchain/test](https://docs.langchain.com/oss/python/langchain/test)
- [18] BetterStack. (n.d.). *pyproject.toml explained*. [https://betterstack.com/community/guides/scaling-python/pyproject-explained/](https://betterstack.com/community/guides/scaling-python/pyproject-explained/)
- [19] Bright Security. (n.d.). *Unit testing best practices: 13 ways to improve your tests*. [https://brightsec.com/blog/unit-testing-best-practices/](https://brightsec.com/blog/unit-testing-best-practices/)
- [20] DEV Community. (n.d.). *How to run jobs in parallel with GitHub Actions*. [https://dev.to/cicube/how-to-run-jobs-in-parallel-with-github-actions-4png](https://dev.to/cicube/how-to-run-jobs-in-parallel-with-github-actions-4png)
- [21] DEV Community. (n.d.). *A practical guide to integrating AI evals into your CI/CD pipeline*. [https://dev.to/kuldeep_paul/a-practical-guide-to-integrating-ai-evals-into-your-cicd-pipeline-3mlb](https://dev.to/kuldeep_paul/a-practical-guide-to-integrating-ai-evals-into-your-cicd-pipeline-3mlb)
- [22] pytest. (n.d.). *pytest documentation*. [https://docs.pytest.org/](https://docs.pytest.org/)
- [23] Upsun. (n.d.). *Why Python developers should switch to uv*. [https://devcenter.upsun.com/posts/why-python-developers-should-switch-to-uv/](https://devcenter.upsun.com/posts/why-python-developers-should-switch-to-uv/)