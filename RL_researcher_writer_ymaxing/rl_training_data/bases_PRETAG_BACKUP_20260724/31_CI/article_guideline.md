## Global Context of the Lesson

### What We Are Planning to Share

We will write a lesson that introduces Continuous Integration as automated infrastructure tailored for AI agent codebases. We begin by anchoring in prior observability and evaluation-driven development work, then explain the core shift from experimental prototypes to maintainable production systems. We contrast traditional software CI with AI-specific realities such as non-deterministic outputs, prompt volatility, and schema evolution. The central framework is the three-tier model (fast formatting/linting, deterministic mocked tests, and selective expensive AI evals). We then walk through practical implementation details for pre-commit hooks, Ruff, FakeModel test patterns, GitHub Actions workflows, and AI evals used as regression tests before synthesizing everything into a daily development workflow and positioning CI as a foundational production skill.

### Why We Think It's Valuable

AI agent code evolves rapidly with prompt tweaks, model swaps, and discovered edge cases, making manual quality control unsustainable and prone to regressions that impact semantic output quality. CI adapted for AI provides fast feedback, enforces consistency, eliminates flaky tests, and selectively applies expensive evals, enabling engineering teams to scale development while maintaining production reliability.

### Expected Length of the Lesson
**4,350 words**

### Theory / Practice Ratio

60% theory - 40% practice

## Anchoring the Lesson in the Course

### Details About the Course

This piece is part of a broader course on AI agents and LLM workflows. The course consists of 3 parts, each with multiple lessons. 

Thus, it's essential to always anchor this piece into the broader course, understanding where the reader is in its journey. You will be careful to consider the following:
- The points of view.
- To not reintroduce concepts already thought in the previous lesson.
- To be careful when talking about concepts introduced only in future lessons.
- To always reference previous and future lessons when discussing topics outside the piece's scope.

### Lesson Scope

This is Lesson 31 of the Agentic AI Engineering course following recent coverage of agent observability (Opik), offline evaluation datasets, and evaluation-driven development; it precedes topics on production deployment, monitoring, and full CI/CD pipelines.

### Point of View

The course is created by a team writing for a single reader, also known as the student. Thus, for voice consistency across the course, we will always use 'we,' 'our,' and 'us' to refer to the team who creates the course, and 'you' or 'your' to address the reader. Avoid singular first person and don't use 'we' to refer to the student.

Examples of correct point of view:
- Instead of "Before we can choose between workflows and agents, we need a clear understanding of what they are." word it as "To choose between workflows and agents, you need a clear understanding of what they are."

### Who Is the Intended Audience

AI engineers who have built prototype agents with LangChain-style frameworks, understand basic LLM integration and Python development, and are now focused on productionizing systems with robust engineering practices like testing and automation.

### Concepts Introduced in Previous Lessons

In previous lessons of the course, we introduced the following concepts:
**Part 1:**

- **Lesson 1 - AI Engineering & Agent Landscape**: Understanding the role, the stack, and why agents matter now
- **Lesson 2 - Workflows vs. Agents**: Grasping the crucial difference between predefined logic and LLM-driven autonomy
- **Lesson 3 - Context Engineering**: The art of managing information flow to LLMs
- **Lesson 4 - Structured Outputs**: Ensuring reliable data extraction from LLM responses
- **Lesson 5 - Basic Workflow Ingredients**: Implementing chaining, routing, parallel and the orchestrator-worker patterns
- **Lesson 6 - Agent Tools & Function Calling**: Giving your LLM the ability to take action
- **Lesson 7 - Planning & Reasoning**: Understanding patterns like ReAct (Reason + Act)
- **Lesson 8 - Implementing ReAct**: Building a reasoning agent from scratch
- **Lesson 9 - Agent Memory & Knowledge**: Short-term vs. long-term memory (procedural, episodic, semantic)
- **Lesson 10 - RAG Deep Dive**: Advanced retrieval techniques for knowledge-augmented agents
- **Lesson 11 - Multimodal Data**: Foundations and Implementations of Multimodal LLMs

**Part 2:**

- **Lesson 12 - Central Project: Scope & Design**: Introducing the scope and design of the central project
- **Lesson 13 - Agent Frameworks Overview & Comparison**: Dimensions of choosing suitable a agent framework, justifying the choices made for our central project
- **Lesson 14 - LLM Agent System Design Considerations and Framework**: Decision framework of system design, inference-time scaling and the cost/latency calculus
- **Lesson 15 - Nova End-to-End Project Walkthrough**: The end-to-end architecture of Nova: The research workflow
- **Lesson 16 - Foundations of Agentic Systems with FastMCP**: The primitives and transports of MCP and how MCP servers and clients are organized
- **Lesson 17 - Initial Data Ingestion and Tooling**: Tools to parallelize data processing in the ingestion layer 
- **Lesson 18 - The Research Loop: Query Generation, Perplexity, and Human Feedback**: The research loop - generating queries, integrating external web searches, and adding human feedbacks.
- **Lesson 19 - Final Outputs and Agent Completion**: Filter and scrape search results, create the final output of the research workflow
- **Lesson 20 - Brown End-to-End Project Walkthrough**: The end-to-end architecture of Brown: The writing workflow
- **Lesson 21 - Behind the Scenes of Iterating AI Architectures with the Brown Writing Agent**: The technical details about the architecture of Brown: The writing workflow
- **Lesson 22 - Implementing the Foundations of the Writing Workflow**: Context loading including writing profiles, media generation using the orchestrator-worker pattern and article generation using context enginnering
- **Lesson 23 - Reviewing and Editing Through the Evaluator-Optimizer Pattern**: Transforming linear writing workflow into a reliable, self-correcting system by implementing the Evaluator-Optimizer pattern
- **Lesson 24 - Human-in-the-Loop Through MCP Servers**: Adding human-in-the-loop MCP tools to enable editing the whole article or selected text workflow 
- **Lesson 25 - Orchestrate and Integrate Our Capstone Agents**: Introducing two architecture of the Central LLM orchestration pattern - Multi-Server Client & Composed Server - to integrate the two agents
- **Lesson 26 - End-to-End Demo: Generating a Course Lesson**: The end-to-end demo of Brown: The writing workflow

**Part 3:**

- **Lesson 27 - Agent Observability with Opik**: Introducing Opik as the main instrument to observe the activities of the two agents
- **Lesson 28 - Creating Datasets for AI Evals**: Building the dataset for evaluating the writing workflow
- **Lesson 29 - Defining the Evaluation Processes and Metrics Theory**: Exploring metric types, prioriting business and custom metrics, adopting binary metrics over anything else
- **Lesson 30 - Evaluating the Writing Workflow**: Designing, implementing and aligning custom LLM judges, building the end-to-end evaluation pipeline

As this is the fifth lesson in Part 3 - Evaluation, Observability, Optimizations, and Deployment, after we integrated Opik for observability, prepared the offline evals dataset from scratch and learned the theory behind writing good business metrics, and covered the evaluation-driven development framework in previous lessons, we shift focus to Continuous Integration (CI): the automated infrastructure that keeps your codebase maintainable and prevents regressions from reaching production.


### Concepts That Will Be Introduced in Future Lessons

In future lessons of the course, we will introduce the following concepts:

- Stateless architecture, authentication with Descope, containerization with Docker
- Database and File Download/Upload, moving all states to a PostgreSQL database
- Continuous Deployment: set up the gcloud infrastructure, create a production-ready deployment pipeline 

If you must mention these, keep it high-level and note we will cover them in their respective lessons.

### Anchoring the Reader in the Educational Journey

Within the course we are teaching the reader multiple topics and concepts. Thus, understanding where the reader is in it's educational journey it's critical for this piece. You have to use only previous introduced concepts, while being reluctant about using concepts that haven't been introduced yet.

When discussing the **concepts introduced in previous lessons** listed in the `Concepts Introduced in Previous Lessons` section, avoid reintroducing them to the reader. Especially don't reintroduce the acronyms. Use them as if the reader already knows what they are. 

Avoid using all the **concepts that haven't been introduced in previous lessons** listed in the `Concepts That Will Be Introduced in Future Lessons` subsection. Whenever another concept requires references to these banned concepts, instead of directly using it, use other intuitive and grounded explanations as you would explain them to a 7-year-old. For example:
- If the "tools" concept wasn't introduced yet and you have to talk about agents, refer them to as "actions".
- If the "routing" concept wasn't introduced yet and you have to talk about it, refer it to as "guiding the workflow between multiple decisions".
You can use the concepts that haven't been introduced in previous lessons listed in the `Concepts That Will Be Introduced in Future Lessons` subsection, only if we explicitly specify them. Still, even in that case, as the reader doesn't know how that concept works, you are just allowed to use the term, while keeping the explanation extremely high-level and intuitive, as if you were explaining it to a 7-year-old.
Whenever you use a concept from the `Concepts That Will Be Introduced in Future Lessons` subsection explicitly specify that it will be explained in more detail in future lessons.

In all use cases avoid using acronyms that aren't explicitly stated in the guidelines. Rather use other more accessible synonyms or descriptions that are easier to understand by non-experts.

## Narrative Flow of the Lesson

Follow the next narrative flow when writing the end-to-end lesson:

- What problem are we solving? Why is it essential to solve it?
	- Start with a personal story where we encountered the problem
- Why other solutions are not working and what's wrong with them.
- At a theoretical level, explain our solution or transformation. Highlight:
    - The theoretical foundations.
    - Why is it better than other solutions?
    - What tools or algorithms can we use?
- Provide some hands-on examples.
- Go deeper into the advanced theory.
- Provide a more complex example supporting the advanced theory.
- Connect our solution to the bigger picture and next steps.

## Lesson Outline

1. Introduction
2. What is Continuous Integration?
3. Pre-commit Hooks: Automated Local Guardrails
4. Ruff: Fast Python Linting and Formatting
5. Unit Tests for Agent Repos
6. CI Workflows: Automated Enforcement
7. AI Evaluations as Regression Tests
8. Daily Development Workflow
9. Conclusion

## Section 1 - Introduction

- Anchor the reader by referencing prior lessons on observability with Opik for tracing and capturing agent runs plus building and using offline evaluation datasets and the evaluation-driven development framework; these give you the visibility required before CI can be effective. Tell the readers that it's time to shift to CI - the automated infrastructure that keeps your codebase maintainable and prevents regressions from reaching production.
- Transition to Section 2: With the problem and failure modes clear, we now define what Continuous Integration means in an AI context and introduce the three-tier model that solves these issues.
- **Section length:** 70 words

## Section 2 - What is Continuous Integration?

- Define standard CI as the practice of frequent merges into a shared repository combined with automated checks that catch integration issues early, preventing "it works on my machine" problems.
- Contrast traditional software CI (focused on deterministic logic, compile checks, and unit tests) versus AI agent needs: non-determinism from LLM calls, rapid prompt iteration that breaks previous assumptions, and high API costs that make naive test suites impractical.

- Elaborate on the three typical failure modes without CI in three numbered subsections: 

1. **Inconsistent code formatting across the team.** - formatting/style drift that wastes review time. Explain the failure mode further with an example where team members using different formatters or manual formatting leading to cluttered code and time-wasting code reviews.

2. **Skipped pre-commit checks, leading to CI failures.** - skipped manual quality gates under velocity pressure without automated enforcement. Explain the failure mode further with an example where developers forgot to run the test suire before pushing, which then results in failure.

3. **Non-deterministic tests that call real LLM APIs.** - flaky tests caused by real LLM calls that are slow, expensive and non-deterministic, and fail unpredictably and slow down the team.

- Introduce the three-tier model calibrated by cost and speed in three subsections:    

  * **Tier 1: Formatting and Linting (Always Run).** These checks are fast (taking seconds) and cheap (no API calls). They catch syntactic issues and enforce style consistency. This tier is identical to traditional CI.
  * **Tier 2: Unit and Integration Tests (Always Run).** These verify deterministic logic, such as parsing, schema validation, and routing, without calling external APIs. By mocking LLM responses, tests run quickly (under a minute) and reliably.
  * **Tier 3: AI Evaluations (Manual/Release).** This tier is unique to AI systems. It involves expensive, LLM-based quality checks that use real API calls to evaluate agent quality on a curated dataset. We run these selectively before major releases or after significant prompt changes.

- Include the image in the link <https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/6bf41859-7dd2-4a23-9a88-55720f54114e/image/w=1920,quality=90,fit=scale-down>, the caption should be verbatim - "Image 1: A three-tier CI model for AI agents, showing the flow from commit checks to PR tests and finally to manual/release AI evaluations, with each tier distinctly colored."

- Position AI evaluations (built on your existing offline evaluation datasets and Opik traces) as a Tier 3 regression test uniquely suited to catch semantic quality regressions that traditional unit tests cannot detect.
- Clarify lesson scope boundaries: This lesson covers CI essentials for building production-ready AI agents. We focus on practical techniques you will use daily: automated quality checks, testing with mocked LLMs, and structuring CI pipelines around cost constraints. We will not cover comprehensive DevOps topics like Kubernetes or Terraform. Instead, we teach you how to effectively move from prototype to production-ready agents.

We will cover:

  * Setting up pre-commit hooks to enforce code quality automatically.
  * Configuring Ruff for linting and formatting.
  * Writing unit tests for deterministic agent code with mocked LLM responses.
  * Building a CI pipeline that runs automatically on every change.
  * Using AI evaluations as selective regression tests in CI.

- Tell the readers this lesson includes a hands-on notebook where you will practice running formatting checks, linting, and tests on Brown, our writing agent.

- Transition to Section 3: With the three-tier model established, the fastest feedback comes from running the first tier locally before you even commit code; this is where pre-commit hooks come in.
- **Section length:** 600 words

## Section 3 - Pre-commit Hooks: Automated Local Guardrails

- Explain pre-commit hooks as Git-based local guardrails that run automatically on every commit, delivering immediate feedback and preventing bad code from ever reaching the shared repository.
- The **pre-commit** framework manages Git hooks using a declarative YAML configuration. You define hooks in `.pre-commit-config.yaml`, and the framework handles installation and execution. Hooks are references to external repositories, so the community maintains them for popular tools.

### Brown’s Pre-commit Configuration

</aside>
💡
You can experiment with the code for this lesson in this [Colab](<https://colab.research.google.com/github/louisfb01/agent-course-notebooks/blob/main/notebooks/lesson_31_notebook.ipynb#scrollTo=b30eba1a>).
Alternatively, you can find the code for this lesson in the notebook for Lesson 31 of the course GitHub repository.
</aside>

- Detail the specific hook selection used in the Brown agent codebase: pyproject.toml validation, prettier for JSON/YAML configs, and ruff check plus format with auto-fix behavior enabled. In order to do that, you need to use the output of `!cat .pre-commit-config.yaml` in the subsection `2.1 Pre-commit Configuration` in the provided Notebook in the section "## Article code" of this guideline - the output show config defined in `lessons/writing_workflow/.pre-commit-config.yaml`.

- Then, walk through each of the three hooks in the output:
  * `**validate-pyproject**`: This tool validates that your `pyproject.toml` file is structurally correct according to PEP standards. A malformed file can break the entire project.
  * `**prettier**`: A popular code formatter we use for configuration files like `.github/workflows/ci.yml`. Consistent formatting makes these files readable and reduces merge conflicts.
  * `**ruff-check**`**and**`**ruff-format**`: These hooks run Ruff, a modern Python linter and formatter. The `-fix` flag automatically fixes issues, and `-exit-non-zero-on-fix` ensures the hook fails even after auto-fixing, forcing you to review and re-stage the changes. The `ruff-check` hook runs before `ruff-format` as recommended by Ruff’s authors.

### Setting Up Pre-commit

- Walk through the installation and daily workflow: 

In the `lessons/writing_workflow repo` (or any repo where you have configured your `.pre-commit-config.yaml` file), you can set up pre-commit hooks with:

    # Install dependencies (includes pre-commit)
    uv sync --dev

    # Install the Git hooks
    pre-commit install

The `pre-commit install` command creates a Git hook at `.git/hooks/pre-commit` . Now, every time you run `git commit`, pre-commit runs automatically. You can also run hooks manually:

    # Run all hooks on all files
    make pre-commit

The workflow is simple: make changes, stage them with `git add`, and run `git commit`. If hooks fail, review the errors, fix them, re-stage, and commit again.

- Transition to Section 4: Pre-commit hooks often rely on fast tools like Ruff to do the actual work; next we examine Ruff in depth and show how to configure and run it both locally and in CI.

- **Section length:** 400 words

## Section 4 - Ruff: Fast Python Linting and Formatting

- Introduce Ruff as a Rust-based, high-speed consolidated replacement for older tools such as Black, isort, Flake8, and pydocstyle, delivering sub-second performance even on large codebases.

- Clearly distinguish formatting (automatic, opinionated enforcement of style such as line length and quote style) from linting (detection of bugs, best-practice violations, and complexity issues):

  * **Formatting** rewrites code to follow consistent style rules (indentation, line breaks). It is automatic and opinionated.
  * **Linting** analyzes code for bugs, suspicious patterns, and violations of best practices (unused variables, missing imports) 

### Brown’s Ruff Configuration

- Use the output of `!grep -A 20 "\[tool.ruff\]" pyproject.toml` in the subsection `2.2 Ruff Configuration` in the provided Notebook in the section "## Article code" of this guideline to cover key configuration dimensions in `lessons/writing_workflow/pyproject.toml`. You also need to explain the keys in Ruff's config:

  * `target-version = "py312"` tells Ruff which Python version to use for syntax checks.
  * `line-length = 140` sets the maximum line length.
  * `select = [“F”, “E”, “I”]` enables rule sets for catching common bugs (Pyflakes), enforcing PEP 8 style (pycodestyle), and organizing imports (isort).
  * `known-first-party = [“src”, “tests”]` tells isort how to group project-specific imports.


- Use the output `!sed -n '/# --- Tests & QA ---/,$p' Makefile | tail -n +2` in the subsection `2.3 Makefile QA Targets` in the provided Notebook in the section "## Article code" of this guideline to show the Makefile convenience targets that wrap `uv run` commands.

- Each target uses `uv run` to execute commands within the project’s virtual environment, which is managed automatically and doesn’t require manual activation. You can run these from the `writing_workflow/` directory to check or fix your code before committing.

### Hands-On Example: Fixing Formatting Issues

- Provide hands-on patterns: use the code and outputs in the section 4 - `Running Formatting Checks` - in the provided Notebook in the section "## Article code" of this guideline to deliberately introduce broken code with various formatting issues, then demonstrate running the check commands followed by auto-fix commands to restore compliance, illustrating the tight iteration loop.

### Hands-On Example: Fixing Linting Issues

- Provide hands-on patterns: use the code and outputs in the section 5 - `Running Linting Checks` - in the provided Notebook in the section "## Article code" of this guideline to deliberately introduce broken code with various linting issues, then demonstrate running the check commands followed by auto-fix commands to restore compliance, illustrating the tight iteration loop.

- Include a contrast with older tools: Ruff combines 10+ legacy linters into one binary, eliminating version conflicts and dramatically reducing CI times.

- Transition to Section 5: Once formatting and linting guardrails are in place, attention turns to verifying the deterministic logic inside your agent nodes; this is the role of unit tests.

- **Section length:** 530 words

## Section 5 - Unit Tests for Agent Repos

- Surface the core challenge of LLM non-determinism: real API calls make tests slow, expensive, and flaky because identical prompts can produce varying outputs or even hit rate limits.

- Explain the role of unit tests in verifying deterministic agent logic such as parsing logic, schema validation, routing decisions, and utility functions that do not involve live LLM calls:
  * **Parsing and rendering:** Does your markdown loader extract articles correctly?
  * **Schema validation:** Does your Pydantic model reject invalid data?
  * **Routing decisions:** Given a specific state, does your workflow route to the correct node?
  * **Utilities:** Do helper functions for URL extraction or text cleaning work correctly?

### Unit Tests vs. Integration Tests

- First present the definition of **unit tests** and **integration tests** in traditional software. Then, discuss the pragmatic blurring of unit versus integration test boundaries that occurs with agent nodes, since a single node often combines prompt templating, structured output parsing, and routing in one logical unit. Tell the readers that we follow a pragmatic approach: if a test runs quickly with mocked dependencies and tests deterministic logic, we call it a unit test regardless of how many internal components it touches.

- Present mocking strategies with emphasis on response injection, which is used in Brown - the writing workflow - via a compatible fake model class rather than patching at the HTTP layer, which provides the best balance of simplicity and control for most AI agents projects.

- Include the following callout box that briefly introduces another mocking strategy - HTTP mocking:

</aside>
💡 Another option to mock LLM calls in tests is HTTP mocking, where you intercept API requests and return canned responses using libraries like responses or httpretty. Some teams prefer fixture-based mocking with pytest fixtures and unittest.mock.patch to replace LLM calls with fixed outputs. There's also record and replay, which captures real API responses once and then replays them in tests using tools like VCR.py.
</aside>

### Our Implementation: The FakeModel Pattern

In our Brown agent, we implement response injection with a `FakeModel` class that is compatible with LangChain’s interface. 

- List the three parts of the FakeModel pattern:

  1. **Configuration specifies the fake model:** The `debug.yaml` configuration at `lessons/writing_workflow/configs/debug.yaml` sets all nodes to use `model_id: “fake`”.
  2. **Model factory returns FakeModel:** The model builder in `src/brown/models/get_model.py` returns a `FakeModel` instance, when the configuration specifies it.
  3. **Tests inject specific responses:** The `FakeModel` in `src/brown/models/fake_model.py` extends LangChain’s `FakeListChatModel` and allows tests to inject a list of responses.

- Insert the following code showcasing the implementation of the `FakeModel` class:

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

- Finally, emphasize that this design ensures that unit tests can run with a fake model by default, and individual tests can inject specific responses when needed.

### Example: Testing Nodes with Mocked Responses

For nodes that call LLMs, you mock the responses.

- Give the test-writing recipe by including an example test from `lessons/writing_workflow/tests/brown/nodes/test_article_writer.py`:

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

The test creates a mock JSON response, builds a fake model, injects the response into it, and then instantiates the `ArticleWriter` node with that fake model. Argue that this pattern keeps tests fast, deterministic, and free.

### Running Brown’s Tests

To run Brown’s test suite, use the command from the `Makefile`:

    # From the writing_workflow directory
    make tests
    
This command runs `CONFIG_FILE=configs/debug.yaml uv run pytest`. The `debug.yaml` configuration ensures tests use the fake models and never call real LLMs.

- Transition to Section 6: Local tests and hooks give fast feedback, but enforcement at the repository level requires automated CI workflows that run on every pull request.

- **Section length:** 750 words

## Section 6 - CI Workflows: Automated Enforcement

- Introduce GitHub Actions as the CI platform of choice for both the Brown and Nova agents: it triggers on pull requests or pushes, supports job isolation, matrix builds, parallel execution so feedback remains fast, and integrates seamlessly with GitHub repositories and requires minimal setup.

### Our Complete CI Configuration

- Include the following complete configuration we use for both agents from the workflow file that lives at `.github/workflows/ci.yml` in our repository:

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

- Dissect the complete ci.yml file anatomy: 

This configuration defines when the workflow runs and what checks it performs. The `on` section specifies that the workflow triggers on pull requests to the `main` and `dev` branches, as well as on direct pushes to `main`. This ensures that every code change gets validated before it can be merged.

The `env` section defines an environment variable `QA_FOLDERS` that lists all the directories we want to check. Notice it includes both `src/brown` and `src/nova`, allowing us to use the same CI configuration for both agents in a monorepo structure.

### Understanding the Job Structure

- Break down the QA job step-by-step: checkout, uv Python setup using .python-version file, installation of dev dependencies, then sequential execution of format-check and lint-check steps:

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

- Transition to Section 7: The first two tiers run on every commit, but semantic quality requires a more expensive third tier; this is where AI evaluations enter as selective regression tests.

- **Section length:** 1350 words

## Section 7 - AI Evaluations as Regression Tests

- Explain the critical purpose of AI evals in CI: they catch semantic quality regressions (e.g., degraded helpfulness or increased hallucination rate) that deterministic unit tests cannot detect.

### Why AI Evals Are Unique to AI Systems

- Justify why evals are an AI-unique Tier 3 gate: each evaluation run incurs real LLM calls whose latency and token cost add up quickly. Include a concrete math example: 500-example dataset at $0.01 per 1k tokens equals roughly $X per full run.

### Manual-Trigger CI Workflow for AI Evals

- Detail the manual-only workflow_dispatch pattern in eval.yml that prevents accidental expensive runs on every commit or PR, reserving the workflow for deliberate triggers by including the following example of what a CI workflow for evaluations - `.github/workflows/eval.yml` (Note that this is illustrative: a working implementation would use the actual evaluation scripts we developed in previous lessons (like those using Opik for scoring and metrics).
):

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

- Mention that this workflow differs from the main CI pipeline in several key ways:

1. The `workflow_dispatch` trigger means it never runs automatically. You must manually trigger it from the Actions tab in GitHub. Stress that this prevents expensive API calls from running on every commit.

2. The workflow uses a production configuration (`configs/production.yaml`) instead of the debug configuration used in tests. Stress that this ensures evaluations use real LLM models rather than fake models. The `LLM_API_KEY` environment variable pulls from GitHub Secrets, which you configure in your repository settings under **Settings → Secrets and variables → Actions**. This keeps API keys secure and out of your codebase.

- The evaluation command (`python -m scripts.run_eval`) should point to your evaluation script that loads your dataset, runs your agent on each sample, and computes metrics. The exact implementation depends on your evaluation framework, whether that’s Opik, LangSmith, or a custom solution.

- To trigger this workflow, navigate to the Actions tab, select “**AI Evaluations** ” from the workflow list, click “**Run workflow,** ” choose your branch, and click the green “**Run workflow** ” button. The workflow will run and display results in the Actions interface, including logs that show evaluation metrics and any failures.

- Present the decision framework for eval frequency by project maturity:

  * **Early development:** Run manually to measure progress weekly or after major changes.
  * **Active development:** Run before merging significant changes to catch regressions.
  * **Mature product:** Run as part of your release process to ensure production quality never degrades.

- Transition to Section 8: With all three tiers understood, we can now assemble them into a cohesive daily development workflow that keeps velocity high while protecting quality.

- **Section length:** 520 words

## Section 8 - Daily Development Workflow

With these tools in place, a typical daily workflow looks like this:
 
  1. **Write code** and corresponding tests.
  2. **Run quick checks** periodically: make lint-check and make format-check.
  3. **Run tests** after changing logic: `make tests`.
  4. **Commit your changes.** Pre-commit hooks will run automatically.
  5. **Push and open a pull request.** CI runs automatically, enforcing all checks.
  6. **Before releasing, run AI evaluations** manually to check for quality regressions.

This workflow takes seconds for most commits and catches issues early.

- Transition to Section 9: We have now covered the full spectrum from theory to daily practice; the conclusion ties everything together.

- **Section length:** 80 words

## Section 9 - Conclusion

- Summarize the three-tier CI model as a pragmatic adaptation of traditional software practices to the unique realities of LLM-powered agent systems (non-determinism, prompt volatility, and cost constraints).
- Reiterate the value proposition: the upfront investment in hooks, Ruff configuration, FakeModel patterns, GitHub Actions, and selective evals pays off by catching regressions before customers experience quality drops.
- Position CI as the foundational engineering step that moves you from fragile prototypes toward reliable, maintainable, team-scale production agents.
- Connect to future lessons by noting that full CI/CD integration (including automated deployment triggers), production monitoring built on your existing observability foundations, and cost optimization strategies will build directly on the practices established here.

- **Section length:** 60 words

## Article code

Links to code that will be used to support the article. Always prioritize this code over every other piece of code found in the sources: 

- [Notebook 1](https://github.com/towardsai/agentic-ai-engineering-course/blob/main/lessons/31_continuous_integration/notebook.ipynb)

## Golden Sources

- [pre-commit](https://pre-commit.com/)
- [Ruff Linter](https://docs.astral.sh/ruff/linter/)
- [Ruff pre-commit](https://github.com/astral-sh/ruff-pre-commit)
- [Ruff Docs](https://docs.astral.sh/ruff/)
- [Integration with GitHub Actions, uv docs](https://docs.astral.sh/uv/guides/integration/github/)
- [Integration with pre-commit, uv docs](https://docs.astral.sh/uv/guides/integration/pre-commit/)
- [GitHub Actions documentation](https://docs.github.com/en/actions)
- [LLM evaluation for CI/CD pipelines](https://www.deepchecks.com/llm-evaluation/ci-cd-pipelines/)
- [Testing](https://docs.langchain.com/oss/python/langchain/test)

## Other Sources

- [pyproject.toml explained](https://betterstack.com/community/guides/scaling-python/pyproject-explained/)
- [Unit testing best practices: 13 ways to improve your tests](https://brightsec.com/blog/unit-testing-best-practices/)
- [How to run jobs in parallel with GitHub Actions](https://dev.to/cicube/how-to-run-jobs-in-parallel-with-github-actions-4png)
- [A practical guide to integrating AI evals into your CI/CD pipeline](https://dev.to/kuldeep_paul/a-practical-guide-to-integrating-ai-evals-into-your-cicd-pipeline-3mlb)
- [pytest documentation](https://docs.pytest.org/)
- [Why Python developers should switch to uv](https://devcenter.upsun.com/posts/why-python-developers-should-switch-to-uv/)