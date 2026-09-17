# Continuous Integration for AI Agents

In our last few lessons, we built the foundation for production-grade AI systems. We used Opik for observability, created datasets for offline evaluation, and established an evaluation-driven development framework. With this visibility and a way to measure quality, we can now shift our focus to Continuous Integration (CI): the automated infrastructure that keeps your codebase maintainable and prevents regressions from reaching production.

With the problem and failure modes clear, we will now define what Continuous Integration means in an AI context and introduce the three-tier model that solves these issues.

## What is Continuous Integration?

Continuous Integration (CI) is the practice of frequently merging code changes into a shared repository, where automated checks run to catch integration issues early [[1]](https://www.atlassian.com/continuous-delivery/continuous-integration). This process prevents the classic "it works on my machine" problem by ensuring all code is validated in a consistent environment [[2]](https://octopus.com/devops/ci-cd).

However, CI for traditional software, which focuses on deterministic logic and code correctness, is not enough for AI agents. The fundamental shift is from validating code to ensuring **behavioral correctness** [[3]](https://galileo.ai/blog/continuous-integration-ci-ai-fundamentals). An AI agent is a complex system of code, prompts, data, and reasoning policies, where behavior can change even if the code does not [[4]](https://www.linkedin.com/posts/ypaulraj_migrating-from-a-microservices-based-distributed-activity-7346381227890798592-43gW). This introduces unique challenges. LLM calls are non-deterministic, meaning the same input can produce different outputs, making standard tests flaky and unreliable [[5]](https://www.guild.ai/glossary/non-deterministic-systems). Rapid prompt iteration can silently break an agent’s behavior, and the high cost of API calls makes running extensive tests on every commit impractical [[6]](https://agiflow.io/blog/effective-practices-for-mocking-llm-responses-during-the-software-development-lifecycle). Without a CI strategy tailored for AI, teams often face three common failure modes.

### Inconsistent Code Quality

Without automated checks, code style and formatting can drift across a team. Different developers might use different formatters or apply them inconsistently, leading to cluttered code. This creates unnecessary noise in code reviews, forcing reviewers to spend time on trivial style nitpicks instead of focusing on the logic of the change [[1]](https://www.atlassian.com/continuous-delivery/continuous-integration).

### Skipped Local Checks

When development velocity is high, manual quality gates are often the first thing to be skipped. A developer might forget to run the test suite before pushing a change, leading to a broken build in the main branch. This disrupts the entire team and erodes trust in the codebase. Automated enforcement is the only way to ensure quality checks are never bypassed [[7]](https://gatling.io/blog/ci-cd-best-practices).

### Flaky and Expensive Tests

The most common mistake when testing AI agents is to call real LLM APIs in the test suite. This approach is slow, expensive, and non-deterministic [[3]](https://galileo.ai/blog/continuous-integration-ci-ai-fundamentals). Tests can fail unpredictably due to network issues, rate limits, or slight variations in the model’s output, even with temperature set to zero [[5]](https://www.guild.ai/glossary/non-deterministic-systems). These flaky tests slow down the development cycle and make it impossible to get a reliable signal on code quality.

To address these challenges, we use a three-tier model that calibrates our checks by cost and speed.

<https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/6bf41859-7dd2-4a23-9a88-55720f54114e/image/w=1920,quality=90,fit=scale-down>
Image 1: A three-tier CI model for AI agents, showing the flow from commit checks to PR tests and finally to manual/release AI evaluations, with each tier distinctly colored.

### Tier 1: Formatting and Linting (Always Run)

These checks are fast, taking only seconds to run, and free, as they involve no API calls. They catch syntactic issues, enforce consistent code style, and are identical to the checks used in traditional CI.

### Tier 2: Unit and Integration Tests (Always Run)

These tests verify the deterministic logic of your agent, such as data parsing, schema validation, and state transitions, without calling external APIs. By mocking LLM responses, these tests run quickly (under a minute), are completely reliable, and provide a strong signal that your agent’s core logic is correct.

### Tier 3: AI Evaluations (Manual/Release)

This tier is unique to AI systems. It involves running expensive, LLM-based quality checks against a curated dataset to evaluate the agent's semantic quality. These AI evaluations, built on the offline datasets and Opik traces we covered in previous lessons, act as regression tests to catch degradations in behavior that unit tests cannot detect. Because they are slow and costly, we run them selectively, either manually before a major release or after a significant change to a prompt.

This lesson covers the CI essentials for building production-ready AI agents. We focus on practical techniques you will use daily: automated quality checks, testing with mocked LLMs, and structuring CI pipelines around cost constraints. We will not cover comprehensive DevOps topics like Kubernetes or Terraform. Instead, we will show you how to effectively move from prototype to production-ready agents.

We will cover:
*   Setting up pre-commit hooks to enforce code quality automatically.
*   Configuring Ruff for linting and formatting.
*   Writing unit tests for deterministic agent code with mocked LLM responses.
*   Building a CI pipeline that runs automatically on every change.
*   Using AI evaluations as selective regression tests in CI.

This lesson includes a hands-on notebook where you will practice running formatting checks, linting, and tests on Brown, our writing agent. With the three-tier model established, the fastest feedback comes from running the first tier locally before you even commit code; this is where pre-commit hooks come in.

## Pre-commit Hooks: Automated Local Guardrails

Pre-commit hooks are automated checks that run on your local machine every time you make a commit [[8]](https://pre-commit.com/). They act as local guardrails, providing immediate feedback and preventing poorly formatted or broken code from ever entering the shared repository [[9]](https://blog.gitguardian.com/automated-guard-rails-for-vibe-coding).

The `pre-commit` framework manages these Git hooks using a declarative YAML configuration [[8]](https://pre-commit.com/). You define the hooks you want to run in a `.pre-commit-config.yaml` file, and the framework handles the installation and execution. A key advantage of this framework is its multi-language support. It manages isolated environments for hooks written in any language, so a Python developer can run a Ruby-based linter without needing to install Ruby on their machine. These hooks often reference external repositories, allowing you to use community-maintained tools for popular linters and formatters without adding them as direct project dependencies.

### Brown’s Pre-commit Configuration

<aside>
💡

You can experiment with the code for this lesson in this [Colab](https://colab.research.google.com/github/louisfb01/agent-course-notebooks/blob/main/notebooks/lesson_31_notebook.ipynb#scrollTo=b30eba1a). Alternatively, you can find the code for this lesson in the notebook for Lesson 31 of the course GitHub repository.

</aside>

In our writing agent, Brown, we use a `.pre-commit-config.yaml` file to define our local checks.

```bash
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

Let's walk through each of these hooks:
*   **`validate-pyproject`**: This tool validates that your `pyproject.toml` file is structurally correct according to PEP standards. A malformed configuration file can break your entire project, so this simple check is a valuable safeguard.
*   **`prettier`**: A popular code formatter we use for configuration files like `.github/workflows/ci.yml`. Consistent formatting makes these files readable and reduces merge conflicts.
*   **`ruff-check` and `ruff-format`**: These hooks run Ruff, a modern Python linter and formatter. The `--fix` argument automatically corrects any fixable issues, while `--exit-non-zero-on-fix` ensures the hook fails even after auto-fixing. This forces you to review the changes, re-stage them, and commit again. As recommended by Ruff’s authors, `ruff-check` runs before `ruff-format`.

### Setting Up Pre-commit

In the `lessons/writing_workflow` repository, you can set up these hooks with just two commands.

```bash
# Install dependencies (includes pre-commit)
uv sync --dev

# Install the Git hooks
pre-commit install
```

The `pre-commit install` command creates a script at `.git/hooks/pre-commit`. From now on, every time you run `git commit`, these hooks will execute automatically. This setup process is idempotent; you only need to run it once per project clone. You can also trigger the hooks manually at any time to check all files in the repository, not just the ones you have staged.

```bash
# Run all hooks on all files
make pre-commit
```

The daily workflow is simple: you make your code changes, stage them with `git add`, and then run `git commit`. If any hooks fail, you review the errors, fix them, re-stage the files, and commit again. This tight feedback loop ensures that your code is always clean before it leaves your machine, saving time for both you and your code reviewers.

Pre-commit hooks often rely on fast tools like Ruff to do the actual work. Next, we will examine Ruff in more detail and show how to configure and run it both locally and in CI.

## Ruff: Fast Python Linting and Formatting

Ruff is an extremely fast Python linter and code formatter written in Rust [[10]](https://docs.astral.sh/ruff). It is designed to be a consolidated replacement for older tools like Black, isort, and Flake8, delivering sub-second performance even on large codebases [[11]](https://docs.astral.sh/ruff/faq). Ruff combines more than ten legacy linters into a single binary, which eliminates version conflicts and dramatically reduces CI times.

It is important to distinguish between its two main functions:
*   **Formatting** automatically rewrites your code to follow consistent style rules, such as indentation, line breaks, and quote style. It is opinionated and designed to be run without manual intervention.
*   **Linting** analyzes your code for bugs, suspicious patterns, and violations of best practices, such as unused variables or missing imports.

### Brown’s Ruff Configuration

Ruff is configured in the `pyproject.toml` file, which keeps all project settings in one place [[12]](https://betterstack.com/community/guides/scaling-python/pyproject-explained/). Here is the configuration from our `writing_workflow` project.

```bash
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
*   `target-version = "py312"` tells Ruff which Python version to use for syntax checks, ensuring compatibility.
*   `line-length = 140` sets the maximum line length for your code.
*   `select = ["F", "E", "I"]` enables specific rule sets: `F` for Pyflakes (catches common bugs like unused variables), `E` for pycodestyle (enforces PEP 8 style conventions), and `I` for isort (automatically organizes and sorts import statements).
*   `known-first-party = ["src", "tests"]` tells isort how to group your project-specific imports separately from third-party libraries, keeping your import blocks clean and organized.

We also use a `Makefile` to provide convenient shortcuts for running these checks.

```bash
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

Each target uses `uv run` to execute commands within the project’s virtual environment. This is managed automatically by `uv` and does not require manual activation, simplifying the workflow [[13]](https://devcenter.upsun.com/posts/why-python-developers-should-switch-to-uv/).

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

2.  Next, we check the file for formatting issues without modifying it.
    ```bash
    !uv run ruff format --check test_formatting.py
    ```
    It outputs:
    ```text
    Would reformat:  test_formatting.py
    1 file would be reformatted
    ```
    The `--check` flag reports that the file would be reformatted but does not make any changes.

3.  Now, we run the formatter to automatically fix the issues.
    ```bash
    !uv run ruff format test_formatting.py
    ```
    It outputs:
    ```text
    1 file reformatted
    ```

4.  If we inspect the file, we can see that Ruff has corrected all the spacing and style inconsistencies.
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

Now let's do the same for linting, which catches potential bugs and style violations.

1.  We create a file with several linting issues, including an unused import, a duplicate import, and an undefined variable.
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

2.  When we run the linter, it reports multiple errors.
    ```bash
    !uv run ruff check test_linting.py
    ```
    It outputs:
    ```text
    Found 7 errors.
    [ *] 4 fixable with the `--fix` option (1 hidden fix can be enabled with the `--unsafe-fixes` option).
    ```

3.  We run the linter with the `--fix` flag to automatically correct what it can.
    ```bash
    !uv run ruff check --fix test_linting.py
    ```
    It outputs:
    ```text
    Found 5 errors (3 fixed, 2 remaining).
    ```
    Ruff removes the unused and duplicate imports but leaves the logical errors, such as the undefined function, for you to fix manually.

Once formatting and linting guardrails are in place, our attention turns to verifying the deterministic logic inside your agent nodes; this is the role of unit tests.

## Unit Tests for Agent Repos

The core challenge of testing AI agents is the non-determinism of LLMs [[5]](https://www.guild.ai/glossary/non-deterministic-systems). Calling a real LLM API in your tests makes them slow, expensive, and flaky. A test might pass once and fail the next time, not because your code is wrong, but because the model returned a slightly different response or a rate limit was hit.

Unit tests solve this by verifying only the deterministic logic within your agent. This includes parts of your code that do not require a live LLM call [[14]](https://www.guild.ai/glossary/unit-testing-ai-agents), such as:
*   **Parsing and rendering:** Does your markdown loader correctly extract an article from a file?
*   **Schema validation:** Does your Pydantic model reject invalid data and accept valid data?
*   **Routing decisions:** Given a specific input, does your workflow route to the correct node?
*   **Utilities:** Do helper functions for text cleaning or data transformation work as expected?

### Unit Tests vs. Integration Tests

In traditional software, a **unit test** verifies a small, isolated piece of code, like a single function, while an **integration test** checks how multiple components work together. For AI agents, these lines blur. A single agent "node" might combine prompt templating, LLM interaction, and output parsing.

We take a pragmatic approach: if a test runs quickly with mocked dependencies and verifies deterministic logic, we consider it a unit test, even if it covers multiple internal components [[15]](https://docs.langchain.com/oss/python/langchain/test). The goal is to isolate the code you wrote from the external, non-deterministic LLM. This ensures your tests are fast, reliable, and repeatable [[16]](https://brightsec.com/blog/unit-testing-best-practices/).

The key is to mock the non-deterministic parts, primarily the LLM call itself. We do this through response injection, where we provide a pre-defined, "canned" response for the LLM to return. This is simpler and gives us more control than patching at the HTTP layer.

<aside>
💡
Another option to mock LLM calls in tests is HTTP mocking, where you intercept API requests and return canned responses using libraries like `responses` or `httpretty`. Some teams prefer fixture-based mocking with `pytest` fixtures and `unittest.mock.patch` to replace LLM calls with fixed outputs. There is also record and replay, which captures real API responses once and then replays them in tests using tools like VCR.py [[6]](https://agiflow.io/blog/effective-practices-for-mocking-llm-responses-during-the-software-development-lifecycle).
</aside>

### Our Implementation: The FakeModel Pattern

In our Brown agent, we implement response injection with a `FakeModel` class that is compatible with LangChain’s interface. This pattern has three parts:

1.  **Configuration specifies the fake model:** The `debug.yaml` configuration at `lessons/writing_workflow/configs/debug.yaml` sets all nodes to use `model_id: “fake”`.
2.  **Model factory returns FakeModel:** The model builder in `src/brown/models/get_model.py` returns a `FakeModel` instance when the configuration specifies it.
3.  **Tests inject specific responses:** The `FakeModel` in `src/brown/models/fake_model.py` extends LangChain’s `FakeListChatModel` and allows tests to inject a list of responses.

Here is a simplified version of our `FakeModel` implementation.

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

An instance of the `FakeModel` class takes a list of pre-scripted responses in its constructor. When `ainvoke()` is called, it returns and consumes the next response from the list. This design ensures that unit tests run with a fake model by default, and individual tests can inject specific responses when needed. This approach allows us to test how our agent logic handles different LLM outputs—including edge cases like empty strings or malformed JSON—without making a single real API call.

### Example: Testing Nodes with Mocked Responses

For nodes that call LLMs, you mock the responses. This test from `lessons/writing_workflow/tests/brown/nodes/test_article_writer.py` shows the pattern.

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

The test creates a mock JSON response, builds a fake model, injects the response into it, and then instantiates the `ArticleWriter` node with that model. The `@pytest.mark.asyncio` decorator tells `pytest` to run this test function in an asyncio event loop, which is necessary for our async agent code. The test then asserts that the `ArticleWriter` correctly parses the mock response and returns an `Article` object with the expected content. This pattern keeps the test fast, deterministic, and free.

### Running Brown’s Tests

To run Brown’s entire test suite, you can use the command from the `Makefile`.

```bash
# From the writing_workflow directory
make tests
```

This command runs `CONFIG_FILE=configs/debug.yaml uv run pytest`. The `debug.yaml` configuration ensures all tests use our fake models and never call real LLMs, keeping the test suite fast and reliable [[17]](https://docs.pytest.org/). The full suite of over 200 tests runs in less than a second, providing immediate feedback on every change.

Local tests and hooks give fast feedback, but enforcement at the repository level requires automated CI workflows that run on every pull request.

## CI Workflows: Automated Enforcement

GitHub Actions is our CI platform for both the Brown and Nova agents. It automatically triggers workflows on events like pull requests or pushes, runs jobs in isolated environments, and supports features like matrix builds and parallel execution to keep feedback fast. Its seamless integration with GitHub repositories requires minimal setup to get started.

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

This configuration defines when the workflow runs and what checks it performs. The `on` section specifies that the workflow triggers on pull requests to the `main` and `dev` branches, as well as on direct pushes to `main`. This ensures every code change is validated before it can be merged. The `env` section defines an environment variable, `QA_FOLDERS`, that lists all directories to check. This allows us to use the same CI configuration for both agents in our monorepo.

### Understanding the Job Structure

The workflow defines two independent jobs that run in parallel: `qa` and `tests`. Splitting them provides clear, fast feedback. If formatting fails, you immediately see "QA job failed" without waiting for tests to complete. This parallel execution saves time and makes it easier to identify which category of checks failed [[18]](https://dev.to/cicube/how-to-run-jobs-in-parallel-with-github-actions-4png). Each job runs on `ubuntu-latest`, a virtual machine provided by GitHub, and is completely isolated.

The `qa` job focuses on code quality. It starts by checking out your code with `actions/checkout@v4`, then installs `uv` using `astral-sh/setup-uv@v4`. This action not only installs `uv` but can also handle caching to speed up subsequent runs. The Python setup step uses `actions/setup-python@v5` and reads the version from your `.python-version` file, ensuring consistency between local development and CI. After syncing dependencies with `uv sync --dev` (which includes development tools), it runs two checks. The format check uses `uv run ruff format --check` to verify code formatting, and the lint check uses `uv run ruff check` to detect quality issues.

The `tests` job follows a similar setup but runs `uv sync` without the `--dev` flag, as tests do not require development tools. The final step runs the test suite using `CONFIG_FILE=configs/debug.yaml`, ensuring that all tests use the fake model configuration and no real LLM APIs are called. This is the most critical part of keeping our CI fast and reliable.

### Setting Up GitHub Actions for Your Repository

To enable this workflow, you need to create the `ci.yml` file in the `.github/workflows/` directory at the root of your repository. First, create the directory structure with `mkdir -p .github/workflows`, then create the `ci.yml` file and paste in the configuration above. Ensure your repository also has a `.python-version` file specifying the Python version (e.g., `3.12`) and a `configs/debug.yaml` file that configures your agents to use fake models for testing.

Once you commit and push this file, the workflow becomes active. No further configuration in the GitHub UI is needed for this basic setup, though you will need to add secrets for API keys in more advanced workflows. This "configuration as code" approach makes your CI pipeline version-controlled, reproducible, and easy to manage.

### Running the Pipeline and Observing Results

The pipeline runs automatically when its trigger conditions are met, such as opening a pull request or pushing to `main`. You can also trigger it manually from the "Actions" tab in your GitHub repository. Select the "CI" workflow, click "Run workflow," choose your branch, and confirm. This is useful for testing changes or re-running failed checks without creating a new commit.

To monitor a run, click on it in the Actions tab. The interface shows both jobs (`qa` and `tests`) and their status. You can drill down into each job to see the output of individual steps. If a step fails, its output is expanded and highlighted in red, making it easy to spot the problem. For example, a failing format check will show you exactly which files Ruff would reformat.

### Interpreting CI Results and Fixing Issues

The CI pipeline reports a success (green checkmark) or failure (red X) for each job. GitHub displays the overall status on your pull request and blocks merges when checks fail, acting as a quality gate.

If the `qa` job fails on a formatting check, the output will show which files need to be reformatted. You can fix this locally by running `make format-fix`, then committing and pushing the changes. If it fails on a linting check, the output will list each violation. Many of these can be fixed automatically with `make lint-fix`.

If the `tests` job fails, the `pytest` output will show a traceback for the failing test. This helps you identify the issue, whether it is a logic error, an incorrect mock response, or a missing dependency. You should fix the issue, verify it by running `make tests` locally, and then push your changes.

A critical principle is that CI should run the exact same commands you run locally. This eliminates "it works on my machine" problems. If your checks pass locally, they will pass in CI.

### Trying It Out

The best way to understand CI is to see it in action. Try introducing a formatting error, committing it, and opening a pull request. Watch the `qa` job fail, then fix it locally with `make format-fix`, push the change, and see the CI pipeline pass. You can also experiment with the manual trigger to get comfortable with the workflow. This hands-on experience will make the abstract concept of CI concrete and help you develop confidence in the system.

We have now covered the first two tiers of our CI model, which run on every commit. However, to ensure semantic quality, we need a more expensive third tier. This is where AI evaluations enter as selective regression tests.

## AI Evaluations as Regression Tests

AI evaluations catch semantic regressions—like a drop in helpfulness or an increase in hallucinations—that deterministic unit tests cannot detect [[19]](https://kinde.com/learn/ai-for-software-engineering/ai-devops/ci-cd-for-evals-running-prompt-and-agent-regression-tests-in-github-actions). They form the third and most specialized tier of our CI strategy. It is also important to distinguish between **outcome grading** (did the agent achieve its goal?) and **transcript grading** (was the reasoning plausible?). While both are useful, only outcome grading confirms real-world success [[3]](https://galileo.ai/blog/continuous-integration-ci-ai-fundamentals).

### Why AI Evals Are Unique to AI Systems

Evaluations are unique to AI systems because they involve real LLM calls, which are both slow and costly. A single evaluation run can take several minutes and incur significant API costs. For example, running an evaluation on a 500-example dataset where each run consumes 2,000 tokens at a rate of $0.50 per million tokens would cost $0.50 per run. While this may seem small, running it on every commit would quickly add up. This is why we treat them as a Tier 3 gate, to be used selectively.

### Manual-Trigger CI Workflow for AI Evals

To manage costs, we run AI evaluations using a separate CI workflow that is triggered manually, not automatically on every commit. This pattern, using `workflow_dispatch`, prevents accidental or unnecessary runs. Here is an example of what this workflow, located at `.github/workflows/eval.yml`, could look like.

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
1.  The `workflow_dispatch` trigger ensures it only runs when you manually start it from the "Actions" tab in GitHub.
2.  It uses a production configuration (`configs/production.yaml`), which means it calls real LLM models instead of our fake ones.
3.  The `LLM_API_KEY` is pulled from GitHub Secrets, which you can configure in your repository settings under **Settings → Secrets and variables → Actions**. This keeps your API keys secure.

To trigger this workflow, you navigate to the Actions tab, select "AI Evaluations," click "Run workflow," choose your branch, and confirm. The workflow will then run your evaluation script and report the results in the Actions interface.

The frequency of these runs depends on your project's maturity:
*   **Early development:** Run evaluations manually to measure progress weekly or after major architectural changes.
*   **Active development:** Run them before merging significant changes, like a major prompt refactor, to catch any regressions.
*   **Mature product:** Run them as a required step in your release process to ensure production quality never degrades.

The most effective evaluation suites evolve. Each production failure should be encoded into a new test, ensuring the regression suite captures real-world failure modes and grows over time [[20]](https://galileo.ai/blog/ai-agent-metrics).

With all three tiers understood, we can now assemble them into a cohesive daily development workflow that keeps velocity high while protecting quality.

## Daily Development Workflow

With these tools in place, a typical daily workflow looks like this:

1.  **Write code** and corresponding unit tests for any new logic.
2.  **Run quick checks** locally as you work: `make lint-check` and `make format-check`.
3.  **Run tests** after changing logic to ensure you have not broken anything: `make tests`.
4.  **Commit your changes.** The pre-commit hooks will run automatically, providing a final quality gate.
5.  **Push and open a pull request.** The main CI workflow will run automatically, enforcing all checks for the entire team.
6.  **Before releasing, run AI evaluations** manually to check for any semantic quality regressions.

This workflow takes seconds for most commits and catches issues at the earliest possible stage, keeping your development cycle fast and your codebase clean. We have now covered the full spectrum from theory to daily practice; the conclusion ties everything together.

## Conclusion

The three-tier CI model adapts software engineering for the realities of LLMs: non-determinism, prompt volatility, and cost. This investment in hooks, tests, and selective evaluations moves projects from fragile prototypes to reliable production systems. These practices form the foundation for full CI/CD and monitoring, where CI evals can extend into runtime guardrails protecting live users [[3]](https://galileo.ai/blog/continuous-integration-ci-ai-fundamentals).

## References

- [1] [What is continuous integration? | Atlassian](https://www.atlassian.com/continuous-delivery/continuous-integration)
- [2] [What is CI/CD? - Octopus Deploy](https://octopus.com/devops/ci-cd)
- [3] [How to Build a Continuous Integration Pipeline for AI Agents](https://galileo.ai/blog/continuous-integration-ci-ai-fundamentals)
- [4] [CI/CD Pipelines Must Evolve to Govern AI Agents](https://www.linkedin.com/posts/ypaulraj_migrating-from-a-microservices-based-distributed-activity-7346381227890798592-43gW)
- [5] [Non-Deterministic Systems](https://www.guild.ai/glossary/non-deterministic-systems)
- [6] [Effective Practices for Mocking LLM Responses During the Software Development Lifecycle | Agiflow Blog](https://agiflow.io/blog/effective-practices-for-mocking-llm-responses-during-the-software-development-lifecycle)
- [7] [CI/CD Best Practices for a More Efficient Workflow - Gatling](https://gatling.io/blog/ci-cd-best-practices)
- [8] [pre-commit](https://pre-commit.com/)
- [9] [Automated guard rails for vibe coding](https://blog.gitguardian.com/automated-guard-rails-for-vibe-coding)
- [10] [Ruff](https://docs.astral.sh/ruff/)
- [11] [Ruff: FAQ](https://docs.astral.sh/ruff/faq)
- [12] [pyproject.toml explained](https://betterstack.com/community/guides/scaling-python/pyproject-explained/)
- [13] [Why Python developers should switch to uv](https://devcenter.upsun.com/posts/why-python-developers-should-switch-to-uv/)
- [14] [Unit Testing AI Agents](https://www.guild.ai/glossary/unit-testing-ai-agents)
- [15] [Testing](https://docs.langchain.com/oss/python/langchain/test)
- [16] [Unit testing best practices: 13 ways to improve your tests](https://brightsec.com/blog/unit-testing-best-practices/)
- [17] [pytest documentation](https://docs.pytest.org/)
- [18] [How to run jobs in parallel with GitHub Actions](https://dev.to/cicube/how-to-run-jobs-in-parallel-with-github-actions-4png)
- [19] [CI/CD for Evals: Running prompt and agent regression tests in GitHub Actions](https://kinde.com/learn/ai-for-software-engineering/ai-devops/ci-cd-for-evals-running-prompt-and-agent-regression-tests-in-github-actions)
- [20] [Key Metrics for Evaluating AI Agent Performance](https://galileo.ai/blog/ai-agent-metrics)
- [21] [Lesson 31: Continuous Integration (CI) for AI Engineering](https://colab.research.google.com/github/louisfb01/agent-course-notebooks/blob/main/notebooks/lesson_31_notebook.ipynb#scrollTo=b30eba1a)
- [22] [LLM evaluation for CI/CD pipelines](https://www.deepchecks.com/llm-evaluation/ci-cd-pipelines/)
- [23] [Integration with GitHub Actions, uv docs](https://docs.astral.sh/uv/guides/integration/github/)
- [24] [Integration with pre-commit, uv docs](https://docs.astral.sh/uv/guides/integration/pre-commit/)
- [25] [GitHub Actions documentation](https://docs.github.com/en/actions)
- [26] [Ruff pre-commit](https://github.com/astral-sh/ruff-pre-commit)
- [27] [Ruff Linter](https://docs.astral.sh/ruff/linter/)
- [28] [A practical guide to integrating AI evals into your CI/CD pipeline](https://dev.to/kuldeep_paul/a-practical-guide-to-integrating-ai-evals-into-your-cicd-pipeline-3mlb)
- [29] [Deterministic vs. Non-Deterministic vs. Probabilistic AI: What AppSec Teams Need to Know](https://cycode.com/blog/deterministic-vs-non-deterministic-vs-probabilistic-ai-appsec)
- [30] [AI Agents - S2E10 - Evals for Monitoring and CI/CD](https://www.youtube.com/watch?v=4u64WEuQHYE&vl=en)
- [31] [The Double-Edged Sword: AI's Non-Determinism in Software and IT](https://codenotary.com/blog/the-double-edged-sword-ais-non-determinism-in-software-and-it)
- [32] [Effective Practices for Mocking LLM Responses During the Software Development Lifecycle](https://home.mlops.community/public/blogs/effective-practices-for-mocking-llm-responses-during-the-software-development-lifecycle)
- [33] [langchain_contrib.llms.fake module](https://langchain-contrib.readthedocs.io/en/latest/llms/fake.html)
- [34] [Unit Testing Custom LangChain Agents](https://www.iamraghuveer.com/posts/unit-testing-custom-agents)
- [35] [Fake Chat Model](https://docs.langchain.com/oss/javascript/integrations/chat/fake)
- [36] [Best AI Eval Tools for CI/CD Pipelines (2026 Review) - Articles - Braintrust](https://www.braintrust.dev/articles/best-ai-evals-tools-cicd-2025)
- [37] [What is AI Regression Testing, and How Does It Work?](https://testgrid.io/blog/what-is-ai-regression-testing)
- [38] [Manually triggering a workflow with workflow_dispatch in GitHub Actions](https://graphite.com/guides/github-actions-workflow-dispatch)
- [39] [Manually running a workflow - GitHub Docs](https://docs.github.com/actions/managing-workflow-runs/manually-running-a-workflow)
- [40] [Run evaluation on an AI agent flow with GitHub Action - Azure AI Studio](https://learn.microsoft.com/en-us/azure/foundry/how-to/evaluation-github-action)
- [41] [Local Guardrails for Secrets Security](https://blog.gitguardian.com/local-guardrails-for-secrets-security)
- [42] [pre-commit/pre-commit-hooks: Some out-of-the-box hooks for pre-commit](https://github.com/pre-commit/pre-commit-hooks)
- [43] [Git Hooks Tutorial | Atlassian Git Tutorial](https://www.atlassian.com/git/tutorials/git-hooks)
- [44] [astral-sh/ruff: An extremely fast Python linter and code formatter, written in Rust.](https://github.com/astral-sh/ruff)
- [45] [Testing AI Agents: A Guide for Developers](https://oneuptime.com/blog/post/2026-01-30-agent-testing/view)
- [46] [4 Frameworks to Test Non-Deterministic AI Agents](https://datagrid.com/blog/4-frameworks-test-non-deterministic-ai-agents)
- [47] [A First Look at Unit Testing in the AI Era](https://arxiv.org/html/2509.19185v1)
- [48] [Unit Testing for AI Systems: A Practical Guide](https://galileo.ai/blog/unit-testing-ai-systems)
- [49] [YAML and GitHub Actions](https://intersect-training.org/CI-CD/yaml-and-github-actions.html)
- [50] [Quickstart for GitHub Actions - GitHub Docs](https://docs.github.com/actions/get-started/quickstart)
- [51] [Week 8: Diving into CI/CD, GitHub Actions, and a little Lambda Magic](https://medium.com/@donovan.brown_75022/week-8-diving-into-ci-cd-github-actions-and-a-little-lambda-magic-997cf8a1e193)
- [52] [How Sotheby’s uses GitHub Actions to automate its development workflow](https://github.com/readme/guides/sothebys-github-actions)
- [53] [CI/CD for reliable delivery of agentic AI](https://developers.redhat.com/articles/2026/05/18/ci-cd-delivery-agentic-ai)
- [54] [What is Continuous Integration (CI)?](https://www.ibm.com/think/topics/continuous-integration)
- [55] [CI/CD Best Practices for Data Projects: Validation and Testing](https://www.sunnydata.ai/blog/cicd-best-practices-data-projects-validation-testing)
- [56] [AI Maturity Assessment Framework: A Guide for Businesses - Ness](https://www.ness.com/blog/ai-maturity-assessment-framework)
- [57] [MITRE AI Maturity Model and Organizational Assessment Tool Guide](https://www.mitre.org/news-insights/publication/mitre-ai-maturity-model-and-organizational-assessment-tool-guide)
- [58] [Assess Your AI Maturity](https://www.infotech.com/research/ss/assess-your-ai-maturity)
- [59] [AI Maturity Model for 2026: A Practical Guide](https://sema4.ai/blog/ai-maturity-model-2026)
- [60] [OWASP AI Maturity Assessment (AIMA) | OWASP Foundation](https://owasp.org/www-project-ai-maturity-assessment)