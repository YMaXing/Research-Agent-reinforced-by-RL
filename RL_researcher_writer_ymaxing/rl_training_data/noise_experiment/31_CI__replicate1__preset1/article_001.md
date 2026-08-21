# CI for AI Agents: From Prototypes to Production

In our recent lessons, we integrated Opik for observability, built offline evaluation datasets, and adopted an evaluation-driven development framework. These steps give you the visibility to understand how your agent behaves. Now, it is time to shift our focus to Continuous Integration (CI), the automated infrastructure that keeps your codebase maintainable and prevents regressions from reaching production.

With the problem and failure modes clear, we will now define what Continuous Integration means in an AI context and introduce the three-tier model that solves these issues.

## What is Continuous Integration?

Continuous Integration is the practice of frequently merging code changes into a shared repository, where automated checks run to catch integration issues early. It is a primary DevOps best practice that allows developers to merge small, frequent updates to a central "trunk" or main branch, with automated tools verifying the new code's correctness before integration. This prevents the classic "it works on my machine" problem by ensuring all code is validated in a clean, consistent environment before it affects other team members [[1]](https://www.atlassian.com/continuous-delivery/continuous-integration).

However, the CI pipelines that work for traditional software are not enough for AI agents. Traditional CI focuses on deterministic logic, running compile checks and unit tests where the same input always produces the same output. AI agents break this assumption. Their behavior is shaped by non-deterministic LLM calls, and a small prompt change can silently degrade the semantic quality of the output. Furthermore, running tests that make real API calls is slow, expensive, and introduces flakiness, making naive test suites impractical [[2]](https://galileo.ai/blog/continuous-integration-ci-ai-fundamentals), [[3]](https://www.guild.ai/glossary/non-deterministic-systems).

Without CI adapted for AI, teams often fall into three failure modes.

1.  **Inconsistent code formatting across the team.** When team members use different formatters or rely on manual formatting, the codebase becomes cluttered with inconsistent styles. This leads to time-wasting code reviews focused on trivial nitpicks instead of meaningful logic, slowing down the entire development cycle.
2.  **Skipped pre-commit checks, leading to CI failures.** Under pressure to ship features quickly, developers might forget to run local quality checks like tests or linters before pushing code. Without automated enforcement, these skipped gates lead to broken builds and CI failures that block the entire team until the issues are resolved.
3.  **Non-deterministic tests that call real LLM APIs.** Tests that rely on live LLM calls are inherently flaky. The same test can pass once and fail the next time due to model variability, network issues, or rate limits. These unreliable tests slow down development, erode trust in the test suite, and add unnecessary costs with every run.

To address these challenges, we use a three-tier model calibrated by cost and speed.

*   **Tier 1: Formatting and Linting (Always Run).** These checks are fast, taking only seconds to run, and cheap, as they involve no API calls. They catch syntactic issues and enforce style consistency across the codebase. This tier is identical to traditional CI and provides the first, quickest layer of feedback.
*   **Tier 2: Unit and Integration Tests (Always Run).** These tests verify the deterministic logic of your agent, such as data parsing, schema validation, and workflow routing, without calling external APIs. By mocking LLM responses, these tests run quickly (under a minute) and reliably, ensuring the core mechanics of your agent are sound.
*   **Tier 3: AI Evaluations (Manual/Release).** This tier is unique to AI systems. It involves running expensive, LLM-based quality checks that use real API calls to evaluate the semantic quality of your agent on a curated dataset. We run these evaluations selectively before major releases or after significant prompt changes to catch regressions in behavior that unit tests cannot.![A three-tier CI model for AI agents, showing the flow from commit checks to PR tests and finally to manual/release AI evaluations, with each tier distinctly colored.](https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/6bf41859-7dd2-4a23-9a88-55720f54114e/image/w=1920,quality=90,fit=scale-down)

Image 1: A three-tier CI model for AI agents, showing the flow from commit checks to PR tests and finally to manual/release AI evaluations, with each tier distinctly colored.

This lesson covers the CI essentials for building production-ready AI agents. We focus on practical techniques you will use daily: automated quality checks, testing with mocked LLMs, and structuring CI pipelines around cost constraints. We will not cover comprehensive DevOps topics like Kubernetes or Terraform. Instead, we teach you how to effectively move from prototype to production-ready agents.

We will cover:
*   Setting up pre-commit hooks to enforce code quality automatically.
*   Configuring Ruff for linting and formatting.
*   Writing unit tests for deterministic agent code with mocked LLM responses.
*   Building a CI pipeline that runs automatically on every change.
*   Using AI evaluations as selective regression tests in CI.

This lesson includes a hands-on notebook where you will practice running formatting checks, linting, and tests on Brown, our writing agent.

With the three-tier model established, the fastest feedback comes from running the first tier locally before you even commit code. This is where pre-commit hooks come in.

## Pre-commit Hooks: Automated Local Guardrails

Pre-commit hooks are local guardrails that run automatically every time you make a commit. They provide immediate feedback on your code, catching issues like formatting errors or failing tests before they ever enter the shared repository. This prevents bad code from breaking the main build and disrupting the team's workflow [[4]](https://pre-commit.com/).

The `pre-commit` framework manages these Git hooks through a declarative YAML configuration file, `.pre-commit-config.yaml`. In this file, you define the hooks you want to run, which are often references to external repositories maintained by the community for popular tools. The framework handles the installation and execution of these hooks for you, creating isolated environments for each tool to prevent dependency conflicts.

<aside>
💡
You can experiment with the code for this lesson in this [Colab](https://colab.research.google.com/github/louisfb01/agent-course-notebooks/blob/main/notebooks/lesson_31_notebook.ipynb#scrollTo=b30eba1a).
Alternatively, you can find the code for this lesson in the notebook for Lesson 31 of the course GitHub repository.
</aside>

### Brown’s Pre-commit Configuration

In our Brown agent, we use a set of pre-commit hooks to automate our Tier 1 checks. Here is the configuration from `lessons/writing_workflow/.pre-commit-config.yaml`.

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

Let's walk through each hook.
*   **`validate-pyproject`**: This tool validates that your `pyproject.toml` file is structurally correct according to PEP standards. A malformed configuration file can break your entire project, so this check is a simple but important safeguard.
*   **`prettier`**: A popular code formatter that we use for configuration files like `.github/workflows/ci.yml`. Enforcing consistent formatting makes these files easier to read and helps reduce merge conflicts.
*   **`ruff-check` and `ruff-format`**: These hooks run Ruff, a modern Python linter and formatter. The `--fix` argument automatically corrects any fixable issues, while `--exit-non-zero-on-fix` ensures the hook fails even after auto-fixing. This forces you to review the changes made by the tool, re-stage them, and commit again. As recommended by Ruff’s authors, the `ruff-check` hook runs before `ruff-format`.

### Setting Up Pre-commit

In the `lessons/writing_workflow` repository, you can set up pre-commit hooks with these commands.

1.  First, install the project's dependencies, which include `pre-commit`.
    ```bash
    # Install dependencies (includes pre-commit)
    uv sync --dev
    ```
2.  Next, install the Git hooks into your local repository.
    ```bash
    # Install the Git hooks
    pre-commit install
    ```
    The `pre-commit install` command creates a script at `.git/hooks/pre-commit`. Now, every time you run `git commit`, these hooks will execute automatically. You can also run them manually on all files.
    ```bash
    # Run all hooks on all files
    make pre-commit
    ```
The workflow is simple: make your changes, stage them with `git add`, and then run `git commit`. If any hooks fail, you will see the errors in your terminal. You can then fix the issues, re-stage the files, and commit again. This tight feedback loop ensures that only high-quality code makes it into your repository.

Pre-commit hooks often rely on fast tools like Ruff to do the actual work. Next, we will examine Ruff in depth and show how to configure and run it both locally and in CI.

## Ruff: Fast Python Linting and Formatting

Ruff is a Python linter and code formatter written in Rust. It is designed to be extremely fast, often 10-100 times faster than the tools it replaces, such as Black, isort, and Flake8. By consolidating the functionality of over ten legacy tools into a single binary, Ruff simplifies configuration, eliminates version conflicts, and dramatically reduces CI run times [[5]](https://docs.astral.sh/ruff).

It is important to distinguish between its two main functions.
*   **Formatting** automatically rewrites your code to follow a consistent style, enforcing rules for indentation, line breaks, and spacing. It is opinionated and designed to be run without manual intervention.
*   **Linting** analyzes your code for potential bugs, suspicious patterns, and violations of best practices, such as unused variables or missing imports. It identifies problems but does not always fix them automatically.

### Brown’s Ruff Configuration

Ruff is configured in the `pyproject.toml` file, which keeps all project settings in one place. Here is the configuration from `lessons/writing_workflow/pyproject.toml`.

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

*   `target-version = "py312"` tells Ruff to check for syntax compatibility with Python 3.12.
*   `line-length = 140` sets the maximum line length for formatting.
*   `select = ["F", "E", "I"]` enables three sets of linting rules: `F` for Pyflakes (catches common bugs), `E` for pycodestyle (enforces PEP 8 style), and `I` for isort (organizes imports).
*   `known-first-party = ["src", "tests"]` helps isort correctly group your project's internal imports separately from third-party libraries.

For convenience, our `Makefile` includes shortcuts for running Ruff.

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

Each target uses `uv run` to execute commands within the project’s virtual environment, which is managed automatically and does not require manual activation. You can run these from the `writing_workflow/` directory to check or fix your code before committing.

### Hands-On Example: Fixing Formatting Issues

Let's see Ruff's formatter in action.

1.  First, create a Python file with several formatting issues.
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
2.  Now, run the format check command. The `--check` flag tells Ruff to report issues without modifying the file.
    ```bash
    uv run ruff format --check test_formatting.py
    ```
    It outputs:
    ```text
    Would reformat: test_formatting.py
    1 file would be reformatted
    ```
3.  To fix the issues, run the command without the `--check` flag.
    ```bash
    uv run ruff format test_formatting.py
    ```
    It outputs:
    ```text
    1 file reformatted
    ```
    Ruff has now fixed all the spacing and formatting inconsistencies.

### Hands-On Example: Fixing Linting Issues

Now let's try the linter.

1.  Create a file with common linting errors like unused imports and undefined variables.
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
2.  Run the lint checker to see the errors.
    ```bash
    uv run ruff check test_linting.py
    ```
    It outputs:
    ```text
    I001 [*] Import block is un-sorted or un-formatted
     --> test_linting.py:1:1
    ...
    F401 [*] `json` imported but unused
     --> test_linting.py:3:8
    ...
    F821 Undefined name `some_undefined_function`
      --> test_linting.py:18:26
    ...
    F811 [*] Redefinition of unused `sys` from line 2
      --> test_linting.py:21:8
    ...
    Found 7 errors.
    [*] 4 fixable with the `--fix` option...
    ```
3.  Run the linter with the `--fix` flag to automatically correct the fixable errors.
    ```bash
    uv run ruff check --fix test_linting.py
    ```
    It outputs:
    ```text
    ...
    Found 5 errors (3 fixed, 2 remaining).
    ```
    Ruff removes the unused and duplicate imports but leaves the `Undefined name` error, as that is a logic issue that requires manual intervention.

Once formatting and linting guardrails are in place, our attention turns to verifying the deterministic logic inside the agent nodes. This is the role of unit tests.

## Unit Tests for Agent Repos

The core challenge in testing AI agents is the non-determinism of LLMs. Making live API calls in tests is slow, expensive, and flaky, as identical prompts can yield different outputs. This makes it impossible to write reliable assertions for tests that depend on a real LLM [[3]](https://www.guild.ai/glossary/non-deterministic-systems).

The solution is to separate the deterministic logic of your agent from the non-deterministic LLM calls. Unit tests should focus exclusively on the deterministic parts of your code, such as data parsing, schema validation, routing decisions, and utility functions.

*   **Parsing and rendering:** Does your markdown loader extract articles correctly?
*   **Schema validation:** Does your Pydantic model reject invalid data?
*   **Routing decisions:** Given a specific state, does your workflow route to the correct node?
*   **Utilities:** Do helper functions for URL extraction or text cleaning work correctly?

These components can be tested reliably without ever calling an LLM.

### Unit Tests vs. Integration Tests

In traditional software, a **unit test** verifies a small, isolated piece of code, like a single function. An **integration test** checks how multiple components work together. For AI agents, these lines blur. A single agent node might combine prompt templating, structured output parsing, and routing logic.

We take a pragmatic approach: if a test runs quickly with mocked dependencies and verifies deterministic logic, we consider it a unit test, even if it touches multiple internal components. This allows us to test the logic of our agent nodes in isolation from the LLM.

To achieve this, we need a strategy for mocking LLM responses. While some teams use HTTP mocking libraries like `responses` or record-and-replay tools like `VCR.py`, we prefer response injection. This involves using a fake model class that returns pre-scripted responses, giving us a good balance of simplicity and control.

<aside>
💡
Another option to mock LLM calls in tests is HTTP mocking, where you intercept API requests and return canned responses using libraries like `responses` or `httpretty`. Some teams prefer fixture-based mocking with `pytest` fixtures and `unittest.mock.patch` to replace LLM calls with fixed outputs. There is also record and replay with tools like `VCR.py`, which records a real API interaction to a file once and then replays that exact response on subsequent test runs, ensuring deterministic behavior without live calls [[6]](https://agiflow.io/blog/effective-practices-for-mocking-llm-responses-during-the-software-development-lifecycle).
</aside>

### Our Implementation: The FakeModel Pattern

In our Brown agent, we implement response injection with a `FakeModel` class that is compatible with LangChain’s interface. This pattern has three parts.

1.  **Configuration specifies the fake model:** The `debug.yaml` configuration at `lessons/writing_workflow/configs/debug.yaml` sets all nodes to use `model_id: “fake”`.
2.  **Model factory returns FakeModel:** The model builder in `src/brown/models/get_model.py` returns a `FakeModel` instance when the configuration specifies it.
3.  **Tests inject specific responses:** The `FakeModel` in `src/brown/models/fake_model.py` extends LangChain’s `FakeListChatModel` and allows tests to inject a list of responses.

Here is the implementation of the `FakeModel` class.

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

An instance of the `FakeModel` class takes a list of pre-scripted responses in its constructor. When `ainvoke()` is called, it returns the first response from the list and consumes it. This design ensures that our unit tests use a fake model by default, and individual tests can inject specific responses when needed.

### Example: Testing Nodes with Mocked Responses

Here is an example from `lessons/writing_workflow/tests/brown/nodes/test_article_writer.py` that shows how we test the `ArticleWriter` node.

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

The test defines a mock JSON response, builds a `FakeModel` instance, injects the response into it, and then instantiates the `ArticleWriter` node with that fake model. When `writer.ainvoke()` is called, it receives the mock response instead of calling a real LLM. This allows us to assert that the node correctly parses the response and produces the expected `Article` object. This pattern keeps our tests fast, deterministic, and free.

### Running Brown’s Tests

To run the complete test suite for our Brown agent, you can use the shortcut defined in the `Makefile`.

```bash
# From the writing_workflow directory
make tests
```

This command runs `CONFIG_FILE=configs/debug.yaml uv run pytest`. The `CONFIG_FILE` environment variable ensures that our tests always use the `debug.yaml` configuration, which is set up to use fake models. This prevents any accidental calls to real LLM APIs during testing. The test suite is comprehensive, covering domain models, agent nodes, utilities, and evaluation logic, all without requiring API keys.

Local tests and hooks give fast feedback, but enforcement at the repository level requires automated CI workflows that run on every pull request.

## CI Workflows: Automated Enforcement

GitHub Actions is the CI platform we use for both our Brown and Nova agents. It integrates seamlessly with GitHub repositories, requires minimal setup, and provides powerful features for automating workflows. It can trigger jobs on events like pull requests or pushes, run jobs in isolated environments, and execute jobs in parallel to provide fast feedback.

### Our Complete CI Configuration

Our entire CI workflow is defined in a single YAML file located at `.github/workflows/ci.yml`.

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

This configuration defines when the workflow runs and what checks it performs. The `on` section specifies that the workflow triggers on pull requests targeting the `main` and `dev` branches, as well as on direct pushes to `main`. This ensures every code change is validated before it can be merged.

The `env` section defines an environment variable, `QA_FOLDERS`, that lists all the directories we want to check. Notice it includes both `src/brown` and `src/nova`, allowing us to use the same CI configuration for both agents in a monorepo structure.

### Understanding the Job Structure

The workflow defines two independent jobs that run in parallel: `qa` and `tests`. Splitting them provides clear, fast feedback. If formatting fails, you immediately see "QA job failed" without waiting for tests to complete. This parallel execution saves time and makes it easier to identify which category of checks failed [[7]](https://intersect-training.org/CI-CD/yaml-and-github-actions.html).

Each job runs on `ubuntu-latest`, a virtual machine provided by GitHub. The jobs are completely isolated from each other, which means they can run simultaneously without interference.

The `qa` job focuses on code quality checks that do not require running the application. It starts by checking out your code with `actions/checkout@v4`, then installs `uv` using `astral-sh/setup-uv@v4`. The Python setup step uses `actions/setup-python@v5` and reads the Python version from your `.python-version` file, ensuring consistency between local development and CI. After syncing dependencies with `uv sync --dev`, which includes development dependencies needed for formatting and linting, it runs two checks. The format check uses `uv run ruff format --check` to verify that all code follows consistent formatting rules without modifying any files. The lint check uses `uv run ruff check` to detect code quality issues, unused imports, and potential bugs.

The `tests` job follows a similar setup process. It runs `uv sync` without the `--dev` flag since tests do not require development tools like formatters. The test step uses `CONFIG_FILE=configs/debug.yaml` to ensure tests run with the fake model configuration, preventing any real LLM API calls during CI. This keeps tests fast, deterministic, and free.

### Setting Up GitHub Actions for Your Repository

To enable this CI workflow in your repository, you need to create the workflow file in the correct location. GitHub Actions looks for workflow files in the `.github/workflows/` directory at the root of your repository.

First, create the directory structure if it does not already exist. From your repository root, run `mkdir -p .github/workflows`. Then, create the file `.github/workflows/ci.yml` and paste the complete configuration shown above. Make sure your repository has a `.python-version` file at the root that specifies which Python version to use, such as `3.12`. You should also ensure that `configs/debug.yaml` exists and configures your agents to use fake models for testing.

Once you commit and push this file to GitHub, the workflow becomes active immediately. You do not need to configure anything in the GitHub UI for basic workflows, though you will need to add secrets for more advanced scenarios, such as API keys for evaluation workflows.

### Running the Pipeline and Observing Results

The pipeline runs automatically whenever its trigger conditions are met. When you push a commit directly to the `main` branch, GitHub Actions executes the workflow within seconds. When you open a pull request targeting `main` or `dev`, the workflow runs automatically and reports its status on the pull request page.

You can also trigger the workflow manually to test changes or re-run failed checks. Navigate to your repository on GitHub and click the "Actions" tab at the top. You will see a list of all your workflows. Click on "CI" to view all runs of this workflow. In the top right corner, you will see a "Run workflow" button. Click it, select the branch you want to run the workflow on, and click the green "Run workflow" button. This is particularly useful when you want to verify that a fix works without creating a new commit or pull request.

To monitor a workflow run, click any run in the list to view its details. The interface shows both jobs (`qa` and `tests`) with their current status. You can click each job to view the output of its individual steps. If a step fails, its output is expanded automatically and highlighted in red, making it easy to identify the problem. The format and lint checks show exactly which files have issues and what needs to be fixed.

### Interpreting CI Results and Fixing Issues

When the CI pipeline runs, it produces one of three outcomes for each job: success (a green checkmark), failure (a red X), or in progress (a yellow dot). GitHub also displays the overall status on your pull request, preventing merges when checks fail.

If the `qa` job fails due to formatting, the output shows which files would be reformatted and exactly what changes Ruff would make to them. You can fix this locally by running `make format-fix` from the `writing_workflow/` directory, then committing and pushing the formatted code. If the `qa` job fails on linting, the output lists each violation with its file location, line number, and error code. Many of these can be auto-fixed by running `make lint-fix` locally.

If the `tests` job fails, the `pytest` output shows which test failed and why. The traceback helps you identify the issue, whether it is a logic error, an incorrect mock response, or a missing dependency. You should fix the underlying issue, verify the fix by running `make tests` locally, then push your changes.

A critical principle is that CI should run the exact same commands you run locally. The `qa` job executes `uv run ruff format --check` and `uv run ruff check`, which are identical to the targets your `Makefile` runs. The `tests` job runs `CONFIG_FILE=configs/debug.yaml uv run pytest`, which is exactly what `make tests` does. This eliminates "works on my machine" problems. If tests pass locally with `make tests`, they will pass in CI, and if they fail in CI, you can reproduce the failure locally by running the same command.

### Trying It Out

The best way to understand how CI works is to intentionally trigger a failure and observe the results. Try introducing a formatting violation by creating a file with inconsistent spacing, committing it, and pushing to a branch. Open a pull request and watch the `qa` job fail with clear output showing what needs to be fixed. Then run `make format-fix` locally, commit the corrected code, and push again. The CI pipeline will re-run automatically, and this time the checks will pass.

You can also experiment with the manual trigger feature. Go to the Actions tab, run the workflow on your current branch, and observe how the jobs execute. This hands-on experience will make the abstract concept of CI concrete and help you develop confidence in the system.

The first two tiers run on every commit, but semantic quality requires a more expensive third tier. This is where AI evaluations enter as selective regression tests.

## AI Evaluations as Regression Tests

AI evaluations are essential for catching semantic quality regressions, such as a drop in helpfulness or an increase in hallucinations, that deterministic unit tests cannot detect. They are a unique and critical part of CI for AI systems [[8]](https://kinde.com/learn/ai-for-software-engineering/ai-devops/ci-cd-for-evals-running-prompt-and-agent-regression-tests-in-github-actions).

### Why AI Evals Are Unique to AI Systems

Unlike the fast and free checks in Tiers 1 and 2, AI evaluations are a Tier 3 gate because they are expensive. Each evaluation run involves real LLM calls, which incur both latency and token costs. For example, running an evaluation on a 500-example dataset where each run consumes 2,000 tokens could cost around $10 per run, assuming a rate of $0.01 per 1,000 tokens. Running this on every single commit would be impractical and costly.

### Manual-Trigger CI Workflow for AI Evals

To manage these costs, we run AI evaluations using a separate, manually triggered workflow. This pattern, defined with `workflow_dispatch` in GitHub Actions, prevents expensive runs on every commit and reserves them for deliberate checks [[9]](https://graphite.com/guides/github-actions-workflow-dispatch). Here is an example of what this workflow might look like in `.github/workflows/eval.yml`.

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

This workflow differs from our main `ci.yml` in a few key ways.

First, the `workflow_dispatch` trigger means it never runs automatically. You must go to the Actions tab in your GitHub repository to trigger it manually. This is the most important guardrail against accidental costs.

Second, it uses a production configuration (`configs/production.yaml`) to ensure that evaluations run against the real LLM models you use in production, not the fake models from your unit tests. The `LLM_API_KEY` is pulled from GitHub Secrets, which you can configure in your repository settings under **Settings → Secrets and variables → Actions**. This keeps your API keys secure and out of your codebase.

Finally, the `run_eval` script should point to the evaluation pipeline you built in previous lessons, which loads your dataset, runs your agent, and computes the relevant metrics using a framework like Opik or LangSmith.

To trigger this workflow, go to the Actions tab, select "AI Evaluations," choose your branch, and click "Run workflow." The results, including logs with your evaluation metrics, will appear in the Actions interface.

We recommend a decision framework for evaluation frequency based on your project's maturity.

*   **Early development:** Run evaluations manually to measure progress weekly or after major architectural changes. The goal is to get a baseline and track improvements.
*   **Active development:** Run them before merging significant feature branches to catch regressions early. This ensures that a change that improves one area does not degrade another.
*   **Mature product:** Run them as a mandatory quality gate before every release to ensure production quality never degrades. At this stage, you have a stable set of "golden" test cases that represent critical user journeys.

With all three tiers understood, we can now assemble them into a cohesive daily development workflow that keeps velocity high while protecting quality.

## Daily Development Workflow

With these tools in place, a typical daily workflow becomes straightforward and efficient, catching issues early and keeping development velocity high.

```mermaid
flowchart LR
  A["Write Code and Tests"]
  B["Run Quick Checks<br/>(Lint/Format)"]
  C["Run Tests"]
  D["Commit Changes"]
  E["Push and Open Pull Request"]
  F["Run AI Evaluations Manually"]

  A -- "proceeds to" --> B
  B -- "if successful" --> C
  C -- "if successful" --> D
  D -- "triggers pre-commit hooks" --> E
  E -- "initiates automated CI workflows" --> F
```

Image 2: A flowchart illustrating the typical daily development workflow for AI agents with Continuous Integration.

1.  **Write code** and the corresponding tests for your new feature or bug fix.
2.  **Run quick checks** periodically with `make lint-check` and `make format-check` to ensure code quality.
3.  **Run tests** after changing logic by executing `make tests` to verify deterministic behavior.
4.  **Commit your changes.** The pre-commit hooks will run automatically, catching any remaining issues.
5.  **Push and open a pull request.** The main CI workflow will run automatically, enforcing all checks in a clean environment.
6.  **Before releasing, run AI evaluations** manually from the GitHub Actions tab to check for semantic quality regressions.

This structured workflow takes only seconds for most commits and ensures that quality is maintained at every step. We have now covered the full spectrum from theory to daily practice.

## Conclusion

Our three-tier CI model adapts traditional software practices for the unique realities of LLM agents, managing non-determinism, prompt volatility, and cost constraints. The upfront investment in hooks, mocked tests, and selective AI evaluations pays off by catching regressions before customers experience quality drops. This is the foundational engineering step that moves you from fragile prototypes toward reliable, maintainable, team-scale production agents.

These practices set the stage for our upcoming lessons, where we will build on this foundation to cover full CI/CD integration, including automated deployment triggers, production monitoring built on your existing observability foundations, and cost optimization strategies.

## References

- [1] https://www.atlassian.com/continuous-delivery/continuous-integration
- [2] https://galileo.ai/blog/continuous-integration-ci-ai-fundamentals
- [3] https://www.guild.ai/glossary/non-deterministic-systems
- [4] https://pre-commit.com/
- [5] https://docs.astral.sh/ruff
- [6] https://agiflow.io/blog/effective-practices-for-mocking-llm-responses-during-the-software-development-lifecycle
- [7] https://intersect-training.org/CI-CD/yaml-and-github-actions.html
- [8] https://kinde.com/learn/ai-for-software-engineering/ai-devops/ci-cd-for-evals-running-prompt-and-agent-regression-tests-in-github-actions
- [9] https://graphite.com/guides/github-actions-workflow-dispatch