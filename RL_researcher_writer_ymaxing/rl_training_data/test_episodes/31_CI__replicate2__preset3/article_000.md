# Lesson 31: Continuous Integration for AI Engineering

In our recent lessons, we have covered how to observe agent behavior with Opik, build offline evaluation datasets, and apply an evaluation-driven development framework. These practices give you the visibility and measurement tools needed to assess your agent's quality. Now, it is time to shift our focus to Continuous Integration (CI), the automated infrastructure that keeps your codebase maintainable and prevents regressions from reaching production, ensuring your AI agents are not just powerful, but also reliable.

## What is Continuous Integration?

Continuous Integration is the practice of frequently merging code changes from multiple contributors into a central repository, where automated builds and tests are run [[3]](https://www.atlassian.com/continuous-delivery/continuous-integration). The goal is to catch integration issues early and provide rapid feedback, preventing the classic "it works on my machine" problem. In traditional software, CI focuses on deterministic logic. It runs checks to ensure code compiles, unit tests pass with predictable outputs, and code style is consistent.

However, CI for AI agents introduces unique challenges that traditional practices do not address. LLM-powered systems are inherently non-deterministic, meaning the same input can produce different valid outputs, which breaks exact-match assertions [[2]](https://www.guild.ai/glossary/non-deterministic-systems). Prompts are constantly tweaked, and a change that improves one scenario can silently degrade performance in another. Another silent killer is model drift: the gradual degradation of performance as production data distributions shift away from the data the model was last evaluated on [[1]](https://galileo.ai/blog/continuous-integration-ci-ai-fundamentals). Furthermore, running tests that make live LLM calls is slow, expensive, and unreliable, making traditional test-on-every-commit strategies impractical. These challenges manifest in subtle but critical ways, such as tool misuse where an agent provides a malformed argument that corrupts a multi-step workflow, or cascading errors where a small mistake by one agent is amplified by another downstream [[47]](https://latitude.so/blog/ai-agent-failure-detection-guide).

Without a CI strategy tailored for AI, teams often fall into three common failure modes:

1.  **Inconsistent code formatting across the team.** When team members use different formatters or apply formatting manually, the codebase becomes cluttered with inconsistent styles. This leads to time-wasting discussions during code reviews about trivial issues like spacing and line breaks, distracting from the actual logic.
2.  **Skipped pre-commit checks, leading to CI failures.** Under pressure to ship features quickly, developers might forget to run local quality checks or even skip them intentionally. Without automated enforcement, this leads to failures in the main pipeline, blocking other team members and slowing down the entire team.
3.  **Non-deterministic tests that call real LLM APIs.** Teams that write tests making live LLM calls quickly discover they are flaky. These tests fail unpredictably due to model non-determinism, network issues, or API rate limits. They are also slow and expensive, which discourages frequent runs and ultimately leads to developers ignoring them.

To solve these problems, we use a three-tier CI model that balances feedback speed, cost, and test reliability.

*   **Tier 1: Formatting and Linting (Always Run).** These checks are fast, taking only seconds to run, and have no associated API costs. They catch syntax errors, style violations, and other basic code quality issues. This tier is identical to traditional CI and provides the quickest feedback.
*   **Tier 2: Unit and Integration Tests (Always Run).** These tests verify the deterministic parts of your agent, such as data parsing, schema validation, and workflow routing. They run quickly, typically in under a minute, because they use mocked LLM responses instead of making live API calls. This ensures they are reliable and free to run.
*   **Tier 3: AI Evaluations (Manual/Release).** This tier is unique to AI systems. It involves running expensive, LLM-based quality checks against a curated dataset to evaluate semantic quality, such as helpfulness or factuality. Because these evaluations are slow and costly, we run them selectively—either manually before a major release or after a significant change to a core prompt.![A three-tier CI model for AI agents, showing the flow from commit checks to PR tests and finally to manual/release AI evaluations, with each tier distinctly colored.](https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/6bf41859-7dd2-4a23-9a88-55720f54114e/image/w=1920,quality=90,fit=scale-down)
Image 1: A three-tier CI model for AI agents, showing the flow from commit checks to PR tests and finally to manual/release AI evaluations, with each tier distinctly colored. (Source [https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/6bf41859-7dd2-4a23-9a88-55720f54114e/image/w=1920,quality=90,fit=scale-down](https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/6bf41859-7dd2-4a23-9a88-55720f54114e/image/w=1920,quality=90,fit=scale-down))

The AI evaluations in Tier 3 serve as regression tests for semantic quality. They build on the offline evaluation datasets and Opik traces we covered in previous lessons, allowing you to catch degradations in your agent's behavior that unit tests structurally cannot.

This lesson covers the CI essentials for building production-ready AI agents. We will focus on practical techniques you will use daily: automated quality checks, testing with mocked LLMs, and structuring CI pipelines around cost constraints. We will not cover comprehensive DevOps topics like Kubernetes or Terraform. Instead, we will show you how to effectively move from prototype to production-ready agents.

We will cover:
*   Setting up pre-commit hooks to enforce code quality automatically.
*   Configuring Ruff for linting and formatting.
*   Writing unit tests for deterministic agent code with mocked LLM responses.
*   Building a CI pipeline that runs automatically on every change.
*   Using AI evaluations as selective regression tests in CI.

This lesson includes a hands-on notebook where you will practice running formatting checks, linting, and tests on Brown, our writing agent. With the three-tier model established, the fastest feedback comes from running the first tier locally before you even commit code. This is where pre-commit hooks come in.

## Pre-commit Hooks: Automated Local Guardrails

Pre-commit hooks are automated checks that run on your local machine every time you make a commit [[4]](https://pre-commit.com). They act as the first line of defense, providing immediate feedback and preventing simple errors like formatting mistakes or syntax issues from ever entering the shared codebase [[5]](https://blog.gitguardian.com/automated-guard-rails-for-vibe-coding).

The `pre-commit` framework manages these Git hooks through a declarative YAML file, `.pre-commit-config.yaml`. In this file, you define which hooks to run by referencing external repositories that maintain them. This allows you to use community-maintained tools for common tasks without having to manage the scripts yourself.

### Brown’s Pre-commit Configuration

<aside>
💡
You can experiment with the code for this lesson in this [Colab](https://colab.research.google.com/github/louisfb01/agent-course-notebooks/blob/main/notebooks/lesson_31_notebook.ipynb#scrollTo=b30eba1a). Alternatively, you can find the code for this lesson in the notebook for Lesson 31 of the course GitHub repository.

</aside>

Let's look at the configuration we use for our Brown writing agent, located at `lessons/writing_workflow/.pre-commit-config.yaml`.

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

This configuration defines three sets of hooks:

*   **`validate-pyproject`**: This tool validates that your `pyproject.toml` file is structurally correct according to PEP standards. A malformed file can break your entire project, so this simple check is a valuable safeguard.
*   **`prettier`**: A popular code formatter that we use for configuration files like `.github/workflows/ci.yml`. Consistent formatting makes these files more readable and helps reduce merge conflicts.
*   **`ruff-check` and `ruff-format`**: These hooks run Ruff, a modern Python linter and formatter. We use the `--fix` argument to automatically correct any issues it finds. The `ruff-check` hook runs before `ruff-format` as recommended by Ruff’s authors to ensure that linting fixes are applied before the final formatting pass.

### Setting Up Pre-commit

In the `lessons/writing_workflow` repository, or any project with a `.pre-commit-config.yaml` file, you can set up the hooks with two commands.

```bash
# Install dependencies (includes pre-commit)
uv sync --dev

# Install the Git hooks
pre-commit install
```

The `pre-commit install` command creates a script at `.git/hooks/pre-commit`. From now on, `pre-commit` will run automatically every time you run `git commit`. You can also trigger the hooks manually on all files in the repository.

```bash
# Run all hooks on all files
make pre-commit
```

The daily workflow is straightforward. You make your changes, stage them with `git add`, and then run `git commit`. If any of the hooks fail, the commit is blocked. You can then review the errors, fix them (often automatically), re-stage the corrected files, and commit again.

Pre-commit hooks often rely on fast, powerful tools like Ruff to perform the actual checks. Let's now examine Ruff in more detail to see how it is configured and run, both locally and in CI.

## Ruff: Fast Python Linting and Formatting

Ruff is an extremely fast Python linter and code formatter written in Rust. It serves as a consolidated replacement for a suite of older tools like Black, isort, Flake8, and pydocstyle, often delivering performance that is 10-100x faster [[6]](https://docs.astral.sh/ruff). Its speed and unified interface make it an ideal choice for the first tier of our CI model.

It is important to distinguish between formatting and linting:

*   **Formatting** automatically rewrites your code to follow a consistent and opinionated style. This includes rules for indentation, line length, and quote style. It is about how the code looks.
*   **Linting** analyzes your code for potential bugs, violations of best practices, and stylistic issues that go beyond simple formatting. This includes detecting unused variables, missing imports, or overly complex code. It is about how the code works.

### Brown’s Ruff Configuration

Ruff is configured in the `pyproject.toml` file. Here is the configuration for our Brown agent from `lessons/writing_workflow/pyproject.toml`.

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

[tool.pytest.ini_options]
pythonpath = ["src"]
markers = [
    "integration: end-to-end workflow tests (mocked LLMs, no network). Select with `-m integration` or skip with `-m 'not integration'`.",
]
```

*   `target-version = "py312"` tells Ruff to enforce rules compatible with Python 3.12 syntax.
*   `line-length = 140` sets the maximum line length, a common practice for modern, wider screens.
*   `select = ["F", "E", "I"]` enables three key rule sets: `F` for Pyflakes (detects common bugs), `E` for pycodestyle (enforces PEP 8 style), and `I` for isort (organizes imports).
*   `known-first-party = ["src", "tests"]` helps isort correctly group our project's internal imports separately from third-party libraries.

We also provide convenient shortcuts in our `Makefile` for running these checks.

```bash
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

Each target uses `uv run` to execute the command within the project's virtual environment, which is managed automatically and does not require manual activation. You can run these commands from the `writing_workflow/` directory to check or fix your code before committing.

### Hands-On Example: Fixing Formatting Issues

Let's see Ruff's formatter in action. First, we create a Python file with deliberate formatting errors.

1.  We create a file named `test_formatting.py` with inconsistent spacing and layout.

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
    Would reformat:  test_formatting.py
    1 file would be reformatted
    ```

3.  Now, we run the formatter again, this time without `--check`, to automatically fix the file.

    ```bash
    uv run ruff format test_formatting.py
    ```

    It outputs:

    ```text
    1 file reformatted
    ```

    The file is now perfectly formatted, with consistent spacing and structure.

### Hands-On Example: Fixing Linting Issues

Now, let's look at linting, which catches potential bugs and style violations.

1.  We create a file named `test_linting.py` with several issues, including unused imports, a duplicate import, and an undefined variable.

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
       I001  [*]  Import block is un-sorted or un-formatted
        --> test_linting.py:1:1
         |
       1 | / import os
       2 | | import sys
       3 | | import json # Unused import
         | |___________^
    ...
       F401  [*]  `json` imported but unused
        --> test_linting.py:3:8
    ...
       F821  Undefined name `some_undefined_function`
         --> test_linting.py:18:26
    ...
       F811  [*]  Redefinition of unused `sys` from line 2
         --> test_linting.py:21:8
    ...
    Found 7 errors.
    [*] 4 fixable with the `--fix` option...
    ```

3.  Using the `--fix` flag, Ruff automatically resolves the import-related issues but leaves the logic error (the undefined function) for us to fix manually.

    ```bash
    uv run ruff check --fix test_linting.py
    ```

    It outputs:

    ```text
    ...
    F821  Undefined name `some_undefined_function`
      --> test_linting.py:18:26
    ...
    Found 5 errors (3 fixed, 2 remaining).
    ```

By consolidating more than ten legacy linters into a single binary, Ruff eliminates version conflicts and dramatically reduces CI execution times.

With formatting and linting guardrails in place, our attention now turns to verifying the deterministic logic inside your agent nodes. This is the role of unit tests.

## Unit Tests for Agent Repos

The core challenge of testing LLM-based systems is non-determinism. Making live API calls to an LLM in your tests is a recipe for disaster. These tests are slow, which discourages frequent runs; expensive, as each call consumes tokens; and flaky, because the same prompt can yield different results, leading to unpredictable test failures [[1]](https://galileo.ai/blog/continuous-integration-ci-ai-fundamentals), [[2]](https://www.guild.ai/glossary/non-deterministic-systems).

Unit tests solve this by focusing on the deterministic logic within your agent. This includes parts of your code that do not require a live LLM call to be verified:

*   **Parsing and rendering:** Does your markdown loader correctly extract article content and metadata?
*   **Schema validation:** Does your Pydantic model correctly reject invalid data and accept valid data?
*   **Routing decisions:** Given a specific state, does your workflow correctly route to the next node?
*   **Utilities:** Do helper functions for tasks like URL extraction or text cleaning work as expected?

### Unit Tests vs. Integration Tests

In traditional software, a **unit test** verifies a single, isolated piece of code, like a function or a class. An **integration test** verifies that multiple components work together correctly. In agentic applications, this distinction can blur. A single agent node often combines several responsibilities, such as prompt templating, structured output parsing, and routing logic.

We adopt a pragmatic approach: if a test verifies deterministic logic, runs quickly with mocked dependencies, and does not make network calls, we consider it a unit test. This allows us to test meaningful chunks of our agent's functionality without getting bogged down in pedantic definitions.

To achieve this, we use mocking to isolate our code from external dependencies like LLM APIs. While there are several ways to mock these calls, we prefer response injection. This involves using a fake model class that returns pre-scripted responses, giving us precise control over the test environment.

<aside>
💡
Another powerful technique is record-and-replay using a library like VCR.py. On the first run, VCR records the real API request and response to a file (a "cassette"). On subsequent runs, it replays the saved response, eliminating network calls entirely. This is useful for integration tests where you want to use the structure of a real LLM response without the cost and non-determinism. Just be sure to configure it to redact API keys from the cassettes before committing them to version control [[48]](https://agiflow.io/blog/effective-practices-for-mocking-llm-responses-during-the-software-development-lifecycle).

</aside>

### Our Implementation: The FakeModel Pattern

In our Brown agent, we implement response injection with a `FakeModel` class that is compatible with LangChain’s chat model interface. This pattern consists of three parts:

1.  **Configuration specifies the fake model:** The `debug.yaml` configuration at `lessons/writing_workflow/configs/debug.yaml` sets all nodes to use `model_id: "fake"`.
2.  **Model factory returns FakeModel:** The model builder in `src/brown/models/get_model.py` checks the configuration and returns a `FakeModel` instance when specified.
3.  **Tests inject specific responses:** The `FakeModel` class, located in `src/brown/models/fake_model.py`, extends LangChain’s `FakeListChatModel` and allows tests to provide a list of canned responses.

Here is a simplified look at our `FakeModel` implementation.

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
            response_content = self.responses.pop(0)

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
                from langchain_core.messages import AIMessage
                raw_message = AIMessage(content=response_content)
                return {"parsed": structured_response, "raw": raw_message}
            else:
                return structured_response

        # For non-structured output, use the parent's implementation
        response = await super().ainvoke(inputs, *args, **kwargs)
        return response
```

An instance of the `FakeModel` class takes a list of pre-scripted responses in its constructor. When its `ainvoke()` method is called, it returns the next response from the list and removes it. This design ensures that our unit tests use a fake model by default, and individual tests can inject specific responses as needed.

### Example: Testing Nodes with Mocked Responses

When testing nodes that call an LLM, we use this pattern to mock the responses and verify the node's logic. Here is an example from `lessons/writing_workflow/tests/brown/nodes/test_article_writer.py`.

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

The test first defines a mock JSON response. It then builds a fake model using our factory and injects the mock response into it. Finally, it instantiates the `ArticleWriter` node with the fake model and calls its `ainvoke()` method. The assertions then verify that the writer correctly parsed the mocked response and produced the expected `Article` object. This pattern keeps our tests fast, deterministic, and free.

### Running Brown’s Tests

To run the entire test suite for our Brown agent, we use a simple command from the `Makefile`.

```bash
# From the writing_workflow directory
make tests
```

This command runs `CONFIG_FILE=configs/debug.yaml uv run pytest`. The `debug.yaml` configuration file ensures that all tests use our fake models and never make calls to real LLM APIs.

Local tests and hooks provide fast feedback, but enforcing these standards across the entire team requires automated CI workflows that run on every pull request.

## CI Workflows: Automated Enforcement

The first two tiers of our CI model, formatting, linting, and unit testing, give us confidence in our code's quality and correctness at the local level. To enforce these standards consistently across the team, we automate them in a CI workflow. For both our Brown and Nova agents, we use GitHub Actions as our CI platform. It integrates seamlessly with our GitHub repository, triggers workflows automatically on events like pull requests or pushes, and allows us to run jobs in parallel for faster feedback [[9]](https://graphite.com/guides/github-actions-workflow-dispatch).

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

This configuration defines when the workflow runs and the checks it performs. The `on` section specifies that the workflow triggers on pull requests to the `main` and `dev` branches, as well as on direct pushes to `main`. This ensures every code change is validated before it can be merged.

The `env` section defines an environment variable, `QA_FOLDERS`, that lists all the directories we want to check. This setup allows us to use the same CI configuration for both our Brown and Nova agents in a monorepo structure.

### Understanding the Job Structure

The workflow defines two independent jobs, `qa` and `tests`, that run in parallel. Splitting them provides clearer and faster feedback. If a formatting check fails, you immediately see "QA job failed" without having to wait for the entire test suite to complete. This parallel execution saves time and makes it easier to pinpoint which category of checks failed.

Each job runs on `ubuntu-latest`, a virtual machine provided by GitHub, and is completely isolated from the other.

The `qa` job focuses on code quality checks that do not require running the application. It begins by checking out the code with `actions/checkout@v4`, then installs `uv` using `astral-sh/setup-uv@v4`. The Python setup step uses `actions/setup-python@v5` and reads the Python version from the `.python-version` file, ensuring consistency between local development and CI. After installing all dependencies, including development tools, with `uv sync --dev`, it runs two checks. The format check, `uv run ruff format --check`, verifies that all code adheres to our formatting rules without modifying any files. The lint check, `uv run ruff check`, analyzes the code for quality issues, unused imports, and potential bugs.

The `tests` job follows a similar setup but installs only the project dependencies with `uv sync`, as it does not need development tools like formatters. The final step runs the test suite with `CONFIG_FILE=configs/debug.yaml uv run pytest`. This command ensures that all tests use our fake model configuration, preventing any real LLM API calls and keeping the tests fast, deterministic, and free.

Image 2: CI Workflow for AI Agents (Brown and Nova)

### Setting Up GitHub Actions for Your Repository

To enable this CI workflow in your own repository, you need to place the workflow file in the correct directory. GitHub Actions automatically discovers and runs workflow files located in the `.github/workflows/` directory at the root of your project.

First, create this directory structure if it does not already exist by running `mkdir -p .github/workflows` from your repository's root. Then, create a file named `ci.yml` inside this directory and paste the complete configuration provided above. You will also need to ensure your repository has a `.python-version` file specifying the Python version to use (e.g., `3.12`) and a `configs/debug.yaml` file that configures your agents to use fake models for testing.

Once you commit and push this file, the workflow becomes active immediately. For a basic setup like this, no further configuration in the GitHub UI is needed, although you will need to add secrets for more advanced workflows, such as those involving API keys for AI evaluations.

### Running the Pipeline and Observing Results

The pipeline runs automatically whenever its trigger conditions are met. When you open a pull request targeting the `main` or `dev` branch, the workflow executes and reports its status directly on the pull request page.

You can also trigger the workflow manually. To do this, navigate to the "Actions" tab in your GitHub repository. You will see a list of your workflows on the left. Select the "CI" workflow, and a "Run workflow" button will appear. Clicking this allows you to choose the branch and manually start a run. This is useful for testing changes to your CI configuration or re-running failed checks after a fix.

To monitor a run, click on it from the list in the Actions tab. The interface will show both the `qa` and `tests` jobs with their current status. You can click on each job to view the detailed output of its steps. If a step fails, it will be highlighted in red, and its log output will be expanded automatically, making it easy to diagnose the problem.

### Interpreting CI Results and Fixing Issues

When the CI pipeline runs, each job will report one of three statuses: success (a green checkmark), failure (a red X), or in progress (a yellow dot). GitHub displays the overall status on your pull request and can be configured to block merging if any checks fail.

If the `qa` job fails due to a formatting issue, the logs will show which files need to be reformatted. You can fix this by running `make format-fix` locally, then committing and pushing the changes. If the failure is due to a linting issue, the logs will detail each violation, including the file, line number, and error code. Running `make lint-fix` will automatically fix many of these issues.

If the `tests` job fails, the `pytest` output will provide a traceback showing exactly which test failed and why. This could be due to a logic error in your code, an incorrect mock response, or a missing dependency. You should fix the underlying issue, verify the fix by running `make tests` locally, and then push your changes.

A critical principle of our CI setup is that the commands run in the pipeline are identical to the ones you run locally. The `qa` job runs the same `ruff format --check` and `ruff check` commands as our Makefile targets. The `tests` job runs the same `pytest` command as `make tests`. This consistency eliminates "it works on my machine" problems. If your checks pass locally, they will pass in CI.

### Trying It Out

The best way to understand CI is to see it in action. Try introducing a deliberate formatting error into a file, commit it, and push it to a new branch. Open a pull request and watch the `qa` job fail. The logs will clearly show the issue. Then, run `make format-fix` locally, commit the corrected file, and push again. The CI pipeline will re-run automatically and pass.

You can also experiment with the manual trigger. Go to the Actions tab and run the workflow on your branch. This hands-on experience will solidify your understanding of how CI works and build your confidence in the system.

An emerging trend is the use of AI assistants like GitHub Copilot to help develop and maintain these CI pipelines. Copilot can generate entire GitHub Actions workflows from simple comments, suggest tests for new code, and help automate repetitive scripting tasks, further accelerating the development cycle [[49]](https://www.cloudthat.com/resources/blog/github-copilot-boost-developer-productivity-with-ai-code-completion).

The first two tiers of our model run on every commit, but ensuring semantic quality requires a more expensive third tier. This is where AI evaluations enter the picture as selective regression tests.

## AI Evaluations as Regression Tests

AI evaluations are essential for catching semantic quality regressions, such as a drop in helpfulness or an increase in hallucinations, that deterministic unit tests cannot detect [[8]](https://kinde.com/learn/ai-for-software-engineering/ai-devops/ci-cd-for-evals-running-prompt-and-agent-regression-tests-in-github-actions). These evaluations form the third tier of our CI model and are unique to AI systems.

### Why AI Evals Are Unique to AI Systems

Unlike formatting checks or unit tests, AI evaluations involve making real LLM calls, which makes them both slow and expensive. Running a full evaluation suite on every commit is impractical. For example, evaluating a dataset of 500 examples, where each run costs an average of $0.01 in tokens, would amount to $5 per full run. While this may not seem like much, it adds up quickly across a team of developers committing frequently. This is why we treat them as a Tier 3 gate, to be used selectively. Some teams adopt a tiered strategy, running a smaller set of evals on pull requests and reserving comprehensive suites for nightly runs [[50]](https://developers.redhat.com/articles/2026/05/18/ci-cd-delivery-agentic-ai).

### Manual-Trigger CI Workflow for AI Evals

To manage the cost and execution time of AI evaluations, we run them using a separate, manually-triggered CI workflow. This is configured in a file like `.github/workflows/eval.yml` using GitHub Actions' `workflow_dispatch` trigger. This ensures that the workflow only runs when a developer deliberately initiates it.

Here is an illustrative example of such a workflow. A working implementation would use the actual evaluation scripts we developed in previous lessons, likely leveraging a tool like Opik for scoring and metrics.

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

1.  The `workflow_dispatch` trigger ensures it only runs manually, preventing accidental, costly runs on every commit.
2.  It uses a production configuration (`configs/production.yaml`) to ensure evaluations are run against the real LLM models, not our fake ones.
3.  It securely accesses the `LLM_API_KEY` from GitHub Secrets, which you configure in your repository settings under **Settings → Secrets and variables → Actions**.

To trigger this workflow, you navigate to the **Actions** tab in your GitHub repository, select **AI Evaluations** from the list, click the **Run workflow** button, choose your branch, and confirm. The workflow will then execute, and you can monitor its progress and view the results in the Actions interface.

The decision of when to run these evaluations depends on the maturity of your project:

*   **Early development:** Run evaluations manually, perhaps weekly, to track progress and measure improvements after major changes.
*   **Active development:** Run them before merging significant new features or prompt changes to catch any regressions.
*   **Mature product:** Integrate them into your release process as a final quality gate to ensure that production quality never degrades.

This is often called golden flow validation, where each build is benchmarked against key interactions. The logic from these CI evals can later be extended into production guardrails that monitor live traffic [[1]](https://galileo.ai/blog/continuous-integration-ci-ai-fundamentals). With all three tiers of our CI model understood, we can now assemble them into a cohesive daily development workflow that maintains high velocity while protecting quality.

## Daily Development Workflow

With these automated guardrails in place, your daily development workflow becomes a smooth and predictable process that catches issues early and keeps your codebase healthy.

1.  **Write code** and the corresponding unit tests for any new logic.
2.  **Run quick checks** periodically as you work using `make lint-check` and `make format-check` to get immediate feedback.
3.  **Run tests** locally after making significant changes to logic by running `make tests`. This ensures your changes have not broken any existing functionality.
4.  **Commit your changes.** The pre-commit hooks will run automatically, catching any remaining formatting or linting issues.
5.  **Push and open a pull request.** The main CI workflow will run automatically, providing a final, comprehensive check in a clean environment.
6.  **Before releasing, run AI evaluations** manually from the GitHub Actions tab to verify that there are no semantic quality regressions.

This workflow takes only seconds for most commits and ensures that issues are caught at the earliest possible stage. We have now covered the full spectrum from theory to daily practice; the conclusion will tie everything together.

## Conclusion

We have now covered the full spectrum of Continuous Integration for AI agents, from theory to daily practice. The three-tier CI model provides a pragmatic approach to adapting traditional software engineering practices to the unique challenges of LLM-powered systems, such as non-determinism, prompt volatility, and high API costs.

The initial investment in setting up pre-commit hooks, configuring Ruff, implementing the `FakeModel` pattern for tests, and building a robust GitHub Actions workflow pays for itself by catching regressions before they impact your users. CI is the foundational engineering step that transforms your project from a fragile prototype into a reliable, maintainable, and production-ready agent system.

The practices we have established here will serve as the foundation for the topics in our upcoming lessons, where we will cover full CI/CD integration, production monitoring, and cost optimization strategies.

## References

- [1] [Continuous Integration (CI) for AI: Fundamentals](https://galileo.ai/blog/continuous-integration-ci-ai-fundamentals)
- [2] [Non-Deterministic Systems](https://www.guild.ai/glossary/non-deterministic-systems)
- [3] [What is Continuous Integration?](https://www.atlassian.com/continuous-delivery/continuous-integration)
- [4] [pre-commit](https://pre-commit.com/)
- [5] [Automated guard rails for vibe coding](https://blog.gitguardian.com/automated-guard-rails-for-vibe-coding)
- [6] [Ruff Docs](https://docs.astral.sh/ruff/)
- [7] [Ruff Linter](https://docs.astral.sh/ruff/linter/)
- [8] [CI/CD for AI Evals: Running prompt and agent regression tests in GitHub Actions](https://kinde.com/learn/ai-for-software-engineering/ai-devops/ci-cd-for-evals-running-prompt-and-agent-regression-tests-in-github-actions)
- [9] [GitHub Actions: workflow_dispatch](https://graphite.com/guides/github-actions-workflow-dispatch)
- [10] [Unit Testing (AI Agents)](https://www.guild.ai/glossary/unit-testing-ai-agents)
- [11] [LangChain Testing](https://docs.langchain.com/oss/python/langchain/test)
- [12] [Effective practices for mocking LLM responses during the software development lifecycle](https://agiflow.io/blog/effective-practices-for-mocking-llm-responses-during-the-software-development-lifecycle)
- [13] [LangChain FakeLLM for testing](https://langchain-contrib.readthedocs.io/en/latest/llms/fake.html)
- [14] [LangChain fake chat model for testing](https://docs.langchain.com/oss/javascript/integrations/chat/fake)
- [15] [Integration with GitHub Actions, uv docs](https://docs.astral.sh/uv/guides/integration/github/)
- [16] [How to run jobs in parallel with GitHub Actions](https://dev.to/cicube/how-to-run-jobs-in-parallel-with-github-actions-4png)
- [17] [Manually running a workflow](https://docs.github.com/actions/managing-workflow-runs/manually-running-a-workflow)
- [18] [Example workflow for AI Agent Evaluation](https://learn.microsoft.com/en-us/azure/foundry/how-to/evaluation-github-action)
- [19] [An Empirical Study of Testing Practices in Open Source AI Agent Frameworks and Agentic Applications](https://arxiv.org/html/2509.19185v1)
- [20] [Best AI Evals Tools for CI/CD in 2025](https://www.braintrust.dev/articles/best-ai-evals-tools-cicd-2025)
- [21] [What is AI Regression Testing?](https://testgrid.io/blog/what-is-ai-regression-testing)
- [22] [A practical guide to integrating AI evals into your CI/CD pipeline](https://dev.to/kuldeep_paul/a-practical-guide-to-integrating-ai-evals-into-your-cicd-pipeline-3mlb)
- [23] [Local Guardrails for Secrets Security with GitGuardian](https://blog.gitguardian.com/local-guardrails-for-secrets-security)
- [24] [pre-commit-hooks GitHub repository](https://github.com/pre-commit/pre-commit-hooks)
- [25] [Git Hooks Tutorial](https://www.atlassian.com/git/tutorials/git-hooks)
- [26] [Ruff FAQ](https://docs.astral.sh/ruff/faq)
- [27] [Ruff GitHub repository](https://github.com/astral-sh/ruff)
- [28] [Testing Non-Deterministic AI Agents](https://datagrid.com/blog/4-frameworks-test-non-deterministic-ai-agents)
- [29] [Unit testing AI systems](https://galileo.ai/blog/unit-testing-ai-systems)
- [30] [CI/CD Best Practices](https://octopus.com/devops/ci-cd)
- [31] [CI/CD Best Practices for Data Projects](https://www.sunnydata.ai/blog/cicd-best-practices-data-projects-validation-testing)
- [32] [Continuous Integration with AI and Machine Learning](https://www.ibm.com/think/topics/continuous-integration)
- [33] [CI/CD Best Practices for 2024](https://gatling.io/blog/ci-cd-best-practices)
- [34] [AI Maturity Assessment Framework](https://www.ness.com/blog/ai-maturity-assessment-framework)
- [35] [MITRE AI Maturity Model](https://www.mitre.org/news-insights/publication/mitre-ai-maturity-model-and-organizational-assessment-tool-guide)
- [36] [Info-Tech AI Maturity Framework](https://www.infotech.com/research/ss/assess-your-ai-maturity)
- [37] [Sema4.ai AI Maturity Model](https://sema4.ai/blog/ai-maturity-model-2026)
- [38] [OWASP AI Maturity Assessment (AIMA)](https://owasp.org/www-project-ai-maturity-assessment)
- [39] [Testing AI Agents](https://oneuptime.com/blog/post/2026-01-30-agent-testing/view)
- [40] [Ruff pre-commit GitHub repository](https://github.com/astral-sh/ruff-pre-commit)
- [41] [Integration with pre-commit, uv docs](https://docs.astral.sh/uv/guides/integration/pre-commit/)
- [42] [LLM evaluation for CI/CD pipelines](https://www.deepchecks.com/llm-evaluation/ci-cd-pipelines/)
- [43] [pyproject.toml explained](https://betterstack.com/community/guides/scaling-python/pyproject-explained/)
- [44] [Unit testing best practices](https://brightsec.com/blog/unit-testing-best-practices/)
- [45] [pytest documentation](https://docs.pytest.org/)
- [46] [Why Python developers should switch to uv](https://devcenter.upsun.com/posts/why-python-developers-should-switch-to-uv/)
- [47] [AI Agent Failure Detection Guide](https://latitude.so/blog/ai-agent-failure-detection-guide)
- [48] [Effective Practices for Mocking LLM Responses During the Software Development Lifecycle](https://agiflow.io/blog/effective-practices-for-mocking-llm-responses-during-the-software-development-lifecycle)
- [49] [GitHub Copilot: Boost Developer Productivity with AI Code Completion](https://www.cloudthat.com/resources/blog/github-copilot-boost-developer-productivity-with-ai-code-completion)
- [50] [CI/CD delivery for agentic AI](https://developers.redhat.com/articles/2026/05/18/ci-cd-delivery-agentic-ai)