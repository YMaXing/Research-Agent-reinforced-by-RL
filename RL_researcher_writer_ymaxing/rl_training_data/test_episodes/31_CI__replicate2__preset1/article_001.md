# Continuous Integration for AI Agents

In our last few lessons, we built a foundation for creating production-ready AI systems. We integrated Opik for observability, created offline evaluation datasets from scratch, and adopted an evaluation-driven development framework. These steps give you the visibility and measurement tools needed to understand agent behavior. Now, it is time to shift our focus to Continuous Integration (CI): the automated infrastructure that keeps your codebase maintainable and prevents regressions from reaching production. With the problem and failure modes clear, we now define what Continuous Integration means in an AI context and introduce the three-tier model that solves these issues.

## What is Continuous Integration?

Continuous Integration is the practice of frequently merging code changes from multiple developers into a central repository. After each merge, an automated build and test sequence runs to detect integration issues early. This prevents the classic "it works on my machine" problem, ensuring that the shared codebase remains stable [[1]](https://www.atlassian.com/continuous-delivery/continuous-integration).

However, the CI pipelines that work for traditional software fall short for AI agents. Traditional CI focuses on deterministic logic, compile-time checks, and fast unit tests. AI systems introduce new challenges: non-deterministic outputs from LLMs, rapid prompt iterations that can silently break behavior, and high API costs that make running extensive tests on every commit impractical [[2]](https://galileo.ai/blog/continuous-integration-ci-ai-fundamentals), [[3]](https://www.guild.ai/glossary/non-deterministic-systems). Cost and latency compound the problem; a single API call can take seconds and cost non-trivial amounts, making any test suite that relies on live calls slow and expensive [[4]](https://agiflow.io/blog/effective-practices-for-mocking-llm-responses-during-the-software-development-lifecycle).

Without a CI process tailored for AI, teams often fall into several common failure modes.

### Inconsistent Code Formatting
When developers use different formatters or apply styles manually, the codebase becomes cluttered. This leads to time-wasting code reviews focused on trivial style nitpicks instead of the core logic, slowing down the entire team.

### Skipped Local Checks
Under pressure to deliver features quickly, developers might forget to run local tests or quality checks before pushing code. Without automated enforcement, this leads to broken builds and wasted time debugging issues that could have been caught earlier in the development cycle.

### Non-deterministic Tests
Tests that rely on live LLM calls are slow, expensive, and flaky. The same test can pass once and fail the next time due to model variability, rate limits, or network issues. This erodes trust in the test suite and slows down the entire team [[3]](https://www.guild.ai/glossary/non-deterministic-systems).

These challenges mean that CI for AI systems must borrow principles from MLOps, where CI is not only about testing code but also about validating data, schemas, and models [[5]](https://docs.cloud.google.com/architecture/mlops-continuous-delivery-and-automation-pipelines-in-machine-learning). To address these challenges, we use a three-tier CI model that balances speed, cost, and coverage.

### Tier 1: Formatting and Linting (Always Run)
These checks are fast (seconds) and free (no API calls). They catch syntax errors and enforce a consistent code style across the project. This tier is identical to traditional CI.

### Tier 2: Unit and Integration Tests (Always Run)
These tests verify the deterministic logic in your agent, such as data parsing, schema validation, and routing. By mocking LLM responses, these tests run quickly (under a minute) and reliably, without incurring API costs.

### Tier 3: AI Evaluations (Manual/Release)
This tier is unique to AI systems. It involves running expensive, LLM-based quality checks against a curated dataset to evaluate semantic quality. We run these evaluations selectively, either manually before a major release or after a significant change to a prompt or model.![A three-tier CI model for AI agents, showing the flow from commit checks to PR tests and finally to manual/release AI evaluations, with each tier distinctly colored.](https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/6bf41859-7dd2-4a23-9a88-55720f54114e/image/w=1920,quality=90,fit=scale-down)

Image 1: A three-tier CI model for AI agents, showing the flow from commit checks to PR tests and finally to manual/release AI evaluations, with each tier distinctly colored.

The AI evaluations in Tier 3 serve as regression tests for semantic quality. Built on the offline evaluation datasets and Opik traces from our previous lessons, they catch regressions in helpfulness, tone, or factuality that traditional unit tests structurally cannot detect [[6]](https://kinde.com/learn/ai-for-software-engineering/ai-devops/ci-cd-for-evals-running-prompt-and-agent-regression-tests-in-github-actions).

This lesson covers the CI essentials for building production-ready AI agents. We will focus on practical techniques you will use daily, such as automated quality checks, testing with mocked LLMs, and structuring CI pipelines around cost constraints. We will not cover comprehensive DevOps topics like Kubernetes or Terraform. Instead, we will show you how to effectively move from prototype to a production-ready agent.

We will cover:

*   Setting up pre-commit hooks to enforce code quality automatically.
*   Configuring Ruff for linting and formatting.
*   Writing unit tests for deterministic agent code with mocked LLM responses.
*   Building a CI pipeline that runs automatically on every change.
*   Using AI evaluations as selective regression tests in CI.

This lesson includes a hands-on notebook where you will practice running formatting checks, linting, and tests on Brown, our writing agent. With the three-tier model established, the fastest feedback comes from running the first tier locally before you even commit code. This is where pre-commit hooks come in.

## Pre-commit Hooks: Automated Local Guardrails

Pre-commit hooks are local guardrails that run automatically every time you make a commit. They provide immediate feedback on your code, catching issues before they ever enter the shared repository. This prevents simple mistakes like formatting errors or syntax issues from breaking the main build [[7]](https://pre-commit.com/).

The `pre-commit` framework manages these hooks using a declarative YAML configuration file. You define the hooks you want to use in a `.pre-commit-config.yaml` file, and the framework handles their installation and execution. Most hooks are maintained by the community in external repositories, making it easy to use popular tools without manual setup.

<aside>
💡

You can experiment with the code for this lesson in this [Colab](https://colab.research.google.com/github/louisfb01/agent-course-notebooks/blob/main/notebooks/lesson_31_notebook.ipynb#scrollTo=b30eba1a). Alternatively, you can find the code for this lesson in the notebook for Lesson 31 of the course GitHub repository.

</aside>

### Brown’s Pre-commit Configuration

In our Brown agent, the pre-commit configuration is defined in `lessons/writing_workflow/.pre-commit-config.yaml`.

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

This configuration defines three sets of hooks:

*   **`validate-pyproject`**: This tool validates that your `pyproject.toml` file is structurally correct according to PEP standards. A malformed configuration file can break your entire project, so this simple check is a valuable safeguard.
*   **`prettier`**: A popular code formatter that we use for configuration files like `.github/workflows/ci.yml`. Consistent formatting makes these files more readable and helps reduce merge conflicts.
*   **ruff-check** and **ruff-format**: These hooks run Ruff, a modern Python linter and formatter. The `--fix` argument automatically corrects any fixable issues, and `--exit-non-zero-on-fix` ensures the hook still fails even after auto-fixing. This forces you to review and re-stage the changes, confirming you are aware of what was modified. As recommended by Ruff’s authors, `ruff-check` runs before `ruff-format`.

### Setting Up Pre-commit

In the `lessons/writing_workflow` repository, you can set up the pre-commit hooks with these commands.

```bash
# Install dependencies (includes pre-commit)
uv sync --dev

# Install the Git hooks
pre-commit install
```

The `pre-commit install` command creates a script at `.git/hooks/pre-commit`. Now, every time you run `git commit`, these hooks will execute automatically. You can also run them manually on all files.

```bash
# Run all hooks on all files
make pre-commit
```

The daily workflow is straightforward. You make your changes, stage them with `git add`, and then run `git commit`. If any hooks fail, you review the errors, fix them, re-stage the files, and commit again. Pre-commit hooks often rely on fast tools like Ruff to do the actual work. Next, we will examine Ruff in depth and show how to configure it.

## Ruff: Fast Python Linting and Formatting

Ruff is a Python linter and code formatter written in Rust. It is extremely fast, often 10-100x faster than legacy tools like Black, isort, and Flake8. By consolidating the functionality of over ten different tools into a single binary, it simplifies configuration, eliminates dependency conflicts, and dramatically reduces CI run times [[8]](https://docs.astral.sh/ruff).

It is important to distinguish between formatting and linting.

*   **Formatting** automatically rewrites your code to follow a consistent style. It handles things like indentation, line breaks, and spacing, and it is generally opinionated to ensure uniformity.
*   **Linting** analyzes your code for potential bugs, violations of best practices, and suspicious patterns. It flags issues like unused variables, missing imports, or overly complex code that could lead to errors.

### Brown’s Ruff Configuration

Ruff is configured in the `pyproject.toml` file. Here is the configuration from `lessons/writing_workflow/pyproject.toml`.

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

*   `target-version = "py312"` tells Ruff to check for syntax compatibility with Python 3.12.
*   `line-length = 140` sets the maximum line length for code formatting.
*   `select = ["F", "E", "I"]` enables specific rule sets: `F` for Pyflakes (detects common bugs), `E` for pycodestyle (enforces PEP 8 style), and `I` for isort (organizes imports).
*   `known-first-party = ["src", "tests"]` tells isort how to group project-specific imports separately from third-party libraries.

We also use a `Makefile` to provide convenient shortcuts for running Ruff commands.

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

Each command uses `uv run` to execute within the project’s virtual environment, which `uv` manages automatically without manual activation.

### Hands-On Example: Fixing Formatting Issues

Let's see Ruff's formatter in action. First, we create a Python file with deliberate formatting mistakes.

1.  We create a test file with inconsistent spacing and layout.
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
2.  Next, we run the format checker. The `--check` flag reports issues without changing the file.
    ```bash
    uv run ruff format --check test_formatting.py
    ```
    It outputs:
    ```text
    Would reformat: test_formatting.py
    1 file would be reformatted
    ```
3.  Now, we run the auto-fix command to correct the formatting.
    ```bash
    uv run ruff format test_formatting.py
    ```
    It outputs:
    ```text
    1 file reformatted
    ```
    Ruff automatically fixes spacing, indentation, and line breaks, producing clean, consistent code.

### Hands-On Example: Fixing Linting Issues

Linting catches a different class of problems. Let's create another file, this time with linting violations.

1.  This file includes unused imports, a duplicate import, and an undefined variable.
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
2.  Running the linter shows several errors, including `F401` (unused import), `F811` (duplicate import), and `F821` (undefined name).
    ```bash
    uv run ruff check test_linting.py
    ```
    It outputs:
    ```text
    Found 7 errors.
    [ *] 4 fixable with the `--fix` option (1 hidden fix can be enabled with the `--unsafe-fixes` option).
    ```
3.  Using the `--fix` flag, Ruff automatically removes the unused and duplicate imports.
    ```bash
    uv run ruff check --fix test_linting.py
    ```
    It outputs:
    ```text
    Found 5 errors (3 fixed, 2 remaining).
    No fixes available (1 hidden fix can be enabled with the `--unsafe-fixes` option).
    ```
    However, it cannot fix the `F821` error because using an undefined function is a logic bug that requires manual intervention. Once your code is clean and formatted, you need to verify its logic. This is the role of unit tests.

## Unit Tests for Agent Repos

The core challenge in testing AI agents is the non-determinism of LLMs. Making live API calls in tests is a bad practice because it makes them slow, expensive, and flaky. The same prompt can produce slightly different outputs on each run, causing tests to fail unpredictably [[3]](https://www.guild.ai/glossary/non-deterministic-systems). A test that waits 15–30 seconds for a real completion is a test developers stop running locally; slow tests get skipped, and skipped tests find no bugs [[4]](https://agiflow.io/blog/effective-practices-for-mocking-llm-responses-during-the-software-development-lifecycle).

Unit tests solve this by focusing on the deterministic parts of your agent's logic. Instead of testing the LLM itself, you test the code *around* the LLM. This includes verifying logic for:

*   **Parsing and rendering:** Does your markdown loader correctly extract article content?
*   **Schema validation:** Does a Pydantic model reject invalid data as expected?
*   **Routing decisions:** Given a specific input state, does your workflow route to the correct node?
*   **Utilities:** Do helper functions for tasks like URL cleaning or text extraction work correctly?

### Unit Tests vs. Integration Tests

In traditional software, a **unit test** verifies a single, isolated piece of code, like a function. An **integration test** checks how multiple components work together. For AI agents, these lines blur. A single agent node might combine prompt templating, an LLM call, and output parsing.

We take a pragmatic approach: if a test runs quickly with mocked dependencies and verifies deterministic logic, we consider it a unit test. This allows us to test meaningful chunks of functionality without the flakiness of live API calls.

To achieve this, we use a mocking strategy called response injection. Instead of patching network requests at the HTTP layer, we use a fake model class that lets us inject pre-defined responses directly into our tests. This gives us precise control over the LLM's output and keeps our tests simple and fast.

<aside>
💡

Another option to mock LLM calls is through HTTP mocking. This involves intercepting API requests and returning pre-defined responses using libraries like `responses` or `httpretty`. This approach allows you to simulate various API behaviors, such as errors or slow responses, without making actual network calls. A popular variation is record-and-replay with tools like `VCR.py`, which records a real API interaction once and replays it for all subsequent test runs, ensuring your tests use realistic data structures.

</aside>

### Our Implementation: The FakeModel Pattern

In our Brown agent, we use a `FakeModel` class that is compatible with LangChain's `BaseChatModel` interface. This pattern has three parts:

1.  **Configuration specifies the fake model:** A dedicated `debug.yaml` configuration file at `lessons/writing_workflow/configs/debug.yaml` sets all nodes to use `model_id: "fake"`.
2.  **Model factory returns FakeModel:** The model builder in `src/brown/models/get_model.py` checks the configuration and returns an instance of our `FakeModel` when specified.
3.  **Tests inject specific responses:** The `FakeModel` itself, defined in `src/brown/models/fake_model.py`, extends LangChain’s `FakeListChatModel` and allows tests to provide a list of canned responses.

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

An instance of `FakeModel` takes a list of pre-scripted responses. Each time `ainvoke()` is called, it returns and consumes the next response from the list. This design ensures that all unit tests use a fake model by default, and individual tests can inject specific responses as needed.

### Example: Testing Nodes with Mocked Responses

Here is how we test a node that calls an LLM, taken from `lessons/writing_workflow/tests/brown/nodes/test_article_writer.py`.

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

The test creates a mock JSON response, builds a fake model using our factory, and injects the response into it. It then instantiates the `ArticleWriter` node with this fake model. When `writer.ainvoke()` is called, the fake model returns our mock response instead of calling a real LLM. This pattern keeps tests fast, deterministic, and free.

### Running Brown’s Tests

To run the entire test suite for the Brown agent, you can use the `Makefile` command.

```bash
# From the writing_workflow directory
make tests
```

This command executes `CONFIG_FILE=configs/debug.yaml uv run pytest`. The `CONFIG_FILE` variable ensures that all tests load the `debug.yaml` configuration, which uses our fake models and prevents any real LLM API calls.

Local tests and hooks provide fast feedback, but enforcement at the repository level requires automated CI workflows that run on every pull request.

## CI Workflows: Automated Enforcement

GitHub Actions is our CI platform for both the Brown and Nova agents. It automatically triggers workflows on events like pull requests or pushes to the main branch. It supports job isolation, matrix builds for testing across different environments, and parallel execution to keep feedback loops fast. Best of all, it integrates seamlessly with GitHub repositories and requires minimal setup.

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

This configuration defines when the workflow runs and what checks it performs. The `on` section specifies that the workflow triggers on pull requests to the `main` and `dev` branches, as well as on direct pushes to `main`. This ensures every code change is validated.

The `env` section defines an environment variable, `QA_FOLDERS`, that lists all directories to be checked. It includes both `src/brown` and `src/nova`, allowing us to use the same CI configuration for both agents in a monorepo structure.

### Understanding the Job Structure

The workflow defines two independent jobs that run in parallel: `qa` and `tests`. Splitting them provides clear, fast feedback. If formatting fails, you immediately see "QA job failed" without waiting for tests to complete. This parallel execution saves time and makes it easier to identify which category of checks failed.

Each job runs on `ubuntu-latest`, a virtual machine provided by GitHub. The jobs are completely isolated from each other, allowing them to run simultaneously without interference.

The `qa` job focuses on code quality checks. It starts by checking out the code with `actions/checkout@v4`, then installs `uv` using `astral-sh/setup-uv@v4`. The Python setup step uses `actions/setup-python@v5` and reads the version from your `.python-version` file, ensuring consistency between local development and CI. After installing dependencies with `uv sync --dev` (which includes development tools for formatting and linting), it runs two checks. The format check uses `uv run ruff format --check` to verify code formatting, and the lint check uses `uv run ruff check` to detect quality issues.

The `tests` job follows a similar setup but runs `uv sync` without the `--dev` flag, as tests do not require development tools. The final step runs the test suite using `CONFIG_FILE=configs/debug.yaml uv run pytest`, ensuring tests use the fake model configuration and never make real LLM API calls.

### Setting Up GitHub Actions for Your Repository

To enable this CI workflow, you need to create the YAML file in the `.github/workflows/` directory at the root of your repository. First, create the directory structure: `mkdir -p .github/workflows`. Then, create the file `.github/workflows/ci.yml` and paste in the configuration above.

You also need to ensure your repository has a `.python-version` file specifying the Python version (e.g., `3.12`) and that your `configs/debug.yaml` file exists and is configured to use fake models for testing. Once you commit and push this file, the workflow becomes active.

### Running the Pipeline and Observing Results

The pipeline runs automatically when its trigger conditions are met. When you open a pull request, the workflow status appears on the PR page, blocking merges if checks fail.

You can also trigger the workflow manually from the "Actions" tab in your GitHub repository. Select the "CI" workflow, click "Run workflow," choose your branch, and start the run. This is useful for verifying a fix without creating a new commit. To monitor a run, click on it to see the status of each job. You can drill down into a job to see the logs for each step, with failures highlighted in red.

### Interpreting CI Results and Fixing Issues

When a job fails, the output tells you exactly what went wrong. If the `qa` job fails on formatting, the logs show which files need to be reformatted. You can fix this locally by running `make format-fix`, committing, and pushing the changes. If it fails on linting, the logs list each violation. Many can be fixed with `make lint-fix`.

If the `tests` job fails, the `pytest` output provides a traceback to help you pinpoint the error. A critical principle here is that CI runs the exact same commands you run locally. This eliminates "it works on my machine" problems. If `make tests` passes on your machine, it will pass in CI.

### Trying It Out

The best way to learn is by doing. Try introducing a formatting error, committing it, and opening a pull request. Watch the `qa` job fail and show you the problem. Then, fix it locally with `make format-fix`, push the change, and watch the CI pipeline pass. This hands-on experience will build your confidence in the system.

The first two tiers of our CI model run on every commit. However, ensuring semantic quality requires a more expensive third tier, which is where AI evaluations come in as selective regression tests.

## AI Evaluations as Regression Tests

AI evaluations are critical for catching semantic quality regressions, such as a drop in helpfulness or an increase in hallucinations, that deterministic unit tests cannot detect [[6]](https://kinde.com/learn/ai-for-software-engineering/ai-devops/ci-cd-for-evals-running-prompt-and-agent-regression-tests-in-github-actions). The curated datasets used for these evaluations are often called **golden datasets**. They represent a collection of inputs and ideal outputs that define the core behaviors your application must get right. A drop in performance against this dataset signals a quality regression that a model update or prompt change may have caused [[4]](https://agiflow.io/blog/effective-practices-for-mocking-llm-responses-during-the-software-development-lifecycle).

### Why AI Evals Are Unique to AI Systems

These evaluations form our Tier 3 gate because they are expensive. Each run involves real LLM calls, which incur latency and token costs. For example, running an evaluation on a 500-example dataset where each example costs $0.01 in API calls would total $5.00 per run. Automating this on every commit would be financially impractical. This is why we treat performance and cost as first-class metrics; quality must be measured alongside real-time efficiency to manage SLAs and budgets [[9]](https://dev.to/kuldeep_paul/a-practical-guide-to-integrating-ai-evals-into-your-cicd-pipeline-3mlb).

### Manual-Trigger CI Workflow for AI Evals

To manage costs, we use a separate, manually triggered workflow for AI evaluations. This is configured in `.github/workflows/eval.yml` using the `workflow_dispatch` trigger.

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

This workflow differs from our main CI pipeline in a few key ways.

1.  The `workflow_dispatch` trigger means it only runs when manually started from the Actions tab in GitHub. This prevents accidental, costly runs.
2.  It uses a production configuration (`configs/production.yaml`) to ensure evaluations run against real LLM models.
3.  It securely accesses an `LLM_API_KEY` from GitHub Secrets, which you must configure in your repository settings under **Settings → Secrets and variables → Actions**.

The evaluation command (`python -m scripts.run_eval`) should point to your evaluation script that loads your dataset, runs your agent on each sample, and computes metrics. The exact implementation depends on your evaluation framework, whether that’s Opik, LangSmith, or a custom solution.

To run this workflow, navigate to the Actions tab, select “AI Evaluations,” click “Run workflow,” choose your branch, and start the run. The results, including all metrics and any failures, will be available in the workflow logs.

We use a decision framework for how often to run evaluations based on project maturity.

*   **Early development:** Run manually on a weekly basis or after major changes to track progress.
*   **Active development:** Run before merging significant feature branches to catch regressions early.
*   **Mature product:** Run as a required step in your release process to ensure production quality never degrades.

With all three tiers of our CI model understood, we can now assemble them into a cohesive daily workflow.

## Daily Development Workflow

With these tools in place, your daily workflow becomes a tight, efficient loop that catches issues early and keeps quality high.

1.  **Write code** and the corresponding unit tests for any new deterministic logic.
2.  **Run quick checks** periodically as you work using `make lint-check` and `make format-check`.
3.  **Run tests** after changing logic by running `make tests`.
4.  **Commit your changes.** The pre-commit hooks will run automatically, catching any issues you missed.
5.  **Push and open a pull request.** The main CI workflow runs automatically, providing a final layer of enforcement.
6.  **Before a release, run AI evaluations** manually from the Actions tab to check for any semantic quality regressions.

This workflow takes only seconds for most commits and ensures that your codebase remains clean, correct, and maintainable.

## Conclusion

The three-tier CI model is a pragmatic adaptation of traditional software practices to the unique realities of LLM-powered agents. The upfront investment in hooks, Ruff, `FakeModel` patterns, and selective evals pays off by catching regressions before they reach users. This CI framework is the foundational step that moves your project from a fragile prototype toward a reliable, production-ready agent.

## References

- [1] https://www.atlassian.com/continuous-delivery/continuous-integration
- [2] https://galileo.ai/blog/continuous-integration-ci-ai-fundamentals
- [3] https://www.guild.ai/glossary/non-deterministic-systems
- [4] https://agiflow.io/blog/effective-practices-for-mocking-llm-responses-during-the-software-development-lifecycle
- [5] https://docs.cloud.google.com/architecture/mlops-continuous-delivery-and-automation-pipelines-in-machine-learning
- [6] https://kinde.com/learn/ai-for-software-engineering/ai-devops/ci-cd-for-evals-running-prompt-and-agent-regression-tests-in-github-actions
- [7] https://pre-commit.com
- [8] https://docs.astral.sh/ruff
- [9] https://dev.to/kuldeep_paul/a-practical-guide-to-integrating-ai-evals-into-your-cicd-pipeline-3mlb