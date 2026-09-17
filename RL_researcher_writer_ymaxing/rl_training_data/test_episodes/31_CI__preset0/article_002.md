# How to Build a Continuous Integration Pipeline for AI Agents

In previous lessons, we established observability with Opik and evaluation-driven development. These steps give you the visibility to understand agent behavior. Now, we will build the automated infrastructure that keeps your codebase maintainable and prevents regressions: Continuous Integration (CI). We will define what CI means in an AI context and introduce the three-tier model that solves the unique challenges of building with LLMs.

## What is Continuous Integration?

Continuous Integration (CI) is the practice of frequently merging code changes from multiple developers into a central repository. After each merge, an automated build and test sequence runs to detect integration issues early, preventing the classic "it works on my machine" problem [[43]](https://www.atlassian.com/continuous-delivery/continuous-integration).

However, traditional software CI, which focuses on deterministic logic, compilation checks, and unit tests, falls short when applied to AI agents. Agent development introduces unique challenges:
- **Non-determinism:** LLMs are probabilistic. The same prompt can produce different outputs, making traditional pass/fail tests unreliable and flaky.
- **Rapid Iteration:** Prompts, models, and agent configurations change constantly. A small tweak can silently break downstream behavior in ways that are hard to predict.
- **High Costs:** Naive test suites that make live LLM calls are slow and expensive. A single test run can quickly burn through your API budget.

Without a CI pipeline adapted for these realities, teams often encounter three common failure modes [[2]](https://www.guild.ai/glossary/non-deterministic-systems), [[14]](https://kinde.com/learn/ai-for-software-engineering/ai-devops/ci-cd-for-evals-running-prompt-and-agent-regression-tests-in-github-actions).

### Inconsistent code formatting across the team

When team members use different formatters or apply styles manually, the codebase becomes a mess of inconsistent spacing, line breaks, and quote styles. This clutters pull requests with trivial style fixes and wastes valuable code review time that should be spent on logic and architecture. Every minute spent debating tabs versus spaces is a minute not spent on improving the agent's reasoning capabilities.

### Skipped pre-commit checks, leading to CI failures

Under pressure to ship quickly, developers might forget or intentionally skip running local quality checks like linting or testing. Without automated enforcement, these issues only surface later in the CI pipeline, causing delays and forcing developers to switch context to fix problems that should have been caught locally. A CI failure discovered hours after a commit breaks the fast feedback loop that is essential for agile development.

### Non-deterministic tests that call real LLM APIs

This is the most common anti-pattern. Tests that depend on live LLM calls are inherently flaky. They can fail due to network issues, API rate limits, or simply the model's non-deterministic nature. These failures are unpredictable, slow down the development cycle, and erode trust in the test suite. Eventually, developers start ignoring failing tests, defeating their purpose entirely [[1]](https://galileo.ai/blog/continuous-integration-ci-ai-fundamentals).

To address these challenges, we use a three-tier model calibrated by cost and speed.

### Tier 1: Formatting and Linting (Always Run)

These checks are fast, taking only seconds, and are cheap because they involve no API calls. They catch syntactic issues and enforce style consistency across the entire codebase. This tier is identical to traditional CI and provides the first line of defense against messy, unmaintainable code.

### Tier 2: Unit and Integration Tests (Always Run)

These tests verify the deterministic logic within your agent, such as prompt construction, response parsing, schema validation, and routing. By mocking LLM responses, these tests run quickly (under a minute), remain deterministic, and incur no API costs. This tier ensures the structural integrity of your agent's components without the flakiness of live model calls.

### Tier 3: AI Evaluations (Manual/Release)

This tier is unique to AI systems. It involves expensive, LLM-based quality checks that use real API calls to evaluate the agent's semantic quality on a curated dataset. These are run selectively before major releases or after significant prompt changes to catch behavioral regressions that deterministic tests cannot detect.![A three-tier CI model for AI agents, showing the flow from commit checks to PR tests and finally to manual/release AI evaluations, with each tier distinctly colored.](https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/6bf41859-7dd2-4a23-9a88-55720f54114e/image/w=1920,quality=90,fit=scale-down)
Image 1: A three-tier CI model for AI agents, showing the flow from commit checks to PR tests and finally to manual/release AI evaluations, with each tier distinctly colored.

The AI evaluations in Tier 3 are built on the offline datasets and Opik traces we covered in previous lessons. They serve as a powerful regression test to catch semantic quality issues—like a drop in helpfulness or an increase in hallucinations—that traditional unit tests structurally cannot detect.

This lesson covers the CI essentials for building production-ready AI agents. We focus on practical techniques you will use daily: automated quality checks, testing with mocked LLMs, and structuring CI pipelines around cost constraints. We will not cover comprehensive DevOps topics like Kubernetes or Terraform. Instead, we teach you how to effectively move from prototype to production-ready agents.

We will cover:
- Setting up pre-commit hooks to enforce code quality automatically.
- Configuring Ruff for linting and formatting.
- Writing unit tests for deterministic agent code with mocked LLM responses.
- Building a CI pipeline that runs automatically on every change.
- Using AI evaluations as selective regression tests in CI.

This lesson includes a hands-on notebook where you will practice running formatting checks, linting, and tests on Brown, our writing agent.

With the three-tier model established, the fastest feedback comes from running the first tier locally before you even commit code. This is where pre-commit hooks come in.

## Pre-commit Hooks: Automated Local Guardrails

Pre-commit hooks are automated checks that run locally on your machine every time you make a commit. They act as a local guardrail, providing immediate feedback and preventing poorly formatted or buggy code from ever entering the central repository. This catches issues at the earliest possible stage, saving time and keeping the shared codebase clean [[25]](https://pre-commit.com/), [[22]](https://blog.gitguardian.com/automated-guard-rails-for-vibe-coding).

The `pre-commit` framework manages these hooks using a declarative YAML configuration file. You define the hooks you want to use in `.pre-commit-config.yaml`, and the framework handles their installation and execution. This declarative approach is powerful because it keeps your configuration version-controlled and easily shareable across a team. The hooks themselves often reference external repositories, allowing you to leverage community-maintained tools for popular linters and formatters without any manual setup.

### Brown’s Pre-commit Configuration

<aside>
💡
You can experiment with the code for this lesson in this [Colab](https://colab.research.google.com/github/louisfb01/agent-course-notebooks/blob/main/notebooks/lesson_31_notebook.ipynb#scrollTo=b30eba1a).
Alternatively, you can find the code for this lesson in the notebook for Lesson 31 of the course GitHub repository.
</aside>

Our Brown writing agent uses a standard set of pre-commit hooks defined in `lessons/writing_workflow/.pre-commit-config.yaml`:

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

Here is a breakdown of the three hooks:
- **`validate-pyproject`**: This tool validates that your `pyproject.toml` file is structurally correct according to official Python standards (PEPs). A malformed `pyproject.toml` can break your entire build and dependency management process.
- **`prettier`**: A popular code formatter that we use to ensure configuration files like `.github/workflows/ci.yml` have consistent styling. This makes them easier to read and helps reduce merge conflicts.
- **`ruff-check` and `ruff-format`**: These hooks run Ruff, our chosen Python linter and formatter. The `--fix` argument automatically corrects any fixable issues, and `--exit-non-zero-on-fix` ensures the hook fails even after auto-fixing. This forces you to review and re-stage the changes, confirming you are aware of what was modified. As recommended by Ruff's authors, `ruff-check` runs before `ruff-format`.

### Setting Up Pre-commit

In the `lessons/writing_workflow` repo, you can set up pre-commit hooks with a few simple commands:

```bash
# Install dependencies (includes pre-commit)
uv sync --dev

# Install the Git hooks
pre-commit install
```

The `pre-commit install` command creates a script at `.git/hooks/pre-commit`. Now, every time you run `git commit`, these hooks will execute automatically. You can also run them manually on all files in the project:

```bash
# Run all hooks on all files
make pre-commit
```

The daily workflow is straightforward: you make your code changes, stage them with `git add`, and then run `git commit`. If any hooks fail, you review the errors, fix them (often automatically), re-stage the modified files, and commit again.

Pre-commit hooks often rely on fast, powerful tools like Ruff to do the actual work. Next, we will examine Ruff in more detail and show how to configure it for both local development and CI.

## Ruff: Fast Python Linting and Formatting

Ruff is a modern, high-performance Python linter and formatter written in Rust. It is designed to be extremely fast, often 10-100 times faster than legacy tools. It consolidates the functionality of multiple older tools like Black, isort, Flake8, and pydocstyle into a single, efficient binary. This consolidation simplifies configuration, eliminates version conflicts between tools, and dramatically speeds up local checks and CI runtimes [[28]](https://docs.astral.sh/ruff).

It is important to distinguish between formatting and linting:
- **Formatting** automatically rewrites your code to follow a consistent style. It is opinionated and focuses on readability, handling things like line length, indentation, and quote style.
- **Linting** analyzes your code for potential bugs, stylistic violations, and anti-patterns. It detects issues like unused variables, missing imports, and overly complex code that could lead to errors.

### Brown’s Ruff Configuration

Ruff is configured in the `pyproject.toml` file, which centralizes settings for many modern Python tools. Here is the configuration from `lessons/writing_workflow/pyproject.toml`:

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

- `target-version = "py312"` tells Ruff to enforce rules compatible with Python 3.12.
- `line-length = 140` sets the maximum line length.
- `select = ["F", "E", "I"]` enables three key rule sets: Pyflakes (`F`) for catching common bugs, pycodestyle (`E`) for enforcing PEP 8 style, and isort (`I`) for organizing imports.
- `known-first-party = ["src", "tests"]` helps isort correctly group project-specific imports separately from third-party libraries.

To make running these checks easier, our `Makefile` provides convenient shortcuts:

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

Each target uses `uv run` to execute commands within the project's virtual environment, which is managed automatically by `uv` and does not require manual activation.

### Hands-On Example: Fixing Formatting Issues

To see Ruff's formatter in action, let's create a file with deliberate formatting errors. This file contains extra spaces in the function definition, no spaces around operators, and inconsistent spacing in the class definition.

1.  Create a file named `test_formatting.py` with these issues.

    ```bash
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
    ```

2.  Run the format check command to see what Ruff would change.

    ```bash
    uv run ruff format --check test_formatting.py
    ```

    It outputs:

    ```text
    Would reformat: test_formatting.py
    1 file would be reformatted
    ```
    The `--check` flag tells Ruff to report issues without modifying the file, which is perfect for CI environments.

3.  Now, auto-fix the file to apply the correct formatting.

    ```bash
    uv run ruff format test_formatting.py
    ```

    It outputs:

    ```text
    1 file reformatted
    ```
    The file is now cleanly formatted, with correct spacing around operators, in function signatures, and class definitions. This instant, consistent formatting is a huge time-saver.

### Hands-On Example: Fixing Linting Issues

Linting goes beyond style to catch potential bugs. Let's create another file with common linting errors.

1.  Create a file named `test_linting.py` with unused imports, duplicate imports, and an undefined variable.

    ```python
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
    ```

2.  Run the lint check to see the reported issues.

    ```bash
    uv run ruff check test_linting.py
    ```

    Ruff reports several issues, including `F401` for the unused `json` import, `F811` for the redefinition of `sys`, and `F821` because `some_undefined_function` does not exist. It also flags unsorted imports (`I001`) and misplaced imports (`E402`).

    ```text
    Found 7 errors.
    [*] 4 fixable with the `--fix` option...
    ```

3.  Run the auto-fix command to correct what can be fixed automatically.

    ```bash
    uv run ruff check --fix test_linting.py
    ```

    Ruff automatically removes the unused `json` import and the duplicate `sys` import, and it sorts the remaining imports correctly. However, it leaves the `F821` (undefined name) error untouched. This is by design: fixing an undefined name requires a logic change that only a developer can make. The linter handles what it can safely, and flags the rest for manual review.

Once formatting and linting guardrails are in place, our attention turns to verifying the deterministic logic inside the agent nodes. This is the role of unit tests.

## Unit Tests for Agent Repos

The core challenge of testing AI agents is the non-determinism of LLMs. Making live API calls in tests is an anti-pattern because it makes them slow, expensive, and flaky. An identical prompt can yield different outputs, or the API might fail due to rate limits or network issues. This unpredictability breaks the reliability needed for an effective test suite [[1]](https://galileo.ai/blog/continuous-integration-ci-ai-fundamentals).

Unit tests solve this by focusing only on the deterministic parts of your agent's logic. This includes any code that does not require a live LLM call, such as:
- **Parsing and rendering:** Verifying that your data loaders correctly extract information from files.
- **Schema validation:** Ensuring your Pydantic models reject invalid data and accept valid data.
- **Routing decisions:** Confirming that your workflow logic correctly routes to the next node based on a given state.
- **Utilities:** Testing helper functions, like those for URL extraction or text cleaning, to ensure they work as expected.

### Unit Tests vs. Integration Tests

In traditional software, a **unit test** verifies a single, isolated piece of code, like a function or a class. An **integration test** checks how multiple components work together. For AI agents, these lines blur. A single agent "node" might combine prompt templating, structured output parsing, and business logic into one unit.

We take a pragmatic approach: if a test runs quickly, uses mocked dependencies to avoid network calls, and verifies deterministic logic, we consider it a unit test. This allows us to test our agent nodes effectively without the flakiness of live API calls. The goal is to verify that the code *around* the LLM call is correct: that the prompt is constructed properly, the API is called with the right parameters, and the response is parsed into a valid output schema [[12]](https://www.iamraghuveer.com/posts/unit-testing-custom-agents).

To achieve this, we use mocking. The most effective strategy for AI agents is response injection, where we provide a pre-scripted response for the LLM to return. In our Brown agent, we use a custom `FakeModel` class for this purpose, which is simpler and gives us more control than patching at the HTTP layer.

<aside>
💡
Another option to mock LLM calls in tests is HTTP mocking, where you intercept API requests and return canned responses using libraries like `responses` or `httpretty`. Some teams prefer fixture-based mocking with `pytest` fixtures and `unittest.mock.patch` to replace LLM calls with fixed outputs. There is also record and replay, which captures real API responses once and then replays them in tests using tools like `VCR.py`.
</aside>

### Our Implementation: The FakeModel Pattern

Our response injection strategy, the `FakeModel` pattern, consists of three parts:

1.  **Configuration specifies the fake model:** The `debug.yaml` configuration at `lessons/writing_workflow/configs/debug.yaml` sets all nodes to use `model_id: "fake"`.
2.  **Model factory returns FakeModel:** The model builder in `src/brown/models/get_model.py` checks the configuration and returns an instance of our `FakeModel` when `model_id` is "fake".
3.  **Tests inject specific responses:** The `FakeModel` in `src/brown/models/fake_model.py` extends LangChain’s `FakeListChatModel` and allows tests to provide a list of canned responses.

Here is a simplified look at the `FakeModel` implementation:

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

An instance of `FakeModel` takes a list of pre-scripted responses in its constructor. Each time `ainvoke()` is called, it returns the next response from the list and consumes it. The logic inside `ainvoke` is particularly important for structured outputs. It checks if a Pydantic model (`_structured_output_type`) is expected, and if so, it parses the mock response string into a JSON object and then validates it against the Pydantic model. This allows us to test our structured output parsing and validation logic with controlled, predictable inputs. This design ensures our unit tests run with a fake model by default, and each test can inject the specific responses it needs. This approach allows us to test everything *except* the LLM itself, giving us confidence that our agent's logic is correct [[31]](https://oneuptime.com/blog/post/2026-01-30-agent-testing/view).

### Example: Testing Nodes with Mocked Responses

Here is how we write a test for a node that calls an LLM, using an example from `lessons/writing_workflow/tests/brown/nodes/test_article_writer.py`:

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

The test follows a simple recipe:
1.  **Define a mock response:** We create a `mock_response` string containing the exact JSON we expect the LLM to return.
2.  **Build the fake model:** We call `get_app_config()` to load our debug configuration, then use our `build_model` factory to create a `FakeModel` instance.
3.  **Inject the response:** We assign our `mock_response` to the model's `responses` list.
4.  **Instantiate the node:** We create an instance of `ArticleWriter`, passing the fake model into its constructor. The other dependencies are provided by `pytest` fixtures.
5.  **Invoke and assert:** We call the `ainvoke` method and then assert that the result is of the correct type (`Article`) and that its content matches our expectations.

This pattern keeps our tests fast, deterministic, and free, providing a reliable way to verify the logic of our agent nodes.

### Running Brown’s Tests

To run the entire test suite for our Brown agent, you can use the `Makefile` command:

```bash
# From the writing_workflow directory
make tests
```

This command executes `CONFIG_FILE=configs/debug.yaml uv run pytest`. The `CONFIG_FILE` environment variable ensures that our `debug.yaml` configuration is used, which directs the model factory to create `FakeModel` instances and guarantees that no real LLM APIs are called during the test run.

Local tests and hooks provide fast feedback, but enforcement at the repository level requires automated CI workflows that run on every pull request.

## CI Workflows: Automated Enforcement

GitHub Actions is our CI platform of choice for both the Brown and Nova agents. It integrates seamlessly with GitHub repositories, requires minimal setup, and provides powerful features. Workflows are triggered by events like pull requests or pushes, and jobs can run in parallel on isolated virtual machines, ensuring that feedback remains fast [[36]](https://docs.github.com/actions/get-started/quickstart).

### Our Complete CI Configuration

Our complete CI configuration is defined in a single workflow file at `.github/workflows/ci.yml`. This file orchestrates all our automated checks.

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

The `on` section specifies that the workflow triggers on pull requests targeting the `main` and `dev` branches, and on direct pushes to `main`. This ensures every code change is validated. The `env` section defines a `QA_FOLDERS` variable that lists all directories to check, allowing us to manage both agents within a monorepo structure using a single CI configuration.

### Understanding the Job Structure

The workflow is divided into two independent jobs, `qa` and `tests`, which run in parallel to provide faster feedback. If a formatting check fails, you see the "QA job failed" status immediately without waiting for the test suite to finish. This parallel execution saves time and makes it easier to identify which category of checks failed. Each job runs on `ubuntu-latest`, a virtual machine provided by GitHub, and is completely isolated.

The `qa` job focuses on code quality checks. Let's break down its steps:
- **Checkout:** The `actions/checkout@v4` step downloads your repository's code into the runner environment.
- **Install uv:** The `astral-sh/setup-uv@v4` action installs our package manager.
- **Set up Python:** The `actions/setup-python@v5` action installs the correct Python version. The `with: python-version-file: ".python-version"` line tells it to read the version from your `.python-version` file, ensuring consistency between local development and CI.
- **Install the project:** `uv sync --dev` installs all project dependencies, including development tools like `ruff` and `pre-commit`.
- **Format Check:** `uv run ruff format --check` verifies that all code follows consistent formatting rules without modifying any files.
- **Lint Check:** `uv run ruff check` detects code quality issues, unused imports, and potential bugs.

The `tests` job follows a similar setup process but with a few key differences. It runs `uv sync` without the `--dev` flag, as it only needs the application's core dependencies. The final step, `Run tests`, executes `CONFIG_FILE=configs/debug.yaml uv run pytest`. This command ensures that tests run with the fake model configuration, preventing any real LLM API calls during CI.

### Setting Up GitHub Actions for Your Repository

To use this workflow, create the directory `.github/workflows/` at the root of your repository. Inside, create a file named `ci.yml` and paste the configuration above. You will also need a `.python-version` file in your repository root specifying your Python version (e.g., `3.12`) and a `configs/debug.yaml` file that configures your agents to use fake models for testing. Once you commit and push this file, the workflow becomes active.

### Running the Pipeline and Observing Results

The pipeline runs automatically on every push or pull request that matches the trigger conditions. You can also trigger it manually from the "Actions" tab in your GitHub repository. Select the "CI" workflow, click "Run workflow," choose your branch, and start the run. This is useful for testing fixes without creating a new commit. To monitor a run, click on it in the Actions tab. You will see both the `qa` and `tests` jobs and their status. You can drill down into each job to see the logs for every step. If a step fails, its output is expanded and highlighted in red, making it easy to diagnose the problem.

### Interpreting CI Results and Fixing Issues

GitHub reports the status of each job with a green checkmark for success or a red X for failure and blocks pull requests from being merged if any checks fail. If the `qa` job fails on a formatting check, the logs will show which files need to be reformatted. You can fix this by running `make format-fix` locally, then committing and pushing the changes. If it fails on a linting check, the logs will detail each violation. Running `make lint-fix` will automatically correct many of these issues.

If the `tests` job fails, the `pytest` output will provide a traceback pointing to the exact test and assertion that failed. The principle is simple: **CI should run the exact same commands you run locally.** This eliminates "it works on my machine" issues. If your checks pass locally, they will pass in CI.

### Trying It Out

The best way to learn is by doing. Try intentionally introducing a formatting error, committing it, and opening a pull request. Watch the `qa` job fail, then fix it locally with `make format-fix` and push the change. The CI will re-run automatically and pass. This hands-on experience will solidify your understanding of how a robust CI pipeline protects your codebase.

The first two tiers of our CI model run on every commit, but ensuring semantic quality requires a more expensive third tier. This is where AI evaluations enter as selective regression tests.

## AI Evaluations as Regression Tests

AI evaluations are critical for catching semantic quality regressions that deterministic unit tests cannot, such as a drop in helpfulness or an increase in hallucination rates. They form the third tier of our CI model, providing a necessary quality gate before releasing changes to users [[15]](https://www.braintrust.dev/articles/best-ai-evals-tools-cicd-2025).

### Why AI Evals Are Unique to AI Systems

Unlike fast, free unit tests, each AI evaluation run makes real LLM calls, incurring both latency and token costs. A full run on a 500-example dataset where each example costs, say, $0.01 in tokens, would add up. This makes it impractical to run evals on every single commit. Instead, we treat them as a specialized, manually triggered gate. This selective approach balances the need for thorough quality checks with the practical constraints of cost and speed, ensuring that you get meaningful feedback without slowing down the entire development process [[18]](https://dev.to/kuldeep_paul/a-practical-guide-to-integrating-ai-evals-into-your-cicd-pipeline-3mlb).

### Manual-Trigger CI Workflow for AI Evals

To manage costs and speed, we run AI evaluations using a separate GitHub Actions workflow that is triggered manually. This pattern, configured with `workflow_dispatch`, ensures that expensive eval runs are intentional. Here is an illustrative example of what `.github/workflows/eval.yml` might look like [[19]](https://graphite.com/guides/github-actions-workflow-dispatch):

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

This workflow differs from our main `ci.yml` in a few key ways:
1.  The `on: workflow_dispatch:` trigger means it only runs when manually started from the GitHub Actions UI. This prevents accidental, costly runs on every commit.
2.  It uses a production configuration (`configs/production.yaml`), ensuring evaluations run against the real LLM models you use in production, not fakes.
3.  It securely accesses your `LLM_API_KEY` from GitHub Secrets. You must configure this in your repository settings under **Settings → Secrets and variables → Actions**. This keeps sensitive keys out of your version-controlled code.

To run this workflow, go to the "Actions" tab in your repository, select "AI Evaluations," and click the "Run workflow" button.

The frequency of running these evaluations depends on your project's maturity:
- **Early development:** During the initial phases, you might run evaluations manually once a week or after major architectural changes. The goal is to track progress on core metrics and validate that your agent is learning the desired behaviors.
- **Active development:** As your project matures, run evaluations before merging significant feature branches. This acts as a regression test, ensuring that new capabilities do not degrade existing ones. It is a crucial quality gate before code enters your main branch.
- **Mature product:** For a stable product, evaluations become a formal part of your release process. Running them before every deployment to production ensures that quality never degrades and that you can ship with confidence.

With all three tiers understood, we can now assemble them into a cohesive daily development workflow that keeps velocity high while protecting quality.

## Daily Development Workflow

With these CI tools and workflows in place, your daily development process becomes a tight, efficient loop that catches issues early and maintains high code quality. This structured approach gives you the confidence to iterate quickly without fear of introducing regressions.

1.  **Write code** and corresponding tests.
2.  **Run quick checks** periodically: `make lint-check` and `make format-check`.
3.  **Run tests** after changing logic: `make tests`.
4.  **Commit your changes.** Pre-commit hooks will run automatically.
5.  **Push and open a pull request.** CI runs automatically, enforcing all checks.
6.  **Before releasing, run AI evaluations** manually to check for quality regressions.

This workflow takes seconds for most commits and catches issues early. It transforms quality assurance from a manual, error-prone task into an automated, reliable process that is integrated directly into your development cycle.

We have now covered the full spectrum from theory to daily practice. The conclusion ties everything together.

## Conclusion

The three-tier CI model is a pragmatic adaptation of traditional software practices to the unique realities of LLM-powered systems. By layering fast, cheap checks with selective, expensive evaluations, you can maintain development velocity without sacrificing quality. The upfront investment in hooks, Ruff, mocked tests, and CI workflows pays off by catching regressions before they ever reach your customers. This is the foundational step that transforms fragile prototypes into reliable, production-grade AI agents. The practices established here are essential as we move toward full CI/CD integration, production monitoring, and cost optimization in future lessons.

## References

- [1] How to Build a Continuous Integration Pipeline for AI Agents
- [2] Non-Deterministic Systems
- [12] Unit Testing Custom Agents
- [14] CI/CD for Evals: Running prompt and agent regression tests in GitHub Actions
- [15] Best AI Eval Tools for CI/CD Pipelines (2026 Review)
- [18] A practical guide to integrating AI evals into your CI/CD pipeline
- [19] GitHub Actions workflow_dispatch guide
- [22] Automated Guard Rails for Vibe Coding
- [25] pre-commit
- [28] Ruff Docs
- [31] Testing AI Agents: A Guide for Developers
- [36] Quickstart for GitHub Actions
- [43] What is continuous integration?