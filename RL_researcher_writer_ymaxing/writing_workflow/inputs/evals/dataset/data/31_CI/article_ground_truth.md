# Lesson 31: Continuous Integration for AI Engineering

In our last lessons, we introduced agent observability with Opik, started building our offline evaluation dataset, and covered the evaluation-driven development framework. We learned that improving a system requires seeing what it does and capturing data to test against. Now, we shift focus to Continuous Integration (CI): the automated infrastructure that keeps your codebase maintainable and prevents regressions from reaching production.

## What is Continuous Integration?

Continuous Integration is a software development practice where developers frequently merge code changes into a shared repository. Each merge triggers automated checks to detect integration issues early. The core principle is to catch bugs quickly and cheaply by automatically testing every change.

For AI agent projects, CI follows the same principles but with unique challenges. Prompts change frequently as new model versions are released with different capabilities and behaviors, and as edge cases are discovered in production that require prompt adjustments to handle properly. Additionally, schemas evolve, and LLM outputs are non-deterministic.

Here are three of the failure modes that typically emerge without CI:

  1. **Inconsistent code formatting across the team.** When team members use different formatters or manual formatting, pull requests become cluttered with whitespace and unrelated style changes. Code reviews waste time debating indentation and formatting instead of focusing on meaningful changes.
  2. **Skipped pre-commit checks, leading to CI failures.** A developer tests a change locally, runs formatting, and pushes the code. Later, the build fails in CI because they forgot to run the test suite before pushing. Without automated enforcement, manual verification steps are skipped under time pressure or due to simple oversight.
  3. **Non-deterministic tests that call real LLM APIs.** The temptation with AI agents is to call real LLMs in tests to verify behavior. But real API calls make tests slow, expensive, and non-deterministic, as the same input can produce different outputs. Your test suite becomes flaky and unreliable, undermining confidence in your CI pipeline.

To address these challenges, we adapt standard CI practices into a three-tier model for AI agents based on cost and speed:

  * **Tier 1: Formatting and Linting (Always Run).** These checks are fast (taking seconds) and cheap (no API calls). They catch syntactic issues and enforce style consistency. This tier is identical to traditional CI.
  * **Tier 2: Unit and Integration Tests (Always Run).** These verify deterministic logic, such as parsing, schema validation, and routing, without calling external APIs. By mocking LLM responses, tests run quickly (under a minute) and reliably.
  * **Tier 3: AI Evaluations (Manual/Release).** This tier is unique to AI systems. It involves expensive, LLM-based quality checks that use real API calls to evaluate agent quality on a curated dataset. We run these selectively before major releases or after significant prompt changes.

![Image 1: A three-tier CI model for AI agents, showing the flow from commit checks to PR tests and finally to manual/release AI evaluations, with each tier distinctly colored.](https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/6bf41859-7dd2-4a23-9a88-55720f54114e/image/w=1920,quality=90,fit=scale-down)Image 1: A three-tier CI model for AI agents, showing the flow from commit checks to PR tests and finally to manual/release AI evaluations, with each tier distinctly colored.

This lesson covers CI essentials for building production-ready AI agents. We focus on practical techniques you will use daily: automated quality checks, testing with mocked LLMs, and structuring CI pipelines around cost constraints. We will not cover comprehensive DevOps topics like Kubernetes or Terraform. Instead, we teach you how to effectively move from prototype to production-ready agents.

We will cover:

  * Setting up pre-commit hooks to enforce code quality automatically.
  * Configuring Ruff for linting and formatting.
  * Writing unit tests for deterministic agent code with mocked LLM responses.
  * Building a CI pipeline that runs automatically on every change.
  * Using AI evaluations as selective regression tests in CI.

This lesson includes a hands-on notebook where you will practice running formatting checks, linting, and tests on Brown, our writing agent.

## Pre-commit Hooks: Automated Local Guardrails

[Pre-commit](<https://pre-commit.com/>) hooks are Git hooks [[13]](<https://pre-commit.com/>) that run automatically before you create a commit. They catch issues immediately in your local environment, providing a fast feedback loop. You fix problems in seconds, not minutes later when CI fails.

The **pre-commit** framework manages Git hooks using a declarative YAML configuration. You define hooks in `.pre-commit-config.yaml`, and the framework handles installation and execution. Hooks are references to external repositories, so the community maintains them for popular tools.

### Brown’s Pre-commit Configuration

</aside>
💡
You can experiment with the code for this lesson in this [Colab](<https://colab.research.google.com/github/louisfb01/agent-course-notebooks/blob/main/notebooks/lesson_31_notebook.ipynb#scrollTo=b30eba1a>).
Alternatively, you can find the code for this lesson in the notebook for Lesson 31 of the course GitHub repository.
</aside>

Our Brown writing agent uses a pre-commit configuration that you can find at `lessons/writing_workflow/.pre-commit-config.yaml`:

    fail_fast: false

    repos:
      - repo: <https://github.com/abravalheri/validate-pyproject>
        rev: v0.24.1
        hooks:
          - id: validate-pyproject

      - repo: <https://github.com/pre-commit/mirrors-prettier>
        rev: v3.1.0
        hooks:
          - id: prettier
            types_or: [yaml, json5]

      - repo: <https://github.com/astral-sh/ruff-pre-commit>
        rev: v0.12.1
        hooks:
          - id: ruff-check
            args: [--fix, --exit-non-zero-on-fix]
          - id: ruff-format

Let’s understand each hook:

  * `**validate-pyproject**`: This tool validates that your `pyproject.toml` file is structurally correct according to PEP standards. A malformed file can break the entire project.
  * `**prettier**`: A popular code formatter we use for configuration files like `.github/workflows/ci.yml`. Consistent formatting makes these files readable and reduces merge conflicts.
  * `**ruff-check**`**and**`**ruff-format**`: These hooks run Ruff, a modern Python linter and formatter. The `-fix` flag automatically fixes issues, and `-exit-non-zero-on-fix` ensures the hook fails even after auto-fixing, forcing you to review and re-stage the changes. The `ruff-check` hook runs before `ruff-format` as recommended by Ruff’s authors.

### Setting Up Pre-commit

In the `lessons/writing_workflow repo` (or any repo where you have configured your `.pre-commit-config.yaml` file), you can set up pre-commit hooks with:

    # Install dependencies (includes pre-commit)
    uv sync --dev

    # Install the Git hooks
    pre-commit install

The `pre-commit install` command creates a Git hook at `.git/hooks/pre-commit` . Now, every time you run `git commit`, pre-commit runs automatically. You can also run hooks manually:

    # Run all hooks on all files
    make pre-commit

The workflow is simple: make changes, stage them with `git add`, and run `git commit`. If hooks fail, review the errors, fix them, re-stage, and commit again. This tight feedback loop catches issues in seconds [[15]](<https://talkpython.fm/episodes/show/482/pre-commit-hooks-for-python-devs>).

## Ruff: Fast Python Linting and Formatting

[Ruff](<https://github.com/astral-sh/ruff>) is an extremely fast Python linter and formatter written in Rust [[3]](<https://docs.astral.sh/ruff/>). It replaces a collection of older tools like [Black](<https://github.com/psf/black>), [isort](<https://github.com/PyCQA/isort>), and [Flake8](<https://github.com/PyCQA/flake8>), consolidating them into a single binary that runs in milliseconds.

It’s important to understand the distinction between formatting and linting:

  * **Formatting** rewrites code to follow consistent style rules (indentation, line breaks). It is automatic and opinionated.
  * **Linting** analyzes code for bugs, suspicious patterns, and violations of best practices (unused variables, missing imports) [[1]](<https://docs.astral.sh/ruff/linter/>).

### Brown’s Ruff Configuration

Ruff’s configuration for Brown is in `lessons/writing_workflow/pyproject.toml`:

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

Here’s its meaning:

  * `target-version = "py312"` tells Ruff which Python version to use for syntax checks.
  * `line-length = 140` sets the maximum line length.
  * `select = [“F”, “E”, “I”]` enables rule sets for catching common bugs (Pyflakes), enforcing PEP 8 style (pycodestyle), and organizing imports (isort).
  * `known-first-party = [“src”, “tests”]` tells isort how to group project-specific imports.

💡
Brown provides convenience wrappers for Ruff in `lessons/writing_workflow/Makefile`:

    # --- Tests & QA ---

    QA_FOLDERS := src/ tests/ scripts/

    format-fix: # Auto-format Python code using ruff formatter.
    	uv run ruff format $(QA_FOLDERS)

    lint-fix: # Auto-fix linting issues using ruff linter.
    	uv run ruff check --fix $(QA_FOLDERS)

    format-check: # Check code formatting without making changes.
    	uv run ruff format --check $(QA_FOLDERS)

    lint-check: # Check code for linting issues without fixing them.
    	uv run ruff check $(QA_FOLDERS)

Each target uses `uv run` to execute commands within the project’s virtual environment [[16]](<https://devcenter.upsun.com/posts/why-python-developers-should-switch-to-uv/>), which is managed automatically and doesn’t require manual activation. You can run these from the `writing_workflow/` directory to check or fix your code before committing.

### Hands-On Example: Fixing Formatting Issues

To see Ruff’s formatter in practice, let’s take a poorly formatted Python file.

  1. Create a file with inconsistent spacing and line breaks.
    # test_formatting.py - intentionally poorly formatted
    def  badly_formatted_function(x,y,z):
        result=x+y+z
        my_list=[1,2,3,4,5,6,7,8,9,10]

  2. Check the formatting without making changes.
    ruff format --check test_formatting.py

  It outputs:

    Would reformat: test_formatting.py
    1 file would be reformatted

  3. Auto-fix the formatting.
  
    ruff format test_formatting.py

  It outputs:
  
    1 file reformatted

The file is now perfectly formatted, with consistent spacing and structure. This automation keeps the codebase clean and stylistically consistent with zero manual effort.

### Hands-On Example: Fixing Linting Issues

Linting catches bugs and quality issues.

  1. Create a file with an unused import and a duplicate import.
    # test_linting.py
    import os
    import sys
    import json  # Unused import

    # ... some code ...

    # Duplicate import at the bottom
    import sys
  
  2. Check for linting issues.
  
    ruff check test_linting.py
  It outputs:
  
    test_linting.py:3:8: F401 [*] `json` imported but unused
    test_linting.py:8:8: F811 [*] Redefinition of unused `sys` from line 2
    Found 2 errors.
    [*] 2 fixable with the `--fix` option.
  
  3. Auto-fix the issues.
  
    ruff check --fix test_linting.py

Ruff automatically removes the unused and duplicate imports. This demonstrates how linting catches and fixes potential bugs before they enter the codebase.

## Unit Tests for Agent Repos

Unit tests verify that code behaves correctly under controlled conditions. For AI agents, the core logic involves calling LLMs, which return non-deterministic outputs. Real API calls make tests slow, flaky, and expensive.
  * **Parsing and rendering:** Does your markdown loader extract articles correctly?
  * **Schema validation:** Does your Pydantic model reject invalid data?
  * **Routing decisions:** Given a specific state, does your workflow route to the correct node?
  * **Utilities:** Do helper functions for URL extraction or text cleaning work correctly?

### Unit Tests vs. Integration Tests

In traditional software, **unit tests** verify individual functions or classes in isolation, while **integration tests** verify that multiple components work together correctly. For AI agents, this distinction becomes blurred because most nodes integrate multiple components (prompt templates, LLM calls, parsers). We follow a pragmatic approach: if a test runs quickly with mocked dependencies and tests deterministic logic, we call it a unit test regardless of how many internal components it touches.

There are several patterns for mocking LLM calls in tests [[11]](<https://docs.langchain.com/oss/python/langchain/test>). In Brown, we use response injection, where we create a fake model class that returns pre-scripted responses. For most AI agent projects, this approach provides the best balance of simplicity and control.

</aside>
💡 Another option to mock LLM calls in tests is HTTP mocking, where you intercept API requests and return canned responses using libraries like responses or httpretty. Some teams prefer fixture-based mocking with pytest fixtures and unittest.mock.patch to replace LLM calls with fixed outputs. There's also record and replay, which captures real API responses once and then replays them in tests using tools like VCR.py.
</aside>

### Our Implementation: The FakeModel Pattern

In our Brown agent, we implement response injection with a `FakeModel` class that is compatible with LangChain’s interface. The pattern has three parts:

  1. **Configuration specifies the fake model:** The `debug.yaml` configuration at `lessons/writing_workflow/configs/debug.yaml` sets all nodes to use `model_id: “fake`”.
  2. **Model factory returns FakeModel:** The model builder in `src/brown/models/get_model.py` returns a `FakeModel` instance, when the configuration specifies it.
  3. **Tests inject specific responses:** The `FakeModel` in `src/brown/models/fake_model.py` extends LangChain’s `FakeListChatModel` and allows tests to inject a list of responses.

Here’s a part of the implementation of the `FakeModel` class:

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

An instance of the `FakeModel` class takes a list of pre-scripted responses in the constructor (`responses: list[str]`). When `ainvoke()` is called, it returns the first response from the list, and consumes it.

This design ensures that unit tests can run with a fake model by default, and individual tests can inject specific responses when needed.

### Example: Testing Nodes with Mocked Responses

For nodes that call LLMs, you mock the responses. Here is an example test from `lessons/writing_workflow/tests/brown/nodes/test_article_writer.py`:

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

The test creates a mock JSON response, builds a fake model, injects the response into it, and then instantiates the `ArticleWriter` node with that fake model. This pattern keeps tests fast, deterministic, and free [[7]](<https://brightsec.com/blog/unit-testing-best-practices/>).

### Running Brown’s Tests

To run Brown’s test suite, use the command from the `Makefile`:

    # From the writing_workflow directory
    make tests
This command runs `CONFIG_FILE=configs/debug.yaml uv run pytest`. The `debug.yaml` configuration ensures tests use the fake models and never call real LLMs.

## CI Workflows: Automated Enforcement

CI enforces checks by running them automatically on every push and pull request. If checks fail, the PR cannot be merged. We use GitHub Actions [[10]](<https://docs.github.com/en/actions>) for both the Brown and Nova agents, which integrates seamlessly with GitHub repositories and requires minimal setup [[4]](<https://docs.astral.sh/uv/guides/integration/github/>).

### Our Complete CI Configuration

The workflow file lives at `.github/workflows/ci.yml` in your repository. Here’s the complete configuration we use for both agents:

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

This configuration defines when the workflow runs and what checks it performs. The `on` section specifies that the workflow triggers on pull requests to the `main` and `dev` branches, as well as on direct pushes to `main`. This ensures that every code change gets validated before it can be merged.

The `env` section defines an environment variable `QA_FOLDERS` that lists all the directories we want to check. Notice it includes both `src/brown` and `src/nova`, allowing us to use the same CI configuration for both agents in a monorepo structure.

### Understanding the Job Structure

The workflow defines two independent jobs that run in parallel: `qa` and `tests`. Splitting them provides clear, fast feedback. If formatting fails, you immediately see “QA job failed” without waiting for tests to complete. This parallel execution saves time and makes it easier to identify which category of checks failed.

Each job runs on `ubuntu-latest`, which is a virtual machine provided by GitHub. The jobs are completely isolated from each other, which means they can run simultaneously without interference.

The `qa` job focuses on code quality checks that don’t require running the application. It starts by checking your code with `actions/checkout@v4 `, then installs  `uv ` using `astral-sh/setup-uv@v4 `. The Python setup step uses actions/setup-python@v5 and reads the Python version from your `.python-version` file, ensuring consistency between local development and CI. After syncing dependencies with `uv sync --dev` (which includes development dependencies needed for formatting and linting), it runs two checks. The format check uses `uv run ruff format --check` to verify that all code follows consistent formatting rules without modifying any files. The lint check uses `uv run ruff check` to detect code quality issues, unused imports, and potential bugs.

The `tests` job follows a similar setup process. It runs `uv sync` without the `--dev` flag since tests don’t require development tools like formatters. The test step uses `CONFIG_FILE=configs/debug.yaml` to ensure tests run with the fake model configuration, preventing any real LLM API calls during CI. This keeps tests fast, deterministic, and free.

### Setting Up GitHub Actions for Your Repository

To enable this CI workflow in your repository, you need to create the workflow file in the correct location. GitHub Actions looks for workflow files in the `.github/workflows/` directory at the root of your repository.

First, create the directory structure if it doesn’t already exist. From your repository root, run `mkdir -p .github/workflows`. Then create the file `.github/workflows/ci.yml` and paste the complete configuration shown above. Make sure your repository has a `.python-version` file at the root that specifies which Python version to use, such as `3.12`. You should also ensure that `configs/debug.yaml` exists and configures your agents to use fake models for testing.

Once you commit and push this file to GitHub, the workflow becomes active immediately. You don’t need to configure anything in the GitHub UI for basic workflows, though you will need to add secrets for more advanced scenarios, such as API keys for evaluation workflows.

### Running the Pipeline and Observing Results

The pipeline runs automatically whenever its trigger conditions are met. When you push a commit directly to the `main` branch, GitHub Actions executes the workflow within seconds. When you open a pull request targeting `main` or `dev`, the workflow runs automatically and reports its status on the pull request page.

You can also trigger the workflow manually to test changes or re-run failed checks. Navigate to your repository on GitHub and click the “Actions” tab at the top. You’ll see a list of all your workflows. Click on “CI” to view all runs of this workflow. In the top right corner, you’ll see a “Run workflow” button. Click it, select the branch you want to run the workflow on, and click the green “Run workflow” button. This is particularly useful when you want to verify that a fix works without creating a new commit or pull request.

To monitor a workflow run, click any run in the list to view its details. The interface shows both jobs (`qa` and `tests`) with their current status. You can click each job to view the output of its individual steps. If a step fails, its output is expanded automatically and highlighted in red, making it easy to identify the problem. The format and lint checks show exactly which files have issues and what needs to be fixed.

### Interpreting CI Results and Fixing Issues

When the CI pipeline runs, it produces one of three outcomes for each job: success (green checkmark), failure (red X), or in progress (yellow dot). GitHub also displays the overall status on your pull request, preventing merges when checks fail.

If the `qa` job fails due to formatting; the output shows which files would be reformatted and exactly what changes Ruff would make to them. You can fix this locally by running `make format-fix` from the `writing_workflow/` directory, then committing and pushing the formatted code. If the `qa` job fails on linting, the output lists each violation with its file location, line number, and error code. Many of these can be auto-fixed by running `make lint-fix` locally.

If the `tests` job fails, the pytest output shows which test failed and why. The traceback helps you identify the issue, whether it’s a logic error, an incorrect mock response, or a missing dependency. You should fix the underlying issue, verify the fix by running `make tests` locally, then push your changes.

A critical principle is that CI should run the exact same commands you run locally. The `qa` job executes `uv run ruff format --check` and `uv run ruff check`, which are identical to the targets your Makefile runs. The `tests` job runs `CONFIG_FILE=configs/debug.yaml uv run pytest`, which is exactly what `make tests` does. This eliminates “works on my machine” problems. If tests pass locally with `make tests`, they will pass in CI, and if they fail in CI, you can reproduce the failure locally by running the same command.

### Trying It Out

The best way to understand how CI works is to intentionally trigger a failure and observe the results. Try introducing a formatting violation by creating a file with inconsistent spacing, committing it, and pushing to a branch. Open a pull request and watch the `qa` job fail with clear output showing what needs to be fixed. Then run `make format-fix` locally, commit the corrected code, and push again. The CI pipeline will re-run automatically, and this time the checks will pass.

You can also experiment with the manual trigger feature. Go to the Actions tab, run the workflow on your current branch, and observe how the jobs execute. This hands-on experience will make the abstract concept of CI concrete and help you develop confidence in the system.

## AI Evaluations as Regression Tests

AI evaluations serve a critical purpose: regression testing [[9]](<https://www.deepchecks.com/llm-evaluation/ci-cd-pipelines/>). A change might pass all unit tests but degrade the semantic quality of the agent’s output. AI evaluations catch these regressions.

### Why AI Evals Are Unique to AI Systems

Traditional CI lacks an equivalent to Tier 3 evaluations because unit and integration tests are fast enough to run on every commit. For AI agents, semantic quality testing requires real LLM calls, which are slow and expensive.

A modest evaluation dataset of 10 samples could require 50-100 LLM calls. At an average cost of $0.05 per call, a single evaluation run might cost $2.50-$5.00 (Note: Frequent current price check from LLM provider is important as costs changes over time). Running this on every commit for a team of five could cost thousands of dollars per month and slow development to a crawl. This is why we run them selectively.

### Manual-Trigger CI Workflow for AI Evals

Here’s an example of what a CI workflow for evaluations might look like. You could save it to `.github/workflows/eval.yml`. Note that this is illustrative: a working implementation would use the actual evaluation scripts we developed in previous lessons (like those using Opik for scoring and metrics).

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

This workflow differs from the main CI pipeline in several key ways. The `workflow_dispatch` trigger means it never runs automatically. You must manually trigger it from the Actions tab in GitHub. This prevents expensive API calls from running on every commit.

The workflow uses a production configuration (`configs/production.yaml`) instead of the debug configuration used in tests. This ensures evaluations use real LLM models rather than fake models. The `LLM_API_KEY` environment variable pulls from GitHub Secrets, which you configure in your repository settings under **Settings → Secrets and variables → Actions**. This keeps API keys secure and out of your codebase.

The evaluation command (`python -m scripts.run_eval`) should point to your evaluation script that loads your dataset, runs your agent on each sample, and computes metrics. The exact implementation depends on your evaluation framework, whether that’s Opik, LangSmith, or a custom solution.

To trigger this workflow, navigate to the Actions tab, select “**AI Evaluations** ” from the workflow list, click “**Run workflow,** ” choose your branch, and click the green “**Run workflow** ” button. The workflow will run and display results in the Actions interface, including logs that show evaluation metrics and any failures.

The decision on when to run AI evals depends on your project’s maturity:

  * **Early development:** Run manually to measure progress weekly or after major changes.
  * **Active development:** Run before merging significant changes to catch regressions.
  * **Mature product:** Run as part of your release process to ensure production quality never degrades.

## Daily Development Workflow

With these tools in place, a typical daily workflow looks like this:
 
  1. **Write code** and corresponding tests.
  2. **Run quick checks** periodically: make lint-check and make format-check.
  3. **Run tests** after changing logic: `make tests`.
  4. **Commit your changes.** Pre-commit hooks will run automatically.
  5. **Push and open a pull request.** CI runs automatically, enforcing all checks.
  6. **Before releasing, run AI evaluations** manually to check for quality regressions.

This workflow takes seconds for most commits and catches issues early.

## Conclusion

Continuous Integration for AI agents adapts traditional software engineering practices to the unique challenges of LLM-powered systems. The three-tier model: fast checks, deterministic tests with mocked LLMs, and selective AI evaluations provides a robust framework for building maintainable and reliable agents. The investment in CI pays for itself the first time it catches a regression before your customers see it.

## References

  1. Astral. (n.d.-a). _Ruff Linter_. Ruff Docs. <https://docs.astral.sh/ruff/linter/>
  2. Astral. (n.d.-b). _ruff-pre-commit_. GitHub. <https://github.com/astral-sh/ruff-pre-commit>
  3. Astral. (n.d.-c). Ruff. Ruff Docs. <https://docs.astral.sh/ruff/>
  4. Astral. (n.d.-d). _Integration with GitHub Actions_. uv Docs. <https://docs.astral.sh/uv/guides/integration/github/>
  5. Astral. (n.d.-e). _Integration with pre-commit_. uv Docs. <https://docs.astral.sh/uv/guides/integration/pre-commit/>
  6. BetterStack. (n.d.). _pyproject.toml explained_. BetterStack Community. <https://betterstack.com/community/guides/scaling-python/pyproject-explained/>
  7. Bright Security. (n.d.). _Unit testing best practices: 13 ways to improve your tests_. Bright Security Blog. <https://brightsec.com/blog/unit-testing-best-practices/>
  8. CiCUBE. (n.d.). _How to run jobs in parallel with GitHub Actions_. DEV Community. <https://dev.to/cicube/how-to-run-jobs-in-parallel-with-github-actions-4png>
  9. Deepchecks. (n.d.). _LLM evaluation for CI/CD pipelines: A practical guide_. <https://www.deepchecks.com/llm-evaluation/ci-cd-pipelines/>
  10. GitHub. (n.d.). _GitHub Actions documentation_. GitHub Docs. <https://docs.github.com/en/actions>
  11. LangChain. (n.d.). _Testing_. LangChain Docs. <https://docs.langchain.com/oss/python/langchain/test>
  12. Paul, K. (n.d.). _A practical guide to integrating AI evals into your CI/CD pipeline_. DEV Community. <https://dev.to/kuldeep_paul/a-practical-guide-to-integrating-ai-evals-into-your-cicd-pipeline-3mlb>
  13. pre-commit. (n.d.). _pre-commit_. [https://pre-commit.com](<https://pre-commit.com/>)
  14. pytest. (n.d.). _pytest documentation_. <https://docs.pytest.org/>
  15. Upsun. (n.d.). _Why Python developers should switch to uv_. Upsun DevCenter. <https://devcenter.upsun.com/posts/why-python-developers-should-switch-to-uv/>