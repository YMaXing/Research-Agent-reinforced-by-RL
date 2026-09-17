# Research

<research_source type="tavily_results" phase="exploitation">
## Research Results

<details>
<summary>How does non-determinism impact CI for AI agents?</summary>

Phase: [EXPLOITATION]

### Source [1]: https://galileo.ai/blog/continuous-integration-ci-ai-fundamentals

Query: How does non-determinism impact CI for AI agents?

Answer: Continuous integration for AI extends traditional build-test-deploy automation to include model evals, data validation, and behavioral regression testing for non-deterministic systems. Where traditional software CI verifies that code compiles and functions return expected outputs, CI for AI verifies that your autonomous agents behave reliably, that they select the right tools, reason coherently, follow instructions, and avoid hallucinating. Autonomous agents make thousands of decisions daily, and a single prompt change can cascade failures across tool selection, reasoning chains, and output quality. CI pipelines built for deterministic software assume that the same input produces the same output, that tests can assert exact matches, and that a passing build means a working system. Autonomous agents violate every one of those assumptions. They produce non-deterministic outputs, evolve with data, and fail in ways that unit tests structurally cannot detect. You can adapt continuous integration fundamentals for AI agent development, build eval-driven pipelines that catch behavioral regressions before they reach production, and extend those evals into runtime safeguards that protect your production traffic continuously.

-----

Phase: [EXPLOITATION]

### Source [2]: https://www.guild.ai/glossary/non-deterministic-systems

Query: How does non-determinism impact CI for AI agents?

Answer: Non-determinism isn't a bug — it's a fundamental property of the systems engineering teams are now building on. The dual nature of non-determinism in generative AI unleashes creativity and adaptability in complex environments while navigating the challenges of unpredictability and consistency. For engineering teams deploying AI agents, non-determinism touches every operational concern. Consider a code review agent triggered on pull requests. Run it twice on the same diff, and it might flag different issues, suggest different refactors, or phrase feedback differently. The reviews might both be valid — but your CI pipeline needs to produce consistent pass/fail signals. Traditional QA assumes deterministic behavior. Traditional quality assurance assumes deterministic behavior — given input X, you always get output Y. That model breaks completely with AI agents. With the shift to LLM-first AI agents, that predictability disappears. Large Language Models introduce non-determinism, meaning the same input can generate an infinite number of responses, many of which could be valid (even with temperature set to 0). This makes AI agents far more natural and capable — but it also breaks the assumptions that traditional testing and evaluation rely on. Research published on arXiv quantified this directly: they demonstrated an alarming degree of variation across equivalent input runs with a varied collection of high performing LLMs under presumed deterministic settings.

-----

Phase: [EXPLOITATION]

### Source [3]: https://cycode.com/blog/deterministic-vs-non-deterministic-vs-probabilistic-ai-appsec

Query: How does non-determinism impact CI for AI agents?

Answer: When an AI agent generates code and another AI agent scans it, and both are non-deterministic, there is no human checkpoint that reliably catches the variance. For teams building or adopting agentic development workflows, the question is no longer just “can I audit my scan results?” It is “can I trust that my AI agents enforce consistent security behavior across thousands of automated decisions per day?” The answer requires deterministic foundations at the enforcement layer, regardless of how much non-deterministic reasoning is happening above it. Finding a vulnerability once is a demo. Finding it every single time, on every run, with the same confidence score, is a security control. An AI agent that makes different decisions on the same codebase on different runs is not just inconsistent. In a security context, it is a liability. Three concepts define this behavioral question: deterministic AI, non-deterministic AI, and probabilistic AI. They define what you can audit, what you can prove in a compliance review, and what posture your AI agents hold when they operate without a human in the loop.

-----

Phase: [EXPLOITATION]

### Source [4]: https://www.youtube.com/watch?v=4u64WEuQHYE&vl=en

Query: How does non-determinism impact CI for AI agents?

Answer: Non-determinism means that each AI generation can produce slightly different results, such as different wording of a sentence or different pixels in a generated image. In highly regulated industries this is particularly challenging as AI models must be explainable, and organizations must be able to prove their outputs are correct. Nobody wants “hallucination” in a banking or payments transaction. Non-determinism doesn't mean we can't use it for real software. It just means we need to think about some unique things when we're designing our applications and our AI agents. The solution to that is something that we've actually talked about before in last season. It's evaluation. AI agents have tools and more complex prompting techniques. There are special evaluation techniques that can help us here. We're going to start with one simple one, which is adding evaluation to every step of an agentic flow.

-----

Phase: [EXPLOITATION]

### Source [5]: https://codenotary.com/blog/the-double-edged-sword-ais-non-determinism-in-software-and-it

Query: How does non-determinism impact CI for AI agents?

Answer: This non-deterministic behavior impacts incident response and troubleshooting. For instance, an AI might recommend restarting a service one time and then, with the exact same input later, suggest a database optimization. This creates confusion and erodes trust in the AI's recommendations, forcing IT professionals to independently verify every suggestion. Another example could be an AI-driven automation script that, given the same trigger conditions, occasionally executes a different set of actions or produces slightly varied configuration changes. This unpredictability makes it incredibly difficult to implement robust automation and ensure system stability, as the "known good" state becomes elusive.

-----

</details>

<details>
<summary>How does the FakeModel pattern mock LLM responses?</summary>

Phase: [EXPLOITATION]

### Source [9]: https://agiflow.io/blog/effective-practices-for-mocking-llm-responses-during-the-software-development-lifecycle

Query: How does the FakeModel pattern mock LLM responses?

Answer: The FakeModel pattern mocks LLM responses by using predefined or custom responses to simulate LLM behavior during testing. It avoids live API calls, ensuring consistent test results. This method is useful for unit testing and integration testing. Technique 1: Mock at the Library Layer. The simplest approach is to replace the LLM client with a fake object inside your test. LangChain ships a `FakeListLLM` that returns responses from a predefined list in sequence: from langchain.llms.fake import FakeListLLM responses = ["The capital of France is Paris.", "I don't know."] llm = FakeListLLM(responses=responses) result = llm.invoke("What is the capital of France?") assert result == "The capital of France is Paris." For TypeScript/JavaScript with Jest or Vitest, you mock the OpenAI or LangChain client module directly. Parameterized Edge Cases with Faker: For testing how your application handles the variety of real LLM outputs — verbose responses, terse responses, JSON with missing fields, responses in unexpected languages — parameterized mocks with a fake data library give you breadth without recording hundreds of cassettes.

-----

Phase: [EXPLOITATION]

### Source [10]: https://home.mlops.community/public/blogs/effective-practices-for-mocking-llm-responses-during-the-software-development-lifecycle

Query: How does the FakeModel pattern mock LLM responses?

Answer: Mocking LLM responses is often ineffective due to the inherent non-deterministic nature of these models. Unlike traditional software systems that produce consistent outputs for given inputs, LLMs can generate a wide range of responses, even when queried with the same prompt. This variability poses significant challenges for mocking methods, which typically rely on predictable and repeatable outputs. Non-Deterministic Outputs: LLMs generate responses based on probability distributions, which means the same input can yield different outputs each time. Mocking these responses would fail to capture the full spectrum of potential behaviors, leading to an inaccurate representation of the model’s capabilities and limitations. Create Mock Data: Generating a comprehensive set of mock responses for your LLM is essential to ensure thorough testing and validation of your application. These mock responses should cover a wide range of scenarios, including both typical interactions and edge cases. This approach guarantees that your application can handle various situations effectively. You can use a fixed set of responses, record real API calls, or leverage libraries like faker to introduce randomization. Example A: Generating a Fixed Set of Mock Data Using a fixed set of responses allows for consistent and repeatable testing. Simply use a dictionary or list to store response, and select the corresponding item based on request.

-----

Phase: [EXPLOITATION]

### Source [11]: https://langchain-contrib.readthedocs.io/en/latest/llms/fake.html

Query: How does the FakeModel pattern mock LLM responses?

Answer: This fake LLM can be useful for mocking LLM calls during testing. It’s extended from langchain’s own `FakeLLM`, but that one is not available for use outside of the langchain project. Custom responses: You can specify custom responses for exact prompt matches by specifying `mapped_responses`. In practice, prompts can get really complicated really fast. As such, you can also specify responses to simply be returned in order by specifying `sequenced_responses` instead. Enforcing stops.

-----

Phase: [EXPLOITATION]

### Source [12]: https://www.iamraghuveer.com/posts/unit-testing-custom-agents

Query: How does the FakeModel pattern mock LLM responses?

Answer: Testing agents at the unit level requires separating what the agent code does — prompt construction, response parsing, business logic — from what the LLM does. The mock pattern shown here patches `anthropic.Anthropic` at the module level, controls the response via `side_effect`, and verifies prompt contents via `call_args`. This approach tests every agent in isolation, runs in under a second, and catches the parsing and validation bugs that occur most frequently in agent development without spending money on API calls. An agent has three testable layers: prompt construction, LLM call mechanics, and output parsing. The LLM itself is not testable — it is a black box that returns different outputs on different runs. The goal of the test suite is to verify that the agent code around the LLM call is correct: that the prompt includes the expected context, that the API is called with the right parameters, and that the response is parsed into a valid output schema.

-----

Phase: [EXPLOITATION]

### Source [13]: https://docs.langchain.com/oss/javascript/integrations/chat/fake

Query: How does the FakeModel pattern mock LLM responses?

Answer: LangChain provides a fake LLM chat model for testing purposes. This allows you to mock out calls to the LLM and simulate what would happen if the LLM responded in a certain way.

-----

</details>

<details>
<summary>Why run AI evals as regression tests in CI?</summary>

Phase: [EXPLOITATION]

### Source [14]: https://kinde.com/learn/ai-for-software-engineering/ai-devops/ci-cd-for-evals-running-prompt-and-agent-regression-tests-in-github-actions

Query: Why run AI evals as regression tests in CI?

Answer: CI/CD for AI evals is the practice of automatically testing your AI prompts, models, and agents within your continuous integration and continuous delivery pipeline. It extends the familiar “code, test, deploy” loop to AI development, ensuring that any change to a prompt or agent doesn’t just work, but works correctly, consistently, and within budget before it ever reaches users. Unlike traditional software testing where a function with the same input reliably produces the same output, LLM-based systems can be non-deterministic. An “eval” (evaluation) is a specialized test that assesses the quality, safety, and performance of an AI’s output, creating a critical safety net against regressions. Automated AI evaluation integrates directly into your version control system, like GitHub, and runs a series of checks whenever a developer proposes a change. By adding this workflow to your pull requests, you create a merge-blocking gate that prevents quality degradation. Integrating evals into your CI/CD pipeline shifts quality control from a manual, post-deployment headache to an automated, proactive process. It’s about building a system that self-regulates quality, performance, and cost.

-----

Phase: [EXPLOITATION]

### Source [15]: https://www.braintrust.dev/articles/best-ai-evals-tools-cicd-2025

Query: Why run AI evals as regression tests in CI?

Answer: Recent adoption trends show that organizations implementing automated LLM evals in their CI/CD pipelines catch regressions before users do and maintain higher quality standards across deployments. This approach transforms evaluation from a bottleneck into an accelerator, enabling teams to move fast while maintaining rigorous quality standards. AI evals (evaluations) in CI/CD are automated tests that measure your LLM application's quality, accuracy, and behavior with every code change. Rather than manually checking if your chatbot still gives good answers after updating a prompt, these tools automatically run dozens or hundreds of eval cases, score the outputs, and fail your build if quality drops below your thresholds. Evals for product managers are how you turn "the AI feels worse this week" into something measurable. Without them, PMs are stuck arbitrating between engineers who insist a prompt change is fine and support tickets suggesting it isn’t. With evals wired into CI/CD, every prompt tweak, model swap, or retrieval change comes with a quality delta you can actually point to.

-----

Phase: [EXPLOITATION]

### Source [16]: https://galileo.ai/blog/continuous-integration-ci-ai-fundamentals

Query: Why run AI evals as regression tests in CI?

Answer: Continuous integration for AI extends traditional build-test-deploy automation to include model evals, data validation, and behavioral regression testing for non-deterministic systems. Where traditional software CI verifies that code compiles and functions return expected outputs, CI for AI verifies that your autonomous agents behave reliably, that they select the right tools, reason coherently, follow instructions, and avoid hallucinating. Systematic evals are not just a reliability practice. When your CI pipeline catches behavioral regressions early, you can ship faster with more confidence. That shifts your engineering time away from reactive debugging and back toward building new capabilities. From a budget perspective, the ROI of eval-driven CI compounds with every deployment cycle you avoid rolling back. The eval suite checks for regressions in multi-step tool selection, reasoning coherence, and action completion across agent workflows. This process gets stronger over time when production incidents become new eval cases.

-----

Phase: [EXPLOITATION]

### Source [17]: https://testgrid.io/blog/what-is-ai-regression-testing

Query: Why run AI evals as regression tests in CI?

Answer: AI testing allows you to run only the tests that matter. Intelligent test impact analysis and change-based selection use code diffs and past failures to identify and prioritize relevant test cases. This means you don’t have to execute the entire test suite for every change. You can cut needless runs and minimize the total testing time, save compute, and speed up feedback loops. When you integrate an AI-driven regression testing tool in your CI/CD pipelines, it can detect the changes you’ve made, execute tests, and give you prompt feedback on issues. This way, you can easily identify and resolve bugs immediately and accelerate your release velocity.

-----

Phase: [EXPLOITATION]

### Source [18]: https://dev.to/kuldeep_paul/a-practical-guide-to-integrating-ai-evals-into-your-cicd-pipeline-3mlb

Query: Why run AI evals as regression tests in CI?

Answer: Engineering teams shipping AI agents and LLM applications need the same confidence they expect from mature software delivery: repeatable tests, clear quality gates, and rapid iteration with guardrails. Automating AI evaluation—“AI evals”—inside CI/CD is how you catch regressions early, prevent silent failures in production, and scale responsible development across teams. This guide distills best practices and an actionable blueprint for CI/CD-integrated evals, grounded in current research and production patterns. At its core, CI/CD-integrated evals run a representative test suite on every relevant change—prompt edits, model swaps, tool configurations, or agent logic. When practiced consistently, teams gain fast feedback loops, reduce rollout risk, and accelerate responsible iteration—all while maintaining observability and governance. Bringing these together enables “AI quality gates” that block releases on meaningful regressions across your core metrics.

-----

</details>

<details>
<summary>How to configure manual workflow_dispatch for AI evals?</summary>

Phase: [EXPLOITATION]

### Source [19]: https://graphite.com/guides/github-actions-workflow-dispatch

Query: How to configure manual workflow_dispatch for AI evals?

Answer: To configure manual workflow_dispatch for AI evaluations, add workflow_dispatch to your GitHub Actions workflow file. Use the Run workflow button on the Actions tab to trigger it manually. Input parameters can be specified during manual trigger. The workflow_dispatch event is designed for manual control, useful for tasks requiring oversight. Add it to .github/workflows directory. Example: name: Manual Workflow on: workflow_dispatch: jobs: example_job: runs-on: ubuntu-latest steps: - name: Checkout code. Use descriptive names for inputs, secure sensitive data with secrets, validate inputs. It enables manual triggers with custom inputs for robust management.

-----

Phase: [EXPLOITATION]

### Source [20]: https://docs.github.com/actions/managing-workflow-runs/manually-running-a-workflow

Query: How to configure manual workflow_dispatch for AI evals?

Answer: To trigger workflow_dispatch, workflow must be in default branch. Write access required. Steps: Navigate to repo, click Actions, select workflow, click Run workflow button (only if workflow_dispatch configured). Select branch, fill inputs if required, click Run workflow. Can also use GitHub CLI or REST API. Configuring: workflow must use workflow_dispatch event.

-----

Phase: [EXPLOITATION]

### Source [21]: https://learn.microsoft.com/en-us/azure/foundry/how-to/evaluation-github-action

Query: How to configure manual workflow_dispatch for AI evals?

Answer: Example workflow for AI Agent Evaluation: name: "AI Agent Evaluation" on: workflow_dispatch: push: branches: - main permissions: id-token: write contents: read jobs: run-action: runs-on: ubuntu-latest steps: - name: Checkout uses: actions/checkout@v4 - name: Azure login using Federated Credentials uses: azure/login@v2 with: client-id etc. - name: Run Evaluation uses: microsoft/ai-agent-evals@v3-beta with: azure-ai-project-endpoint, deployment-name, agent-ids, data-path. Tip: minimize costs by not running on every commit. Useful for comparing agents by IDs.

-----

</details>

<details>
<summary>What are pre-commit hooks as automated local guardrails?</summary>

Phase: [EXPLOITATION]

### Source [22]: https://blog.gitguardian.com/automated-guard-rails-for-vibe-coding

Query: What are pre-commit hooks as automated local guardrails?

Answer: Pre-commit hooks are automated checks that run locally on your machine before code enters the repository. They enforce deterministic security validation through pre-commit hooks, CI pipelines, and integrated security scanning tools. These controls ensure that all code—whether human- or AI-generated—undergoes rigorous checks for secrets, code quality, test coverage, and known vulnerability patterns before being merged or released. Automated guardrails enforce deterministic security validation, providing binary, auditable assurances that critical requirements are met. They are configured via .pre-commit-config.yaml which defines hooks including GitGuardian, Black, Flake8, and pytest using the pre-commit framework.

-----

Phase: [EXPLOITATION]

### Source [23]: https://blog.gitguardian.com/local-guardrails-for-secrets-security

Query: What are pre-commit hooks as automated local guardrails?

Answer: Git hooks add another layer of protection. Using ggshield pre-commit hooks means a scan runs before Git creates a commit. Teams can configure it through the pre-commit framework, install it locally for specific repositories, or install it globally across current and future repositories on a developer workstation. The global option is important for broader default protection. A pre-push hook catches a later moment before code leaves the machine for a remote repository. Together, pre-commit and pre-push hooks create two useful gates: one before local history becomes durable, and one before code reaches shared infrastructure. ggshield is the GitGuardian command-line interface for scanning developer workflows locally or in CI, detecting hardcoded credentials.

-----

Phase: [EXPLOITATION]

### Source [24]: https://github.com/pre-commit/pre-commit-hooks

Query: What are pre-commit hooks as automated local guardrails?

Answer: Provides out-of-the-box hooks for pre-commit such as forbid-new-submodules, forbid-submodules, mixed-line-ending, name-tests-test, no-commit-to-branch, check-case-conflict, check-executables-have-shebangs, check-illegal-windows-names, check-json, check-merge-conflict, check-shebang-scripts-are-executable, check-symlinks, check-toml, check-vcs-permalinks, check-xml, check-yaml, debug-statements.

-----

Phase: [EXPLOITATION]

### Source [25]: https://pre-commit.com

Query: What are pre-commit hooks as automated local guardrails?

Answer: pre-commit is a framework for managing and maintaining multi-language pre-commit hooks. Git hook scripts are useful for identifying simple issues before submission to code review. Hooks run on every commit to automatically point out issues in code such as missing semicolons, trailing whitespace, and debug statements. By pointing these issues out before code review, this allows a code reviewer to focus on the architecture of a change. Repository-local hooks are useful when scripts are tightly coupled to the repository. Local hooks can use any language which supports additional_dependencies or docker_image / fail / pygrep / unsupported / unsupported_script.

-----

Phase: [EXPLOITATION]

### Source [26]: https://www.atlassian.com/git/tutorials/git-hooks

Query: What are pre-commit hooks as automated local guardrails?

Answer: The pre-commit hook is executed every time you run git commit before Git asks the developer for a commit message or generates a commit object. You can use this hook to inspect the snapshot that is about to be committed. For example, you may want to run some automated tests that make sure the commit doesn’t break any existing functionality. It can use existing Git commands to run tests on the changes introduced by the proposed commit, but you can do anything you want in pre-commit including executing other scripts, running a 3rd-party test suite, or checking code style with Lint. Local hooks affect only the repository in which they reside.

-----

</details>

<details>
<summary>How does Ruff replace Black isort and Flake8?</summary>

Phase: [EXPLOITATION]

### Source [27]: https://docs.astral.sh/ruff/faq

Query: How does Ruff replace Black isort and Flake8?

Answer: Ruff replaces Flake8, Black, and isort by providing complete Flake8 compatibility, Black's formatting, and isort's import sorting, all in a single, faster tool. Ruff can be used to replace Flake8 when used with any of the following plugins. Ruff can also replace Black, isort, yesqa, eradicate, and most of the rules implemented in pyupgrade. Ruff's linter and formatter can be used independently of one another. Ruff can be used as a drop-in replacement for Flake8 when used (1) without or with a small number of plugins, (2) alongside Black, and (3) on Python 3 code. Under those conditions, Ruff implements every rule in Flake8. In practice, that means Ruff implements all of the F rules (which originate from Pyflakes), along with a subset of the E and W rules (which originate from pycodestyle). Ruff also re-implements some of the most popular Flake8 plugins and related code quality tools natively. The formatter is intended to emit near-identical output when run over Black-formatted code. When run over extensive Black-formatted projects like Django and Zulip, > 99.9% of lines are formatted identically. When migrating an existing project from Black to Ruff, you should expect to see a few differences on the margins, but the vast majority of your code should be unchanged. When run over non-Black-formatted code, the formatter makes some different decisions than Black, and so more deviations should be expected, especially around the treatment of end-of-line comments.

-----

Phase: [EXPLOITATION]

### Source [28]: https://docs.astral.sh/ruff

Query: How does Ruff replace Black isort and Flake8?

Answer: Ruff aims to be orders of magnitude faster than alternative tools while integrating more functionality behind a single, common interface. Ruff can be used to replace Flake8 (plus dozens of plugins), Black, isort, pydocstyle, pyupgrade, autoflake, and more, all while executing tens or hundreds of times faster than any individual tool.

-----

Phase: [EXPLOITATION]

### Source [29]: https://github.com/astral-sh/ruff

Query: How does Ruff replace Black isort and Flake8?

Answer: Ruff aims to be orders of magnitude faster than alternative tools while integrating more functionality behind a single, common interface. Ruff can be used to replace Flake8 (plus dozens of plugins), Black, isort, pydocstyle, pyupgrade, autoflake, and more, all while executing tens or hundreds of times faster than any individual tool. Ruff supports over 900 lint rules, many of which are inspired by popular tools like Flake8, isort, pyupgrade, and others. Regardless of the rule's origin, Ruff re-implements every rule in Rust as a first-party feature. By default, Ruff enables Flake8's F rules, along with a subset of the E rules, omitting any stylistic rules that overlap with the use of a formatter, like ruff format or Black. Beyond the defaults, Ruff re-implements some of the most popular Flake8 plugins and related code quality tools, including.

-----

</details>

<details>
<summary>What deterministic logic do AI agent unit tests verify?</summary>

Phase: [EXPLOITATION]

### Source [30]: https://www.guild.ai/glossary/unit-testing-ai-agents

Query: What deterministic logic do AI agent unit tests verify?

Answer: Traditional unit tests verify deterministic functions where the same input always produces the same output. Agent unit testing must handle probabilistic outputs, evaluate semantic correctness rather than exact matches, and assess multi-step reasoning paths. It combines deterministic checks (schema validation, tool call format) with probabilistic evaluation (LLM-as-judge, semantic similarity scoring). Frameworks such as LangChain, AutoGen, CrewAI, and LangGraph have become instrumental in implementing robust unit testing strategies. Evaluation platforms like LangSmith, Arize Phoenix, Langfuse, and DeepEval provide infrastructure for running and scoring agent evaluations. LangChain's AgentEvals library offers pre-built trajectory evaluators for comparing agent execution paths. [...] ### Testing a Code Review Agent

A code review agent needs tests at multiple levels. Deterministic checks verify it outputs valid review comments in the expected format. Semantic evaluation (using LLM-as-judge) verifies the comments are relevant to the actual code changes. For a more complex multi-turn eval, a coding agent receives tools, a task, and an environment, executes an "agent loop" (tool calls and reasoning), and updates the environment with the implementation. Grading then uses unit tests to verify the working output.

### Testing a Customer Service Agent [...] For a code review agent, this means writing separate tests for: does the prompt correctly identify a security vulnerability when given a known-vulnerable code snippet? Does the tool selector route to the correct linter for Python vs. TypeScript? Does the memory module recall the repository's coding conventions from prior runs?

### Deterministic vs. Probabilistic Assertions

Traditional unit tests use exact-match assertions: `assertEqual(expected, actual)`. Agent unit tests require a layered approach. Deterministic checks handle the parts you can pin down — JSON schema validation, tool call parameter formats, token count limits. Probabilistic evaluation handles the rest.

-----

Phase: [EXPLOITATION]

### Source [31]: https://oneuptime.com/blog/post/2026-01-30-agent-testing/view

Query: What deterministic logic do AI agent unit tests verify?

Answer: Best Practices Summary

| Practice | Why It Matters |
 --- |
| Mock at boundaries | Test agent logic, not LLM APIs |
| Use response sequences | Create deterministic multi-turn tests |
| Test error paths | Agents must recover gracefully |
| Record regression cases | Capture known-good behaviors |
| Run safety tests | Catch harmful outputs early |
| Track metrics over time | Detect quality degradation |
| Parallelize CI stages | Fast feedback on changes |

## Summary

Testing AI agents requires a layered approach:

The key insight is that agent tests should be deterministic by mocking the LLM layer while testing everything else with real implementations. This gives you confidence that your agent logic is correct without the flakiness of actual LLM calls.

-----

Phase: [EXPLOITATION]

### Source [32]: https://datagrid.com/blog/4-frameworks-test-non-deterministic-ai-agents

Query: What deterministic logic do AI agent unit tests verify?

Answer: Conventional QA is built on predictability. Unit tests verify expected outputs, integration tests confirm components interact correctly, and regression tests ensure updates don't break functionality.

Agents operate differently; they produce variable, contextual responses based on probabilistic reasoning. The same input might yield different outputs depending on context, conversation history, or model state.

This fundamental mismatch invalidates traditional testing approaches in four ways.

Dynamic Learning Invalidates Static Tests: AI agents evolve without code changes. Traditional regression testing assumes constant behavior, penalizing agent improvement. [...] In turn, these processes help CTOs efficiently project deployment timelines and plan risk mitigation strategies.

Testing frameworks designed for AI agents address these challenges through five key shifts:

Embrace probabilistic validation instead of exact output matching

Monitor behavior over time rather than single-point verification

Measure behavioral bounds instead of deterministic correctness

Incorporate human judgment where automated testing reaches its limits

Validate reasoning processes alongside functional outcomes

## Framework #1: Simulation-Based Testing

Simulation-based testing validates agent behavior in synthetic environments before production deployment, exposing agents to edge cases systematically rather than discovering failures in production. [...] Context Sensitivity Beyond Integration Testing: Agent performance depends on real-time data and environmental state. Traditional integration tests can't capture infinite contextual variations.

Non-Determinism Breaks Output Validation: AI agents produce probabilistic outputs. Unit tests rely on exact matching, but agents operate in probability spaces where you can't assert equality.

Explainability and Ethical Operation: AI agents require validation for bias and transparency. Traditional QA focuses on "does it work?" not "should it work this way?"

## Why Agent Testing Frameworks Matter for Architecture Teams

-----

Phase: [EXPLOITATION]

### Source [33]: https://arxiv.org/html/2509.19185v1

Query: What deterministic logic do AI agent unit tests verify?

Answer: To illustrate how practitioners set up a test function and verify the output of the SUT, we present a sample unit test function in Figure 2 that validates the behavior of the oas3\_openai\_text\_to\_embedding function. This function internally interacts with the OpenAI API, and the test isolates it by mocking external dependencies. Specifically, the test uses the patching technique to intercept and override the behavior of the aiohttp.ClientSession.post method (lines 3-4). The mocked response is configured to return a predefined JSON payload, simulating a successful API call (lines 5-8). This setup phase demonstrates two common structural patterns, i.e., Mocking and Patching to handle the dependencies. Additionally, the test includes verification logic that checks both the existence and [...] verification logic that checks both the existence and structure of the returned embedding (lines 14-17). These lines reflect a combination of basic presence assertions (e.g., assert result) and threshold assertions (e.g., assert len(result.data.embedding) > 0), which are often used to confirm the correctness and completeness of test outputs. [...] Findings: We identify 13 canonical components that receive unit-testing attention in agent frameworks and agentic applications. First, we observe a strategic inversion of testing efforts in agent frameworks and agentic applications compared to traditional ML applications: instead of focusing on the model itself, developers concentrate on deterministic infrastructure such as Resource Artifacts (tools, parsers), which account for 29.7% of tests in frameworks and 40.1% in applications. Second, we identify a critical testing blind spot: the Trigger component (prompts) is dangerously under-tested, appearing in around 1% of test functions, which can introduce significant risks of silent failures and performance degradation as the underlying foundation models evolve.

-----

Phase: [EXPLOITATION]

### Source [34]: https://galileo.ai/blog/unit-testing-ai-systems

Query: What deterministic logic do AI agent unit tests verify?

Answer: Connect rule tests to audit logging by verifying expected log entries exist after each assertion, enabling compliance officers to trace decisions without manual investigation.

### Test Integration and API Response Reliability

Perfect internal logic can still fail once it crosses service boundaries. Downstream consumers expect stable latency, proper status codes, and graceful degradation during failures. Integration tests should exercise the complete API surface under realistic load conditions. [...] For calculations that follow known laws—say, min-max scaling or log inverses—verify invariants: applying a transform and its inverse should reproduce the original value within tolerance. Property-based frameworks excel in this area, generating random numeric arrays to stress test rounding thresholds and overflow boundaries.

How do you handle missing values, outliers, and categorical unknowns? Tests should confirm that imputation strategies leave statistical moments unchanged and that unseen categories fall into a safe "other" bucket rather than crashing the pipeline. [...] Contract tests spin up mock consumers, issue requests, and validate both payload structure and HTTP headers. Simulate 4xx and 5xx scenarios to ensure services return actionable error messages rather than raw stack traces. Performance testing matters too—saturate APIs with concurrency levels matching peak traffic and alert when p95 latency exceeds agreed budgets.

Resilience testing validates real-world failure scenarios. Chaos engineering techniques—network throttling, container restarts, dependency timeouts—prove that retry logic and idempotency guarantees work correctly.

-----

</details>

<details>
<summary>What is the full GitHub Actions CI YAML for Brown?</summary>

Phase: [EXPLOITATION]

### Source [35]: https://intersect-training.org/CI-CD/yaml-and-github-actions.html

Query: What is the full GitHub Actions CI YAML for Brown?

Answer: The GitHub Actions configurations are specified using YAML files stored in the .github/workflows/ directory. A basic example is provided with structure including name, on, jobs, job_1 with runs-on and steps. Reference guide at workflow-syntax-for-github-actions. Example YAML: name: example on: push jobs: job_1: runs-on: ubuntu-latest steps: - name: My first step run: echo This is the first step of my first job.

-----

Phase: [EXPLOITATION]

### Source [36]: https://docs.github.com/actions/get-started/quickstart

Query: What is the full GitHub Actions CI YAML for Brown?

Answer: GitHub Actions is a CI/CD platform. Workflow files use .yml or .yaml extension in .github/workflows/. Provides workflow templates for CI, Deployments, etc. Example YAML contents for github-actions-demo.yml file mentioned but not fully detailed in snippet.

-----

Phase: [EXPLOITATION]

### Source [37]: https://medium.com/@donovan.brown_75022/week-8-diving-into-ci-cd-github-actions-and-a-little-lambda-magic-997cf8a1e193

Query: What is the full GitHub Actions CI YAML for Brown?

Answer: GitHub Actions uses YAML workflows that react to events like pushes, pull requests. Components: Triggers, Jobs, Steps, Runners, Actions. Example of workflow for deploying to AWS Lambda on push to Lambda function’s folder.

-----

Phase: [EXPLOITATION]

### Source [38]: https://github.com/readme/guides/sothebys-github-actions

Query: What is the full GitHub Actions CI YAML for Brown?

Answer: Workflows defined in YAML files in .github/workflows/. Example workflow 'Animal Farm Node.js CI' triggered on push and pull request to main branch. Includes jobs for cloning, installing, running tests. Uses secrets for credentials.

-----

</details>

<details>
<summary>What does the daily AI agent CI workflow include?</summary>

Phase: [EXPLOITATION]

### Source [39]: https://galileo.ai/blog/continuous-integration-ci-ai-fundamentals

Query: What does the daily AI agent CI workflow include?

Answer: Continuous integration for AI extends traditional build-test-deploy automation to include model evals, data validation, and behavioral regression testing for non-deterministic systems. CI for AI verifies that autonomous agents behave reliably, that they select the right tools, reason coherently, follow instructions, and avoid hallucinating. Build CI around behavior not just builds: treat behavior as the release artifact, not just code. Version prompts and datasets alongside code, replace brittle unit tests with eval-driven gates, track drift before it becomes a customer problem, and extend successful offline checks into production safeguards. Need agent observability to see how changes affect real workflows.

-----

Phase: [EXPLOITATION]

### Source [42]: https://developers.redhat.com/articles/2026/05/18/ci-cd-delivery-agentic-ai

Query: What does the daily AI agent CI workflow include?

Answer: Supports post-run audit and evaluation. Export conversations from API, pass into DeepEval evaluation pipeline. Extend nightly CI/CD with scheduled workflow pulling random sample of previous day's conversations and evaluating them for daily signal on agent performance with real users. Running basic evaluations using DeepEval to validate predefined conversations and one generated conversation. Nightly CI/CD approach for production deployment.

-----

</details>

<details>
<summary>What is standard CI practice for frequent merges and automated checks?</summary>

Phase: [EXPLOITATION]

### Source [43]: https://www.atlassian.com/continuous-delivery/continuous-integration

Query: What is standard CI practice for frequent merges and automated checks?

Answer: Continuous integration (CI) is the practice of automating the integration of code changes from multiple contributors into a single software project. It’s a primary DevOps best practice, allowing developers to frequently merge code changes into a central repository where builds and tests then run. Automated tools are used to assert the new code’s correctness before integration. Trunk-based development is a version control management practice where developers merge small, frequent updates to a core “trunk” or main branch. Without CI, developers must manually coordinate and communicate when they are contributing code to the end product. After version control has been established on the project, integration approval steps should be added. The most valuable integration approval step to have in place is automated tests. Adding automated tests to a project can have an initial cost overhead. A testing framework has to be installed, then test code and test cases must be written by developers. Some ideas for other, less expensive CI approval mechanisms to add are syntax checkers, code style formatters, or dependency vulnerability scans. Once you have a version control system setup with some merge approval steps in place, you’ve established continuous integration!

-----

Phase: [EXPLOITATION]

### Source [44]: https://octopus.com/devops/ci-cd

Query: What is standard CI practice for frequent merges and automated checks?

Answer: CI/CD, or Continuous Integration/Continuous Delivery, is a software development practice that automates the process of building, testing, and deploying code. It’s a key part of the DevOps toolchain. Continuous Integration (CI): Developers merge code changes into a central repository as often as possible. This practice helps reduce testing costs and the number of bugs that get shipped to production. In a CI process, a build server is responsible for taking new code changes, running automated tests using multiple tools, integrating the code into the master branch, and generating a build—a new version of software artifacts needed to deploy the software. CI greatly improves the quality and speed of software development. Teams can create more features that provide value to users, and many organizations now release software every week, every day, or multiple times a day.

-----

Phase: [EXPLOITATION]

### Source [45]: https://gatling.io/blog/ci-cd-best-practices

Query: What is standard CI practice for frequent merges and automated checks?

Answer: Using the CI approach, developers frequently integrate code into a shared repository. Automated tests and builds are run for the code, checking for accuracy. This process is able to catch bugs early, allowing developers to make small code changes when necessary. Because of such frequent automated testing, the pipeline gives quick feedback to developers, and they can immediately make the necessary changes. Best practices include keeping builds fast, using version control, automating tests, committing small changes frequently, and monitoring pipelines and apps. These ensure efficiency, reliability, and quick feedback throughout development. Quality is maintained with automated unit, integration, and end-to-end tests, static code analysis, peer reviews, regression testing, and tracking metrics like coverage. This prevents defects and ensures stable releases.

-----

Phase: [EXPLOITATION]

### Source [46]: https://www.ibm.com/think/topics/continuous-integration

Query: What is standard CI practice for frequent merges and automated checks?

Answer: Continuous integration is an inherently agile practice. Continuous integration helps development teams iterate faster and deliver better software to users, but there are additional steps a business can take to optimize the process. Commonly implemented CI practices include: frequent, incremental code updates and continuous code validation. Continuous integration refers to the frequent code merges and the builds and unit tests that follow. For instance, the use of artificial intelligence (AI) and machine learning (ML) in continuous integration processes is becoming standard development practice. AI-enabled tools can help developers create self-healing systems that automatically and autonomously identify and correct problematic code before it affects the main development stream. ML-driven CI systems can also autogenerate tailored test cases based on code submissions and modifications, so developers spend less time manually creating code tests.

-----

Phase: [EXPLOITATION]

### Source [47]: https://www.sunnydata.ai/blog/cicd-best-practices-data-projects-validation-testing

Query: What is standard CI practice for frequent merges and automated checks?

Answer: It’s not enough to detect errors you also need to notify the team when something goes wrong. That’s why automated alerts are essential. If a validation fails, the pipeline should send a message to a channel like Slack or Teams. For Slack, this is done using an Incoming Webhook. You generate a URL from Slack, store it as a GitHub Secret, and send a message from the pipeline only when something fails. CI/CD is often described as the process that automates the deployment. It includes actions like testing, building, and deploying, but sometimes those steps are not enough. A pipeline can be completed successfully while still deploying something that's not working as intended.

-----

</details>

<details>
<summary>What decision framework guides AI eval frequency by project maturity?</summary>

Phase: [EXPLOITATION]

### Source [48]: https://www.ness.com/blog/ai-maturity-assessment-framework

Query: What decision framework guides AI eval frequency by project maturity?

Answer: AI evaluation frequency depends on project maturity, guided by frameworks like MITRE's and Info-Tech's, focusing on strategic alignment and governance. Higher maturity projects require more frequent assessments. Frameworks such as OWASP AIMA, Gartner AI Maturity Model, MITRE AI Maturity Framework, and MIT CISR are compared. MITRE provides capability-driven evaluation for government and mission-critical environments. Core domains include Strategy and Leadership, Data Foundations, and Technology and Infrastructure. A 7-step process for AI maturity assessment starts with Scope and Stakeholder Alignment.

-----

Phase: [EXPLOITATION]

### Source [49]: https://www.mitre.org/news-insights/publication/mitre-ai-maturity-model-and-organizational-assessment-tool-guide

Query: What decision framework guides AI eval frequency by project maturity?

Answer: The MITRE AI Maturity Model uses pillars, readiness levels, and 20 dimensions for qualitative evaluation of AI adoption maturity. Advancement depends on achieving benchmarks at previous levels. Target maturity level is based on mission and business practices, not all organizations need level 5 for all pillars.

-----

Phase: [EXPLOITATION]

### Source [50]: https://www.infotech.com/research/ss/assess-your-ai-maturity

Query: What decision framework guides AI eval frequency by project maturity?

Answer: Info-Tech Research Group's AI maturity framework assesses across five dimensions: AI Governance, Data Management, People, Process, and Technology. It provides a structured framework and tool for assessment to set achievable AI goals, addressing complications like lack of formal assessment methods and cross-functional alignment.

-----

Phase: [EXPLOITATION]

### Source [51]: https://sema4.ai/blog/ai-maturity-model-2026

Query: What decision framework guides AI eval frequency by project maturity?

Answer: AI maturity model has 5 pillars: Strategy & alignment, and others. 5 stages from Ad hoc to higher maturity. Benchmarking involves evaluating across pillars using low/medium/high framework.

-----

Phase: [EXPLOITATION]

### Source [52]: https://owasp.org/www-project-ai-maturity-assessment

Query: What decision framework guides AI eval frequency by project maturity?

Answer: OWASP AI Maturity Assessment (AIMA) provides a framework across five core domains: Strategy, Design, Implementation, Operations, and Governance, with actionable maturity levels to guide adoption and improvement.

-----

</details>

</research_source>

<research_source type="tavily_results" phase="exploration">
## Research Results

<details>
<summary>What failure modes emerge scaling three-tier AI CI at enterprise scale?</summary>

Phase: [EXPLORATION]

### Source [53]: https://www.alation.com/blog/why-enterprise-ai-projects-fail

Query: What failure modes emerge scaling three-tier AI CI at enterprise scale?

Answer: Common failure modes include inadequate data management, lack of model ownership, and insufficient integration with existing systems. These issues hinder scaling of three-tier AI CI at enterprise scale. All six of these failure modes share the same root assumption: that AI is something you build once and ship. It isn't. The organizations making real progress at enterprise scale have internalized a different model. They treat data products as living infrastructure, context as a system that must improve from use, and agents as specialists that require ongoing evaluation and tuning. The instinctive response is to assign someone to keep the context current: catch the drift, update the definition, re-deploy, repeat. That approach breaks at the second use case. By the time you've deployed five AI applications without automated context management, you've effectively created a new department whose only job is keeping yesterday's AI accurate enough to use today. Scale becomes impossible before it begins. There is also a subtler problem: A context layer built in a conference room and handed to agents as a finished product will always be incomplete. The gaps only show up in production, when real queries expose definitions that seemed clear in a document but fall apart under actual use. Failure #3: Deploying generic agents where specialists are required. The past two years have brought a wave of general-purpose AI agents marketed as enterprise-ready. The pitch is seductive: plug it in, zero configuration required, and watch it work. The problem is that no out-of-the-box agent ships with knowledge of your fiscal year definition, your trust hierarchy for competing data sources, or the filtering conventions your analysts have spent years refining.

-----

Phase: [EXPLORATION]

### Source [54]: https://www.reddit.com/r/AI_Agents/comments/1s02oaq/enterprise_ai_has_an_80_failure_rate_the_models

Query: What failure modes emerge scaling three-tier AI CI at enterprise scale?

Answer: Common failure modes include inadequate data management, lack of model ownership, and insufficient integration with existing systems. These issues hinder scaling of three-tier AI CI at enterprise scale. A few questions that came out of applying it: 1. The Walk-to-Run transition. Is that a gradual dial (routine operations go autonomous first, novel ones keep human gates) or more of a cliff edge where the org either trusts the architecture or doesn't? Does the trust gap look different for write capable agents vs read only systems? 2. The AIL. In practice, building that layer is a significant engineering effort. Data definition store, structured hub, vector store, permission scoping, automated maintenance. Have you seen anyone actually stand one up end-to-end? Not the vector store part (that's the easy bit). The automated maintenance, the freshness tracking, the permission model. Or is the "10th agent is configuration" state still ahead of where implementations currently are? The gap isn’t just infra or org — it’s that we don’t have a clean way to control and verify side effects yet. The "propose enforce verify" framing is sharp. I’ve seen teams nail the enforcement layer with API gateways, permission boundaries, that kind of thing. But the full loop? Propose, enforce, AND verify the resulting state? That’s where it gets murky. Have you seen anyone actually build all three layers into a working system at scale, or are most teams still improvising on at least one of them? 3. Beyond the whitepaper. Do you have any reference implementations, starter code, or tooling recommendations for actually building toward this? Or is it all custom built at this point? The principles are clear but the "how do you actually start implementing this in an enterprise" question is where I keep getting stuck. Are there specific packages, platforms, or patterns you’ve seen teams use as a foundation? 4. The anti-patterns as diagnostics. Do most orgs exhibit the same failure modes, or is it industry-specific? I found the orchestrator avoids operational anti-patterns (lean agents, structured logging, self-healing) but exhibits strategic ones (Disposable Agent, partial Oracle). Curious whether that pattern is common.

-----

Phase: [EXPLORATION]

### Source [55]: https://writer.com/blog/four-ai-failure-modes

Query: What failure modes emerge scaling three-tier AI CI at enterprise scale?

Answer: Common failure modes include inadequate data management, lack of model ownership, and insufficient integration with existing systems. These issues hinder scaling of three-tier AI CI at enterprise scale. McKinsey reports that 88% of companies now use AI regularly. That’s nearly universal adoption — at least on paper. But when you dig deeper, a different picture emerges: only 21% of AI projects reach production scale with measurable returns. That means 79% of AI initiatives are stuck somewhere between pilot and production, burning budget and credibility without delivering business value. This isn’t a technology problem. The models work. The capabilities are real. The bottleneck is operational — and it shows up in four distinct failure modes that most teams don’t recognize until they’re 18 months deep in pilot purgatory. The scaling crisis: When adoption doesn’t equal transformation. The statistics tell a story of widespread experimentation but limited transformation. The AI adoption gap is real. McKinsey reports 88% of companies now use AI regularly, yet only 21% reach production scale with measurable returns—leaving 79% of initiatives burning budget without delivering business value. Four distinct failure modes derail most AI projects. Teams encounter scaling hurdles when pilots rely on manual workarounds, data readiness issues when systems don’t integrate properly, security bottlenecks when IT reviews stall progress, and cultural resistance when adoption remains stubbornly low despite training. 88% of companies report regular AI use, yet nearly two-thirds haven’t begun enterprise-wide scaling (McKinsey, 2025) 95% of enterprise AI pilots are failing due to integration gaps (MIT, 2025) 60% of AI projects will be abandoned through 2026 when unsupported by AI-ready data (Gartner, 2025) 46% of AI pilots are scrapped between proof of concept and broad adoption (S&P Global, 2025) 42% of companies abandoned most AI initiatives in 2025, up from 17% in 2024 (S&P Global, 2025). Think about that last number: The abandonment rate more than doubled in a single year. More companies are trying AI, but fewer are succeeding at scaling it.

-----

Phase: [EXPLORATION]

### Source [56]: https://agility-at-scale.com/ai/strategy/scaling-ai-from-pilots-to-enterprise-wide-deployment

Query: What failure modes emerge scaling three-tier AI CI at enterprise scale?

Answer: Common failure modes include inadequate data management, lack of model ownership, and insufficient integration with existing systems. These issues hinder scaling of three-tier AI CI at enterprise scale. The risks run in both directions. Scaling too early — before infrastructure, governance, and adoption readiness are confirmed — creates visible failures that erode executive trust. Scaling too late — staying in Pilot Fatigue while competitors build enterprise capability — means losing competitive advantage. The question isn’t whether to invest in AI; it’s whether your pilots are ready to scale and deliver measurable business value before others outpace you (WWT). Enterprise AI Scaling Best Practices: What Works at Scale. The statistics are stark: recent research from IDC, undertaken in partnership with Lenovo, found that 88% of observed POCs don’t make the cut to widescale deployment (CIO). EPAM research places the figure around 80%. Either way, the vast majority of AI pilots never become production systems. The root causes cluster into two categories — technical failures and organizational failures — and the organizational ones are typically harder to fix. Technical and infrastructure blockers: Organizational and strategic blockers: The Enterprise AI Scaling Framework: Phases from Pilot to Enterprise-Wide Deployment. Signals That Favor Staying in Pilot Mode. Not every organization is ready to scale, and forcing it creates expensive failures. Stay in pilot mode when: data access issues remain unresolved at the enterprise level, no executive sponsor has taken genuine ownership (not just budget approval), AI ROI remains unclear or speculative, or the Business Alignment between AI capabilities and strategic priorities hasn’t been validated. Organizational AI Readiness is a prerequisite, not an outcome, of scaling. Signals That Favor Scaling.

-----

Phase: [EXPLORATION]

### Source [57]: https://www.ai.se/sites/default/files/2025-12/Strategies%20for%20Scaling%20to%20a%20Large%20Number%20of%20AI%20Models%20in%20production%20-%20251215.pdf

Query: What failure modes emerge scaling three-tier AI CI at enterprise scale?

Answer: Common failure modes include inadequate data management, lack of model ownership, and insufficient integration with existing systems. These issues hinder scaling of three-tier AI CI at enterprise scale. When data availability, quality, and lineage are the biggest blockers to deployment at scale Data-centric scaling addresses the other major scaling law: models degrade because data changes. At scale, the costliest failure mode is not pipeline breakage but silent accuracy loss due to drifting data semantics. Relationship Between the Two Patterns These patterns solve different scaling bottlenecks: If your bottleneck is… The pattern that helps most is… Too much custom code per model Pipeline-centric scaling Too many inconsistent data transformations Data-centric scaling High cost of onboarding new models Pipeline-centric High cost of maintaining existing models Data-centric Compliance requiring full lineage from data → model → prediction Both, but data-centric is foundational Frequent gates) 3. Decouple data from models (shared feature objects, versioning, backfills) 4. Enable closed-loop evolution (monitoring → retraining → republishing) 5. Attach business value to model ownership (no model exists “just because it’s possible”) In fact, a mature platform will incorporate aspects from all the three different aspects. A key observation is that technology alone does not unlock scale. A fully working MLOps stack still fails if: Nobody owns the model after deployment Retraining triggers are manual or undefined Model metrics are not connected to business KPIs Feature stores are bypassed and ad-hoc data wrangling reappears Compliance processes are still document-driven instead of policy-as-code The Thousand-Model Challenge is therefore not just a manage the complexity. MLOps: Organizational Processes Organizational considerations in MLOps involve the management of the assets (data and models) and infrastructure (both hardware infrastructure such as GPUs and virtual machines but also software infrastructure) across different teams (DevOps, MLOps, Data engineering, Data Science) and organisational units. Figure 4; Organizational bottlenecks across Data, ML, and Infra teams in enterprise MLOps. In standard organisations, the nature of machine learning models in production surfaces additional hurdles related to the structure of the organisations that go beyond the technical challenges (scale, monitoring, deployment, model management). Team-Specific Issues: 1. Data Engineering: - Data sources accessibility - Unclear ownership of

-----

</details>

<details>
<summary>How do latency tradeoffs impact selective AI eval execution in high-frequency CI?</summary>

Phase: [EXPLORATION]

### Source [58]: https://galileo.ai/blog/continuous-integration-ci-ai-fundamentals

Query: How do latency tradeoffs impact selective AI eval execution in high-frequency CI?

Answer: Latency tradeoffs impact selective AI eval execution by balancing speed and accuracy, crucial for high-frequency CI to maintain system performance and user satisfaction. Lower latency often reduces accuracy, requiring careful model optimization. Adaptive strategies help manage this tradeoff effectively. This is also where purpose-built eval models become practical. Galileo's Luna-2 is designed for this transition, running 10-20 evaluation checks simultaneously at sub-200ms latency and operating at 98% lower cost than LLM-based evaluation. That kind of cost and latency profile makes it easier to keep quality checks inside your CI loop instead of treating them as an occasional batch job. Higher deployment frequency should correlate with fewer production incidents if your eval gates are working. Track rollback rates as a leading indicator of pipeline maturity. A high rollback rate usually means your eval gates are either misconfigured or missing coverage for important failure modes. Latency budgets matter for production agents. Every CI build should verify that prompt changes, model updates, or new tool integrations do not push inference latency past acceptable thresholds. A model that is more accurate but much slower may still degrade the overall experience enough to erase the quality gain. You should also track the compute cost per build alongside latency. As your eval suites become more comprehensive, you need visibility into whether infrastructure costs are scaling cleanly or whether a staged testing strategy would work better. Running lightweight checks first and expensive evals only on passing builds can preserve coverage while controlling spend. The main constraint is cost and latency. Full-fidelity LLM-as-judge evaluators are too slow and expensive to run synchronously on every production request. Purpose-built evaluation models change that equation by making continuous scoring practical at a production scale. Once those scores exist, Galileo's Runtime Protection can act on them in real time, blocking hallucinations, intercepting prompt injections, redacting PII leakage, and enforcing safety policies before unsafe outputs reach your production traffic. The result is a closed loop where development evals and production guardrails share the same quality logic, eliminating the gap between what you test and what you enforce. Adopt Continuous Monitoring as the Final CI Stage

-----

Phase: [EXPLORATION]

### Source [59]: https://www.emergentmind.com/topics/latency-quality-trade-off

Query: How do latency tradeoffs impact selective AI eval execution in high-frequency CI?

Answer: Model Quantization Ratio α (Vision/LM Inference): The proportion of low-bitwidth channels or layers, α, directly trades accuracy for lower per-inference or aggregate latency. For example, FlexiQ’s channel-level ratio α governs a smooth Pareto curve: at α=50%, accuracy loss is under 0.6% with a 40% speedup compared to full-precision (Kim et al., 3 Oct 2025). Precision Assignment γ (LLMs): The fraction of transformer layers quantized to lower-precision (e.g., FP4) in adaptive LLM inference can be calibrated offline to meet specific latency caps; moderate values (e.g., γ∼0.2) capture most speedup with minimal reward loss on high-frequency trading tasks (Kang et al., 26 May 2025). Domain practitioners are encouraged to: Determine application-critical latency or quality thresholds, then evaluate trade-off curves to select domain-specific parameters (e.g., b, α, γ, split point). For real-time and high-frequency settings, operate close to “knee points” on the Pareto frontier to maximize performance under constraint. Exploit recent advances in adaptive, mixed-precision, or hardware-aware architectures to expand the efficient frontier. Leverage economic models or user-value assessments to justify latency-reducing strategies where quality sacrifices are marginal. Recognize that in interactive or decision-driven applications, post-hoc error correction is impossible, magnifying the cost of quality losses due to latency optimization. The latency-quality trade-off describes the fundamental interdependence between the responsiveness (latency) of a system or algorithm and the correctness, fidelity, or utility (quality) of its outputs. This trade-off permeates a wide range of domains, from real-time machine learning inference and communications to financial trading, speech translation, and networked control systems. In most settings, reduced latency can be achieved only at the cost of degraded output quality—whether that means lower accuracy, increased error probability, diminished reward, or loss of semantic integrity. Understanding and managing this trade-off is essential for designing systems that satisfy application-level service constraints and user experience goals.

-----

Phase: [EXPLORATION]

### Source [60]: https://www.gmicloud.ai/ko/blog/latency-vs-quality-tradeoffs-in-ai-workflow-design

Query: How do latency tradeoffs impact selective AI eval execution in high-frequency CI?

Answer: Designing effective AI workflows is not about eliminating the tradeoff between latency and quality, but about managing it intentionally. Every decision, from model selection to orchestration and infrastructure, directly impacts how fast a system responds and how accurate its outputs are. As workflows become more complex, optimization moves beyond individual techniques like caching or parallel execution and becomes a system-level challenge. The ability to balance real-time performance with reliable outputs depends on how well the entire stack works together. Latency measures the time delay between initiating a request and receiving a complete response. AI systems have latency that spans multiple components. Model latency tracks how long the AI model takes to process input and generate output. Retrieval latency measures the time needed to fetch additional data from applications before returning a response. Network latency captures the delay as data travels between client devices and servers. Understanding the latency-quality tradeoff is crucial for building effective AI workflows that balance user experience with output accuracy.

-----

Phase: [EXPLORATION]

### Source [61]: https://galileo.ai/blog/understanding-latency-in-ai-what-it-is-and-how-it-works

Query: How do latency tradeoffs impact selective AI eval execution in high-frequency CI?

Answer: Latency significantly affects AI system performance. High latency can lead to slower responses, making AI applications impractical when quick reactions are essential. For example, in autonomous vehicles, even slight processing delays can pose serious safety risks, potentially leading to accidents. Maintaining low latency ensures tasks are executed promptly and effectively. Reducing latency improves your system's efficiency and enhances user satisfaction. Different applications prioritize latency in unique ways based on their specific needs: Mission-Critical Systems: Autonomous vehicles, for example, require ultra-low latency to make split-second decisions in real-time, justifying the investment in high-end hardware like GPUs and custom accelerators. Batch Processing: Data analytics platforms prioritize throughput over immediate response times. They handle large volumes of data efficiently, allowing for higher latency without impacting performance significantly. Interactive Services: Virtual assistants like Siri or Alexa balance latency and throughput. This ensures quick responses to user commands while preventing system overload. When choosing your preferred hosting, finding the right balance between the cloud’s flexibility and the speed of on-premise systems is crucial to meeting the latency needs of your AI applications. Tasks are processed step by step, which can increase latency. Optimization focuses on improving algorithm efficiency. Involves handling large amounts of pixel data at once. Requires faster hardware and efficient data flow to reduce latency.

-----

Phase: [EXPLORATION]

### Source [62]: https://arxiv.org/html/2505.19481v1

Query: How do latency tradeoffs impact selective AI eval execution in high-frequency CI?

Answer: Table 1 demonstrates that FPX , by dynamically trading off latency and quality through adaptive model size and bitwidth selection, achieves the highest daily yield on HFTBench and the best overall reward across both benchmarks. High-Frequency Trading (HFTBench). Latency–Quality Trade-off. We are the first to systematically formulate and investigate the latency–quality trade-off in the context of latency-sensitive agent decision tasks. Latency-Sensitive Evaluation Benchmarks: We introduce two novel benchmarks for evaluating LLM performance in the latency-sensitive settings: (1) a high-frequency trading (HFT) system specifically tailored to LLMs, and (2) a competitive fighting game environment based on Street Fighter from the DIAMBRA platform (Palmas, 2022). Adaptive Mixed Precision Inference Framework. We propose an adaptive mixed-precision inference framework that that enables flexible control over inference latency while minimizing quality degradation. Low Precision Inference to Reduce Latency. In this work, we present the first systematic study of the latency–quality trade-off for LLM-based agents in latency-sensitive agent decision tasks. To support this investigation, we introduce two real-time evaluation benchmarks: HFTBench, a high-frequency trading simulator, and StreetFighter, a competitive gaming environment. In both settings, rapid yet accurate decisions are essential to achieving high downstream rewards.

-----

</details>

<details>
<summary>What production metrics quantify AI eval effectiveness as regression detectors in CI?</summary>

Phase: [EXPLORATION]

### Source [68]: https://semaphore.io/what-metrics-should-you-use-to-evaluate-ai-in-your-ci-cd-pipeline

Query: What production metrics quantify AI eval effectiveness as regression detectors in CI?

Answer: Track deployment success rate, rollback frequency, mean time to recovery, incident frequency. AI should reduce incidents, not increase unpredictable rollbacks. Watch for behavioral signals like developers bypassing AI suggestions, teams disabling AI features, builds being re-run more often. Guard against false confidence where AI selects a subset of tests, build passes, but regression appears in production, increasing defect escape rate. For performance optimizations like intelligent test selection, track pull request validation time, time from commit to first feedback, end-to-end pipeline duration. A meaningful improvement should reduce median build time without increasing failure escape rate. If build time decreases but post-merge failures increase, AI may be trading speed for reliability. Measure flaky test frequency, re-run rate, test stability over time, false negative rate.

-----

Phase: [EXPLORATION]

### Source [69]: https://productschool.com/blog/artificial-intelligence/evaluation-metrics

Query: What production metrics quantify AI eval effectiveness as regression detectors in CI?

Answer: Tier 0: Smoke tests for immediate red flags. Tier 1: Core eval suite on golden sets and adversarial tests running in CI pipeline for each significant model update to cover common failure modes and ensure no regression on key metrics. Use ROC-AUC / PR-AUC to evaluate how well model separates classes. Accuracy, precision, recall, F1 score to compare models, catch regressions on labeled datasets. Accuracy tells fraction of predictions correct, works well when classes balanced and mistakes cost same.

-----

Phase: [EXPLORATION]

### Source [70]: https://galileo.ai/blog/continuous-integration-ci-ai-fundamentals

Query: What production metrics quantify AI eval effectiveness as regression detectors in CI?

Answer: Track evaluation score stability across builds for accuracy, context adherence, instruction adherence, tool selection quality, action completion, reasoning coherence. Healthy CI shows stable or improving scores; sudden drops signal regressions. Group into quality metrics (context/instruction adherence), agentic metrics (tool selection/action completion), diagnostic metrics (reasoning coherence). Comprehensive eval coverage predicts production reliability. Integrate evals into CI/CD for regression testing, model comparison, A/B testing, gating deployments on quality thresholds.

-----

Phase: [EXPLORATION]

### Source [71]: https://galileo.ai/blog/ai-agent-metrics

Query: What production metrics quantify AI eval effectiveness as regression detectors in CI?

Answer: CI/CD integration ensures evaluations run automatically on every change, catching regressions before production. Configure evaluation failures to prevent deployment. Track ratio of production-incident-derived evals to pre-designed evals for organizational learning. Each production failure becomes encoded as a test preventing recurrence, building comprehensive regression suite capturing real-world failure modes.

-----

Phase: [EXPLORATION]

### Source [72]: https://www.version1.com/en-us/blog/ai-performance-metrics-the-science-and-art-of-measuring-ai

Query: What production metrics quantify AI eval effectiveness as regression detectors in CI?

Answer: Classification metrics: accuracy, precision, recall, F1 score, AUC-ROC. Regression metrics: MAE, MSE, RMSE. F1 score is harmonic mean of precision and recall. AUC-ROC measures area under ROC curve. These metrics assess performance, detect regressions when changing prompts/data/architecture, compare models on labeled datasets.

-----

</details>

<details>
<summary>How do microservices CI patterns inform three-tier AI agent pipelines?</summary>

Phase: [EXPLORATION]

### Source [73]: https://redis.io/blog/ai-agent-pipeline

Query: How do microservices CI patterns inform three-tier AI agent pipelines?

Answer: A common production pattern is "Context + Retrieval Store": working memory in the context window, long-term records in an external vector or structured store, with a retrieval pipeline injecting relevant records at each step. This pattern shows up across coding assistants, customer-service bots, and enterprise copilots. Together, these three tiers are what let the pipeline behave like a system instead of a single inference call. Production agent reliability is a systems engineering problem more than a prompting problem. Most of the mitigations that matter live in the infrastructure around the model. The pipeline starts by turning a broad goal into steps the agent can actually execute. One approach is task decomposition, breaking complex queries into manageable pieces as part of an LLM workflow. Some planning architectures use detailed reasoning and refine the plan after each step based on tool outputs. An architecture guide identifies five orchestration patterns at this stage: prompt chaining, routing, parallelization, evaluator-optimizer, and orchestrator-workers. Those patterns shape how work moves through the system before the agent ever calls a tool. When that scope gets too broad, multi-agent systems split objectives and assign each to a dedicated agent with its own prompt, LLM, tools, and custom code. Common orchestration patterns include: Supervisor: A central agent analyzes requests and routes sub-tasks to specialized agents; Hierarchical: Multiple levels of control, from a high-level planner to domain coordinators to execution agents, with more scalability but also more coordination overhead; Sequential: Agents share session state, with outputs flowing forward in a fixed order; Swarm: Fully decentralized with no central control, where local rules shape coordination.

-----

Phase: [EXPLORATION]

### Source [74]: https://www.linkedin.com/posts/ypaulraj_migrating-from-a-microservices-based-distributed-activity-7346381227890798592-43gW

Query: How do microservices CI patterns inform three-tier AI agent pipelines?

Answer: Why CI/CD Pipelines Must Evolve to Govern AI Agents CI/CD pipelines transformed software delivery. They brought speed, consistency, and trust to how we release code. But as enterprises embrace AI agents—autonomous systems that act, decide, and remediate—the old rules no longer apply. The pipelines we built for microservices are not enough to govern intelligence. An AI agent isn’t just another service. It is a system that combines code, prompts, data, reasoning policies, and guardrails. Unlike static applications, its behavior can shift depending on context, feedback, and evolving knowledge. If traditional CI/CD pipelines only validate code correctness, they leave a blind spot: the agent’s decision-making. Here’s why pipelines must evolve: Intelligence Must Be Versioned Prompts and Microservices are not only for bigco’s anymore, the best new startup teams I talk to are going ALL IN on microservices these days. Sounds weird..? Shocker: AI is behind it. AI + microservices for small teams is not about architecture opinions. It is about creating the conditions to use AI to ship fast, learn weekly, and safely delete what didn’t work. As I speak to more of these teams, some patterns are emerging. Here’s the beta AI-native engineering playbook for the fastest startups: 1️⃣ Start with boundaries Define clear service contracts first. Ensure APIs and events are clear. Ensure AI builds inside guardrails. 2️⃣ Standardize what might hurt One way to auth. One way to log, trace, and alert. Framework features beat documentation. 3️⃣ Make contracts the context Feed your LLM the

-----

Phase: [EXPLORATION]

### Source [75]: https://techcommunity.microsoft.com/blog/azureinfrastructureblog/cicd-as-a-platform-shipping-microservices-and-ai-agents-with-reusable-github-act/4504550

Query: How do microservices CI patterns inform three-tier AI agent pipelines?

Answer: Maturity Model Stage | Delivery Mechanism | Validation CI/CD as Automation | Per-repo YAML | Tests CI/CD as Product | Reusable versioned workflows | Tests + Approval gates CI/CD as Governance | Platform repo + GitHub Environments | Tests + Reviews + Traceability AI Delivery Platform | Evaluation gates + Foundry runtime | Semantic scoring + Drift monitoring Each stage is additive — the platform repo from stage 2 powers all subsequent stages. No rebuild required. The same architectural principle scales from microservices to AI agents: centralize delivery logic, version it, expose it as a reusable interface. What changes for AI is the definition of "correct" — from binary pass/fail to continuous behavioral scoring. At ten services, duplicated CI/CD pipelines are annoying. At fifty, they’re a liability. Versions diverge, security fixes propagate inconsistently, and deployment logic becomes org-wide technical debt. The fix isn’t better templates — it’s a different architecture. This post builds a two-tier delivery platform: reusable GitHub Actions workflows for microservices, extended with evaluation gates for AI agents. The core insight is that AI systems break CI/CD’s fundamental assumption — deterministic correctness. A unit test validates code behavior. It cannot validate whether an agent hallucinates, drifts, or degrades silently across prompt changes. Addressing that requires evaluation as a first-class deployment gate, not a manual afterthought. By the end: a versioned CI/CD platform, a

-----

Phase: [EXPLORATION]

### Source [76]: https://agility-at-scale.com/ai/architecture/three-tier-agentic-ai-architecture-framework

Query: How do microservices CI patterns inform three-tier AI agent pipelines?

Answer: How Orchestration Coordinates Complex Work The Manager Agent pattern sits at the heart of this tier. A Manager Agent maintains a high-level plan, breaks it into delegatable tasks, and monitors progress through a shared ledger. The critical capability is iterative refinement: the Manager Agent backtracks when sub-tasks fail, re-delegates when agents stall, and adjusts the overall plan based on intermediate results. As Microsoft’s agent design pattern documentation describes, the manager agent “iterates, backtracks, and delegates as many times as needed to build a complete plan that it can successfully carry out” and “regularly checks whether the original request is satisfied or stalled and updates the ledger to adjust” (Microsoft). Why Tiers Matter More Than Features In flat multi-agent architectures, every agent operates at the same privilege level with the same access patterns. This works in prototypes. It collapses in production. The Three-Tier Agentic AI Architecture Framework addresses this by requiring organizations to demonstrate capability maturity before granting agents additional autonomy. Each tier serves a distinct architectural purpose: The Tool Orchestration Pattern defines how agents access external tools, APIs, and services. Without a coordinated pattern, agents make redundant calls, create race conditions, and generate inconsistent outputs. Orchestration applies Reasoning Transparency with Continuous Evaluation so every decision is traceable through Audit Trails and Explainability Layers. Key Human-in-the-Loop capabilities in this tier include:

-----

Phase: [EXPLORATION]

### Source [77]: https://www.augmentcode.com/guides/cicd-ai-agents-pipeline-integration

Query: How do microservices CI patterns inform three-tier AI agent pipelines?

Answer: Intent, Augment Code's agentic development environment, addresses this gap through two components that work together: a living spec layer that gives agents a shared source of truth, and the Auggie CLI that enforces that truth inside CI/CD pipelines. This guide covers the practical integration patterns: running the Auggie CLI in GitHub Actions, configuring Service Accounts for automated agent execution, enforcing spec validation as a CI gate, and wiring agent-generated PRs into existing test suites. Why AI Agents Need CI/CD Integration, Not Just Manual Runs AI agent pipeline automation fails when teams treat agents as interactive tools rather than pipeline participants. Manual agent runs create three structural problems that compound as agent adoption scales across a team. Standard CI/CD pipelines miss the failure modes AI agents introduce: spec drift, hallucinated dependencies, and code that passes tests while violating the agreed contract. Closing that gap requires spec validation as a first-class CI stage and a Verifier gate that blocks merges when agent output drifts from the plan. This guide covers the integration patterns that make it work. The CI/CD approach for AI agents is an agent-aware pipeline architecture that validates spec alignment and behavioral consistency before code reaches production. Intent, Augment Code's agentic development environment, provides the spec layer and automation tooling that make this architecture practical.

-----

</details>

<details>
<summary>What serverless tools could optimize selective AI evaluation triggers?</summary>

Phase: [EXPLORATION]

### Source [78]: https://ijcsrr.org/wp-content/uploads/2025/05/02-0205-2025.pdf

Query: What serverless tools could optimize selective AI evaluation triggers?

Answer: Serverless tools like AWS Lambda optimize AI evaluation triggers through event-driven execution and pay-per-use. Amazon API Gateway serves as entry point for invoking AI models on Lambda. Benchmarking tools like Amazon SageMaker Serverless Inference Benchmarking Toolkit measure performance of serverless inference endpoints under different loads. AWS offers Serverless Inference within Amazon SageMaker with distinct performance characteristics. Integration of AWS Inferentia and Trainium accelerators within serverless functions for inference workloads. Adaptive batching algorithms dynamically adjust batch sizes based on real-time workload characteristics.

-----

Phase: [EXPLORATION]

### Source [79]: https://www.siliconflow.com/articles/en/the-best-serverless-ai-deployment-solution

Query: What serverless tools could optimize selective AI evaluation triggers?

Answer: Azure Functions is a serverless computing service enabling event-driven functions with triggers like HTTP requests, queues, and timers. It offers built-in CI/CD integration and advanced monitoring. SiliconFlow provides automatic scaling, optimized inference engine, and unified API for serverless AI workloads. AWS Lambda and Google Cloud Functions offer general-purpose serverless computing. Modal provides specialized GPU access for AI-optimized performance.

-----

Phase: [EXPLORATION]

### Source [80]: https://medium.com/aidatatools/serverless-ai-the-complete-guide-to-building-and-deploying-ai-applications-without-infrastructure-9a454cf6c48d

Query: What serverless tools could optimize selective AI evaluation triggers?

Answer: Azure AI serverless supports advanced optimization techniques with reduced initialization times for ML workloads. Resource optimization includes multi-instance GPU sharing, automated scaling based on traffic patterns, memory-efficient model serving. Platform improvements feature GPU sharing mechanisms, memory-efficient model serving, automated model deployment. Tools support cold start reduction, resource utilization, performance monitoring.

-----

Phase: [EXPLORATION]

### Source [81]: https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-serverless/designing-serverless-ai-architectures.html

Query: What serverless tools could optimize selective AI evaluation triggers?

Answer: Amazon S3 triggers on object creation such as document uploads. Amazon Kinesis and Amazon MSK ingest streaming events. EventBridge rules initiate workflows. Processing layer handles input validation, formatting, metadata tagging. Use serverless components like Lambda, Amazon Bedrock, SageMaker Serverless Inference. Security with fine-grained IAM roles, observability with CloudWatch and X-Ray, scalability with serverless components.

-----

Phase: [EXPLORATION]

### Source [82]: https://aws.amazon.com/blogs/big-data/optimize-your-workloads-with-amazon-redshift-serverless-ai-driven-scaling-and-optimization

Query: What serverless tools could optimize selective AI evaluation triggers?

Answer: Amazon Redshift Serverless uses AI-driven scaling and optimization with visual slider for price-performance balance. Automatically adds or removes resources based on query complexity, data volume, and queuing. Performs AI-driven optimizations like automatic materialized views and table design optimization to meet price-performance targets.

-----

</details>

<details>
<summary>How did build systems evolve from Make to influence AI CI?</summary>

Phase: [EXPLORATION]

### Source [83]: https://buildkite.com/resources/blog/build-systems-in-the-age-of-ai-assisted-coding

Query: How did build systems evolve from Make to influence AI CI?

Answer: Build systems evolved from Make to influence AI CI by enhancing automation and integration, addressing scalability and complexity, and adapting to modern development practices. Software development practices have evolved significantly over the past two decades. The introduction of continuous integration and deployment (CI/CD) systems was an enormous boon to software delivery speed and quality. CI/CD uses highly controlled ephemeral environments to build and test software consistently. This solves the “works on my machine”-type problems and mitigates the risks of shipping buggy software. However, the increased usage of AI-assisted coding tools has ripple effects. The generated code may have poor style and bugs. More tests might be needed to compensate for this. And because more code is being produced, the number of pull requests and code reviews per day will increase. These ripple effects put more strain on build systems, and for reasons we will explore in this article, not all build systems scale up well to handle the new load. The rate of uptake of AI-assisted coding is astonishing. GitHub Copilot was released just three years ago (October 2021), and according to a GitHub survey, 92% of U.S.-based developers use AI coding tools both in and outside work. However, in the 2020s, more improvement is needed. The complexity of software, the expectations of fast delivery, the extensive software supply chains, and the increasing size of teams and projects add too much pressure to simple CI/CD systems. With AI-assisted development increasing the commit frequency, those systems have reached their limits. A fresh approach is needed to create build systems capable of meeting these modern demands. To meet the challenges created by the prolific use of AI assistance, we need build systems that are both scalable and flexible.

-----

Phase: [EXPLORATION]

### Source [84]: https://signalsandthreads.com/build-systems

Query: How did build systems evolve from Make to influence AI CI?

Answer: One thing that strikes me about the world of build systems is just how many of them there are. Not only are there lots of successor systems to Make, but these systems are broken off into different organizations and communities. Lots of companies have their own build systems. There’s Bazel, which is an open source build system, but it’s actually a successor to an older internal one from Google called Blaze and then Twitter and Facebook built similar systems called Pants and Buck and then there’s a ton of different language specific build systems. Some build systems were designed with that in mind. It’s pretty common to come across projects that instead of using a build system directly they generate build scripts from higher level specifications. For example, you might take a build system like Make or a build system like Ninja and you would generate these low level descriptions of what needs to be built from a higher level description that can be written in your own language of choice. This does happen and I’ve seen a few examples like that. In some sense we’re saying, well, don’t use Make for big projects at all. After we finished that paper, we also wanted to look at the wider context of build systems. There are a lot of build systems out there, and in some sense it feels a bit sad that every community has to redevelop their own build system. We were trying to figure out what were the differences and commonalities in all the major build systems out there, so we wrote another paper called, “Build Systems à la Carte,” where our goal was to look at these systems and distill their differences, at least the differences in their algorithmic core, to simple models, maybe 20-30 lines of code so that they become comprehensible to a human being unlike looking at a million line project.

-----

Phase: [EXPLORATION]

### Source [85]: https://www.harness.io/blog/build-system-vs-ci

Query: How did build systems evolve from Make to influence AI CI?

Answer: The build system remains at the core of any CI system, but modern CI systems de-incentivize Continuous Build, Occasional Integration (CBOI) practices and foster collaboration, frequent integration, constant code review, and many best practices that, ultimately, benefit software quality, security, and the velocity and trust of development teams. The beauty of CI is that the system (or at the very least, the necessary bit for the developer to be confident changes won't break anything (i.e. their microservice)), can be completely spun up, integrated with the changes, and ran through syntax, tests, scanners, and so on to return a sanity check to the user to deliver the artifact. A bit of History First, Young Fellas. I personally equate build systems to Continuous Integration systems. At least, I do so nowadays. I probably wouldn't 20 years ago. We are, after all, comparing two sides of the same coin; a problem that has been present in software development since forever! Just kidding. The term 'build system' started becoming popular in English literature around the 60s. That's around the time software started becoming a thing and mainframes were being set up at company HQs with cranes! No customers enjoyed interacting with software. CD pipelines were just a dream and no one spoke about lead time, deployment steps, or even releases. But then, new stuff came rolling down the timeline. Version control was likely the best new thing to land in anyone's dev environment. Continuous Integration was arguably the second category in software development that reached a certain maturity in the naughts, according to Google. Applications were becoming first-class citizens in any organization, open source was exploding, and build servers were becoming an utter annoyance. Hence, we got modern / mature CI systems to toughen the software development process with ongoing automation to a previous manual process.

-----

</details>

<details>
<summary>What robotics simulation CI lessons apply to LLM agent testing?</summary>

Phase: [EXPLORATION]

### Source [86]: https://arxiv.org/html/2601.20334v1

Query: What robotics simulation CI lessons apply to LLM agent testing?

Answer: Robotics simulation CI lessons for LLM agent testing include using simulation environments to evaluate agent behavior, employing action primitives for control, and combining evaluations with simulation-based testing for comprehensive results.

-----

Phase: [EXPLORATION]

### Source [87]: https://hlfshell.ai/posts/llm-task-planner

Query: What robotics simulation CI lessons apply to LLM agent testing?

Answer: Robotics simulation CI lessons for LLM agent testing include using simulation environments to evaluate agent behavior, employing action primitives for control, and combining evaluations with simulation-based testing for comprehensive results.

-----

Phase: [EXPLORATION]

### Source [88]: http://rdi.berkeley.edu/llm-agents/f24

Query: What robotics simulation CI lessons apply to LLM agent testing?

Answer: Robotics simulation CI lessons for LLM agent testing include using simulation environments to evaluate agent behavior, employing action primitives for control, and combining evaluations with simulation-based testing for comprehensive results.

-----

Phase: [EXPLORATION]

### Source [89]: https://langwatch.ai/scenario/introduction/simulation-based-testing

Query: What robotics simulation CI lessons apply to LLM agent testing?

Answer: Robotics simulation CI lessons for LLM agent testing include using simulation environments to evaluate agent behavior, employing action primitives for control, and combining evaluations with simulation-based testing for comprehensive results.

-----

Phase: [EXPLORATION]

### Source [90]: https://mikelikesrobots.github.io/blog/llm-robot-control

Query: What robotics simulation CI lessons apply to LLM agent testing?

Answer: Robotics simulation CI lessons for LLM agent testing include using simulation environments to evaluate agent behavior, employing action primitives for control, and combining evaluations with simulation-based testing for comprehensive results.

-----

</details>

</research_source>

<research_source type="scraped_from_research" phase="exploitation" file="best-ai-eval-tools-for-ci-cd-pipelines-2026-review-articles-.md">
<details>
<summary>Best AI Eval Tools for CI/CD Pipelines (2026 Review) - Articles - Braintrust</summary>

Phase: [EXPLOITATION]

**Source URL:** <https://www.braintrust.dev/articles/best-ai-evals-tools-cicd-2025>

# Best AI Eval Tools for CI/CD Pipelines (2026 Review) - Articles - Braintrust

Best AI Eval Tools for CI/CD Pipelines (2026 Review)

The best LLM applications aren't built through endless manual testing sessions. They're built through systematic, automated evaluation that runs with every code change. As AI engineering teams mature, they're discovering what software teams learned decades ago: continuous testing catches problems early, saves time, and ships better products.

The shift toward CI/CD-integrated evals represents an evolution in how we build with LLMs. Teams are moving beyond one-off evaluations to continuous validation that runs automatically with every deployment, giving them confidence that prompt changes, model swaps, and code updates won't degrade their application's quality. Early adopters are seeing the benefits: faster iteration cycles, fewer production surprises, and the ability to ship AI features with the same confidence they have deploying traditional software.

Recent adoption trends show that organizations implementing automated [LLM evals](https://www.braintrust.dev/articles/best-llm-evaluation-platforms-2025) in their CI/CD pipelines catch regressions before users do and maintain higher quality standards across deployments. This approach transforms evaluation from a bottleneck into an accelerator, enabling teams to move fast while maintaining rigorous quality standards.

## What are AI evals in CI/CD?

[AI evals](https://www.braintrust.dev/articles/best-ai-evaluation-tools-2026) (evaluations) in CI/CD are automated tests that measure your LLM application's quality, accuracy, and behavior with every code change. Rather than manually checking if your chatbot still gives good answers after updating a prompt, these tools automatically run dozens or hundreds of eval cases, score the outputs, and fail your build if quality drops below your thresholds.

This becomes important when you're not just running assertions but need LLM-as-a-judge evaluators, retrieval quality metrics, and complex multi-step agent evals. A feature might check if outputs contain certain keywords. A platform provides comprehensive evaluation frameworks that integrate with your entire development workflow.

**Key trends shaping the space:**

- **Semantic evaluation**: Moving beyond keyword matching to understand meaning through embedding similarity and LLM judges that assess relevance, factuality, and tone
- **Agent-specific evals**: Evaluating multi-step reasoning, tool usage accuracy, and whether agents converge on correct solutions (going beyond single LLM call validation)
- **Production-ready automation**: Tools designed for high-volume concurrent evals with rate limiting, caching, and failure reporting that integrates with GitHub Actions, CircleCI, and other modern pipelines

## How we chose the best AI evals tools for CI/CD

When evaluating these platforms, we focused on features that matter for production-ready CI/CD integration:

- **GitHub Actions integration quality**: Does it provide a dedicated action, or do you need to cobble together scripts? How clean is the PR commenting?
- **Evaluation capabilities**: Breadth and accuracy of built-in evaluators (LLM-as-a-judge, retrieval metrics, custom scorers)
- **Developer experience**: How straightforward is it to define eval cases, run evals locally, and debug failures?
- **Deployment flexibility**: Self-hosted versus cloud options, especially for teams with data residency requirements

## The 4 best AI evals tools that integrate in CI/CD

### 1. Braintrust

**Quick overview**

Braintrust is a complete AI development platform that brings production-grade [evaluation](https://www.braintrust.dev/articles/how-to-eval) directly into your development workflow. Built by engineers who've scaled LLM applications at companies like Google and Stripe, it provides native CI/CD integration through a dedicated GitHub Action that automatically runs experiments and posts results to your pull requests.

**Best for**

Teams who want eval results that integrate with their development workflow, not just pass/fail metrics. Braintrust excels when you need side-by-side comparisons of prompt changes, detailed experiment tracking, and insights that help you understand why outputs changed, not just that they changed.

**Pros**

- **Dedicated GitHub Action with PR comments**: The `braintrustdata/eval-action` automatically posts detailed experiment comparisons directly on pull requests, showing how your changes affected output quality with score breakdowns
- **Experiment tracking**: Every eval run creates a full experiment with git metadata, making it straightforward to trace quality changes back to specific code commits and compare results over time
- **Cross-language SDK support**: Full-featured SDKs for both [Python](https://www.braintrust.dev/docs/reference/python) and [TypeScript](https://www.braintrust.dev/docs/reference/nodejs) with identical evaluation APIs, making it straightforward to run evals across your stack
- **Built-in concurrency management**: Automatic rate limiting and concurrency controls prevent hitting API limits during large eval runs, with configurable `maxConcurrency` settings
- **Watch mode for rapid iteration**: Run `braintrust eval --watch` to automatically re-run evals as you edit code, speeding up local development
- **Comprehensive evaluation library**: Built-in scorers for factuality, relevance, security, and more through the [AutoEvals library](https://www.braintrust.dev/docs/reference/autoevals), plus custom scoring support

**Cons**

- **Self-hosting requires enterprise plan**: While the platform offers generous free tiers, running your own instance requires an enterprise agreement, which may not fit teams with strict data residency requirements on a budget

**Pricing**

- **Free**: $0/month (1M trace spans, 1GB processed data, 10K scores, 14 days retention, unlimited users)
- **Pro**: $249/month (Unlimited traces, 5GB processed data, 50K scores, 1 month retention)
- **Enterprise**: Custom pricing (Self-hosted deployment, premium support, extended retention)

### 2. Promptfoo

**Quick overview**

Promptfoo is a developer-first, open-source eval framework. It offers a CI/CD integration through its native GitHub Action, CLI tools for GitLab CI, Jenkins, and other platforms.

**Best for**

Engineering teams who want full control over their testing infrastructure and prefer open-source tools.

**Pros**

- **Fully open-source with no feature gates**: Community version includes all core features for local evals, evaluation, and vulnerability scanning without paid upgrades required
- **Native CI/CD support across platforms**: GitHub Actions, GitLab CI, Jenkins, CircleCI, and more with built-in caching and quality gate support
- **Security-first approach**: Built-in red teaming capabilities for prompt injection, PII leaks, jailbreaks, and other vulnerabilities
- **Configuration-driven evals**: Define eval cases in YAML files that live alongside your code, making eval maintenance straightforward

**Cons**

- **Requires infrastructure management**: Unlike cloud platforms, you're responsible for hosting results, managing secrets, and maintaining the eval infrastructure
- **Learning curve for advanced features**: The YAML configuration can become complex for sophisticated eval scenarios with multiple providers and custom evaluators
- **No centralized experiment tracking**: Results are stored locally or in your CI artifacts. There's no platform for comparing eval runs over time or analyzing quality trends across deployments

**Pricing**

- **Community**: Free and open-source
- **Enterprise**: Custom pricing for teams needing centralized dashboards, SSO, and priority support

### 3. Arize Phoenix

**Quick overview**

Arize Phoenix is an open-source observability and evaluation platform built on OpenTelemetry standards, backed by Arize AI. It integrates with CI/CD pipelines through custom Python scripts and GitHub Actions workflows.

**Best for**

Teams interested in open source tools or already in the Arize ecosystem.

**Pros**

- **Fully open-source and self-hostable**: Deploy with a single Docker command, free with no feature gates or restrictions
- **Built on open standards**: Based on OpenTelemetry and OpenInference, ensuring your instrumentation work is reusable across platforms

**Cons**

- **CI/CD integration requires writing custom code**: No dedicated GitHub Action. You must write your own workflows using the experiments API and Python scripts, significantly increasing setup complexity compared to tools with native actions
- **Evaluation features less mature than dedicated tools**: While comprehensive, the evaluation library is newer compared to specialized eval platforms
- **Limited experiment comparison UI**: While you can run experiments, comparing multiple runs side-by-side requires navigating through trace views rather than a dedicated experiment comparison interface

**Pricing**

- **Self-hosted**: Free and unlimited
- **Cloud (app.phoenix.arize.com)**: Free with limits
- **Arize AX**: Contact for enterprise features (HIPAA, custom dashboards, dedicated support)

### 4. Langfuse

**Quick overview**

Langfuse is an open-source LLM engineering platform focused on observability, prompt management, and evaluation. While it has some features outside of CI/CD, the CI/CD process is complex to set up.

**Best for**

Teams who want to self-host and aren't deterred by writing their own CI/CD integration to fetch traces, run evals, and save results.

**Pros**

- **Flexible evaluation approaches**: Supports LLM-as-a-judge, human annotations, and custom scoring via APIs/SDKs
- **Self-hosting with no limits**: Self-host all core features for free without any limitations
- **GitHub integration for prompts**: Webhook integration that triggers workflows when prompts change

**Cons**

- **No native CI/CD action**: Requires building custom evaluation pipelines. Unlike competitors with dedicated actions, you must manually orchestrate the entire workflow: write custom Python scripts to fetch traces, run evaluations, and save results back. This means setting up cron jobs or custom GitHub workflows yourself, making it significantly more complex than tools with out-of-the-box CI/CD support
- **Evaluation runs separate from observability**: Dataset experiments and production trace evaluations live in different parts of the platform, requiring you to switch contexts rather than having unified experiment tracking

**Pricing**

- **Self-hosted**: Free and unlimited for all core features
- **Hobby (Cloud)**: Free (50K units/month, 30 days retention, 2 users)
- **Core (Cloud)**: $29/month (100K units/month, 90 days retention, unlimited users)
- **Pro (Cloud)**: $199/month (Unlimited history, higher rate limits)
- **Enterprise**: Custom pricing for SSO, advanced security, dedicated support

## Summary table

| Tool | Starting price | Best for | Notable features |
| --- | --- | --- | --- |
| **Braintrust** | Free ($0, 1M spans) | Teams needing experiment tracking | Dedicated GitHub Action, PR comments, cross-language SDKs |
| **Promptfoo** | Free (Open source) | Security-focused engineering teams | Red teaming, 50+ provider support, runs 100% locally |
| **Arize Phoenix** | Free (Self-hosted) | Teams prioritizing observability + evals | OpenTelemetry-based, 50+ auto-instrumentations, agent evaluation |
| **Langfuse** | Free (Self-hosted) | Teams building custom eval workflows | Comprehensive platform, strong prompt management, GitHub webhooks |

## Why Braintrust wins for CI/CD evals

The future of AI development belongs to teams that can move fast with confidence. While all these tools bring value, Braintrust's dedicated focus on CI/CD-native [evaluation](https://www.braintrust.dev/articles/llm-evaluation-metrics-guide) sets it apart. The platform automatically creates [experiments](https://www.braintrust.dev/docs/evaluate) in Braintrust with every eval run and displays comprehensive summaries in your terminal and pull requests, making it straightforward to track quality over time. Braintrust integrates with GitHub, CircleCI, and can be extended to others with custom eval functions.

What truly differentiates Braintrust is its experiment-first approach. Rather than treating evals as pass/fail gates, every eval run becomes a full experiment you can analyze, compare, and learn from. When an eval fails, you don't just know that something broke. You see exactly which eval cases regressed, by how much, and can compare side-by-side with previous runs. This transforms debugging from guesswork into investigation.

For teams serious about building production-grade AI applications, the question isn't whether to automate evaluation. It's how quickly you can get started. Braintrust removes the friction, giving you a dedicated GitHub Action that works out of the box, comprehensive evaluation libraries, and the experiment tracking infrastructure to continuously improve your LLM applications. The competitive advantage goes to teams who can iterate faster while maintaining quality, and that's exactly what Braintrust enables.

## FAQs

### How do I add AI evals to my CI/CD?

Start by creating a dataset of eval cases that represent your application's key scenarios (inputs paired with expected outputs or quality criteria). Next, define your evaluation metrics (accuracy, relevance, factuality, etc.) and set quality thresholds. Finally, integrate an evaluation tool into your pipeline: with Braintrust, add the `braintrustdata/eval-action` to your GitHub workflow file, configure your API keys, and the action automatically runs evals on every pull request, posting results as comments.

### What AI evals platform offers the best CI/CD integration?

Braintrust provides the most comprehensive CI/CD integration with its dedicated GitHub Action that automatically runs experiments and posts detailed comparisons directly on pull requests. The action shows score breakdowns and experiment links without requiring custom code. Promptfoo offers good GitHub Actions support but requires more manual configuration, while Phoenix and Langfuse require writing custom Python scripts to orchestrate the evaluation workflow (significantly increasing setup complexity).

### How do I test if changes in my PR make my AI agents perform better or worse on our evals?

Use an evaluation platform that automatically runs experiments on every pull request and compares results against your baseline. Braintrust excels here. When you open a PR, the GitHub Action runs your eval suite and posts a comment showing exactly which eval cases improved, which regressed, and by how much. You see side-by-side comparisons of outputs, score changes, and can click through to full experiment details to understand why performance changed before merging.

### Why should product managers care about AI evals?

[Evals for product managers](https://www.braintrust.dev/blog/evals-for-pms) are how you turn "the AI feels worse this week" into something measurable. Without them, PMs are stuck arbitrating between engineers who insist a prompt change is fine and support tickets suggesting it isn't. With evals wired into CI/CD, every prompt tweak, model swap, or retrieval change comes with a quality delta you can actually point to. That's why evals for product managers matter: they change the conversation from gut feel to data, and they're the difference between shipping AI features cautiously and shipping them confidently.

</details>

</research_source>

<research_source type="scraped_from_research" phase="exploration" file="ci-pipelines-for-ai-agents-best-practices-galileo.md">
<details>
<summary>How to Build a Continuous Integration Pipeline for AI Agents</summary>

Phase: [EXPLORATION]

**Source URL:** <https://galileo.ai/blog/continuous-integration-ci-ai-fundamentals>

# How to Build a Continuous Integration Pipeline for AI Agents

https://framerusercontent.com/images/XYjGANE1CFuX2YfmXO58mf2zPY.jpeg?width=2048&height=1638

Conor Bronsdon
Head of Developer Awareness

https://framerusercontent.com/images/v6LuQKJwevIVpqiWNYwC3wWEtIA.png?width=2400&height=1256

Your team ships a prompt change to a production agent on a Friday afternoon. By Saturday morning, the agent is hallucinating in 4% of customer interactions, confidently recommending products that don't exist, fabricating policy details, and citing support articles that were never written. No regression test flagged it. No automated gate blocked the deployment. The logs show green across the board.

This is the [failure mode](https://galileo.ai/blog/agent-failure-modes-guide) that traditional continuous integration was never designed to catch. CI pipelines built for deterministic software assume that the same input produces the same output, that tests can assert exact matches, and that a passing build means a working system. Autonomous agents violate every one of those assumptions. They produce non-deterministic outputs, evolve with data, and fail in ways that unit tests structurally cannot detect.

You can adapt continuous integration fundamentals for AI agent development, build eval-driven pipelines that catch behavioral regressions before they reach production, and extend those evals into runtime safeguards that protect your production traffic continuously.

**TLDR:**

- Traditional CI pipelines miss non-deterministic failures in AI agents.
- Eval-driven CI gates catch quality regressions before deployment.
- Drift detection and benchmarking replace manual QA.
- Purpose-built eval models enable real-time scoring at CI scale.
- The eval-to-guardrail lifecycle turns development tests into production safeguards.

## **What Is Continuous Integration for AI?**

Continuous integration for AI extends traditional build-test-deploy automation to include model evals, data validation, and behavioral regression testing for non-deterministic systems. Where traditional software CI verifies that code compiles and functions return expected outputs, CI for AI verifies that your autonomous agents behave reliably, that they select the right tools, reason coherently, follow instructions, and avoid hallucinating.

The distinction matters now more than ever. Autonomous agents make thousands of decisions daily, and a single prompt change can cascade failures across tool selection, reasoning chains, and output quality. That gap demands systematic quality infrastructure, not manual spot-checking.

The fundamental shift is from code correctness to behavioral correctness as the CI standard. Your production agent can execute syntactically perfect code while still producing outputs that damage trust, violate policies, or generate dangerous misinformation.

Eval-driven CI catches what unit tests cannot, and it creates a common quality framework that connects data scientists, ML engineers, and product teams around measurable behavioral standards.

## **Why Traditional CI Pipelines Fail for AI Agents**

Bringing continuous integration into autonomous agent workflows exposes several structural failures in traditional CI assumptions. Understanding these failures is essential if you want to [design pipelines](https://galileo.ai/blog/automated-ai-pipelines-architectures) that actually protect production reliability.

### **Non-Deterministic Outputs Break Pass Fail Testing**

Traditional software produces the same result given the same input. Autonomous agents often do not. When you send identical prompts to the same production agent, you can get meaningfully different responses due to model sampling, weight initialization, and even hidden infrastructure variability. The output is probabilistic by design, which means variation is expected behavior, not a bug.

This variability means traditional pass/fail assertions are structurally incompatible with production agent testing. An exact-match test will either produce constant false failures, flagging acceptable variation, or miss genuine regressions by setting thresholds too loosely. CI pipelines for autonomous agents need statistical validation, tolerance thresholds, confidence intervals, and distribution comparisons rather than binary assertions.

Without those probabilistic quality checks, your pipeline becomes a rubber stamp that masks behavioral degradation behind a green build status. This underscores the need for strong, systematic agent observability and governance when you deploy production agents at enterprise scale.

### **Model Drift Degrades Performance Silently**

Production data distributions shift over time. Your production agent that performed reliably last month may silently degrade as user patterns, data schemas, or upstream APIs change. Drift can accumulate without obvious alerts until model performance degrades noticeably in production.

Your CI pipeline for autonomous agents needs automated drift detection as a first-class gate, not an afterthought. The challenge is that drift rarely triggers hard failures; it gradually shifts output distributions until quality crosses a threshold your team only notices from customer complaints.

Without that layer, you end up validating yesterday's conditions while shipping into today's traffic. The result is a false sense of confidence. Your pipeline may still report a clean build even while real-world behavior keeps drifting away from the examples your team originally tested.

From a leadership perspective, this is one of the most dangerous failure modes because it erodes production reliability gradually rather than catastrophically, making it harder to justify investment in detection until after a significant incident surfaces.

### **Data and Compute Scale Outstrip Standard CI Infrastructure**

AI agent development handles significantly larger datasets and more computationally intensive eval suites than traditional software projects. Running a comprehensive eval suite against a golden dataset on every commit requires more than a default CI runner and a few fast assertions. Your eval suite might need to score hundreds of agent interactions across multiple quality dimensions, each requiring inference calls that dwarf the cost of compiling code.

Eval suites, training runs, and large reference datasets demand infrastructure that standard CI runners often cannot provide. Resource management becomes a core pipeline design decision. You need to balance eval thoroughness against build times and compute costs so your developer velocity does not collapse under slow feedback loops.

Many enterprise AI teams address this with tiered eval strategies, running lightweight checks on every commit while reserving full-suite evals for merge requests and release candidates. That layered approach keeps feedback fast without sacrificing coverage at the decision points that matter most.

## **Building an Eval-Driven CI Pipeline for AI Agents**

For autonomous agents, the paradigm shifts from testing code functionality to evaluating behavioral quality. This reframing, from test suites to eval suites, is the foundation of effective CI for agentic systems.

### **Designing Evaluation Gates That Replace Unit Tests**

For autonomous agents, the eval suite is the test suite. Eval gates are automated quality checks for context adherence, instruction adherence, tool selection quality, and hallucination detection that run on every commit or prompt change. Unlike binary pass/fail unit tests, these gates produce continuous quality scores across multiple dimensions.

An evaluation harness runs evals end to end: providing instructions and tools, running tasks concurrently, recording all steps, grading outputs, and aggregating results. For autonomous systems, you are evaluating the harness and the model working together, because the harness itself shapes behavior.

One of the most important distinctions is between outcome grading and transcript grading. A booking workflow succeeds when the reservation exists in the database, not when the reasoning merely sounds plausible.

Transcript grading still matters because it helps you diagnose why the behavior changed. You should treat these as separate dimensions inside your CI gates. Statistical significance, not raw metric comparison, should determine whether a build passes.

### **Versioning Data Prompts and Agent Configurations**

CI for autonomous agents must track far more than code. Prompt templates, system instructions, retrieval configurations, tool definitions, and eval datasets all need version control and reproducibility.

When your production agent starts behaving differently, you need to identify whether the change came from code, a prompt update, a data shift, or a configuration change. Without that traceability, debugging becomes guesswork at scale.

Large data files, model outputs, and experiment artifacts add another layer of complexity. You need a workflow that lets your team reproduce any previous production agent configuration exactly, especially when you are debugging a regression that appears only under specific conditions.

Golden dataset construction should be treated as a continuous engineering activity, not a one-time setup task. As your autonomous agents encounter new successes and failures in the wild, you should fold those cases back into a versioned reference set that evolves with the system. The teams that maintain disciplined versioning across all three dimensions, code, data, and configuration, consistently resolve regressions faster.

### **Automating Regression Testing for Agent Workflows**

Golden flow validation is the backbone of regression testing for autonomous agents. You maintain a representative set of production agent interactions, common tasks, edge cases, and known failure modes, then benchmark every build against them.

The eval suite checks for regressions in multi-step tool selection, reasoning coherence, and action completion across agent workflows.

This process gets stronger over time when production incidents become new eval cases. Tasks that once answered "Can we do this at all?" eventually shift into a more important question: "Can we still do this reliably after the latest prompt change, model swap, or tool update?"

You get the most value when these evals integrate directly into your [CI/CD workflows](https://galileo.ai/blog/cd-vs-ct-ai) with automated quality benchmarking on every build. That gives you regression testing, model comparison, and A/B testing of production agent configurations, with results that can gate or approve deployments based on predefined quality thresholds.

The operational benefit compounds: each deployment cycle adds new golden flow cases, steadily reducing the surface area for undetected regressions.

## **Key CI Metrics for AI Agent Reliability**

Tracking the right metrics transforms CI from a checkbox exercise into a continuous quality signal. The metrics that matter for autonomous agents differ fundamentally from traditional software build metrics.

### **Evaluation Score Stability Across Builds**

Track how [accuracy](https://v2docs.galileo.ai/concepts/metrics/response-quality/correctness#correctness), [context adherence](https://v2docs.galileo.ai/concepts/metrics/rag/generation-quality/context-adherence#context-adherence), [instruction adherence](https://v2docs.galileo.ai/concepts/metrics/response-quality/instruction-adherence), and [agentic-specific metrics](https://v2docs.galileo.ai/concepts/metrics/agentic/agentic-overview) such as [tool selection quality](https://v2docs.galileo.ai/concepts/metrics/agentic/tool-selection-quality), [action completion](https://v2docs.galileo.ai/concepts/metrics/agentic/action-completion), and [reasoning coherence](https://v2docs.galileo.ai/concepts/metrics/agentic/reasoning-coherence) trend across builds. A healthy CI pipeline should show stable or improving scores over time. Sudden drops signal regressions that deserve investigation before deployment.

The broader argument is straightforward: comprehensive eval coverage across builds is one of the strongest predictors of production reliability. If you skip evals for behaviors that seem low risk, you create blind spots that only surface after deployment. A mature CI practice measures enough of the workflow that changes in behavior become visible before your team feels them in production.

A simple way to make this section easier to operationalize is to group metrics by role:

- Quality metrics, such as context adherence and instruction adherence
- Agentic metrics, such as tool selection and action completion
- Diagnostic metrics, such as reasoning coherence trends across builds

That split helps you decide which scores should block a deployment and which ones should trigger investigation.

### **Inference Latency and Resource Efficiency**

Latency budgets matter for production agents. Every CI build should verify that prompt changes, model updates, or new tool integrations do not push inference latency past acceptable thresholds. A model that is more accurate but much slower may still degrade the overall experience enough to erase the quality gain.

You should also track the compute cost per build alongside latency. As your eval suites become more comprehensive, you need visibility into whether infrastructure costs are scaling cleanly or whether a staged testing strategy would work better. Running lightweight checks first and expensive evals only on passing builds can preserve coverage while controlling spend.

This is also where purpose-built eval models become practical. Galileo's [Luna-2](https://v2docs.galileo.ai/concepts/luna/luna#luna-2-overview) is designed for this transition, running 10-20 evaluation checks simultaneously at sub-200ms latency and operating at 98% lower cost than LLM-based evaluation. That kind of cost and latency profile makes it easier to keep quality checks inside your CI loop instead of treating them as an occasional batch job.

### **Deployment Frequency and Incident Correlation**

Higher deployment frequency should correlate with fewer production incidents if your eval gates are working. Track rollback rates as a leading indicator of pipeline maturity. A high rollback rate usually means your eval gates are either misconfigured or missing coverage for important failure modes.

Systematic evals are not just a reliability practice. When your CI pipeline catches behavioral regressions early, you can ship faster with more confidence. That shifts your engineering time away from reactive debugging and back toward building new capabilities. From a budget perspective, the ROI of eval-driven CI compounds with every deployment cycle you avoid rolling back.

You can make this more actionable by reviewing three questions after each release cycle:

- Did the latest build increase rollback risk?
- Did any metric degrade without crossing the deployment threshold?
- Did production incidents expose a behavior your golden dataset missed?

That review keeps your CI pipeline tied to real production outcomes rather than isolated benchmark scores.

## **How to Go From Development Evals to Production Guardrails**

The most mature CI pipelines do not treat deployment as the finish line. They extend eval logic from development gates into production safeguards, creating a continuous quality system that protects your production traffic long after the build passes.

### **Turn Offline Evals into Runtime Safeguards**

The evals you run in CI should not stop at the deployment gate. An increasingly practical pattern is to distill development evaluators into lightweight production monitors that score live traffic continuously. The goal is a single quality framework where the same behavioral standards you enforce pre-deployment also govern what reaches your end users.

The main constraint is cost and latency. Full-fidelity LLM-as-judge evaluators are too slow and expensive to run synchronously on every production request. Purpose-built evaluation models change that equation by making continuous scoring practical at a production scale.

Once those scores exist, Galileo's [Runtime Protection](https://v2docs.galileo.ai/concepts/protect/overview) can act on them in real time, blocking hallucinations, intercepting prompt injections, redacting PII leakage, and enforcing safety policies before unsafe outputs reach your production traffic.

The result is a closed loop where development evals and production guardrails share the same quality logic, eliminating the gap between what you test and what you enforce.

### **Adopt Continuous Monitoring as the Final CI Stage**

Production is not the end of the pipeline. It is the next stage. Even the most comprehensive eval suite cannot anticipate every [failure mode](https://galileo.ai/blog/agent-failure-modes-guide) that emerges in the wild. Automated failure detection must surface the unknown unknowns that pre-deployment gates did not catch.

Industry frameworks increasingly stress that pre-deployment evals alone are insufficient for non-deterministic systems. Controlled testing environments cannot fully account for real-world dynamics. Post-deployment monitoring closes that gap by validating behavior against live traffic patterns your golden dataset never captured.

The feedback loop is what makes this a continuous integration system rather than a one-time deployment check. Production failures feed back into the eval suite, real-world edge cases become new golden dataset entries, detected drift patterns become new eval dimensions, and the system grows more comprehensive with every deployment cycle.

Automated failure pattern detection through platforms like [Galileo's Signals](https://galileo.ai/signals) can proactively analyze production traces to surface issues your team did not know to look for, then help turn those patterns into future evals.

## **Build CI Around Behavior Not Just Builds**

Continuous integration for autonomous agents works when you treat behavior as the release artifact, not just code. That means versioning prompts and datasets alongside code, replacing brittle unit tests with eval-driven gates, tracking drift before it becomes a customer problem, and extending successful offline checks into production safeguards.

You also need agent observability so you can see how changes affect real workflows, not just benchmark scores. When you connect pre-deployment evals with runtime controls and feedback loops from production, your CI pipeline becomes a real reliability system instead of a basic build script.

## **FAQ**

### **What Is Continuous Integration for AI?**

Continuous integration for AI extends traditional CI automation to include model evals, data validation, and behavioral regression testing for non-deterministic systems. Instead of verifying only that code compiles and functions return expected values, CI for AI verifies that autonomous agents behave reliably: selecting correct tools, reasoning coherently, following instructions, and avoiding hallucinations.

### **How Do I Test Non-Deterministic AI Outputs in a CI Pipeline?**

Replace exact-match assertions with statistical validation. Run multiple inferences on identical inputs to establish output distributions, define acceptable ranges for variation, and use confidence intervals to determine whether changes represent genuine regressions or natural variation. Set tolerance thresholds for key [evaluation metrics](https://v2docs.galileo.ai/concepts/metrics/overview) and flag builds only when scores fall outside statistically significant bounds.

### **What Is the Difference Between CI for Traditional Software and CI for AI Agents?**

Traditional software CI focuses on code correctness: does the function return the expected output for a given input? CI for autonomous agents focuses on behavioral correctness: does your production agent make reliable decisions across a distribution of inputs? This requires evaluating probabilistic outputs against quality thresholds, versioning prompts and data alongside code, tracking model drift, and running [eval experiments](https://v2docs.galileo.ai/concepts/experiments/running-experiments) that measure hallucination rate, reasoning coherence, and action completion.

### **When Should I Add Evaluation Gates to My AI Development Pipeline?**

Immediately. Staged evals should start pre-launch with automated checks on each production agent change, then extend to production monitoring, A/B testing, and continuous human calibration. Establish a structured quality gate as early as possible while you build your golden dataset. Even a minimal eval suite on day one catches regressions that manual review consistently misses.

### **How Does Galileo Support Continuous Integration for AI Agents?**

Galileo supports CI/CD workflows through [automated eval gates](https://v2docs.galileo.ai/getting-started/evaluate-and-improve/evaluate-and-improve) that enable regression testing, model comparison, and A/B testing of agent configurations. Luna-2 enables real-time eval scoring at production scale with sub-200ms latency, while Runtime Protection converts development evals into guardrails that block unsafe outputs before they reach production. The platform also integrates with major agent frameworks through OpenTelemetry.

</details>

</research_source>

<research_source type="scraped_from_research" phase="exploitation" file="effective-practices-for-mocking-llm-responses-during-the-sof.md">
<details>
<summary>Effective Practices for Mocking LLM Responses During the Software Development Lifecycle | Agiflow Blog</summary>

Phase: [EXPLOITATION]

**Source URL:** <https://agiflow.io/blog/effective-practices-for-mocking-llm-responses-during-the-software-development-lifecycle>

# Effective Practices for Mocking LLM Responses During the Software Development Lifecycle | Agiflow Blog

https://miro.medium.com/v2/resize:fit:1400/format:webp/1*6yMmt6xEInxnLKzl7dTx2g.png

Testing software that calls a Large Language Model is genuinely different from testing software that calls a database or a REST API. Databases return the same row for the same query. LLMs return something different every time — and that something can be brilliant, mediocre, or confidently wrong depending on factors no test harness controls. Add to that API costs that accumulate quickly across a CI run, round-trip latencies of 5–45 seconds per call, and aggressive rate limits from providers, and you have a category of dependency that will break any naive test suite.

Mocking is the pragmatic answer for most of this. This article covers when to reach for it, which technique fits which scenario, and what to pair it with so your test coverage stays honest.

## Why LLMs Are Uniquely Hard to Test Against Directly

The core problem is non-determinism. A standard unit test passes or fails based on a deterministic assertion: function returns X, database row has value Y. That contract doesn't exist with LLMs. The same prompt produces different completions on different runs, different days, and after model updates — any of which can happen silently mid-sprint.

Cost compounds the problem. Running a suite of 200 integration tests where each test makes one GPT-4 call can cost $10–$40 per run. Teams that try to run the real API in CI discover this fast, usually via a surprise billing spike. A single API call to an advanced model can cost close to $1 with long prompts, according to WireMock's analysis of MockGPT adoption.

Latency follows close behind. A test that waits 15–30 seconds for a real completion is a test developers stop running locally. Slow tests get skipped, skipped tests find no bugs.

## When Mocking Is the Right Tool

Mocking is the right choice in four scenarios:

**Developing library or integration code that sits around LLM calls.** If you're building a prompt template engine, a response parser, a retry handler, or a streaming adapter, the LLM output itself is irrelevant to what you're testing. Mock it out completely.

**Unblocking parallel development.** If a teammate owns the LLM integration layer and you own downstream processing, a mock gives you a stable fixture to work against while the real integration is still being built.

**CI/CD pipelines.** Every pull request triggering live API calls is a cost and reliability antipattern. Flaky network responses and rate-limit errors should not fail your CI runs. Mocks eliminate both.

**Regression testing for prompt parsing and extraction.** When you want to verify that your parsing logic correctly handles edge cases — empty responses, malformed JSON, truncated outputs — you control exactly what the "LLM" returns and test your handling of it.

Mocking is _not_ the right choice for evaluating whether the LLM itself produces good outputs. That's a different problem requiring a different tool (covered in the final section).

## Technique 1: Mock at the Library Layer

The simplest approach is to replace the LLM client with a fake object inside your test. LangChain ships a `FakeListLLM` that returns responses from a predefined list in sequence:

```python
from langchain.llms.fake import FakeListLLM

responses = ["The capital of France is Paris.", "I don't know."]
llm = FakeListLLM(responses=responses)
result = llm.invoke("What is the capital of France?")
assert result == "The capital of France is Paris."
```

For TypeScript/JavaScript with Jest or Vitest, you mock the OpenAI or LangChain client module directly:

```typescript
import { vi } from 'vitest';
import OpenAI from 'openai';

vi.mock('openai', () => ({
  default: vi.fn().mockImplementation(() => ({
    chat: {
      completions: {
        create: vi.fn().mockResolvedValue({
          choices: [{ message: { content: 'Mocked response' } }],
        }),
      },
    },
  })),
}));
```

One important nuance: avoid mocking internal methods of the library itself. LangChain's internals change frequently between minor versions. Mock at the boundary — the API call — not deep inside the framework.

## Technique 2: Record and Replay with VCR

Library-layer mocks require you to handwrite responses. For integration tests where you want to verify your code works with _real_ LLM output structures, VCR (Video Cassette Recorder) is a better fit.

VCR records actual HTTP interactions to YAML "cassette" files during an initial run, then replays them deterministically on subsequent runs. The test talks to a real API exactly once; after that, it's completely offline.

```python
import pytest

@pytest.mark.vcr()
def test_summarize_document():
    result = summarize("Long document text here...")
    assert len(result) < 200
    assert "key points" in result.lower()
```

Running with `--record-mode=new_episodes` hits the real API and saves the cassette. Future runs skip the network entirely. The cassette file goes into version control, so the team shares reproducible fixtures automatically.

One critical security note: VCR cassettes contain the full request and response, including authorization headers. Override the default config to redact credentials before committing:

```python
@pytest.fixture(scope="module")
def vcr_config():
    return {"filter_headers": ["authorization", "x-api-key"]}
```

## Technique 3: Network-Level Mocks

When you want to test without touching test code at all — for example, in end-to-end local development with a frontend team — a network-level mock server is the right tool. WireMock's MockGPT exposes a drop-in replacement for the OpenAI API at `https://mockgpt.wiremockapi.cloud/v1`. Point your `OPENAI_BASE_URL` environment variable there and your entire application stack runs without any API credentials or costs.

This approach is particularly useful for:

- Frontend developers who need a running backend with realistic AI responses
- QA engineers writing Playwright or Cypress tests against a full stack
- Chaos engineering: configuring the mock to return errors, delays, or malformed responses to test your application's error handling

MockLLM and similar local mock servers serve the same purpose for self-hosted scenarios. A local Docker container exposing an OpenAI-compatible API gives your team a fully air-gapped development environment with zero ongoing cost.

## Technique 4: Parameterized Edge Cases with Faker

For testing how your application handles the _variety_ of real LLM outputs — verbose responses, terse responses, JSON with missing fields, responses in unexpected languages — parameterized mocks with a fake data library give you breadth without recording hundreds of cassettes:

```python
import pytest
from faker import Faker

fake = Faker()

@pytest.mark.parametrize("response", [
    "",                            # Empty response
    fake.paragraph(nb_sentences=1),  # Very short
    fake.paragraph(nb_sentences=20), # Very long
    '{"key": "value"}',            # Valid JSON
    '{"key":',                     # Truncated JSON
])
def test_response_parser_handles_edge_cases(response):
    result = parse_llm_response(response)
    assert result is not None  # Should never raise
```

This catches parsing failures and unhandled exceptions without a single real API call.

## Wiring Mocks into CI/CD

The practical rule: no live LLM calls in CI unless the test is specifically an evaluation run. Structure your test suite in layers:

- **Unit tests** (always mocked): test prompt formatting, response parsing, retry logic, error handling
- **Integration tests** (VCR cassettes): test the full request-response cycle against recorded real output
- **Evaluation runs** (live, scheduled separately): assess output quality using frameworks like DeepEval or Promptfoo

DeepEval integrates with pytest and can run evaluation metrics in the same CI infrastructure you already use. Promptfoo offers declarative YAML-based test configs and native CI/CD integration for running regression suites against prompt changes. Both allow you to gate deployments on quality thresholds — fail the pipeline if answer relevance drops below 0.8.

Keep evaluation runs on a schedule (nightly or per release) rather than per pull request. They're expensive and slow by design; they're not a substitute for fast mock-based unit tests.

## Beyond Mocking: Golden Datasets

Mocks verify that your _code_ behaves correctly given a controlled input. They can't tell you whether your _prompt_ produces good outputs. That's where golden datasets come in.

A golden dataset is a curated set of input/expected-output pairs representing the behaviors your application must get right. Each entry contains a question, the ideal answer characteristics, and sometimes explicit negative examples. Teams typically build these from real user interactions (with privacy considerations) or from domain expert curation.

Evaluation against a golden dataset runs outside the normal test suite: feed each input through your real LLM, score the output with automated metrics or an LLM judge, and track scores over time. Score drops between versions are your signal that a model update or prompt change degraded behavior.

The two roles complement each other cleanly: mocks keep your test suite fast and your CI costs predictable; golden dataset evaluations tell you whether the actual model behavior is moving in the right direction.

## Practical Starting Point

If you're just getting started, apply mocks in this order of priority:

1. **Swap the LLM client in unit tests immediately** — eliminates cost and flakiness from the entire unit test layer overnight
2. **Add VCR cassettes to integration tests** — gives you real response structures without live network calls
3. **Set up a mock server for local full-stack development** — unblocks frontend and QA work from the LLM integration timeline
4. **Build a small golden dataset for your most critical flows** — gives you a quality regression signal as the application evolves

Mocking is not a compromise on test quality. It's the correct boundary between testing your application logic and evaluating your AI system. Conflating the two leads to either expensive, flaky tests or blind spots in coverage. Keep them separate and you get both fast, reliable CI and meaningful quality signals — which is the actual goal.

On this page

</details>

</research_source>

<research_source type="scraped_from_research" phase="exploitation" file="kinde-ci-cd-for-evals-running-prompt-agent-regression-tests-.md">
<details>
<summary>kinde-ci-cd-for-evals-running-prompt-agent-regression-tests-</summary>

Phase: [EXPLOITATION]

**Source URL:** <https://kinde.com/learn/ai-for-software-engineering/ai-devops/ci-cd-for-evals-running-prompt-and-agent-regression-tests-in-github-actions>

## What is CI/CD for AI Evals?

CI/CD for AI evals is the practice of automatically testing your AI prompts, models, and agents within your continuous integration and continuous delivery pipeline. It extends the familiar “code, test, deploy” loop to AI development, ensuring that any change to a prompt or agent doesn’t just work, but works correctly, consistently, and within budget before it ever reaches users.

Unlike traditional software testing where a function with the same input reliably produces the same output, LLM-based systems can be non-deterministic. An “eval” (evaluation) is a specialized test that assesses the quality, safety, and performance of an AI’s output, creating a critical safety net against regressions.

## How Does Automated AI Evaluation Work?

Automated AI evaluation integrates directly into your version control system, like GitHub, and runs a series of checks whenever a developer proposes a change. By adding this workflow to your pull requests, you create a merge-blocking gate that prevents quality degradation.

The process typically follows these steps:

1.  **Trigger**: A developer opens a pull request with a modified prompt or agent configuration.
2.  **CI Job Starts**: A platform like GitHub Actions automatically initiates a new workflow.
3.  **Run Evals**: The workflow executes a script that runs the new AI configuration against a predefined “golden dataset” of inputs.
4.  **Assert on Outputs**: The script compares the AI’s outputs against a set of assertions. These can include:

    -   **Deterministic checks**: Does the output contain a required keyword? Is it valid JSON? Does it follow a specific format?
    -   **Semantic checks**: Does the output’s meaning align with the expected answer? This often involves using another LLM to “grade” the result.
    -   **Safety checks**: Does the output contain harmful content or leak private information?
5.  **Check Performance Budgets**: The workflow analyzes the cost (token usage) and latency of the AI’s responses, failing the check if they exceed preset budgets.
6.  **Report Status**: The results are reported back to the pull request as a “pass” or “fail” status. A failing check blocks the merge, prompting the developer to revise their changes.

This automated loop ensures every change is rigorously vetted, allowing your team to iterate quickly and confidently.

## Why Integrate Evals into Your CI/CD Pipeline?

Integrating evals into your CI/CD pipeline shifts quality control from a manual, post-deployment headache to an automated, proactive process. It’s about building a system that self-regulates quality, performance, and cost.

The key benefits of this approach are:

-   **Preventing regressions**: The primary goal is to catch issues early. An eval suite ensures that a prompt optimized for one use case doesn’t inadvertently break five others.
-   **Controlling costs**: LLM APIs are priced by the token. A small change to a prompt can have a huge impact on cost. Automated checks can flag a change that, for example, doubles the average token usage, preventing budget overruns.
-   **Enforcing consistency**: Ensure the AI’s tone, style, and output structure remain consistent and on-brand across all interactions.
-   **Improving developer velocity**: When developers trust the test suite to catch regressions, they can experiment and innovate more freely without fear of breaking the build.
-   **Objective quality measurement**: Evals provide a concrete, objective measure of quality that can be tracked over time, replacing subjective manual checks with data-driven insights.

## Best Practices for Implementing CI/CD for Evals

Getting started with CI/CD for evals doesn’t have to be complicated. You can build a robust system using popular, CLI-friendly tools and a simple workflow configuration.

### Start with a Golden Dataset

A golden dataset is a curated collection of inputs and their ideal outputs or evaluation criteria. This is the foundation of your regression testing. Start small with 10-20 high-priority examples that cover your most critical use cases and common edge cases. Store this dataset as a CSV or JSON file in your repository.

### Create a Simple CLI Command

To ensure consistency between local development and CI, create a single command to run your evals. Many open-source tools (like `promptfoo`, `llm-test`, or `lunary`) can be configured to run from the command line.

For example, your `package.json` might contain a script like this:

```json
{
    "scripts": {
        "test:evals": "promptfoo eval -c ./promptfoo.config.yaml"
    }
}
```

This allows a developer to run `npm run test:evals` on their machine to validate changes before pushing.

### Set Up a GitHub Actions Workflow

Now, use that same command in a GitHub Actions workflow to automate the process. Create a file named `.github/workflows/evals.yml` with the following configuration. This workflow triggers on every pull request, checks out the code, and runs the eval script.

```yaml
# .github/workflows/evals.yml

name: "Run AI Evals"

on:
    pull_request:
        paths:
            - "prompts/**" # Reruns if a prompt file changes
            - "promptfoo.config.yaml" # Reruns if the eval config changes

jobs:
    evaluate:
        runs-on: ubuntu-latest
        steps:
            - name: "Checkout code"
              uses: actions/checkout@v4

            - name: "Set up Node.js"
              uses: actions/setup-node@v4
              with:
                  node-version: "20"

            - name: "Install dependencies"
              run: npm install

            - name: "Run prompt evaluations"
              id: prompt_eval
              env:
                  # Securely access your LLM API key
                  OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}
              run: npm run test:evals

            # You can add more steps here to, for example,
            # post a comment to the PR with the results summary.
```

This simple setup turns your evaluation suite into a powerful merge-blocking gate.

### Triage Flaky Tests

LLMs can be non-deterministic, which can lead to “flaky” tests that sometimes pass and sometimes fail without any code changes. To manage this, set the `temperature` parameter of your LLM to `0` for tests that require deterministic, factual outputs. For tests that assess semantic meaning or style, use model-graded assertions that are more flexible than exact-match comparisons.

## How Kinde Helps

Building a reliable, production-grade AI application requires excellence on two fronts: the quality of the AI itself and the security of the user-facing application. While you focus on implementing robust CI/CD pipelines to ensure AI quality and prevent regressions, Kinde provides the critical infrastructure for secure authentication, user management, and authorization.

By handling the complexities of user sign-up, sign-in, and permissions, Kinde lets your team focus on the core AI functionality. For instance, you could use Kinde’s feature flags to roll out a newly-tested AI agent to a specific subset of users, confident that your automated evals have already vetted its quality. This combination allows you to build sophisticated, secure AI products faster and with greater confidence.

For more on how to manage application features and user access, see the Kinde docs.

## Kinde Doc References

-   [Manage feature flags](https://docs.kinde.com/releases/feature-flags/manage-feature-flags/)
-   [Manage roles](https://docs.kinde.com/manage-users/roles-and-permissions/user-roles/)
-   [Manage users](https://docs.kinde.com/manage-users/about/)

</details>

</research_source>

<research_source type="scraped_from_research" phase="exploitation" file="non-deterministic-systems-guild-ai.md">
<details>
<summary>Non-Deterministic Systems</summary>

Phase: [EXPLOITATION]

**Source URL:** <https://www.guild.ai/glossary/non-deterministic-systems>

# Non-Deterministic Systems

https://www.guild.ai/_next/image?url=%2Fimages%2Farticles%2Fauthor.png&w=64&q=100

Guild.ai team

Feb 23, 2026

5 min read

## Key Takeaways

- Non-deterministic systems produce different outputs from the same inputs across runs, making traditional testing, debugging, and compliance fundamentally harder than with deterministic software.
- LLMs are non-deterministic even at temperature=0 due to floating-point arithmetic, GPU parallelism, Mixture-of-Experts routing, and batch-level dependencies — no major provider guarantees fully deterministic outputs.
- Non-determinism enables the flexibility and adaptability that make AI agents useful, but introduces risks around reproducibility, auditability, and trust that engineering teams must actively manage.
- Traditional QA breaks down because it assumes input X always produces output Y — testing non-deterministic AI agents requires probabilistic validation, behavioral bounds, and goal-driven evaluation.
- Only 21.1% of LLM-based code generation research papers account for non-determinism in their experiments, exposing a widespread validity gap in how the industry evaluates AI systems.
- Governance, observability, and structured guardrails are essential for deploying non-deterministic systems in production without exposing organizations to uncontrolled risk.

## What Are Non-Deterministic Systems?

A non-deterministic system is a system that can produce different outputs from the same input under identical conditions, meaning its behavior is not fully prescribed by its specification and cannot be exactly repeated across runs. Non-deterministic software, by its very nature, can produce different outputs for the same input under seemingly identical conditions.

In classical computing, non-determinism has roots in [concurrency](https://slikts.github.io/concurrency-glossary/?id=nondeterministic-vs-deterministic), distributed systems, and theoretical computer science — as [Wikipedia's entry on nondeterministic algorithms](https://en.wikipedia.org/wiki/Nondeterministic_algorithm) documents. But the term has taken on urgent new meaning with the rise of LLM-powered AI agents. Generative AI has sparked a significant shift in the technological landscape by introducing a new non-deterministic element to modern computing.

Think of it this way: a deterministic system is like a vending machine — insert the same coins, press the same button, get the same product every time. A non-deterministic system is more like asking a skilled engineer to solve a problem. They'll produce a valid solution, but it might differ each time in approach, phrasing, or structure. The answer might be equally correct, but it won't be identical.

As [Salesforce explains in their guide to agentic AI design](https://www.salesforce.com/blog/deterministic-ai/?bc=OTH), in the world of agentic systems, behavior falls along a spectrum from deterministic AI to non-deterministic AI. Non-deterministic AI behavior equals flexibility — probabilistic, adaptive, and context-aware. The engineering challenge is knowing where on that spectrum your system should live.

## How Non-Deterministic Systems Work

### Sources of Non-Determinism in AI

Non-determinism in modern AI systems doesn't come from a single source. It emerges from multiple layers of the stack simultaneously.

**Token sampling.** LLMs predict probability distributions over tokens and sample from them. LLMs predict the probability of a word or token given the context. The randomness typically comes from the sampling methods used during text generation, such as top-k sampling or nucleus sampling. As a result, identical instructions or prompts can yield completely different responses.

**Floating-point non-associativity.** Even with temperature set to zero, GPU operations introduce variability. Deep learning frameworks often prioritize performance, sometimes at the expense of bit-for-bit reproducibility. Unless explicitly using deterministic algorithms, operations like matrix multiplication, convolution, or reduction can have nondeterministic implementations. Using atomic operations or multi-pass algorithms on GPU can yield slightly different results run-to-run.

**Mixture-of-Experts routing.** As explored in research covered by [Thinking Machines Lab](https://thinkingmachines.ai/blog/defeating-nondeterminism-in-llm-inference/), batch composition affects expert routing. When groups contain tokens from different sequences or inputs, these tokens often compete against each other for available spots in expert buffers. As a consequence, the model is no longer deterministic at the sequence-level, but only at the batch-level. Even if you submit the exact same input multiple times, you may receive different outputs depending on what other inputs are processed in the same batch.

**Infrastructure variability.** The precision used (FP32, FP16, BF16, etc.) also affects reproducibility. Lower precision has more rounding error and thus more potential variability. If an LLM service switches hardware or uses a mix of hardware, the floating-point behavior might not be identical.

### The Temperature=0 Misconception

Many engineers assume setting temperature to zero makes their LLM calls deterministic. It doesn't. OpenAI states that their API can only be "mostly deterministic" irrespective of the value of the temperature parameter. They've added a seed parameter that improves reproducibility but still doesn't guarantee identical outputs due to system updates and load balancing across different hardware. It's a "best effort" kind of situation.

With the shift to LLM-first AI agents, that predictability disappears. Large Language Models introduce non-determinism, meaning the same input can generate an infinite number of responses, many of which could be valid (even with temperature set to 0). This makes AI agents far more natural and capable — but it also breaks the assumptions that traditional testing and evaluation rely on.

Research published on [arXiv](https://arxiv.org/html/2408.04667v5) quantified this directly: they demonstrated an alarming degree of variation across equivalent input runs with a varied collection of high performing LLMs under presumed deterministic settings. Their findings suggest there is far too much uncertainty in a realm where robust engineering is the expectation.

## Why Non-Deterministic Systems Matter

Non-determinism isn't a bug — it's a fundamental property of the systems engineering teams are now building on. The dual nature of non-determinism in generative AI unleashes creativity and adaptability in complex environments while navigating the challenges of unpredictability and consistency.

The scale of adoption makes this urgent. According to [Stanford's 2025 AI Index Report](https://hai.stanford.edu/ai-index/2025-ai-index-report), 78% of organizations reported using AI in 2024, up from 55% the year before. That means non-deterministic behavior is now embedded in production systems across most enterprises — whether they've accounted for it or not.

For engineering teams deploying AI agents, non-determinism touches every operational concern:

- **Debugging becomes probabilistic.** When an LLM produces inconsistent outputs, it becomes nearly impossible to debug problems effectively. If a model generates an incorrect or harmful response, engineers cannot reliably reproduce the issue. This makes it extraordinarily difficult to identify whether the problem stems from the model itself, the prompt engineering, the data, or some other factor. Debugging becomes a game of chance rather than a systematic process of elimination.
- **Compliance requires auditability.** Beyond debugging, reproducibility is critical for auditing and verification. Regulatory bodies, compliance officers, and security teams need to understand how AI systems make decisions.
- **Benchmarks lose meaning.** Non-determinism introduces noise into benchmarks, making it difficult to determine whether performance differences are real or artifacts of randomness.

The industry's response? As a [Comet.com guide to agentic systems](https://www.comet.com/site/blog/ai-agents/) puts it, there's a tension in software engineering between the desire for predictable, deterministic systems and the powerful but unreliable non-determinism of LLM-driven intelligence. That tension defines the engineering challenge of this era.

## Non-Deterministic Systems in Practice

### AI Agents in Production

The core of production challenges stems from the agent's autonomous and non-deterministic nature, which can deviate from original intent in unpredictable ways. This is "agentic drift" — the inevitable divergence between what you designed the agent to do and what it actually does in production.

Consider a code review agent triggered on pull requests. Run it twice on the same diff, and it might flag different issues, suggest different refactors, or phrase feedback differently. The reviews might both be valid — but your CI pipeline needs to produce consistent pass/fail signals.

### Testing Non-Deterministic AI

Traditional QA assumes deterministic behavior. Traditional quality assurance assumes deterministic behavior — given input X, you always get output Y. That model breaks completely with AI agents.

As [Datagrid's testing framework guide](https://datagrid.com/blog/4-frameworks-test-non-deterministic-ai-agents) explains, modern AI testing requires five key shifts: embrace probabilistic validation instead of exact output matching, monitor behavior over time rather than single-point verification, measure behavioral bounds instead of deterministic correctness, incorporate human judgment where automated testing reaches its limits, and validate reasoning processes alongside functional outcomes.

### Hybrid Deterministic/Non-Deterministic Architectures

The smartest production architectures don't try to eliminate non-determinism — they contain it. You want the best of both worlds — an agent that's helpful and conversational up front, but transitions to predictable processes to finish. A deployment agent might use an LLM to interpret intent (non-deterministic) but execute the actual deployment through a deterministic pipeline with strict guardrails.

## Key Considerations

### Reproducibility Is Not Guaranteed

No major provider currently promises fully deterministic outputs for their generative models. It's generally understood as a limitation of today's LLM technology. Engineers should design systems to tolerate minor output variations rather than expecting bit-perfect determinism.

### Testing Requires New Frameworks

Chaos engineering can be applied to testing non-deterministic systems. You can deliberately introduce failures and perturbations into a system to test its resilience and identify potential issues before they occur in production — randomly terminate instances, simulate network latency, or inject errors into data streams. By systematically introducing chaos in a controlled environment, you uncover weaknesses that might not be apparent under normal testing conditions.

### Non-Determinism Creates Security Exposure

Self-directed behavior in advanced agents introduces risks of uncontrolled operations, explainability, and auditability, and makes it difficult to maintain predictable security boundaries. These capabilities transform security from a boundary problem to a continuous monitoring and control challenge. An agent that behaves differently on every run is harder to threat-model than a deterministic workflow.

### The Validity Gap in Research

To understand how the literature handles the non-determinism threat, researchers collected 76 LLM-based code generation papers that appeared in the last 2 years. Only 21.1% of these papers consider the non-determinism threat in their experiments. These results highlight that there is currently a significant threat to the validity of scientific conclusions. If you're evaluating agents based on published benchmarks, factor in this uncertainty.

### Over-Reliance on Deterministic Assumptions

For enterprise, unpredictability is a major drawback. Non-deterministic AI tends to produce [varying outcomes for the same input](https://shieldbase.ai/en/glossary/non-deterministic), making it unreliable for sensitive or customer-facing tasks. Teams must explicitly map which parts of their system require deterministic guarantees and which can tolerate variation — then architect accordingly.

What makes a system non-deterministic?

A system is non-deterministic when it can produce different outputs from the same input across separate runs. In AI, this stems from probabilistic token sampling, floating-point arithmetic on parallel hardware, Mixture-of-Experts routing, and batch-level dependencies. Even setting temperature to zero doesn't eliminate all sources of variability.

Is non-determinism in AI a bug or a feature?

Both. Non-determinism enables the flexibility, creativity, and adaptability that make LLM-powered agents useful for complex, open-ended tasks. But it also breaks traditional assumptions about testing, debugging, and auditability. The engineering challenge is containing non-determinism where consistency matters while preserving it where flexibility adds value.

How do you test non-deterministic AI agents?

Replace exact output matching with probabilistic validation. Measure behavioral bounds across multiple runs rather than checking single-point correctness. Use simulation-based testing, adversarial inputs, and goal-driven evaluation that checks whether the agent achieved the desired outcome — not whether it produced identical tokens.

Can you make an LLM fully deterministic?

In practice, no. Even with temperature=0 and fixed seeds, today's LLM infrastructure introduces variability through GPU kernel scheduling, floating-point precision, and Mixture-of-Experts routing. You can reduce variance, but fully eliminating it requires trade-offs in performance that most production systems cannot accept.

Why does non-determinism matter for enterprise compliance?

Regulators and auditors demand that automated decisions be explainable and consistent. When an AI agent produces different outputs on each run, reproducing and auditing its decision-making becomes extremely difficult. This is why production-grade agent infrastructure requires comprehensive logging, session traceability, and behavioral monitoring.

What is agentic drift?

Agentic drift describes the divergence between what you designed an AI agent to do and what it actually does in production. Because non-deterministic reasoning can lead agents down different paths each time, their behavior can gradually deviate from the original intent — especially as they interact with changing environments and real-world data.

</details>

</research_source>

<research_source type="scraped_from_research" phase="exploration" file="what-metrics-should-you-use-to-evaluate-ai-in-your-ci-cd-pip.md">
<details>
<summary>What Metrics Should You Use to Evaluate AI in Your CI/CD Pipeline? - Semaphore</summary>

Phase: [EXPLORATION]

**Source URL:** <https://semaphore.io/what-metrics-should-you-use-to-evaluate-ai-in-your-ci-cd-pipeline>

# What Metrics Should You Use to Evaluate AI in Your CI/CD Pipeline? - Semaphore

AI is increasingly being integrated into CI/CD pipelines. It can suggest pipeline changes, optimize test selection, detect flaky tests, generate YAML, or even assist with deployment decisions.

But before adopting AI-assisted CI/CD workflows, there’s a more important question:

How do you know if AI is actually improving your pipeline?

Without measurable outcomes, AI becomes another layer of complexity. This article outlines the key metrics engineering teams should track to determine whether AI assistance improves or degrades CI/CD performance.

## **Start With Baseline Metrics**

Before introducing AI into your CI/CD pipeline, establish a baseline.

Track these metrics over several weeks:

- Average build duration
- Median build duration
- 95th percentile build time
- Queue time
- Test failure rate
- Flaky test rate
- Deployment frequency
- Mean time to recovery (MTTR)

CI systems like Semaphore provide visibility into build timing and [test reporting](https://docs.semaphore.io/using-semaphore/tests/test-reports).

You cannot evaluate improvement without knowing your starting point.

## **Build Duration and Feedback Time**

One of the most common AI use cases in CI/CD is optimization, such as:

- Intelligent test selection
- Detecting impacted files
- Skipping redundant jobs
- Suggesting caching improvements

If AI is introduced for performance reasons, the primary metrics to track are:

- Pull request validation time
- Time from commit to first feedback
- End-to-end pipeline duration

A meaningful improvement should reduce median build time without increasing failure escape rate.

If build time decreases but post-merge failures increase, AI may be trading speed for reliability.

## **Test Reliability Metrics**

If AI is helping identify flaky tests or prioritizing test execution, measure:

- Flaky test frequency
- Re-run rate
- Test stability over time
- False negative rate

If AI-based test selection skips tests that should have run, you’ll see an increase in escaped defects or post-deployment failures.

Improved CI performance should not come at the cost of reduced confidence.

## **Failure Signal Quality**

AI-assisted pipelines often aim to improve signal quality by:

- Grouping similar failures
- Detecting root causes
- Suggesting fixes

Track:

- Time spent debugging CI failures
- Number of re-runs per failure
- Ratio of actionable vs non-actionable failures

If developers re-run builds frequently to “see if it passes,” AI is not improving signal quality.

## **Deployment Safety Metrics**

If AI influences deployment decisions, such as:

- Auto-rollback triggers
- Risk scoring pull requests
- Suggesting production promotions

Track:

- Deployment success rate
- Rollback frequency
- Mean time to recovery
- Incident frequency

AI should reduce incidents, not increase unpredictable rollbacks.

## **Human Trust and Adoption**

Quantitative metrics matter, but so does trust.

Watch for behavioral signals:

- Are developers bypassing AI suggestions?
- Are teams disabling AI features?
- Are builds being re-run more often?

If trust erodes, the system becomes noise.

AI in CI/CD should feel like assistance, not interference.

## **Guard Against False Confidence**

One of the biggest risks in AI-assisted CI/CD is false confidence.

For example:

- AI selects a subset of tests to run
- Build passes
- A regression appears in production

In this case, pipeline duration improves, but defect escape rate increases.

Always pair speed metrics with quality metrics.

Optimization without guardrails creates risk.

## **A Practical Evaluation Framework**

When introducing AI into CI/CD, use this simple approach:

1. Establish baseline metrics
2. Introduce AI assistance incrementally
3. Run controlled comparisons (A/B if possible)
4. Monitor performance and quality metrics simultaneously
5. Roll back if reliability degrades

Treat AI features like experimental infrastructure changes, not permanent upgrades.

## **When AI Actually Helps**

AI tends to provide the most value when:

- Pipelines are already well-instrumented
- Test suites are large and stable
- Flaky tests are actively tracked
- Baseline metrics are known

If your pipeline is unstable or poorly measured, AI may amplify problems instead of solving them.

## **Summary**

AI can improve CI/CD performance, but only if its impact is measured carefully.

Track build time, test reliability, deployment safety, and developer trust. Compare improvements against baseline metrics. Avoid trading reliability for speed.

AI in CI/CD should reduce friction and improve signal quality. If it increases uncertainty, it is not helping.

## **FAQ** s
**What is the most important metric when adding AI to CI/CD?**

Build duration is common, but it must be balanced with failure escape rate and deployment stability.

**Can AI reduce CI build times safely?**

Yes, but only if test coverage integrity is maintained and skipped tests do not increase defect leakage.

**How long should we measure before deciding?**

At least several weeks of baseline data before and after introducing AI assistance.

**Should AI control production deployments?**

Only with strong guardrails, clear rollback mechanisms, and continuous monitoring.

</details>

</research_source>

<golden_source type="guideline_code">
## Code Sources (from Article Guidelines)

<details>
<summary>Ruff pre-commit</summary>

# Ruff pre-commit

## Summary
Repository: astral-sh/ruff-pre-commit
Commit: 3b3f7c3f57fe9925356faf5fe6230835138be230
Files analyzed: 10

Estimated tokens: 5.8k

## File tree
```Directory structure:
└── astral-sh-ruff-pre-commit/
    ├── README.md
    ├── LICENSE-APACHE
    ├── LICENSE-MIT
    ├── mirror.py
    ├── pyproject.toml
    ├── .pre-commit-hooks.yaml
    └── .github/
        ├── dependabot.yml
        ├── ISSUE_TEMPLATE.md
        ├── PULL_REQUEST_TEMPLATE.md
        └── workflows/
            └── main.yml

```

## Extracted content
================================================
FILE: README.md
================================================
# ruff-pre-commit

[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![image](https://img.shields.io/pypi/v/ruff/0.15.17.svg)](https://pypi.python.org/pypi/ruff)
[![image](https://img.shields.io/pypi/l/ruff/0.15.17.svg)](https://pypi.python.org/pypi/ruff)
[![image](https://img.shields.io/pypi/pyversions/ruff/0.15.17.svg)](https://pypi.python.org/pypi/ruff)
[![Actions status](https://github.com/astral-sh/ruff-pre-commit/workflows/main/badge.svg)](https://github.com/astral-sh/ruff-pre-commit/actions)

A [pre-commit](https://pre-commit.com/) hook for [Ruff](https://github.com/astral-sh/ruff).

Distributed as a standalone repository to enable installing Ruff via prebuilt wheels from
[PyPI](https://pypi.org/project/ruff/).

### Using Ruff with pre-commit

To run Ruff's [linter](https://docs.astral.sh/ruff/linter) and [formatter](https://docs.astral.sh/ruff/formatter)
(available as of Ruff v0.0.289) via pre-commit, add the following to your `.pre-commit-config.yaml`:

```yaml
repos:
- repo: https://github.com/astral-sh/ruff-pre-commit
  # Ruff version.
  rev: v0.15.17
  hooks:
    # Run the linter.
    - id: ruff-check
    # Run the formatter.
    - id: ruff-format
```

To enable lint fixes, add the `--fix` argument to the lint hook:

```yaml
repos:
- repo: https://github.com/astral-sh/ruff-pre-commit
  # Ruff version.
  rev: v0.15.17
  hooks:
    # Run the linter.
    - id: ruff-check
      args: [ --fix ]
    # Run the formatter.
    - id: ruff-format
```

To select or ignore specific rules, pass the relevant Ruff arguments through `args`.
When using inline YAML lists, quote arguments that contain commas:

```yaml
repos:
- repo: https://github.com/astral-sh/ruff-pre-commit
  # Ruff version.
  rev: v0.15.17
  hooks:
    # Run the linter.
    - id: ruff-check
      args: [ --fix, "--extend-select=I,E", "--ignore=F401" ]
```

To avoid running on Jupyter Notebooks, remove `jupyter` from the list of allowed filetypes:

```yaml
repos:
- repo: https://github.com/astral-sh/ruff-pre-commit
  # Ruff version.
  rev: v0.15.17
  hooks:
    # Run the linter.
    - id: ruff-check
      types_or: [ python, pyi ]
      args: [ --fix ]
    # Run the formatter.
    - id: ruff-format
      types_or: [ python, pyi ]
```

To lint `pyproject.toml`, add `pyproject` to the list of allowed filetypes (requires `identify>=2.6.18`):

```yaml
repos:
- repo: https://github.com/astral-sh/ruff-pre-commit
  # Ruff version.
  rev: v0.15.17
  hooks:
    # Run the linter.
    - id: ruff-check
      types_or: [ python, pyi, jupyter, pyproject ]
      args: [ --fix ]
    # Run the formatter.
    - id: ruff-format
      types_or: [ python, pyi, jupyter ]
```

When running with `--fix`, Ruff's lint hook should be placed _before_ Ruff's formatter hook, and
_before_ Black, isort, and other formatting tools, as Ruff's fix behavior can output code changes
that require reformatting.

When running without `--fix`, Ruff's formatter hook can be placed before or after Ruff's lint hook.

(As long as your Ruff configuration avoids any [linter-formatter incompatibilities](https://docs.astral.sh/ruff/formatter/#conflicting-lint-rules),
`ruff format` should never introduce new lint errors, so it's safe to run Ruff's format hook _after_
`ruff check --fix`.)

### Using Ruff with prek

If you prefer using [prek](https://github.com/j178/prek) instead of
pre-commit, you can define a `prek.toml` file with your hooks. Here's an example
equivalent to the `.pre-commit-config.yaml` configuration:

```toml
[[repos]]
repo = "https://github.com/astral-sh/ruff-pre-commit"
rev = "v0.15.0" # Ruff version.
hooks = [
  # Run the linter.
  { id = "ruff-check", args = ["--fix"], types_or = ["python", "pyi"] },

  # Run the formatter.
  { id = "ruff-format", types_or = ["python", "pyi"] },
]
```

See the section above on pre-commit for guidance on hook order when using `--fix`.

## License

ruff-pre-commit is licensed under either of

- Apache License, Version 2.0, ([LICENSE-APACHE](LICENSE-APACHE) or <https://www.apache.org/licenses/LICENSE-2.0>)
- MIT license ([LICENSE-MIT](LICENSE-MIT) or <https://opensource.org/licenses/MIT>)

at your option.

Unless you explicitly state otherwise, any contribution intentionally submitted
for inclusion in ruff-pre-commit by you, as defined in the Apache-2.0 license, shall be
dually licensed as above, without any additional terms or conditions.

<div align="center">
  <a target="_blank" href="https://astral.sh" style="background:none">
    <img src="https://raw.githubusercontent.com/astral-sh/ruff/main/assets/svg/Astral.svg">
  </a>
</div>



================================================
FILE: LICENSE-APACHE
================================================

                                 Apache License
                           Version 2.0, January 2004
                        http://www.apache.org/licenses/

   TERMS AND CONDITIONS FOR USE, REPRODUCTION, AND DISTRIBUTION

   1. Definitions.

      "License" shall mean the terms and conditions for use, reproduction,
      and distribution as defined by Sections 1 through 9 of this document.

      "Licensor" shall mean the copyright owner or entity authorized by
      the copyright owner that is granting the License.

      "Legal Entity" shall mean the union of the acting entity and all
      other entities that control, are controlled by, or are under common
      control with that entity. For the purposes of this definition,
      "control" means (i) the power, direct or indirect, to cause the
      direction or management of such entity, whether by contract or
      otherwise, or (ii) ownership of fifty percent (50%) or more of the
      outstanding shares, or (iii) beneficial ownership of such entity.

      "You" (or "Your") shall mean an individual or Legal Entity
      exercising permissions granted by this License.

      "Source" form shall mean the preferred form for making modifications,
      including but not limited to software source code, documentation
      source, and configuration files.

      "Object" form shall mean any form resulting from mechanical
      transformation or translation of a Source form, including but
      not limited to compiled object code, generated documentation,
      and conversions to other media types.

      "Work" shall mean the work of authorship, whether in Source or
      Object form, made available under the License, as indicated by a
      copyright notice that is included in or attached to the work
      (an example is provided in the Appendix below).

      "Derivative Works" shall mean any work, whether in Source or Object
      form, that is based on (or derived from) the Work and for which the
      editorial revisions, annotations, elaborations, or other modifications
      represent, as a whole, an original work of authorship. For the purposes
      of this License, Derivative Works shall not include works that remain
      separable from, or merely link (or bind by name) to the interfaces of,
      the Work and Derivative Works thereof.

      "Contribution" shall mean any work of authorship, including
      the original version of the Work and any modifications or additions
      to that Work or Derivative Works thereof, that is intentionally
      submitted to Licensor for inclusion in the Work by the copyright owner
      or by an individual or Legal Entity authorized to submit on behalf of
      the copyright owner. For the purposes of this definition, "submitted"
      means any form of electronic, verbal, or written communication sent
      to the Licensor or its representatives, including but not limited to
      communication on electronic mailing lists, source code control systems,
      and issue tracking systems that are managed by, or on behalf of, the
      Licensor for the purpose of discussing and improving the Work, but
      excluding communication that is conspicuously marked or otherwise
      designated in writing by the copyright owner as "Not a Contribution."

      "Contributor" shall mean Licensor and any individual or Legal Entity
      on behalf of whom a Contribution has been received by Licensor and
      subsequently incorporated within the Work.

   2. Grant of Copyright License. Subject to the terms and conditions of
      this License, each Contributor hereby grants to You a perpetual,
      worldwide, non-exclusive, no-charge, royalty-free, irrevocable
      copyright license to reproduce, prepare Derivative Works of,
      publicly display, publicly perform, sublicense, and distribute the
      Work and such Derivative Works in Source or Object form.

   3. Grant of Patent License. Subject to the terms and conditions of
      this License, each Contributor hereby grants to You a perpetual,
      worldwide, non-exclusive, no-charge, royalty-free, irrevocable
      (except as stated in this section) patent license to make, have made,
      use, offer to sell, sell, import, and otherwise transfer the Work,
      where such license applies only to those patent claims licensable
      by such Contributor that are necessarily infringed by their
      Contribution(s) alone or by combination of their Contribution(s)
      with the Work to which such Contribution(s) was submitted. If You
      institute patent litigation against any entity (including a
      cross-claim or counterclaim in a lawsuit) alleging that the Work
      or a Contribution incorporated within the Work constitutes direct
      or contributory patent infringement, then any patent licenses
      granted to You under this License for that Work shall terminate
      as of the date such litigation is filed.

   4. Redistribution. You may reproduce and distribute copies of the
      Work or Derivative Works thereof in any medium, with or without
      modifications, and in Source or Object form, provided that You
      meet the following conditions:

      (a) You must give any other recipients of the Work or
          Derivative Works a copy of this License; and

      (b) You must cause any modified files to carry prominent notices
          stating that You changed the files; and

      (c) You must retain, in the Source form of any Derivative Works
          that You distribute, all copyright, patent, trademark, and
          attribution notices from the Source form of the Work,
          excluding those notices that do not pertain to any part of
          the Derivative Works; and

      (d) If the Work includes a "NOTICE" text file as part of its
          distribution, then any Derivative Works that You distribute must
          include a readable copy of the attribution notices contained
          within such NOTICE file, excluding those notices that do not
          pertain to any part of the Derivative Works, in at least one
          of the following places: within a NOTICE text file distributed
          as part of the Derivative Works; within the Source form or
          documentation, if provided along with the Derivative Works; or,
          within a display generated by the Derivative Works, if and
          wherever such third-party notices normally appear. The contents
          of the NOTICE file are for informational purposes only and
          do not modify the License. You may add Your own attribution
          notices within Derivative Works that You distribute, alongside
          or as an addendum to the NOTICE text from the Work, provided
          that such additional attribution notices cannot be construed
          as modifying the License.

      You may add Your own copyright statement to Your modifications and
      may provide additional or different license terms and conditions
      for use, reproduction, or distribution of Your modifications, or
      for any such Derivative Works as a whole, provided Your use,
      reproduction, and distribution of the Work otherwise complies with
      the conditions stated in this License.

   5. Submission of Contributions. Unless You explicitly state otherwise,
      any Contribution intentionally submitted for inclusion in the Work
      by You to the Licensor shall be under the terms and conditions of
      this License, without any additional terms or conditions.
      Notwithstanding the above, nothing herein shall supersede or modify
      the terms of any separate license agreement you may have executed
      with Licensor regarding such Contributions.

   6. Trademarks. This License does not grant permission to use the trade
      names, trademarks, service marks, or product names of the Licensor,
      except as required for reasonable and customary use in describing the
      origin of the Work and reproducing the content of the NOTICE file.

   7. Disclaimer of Warranty. Unless required by applicable law or
      agreed to in writing, Licensor provides the Work (and each
      Contributor provides its Contributions) on an "AS IS" BASIS,
      WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
      implied, including, without limitation, any warranties or conditions
      of TITLE, NON-INFRINGEMENT, MERCHANTABILITY, or FITNESS FOR A
      PARTICULAR PURPOSE. You are solely responsible for determining the
      appropriateness of using or redistributing the Work and assume any
      risks associated with Your exercise of permissions under this License.

   8. Limitation of Liability. In no event and under no legal theory,
      whether in tort (including negligence), contract, or otherwise,
      unless required by applicable law (such as deliberate and grossly
      negligent acts) or agreed to in writing, shall any Contributor be
      liable to You for damages, including any direct, indirect, special,
      incidental, or consequential damages of any character arising as a
      result of this License or out of the use or inability to use the
      Work (including but not limited to damages for loss of goodwill,
      work stoppage, computer failure or malfunction, or any and all
      other commercial damages or losses), even if such Contributor
      has been advised of the possibility of such damages.

   9. Accepting Warranty or Additional Liability. While redistributing
      the Work or Derivative Works thereof, You may choose to offer,
      and charge a fee for, acceptance of support, warranty, indemnity,
      or other liability obligations and/or rights consistent with this
      License. However, in accepting such obligations, You may act only
      on Your own behalf and on Your sole responsibility, not on behalf
      of any other Contributor, and only if You agree to indemnify,
      defend, and hold each Contributor harmless for any liability
      incurred by, or claims asserted against, such Contributor by reason
      of your accepting any such warranty or additional liability.

   END OF TERMS AND CONDITIONS

   APPENDIX: How to apply the Apache License to your work.

      To apply the Apache License to your work, attach the following
      boilerplate notice, with the fields enclosed by brackets "[]"
      replaced with your own identifying information. (Don't include
      the brackets!)  The text should be enclosed in the appropriate
      comment syntax for the file format. We also recommend that a
      file or class name and description of purpose be included on the
      same "printed page" as the copyright notice for easier
      identification within third-party archives.

   Copyright [yyyy] [name of copyright owner]

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.



================================================
FILE: LICENSE-MIT
================================================
MIT License

Copyright (c) 2024 Astral Software Inc.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.



================================================
FILE: mirror.py
================================================
# /// script
# requires-python = ">=3.12"
# dependencies = [
#   "packaging==23.1",
#   "urllib3==2.0.5",
# ]
# ///
"""Update ruff-pre-commit to the latest version of ruff."""

import re
import subprocess
import tomllib
import typing
from pathlib import Path

import urllib3
from packaging.requirements import Requirement
from packaging.version import Version


def main():
    with open(Path(__file__).parent / "pyproject.toml", "rb") as f:
        pyproject = tomllib.load(f)

    all_versions = get_all_versions()
    current_version = get_current_version(pyproject=pyproject)
    target_versions = [v for v in all_versions if v > current_version]

    for version in target_versions:
        paths = process_version(version)
        if subprocess.check_output(["git", "status", "-s"]).strip():
            subprocess.run(["git", "add", *paths], check=True)
            subprocess.run(["git", "commit", "-m", f"Mirror: {version}"], check=True)
            subprocess.run(["git", "tag", f"v{version}"], check=True)
        else:
            print(f"No change v{version}")


def get_all_versions() -> list[Version]:
    response = urllib3.request("GET", "https://pypi.org/pypi/ruff/json")
    if response.status != 200:
        raise RuntimeError("Failed to fetch versions from pypi")

    versions = [Version(release) for release in response.json()["releases"]]
    return sorted(versions)


def get_current_version(pyproject: dict) -> Version:
    requirements = [Requirement(d) for d in pyproject["project"]["dependencies"]]
    requirement = next((r for r in requirements if r.name == "ruff"), None)
    assert requirement is not None, "pyproject.toml does not have ruff requirement"

    specifiers = list(requirement.specifier)
    assert (
        len(specifiers) == 1 and specifiers[0].operator == "=="
    ), f"ruff's specifier should be exact matching, but `{requirement}`"

    return Version(specifiers[0].version)


def process_version(version: Version) -> typing.Sequence[str]:
    def replace_pyproject_toml(content: str) -> str:
        return re.sub(r'"ruff==.*"', f'"ruff=={version}"', content)

    def replace_readme_md(content: str) -> str:
        content = re.sub(r"rev: v\d+\.\d+\.\d+", f"rev: v{version}", content)
        return re.sub(r"/ruff/\d+\.\d+\.\d+\.svg", f"/ruff/{version}.svg", content)

    paths = {
        "pyproject.toml": replace_pyproject_toml,
        "README.md": replace_readme_md,
    }

    for path, replacer in paths.items():
        with open(path) as f:
            content = replacer(f.read())
        with open(path, mode="w") as f:
            f.write(content)

    return tuple(paths.keys())


if __name__ == "__main__":
    main()



================================================
FILE: pyproject.toml
================================================
[project]
name = "ruff-pre-commit"
version = "0.0.0"
dependencies = [
    "ruff==0.15.17",
]



================================================
FILE: .pre-commit-hooks.yaml
================================================
- id: ruff-check
  name: ruff check
  description: "Run 'ruff check' for extremely fast Python linting"
  entry: ruff check --force-exclude
  language: python
  types_or: [python, pyi, jupyter]
  args: []
  require_serial: true
  additional_dependencies: []
  minimum_pre_commit_version: "2.9.2"

- id: ruff-format
  name: ruff format
  description: "Run 'ruff format' for extremely fast Python formatting"
  entry: ruff format --force-exclude
  language: python
  types_or: [python, pyi, jupyter]
  args: []
  require_serial: true
  additional_dependencies: []
  minimum_pre_commit_version: "2.9.2"

# Legacy alias
- id: ruff
  name: ruff (legacy alias)
  description: "Run 'ruff check' for extremely fast Python linting"
  entry: ruff check --force-exclude
  language: python
  types_or: [python, pyi, jupyter]
  args: []
  require_serial: true
  additional_dependencies: []
  minimum_pre_commit_version: "2.9.2"



================================================
FILE: .github/dependabot.yml
================================================
version: 2
updates:
  - package-ecosystem: github-actions
    directory: /
    schedule:
      interval: weekly
    groups:
      github-actions:
        patterns:
          - "*"
    cooldown:
      default-days: 7



================================================
FILE: .github/ISSUE_TEMPLATE.md
================================================
<!--
Thank you for taking the time to report an issue! We're glad to have you involved with Ruff.

If you're filing a bug report, please consider including the following information:

* A minimal code snippet that reproduces the bug.
* The current Ruff settings (any relevant sections from your `pyproject.toml`).
* The current Ruff version (`ruff --version`).
* A description of your environment (e.g., operating system, Python version, etc.).
-->



================================================
FILE: .github/PULL_REQUEST_TEMPLATE.md
================================================
<!--
Thank you for contributing to Ruff! To help us out with reviewing, please consider the following:

- Does this pull request include a summary of the change? (See below.)
- Does this pull request include a descriptive title?
- Does this pull request include references to any relevant issues?
-->

## Summary

<!-- What's the purpose of the change? What does it do, and why? -->

## Test Plan

<!-- How was it tested? -->



================================================
FILE: .github/workflows/main.yml
================================================
name: main
on:
  schedule:
    - cron: "0 */4 * * *"
  workflow_dispatch:

permissions: {}

jobs:
  build:
    name: main
    runs-on: ubuntu-latest
    permissions:
      contents: write
    steps:
      - uses: actions/checkout@df4cb1c069e1874edd31b4311f1884172cec0e10 # v6.0.3
        with:
          persist-credentials: true # needed to push commits below

      - name: Install uv
        uses: astral-sh/setup-uv@fac544c07dec837d0ccb6301d7b5580bf5edae39 # v8.2.0

      - name: set git config
        run: |
          git config user.name "$GITHUB_ACTOR"
          git config user.email "$GITHUB_ACTOR@users.noreply.github.com"

      - run: uv run --no-project mirror.py

      - name: check for unpushed commits
        id: check_unpushed
        run: |
          UNPUSHED_COMMITS=$(git log origin/main..HEAD)
          if [ -z "$UNPUSHED_COMMITS" ]; then
            echo "No unpushed commits found."
            echo "changes_exist=false" >> "$GITHUB_ENV"
          else
            echo "Unpushed commits found."
            echo "changes_exist=true" >> "$GITHUB_ENV"
          fi

      - name: push changes if they exist
        if: env.changes_exist == 'true'
        run: |
          git push origin HEAD:refs/heads/main
          git push origin HEAD:refs/heads/main --tags

      - name: create release on new tag if new changes exist
        if: env.changes_exist == 'true'
        run: |
          TAG_NAME=$(git describe --tags "$(git rev-list --tags --max-count=1)")
          echo "$TAG_NAME"
          gh release create "$TAG_NAME" \
            --title "$TAG_NAME" \
            --notes "See: https://github.com/astral-sh/ruff/releases/tag/${TAG_NAME/v}" \
            --latest
        env:
          GH_TOKEN: ${{ secrets.GITHUB_TOKEN }}

</details>

<details>
<summary>Notebook 1</summary>

# Notebook 1

## Summary
Repository: towardsai/agentic-ai-engineering-course
Commit: 8c8a1150c28d2639171eb63e7e39d57df29c6d34
Subpath: /lessons/31_continuous_integration
Files analyzed: 1

Estimated tokens: 23.8k

## File tree
```Directory structure:
└── 31_continuous_integration/
    └── notebook.ipynb

```

## Extracted content
================================================
FILE: lessons/31_continuous_integration/notebook.ipynb
================================================
# Jupyter notebook converted to Python script.

"""
<a href="https://colab.research.google.com/github/towardsai/agentic-ai-engineering-course/blob/main/lessons/31_continuous_integration/notebook.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

# Lesson 31: Continuous Integration (CI) for AI Engineering

In this notebook, we'll practice the CI essentials covered in Lesson 31. You'll run formatting checks, linting, and tests to see how CI tools maintain code quality.

**Learning Objectives:**

- Understand Brown's CI configuration files
- Practice running formatting and linting checks with Ruff
- Learn to fix code quality issues automatically
- Run unit tests with mocked LLM responses
"""

"""
## 1. Setup

"""

"""
### Set Up Python Environment

**Google Colab:** Run the code cell below — it installs all required packages.

To set up your Python virtual environment using `uv` and load it into the Notebook, follow the step-by-step instructions from the `Course Admin` lesson from the beginning of the course.

**TL;DR:** Be sure the correct kernel pointing to your `uv` virtual environment is selected.

"""

# ============================================================
# Google Colab Setup — runs only when executed in Colab
# ============================================================
import sys

IN_COLAB = "google.colab" in sys.modules

if IN_COLAB:
    import importlib
    import os
    import site
    import subprocess

    # Install the course package (published from pyproject.toml)
    subprocess.run(
        [
            sys.executable,
            "-m",
            "pip",
            "install",
            "-q",
            "-U",
            "agentic-ai-engineering-course==0.4.8",
        ],
        check=True,
    )
    importlib.reload(site)  # make newly installed packages importable without restart

    from google.colab import userdata

    os.environ["OPIK_API_KEY"] = userdata.get("OPIK_API_KEY")

if not IN_COLAB:
    get_ipython().run_line_magic("load_ext", "autoreload")
    get_ipython().run_line_magic("autoreload", "2")

    from utils import env

    env.load(required_env_vars=["OPIK_API_KEY"])

import os

if IN_COLAB:
    import writing_workflow

    %cd {list(writing_workflow.__path__)[0]}
else:
    %cd ../writing_workflow
# Output:
#   /Users/jai/Documents/code-repo/agentic-ai-engineering-course/lessons/writing_workflow


"""
## 2. Viewing Brown's CI Configuration

Let's examine Brown's actual CI configuration files to understand how CI is set up.
"""

"""
### 2.1 Pre-commit Configuration

The `.pre-commit-config.yaml` file defines Git hooks that run automatically before each commit. These hooks catch issues immediately in your local development environment.

Brown's pre-commit configuration includes three types of hooks:
1. **validate-pyproject** - Validates that `pyproject.toml` is structurally correct
2. **prettier** - Formats YAML and JSON configuration files consistently
3. **ruff-check** and **ruff-format** - Lints and formats Python code
"""

# Show the content of the file
!cat .pre-commit-config.yaml
# Output:
#   fail_fast: false

#   

#   repos:

#     - repo: https://github.com/abravalheri/validate-pyproject

#       rev: v0.24.1

#       hooks:

#         - id: validate-pyproject

#   

#     - repo: https://github.com/pre-commit/mirrors-prettier

#       rev: v3.1.0

#       hooks:

#         - id: prettier

#           types_or: [yaml, json5]

#   

#     - repo: https://github.com/astral-sh/ruff-pre-commit

#       # Ruff version. Keep in sync with the CI workflows (.github/workflows/*.yml).

#       rev: v0.14.6

#       hooks:

#         # Run the linter.

#         - id: ruff-check

#           args: [--fix, --exit-non-zero-on-fix]

#         # Run the formatter.

#         - id: ruff-format


"""
### 2.2 Ruff Configuration

The `pyproject.toml` file contains Ruff's configuration in the `[tool.ruff]` section. This defines:
- **target-version**: Which Python version to target (py312 for Python 3.12)
- **line-length**: Maximum line length (140 characters for modern screens)
- **select rules**: Which linting rules to enable (F=Pyflakes, E=pycodestyle, I=isort)
- **known-first-party**: How to group imports correctly
"""

# Show the content of the file related to ruff
!grep -A 20 "\[tool.ruff\]" pyproject.toml
# Output:
#   [tool.ruff]

#   target-version = "py312"

#   line-length = 140

#   

#   [tool.ruff.lint]

#   select = [

#       "F",    # Pyflakes

#       "E",    # pycodestyle errors

#       "I",    # isort

#   ]

#   

#   [tool.ruff.lint.isort]

#   known-first-party = ["src", "tests"]

#   

#   [tool.pytest.ini_options]

#   pythonpath = ["src"]

#   markers = [

#       "integration: end-to-end workflow tests (mocked LLMs, no network). Select with `-m integration` or skip with `-m 'not integration'`.",

#   ]


"""
### 2.3 Makefile QA Targets

The Makefile provides convenient shortcuts for running CI commands. Instead of typing long `uv run ruff format --check src/ tests/ scripts/` commands, you can simply run `make format-check`.

The Makefile defines:
- **QA_FOLDERS** - Which directories to check (src/, tests/, scripts/)
- **format-check/format-fix** - Formatting commands
- **lint-check/lint-fix** - Linting commands
- **tests** - Test suite with the correct configuration
- **pre-commit** - Manual pre-commit hook execution
"""

# Show the commands in the Makefile related to QA
!sed -n '/# --- Tests & QA ---/,$p' Makefile | tail -n +2
# Output:
#   

#   tests: # Run tests.

#   	CONFIG_FILE=configs/debug.yaml uv run pytest

#   

#   pre-commit: # Run pre-commit hooks.

#   	uv run pre-commit run --all-files

#   

#   format-fix: # Auto-format Python code using ruff formatter.

#   	uv run ruff format $(QA_FOLDERS)

#   

#   lint-fix: # Auto-fix linting issues using ruff linter.

#   	uv run ruff check --fix $(QA_FOLDERS)

#   

#   format-check: # Check code formatting without making changes using ruff formatter.

#   	uv run ruff format --check $(QA_FOLDERS) 

#   

#   lint-check: # Check code for linting issues without fixing them using ruff linter.

#   	uv run ruff check $(QA_FOLDERS)


"""
## 3. Pre-commit Hooks (Local Enforcement)

Pre-commit hooks run automatically before each commit, catching issues before they enter version control.

> **If running from Colab:** the installed package isn't a git repository, but `pre-commit` requires one — we initialize it as a git repo first.

Let's run them manually:
"""

if IN_COLAB:
    !git init

!uv run pre-commit run --files ./**/*
# Output:
#   [1m[33mwarning[39m[0m[1m:[0m [1m`VIRTUAL_ENV=/Users/jai/Documents/code-repo/agentic-ai-engineering-course/.venv` does not match the project environment path `.venv` and will be ignored; use `--active` to target the active environment instead[0m

#   Validate pyproject.toml..............................(no files to check)[46;30mSkipped[m

#   prettier.................................................................[42mPassed[m

#   ruff check...............................................................[42mPassed[m

#   ruff format..............................................................[42mPassed[m


"""
These hooks will:
1. Validate your `pyproject.toml` structure
2. Format all YAML/JSON files with prettier
3. Lint Python code with ruff-check (and auto-fix issues)
4. Format Python code with ruff-format

If any hook fails, you'll see the error, fix it, re-stage the files, and commit again. This tight feedback loop keeps code quality high.

"""

"""
## 4. Running Formatting Checks

Now let's practice using Ruff's formatter. Instead of running it on Brown's existing code (which is already formatted), we'll create a simple Python file with formatting issues and fix them.
"""

"""
### 4.1 Create a Test File with Formatting Issues
"""

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
# Output:
#   Created test_formatting.py


"""
### 4.2 Check Formatting (Without Fixing)

Let's check if the file has formatting issues without modifying it:
"""

!uv run ruff format --check test_formatting.py
# Output:
#   [1m[33mwarning[39m[0m[1m:[0m [1m`VIRTUAL_ENV=/Users/jai/Documents/code-repo/agentic-ai-engineering-course/.venv` does not match the project environment path `.venv` and will be ignored; use `--active` to target the active environment instead[0m

#   Would reformat: [1mtest_formatting.py[0m

#   1 file would be reformatted


"""
You'll see that Ruff reports the file would be reformatted. The `--check` flag means Ruff only reports issues without changing the file.
"""

"""
### 4.3 Auto-fix Formatting Issues

Now let's fix all the formatting issues automatically:
"""

!uv run ruff format test_formatting.py
# Output:
#   [1m[33mwarning[39m[0m[1m:[0m [1m`VIRTUAL_ENV=/Users/jai/Documents/code-repo/agentic-ai-engineering-course/.venv` does not match the project environment path `.venv` and will be ignored; use `--active` to target the active environment instead[0m

#   1 file reformatted


"""
Ruff will reformat the file to follow consistent style rules. Let's see the result:
"""

!cat test_formatting.py
# Output:
#   # This file has formatting issues

#   def badly_formatted_function(x, y, z):

#       result = x + y + z

#       my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#       my_dict = {"key1": "value1", "key2": "value2", "key3": "value3"}

#       if result > 10:

#           print("Result is greater than 10")

#       else:

#           print("Result is 10 or less")

#       return result

#   

#   

#   class BadlyFormattedClass:

#       def __init__(self, name, age):

#           self.name = name

#           self.age = age

#   

#       def get_info(self):

#           return f"{self.name} is {self.age} years old"


"""
Notice how Ruff has:
- Fixed spacing around operators (`x+y+z` → `x + y + z`)
- Added proper spacing in function signatures
- Formatted lists and dictionaries consistently
- Fixed class definition spacing

Let's remove the file now:
"""

!rm test_formatting.py

"""
## 5. Running Linting Checks

Linting goes beyond formatting—it checks for bugs, code quality issues, and best practices. Let's create a file with linting issues and fix them.
"""

"""
### 5.1 Create a Test File with Linting Issues
"""

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
# Output:
#   Created test_linting.py


"""
### 5.2 Check Linting Issues (Without Fixing)
"""

!uv run ruff check test_linting.py
# Output:
#   [1m[33mwarning[39m[0m[1m:[0m [1m`VIRTUAL_ENV=/Users/jai/Documents/code-repo/agentic-ai-engineering-course/.venv` does not match the project environment path `.venv` and will be ignored; use `--active` to target the active environment instead[0m

#   [1m[91mI001 [0m[[1m[96m*[0m] [1mImport block is un-sorted or un-formatted[0m

#    [1m[94m-->[0m test_linting.py:1:1

#     [1m[94m|[0m

#   [1m[94m1 |[0m [1m[91m/[0m import os

#   [1m[94m2 |[0m [1m[91m|[0m import sys

#   [1m[94m3 |[0m [1m[91m|[0m import json # Unused import

#     [1m[94m|[0m [1m[91m|___________^[0m

#   [1m[94m4 |[0m

#   [1m[94m5 |[0m   def calculate_sum(numbers):

#     [1m[94m|[0m

#   [1m[96mhelp[0m: [1mOrganize imports[0m

#   

#   [1m[91mF401 [0m[[1m[96m*[0m] [1m`json` imported but unused[0m

#    [1m[94m-->[0m test_linting.py:3:8

#     [1m[94m|[0m

#   [1m[94m1 |[0m import os

#   [1m[94m2 |[0m import sys

#   [1m[94m3 |[0m import json # Unused import

#     [1m[94m|[0m        [1m[91m^^^^[0m

#   [1m[94m4 |[0m

#   [1m[94m5 |[0m def calculate_sum(numbers):

#     [1m[94m|[0m

#   [1m[96mhelp[0m: [1mRemove unused import: `json`[0m

#   

#   [1m[91mF841 [0m[1mLocal variable `undefined_variable` is assigned to but never used[0m

#     [1m[94m-->[0m test_linting.py:18:5

#      [1m[94m|[0m

#   [1m[94m16 |[0m     _ = os.getcwd()  # Use os

#   [1m[94m17 |[0m     _ = sys.argv[0]  # Use sys

#   [1m[94m18 |[0m     undefined_variable = some_undefined_function()  # Using undefined name

#      [1m[94m|[0m     [1m[91m^^^^^^^^^^^^^^^^^^[0m

#   [1m[94m19 |[0m     return result

#      [1m[94m|[0m

#   [1m[96mhelp[0m: [1mRemove assignment to unused variable `undefined_variable`[0m

#   

#   [1m[91mF821 [0m[1mUndefined name `some_undefined_function`[0m

#     [1m[94m-->[0m test_linting.py:18:26

#      [1m[94m|[0m

#   [1m[94m16 |[0m     _ = os.getcwd()  # Use os

#   [1m[94m17 |[0m     _ = sys.argv[0]  # Use sys

#   [1m[94m18 |[0m     undefined_variable = some_undefined_function()  # Using undefined name

#      [1m[94m|[0m                          [1m[91m^^^^^^^^^^^^^^^^^^^^^^^[0m

#   [1m[94m19 |[0m     return result

#      [1m[94m|[0m

#   

#   [1m[91mE402 [0m[1mModule level import not at top of file[0m

#     [1m[94m-->[0m test_linting.py:21:1

#      [1m[94m|[0m

#   [1m[94m19 |[0m     return result

#   [1m[94m20 |[0m

#   [1m[94m21 |[0m import sys # Duplicate import

#      [1m[94m|[0m [1m[91m^^^^^^^^^^[0m

#      [1m[94m|[0m

#   

#   [1m[91mI001 [0m[[1m[96m*[0m] [1mImport block is un-sorted or un-formatted[0m

#     [1m[94m-->[0m test_linting.py:21:1

#      [1m[94m|[0m

#   [1m[94m19 |[0m     return result

#   [1m[94m20 |[0m

#   [1m[94m21 |[0m import sys # Duplicate import

#      [1m[94m|[0m [1m[91m^^^^^^^^^^[0m

#      [1m[94m|[0m

#   [1m[96mhelp[0m: [1mOrganize imports[0m

#   

#   [1m[91mF811 [0m[[1m[96m*[0m] [1mRedefinition of unused `sys` from line 2[0m

#     [1m[94m-->[0m test_linting.py:21:8

#      [1m[94m|[0m

#   [1m[94m19 |[0m     return result

#   [1m[94m20 |[0m

#   [1m[94m21 |[0m import sys # Duplicate import

#      [1m[94m|[0m        [1m[91m^^^[0m [1m[91m`sys` redefined here[0m

#      [1m[94m|[0m

#     [1m[94m:::[0m test_linting.py:2:8

#      [1m[94m|[0m

#   [1m[94m 1 |[0m import os

#   [1m[94m 2 |[0m import sys

#      [1m[94m|[0m        [1m[33m---[0m [1m[33mprevious definition of `sys` here[0m

#   [1m[94m 3 |[0m import json # Unused import

#      [1m[94m|[0m

#   [1m[96mhelp[0m: [1mRemove definition: `sys`[0m

#   

#   Found 7 errors.

#   [[36m*[0m] 4 fixable with the `--fix` option (1 hidden fix can be enabled with the `--unsafe-fixes` option).


"""
Ruff will report several issues:
- **F401**: Unused import (`json` is imported but never used)
- **F811**: Duplicate import (`sys` is imported twice)
- **F821**: Undefined name (`some_undefined_function` doesn't exist)
"""

"""
### 5.3 Auto-fix Linting Issues (Where Possible)
"""

!uv run ruff check --fix test_linting.py
# Output:
#   [1m[33mwarning[39m[0m[1m:[0m [1m`VIRTUAL_ENV=/Users/jai/Documents/code-repo/agentic-ai-engineering-course/.venv` does not match the project environment path `.venv` and will be ignored; use `--active` to target the active environment instead[0m

#   [1m[91mF841 [0m[1mLocal variable `undefined_variable` is assigned to but never used[0m

#     [1m[94m-->[0m test_linting.py:18:5

#      [1m[94m|[0m

#   [1m[94m16 |[0m     _ = os.getcwd()  # Use os

#   [1m[94m17 |[0m     _ = sys.argv[0]  # Use sys

#   [1m[94m18 |[0m     undefined_variable = some_undefined_function()  # Using undefined name

#      [1m[94m|[0m     [1m[91m^^^^^^^^^^^^^^^^^^[0m

#   [1m[94m19 |[0m     return result

#      [1m[94m|[0m

#   [1m[96mhelp[0m: [1mRemove assignment to unused variable `undefined_variable`[0m

#   

#   [1m[91mF821 [0m[1mUndefined name `some_undefined_function`[0m

#     [1m[94m-->[0m test_linting.py:18:26

#      [1m[94m|[0m

#   [1m[94m16 |[0m     _ = os.getcwd()  # Use os

#   [1m[94m17 |[0m     _ = sys.argv[0]  # Use sys

#   [1m[94m18 |[0m     undefined_variable = some_undefined_function()  # Using undefined name

#      [1m[94m|[0m                          [1m[91m^^^^^^^^^^^^^^^^^^^^^^^[0m

#   [1m[94m19 |[0m     return result

#      [1m[94m|[0m

#   

#   Found 5 errors (3 fixed, 2 remaining).

#   No fixes available (1 hidden fix can be enabled with the `--unsafe-fixes` option).


"""
Ruff will automatically fix:
- Remove unused imports
- Remove duplicate imports

But it won't fix the undefined name. That requires manual intervention since it's a logic error.

"""

!cat test_linting.py
# Output:
#   import os

#   import sys

#   

#   

#   def calculate_sum(numbers):

#       """Calculate sum of numbers."""

#       total = 0

#       for num in numbers:

#           total = total + num

#       return total

#   

#   def process_data(data):

#       """Process some data."""

#       result = calculate_sum(data)

#       print(f"Result: {result}")

#       _ = os.getcwd()  # Use os

#       _ = sys.argv[0]  # Use sys

#       undefined_variable = some_undefined_function()  # Using undefined name

#       return result

#   


"""
Let's remove the file now:
"""

!rm test_linting.py

"""
## 6. Running Unit Tests

Now let's run Brown's test suite with mocked LLM responses. The tests use fake models instead of real LLMs, making them fast, deterministic, and free.
"""

!CONFIG_FILE=configs/debug.yaml uv run pytest -v
# Output:
#   [1m[33mwarning[39m[0m[1m:[0m [1m`VIRTUAL_ENV=/Users/jai/Documents/code-repo/agentic-ai-engineering-course/.venv` does not match the project environment path `.venv` and will be ignored; use `--active` to target the active environment instead[0m

#   [1m============================= test session starts ==============================[0m

#   platform darwin -- Python 3.14.4, pytest-9.0.3, pluggy-1.6.0 -- /Users/jai/Documents/code-repo/agentic-ai-engineering-course/lessons/writing_workflow/.venv/bin/python

#   cachedir: .pytest_cache

#   rootdir: /Users/jai/Documents/code-repo/agentic-ai-engineering-course/lessons/writing_workflow

#   configfile: pyproject.toml

#   plugins: asyncio-1.4.0, langsmith-0.8.14, opik-2.0.62, anyio-4.13.0

#   asyncio: mode=Mode.STRICT, debug=False, asyncio_default_fixture_loop_scope=None, asyncio_default_test_loop_scope=function

#   collected 225 items                                                            [0m

#   

#   tests/brown/data/test_loaders.py::TestMarkdownArticleLoader::test_article_loader_success [32mPASSED[0m[33m [  0%][0m

#   tests/brown/data/test_loaders.py::TestMarkdownArticleLoader::test_article_loader_file_not_found [32mPASSED[0m[33m [  0%][0m

#   tests/brown/data/test_loaders.py::TestMarkdownArticleGuidelineLoader::test_article_guideline_loader_success [32mPASSED[0m[33m [  1%][0m

#   tests/brown/data/test_loaders.py::TestMarkdownArticleGuidelineLoader::test_article_guideline_loader_file_not_found [32mPASSED[0m[33m [  1%][0m

#   tests/brown/data/test_loaders.py::TestMarkdownResearchLoader::test_research_loader_success [32mPASSED[0m[33m [  2%][0m

#   tests/brown/data/test_loaders.py::TestMarkdownResearchLoader::test_research_loader_with_markdown_links [32mPASSED[0m[33m [  2%][0m

#   tests/brown/data/test_loaders.py::TestMarkdownResearchLoader::test_research_loader_file_not_found [32mPASSED[0m[33m [  3%][0m

#   tests/brown/data/test_loaders.py::TestMarkdownArticleProfilesLoader::test_profiles_loader_success [32mPASSED[0m[33m [  3%][0m

#   tests/brown/data/test_loaders.py::TestMarkdownArticleProfilesLoader::test_profiles_loader_missing_file [32mPASSED[0m[33m [  4%][0m

#   tests/brown/data/test_loaders.py::TestMarkdownArticleProfilesLoader::test_profiles_loader_get_supported_profiles [32mPASSED[0m[33m [  4%][0m

#   tests/brown/data/test_loaders.py::TestMarkdownArticleExampleLoader::test_article_example_loader_success [32mPASSED[0m[33m [  4%][0m

#   tests/brown/data/test_loaders.py::TestMarkdownArticleExampleLoader::test_article_example_loader_empty_dir [32mPASSED[0m[33m [  5%][0m

#   tests/brown/data/test_loaders.py::TestMarkdownArticleExampleLoader::test_article_example_loader_dir_not_found [32mPASSED[0m[33m [  5%][0m

#   tests/brown/data/test_loaders.py::TestMarkdownArticleExampleLoader::test_article_example_loader_ignores_non_md_files [32mPASSED[0m[33m [  6%][0m

#   tests/brown/data/test_renderers.py::TestMarkdownArticleRenderer::test_article_markdown_renderer [32mPASSED[0m[33m [  6%][0m

#   tests/brown/data/test_renderers.py::TestMarkdownArticleRenderer::test_article_markdown_renderer_overwrites_existing [32mPASSED[0m[33m [  7%][0m

#   tests/brown/data/test_renderers.py::TestMarkdownArticleRenderer::test_article_markdown_renderer_empty_content [32mPASSED[0m[33m [  7%][0m

#   tests/brown/data/test_renderers.py::TestMarkdownArticleReviewsRenderer::test_article_reviews_context_renderer [32mPASSED[0m[33m [  8%][0m

#   tests/brown/data/test_renderers.py::TestMarkdownArticleReviewsRenderer::test_article_reviews_context_renderer_overwrites_existing [32mPASSED[0m[33m [  8%][0m

#   tests/brown/data/test_renderers.py::TestMarkdownArticleReviewsRenderer::test_article_reviews_context_renderer_empty_reviews [32mPASSED[0m[33m [  8%][0m

#   tests/brown/data/test_renderers.py::TestMarkdownArticleReviewsRenderer::test_article_reviews_context_renderer_without_article [32mPASSED[0m[33m [  9%][0m

#   tests/brown/domain/test_articles.py::TestArticle::test_article_creation [32mPASSED[0m[33m [  9%][0m

#   tests/brown/domain/test_articles.py::TestArticle::test_article_to_context [32mPASSED[0m[33m [ 10%][0m

#   tests/brown/domain/test_articles.py::TestArticle::test_article_to_markdown [32mPASSED[0m[33m [ 10%][0m

#   tests/brown/domain/test_articles.py::TestArticle::test_article_str_representation [32mPASSED[0m[33m [ 11%][0m

#   tests/brown/domain/test_articles.py::TestArticle::test_article_empty_content [32mPASSED[0m[33m [ 11%][0m

#   tests/brown/domain/test_articles.py::TestSelectedText::test_selected_text_creation [32mPASSED[0m[33m [ 12%][0m

#   tests/brown/domain/test_articles.py::TestSelectedText::test_selected_text_to_context [32mPASSED[0m[33m [ 12%][0m

#   tests/brown/domain/test_articles.py::TestSelectedText::test_selected_text_single_line [32mPASSED[0m[33m [ 12%][0m

#   tests/brown/domain/test_articles.py::TestArticleExample::test_article_example_creation [32mPASSED[0m[33m [ 13%][0m

#   tests/brown/domain/test_articles.py::TestArticleExample::test_article_example_to_context [32mPASSED[0m[33m [ 13%][0m

#   tests/brown/domain/test_articles.py::TestArticleExample::test_article_example_str_representation [32mPASSED[0m[33m [ 14%][0m

#   tests/brown/domain/test_articles.py::TestArticleExamples::test_article_examples_creation [32mPASSED[0m[33m [ 14%][0m

#   tests/brown/domain/test_articles.py::TestArticleExamples::test_article_examples_to_context [32mPASSED[0m[33m [ 15%][0m

#   tests/brown/domain/test_articles.py::TestArticleExamples::test_article_examples_empty [32mPASSED[0m[33m [ 15%][0m

#   tests/brown/domain/test_articles.py::TestArticleExamples::test_article_examples_single [32mPASSED[0m[33m [ 16%][0m

#   tests/brown/domain/test_guidelines.py::TestArticleGuideline::test_article_guideline_creation [32mPASSED[0m[33m [ 16%][0m

#   tests/brown/domain/test_guidelines.py::TestArticleGuideline::test_article_guideline_to_context [32mPASSED[0m[33m [ 16%][0m

#   tests/brown/domain/test_guidelines.py::TestArticleGuideline::test_article_guideline_empty_content [32mPASSED[0m[33m [ 17%][0m

#   tests/brown/domain/test_guidelines.py::TestArticleGuideline::test_article_guideline_complex_content [32mPASSED[0m[33m [ 17%][0m

#   tests/brown/domain/test_media_items.py::TestMediaItem::test_media_item_creation [32mPASSED[0m[33m [ 18%][0m

#   tests/brown/domain/test_media_items.py::TestMediaItem::test_media_item_to_context [32mPASSED[0m[33m [ 18%][0m

#   tests/brown/domain/test_media_items.py::TestMediaItem::test_media_item_different_types [32mPASSED[0m[33m [ 19%][0m

#   tests/brown/domain/test_media_items.py::TestMediaItem::test_media_item_str_representation [32mPASSED[0m[33m [ 19%][0m

#   tests/brown/domain/test_media_items.py::TestMediaItems::test_media_items_creation [32mPASSED[0m[33m [ 20%][0m

#   tests/brown/domain/test_media_items.py::TestMediaItems::test_media_items_to_context [32mPASSED[0m[33m [ 20%][0m

#   tests/brown/domain/test_media_items.py::TestMediaItems::test_media_items_empty [32mPASSED[0m[33m [ 20%][0m

#   tests/brown/domain/test_media_items.py::TestMediaItems::test_media_items_single [32mPASSED[0m[33m [ 21%][0m

#   tests/brown/domain/test_media_items.py::TestMediaItems::test_media_items_str_representation [32mPASSED[0m[33m [ 21%][0m

#   tests/brown/domain/test_media_items.py::TestMediaItems::test_media_items_build_classmethod [32mPASSED[0m[33m [ 22%][0m

#   tests/brown/domain/test_media_items.py::TestMediaItems::test_are_available_only_in_source_property [32mPASSED[0m[33m [ 22%][0m

#   tests/brown/domain/test_media_items.py::TestMermaidDiagram::test_mermaid_diagram_creation [32mPASSED[0m[33m [ 23%][0m

#   tests/brown/domain/test_mixins.py::TestContextMixin::test_context_mixin_xml_tag [32mPASSED[0m[33m [ 23%][0m

#   tests/brown/domain/test_mixins.py::TestContextMixin::test_context_mixin_xml_tag_with_profile [32mPASSED[0m[33m [ 24%][0m

#   tests/brown/domain/test_mixins.py::TestContextMixin::test_context_mixin_xml_tag_with_suffix [32mPASSED[0m[33m [ 24%][0m

#   tests/brown/domain/test_mixins.py::TestMarkdownMixin::test_markdown_mixin_abstract [32mPASSED[0m[33m [ 24%][0m

#   tests/brown/domain/test_mixins.py::TestMarkdownMixin::test_markdown_mixin_implementation [32mPASSED[0m[33m [ 25%][0m

#   tests/brown/domain/test_mixins.py::TestMarkdownMixin::test_markdown_mixin_missing_implementation [32mPASSED[0m[33m [ 25%][0m

#   tests/brown/domain/test_profiles.py::TestProfile::test_profile_creation [32mPASSED[0m[33m [ 26%][0m

#   tests/brown/domain/test_profiles.py::TestProfile::test_profile_xml_tag [32mPASSED[0m[33m [ 26%][0m

#   tests/brown/domain/test_profiles.py::TestProfile::test_profile_to_context [32mPASSED[0m[33m [ 27%][0m

#   tests/brown/domain/test_profiles.py::TestCharacterProfile::test_character_profile_creation [32mPASSED[0m[33m [ 27%][0m

#   tests/brown/domain/test_profiles.py::TestCharacterProfile::test_character_profile_to_context [32mPASSED[0m[33m [ 28%][0m

#   tests/brown/domain/test_profiles.py::TestArticleProfile::test_article_profile_creation [32mPASSED[0m[33m [ 28%][0m

#   tests/brown/domain/test_profiles.py::TestArticleProfile::test_article_profile_to_context [32mPASSED[0m[33m [ 28%][0m

#   tests/brown/domain/test_profiles.py::TestStructureProfile::test_structure_profile_creation [32mPASSED[0m[33m [ 29%][0m

#   tests/brown/domain/test_profiles.py::TestStructureProfile::test_structure_profile_to_context [32mPASSED[0m[33m [ 29%][0m

#   tests/brown/domain/test_profiles.py::TestMechanicsProfile::test_mechanics_profile_creation [32mPASSED[0m[33m [ 30%][0m

#   tests/brown/domain/test_profiles.py::TestMechanicsProfile::test_mechanics_profile_to_context [32mPASSED[0m[33m [ 30%][0m

#   tests/brown/domain/test_profiles.py::TestTerminologyProfile::test_terminology_profile_creation [32mPASSED[0m[33m [ 31%][0m

#   tests/brown/domain/test_profiles.py::TestTerminologyProfile::test_terminology_profile_to_context [32mPASSED[0m[33m [ 31%][0m

#   tests/brown/domain/test_profiles.py::TestTonalityProfile::test_tonality_profile_creation [32mPASSED[0m[33m [ 32%][0m

#   tests/brown/domain/test_profiles.py::TestTonalityProfile::test_tonality_profile_to_context [32mPASSED[0m[33m [ 32%][0m

#   tests/brown/domain/test_profiles.py::TestArticleProfiles::test_article_profiles_creation [32mPASSED[0m[33m [ 32%][0m

#   tests/brown/domain/test_profiles.py::TestArticleProfiles::test_article_profiles_to_context [32mPASSED[0m[33m [ 33%][0m

#   tests/brown/domain/test_research.py::TestResearch::test_research_creation [32mPASSED[0m[33m [ 33%][0m

#   tests/brown/domain/test_research.py::TestResearch::test_research_to_context [32mPASSED[0m[33m [ 34%][0m

#   tests/brown/domain/test_research.py::TestResearch::test_research_empty_content [32mPASSED[0m[33m [ 34%][0m

#   tests/brown/domain/test_research.py::TestResearch::test_research_complex_content [32mPASSED[0m[33m [ 35%][0m

#   tests/brown/domain/test_research.py::TestResearch::test_research_str_representation [32mPASSED[0m[33m [ 35%][0m

#   tests/brown/domain/test_reviews.py::TestReview::test_review_creation [32mPASSED[0m[33m [ 36%][0m

#   tests/brown/domain/test_reviews.py::TestReview::test_review_to_context [32mPASSED[0m[33m [ 36%][0m

#   tests/brown/domain/test_reviews.py::TestReview::test_review_score_validation [32mPASSED[0m[33m [ 36%][0m

#   tests/brown/domain/test_reviews.py::TestReview::test_review_str_representation [32mPASSED[0m[33m [ 37%][0m

#   tests/brown/domain/test_reviews.py::TestArticleReviews::test_article_reviews_creation [32mPASSED[0m[33m [ 37%][0m

#   tests/brown/domain/test_reviews.py::TestArticleReviews::test_article_reviews_to_context [32mPASSED[0m[33m [ 38%][0m

#   tests/brown/domain/test_reviews.py::TestArticleReviews::test_article_reviews_with_article [32mPASSED[0m[33m [ 38%][0m

#   tests/brown/domain/test_reviews.py::TestArticleReviews::test_article_reviews_without_article [32mPASSED[0m[33m [ 39%][0m

#   tests/brown/domain/test_reviews.py::TestArticleReviews::test_article_reviews_empty [32mPASSED[0m[33m [ 39%][0m

#   tests/brown/domain/test_reviews.py::TestArticleReviews::test_article_reviews_single [32mPASSED[0m[33m [ 40%][0m

#   tests/brown/domain/test_reviews.py::TestArticleReviews::test_article_reviews_str_representation [32mPASSED[0m[33m [ 40%][0m

#   tests/brown/domain/test_reviews.py::TestHumanFeedback::test_human_feedback_creation [32mPASSED[0m[33m [ 40%][0m

#   tests/brown/domain/test_reviews.py::TestHumanFeedback::test_human_feedback_to_context [32mPASSED[0m[33m [ 41%][0m

#   tests/brown/domain/test_reviews.py::TestSelectedTextReviews::test_selected_text_reviews_creation [32mPASSED[0m[33m [ 41%][0m

#   tests/brown/domain/test_reviews.py::TestSelectedTextReviews::test_selected_text_reviews_to_context [32mPASSED[0m[33m [ 42%][0m

#   tests/brown/evals/metrics/follows_gt/test_follows_gt_metric.py::test_article_metric_perfect_score [32mPASSED[0m[33m [ 42%][0m

#   tests/brown/evals/metrics/follows_gt/test_follows_gt_metric.py::test_article_metric_mixed_scores [32mPASSED[0m[33m [ 43%][0m

#   tests/brown/evals/metrics/follows_gt/test_follows_gt_metric.py::test_article_metric_empty_sections [32mPASSED[0m[33m [ 43%][0m

#   tests/brown/evals/metrics/follows_gt/test_follows_gt_metric.py::test_article_metric_init_requires_mocked_response_for_fake_model [32mPASSED[0m[33m [ 44%][0m

#   tests/brown/evals/metrics/follows_gt/test_follows_gt_metric.py::test_article_metric_init_default_model [32mPASSED[0m[33m [ 44%][0m

#   tests/brown/evals/metrics/follows_gt/test_follows_gt_metric.py::test_article_metric_init_custom_name [32mPASSED[0m[33m [ 44%][0m

#   tests/brown/evals/metrics/user_intent/test_user_intent_metric.py::test_user_intent_metric_perfect_score [32mPASSED[0m[33m [ 45%][0m

#   tests/brown/evals/metrics/user_intent/test_user_intent_metric.py::test_user_intent_metric_mixed_scores [32mPASSED[0m[33m [ 45%][0m

#   tests/brown/evals/metrics/user_intent/test_user_intent_metric.py::test_user_intent_metric_poor_scores [32mPASSED[0m[33m [ 46%][0m

#   tests/brown/evals/metrics/user_intent/test_user_intent_metric.py::test_user_intent_metric_empty_sections [32mPASSED[0m[33m [ 46%][0m

#   tests/brown/evals/metrics/user_intent/test_user_intent_metric.py::test_user_intent_metric_missing_research_in_context [32mPASSED[0m[33m [ 47%][0m

#   tests/brown/evals/metrics/user_intent/test_user_intent_metric.py::test_user_intent_metric_init_requires_mocked_response_for_fake_model [32mPASSED[0m[33m [ 47%][0m

#   tests/brown/evals/metrics/user_intent/test_user_intent_metric.py::test_user_intent_metric_init_default_model [32mPASSED[0m[33m [ 48%][0m

#   tests/brown/evals/metrics/user_intent/test_user_intent_metric.py::test_user_intent_metric_init_custom_name [32mPASSED[0m[33m [ 48%][0m

#   tests/brown/evals/metrics/user_intent/test_user_intent_metric.py::test_user_intent_metric_init_custom_few_shot_examples [32mPASSED[0m[33m [ 48%][0m

#   tests/brown/evals/metrics/user_intent/test_user_intent_metric.py::test_user_intent_metric_score_result_structure [32mPASSED[0m[33m [ 49%][0m

#   tests/brown/evals/metrics/user_intent/test_user_intent_metric.py::test_user_intent_metric_async_score [32mPASSED[0m[33m [ 49%][0m

#   tests/brown/evals/metrics/user_intent/test_user_intent_metric.py::test_user_intent_scores_to_context [32mPASSED[0m[33m [ 50%][0m

#   tests/brown/evals/metrics/user_intent/test_user_intent_metric.py::test_user_intent_article_scores_to_context [32mPASSED[0m[33m [ 50%][0m

#   tests/brown/evals/test_dataset.py::test_load_dataset_success [32mPASSED[0m[33m      [ 51%][0m

#   tests/brown/evals/test_dataset.py::test_load_dataset_few_shot_example [32mPASSED[0m[33m [ 51%][0m

#   tests/brown/evals/test_dataset.py::test_load_dataset_file_not_found [32mPASSED[0m[33m [ 52%][0m

#   tests/brown/evals/test_dataset.py::test_load_dataset_metadata_not_found [32mPASSED[0m[33m [ 52%][0m

#   tests/brown/evals/test_dataset.py::test_load_dataset_empty_metadata [32mPASSED[0m[33m [ 52%][0m

#   tests/brown/evals/test_dataset.py::test_load_dataset_invalid_metadata_structure [32mPASSED[0m[33m [ 53%][0m

#   tests/brown/evals/test_tasks.py::TestEvaluationTask::test_evaluation_task_creation [32mPASSED[0m[33m [ 53%][0m

#   tests/brown/evals/test_tasks.py::TestEvaluationTask::test_evaluation_task_function_signature [32mPASSED[0m[33m [ 54%][0m

#   tests/brown/evals/test_tasks.py::TestEvaluationTask::test_create_evaluation_task_parameters [32mPASSED[0m[33m [ 54%][0m

#   tests/brown/evals/test_tasks.py::TestEvaluationTask::test_evaluation_task_async [32mPASSED[0m[33m [ 55%][0m

#   tests/brown/models/test_config.py::TestModelConfigThinking::test_thinking_budget_only [32mPASSED[0m[33m [ 55%][0m

#   tests/brown/models/test_config.py::TestModelConfigThinking::test_thinking_level_only [32mPASSED[0m[33m [ 56%][0m

#   tests/brown/models/test_config.py::TestModelConfigThinking::test_neither_is_allowed [32mPASSED[0m[33m [ 56%][0m

#   tests/brown/models/test_config.py::TestModelConfigThinking::test_budget_and_level_are_mutually_exclusive [32mPASSED[0m[33m [ 56%][0m

#   tests/brown/models/test_config.py::TestModelConfigThinking::test_invalid_thinking_level_rejected [32mPASSED[0m[33m [ 57%][0m

#   tests/brown/models/test_config.py::TestModelConfigThinking::test_model_dump_drops_top_k_top_p [32mPASSED[0m[33m [ 57%][0m

#   tests/brown/models/test_config.py::TestModelConfigThinking::test_model_dump_excludes_unset_params [32mPASSED[0m[33m [ 58%][0m

#   tests/brown/models/test_config.py::TestModelConfigThinking::test_model_dump_includes_set_params [32mPASSED[0m[33m [ 58%][0m

#   tests/brown/nodes/test_article_reviewer.py::TestArticleReviewer::test_article_reviewer_initialization [32mPASSED[0m[33m [ 59%][0m

#   tests/brown/nodes/test_article_reviewer.py::TestArticleReviewer::test_article_reviewer_ainvoke_success [32mPASSED[0m[33m [ 59%][0m

#   tests/brown/nodes/test_article_reviewer.py::TestArticleReviewer::test_article_reviewer_structured_output [32mPASSED[0m[33m [ 60%][0m

#   tests/brown/nodes/test_article_reviewer.py::TestArticleReviewer::test_article_reviewer_empty_article [32mPASSED[0m[33m [ 60%][0m

#   tests/brown/nodes/test_article_reviewer.py::TestArticleReviewer::test_article_reviewer_multiple_reviews [32mPASSED[0m[33m [ 60%][0m

#   tests/brown/nodes/test_article_reviewer.py::TestArticleReviewer::test_article_reviewer_requires_mocked_response_for_fake_model [32mPASSED[0m[33m [ 61%][0m

#   tests/brown/nodes/test_article_reviewer.py::TestArticleReviewer::test_article_reviewer_selected_text_initialization [32mPASSED[0m[33m [ 61%][0m

#   tests/brown/nodes/test_article_reviewer.py::TestArticleReviewer::test_article_reviewer_selected_text_ainvoke [32mPASSED[0m[33m [ 62%][0m

#   tests/brown/nodes/test_article_reviewer.py::TestArticleReviewer::test_article_reviewer_selected_text_with_human_feedback [32mPASSED[0m[33m [ 62%][0m

#   tests/brown/nodes/test_article_reviewer.py::TestArticleReviewer::test_article_reviewer_article_property [32mPASSED[0m[33m [ 63%][0m

#   tests/brown/nodes/test_article_writer.py::TestArticleWriter::test_article_writer_initialization [32mPASSED[0m[33m [ 63%][0m

#   tests/brown/nodes/test_article_writer.py::TestArticleWriter::test_article_writer_ainvoke_success [32mPASSED[0m[33m [ 64%][0m

#   tests/brown/nodes/test_article_writer.py::TestArticleWriter::test_article_writer_with_media_items [32mPASSED[0m[33m [ 64%][0m

#   tests/brown/nodes/test_article_writer.py::TestArticleWriter::test_article_writer_with_reviews [32mPASSED[0m[33m [ 64%][0m

#   tests/brown/nodes/test_article_writer.py::TestArticleWriter::test_article_writer_empty_input [32mPASSED[0m[33m [ 65%][0m

#   tests/brown/nodes/test_article_writer.py::TestArticleWriter::test_article_writer_requires_mocked_response_for_fake_model [32mPASSED[0m[33m [ 65%][0m

#   tests/brown/nodes/test_article_writer.py::TestArticleWriter::test_article_writer_with_selected_text_reviews [32mPASSED[0m[33m [ 66%][0m

#   tests/brown/nodes/test_article_writer.py::TestArticleWriter::test_article_writer_selected_text_preserves_line_numbers [32mPASSED[0m[33m [ 66%][0m

#   tests/brown/nodes/test_article_writer.py::TestArticleWriter::test_article_writer_selected_text_vs_article_output [32mPASSED[0m[33m [ 67%][0m

#   tests/brown/nodes/test_article_writer.py::TestArticleWriter::test_article_writer_selected_text_content [32mPASSED[0m[33m [ 67%][0m

#   tests/brown/nodes/test_base.py::TestNode::test_node_initialization [32mPASSED[0m[33m [ 68%][0m

#   tests/brown/nodes/test_base.py::TestNode::test_node_build_toolkit [32mPASSED[0m[33m [ 68%][0m

#   tests/brown/nodes/test_base.py::TestNode::test_node_build_model_client [32mPASSED[0m[33m [ 68%][0m

#   tests/brown/nodes/test_base.py::TestNode::test_node_build_model_client_fake [32mPASSED[0m[33m [ 69%][0m

#   tests/brown/nodes/test_base.py::TestNode::test_node_build_user_input_content [32mPASSED[0m[33m [ 69%][0m

#   tests/brown/nodes/test_base.py::TestNode::test_node_as_tool [32mPASSED[0m[33m       [ 70%][0m

#   tests/brown/nodes/test_base.py::TestNode::test_node_with_fake_model_requires_mocked_response [32mPASSED[0m[33m [ 70%][0m

#   tests/brown/nodes/test_base.py::TestNode::test_node_set_mocked_responses [32mPASSED[0m[33m [ 71%][0m

#   tests/brown/nodes/test_base.py::TestToolkit::test_toolkit_initialization [32mPASSED[0m[33m [ 71%][0m

#   tests/brown/nodes/test_base.py::TestToolkit::test_toolkit_abstract_methods [32mPASSED[0m[33m [ 72%][0m

#   tests/brown/nodes/test_media_generator.py::TestMermaidDiagramGenerator::test_mermaid_diagram_generator_initialization [32mPASSED[0m[33m [ 72%][0m

#   tests/brown/nodes/test_media_generator.py::TestMermaidDiagramGenerator::test_mermaid_diagram_generator_ainvoke [32mPASSED[0m[33m [ 72%][0m

#   tests/brown/nodes/test_media_generator.py::TestMermaidDiagramGenerator::test_mermaid_diagram_generator_error_handling [32mPASSED[0m[33m [ 73%][0m

#   tests/brown/nodes/test_media_generator.py::TestMermaidDiagramGenerator::test_mermaid_diagram_generator_requires_mocked_response_for_fake_model [32mPASSED[0m[33m [ 73%][0m

#   tests/brown/nodes/test_media_generator.py::TestMediaGeneratorOrchestrator::test_media_generator_orchestrator_initialization [32mPASSED[0m[33m [ 74%][0m

#   tests/brown/nodes/test_media_generator.py::TestMediaGeneratorOrchestrator::test_media_generator_orchestrator_ainvoke [32mPASSED[0m[33m [ 74%][0m

#   tests/brown/nodes/test_media_generator.py::TestMediaGeneratorOrchestrator::test_media_generator_orchestrator_requires_mocked_response_for_fake_model [32mPASSED[0m[33m [ 75%][0m

#   tests/brown/utils/test_a.py::TestAsSync::test_as_sync_decorator [32mPASSED[0m[33m   [ 75%][0m

#   tests/brown/utils/test_a.py::TestAsSync::test_as_sync_with_exception [32mPASSED[0m[33m [ 76%][0m

#   tests/brown/utils/test_a.py::TestAsSync::test_as_sync_invalid_function [32mPASSED[0m[33m [ 76%][0m

#   tests/brown/utils/test_a.py::TestAsyncioRun::test_asyncio_run_new_loop [32mPASSED[0m[33m [ 76%][0m

#   tests/brown/utils/test_a.py::TestAsyncioRun::test_asyncio_run_with_exception [32mPASSED[0m[33m [ 77%][0m

#   tests/brown/utils/test_a.py::TestAsyncioRun::test_asyncio_run_existing_loop [32mPASSED[0m[33m [ 77%][0m

#   tests/brown/utils/test_a.py::TestRunAsyncTasks::test_run_async_tasks [32mPASSED[0m[33m [ 78%][0m

#   tests/brown/utils/test_a.py::TestRunAsyncTasks::test_run_async_tasks_empty [32mPASSED[0m[33m [ 78%][0m

#   tests/brown/utils/test_a.py::TestRunAsyncTasks::test_run_async_tasks_with_progress [32mPASSED[0m[33m [ 79%][0m

#   tests/brown/utils/test_a.py::TestBatchGather::test_batch_gather [32mPASSED[0m[33m   [ 79%][0m

#   tests/brown/utils/test_a.py::TestBatchGather::test_batch_gather_single_batch [32mPASSED[0m[33m [ 80%][0m

#   tests/brown/utils/test_a.py::TestBatchGather::test_batch_gather_with_verbose [32mPASSED[0m[33m [ 80%][0m

#   tests/brown/utils/test_a.py::TestRunJobs::test_run_jobs [32mPASSED[0m[33m           [ 80%][0m

#   tests/brown/utils/test_a.py::TestRunJobs::test_run_jobs_single_worker [32mPASSED[0m[33m [ 81%][0m

#   tests/brown/utils/test_a.py::TestRunJobs::test_run_jobs_with_progress [32mPASSED[0m[33m [ 81%][0m

#   tests/brown/utils/test_a.py::TestRunJobs::test_run_jobs_empty [32mPASSED[0m[33m     [ 82%][0m

#   tests/brown/utils/test_a.py::TestRunJobs::test_run_jobs_with_exception [32mPASSED[0m[33m [ 82%][0m

#   tests/brown/utils/test_network.py::TestIsImageDomainAccepted::test_valid_domains [32mPASSED[0m[33m [ 83%][0m

#   tests/brown/utils/test_network.py::TestIsImageDomainAccepted::test_invalid_domains [32mPASSED[0m[33m [ 83%][0m

#   tests/brown/utils/test_network.py::TestIsImageDomainAccepted::test_edge_cases [32mPASSED[0m[33m [ 84%][0m

#   tests/brown/utils/test_network.py::TestPing::test_ping_success [32mPASSED[0m[33m    [ 84%][0m

#   tests/brown/utils/test_network.py::TestPing::test_ping_head_fallback_to_get [32mPASSED[0m[33m [ 84%][0m

#   tests/brown/utils/test_network.py::TestPing::test_ping_invalid_content_type [32mPASSED[0m[33m [ 85%][0m

#   tests/brown/utils/test_network.py::TestPing::test_ping_non_200_status [32mPASSED[0m[33m [ 85%][0m

#   tests/brown/utils/test_network.py::TestPing::test_ping_request_error [32mPASSED[0m[33m [ 86%][0m

#   tests/brown/utils/test_network.py::TestPing::test_ping_timeout [32mPASSED[0m[33m    [ 86%][0m

#   tests/brown/utils/test_network.py::TestPing::test_ping_invalid_url [32mPASSED[0m[33m [ 87%][0m

#   tests/brown/utils/test_network.py::TestIsImageUrlValid::test_valid_image_url [32mPASSED[0m[33m [ 87%][0m

#   tests/brown/utils/test_network.py::TestIsImageUrlValid::test_invalid_domain [32mPASSED[0m[33m [ 88%][0m

#   tests/brown/utils/test_network.py::TestIsImageUrlValid::test_valid_domain_but_unreachable [32mPASSED[0m[33m [ 88%][0m

#   tests/brown/utils/test_network.py::TestIsImageUrlValid::test_custom_timeout [32mPASSED[0m[33m [ 88%][0m

#   tests/brown/utils/test_network.py::TestIsImageUrlValid::test_empty_url [32mPASSED[0m[33m [ 89%][0m

#   tests/brown/utils/test_network.py::TestIsImageUrlValid::test_malformed_url [32mPASSED[0m[33m [ 89%][0m

#   tests/brown/utils/test_s.py::TestCamelToSnake::test_camel_to_snake_simple [32mPASSED[0m[33m [ 90%][0m

#   tests/brown/utils/test_s.py::TestCamelToSnake::test_camel_to_snake_with_numbers [32mPASSED[0m[33m [ 90%][0m

#   tests/brown/utils/test_s.py::TestCamelToSnake::test_camel_to_snake_single_word [32mPASSED[0m[33m [ 91%][0m

#   tests/brown/utils/test_s.py::TestCamelToSnake::test_camel_to_snake_empty [32mPASSED[0m[33m [ 91%][0m

#   tests/brown/utils/test_s.py::TestCamelToSnake::test_camel_to_snake_already_snake [32mPASSED[0m[33m [ 92%][0m

#   tests/brown/utils/test_s.py::TestNormalizeAnyToStr::test_normalize_any_to_str_with_string [32mPASSED[0m[33m [ 92%][0m

#   tests/brown/utils/test_s.py::TestNormalizeAnyToStr::test_normalize_any_to_str_with_list [32mPASSED[0m[33m [ 92%][0m

#   tests/brown/utils/test_s.py::TestNormalizeAnyToStr::test_normalize_any_to_str_with_dict [32mPASSED[0m[33m [ 93%][0m

#   tests/brown/utils/test_s.py::TestNormalizeAnyToStr::test_normalize_any_to_str_invalid_list [32mPASSED[0m[33m [ 93%][0m

#   tests/brown/utils/test_s.py::TestNormalizeAnyToStr::test_normalize_any_to_str_invalid_dict [32mPASSED[0m[33m [ 94%][0m

#   tests/brown/utils/test_s.py::TestNormalizeAnyToStr::test_normalize_any_to_str_invalid_type [32mPASSED[0m[33m [ 94%][0m

#   tests/brown/utils/test_s.py::TestCleanMarkdownLinks::test_clean_markdown_links_simple [32mPASSED[0m[33m [ 95%][0m

#   tests/brown/utils/test_s.py::TestCleanMarkdownLinks::test_clean_markdown_links_multiple [32mPASSED[0m[33m [ 95%][0m

#   tests/brown/utils/test_s.py::TestCleanMarkdownLinks::test_clean_markdown_links_with_images [32mPASSED[0m[33m [ 96%][0m

#   tests/brown/utils/test_s.py::TestCleanMarkdownLinks::test_clean_markdown_links_malformed [32mPASSED[0m[33m [ 96%][0m

#   tests/brown/utils/test_s.py::TestCleanMarkdownLinks::test_clean_markdown_links_no_links [32mPASSED[0m[33m [ 96%][0m

#   tests/brown/utils/test_s.py::TestCleanMarkdownLinks::test_clean_markdown_links_empty [32mPASSED[0m[33m [ 97%][0m

#   tests/brown/utils/test_s.py::TestCleanMarkdownLinks::test_clean_markdown_links_complex [32mPASSED[0m[33m [ 97%][0m

#   tests/brown/utils/test_s.py::TestCleanMarkdownLinks::test_clean_markdown_links_with_text [32mPASSED[0m[33m [ 98%][0m

#   tests/brown/utils/test_s.py::TestCleanMarkdownLinks::test_clean_markdown_links_nested_brackets [32mPASSED[0m[33m [ 98%][0m

#   tests/brown/workflows/test_edit_article.py::TestEditArticleWorkflow::test_edit_article_workflow [32mPASSED[0m[33m [ 99%][0m

#   tests/brown/workflows/test_edit_selected_text.py::TestEditSelectedTextWorkflow::test_edit_selected_text_workflow [32mPASSED[0m[33m [ 99%][0m

#   tests/brown/workflows/test_generate_article.py::TestGenerateArticleWorkflow::test_generate_article_workflow [32mPASSED[0m[33m [100%][0m

#   

#   [33m=============================== warnings summary ===============================[0m

#   src/brown/models/fake_model.py:4

#     /Users/jai/Documents/code-repo/agentic-ai-engineering-course/lessons/writing_workflow/src/brown/models/fake_model.py:4: DeprecationWarning: `langchain-community` is being sunset and is no longer actively maintained. See https://github.com/langchain-ai/langchain-community/issues/674 for details and migration guidance toward standalone integration packages.

#       from langchain_community.chat_models import FakeListChatModel

#   

#   tests/brown/utils/test_network.py::TestPing::test_ping_non_200_status

#     /Users/jai/Documents/code-repo/agentic-ai-engineering-course/lessons/writing_workflow/src/brown/utils/network.py:39: RuntimeWarning: coroutine 'AsyncMockMixin._execute_mock_call' was never awaited

#       if response.status_code == 405 or not response.headers.get("Content-Type"):

#     Enable tracemalloc to get traceback where the object was allocated.

#     See https://docs.pytest.org/en/stable/how-to/capture-warnings.html#resource-warnings for more info.

#   

#   -- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html

#   [33m======================= [32m225 passed[0m, [33m[1m2 warnings[0m[33m in 0.84s[0m[33m ========================[0m

#   /Users/jai/Documents/code-repo/agentic-ai-engineering-course/lessons/writing_workflow/.venv/lib/python3.14/site-packages/_pytest/unraisableexception.py:33: RuntimeWarning: coroutine 'run_jobs.<locals>.worker' was never awaited

#     gc.collect()

#   RuntimeWarning: Enable tracemalloc to get the object allocation traceback


"""
The `-v` flag provides verbose output, showing each test as it runs. The `CONFIG_FILE=configs/debug.yaml` ensures all tests use fake models instead of real LLMs.

### 6.1 Running Specific Test Files

You can run tests for specific components:
"""

!CONFIG_FILE=configs/debug.yaml uv run pytest tests/brown/domain/ -v
# Output:
#   [1m[33mwarning[39m[0m[1m:[0m [1m`VIRTUAL_ENV=/Users/jai/Documents/code-repo/agentic-ai-engineering-course/.venv` does not match the project environment path `.venv` and will be ignored; use `--active` to target the active environment instead[0m

#   [1m============================= test session starts ==============================[0m

#   platform darwin -- Python 3.14.4, pytest-9.0.3, pluggy-1.6.0 -- /Users/jai/Documents/code-repo/agentic-ai-engineering-course/lessons/writing_workflow/.venv/bin/python

#   cachedir: .pytest_cache

#   rootdir: /Users/jai/Documents/code-repo/agentic-ai-engineering-course/lessons/writing_workflow

#   configfile: pyproject.toml

#   plugins: asyncio-1.4.0, langsmith-0.8.14, opik-2.0.62, anyio-4.13.0

#   asyncio: mode=Mode.STRICT, debug=False, asyncio_default_fixture_loop_scope=None, asyncio_default_test_loop_scope=function

#   collected 74 items                                                             [0m

#   

#   tests/brown/domain/test_articles.py::TestArticle::test_article_creation [32mPASSED[0m[33m [  1%][0m

#   tests/brown/domain/test_articles.py::TestArticle::test_article_to_context [32mPASSED[0m[33m [  2%][0m

#   tests/brown/domain/test_articles.py::TestArticle::test_article_to_markdown [32mPASSED[0m[33m [  4%][0m

#   tests/brown/domain/test_articles.py::TestArticle::test_article_str_representation [32mPASSED[0m[33m [  5%][0m

#   tests/brown/domain/test_articles.py::TestArticle::test_article_empty_content [32mPASSED[0m[33m [  6%][0m

#   tests/brown/domain/test_articles.py::TestSelectedText::test_selected_text_creation [32mPASSED[0m[33m [  8%][0m

#   tests/brown/domain/test_articles.py::TestSelectedText::test_selected_text_to_context [32mPASSED[0m[33m [  9%][0m

#   tests/brown/domain/test_articles.py::TestSelectedText::test_selected_text_single_line [32mPASSED[0m[33m [ 10%][0m

#   tests/brown/domain/test_articles.py::TestArticleExample::test_article_example_creation [32mPASSED[0m[33m [ 12%][0m

#   tests/brown/domain/test_articles.py::TestArticleExample::test_article_example_to_context [32mPASSED[0m[33m [ 13%][0m

#   tests/brown/domain/test_articles.py::TestArticleExample::test_article_example_str_representation [32mPASSED[0m[33m [ 14%][0m

#   tests/brown/domain/test_articles.py::TestArticleExamples::test_article_examples_creation [32mPASSED[0m[33m [ 16%][0m

#   tests/brown/domain/test_articles.py::TestArticleExamples::test_article_examples_to_context [32mPASSED[0m[33m [ 17%][0m

#   tests/brown/domain/test_articles.py::TestArticleExamples::test_article_examples_empty [32mPASSED[0m[33m [ 18%][0m

#   tests/brown/domain/test_articles.py::TestArticleExamples::test_article_examples_single [32mPASSED[0m[33m [ 20%][0m

#   tests/brown/domain/test_guidelines.py::TestArticleGuideline::test_article_guideline_creation [32mPASSED[0m[33m [ 21%][0m

#   tests/brown/domain/test_guidelines.py::TestArticleGuideline::test_article_guideline_to_context [32mPASSED[0m[33m [ 22%][0m

#   tests/brown/domain/test_guidelines.py::TestArticleGuideline::test_article_guideline_empty_content [32mPASSED[0m[33m [ 24%][0m

#   tests/brown/domain/test_guidelines.py::TestArticleGuideline::test_article_guideline_complex_content [32mPASSED[0m[33m [ 25%][0m

#   tests/brown/domain/test_media_items.py::TestMediaItem::test_media_item_creation [32mPASSED[0m[33m [ 27%][0m

#   tests/brown/domain/test_media_items.py::TestMediaItem::test_media_item_to_context [32mPASSED[0m[33m [ 28%][0m

#   tests/brown/domain/test_media_items.py::TestMediaItem::test_media_item_different_types [32mPASSED[0m[33m [ 29%][0m

#   tests/brown/domain/test_media_items.py::TestMediaItem::test_media_item_str_representation [32mPASSED[0m[33m [ 31%][0m

#   tests/brown/domain/test_media_items.py::TestMediaItems::test_media_items_creation [32mPASSED[0m[33m [ 32%][0m

#   tests/brown/domain/test_media_items.py::TestMediaItems::test_media_items_to_context [32mPASSED[0m[33m [ 33%][0m

#   tests/brown/domain/test_media_items.py::TestMediaItems::test_media_items_empty [32mPASSED[0m[33m [ 35%][0m

#   tests/brown/domain/test_media_items.py::TestMediaItems::test_media_items_single [32mPASSED[0m[33m [ 36%][0m

#   tests/brown/domain/test_media_items.py::TestMediaItems::test_media_items_str_representation [32mPASSED[0m[33m [ 37%][0m

#   tests/brown/domain/test_media_items.py::TestMediaItems::test_media_items_build_classmethod [32mPASSED[0m[33m [ 39%][0m

#   tests/brown/domain/test_media_items.py::TestMediaItems::test_are_available_only_in_source_property [32mPASSED[0m[33m [ 40%][0m

#   tests/brown/domain/test_media_items.py::TestMermaidDiagram::test_mermaid_diagram_creation [32mPASSED[0m[33m [ 41%][0m

#   tests/brown/domain/test_mixins.py::TestContextMixin::test_context_mixin_xml_tag [32mPASSED[0m[33m [ 43%][0m

#   tests/brown/domain/test_mixins.py::TestContextMixin::test_context_mixin_xml_tag_with_profile [32mPASSED[0m[33m [ 44%][0m

#   tests/brown/domain/test_mixins.py::TestContextMixin::test_context_mixin_xml_tag_with_suffix [32mPASSED[0m[33m [ 45%][0m

#   tests/brown/domain/test_mixins.py::TestMarkdownMixin::test_markdown_mixin_abstract [32mPASSED[0m[33m [ 47%][0m

#   tests/brown/domain/test_mixins.py::TestMarkdownMixin::test_markdown_mixin_implementation [32mPASSED[0m[33m [ 48%][0m

#   tests/brown/domain/test_mixins.py::TestMarkdownMixin::test_markdown_mixin_missing_implementation [32mPASSED[0m[33m [ 50%][0m

#   tests/brown/domain/test_profiles.py::TestProfile::test_profile_creation [32mPASSED[0m[33m [ 51%][0m

#   tests/brown/domain/test_profiles.py::TestProfile::test_profile_xml_tag [32mPASSED[0m[33m [ 52%][0m

#   tests/brown/domain/test_profiles.py::TestProfile::test_profile_to_context [32mPASSED[0m[33m [ 54%][0m

#   tests/brown/domain/test_profiles.py::TestCharacterProfile::test_character_profile_creation [32mPASSED[0m[33m [ 55%][0m

#   tests/brown/domain/test_profiles.py::TestCharacterProfile::test_character_profile_to_context [32mPASSED[0m[33m [ 56%][0m

#   tests/brown/domain/test_profiles.py::TestArticleProfile::test_article_profile_creation [32mPASSED[0m[33m [ 58%][0m

#   tests/brown/domain/test_profiles.py::TestArticleProfile::test_article_profile_to_context [32mPASSED[0m[33m [ 59%][0m

#   tests/brown/domain/test_profiles.py::TestStructureProfile::test_structure_profile_creation [32mPASSED[0m[33m [ 60%][0m

#   tests/brown/domain/test_profiles.py::TestStructureProfile::test_structure_profile_to_context [32mPASSED[0m[33m [ 62%][0m

#   tests/brown/domain/test_profiles.py::TestMechanicsProfile::test_mechanics_profile_creation [32mPASSED[0m[33m [ 63%][0m

#   tests/brown/domain/test_profiles.py::TestMechanicsProfile::test_mechanics_profile_to_context [32mPASSED[0m[33m [ 64%][0m

#   tests/brown/domain/test_profiles.py::TestTerminologyProfile::test_terminology_profile_creation [32mPASSED[0m[33m [ 66%][0m

#   tests/brown/domain/test_profiles.py::TestTerminologyProfile::test_terminology_profile_to_context [32mPASSED[0m[33m [ 67%][0m

#   tests/brown/domain/test_profiles.py::TestTonalityProfile::test_tonality_profile_creation [32mPASSED[0m[33m [ 68%][0m

#   tests/brown/domain/test_profiles.py::TestTonalityProfile::test_tonality_profile_to_context [32mPASSED[0m[33m [ 70%][0m

#   tests/brown/domain/test_profiles.py::TestArticleProfiles::test_article_profiles_creation [32mPASSED[0m[33m [ 71%][0m

#   tests/brown/domain/test_profiles.py::TestArticleProfiles::test_article_profiles_to_context [32mPASSED[0m[33m [ 72%][0m

#   tests/brown/domain/test_research.py::TestResearch::test_research_creation [32mPASSED[0m[33m [ 74%][0m

#   tests/brown/domain/test_research.py::TestResearch::test_research_to_context [32mPASSED[0m[33m [ 75%][0m

#   tests/brown/domain/test_research.py::TestResearch::test_research_empty_content [32mPASSED[0m[33m [ 77%][0m

#   tests/brown/domain/test_research.py::TestResearch::test_research_complex_content [32mPASSED[0m[33m [ 78%][0m

#   tests/brown/domain/test_research.py::TestResearch::test_research_str_representation [32mPASSED[0m[33m [ 79%][0m

#   tests/brown/domain/test_reviews.py::TestReview::test_review_creation [32mPASSED[0m[33m [ 81%][0m

#   tests/brown/domain/test_reviews.py::TestReview::test_review_to_context [32mPASSED[0m[33m [ 82%][0m

#   tests/brown/domain/test_reviews.py::TestReview::test_review_score_validation [32mPASSED[0m[33m [ 83%][0m

#   tests/brown/domain/test_reviews.py::TestReview::test_review_str_representation [32mPASSED[0m[33m [ 85%][0m

#   tests/brown/domain/test_reviews.py::TestArticleReviews::test_article_reviews_creation [32mPASSED[0m[33m [ 86%][0m

#   tests/brown/domain/test_reviews.py::TestArticleReviews::test_article_reviews_to_context [32mPASSED[0m[33m [ 87%][0m

#   tests/brown/domain/test_reviews.py::TestArticleReviews::test_article_reviews_with_article [32mPASSED[0m[33m [ 89%][0m

#   tests/brown/domain/test_reviews.py::TestArticleReviews::test_article_reviews_without_article [32mPASSED[0m[33m [ 90%][0m

#   tests/brown/domain/test_reviews.py::TestArticleReviews::test_article_reviews_empty [32mPASSED[0m[33m [ 91%][0m

#   tests/brown/domain/test_reviews.py::TestArticleReviews::test_article_reviews_single [32mPASSED[0m[33m [ 93%][0m

#   tests/brown/domain/test_reviews.py::TestArticleReviews::test_article_reviews_str_representation [32mPASSED[0m[33m [ 94%][0m

#   tests/brown/domain/test_reviews.py::TestHumanFeedback::test_human_feedback_creation [32mPASSED[0m[33m [ 95%][0m

#   tests/brown/domain/test_reviews.py::TestHumanFeedback::test_human_feedback_to_context [32mPASSED[0m[33m [ 97%][0m

#   tests/brown/domain/test_reviews.py::TestSelectedTextReviews::test_selected_text_reviews_creation [32mPASSED[0m[33m [ 98%][0m

#   tests/brown/domain/test_reviews.py::TestSelectedTextReviews::test_selected_text_reviews_to_context [32mPASSED[0m[33m [100%][0m

#   

#   [33m=============================== warnings summary ===============================[0m

#   src/brown/models/fake_model.py:4

#     /Users/jai/Documents/code-repo/agentic-ai-engineering-course/lessons/writing_workflow/src/brown/models/fake_model.py:4: DeprecationWarning: `langchain-community` is being sunset and is no longer actively maintained. See https://github.com/langchain-ai/langchain-community/issues/674 for details and migration guidance toward standalone integration packages.

#       from langchain_community.chat_models import FakeListChatModel

#   

#   -- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html

#   [33m======================== [32m74 passed[0m, [33m[1m1 warning[0m[33m in 0.05s[0m[33m =========================[0m


!CONFIG_FILE=configs/debug.yaml uv run pytest tests/brown/nodes/ -v
# Output:
#   [1m[33mwarning[39m[0m[1m:[0m [1m`VIRTUAL_ENV=/Users/jai/Documents/code-repo/agentic-ai-engineering-course/.venv` does not match the project environment path `.venv` and will be ignored; use `--active` to target the active environment instead[0m

#   [1m============================= test session starts ==============================[0m

#   platform darwin -- Python 3.14.4, pytest-9.0.3, pluggy-1.6.0 -- /Users/jai/Documents/code-repo/agentic-ai-engineering-course/lessons/writing_workflow/.venv/bin/python

#   cachedir: .pytest_cache

#   rootdir: /Users/jai/Documents/code-repo/agentic-ai-engineering-course/lessons/writing_workflow

#   configfile: pyproject.toml

#   plugins: asyncio-1.4.0, langsmith-0.8.14, opik-2.0.62, anyio-4.13.0

#   asyncio: mode=Mode.STRICT, debug=False, asyncio_default_fixture_loop_scope=None, asyncio_default_test_loop_scope=function

#   collected 37 items                                                             [0m

#   

#   tests/brown/nodes/test_article_reviewer.py::TestArticleReviewer::test_article_reviewer_initialization [32mPASSED[0m[33m [  2%][0m

#   tests/brown/nodes/test_article_reviewer.py::TestArticleReviewer::test_article_reviewer_ainvoke_success [32mPASSED[0m[33m [  5%][0m

#   tests/brown/nodes/test_article_reviewer.py::TestArticleReviewer::test_article_reviewer_structured_output [32mPASSED[0m[33m [  8%][0m

#   tests/brown/nodes/test_article_reviewer.py::TestArticleReviewer::test_article_reviewer_empty_article [32mPASSED[0m[33m [ 10%][0m

#   tests/brown/nodes/test_article_reviewer.py::TestArticleReviewer::test_article_reviewer_multiple_reviews [32mPASSED[0m[33m [ 13%][0m

#   tests/brown/nodes/test_article_reviewer.py::TestArticleReviewer::test_article_reviewer_requires_mocked_response_for_fake_model [32mPASSED[0m[33m [ 16%][0m

#   tests/brown/nodes/test_article_reviewer.py::TestArticleReviewer::test_article_reviewer_selected_text_initialization [32mPASSED[0m[33m [ 18%][0m

#   tests/brown/nodes/test_article_reviewer.py::TestArticleReviewer::test_article_reviewer_selected_text_ainvoke [32mPASSED[0m[33m [ 21%][0m

#   tests/brown/nodes/test_article_reviewer.py::TestArticleReviewer::test_article_reviewer_selected_text_with_human_feedback [32mPASSED[0m[33m [ 24%][0m

#   tests/brown/nodes/test_article_reviewer.py::TestArticleReviewer::test_article_reviewer_article_property [32mPASSED[0m[33m [ 27%][0m

#   tests/brown/nodes/test_article_writer.py::TestArticleWriter::test_article_writer_initialization [32mPASSED[0m[33m [ 29%][0m

#   tests/brown/nodes/test_article_writer.py::TestArticleWriter::test_article_writer_ainvoke_success [32mPASSED[0m[33m [ 32%][0m

#   tests/brown/nodes/test_article_writer.py::TestArticleWriter::test_article_writer_with_media_items [32mPASSED[0m[33m [ 35%][0m

#   tests/brown/nodes/test_article_writer.py::TestArticleWriter::test_article_writer_with_reviews [32mPASSED[0m[33m [ 37%][0m

#   tests/brown/nodes/test_article_writer.py::TestArticleWriter::test_article_writer_empty_input [32mPASSED[0m[33m [ 40%][0m

#   tests/brown/nodes/test_article_writer.py::TestArticleWriter::test_article_writer_requires_mocked_response_for_fake_model [32mPASSED[0m[33m [ 43%][0m

#   tests/brown/nodes/test_article_writer.py::TestArt

[... Content truncated due to length ...]

</details>

</golden_source>

<golden_source type="guideline_youtube">
## YouTube Video Transcripts (from Article Guidelines)

_No guideline YouTube video transcripts found._

</golden_source>

<golden_source type="guideline_urls">
## Additional Sources Scraped (from Article Guidelines)

<details>
<summary>Integration with GitHub Actions, uv docs</summary>

# Integration with GitHub Actions, uv docs

**Source URL:** <https://docs.astral.sh/uv/guides/integration/github/>

## [Installation](https://docs.astral.sh/uv/guides/integration/github/\#installation)

For use with GitHub Actions, we recommend the official
[`astral-sh/setup-uv`](https://github.com/astral-sh/setup-uv) action, which installs uv, adds it to
PATH, (optionally) persists the cache, and more, with support for all uv-supported platforms.

To install the latest version of uv:

example.yml

```
name: Example

jobs:
  uv-example:
    name: python
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v6

      - name: Install uv
        uses: astral-sh/setup-uv@08807647e7069bb48b6ef5acd8ec9567f424441b # v8.1.0
```

It is considered best practice to pin to a specific uv version, e.g., with:

example.yml

```
name: Example

jobs:
  uv-example:
    name: python
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v6

      - name: Install uv
        uses: astral-sh/setup-uv@08807647e7069bb48b6ef5acd8ec9567f424441b # v8.1.0
        with:
          # Install a specific version of uv.
          version: "0.11.21"
```

## [Setting up Python](https://docs.astral.sh/uv/guides/integration/github/\#setting-up-python)

Python can be installed with the `python install` command:

example.yml

```
name: Example

jobs:
  uv-example:
    name: python
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v6

      - name: Install uv
        uses: astral-sh/setup-uv@08807647e7069bb48b6ef5acd8ec9567f424441b # v8.1.0

      - name: Set up Python
        run: uv python install
```

This will respect the Python version pinned in the project.

Alternatively, the official GitHub `setup-python` action can be used. This can be faster, because
GitHub caches the Python versions alongside the runner.

Set the
[`python-version-file`](https://github.com/actions/setup-python/blob/main/docs/advanced-usage.md#using-the-python-version-file-input)
option to use the pinned version for the project:

example.yml

```
name: Example

jobs:
  uv-example:
    name: python
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v6

      - name: "Set up Python"
        uses: actions/setup-python@v6
        with:
          python-version-file: ".python-version"

      - name: Install uv
        uses: astral-sh/setup-uv@08807647e7069bb48b6ef5acd8ec9567f424441b # v8.1.0
```

Or, specify the `pyproject.toml` file to ignore the pin and use the latest version compatible with
the project's `requires-python` constraint:

example.yml

```
name: Example

jobs:
  uv-example:
    name: python
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v6

      - name: "Set up Python"
        uses: actions/setup-python@v6
        with:
          python-version-file: "pyproject.toml"

      - name: Install uv
        uses: astral-sh/setup-uv@08807647e7069bb48b6ef5acd8ec9567f424441b # v8.1.0
```

## [Multiple Python versions](https://docs.astral.sh/uv/guides/integration/github/\#multiple-python-versions)

When using a matrix to test multiple Python versions, set the Python version using
`astral-sh/setup-uv`, which will override the Python version specification in the `pyproject.toml`
or `.python-version` files:

example.yml

```
jobs:
  build:
    name: continuous-integration
    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version:
          - "3.10"
          - "3.11"
          - "3.12"

    steps:
      - uses: actions/checkout@v6

      - name: Install uv and set the Python version
        uses: astral-sh/setup-uv@08807647e7069bb48b6ef5acd8ec9567f424441b # v8.1.0
        with:
          python-version: ${{ matrix.python-version }}
```

If not using the `setup-uv` action, you can set the `UV_PYTHON` environment variable:

example.yml

```
jobs:
  build:
    name: continuous-integration
    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version:
          - "3.10"
          - "3.11"
          - "3.12"
    env:
      UV_PYTHON: ${{ matrix.python-version }}
    steps:
      - uses: actions/checkout@v6
```

## [Syncing and running](https://docs.astral.sh/uv/guides/integration/github/\#syncing-and-running)

Once uv and Python are installed, the project can be installed with `uv sync` and commands can be
run in the environment with `uv run`:

example.yml

```
name: Example

jobs:
  uv-example:
    name: python
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v6

      - name: Install uv
        uses: astral-sh/setup-uv@08807647e7069bb48b6ef5acd8ec9567f424441b # v8.1.0

      - name: Install the project
        run: uv sync --locked --all-extras --dev

      - name: Run tests
        # For example, using `pytest`
        run: uv run pytest tests
```

Tip

The
[`UV_PROJECT_ENVIRONMENT` setting](https://docs.astral.sh/uv/concepts/projects/config/#project-environment-path) can
be used to install to the system Python environment instead of creating a virtual environment.

## [Caching](https://docs.astral.sh/uv/guides/integration/github/\#caching)

It may improve CI times to store uv's cache across workflow runs.

The [`astral-sh/setup-uv`](https://github.com/astral-sh/setup-uv) has built-in support for
persisting the cache:

example.yml

```
- name: Enable caching
  uses: astral-sh/setup-uv@08807647e7069bb48b6ef5acd8ec9567f424441b # v8.1.0
  with:
    enable-cache: true
```

Alternatively, you can manage the cache manually with the `actions/cache` action:

example.yml

```
jobs:
  install_job:
    env:
      # Configure a constant location for the uv cache
      UV_CACHE_DIR: /tmp/.uv-cache

    steps:
      # ... setup up Python and uv ...

      - name: Restore uv cache
        uses: actions/cache@v5
        with:
          path: /tmp/.uv-cache
          key: uv-${{ runner.os }}-${{ hashFiles('uv.lock') }}
          restore-keys: |
            uv-${{ runner.os }}-${{ hashFiles('uv.lock') }}
            uv-${{ runner.os }}

      # ... install packages, run tests, etc ...

      - name: Minimize uv cache
        run: uv cache prune --ci
```

The `uv cache prune --ci` command is used to reduce the size of the cache and is optimized for CI.
Its effect on performance is dependent on the packages being installed.

Tip

If using `uv pip`, use `requirements.txt` instead of `uv.lock` in the cache key.

Note

When using non-ephemeral, self-hosted runners the default cache directory can grow unbounded.
In this case, it may not be optimal to share the cache between jobs. Instead, move the cache
inside the GitHub Workspace and remove it once the job finishes using a
[Post Job Hook](https://docs.github.com/en/actions/hosting-your-own-runners/managing-self-hosted-runners/running-scripts-before-or-after-a-job).

```
install_job:
  env:
    # Configure a relative location for the uv cache
    UV_CACHE_DIR: ${{ github.workspace }}/.cache/uv
```

Using a post job hook requires setting the `ACTIONS_RUNNER_HOOK_JOB_STARTED` environment
variable on the self-hosted runner to the path of a cleanup script such as the one shown below.

clean-uv-cache.sh

```
#!/usr/bin/env sh
uv cache clean
```

## [Using `uv pip`](https://docs.astral.sh/uv/guides/integration/github/\#using-uv-pip)

If using the `uv pip` interface instead of the uv project interface, uv requires a virtual
environment by default. To allow installing packages into the system environment, use the `--system`
flag on all `uv` invocations or set the `UV_SYSTEM_PYTHON` variable.

The `UV_SYSTEM_PYTHON` variable can be defined in at different scopes.

Opt-in for the entire workflow by defining it at the top level:

example.yml

```
env:
  UV_SYSTEM_PYTHON: 1

jobs: ...
```

Or, opt-in for a specific job in the workflow:

example.yml

```
jobs:
  install_job:
    env:
      UV_SYSTEM_PYTHON: 1
    ...
```

Or, opt-in for a specific step in a job:

example.yml

```
steps:
  - name: Install requirements
    run: uv pip install -r requirements.txt
    env:
      UV_SYSTEM_PYTHON: 1
```

To opt-out again, the `--no-system` flag can be used in any uv invocation.

## [Private repos](https://docs.astral.sh/uv/guides/integration/github/\#private-repos)

If your project has [dependencies](https://docs.astral.sh/uv/concepts/projects/dependencies/#git) on private GitHub
repositories, you will need to configure a [personal access token (PAT)](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens) to allow uv to fetch
them.

After creating a PAT that has read access to the private repositories, add it as a [repository\\
secret](https://docs.github.com/en/actions/security-for-github-actions/security-guides/using-secrets-in-github-actions#creating-secrets-for-a-repository).

Then, you can use the [`gh`](https://cli.github.com/) CLI (which is installed in GitHub Actions
runners by default) to configure a
[credential helper for Git](https://docs.astral.sh/uv/concepts/authentication/git/#git-credential-helpers) to use the
PAT for queries to repositories hosted on `github.com`.

For example, if you called your repository secret `MY_PAT`:

example.yml

```
steps:
  - name: Register the personal access token
    run: echo "${{ secrets.MY_PAT }}" | gh auth login --with-token
  - name: Configure the Git credential helper
    run: gh auth setup-git
```

## [Publishing to PyPI](https://docs.astral.sh/uv/guides/integration/github/\#publishing-to-pypi)

uv can be used to build and publish your package to PyPI from GitHub Actions. We provide a
standalone example alongside this guide in
[astral-sh/trusted-publishing-examples](https://github.com/astral-sh/trusted-publishing-examples).
The workflow uses [trusted publishing](https://docs.pypi.org/trusted-publishers/), so no credentials
need to be configured.

In the example workflow, we use a script to test that the source distribution and the wheel are both
functional and we didn't miss any files. This step is recommended, but optional.

First, add a release workflow to your project:

.github/workflows/release.yml

```
name: "Publish release to PyPI"

on:
  push:
    tags:
      # Publish on any tag starting with a `v`, e.g., v0.1.0
      - v*

jobs:
  run:
    runs-on: ubuntu-latest
    environment:
      name: pypi
    permissions:
      id-token: write
      contents: read
    steps:
      - name: Checkout
        uses: actions/checkout@v6
      - name: Install uv
        uses: astral-sh/setup-uv@08807647e7069bb48b6ef5acd8ec9567f424441b # v8.1.0
      - name: Install Python 3.13
        run: uv python install 3.13
      - name: Build
        run: uv build
      # Check that basic features work and we didn't miss to include crucial files
      - name: Smoke test (wheel)
        run: uv run --isolated --no-project --with dist/*.whl tests/smoke_test.py
      - name: Smoke test (source distribution)
        run: uv run --isolated --no-project --with dist/*.tar.gz tests/smoke_test.py
      - name: Publish
        run: uv publish
```

Then, create the environment defined in the workflow in the GitHub repository under "Settings" ->
"Environments".

https://docs.astral.sh/uv/assets/github-add-environment.png

Add a [trusted publisher](https://docs.pypi.org/trusted-publishers/adding-a-publisher/) to your PyPI
project in the project settings under "Publishing". Ensure that all fields match with your GitHub
configuration.

https://docs.astral.sh/uv/assets/pypi-add-trusted-publisher.png

After saving:

https://docs.astral.sh/uv/assets/pypi-with-trusted-publisher.png

Finally, tag a release and push it. Make sure it starts with `v` to match the pattern in the
workflow.

```
$ git tag -a v0.1.0 -m v0.1.0
$ git push --tags
```

</details>

<details>
<summary>Integration with pre-commit, uv docs</summary>

# Integration with pre-commit, uv docs

**Source URL:** <https://docs.astral.sh/uv/guides/integration/pre-commit/>

An official pre-commit hook is provided at
[`astral-sh/uv-pre-commit`](https://github.com/astral-sh/uv-pre-commit).

To use uv with pre-commit, add one of the following examples to the `repos` list in the
`.pre-commit-config.yaml`.

To make sure your `uv.lock` file is up to date even if your `pyproject.toml` file was changed:

.pre-commit-config.yaml

```
repos:
  - repo: https://github.com/astral-sh/uv-pre-commit
    # uv version.
    rev: 0.11.21
    hooks:
      - id: uv-lock
```

To keep a `requirements.txt` file in sync with your `uv.lock` file:

.pre-commit-config.yaml

```
repos:
  - repo: https://github.com/astral-sh/uv-pre-commit
    # uv version.
    rev: 0.11.21
    hooks:
      - id: uv-export
```

To compile requirements files:

.pre-commit-config.yaml

```
repos:
  - repo: https://github.com/astral-sh/uv-pre-commit
    # uv version.
    rev: 0.11.21
    hooks:
      # Compile requirements
      - id: pip-compile
        args: [requirements.in, -o, requirements.txt]
```

To compile alternative requirements files, modify `args` and `files`:

.pre-commit-config.yaml

```
repos:
  - repo: https://github.com/astral-sh/uv-pre-commit
    # uv version.
    rev: 0.11.21
    hooks:
      # Compile requirements
      - id: pip-compile
        args: [requirements-dev.in, -o, requirements-dev.txt]
        files: ^requirements-dev\.(in|txt)$
```

To run the hook over multiple files at the same time, add additional entries:

.pre-commit-config.yaml

```
repos:
  - repo: https://github.com/astral-sh/uv-pre-commit
    # uv version.
    rev: 0.11.21
    hooks:
      # Compile requirements
      - id: pip-compile
        name: pip-compile requirements.in
        args: [requirements.in, -o, requirements.txt]
      - id: pip-compile
        name: pip-compile requirements-dev.in
        args: [requirements-dev.in, -o, requirements-dev.txt]
        files: ^requirements-dev\.(in|txt)$
```

</details>

<details>
<summary>Lesson 31: Continuous Integration (CI) for AI Engineering</summary>

**Source URL:** <https://colab.research.google.com/github/louisfb01/agent-course-notebooks/blob/main/notebooks/lesson_31_notebook.ipynb#scrollTo=b30eba1a>

# Lesson 31: Continuous Integration (CI) for AI Engineering

In this notebook, we'll practice the CI essentials covered in Lesson 31. You'll run formatting checks, linting, and tests to see how CI tools maintain code quality.

**Learning Objectives:**

- Understand Brown's CI configuration files
- Practice running formatting and linting checks with Ruff
- Learn to fix code quality issues automatically
- Run unit tests with mocked LLM responses

## 1. Setup

First, let's navigate to the Brown writing agent directory.

%pip install -q agentic-ai-engineering-course

%pip check

import IPython; IPython.Application.instance().kernel.do_shutdown(True)

Restart the notebook before executing the next cell.

# navigate to the writing_workflow directory

%cd /usr/local/lib/python3.12/dist-packages/writing_workflow

## 2. Viewing Brown's CI Configuration

Let's examine Brown's actual CI configuration files to understand how CI is set up.

### 2.1 Pre-commit Configuration

The `.pre-commit-config.yaml` file defines Git hooks that run automatically before each commit. These hooks catch issues immediately in your local development environment.

Brown's pre-commit configuration includes three types of hooks:

1.  **validate-pyproject** - Validates that `pyproject.toml` is structurally correct
2.  **prettier** - Formats YAML and JSON configuration files consistently
3.  **ruff-check** and **ruff-format** - Lints and formats Python code

# Show the content of the file

!cat .pre-commit-config.yaml

```
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
    rev: v0.12.1
    hooks:
      # Run the linter.
      - id: ruff-check
        args: [--fix, --exit-non-zero-on-fix]
      # Run the formatter.
      - id: ruff-format
```

### 2.2 Ruff Configuration

The `pyproject.toml` file contains Ruff's configuration in the `[tool.ruff]` section. This defines:

-   **target-version**: Which Python version to target (py312 for Python 3.12)
-   **line-length**: Maximum line length (140 characters for modern screens)
-   **select rules**: Which linting rules to enable (F=Pyflakes, E=pycodestyle, I=isort)
-   **known-first-party**: How to group imports correctly

# Show the content of the file related to ruff

!grep -A 20 "\[tool.ruff\]" pyproject.toml

```
[tool.ruff]
target-version = "py312"
line-length = 140

[tool.ruff.lint]
select = [\
    "F",    # Pyflakes\
    "E",    # pycodestyle errors\
    "I",    # isort\
]

[tool.ruff.lint.isort]
known-first-party = ["src", "tests"]

[tool.pytest.ini_options]
pythonpath = ["src"]
```

### 2.3 Makefile QA Targets

The Makefile provides convenient shortcuts for running CI commands. Instead of typing long `uv run ruff format --check src/ tests/ scripts/` commands, you can simply run `make format-check`.

The Makefile defines:

-   **QA\_FOLDERS** - Which directories to check (src/, tests/, scripts/)
-   **format-check/format-fix** - Formatting commands
-   **lint-check/lint-fix** - Linting commands
-   **tests** - Test suite with the correct configuration
-   **pre-commit** - Manual pre-commit hook execution

# Show the commands in the Makefile related to QA

!sed -n '/# --- Tests & QA ---/,$p' Makefile | tail -n +2

```
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

## 3. Pre-commit Hooks (Local Enforcement)

Pre-commit hooks run automatically before each commit, catching issues before they enter version control.

> If running from Colab: we need to initialize the "writing_workflow" folder as a git repository first to use the pre-commit hooks.

Let's run them manually:

!git init

!uv run pre-commit run --files ./**/*

```
warning: `VIRTUAL_ENV=/Users/fabio/Desktop/course-ai-agents/.venv` does not match the project environment path `.venv` and will be ignored; use `--active` to target the active environment instead
Validate pyproject.toml..............................(no files to check)Skipped
prettier.................................................................Passed
ruff check...............................................................Passed
ruff format..............................................................Passed
```

These hooks will:

1.  Validate your `pyproject.toml` structure
2.  Format all YAML/JSON files with prettier
3.  Lint Python code with ruff-check (and auto-fix issues)
4.  Format Python code with ruff-format

If any hook fails, you'll see the error, fix it, re-stage the files, and commit again. This tight feedback loop keeps code quality high.

## 4. Running Formatting Checks

Now let's practice using Ruff's formatter. Instead of running it on Brown's existing code (which is already formatted), we'll create a simple Python file with formatting issues and fix them.

### 4.1 Create a Test File with Formatting Issues

%%bash

# Create a Python file with various formatting issues

cat > test_formatting.py << 'EOF'

# This file has formatting issues

def badly_formatted_function(x,y,z):

    result=x+y+z

    my_list=[1,2,3,4,5,6,7,8,9,10]

    my_dict={"key1":"value1","key2":"value2","key3":"value3"}

    if result>10:

        print("Result is greater than 10")

    else:

        print("Result is 10 or less")

    return result

class BadlyFormattedClass:

    def __init__(self,name,age):

        self.name=name

        self.age=age

    def get_info(self):

        return f"{self.name} is {self.age} years old"

EOF

echo "Created test_formatting.py"

```
Created test_formatting.py
```

### 4.2 Check Formatting (Without Fixing)

Let's check if the file has formatting issues without modifying it:

!uv run ruff format --check test_formatting.py

```
warning: `VIRTUAL_ENV=/Users/fabio/Desktop/course-ai-agents/.venv` does not match the project environment path `.venv` and will be ignored; use `--active` to target the active environment instead
Would reformat: test_formatting.py
1 file would be reformatted
```

You'll see that Ruff reports the file would be reformatted. The `--check` flag means Ruff only reports issues without changing the file.

### 4.3 Auto-fix Formatting Issues

Now let's fix all the formatting issues automatically:

!uv run ruff format test_formatting.py

```
warning: `VIRTUAL_ENV=/Users/fabio/Desktop/course-ai-agents/.venv` does not match the project environment path `.venv` and will be ignored; use `--active` to target the active environment instead
1 file reformatted
```

Ruff will reformat the file to follow consistent style rules. Let's see the result:

cat test_formatting.py

```
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

Notice how Ruff has:

-   Fixed spacing around operators (`x+y+z` → `x + y + z`)
-   Added proper spacing in function signatures
-   Formatted lists and dictionaries consistently
-   Fixed class definition spacing

Let's remove the file now:

!rm test_formatting.py

## 5. Running Linting Checks

Linting goes beyond formatting—it checks for bugs, code quality issues, and best practices. Let's create a file with linting issues and fix them.

### 5.1 Create a Test File with Linting Issues

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
Created test_linting.py
```

### 5.2 Check Linting Issues (Without Fixing)

!uv run ruff check test_linting.py

```
warning: `VIRTUAL_ENV=/Users/fabio/Desktop/course-ai-agents/.venv` does not match the project environment path `.venv` and will be ignored; use `--active` to target the active environment instead
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

Ruff will report several issues:

-   **F401**: Unused import (`json` is imported but never used)
-   **F811**: Duplicate import (`sys` is imported twice)
-   **F821**: Undefined name (`some_undefined_function` doesn't exist)

### 5.3 Auto-fix Linting Issues (Where Possible)

!uv run ruff check --fix test_linting.py

```
warning: `VIRTUAL_ENV=/Users/fabio/Desktop/course-ai-agents/.venv` does not match the project environment path `.venv` and will be ignored; use `--active` to target the active environment instead
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

Ruff will automatically fix:

-   Remove unused imports
-   Remove duplicate imports

But it won't fix the undefined name. That requires manual intervention since it's a logic error.

cat test_linting.py

```
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

Let's remove the file now:

!rm test_linting.py

## 6. Running Unit Tests

Now let's run Brown's test suite with mocked LLM responses. The tests use fake models instead of real LLMs, making them fast, deterministic, and free.

!CONFIG_FILE=configs/debug.yaml uv run pytest -v

```
warning: `VIRTUAL_ENV=/Users/fabio/Desktop/course-ai-agents/.venv` does not match the project environment path `.venv` and will be ignored; use `--active` to target the active environment instead
============================= test session starts ==============================
platform darwin -- Python 3.12.11, pytest-8.4.2, pluggy-1.6.0 -- /Users/fabio/Desktop/course-ai-agents/lessons/writing_workflow/.venv/bin/python
cachedir: .pytest_cache
rootdir: /Users/fabio/Desktop/course-ai-agents/lessons/writing_workflow
configfile: pyproject.toml
plugins: asyncio-1.2.0, anyio-4.11.0, langsmith-0.4.38, opik-1.8.96
asyncio: mode=Mode.STRICT, debug=False, asyncio_default_fixture_loop_scope=None, asyncio_default_test_loop_scope=function
collected 214 items

tests/brown/data/test_loaders.py::TestMarkdownArticleLoader::test_article_loader_success PASSED [  0%]
tests/brown/data/test_loaders.py::TestMarkdownArticleLoader::test_article_loader_file_not_found PASSED [  0%]
tests/brown/data/test_loaders.py::TestMarkdownArticleGuidelineLoader::test_article_guideline_loader_success PASSED [  1%]
tests/brown/data/test_loaders.py::TestMarkdownArticleGuidelineLoader::test_article_guideline_loader_file_not_found PASSED [  1%]
tests/brown/data/test_loaders.py::TestMarkdownResearchLoader::test_research_loader_success PASSED [  2%]
tests/brown/data/test_loaders.py::TestMarkdownResearchLoader::test_research_loader_with_markdown_links PASSED [  2%]
tests/brown/data/test_loaders.py::TestMarkdownResearchLoader::test_research_loader_file_not_found PASSED [  3%]
tests/brown/data/test_loaders.py::TestMarkdownArticleProfilesLoader::test_profiles_loader_success PASSED [  3%]
tests/brown/data/test_loaders.py::TestMarkdownArticleProfilesLoader::test_profiles_loader_missing_file PASSED [  4%]
tests/brown/data/test_loaders.py::TestMarkdownArticleProfilesLoader::test_profiles_loader_get_supported_profiles PASSED [  4%]
tests/brown/data/test_loaders.py::TestMarkdownArticleExampleLoader::test_article_example_loader_success PASSED [  5%]
tests/brown/data/test_loaders.py::TestMarkdownArticleExampleLoader::test_article_example_loader_empty_dir PASSED [  5%]
tests/brown/data/test_loaders.py::TestMarkdownArticleExampleLoader::test_article_example_loader_dir_not_found PASSED [  6%]
tests/brown/data/test_loaders.py::TestMarkdownArticleExampleLoader::test_article_example_loader_ignores_non_md_files PASSED [  6%]
tests/brown/data/test_renderers.py::TestMarkdownArticleRenderer::test_article_markdown_renderer PASSED [  7%]
tests/brown/data/test_renderers.py::TestMarkdownArticleRenderer::test_article_markdown_renderer_overwrites_existing PASSED [  7%]
tests/brown/data/test_renderers.py::TestMarkdownArticleRenderer::test_article_markdown_renderer_empty_content PASSED [  7%]
tests/brown/data/test_renderers.py::TestMarkdownArticleReviewsRenderer::test_article_reviews_context_renderer PASSED [  8%]
tests/brown/data/test_renderers.py::TestMarkdownArticleReviewsRenderer::test_article_reviews_context_renderer_overwrites_existing PASSED [  8%]
tests/brown/data/test_renderers.py::TestMarkdownArticleReviewsRenderer::test_article_reviews_context_renderer_empty_reviews PASSED [  9%]
tests/brown/data/test_renderers.py::TestMarkdownArticleReviewsRenderer::test_article_reviews_context_renderer_without_article PASSED [  9%]
tests/brown/domain/test_articles.py::TestArticle::test_article_creation PASSED [ 10%]
tests/brown/domain/test_articles.py::TestArticle::test_article_to_context PASSED [ 10%]
tests/brown/domain/test_articles.py::TestArticle::test_article_to_markdown PASSED [ 11%]
tests/brown/domain/test_articles.py::TestArticle::test_article_str_representation PASSED [ 11%]
tests/brown/domain/test_articles.py::TestArticle::test_article_empty_content PASSED [ 12%]
tests/brown/domain/test_articles.py::TestSelectedText::test_selected_text_creation PASSED [ 12%]
tests/brown/domain/test_articles.py::TestSelectedText::test_selected_text_to_context PASSED [ 13%]
tests/brown/domain/test_articles.py::TestSelectedText::test_selected_text_single_line PASSED [ 13%]
tests/brown/domain/test_articles.py::TestArticleExample::test_article_example_creation PASSED [ 14%]
tests/brown/domain/test_articles.py::TestArticleExample::test_article_example_to_context PASSED [ 14%]
tests/brown/domain/test_articles.py::TestArticleExample::test_article_example_str_representation PASSED [ 14%]
tests/brown/domain/test_articles.py::TestArticleExamples::test_article_examples_creation PASSED [ 15%]
tests/brown/domain/test_articles.py::TestArticleExamples::test_article_examples_to_context PASSED [ 15%]
tests/brown/domain/test_articles.py::TestArticleExamples::test_article_examples_empty PASSED [ 16%]
tests/brown/domain/test_articles.py::TestArticleExamples::test_article_examples_single PASSED [ 16%]
tests/brown/domain/test_guidelines.py::TestArticleGuideline::test_article_guideline_creation PASSED [ 17%]
tests/brown/domain/test_guidelines.py::TestArticleGuideline::test_article_guideline_to_context PASSED [ 17%]
tests/brown/domain/test_guidelines.py::TestArticleGuideline::test_article_guideline_empty_content PASSED [ 18%]
tests/brown/domain/test_guidelines.py::TestArticleGuideline::test_article_guideline_complex_content PASSED [ 18%]
tests/brown/domain/test_media_items.py::TestMediaItem::test_media_item_creation PASSED [ 19%]
tests/brown/domain/test_media_items.py::TestMediaItem::test_media_item_to_context PASSED [ 19%]
tests/brown/domain/test_media_items.py::TestMediaItem::test_media_item_different_types PASSED [ 20%]
tests/brown/domain/test_media_items.py::TestMediaItem::test_media_item_str_representation PASSED [ 20%]
tests/brown/domain/test_media_items.py::TestMediaItems::test_media_items_creation PASSED [ 21%]
tests/brown/domain/test_media_items.py::TestMediaItems::test_media_items_to_context PASSED [ 21%]
tests/brown/domain/test_media_items.py::TestMediaItems::test_media_items_empty PASSED [ 21%]
tests/brown/domain/test_media_items.py::TestMediaItems::test_media_items_single PASSED [ 22%]
tests/brown/domain/test_media_items.py::TestMediaItems::test_media_items_str_representation PASSED [ 22%]
tests/brown/domain/test_media_items.py::TestMediaItems::test_media_items_build_classmethod PASSED [ 23%]
tests/brown/domain/test_media_items.py::TestMediaItems::test_are_available_only_in_source_property PASSED [ 23%]
tests/brown/domain/test_media_items.py::TestMermaidDiagram::test_mermaid_diagram_creation PASSED [ 24%]
tests/brown/domain/test_mixins.py::TestContextMixin::test_context_mixin_xml_tag PASSED [ 24%]
tests/brown/domain/test_mixins.py::TestContextMixin::test_context_mixin_xml_tag_with_profile PASSED [ 25%]
tests/brown/domain/test_mixins.py::TestContextMixin::test_context_mixin_xml_tag_with_suffix PASSED [ 25%]
tests/brown/domain/test_mixins.py::TestMarkdownMixin::test_markdown_mixin_abstract PASSED [ 26%]
tests/brown/domain/test_mixins.py::TestMarkdownMixin::test_markdown_mixin_implementation PASSED [ 26%]
tests/brown/domain/test_mixins.py::TestMarkdownMixin::test_markdown_mixin_missing_implementation PASSED [ 27%]
tests/brown/domain/test_profiles.py::TestProfile::test_profile_creation PASSED [ 27%]
tests/brown/domain/test_profiles.py::TestProfile::test_profile_xml_tag PASSED [ 28%]
tests/brown/domain/test_profiles.py::TestProfile::test_profile_to_context PASSED [ 28%]
tests/brown/domain/test_profiles.py::TestCharacterProfile::test_character_profile_creation PASSED [ 28%]
tests/brown/domain/test_profiles.py::TestCharacterProfile::test_character_profile_to_context PASSED [ 29%]
tests/brown/domain/test_profiles.py::TestArticleProfile::test_article_profile_creation PASSED [ 29%]
tests/brown/domain/test_profiles.py::TestArticleProfile::test_article_profile_to_context PASSED [ 30%]
tests/brown/domain/test_profiles.py::TestStructureProfile::test_structure_profile_creation PASSED [ 30%]
tests/brown/domain/test_profiles.py::TestStructureProfile::test_structure_profile_to_context PASSED [ 31%]
tests/brown/domain/test_profiles.py::TestMechanicsProfile::test_mechanics_profile_creation PASSED [ 31%]
tests/brown/domain/test_profiles.py::TestMechanicsProfile::test_mechanics_profile_to_context PASSED [ 32%]
tests/brown/domain/test_profiles.py::TestTerminologyProfile::test_terminology_profile_creation PASSED [ 32%]
tests/brown/domain/test_profiles.py::TestTerminologyProfile::test_terminology_profile_to_context PASSED [ 33%]
tests/brown/domain/test_profiles.py::TestTonalityProfile::test_tonality_profile_creation PASSED [ 33%]
tests/brown/domain/test_profiles.py::TestTonalityProfile::test_tonality_profile_to_context PASSED [ 34%]
tests/brown/domain/test_profiles.py::TestArticleProfiles::test_article_profiles_creation PASSED [ 34%]
tests/brown/domain/test_profiles.py::TestArticleProfiles::test_article_profiles_to_context PASSED [ 35%]
tests/brown/domain/test_research.py::TestResearch::test_research_creation PASSED [ 35%]
tests/brown/domain/test_research.py::TestResearch::test_research_to_context PASSED [ 35%]
tests/brown/domain/test_research.py::TestResearch::test_research_empty_content PASSED [ 36%]
tests/brown/domain/test_research.py::TestResearch::test_research_complex_content PASSED [ 36%]
tests/brown/domain/test_research.py::TestResearch::test_research_str_representation PASSED [ 37%]
tests/brown/domain/test_reviews.py::TestReview::test_review_creation PASSED [ 37%]
tests/brown/domain/test_reviews.py::TestReview::test_review_to_context PASSED [ 38%]
tests/brown/domain/test_reviews.py::TestReview::test_review_score_validation PASSED [ 38%]
tests/brown/domain/test_reviews.py::TestReview::test_review_str_representation PASSED [ 39%]
tests/brown/domain/test_reviews.py::TestArticleReviews::test_article_reviews_creation PASSED [ 39%]
tests/brown/domain/test_reviews.py::TestArticleReviews::test_article_reviews_to_context PASSED [ 40%]
tests/brown/domain/test_reviews.py::TestArticleReviews::test_article_reviews_with_article PASSED [ 40%]
tests/brown/domain/test_reviews.py::TestArticleReviews::test_article_reviews_without_article PASSED [ 41%]
tests/brown/domain/test_reviews.py::TestArticleReviews::test_article_reviews_empty PASSED [ 41%]
tests/brown/domain/test_reviews.py::TestArticleReviews::test_article_reviews_single PASSED [ 42%]
tests/brown/domain/test_reviews.py::TestArticleReviews::test_article_reviews_str_representation PASSED [ 42%]
tests/brown/domain/test_reviews.py::TestHumanFeedback::test_human_feedback_creation PASSED [ 42%]
tests/brown/domain/test_reviews.py::TestHumanFeedback::test_human_feedback_to_context PASSED [ 43%]
tests/brown/domain/test_reviews.py::TestSelectedTextReviews::test_selected_text_reviews_creation PASSED [ 43%]
tests/brown/domain/test_reviews.py::TestSelectedTextReviews::test_selected_text_reviews_to_context PASSED [ 44%]
tests/brown/evals/metrics/follows_gt/test_follows_gt_metric.py::test_article_metric_perfect_score PASSED [ 44%]
tests/brown/evals/metrics/follows_gt/test_follows_gt_metric.py::test_article_metric_mixed_scores PASSED [ 45%]
tests/brown/evals/metrics/follows_gt/test_follows_gt_metric.py::test_article_metric_empty_sections PASSED [ 45%]
tests/brown/evals/metrics/follows_gt/test_follows_gt_metric.py::test_article_metric_init_requires_mocked_response_for_fake_model PASSED [ 46%]
tests/brown/evals/metrics/follows_gt/test_follows_gt_metric.py::test_article_metric_init_default_model PASSED [ 46%]
tests/brown/evals/metrics/follows_gt/test_follows_gt_metric.py::test_article_metric_init_custom_name PASSED [ 47%]
tests/brown/evals/metrics/user_intent/test_user_intent_metric.py::test_user_intent_metric_perfect_score PASSED [ 47%]
tests/brown/evals/metrics/user_intent/test_user_intent_metric.py::test_user_intent_metric_mixed_scores PASSED [ 48%]
tests/brown/evals/metrics/user_intent/test_user_intent_metric.py::test_user_intent_metric_poor_scores PASSED [ 48%]
tests/brown/evals/metrics/user_intent/test_user_intent_metric.py::test_user_intent_metric_empty_sections PASSED [ 49%]
tests/brown/evals/metrics/user_intent/test_user_intent_metric.py::test_user_intent_metric_missing_research_in_context PASSED [ 49%]
tests/brown/evals/metrics/user_intent/test_user_intent_metric.py::test_user_intent_metric_init_requires_mocked_response_for_fake_model PASSED [ 50%]
tests/brown/evals/metrics/user_intent/test_user_intent_metric.py::test_user_intent_metric_init_default_model PASSED [ 50%]
tests/brown/evals/metrics/user_intent/test_user_intent_metric.py::test_user_intent_metric_init_custom_name PASSED [ 50%]
tests/brown/evals/metrics/user_intent/test_user_intent_metric.py::test_user_intent_metric_init_custom_few_shot_examples PASSED [ 51%]
tests/brown/evals/metrics/user_intent/test_user_intent_metric.py::test_user_intent_metric_score_result_structure PASSED [ 51%]
tests/brown/evals/metrics/user_intent/test_user_intent_metric.py::test_user_intent_metric_async_score PASSED [ 52%]
tests/brown/evals/metrics/user_intent/test_user_intent_metric.py::test_user_intent_scores_to_context PASSED [ 52%]
tests/brown/evals/metrics/user_intent/test_user_intent_metric.py::test_user_intent_article_scores_to_context PASSED [ 53%]
tests/brown/evals/test_dataset.py::test_load_dataset_success PASSED      [ 53%]
tests/brown/evals/test_dataset.py::test_load_dataset_few_shot_example PASSED [ 54%]
tests/brown/evals/test_dataset.py::test_load_dataset_file_not_found PASSED [ 54%]
tests/brown/evals/test_dataset.py::test_load_dataset_metadata_not_found PASSED [ 55%]
tests/brown/evals/test_dataset.py::test_load_dataset_empty_metadata PASSED [ 55%]
tests/brown/evals/test_dataset.py::test_load_dataset_invalid_metadata_structure PASSED [ 56%]
tests/brown/evals/test_tasks.py::TestEvaluationTask::test_evaluation_task_creation PASSED [ 56%]
tests/brown/evals/test_tasks.py::TestEvaluationTask::test_evaluation_task_function_signature PASSED [ 57%]
tests/brown/evals/test_tasks.py::TestEvaluationTask::test_create_evaluation_task_parameters PASSED [ 57%]
tests/brown/evals/test_tasks.py::TestEvaluationTask::test_evaluation_task_async PASSED [ 57%]
tests/brown/nodes/test_article_reviewer.py::TestArticleReviewer::test_article_reviewer_initialization PASSED [ 58%]
tests/brown/nodes/test_article_reviewer.py::TestArticleReviewer::test_article_reviewer_ainvoke_success PASSED [ 58%]
tests/brown/nodes/test_article_reviewer.py::TestArticleReviewer::test_article_reviewer_structured_output PASSED [ 59%]
tests/brown/nodes/test_article_reviewer.py::TestArticleReviewer::test_article_reviewer_empty_article PASSED [ 59%]
tests/brown/nodes/test_article_reviewer.py::TestArticleReviewer::test_article_reviewer_multiple_reviews PASSED [ 60%]
tests/brown/nodes/test_article_reviewer.py::TestArticleReviewer::test_article_reviewer_requires_mocked_response_for_fake_model PASSED [ 60%]
tests/brown/nodes/test_article_reviewer.py::TestArticleReviewer::test_article_reviewer_selected_text_initialization PASSED [ 61%]
tests/brown/nodes/test_article_reviewer.py::TestArticleReviewer::test_article_reviewer_selected_text_ainvoke PASSED [ 61%]
tests/brown/nodes/test_article_reviewer.py::TestArticleReviewer::test_article_reviewer_selected_text_with_human_feedback PASSED [ 62%]
tests/brown/nodes/test_article_reviewer.py::TestArticleReviewer::test_article_reviewer_article_property PASSED [ 62%]
tests/brown/nodes/test_article_writer.py::TestArticleWriter::test_article_writer_initialization PASSED [ 63%]
tests/brown/nodes/test_article_writer.py::TestArticleWriter::test_article_writer_ainvoke_success PASSED [ 63%]
tests/brown/nodes/test_article_writer.py::TestArticleWriter::test_article_writer_with_media_items PASSED [ 64%]
tests/brown/nodes/test_article_writer.py::TestArticleWriter::test_article_writer_with_reviews PASSED [ 64%]
tests/brown/nodes/test_article_writer.py::TestArticleWriter::test_article_writer_empty_input PASSED [ 64%]
tests/brown/nodes/test_article_writer.py::TestArticleWriter::test_article_writer_requires_mocked_response_for_fake_model PASSED [ 65%]
tests/brown/nodes/test_article_writer.py::TestArticleWriter::test_article_writer_with_selected_text_reviews PASSED [ 65%]
tests/brown/nodes/test_article_writer.py::TestArticleWriter::test_article_writer_selected_text_preserves_line_numbers PASSED [ 66%]
tests/brown/nodes/test_article_writer.py::TestArticleWriter::test_article_writer_selected_text_vs_article_output PASSED [ 66%]
tests/brown/nodes/test_article_writer.py::TestArticleWriter::test_article_writer_selected_text_content PASSED [ 67%]
tests/brown/nodes/test_base.py::TestNode::test_node_initialization PASSED [ 67%]
tests/brown/nodes/test_base.py::TestNode::test_node_build_toolkit PASSED [ 68%]
tests/brown/nodes/test_base.py::TestNode::test_node_build_model_client PASSED [ 68%]
tests/brown/nodes/test_base.py::TestNode::test_node_build_model_client_fake PASSED [ 69%]
tests/brown/nodes/test_base.py::TestNode::test_node_build_user_input_content PASSED [ 69%]
tests/brown/nodes/test_base.py::TestNode::test_node_as_tool PASSED       [ 70%]
tests/brown/nodes/test_base.py::TestNode::test_node_with_fake_model_requires_mocked_response PASSED [ 70%]
tests/brown/nodes/test_base.py::TestNode::test_node_set_mocked_responses PASSED [ 71%]
tests/brown/nodes/test_base.py::TestToolkit::test_toolkit_initialization PASSED [ 71%]
tests/brown/nodes/test_base.py::TestToolkit::test_toolkit_abstract_methods PASSED [ 71%]
tests/brown/nodes/test_media_generator.py::TestMermaidDiagramGenerator::test_mermaid_diagram_generator_initialization PASSED [ 72%]
tests/brown/nodes/test_media_generator.py::TestMermaidDiagramGenerator::test_mermaid_diagram_generator_ainvoke PASSED [ 72%]
tests/brown/nodes/test_media_generator.py::TestMermaidDiagramGenerator::test_mermaid_diagram_generator_error_handling PASSED [ 73%]
tests/brown/nodes/test_media_generator.py::TestMermaidDiagramGenerator::test_mermaid_diagram_generator_requires_mocked_response_for_fake_model PASSED [ 73%]
tests/brown/nodes/test_media_generator.py::TestMediaGeneratorOrchestrator::test_media_generator_orchestrator_initialization PASSED [ 74%]
tests/brown/nodes/test_media_generator.py::TestMediaGeneratorOrchestrator::test_media_generator_orchestrator_ainvoke PASSED [ 74%]
tests/brown/nodes/test_media_generator.py::TestMediaGeneratorOrchestrator::test_media_generator_orchestrator_requires_mocked_response_for_fake_model PASSED [ 75%]
tests/brown/utils/test_a.py::TestAsSync::test_as_sync_decorator PASSED   [ 75%]
tests/brown/utils/test_a.py::TestAsSync::test_as_sync_with_exception PASSED [ 76%]
tests/brown/utils/test_a.py::TestAsSync::test_as_sync_invalid_function PASSED [ 76%]
tests/brown/utils/test_a.py::TestAsyncioRun::test_asyncio_run_new_loop PASSED [ 77%]
tests/brown/utils/test_a.py::TestAsyncioRun::test_asyncio_run_with_exception PASSED [ 77%]
tests/brown/utils/test_a.py::TestAsyncioRun::test_asyncio_run_existing_loop PASSED [ 78%]
tests/brown/utils/test_a.py::TestRunAsyncTasks::test_run_async_tasks PASSED [ 78%]
tests/brown/utils/test_a.py::TestRunAsyncTasks::test_run_async_tasks_empty PASSED [ 78%]
tests/brown/utils/test_a.py::TestRunAsyncTasks::test_run_async_tasks_with_progress PASSED [ 79%]
tests/brown/utils/test_a.py::TestBatchGather::test_batch_gather PASSED   [ 79%]
tests/brown/utils/test_a.py::TestBatchGather::test_batch_gather_single_batch PASSED [ 80%]
tests/brown/utils/test_a.py::TestBatchGather::test_batch_gather_with_verbose PASSED [ 80%]
tests/brown/utils/test_a.py::TestRunJobs::test_run_jobs PASSED           [ 81%]
tests/brown/utils/test_a.py::TestRunJobs::test_run_jobs_single_worker PASSED [ 81%]
tests/brown/utils/test_a.py::TestRunJobs::test_run_jobs_with_progress PASSED [ 82%]
tests/brown/utils/test_a.py::TestRunJobs::test_run_jobs_empty PASSED     [ 82%]
tests/brown/utils/test_a.py::TestRunJobs::test_run_jobs_with_exception PASSED [ 83%]
tests/brown/utils/test_network.py::TestIsImageDomainAccepted::test_valid_domains PASSED [ 83%]
tests/brown/utils/test_network.py::TestIsImageDomainAccepted::test_invalid_domains PASSED [ 84%]
tests/brown/utils/test_network.py::TestIsImageDomainAccepted::test_edge_cases PASSED [ 84%]
tests/brown/utils/test_network.py::TestPing::test_ping_success PASSED    [ 85%]
tests/brown/utils/test_network.py::TestPing::test_ping_head_fallback_to_get PASSED [ 85%]
tests/brown/utils/test_network.py::TestPing::test_ping_invalid_content_type PASSED [ 85%]
tests/brown/utils/test_network.py::TestPing::test_ping_non_200_status PASSED [ 86%]
tests/brown/utils/test_network.py::TestPing::test_ping_request_error PASSED [ 86%]
tests/brown/utils/test_network.py::TestPing::test_ping_timeout PASSED    [ 87%]
tests/brown/utils/test_network.py::TestPing::test_ping_invalid_url PASSED [ 87%]
tests/brown/utils/test_network.py::TestIsImageUrlValid::test_valid_image_url PASSED [ 88%]
tests/brown/utils/test_network.py::TestIsImageUrlValid::test_invalid_domain PASSED [ 88%]
tests/brown/utils/test_network.py::TestIsImageUrlValid::test_valid_domain_but_unreachable PASSED [ 89%]
tests/brown/utils/test_network.py::TestIsImageUrlValid::test_custom_timeout PASSED [ 89%]
tests/brown/utils/test_network.py::TestIsImageUrlValid::test_empty_url PASSED [ 90%]
tests/brown/utils/test_network.py::TestIsImageUrlValid::test_malformed_url PASSED [ 90%]
tests/brown/utils/test_s.py::TestCamelToSnake::test_camel_to_snake_simple PASSED [ 91%]
tests/brown/utils/test_s.py::TestCamelToSnake::test_camel_to_snake_with_numbers PASSED [ 91%]
tests/brown/utils/test_s.py::TestCamelToSnake::test_camel_to_snake_single_word PASSED [ 92%]
tests/brown/utils/test_s.py::TestCamelToSnake::test_camel_to_snake_empty PASSED [ 92%]
tests/brown/utils/test_s.py::TestCamelToSnake::test_camel_to_snake_already_snake PASSED [ 92%]
tests/brown/utils/test_s.py::TestNormalizeAnyToStr::test_normalize_any_to_str_with_string PASSED [ 93%]
tests/brown/utils/test_s.py::TestNormalizeAnyToStr::test_normalize_any_to_str_with_list PASSED [ 93%]
tests/brown/utils/test_s.py::TestNormalizeAnyToStr::test_normalize_any_to_str_with_dict PASSED [ 94%]
tests/brown/utils/test_s.py::TestNormalizeAnyToStr::test_normalize_any_to_str_invalid_list PASSED [ 94%]
tests/brown/utils/test_s.py::TestNormalizeAnyToStr::test_normalize_any_to_str_invalid_dict PASSED [ 95%]
tests/brown/utils/test_s.py::TestNormalizeAnyToStr::test_normalize_any_to_str_invalid_type PASSED [ 95%]
tests/brown/utils/test_s.py::TestCleanMarkdownLinks::test_clean_markdown_links_simple PASSED [ 96%]
tests/brown/utils/test_s.py::TestCleanMarkdownLinks::test_clean_markdown_links_multiple PASSED [ 96%]
tests/brown/utils/test_s.py::TestCleanMarkdownLinks::test_clean_markdown_links_with_images PASSED [ 97%]
tests/brown/utils/test_s.py::TestCleanMarkdownLinks::test_clean_markdown_links_malformed PASSED [ 97%]
tests/brown/utils/test_s.py::TestCleanMarkdownLinks::test_clean_markdown_links_no_links PASSED [ 98%]
tests/brown/utils/test_s.py::TestCleanMarkdownLinks::test_clean_markdown_links_empty PASSED [ 98%]
tests/brown/utils/test_s.py::TestCleanMarkdownLinks::test_clean_markdown_links_complex PASSED [ 99%]
tests/brown/utils/test_s.py::TestCleanMarkdownLinks::test_clean_markdown_links_with_text PASSED [ 99%]
tests/brown/utils/test_s.py::TestCleanMarkdownLinks::test_clean_markdown_links_nested_brackets PASSED [100%]

=============================== warnings summary ===============================
tests/brown/domain/test_research.py::TestResearch::test_research_str_representation
  /Users/fabio/Desktop/course-ai-agents/lessons/writing_workflow/src/brown/utils/a.py:90: DeprecationWarning: There is no current event loop
    loop = asyncio.get_event_loop()

tests/brown/utils/test_network.py::TestPing::test_ping_success
  /Users/fabio/.local/share/uv/python/cpython-3.12.11-macos-aarch64-none/lib/python3.12/unittest/mock.py:2217: RuntimeWarning: coroutine 'run_jobs.<locals>.worker' was never awaited
    def __init__(self, name, parent):
  Enable tracemalloc to get traceback where the object was allocated.
  See https://docs.pytest.org/en/stable/how-to/capture-warnings.html#resource-warnings for more info.

tests/brown/utils/test_network.py::TestPing::test_ping_non_200_status
  /Users/fabio/Desktop/course-ai-agents/lessons/writing_workflow/src/brown/utils/network.py:39: RuntimeWarning: coroutine 'AsyncMockMixin._execute_mock_call' was never awaited
    if response.status_code == 405 or not response.headers.get("Content-Type"):
  Enable tracemalloc to get traceback where the object was allocated.
  See https://docs.pytest.org/en/stable/how-to/capture-warnings.html#resource-warnings for more info.

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
======================= 214 passed, 3 warnings in 0.91s ========================
```

The `-v` flag provides verbose output, showing each test as it runs. The `CONFIG_FILE=configs/debug.yaml` ensures all tests use fake models instead of real LLMs.

### 6.1 Running Specific Test Files

You can run tests for specific components:

!CONFIG_FILE=configs/debug.yaml uv run pytest tests/brown/domain/ -v

```
warning: `VIRTUAL_ENV=/Users/fabio/Desktop/course-ai-agents/.venv` does not match the project environment path `.venv` and will be ignored; use `--active` to target the active environment instead
============================= test session starts ==============================
platform darwin -- Python 3.12.11, pytest-8.4.2, pluggy-1.6.0 -- /Users/fabio/Desktop/course-ai-agents/lessons/writing_workflow/.venv/bin/python
cachedir: .pytest_cache
rootdir: /Users/fabio/Desktop/course-ai-agents/lessons/writing_workflow
configfile: pyproject.toml
plugins: asyncio-1.2.0, anyio-4.11.0, langsmith-0.4.38, opik-1.8.96
asyncio: mode=Mode.STRICT, debug=False, asyncio_default_fixture_loop_scope=None, asyncio_default_test_loop_scope=function
collected 74 items

tests/brown/domain/test_articles.py::TestArticle::test_article_creation PASSED [  1%]
tests/brown/domain/test_articles.py::TestArticle::test_article_to_context PASSED [  2%]
tests/brown/domain/test_articles.py::TestArticle::test_article_to_markdown PASSED [  4%]
tests/brown/domain/test_articles.py::TestArticle::test_article_str_representation PASSED [  5%]
tests/brown/domain/test_articles.py::TestArticle::test_article_empty_content PASSED [  6%]
tests/brown/domain/test_articles.py::TestSelectedText::test_selected_text_creation PASSED [  8%]
tests/brown/domain/test_articles.py::TestSelectedText::test_selected_text_to_context PASSED [  9%]
tests/brown/domain/test_articles.py::TestSelectedText::test_selected_text_single_line PASSED [ 10%]
tests/brown/domain/test_articles.py::TestArticleExample::test_article_example_creation PASSED [ 12%]
tests/brown/domain/test_articles.py::TestArticleExample::test_article_example_to_context PASSED [ 13%]
tests/brown/domain/test_articles.py::TestArticleExample::test_article_example_str_representation PASSED [ 14%]
tests/brown/domain/test_articles.py::TestArticleExamples::test_article_examples_creation PASSED [ 16%]
tests/brown/domain/test_articles.py::TestArticleExamples::test_article_examples_to_context PASSED [ 17%]
tests/brown/domain/test_articles.py::TestArticleExamples::test_article_examples_empty PASSED [ 18%]
tests/brown/domain/test_articles.py::TestArticleExamples::test_article_examples_single PASSED [ 20%]
tests/brown/domain/test_guidelines.py::TestArticleGuideline::test_article_guideline_creation PASSED [ 21%]
tests/brown/domain/test_guidelines.py::TestArticleGuideline::test_article_guideline_to_context PASSED [ 22%]
tests/brown/domain/test_guidelines.py::TestArticleGuideline::test_article_guideline_empty_content PASSED [ 24%]
tests/brown/domain/test_guidelines.py::TestArticleGuideline::test_article_guideline_complex_content PASSED [ 25%]
tests/brown/domain/test_media_items.py::TestMediaItem::test_media_item_creation PASSED [ 27%]
tests/brown/domain/test_media_items.py::TestMediaItem::test_media_item_to_context PASSED [ 28%]
tests/brown/domain/test_media_items.py::TestMediaItem::test_media_item_different_types PASSED [ 29%]
tests/brown/domain/test_media_items.py::TestMediaItem::test_media_item_str_representation PASSED [ 31%]
tests/brown/domain/test_media_items.py::TestMediaItems::test_media_items_creation PASSED [ 32%]
tests/brown/domain/test_media_items.py::TestMediaItems::test_media_items_to_context PASSED [ 33%]
tests/brown/domain/test_media_items.py::TestMediaItems::test_media_items_empty PASSED [ 35%]
tests/brown/domain/test_media_items.py::TestMediaItems::test_media_items_single PASSED [ 36%]
tests/brown/domain/test_media_items.py::TestMediaItems::test_media_items_str_representation PASSED [ 37%]
tests/brown/domain/test_media_items.py::TestMediaItems::test_media_items_build_classmethod PASSED [ 39%]
tests/brown/domain/test_media_items.py::TestMediaItems::test_are_available_only_in_source_property PASSED [ 40%]
tests/brown/domain/test_media_items.py::TestMermaidDiagram::test_mermaid_diagram_creation PASSED [ 41%]
tests/brown/domain/test_mixins.py::TestContextMixin::test_context_mixin_xml_tag PASSED [ 43%]
tests/brown/domain/test_mixins.py::TestContextMixin::test_context_mixin_xml_tag_with_profile PASSED [ 44%]
tests/brown/domain/test_mixins.py::TestContextMixin::test_context_mixin_xml_tag_with_suffix PASSED [ 45%]
tests/brown/domain/test_mixins.py::TestMarkdownMixin::test_markdown_mixin_abstract PASSED [ 47%]
tests/brown/domain/test_mixins.py::TestMarkdownMixin::test_markdown_mixin_implementation PASSED [ 48%]
tests/brown/domain/test_mixins.py::TestMarkdownMixin::test_markdown_mixin_missing_implementation PASSED [ 50%]
tests/brown/domain/test_profiles.py::TestProfile::test_profile_creation PASSED [ 51%]
tests/brown/domain/test_profiles.py::TestProfile::test_profile_xml_tag PASSED [ 52%]
tests/brown/domain/test_profiles.py::TestProfile::test_profile_to_context PASSED [ 54%]
tests/brown/domain/test_profiles.py::TestCharacterProfile::test_character_profile_creation PASSED [ 55%]
tests/brown/domain/test_profiles.py::TestCharacterProfile::test_character_profile_to_context PASSED [ 56%]
tests/brown/domain/test_profiles.py::TestArticleProfile::test_article_profile_creation PASSED [ 58%]
tests/brown/domain/test_profiles.py::TestArticleProfile::test_article_profile_to_context PASSED [ 59%]
tests/brown/domain/test_profiles.py::TestStructureProfile::test_structure_profile_creation PASSED [ 60%]
tests/brown/domain/test_profiles.py::TestStructureProfile::test_structure_profile_to_context PASSED [ 62%]
tests/brown/domain/test_profiles.py::TestMechanicsProfile::test_mechanics_profile_creation PASSED [ 63%]
tests/brown/domain/test_profiles.py::TestMechanicsProfile::test_mechanics_profile_to_context PASSED [ 64%]
tests/brown/domain/test_profiles.py::TestTerminologyProfile::test_terminology_profile_creation PASSED [ 66%]
tests/brown/domain/test_profiles.py::TestTerminologyProfile::test_terminology_profile_to_context PASSED [ 67%]
tests/brown/domain/test_profiles.py::TestTonalityProfile::test_tonality_profile_creation PASSED [ 68%]
tests/brown/domain/test_profiles.py::TestTonalityProfile::test_tonality_profile_to_context PASSED [ 70%]
tests/brown/domain/test_profiles.py::TestArticleProfiles::test_article_profiles_creation PASSED [ 71%]
tests/brown/domain/test_profiles.py::TestArticleProfiles::test_article_profiles_to_context PASSED [ 72%]
tests/brown/domain/test_research.py::TestResearch::test_research_creation PASSED [ 74%]
tests/brown/domain/test_research.py::TestResearch::test_research_to_context PASSED [ 75%]
tests/brown/domain/test_research.py::TestResearch::test_research_empty_content PASSED [ 77%]
tests/brown/domain/test_research.py::TestResearch::test_research_complex_content PASSED [ 78%]
tests/brown/domain/test_research.py::TestResearch::test_research_str_representation PASSED [ 79%]
tests/brown/domain/test_reviews.py::TestReview::test_review_creation PASSED [ 81%]
tests/brown/domain/test_reviews.py::TestReview::test_review_to_context PASSED [ 82%]
tests/brown/domain/test_reviews.py::TestReview::test_review_score_validation PASSED [ 83%]
tests/brown/domain/test_reviews.py::TestReview::test_review_str_representation PASSED [ 85%]
tests/brown/domain/test_reviews.py::TestArticleReviews::test_article_reviews_creation PASSED [ 86%]
tests/brown/domain/test_reviews.py::TestArticleReviews::test_article_reviews_to_context PASSED [ 87%]
tests/brown/domain/test_reviews.py::TestArticleReviews::test_article_reviews_with_article PASSED [ 89%]
tests/brown/domain/test_reviews.py::TestArticleReviews::test_article_reviews_without_article PASSED [ 90%]
tests/brown/domain/test_reviews.py::TestArticleReviews::test_article_reviews_empty PASSED [ 91%]
tests/brown/domain/test_reviews.py::TestArticleReviews::test_article_reviews_single PASSED [ 93%]
tests/brown/domain/test_reviews.py::TestArticleReviews::test_article_reviews_str_representation PASSED [ 94%]
tests/brown/domain/test_reviews.py::TestHumanFeedback::test_human_feedback_creation PASSED [ 95%]
tests/brown/domain/test_reviews.py::TestHumanFeedback::test_human_feedback_to_context PASSED [ 97%]
tests/brown/domain/test_reviews.py::TestSelectedTextReviews::test_selected_text_reviews_creation PASSED [ 98%]
tests/brown/domain/test_reviews.py::TestSelectedTextReviews::test_selected_text_reviews_to_context PASSED [100%]

=============================== warnings summary ===============================
tests/brown/domain/test_research.py::TestResearch::test_research_str_representation
  /Users/fabio/Desktop/course-ai-agents/lessons/writing_workflow/src/brown/utils/a.py:90: DeprecationWarning: There is no current event loop
    loop = asyncio.get_event_loop()

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
======================== 74 passed, 1 warning in 0.07s =========================
```

!CONFIG_FILE=configs/debug.yaml uv run pytest tests/brown/nodes/ -v

```
warning: `VIRTUAL_ENV=/Users/fabio/Desktop/course-ai-agents/.venv` does not match the project environment path `.venv` and will be ignored; use `--active` to target the active environment instead
============================= test session starts ==============================
platform darwin -- Python 3.12.11, pytest-8.4.2, pluggy-1.6.0 -- /Users/fabio/Desktop/course-ai-agents/lessons/writing_workflow/.venv/bin/python
cachedir: .pytest_cache
rootdir: /Users/fabio/Desktop/course-ai-agents/lessons/writing_workflow
configfile: pyproject.toml
plugins: asyncio-1.2.0, anyio-4.11.0, langsmith-0.4.38, opik-1.8.96
asyncio: mode=Mode.STRICT, debug=False, asyncio_default_fixture_loop_scope=None, asyncio_default_test_loop_scope=function
collected 37 items

tests/brown/nodes/test_article_reviewer.py::TestArticleReviewer::test_article_reviewer_initialization PASSED [  2%]
tests/brown/nodes/test_article_reviewer.py::TestArticleReviewer::test_article_reviewer_ainvoke_success PASSED [  5%]
tests/brown/nodes/test_article_reviewer.py::TestArticleReviewer::test_article_reviewer_structured_output PASSED [  8%]
tests/brown/nodes/test_article_reviewer.py::TestArticleReviewer::test_article_reviewer_empty_article PASSED [ 10%]
tests/brown/nodes/test_article_reviewer.py::TestArticleReviewer::test_article_reviewer_multiple_reviews PASSED [ 13%]
tests/brown/nodes/test_article_reviewer.py::TestArticleReviewer::test_article_reviewer_requires_mocked_response_for_fake_model PASSED [ 16%]
tests/brown/nodes/test_article_reviewer.py::TestArticleReviewer::test_article_reviewer_selected_text_initialization PASSED [ 18%]
tests/brown/nodes/test_article_reviewer.py::TestArticleReviewer::test_article_reviewer_selected_text_ainvoke PASSED [ 21%]
tests/brown/nodes/test_article_reviewer.py::TestArticleReviewer::test_article_reviewer_selected_text_with_human_feedback PASSED [ 24%]
tests/brown/nodes/test_article_reviewer.py::TestArticleReviewer::test_article_reviewer_article_property PASSED [ 27%]
tests/brown/nodes/test_article_writer.py::TestArticleWriter::test_article_writer_initialization PASSED [ 29%]
tests/brown/nodes/test_article_writer.py::TestArticleWriter::test_article_writer_ainvoke_success PASSED [ 32%]
tests/brown/nodes/test_article_writer.py::TestArticleWriter::test_article_writer_with_media_items PASSED [ 35%]
tests/brown/nodes/test_article_writer.py::TestArticleWriter::test_article_writer_with_reviews PASSED [ 37%]
tests/brown/nodes/test_article_writer.py::TestArticleWriter::test_article_writer_empty_input PASSED [ 40%]
tests/brown/nodes/test_article_writer.py::TestArticleWriter::test_article_writer_requires_mocked_response_for_fake_model PASSED [ 43%]
tests/brown/nodes/test_article_writer.py::TestArticleWriter::test_article_writer_with_selected_text_reviews PASSED [ 45%]
tests/brown/nodes/test_article_writer.py::TestArticleWriter::test_article_writer_selected_text_preserves_line_numbers PASSED [ 48%]
tests/brown/nodes/test_article_writer.py::TestArticleWriter::test_article_writer_selected_text_vs_article_output PASSED [ 51%]
tests/brown/nodes/test_article_writer.py::TestArticleWriter::test_article_writer_selected_text_content PASSED [ 54%]
tests/brown/nodes/test_base.py::TestNode::test_node_initialization PASSED [ 56%]
tests/brown/nodes/test_base.py::TestNode::test_node_build_toolkit PASSED [ 59%]
tests/brown/nodes/test_base.py::TestNode::test_node_build_model_client PASSED [ 62%]
tests/brown/nodes/test_base.py::TestNode::test_node_build_model_client_fake PASSED [ 64%]
tests/brown/nodes/test_base.py::TestNode::test_node_build_user_input_content PASSED [ 67%]
tests/brown/nodes/test_base.py::TestNode::test_node_as_tool PASSED       [ 70%]
tests/brown/nodes/test_base.py::TestNode::test_node_with_fake_model_requires_mocked_response PASSED [ 72%]
tests/brown/nodes/test_base.py::TestNode::test_node_set_mocked_responses PASSED [ 75%]
tests/brown/nodes/test_base.py::TestToolkit::test_toolkit_initialization PASSED [ 78%]
tests/brown/nodes/test_base.py::TestToolkit::test_toolkit_abstract_methods PASSED [ 81%]
tests/brown/nodes/test_media_generator.py::TestMermaidDiagramGenerator::test_mermaid_diagram_generator_initialization PASSED [ 83%]
tests/brown/nodes/test_media_generator.py::TestMermaidDiagramGenerator::test_mermaid_diagram_generator_ainvoke PASSED [ 86%]
tests/brown/nodes/test_media_generator.py::TestMermaidDiagramGenerator::test_mermaid_diagram_generator_error_handling PASSED [ 89%]
tests/brown/nodes/test_media_generator.py::TestMermaidDiagramGenerator::test_mermaid_diagram_generator_requires_mocked_response_for_fake_model PASSED [ 91%]
tests/brown/nodes/test_media_generator.py::TestMediaGeneratorOrchestrator::test_media_generator_orchestrator_initialization PASSED [ 94%]
tests/brown/nodes/test_media_generator.py::TestMediaGeneratorOrchestrator::test_media_generator_orchestrator_ainvoke PASSED [ 97%]
tests/brown/nodes/test_media_generator.py::TestMediaGeneratorOrchestrator::test_media_generator_orchestrator_requires_mocked_response_for_fake_model PASSED [100%]

============================== 37 passed in 0.13s ==============================
```

### 6.3 Understanding What's Being Tested

Brown's test suite includes:

-   **Domain tests** (`tests/brown/domain/`): Testing Pydantic models and data structures without any LLM calls
-   **Node tests** (`tests/brown/nodes/`): Testing agent nodes like ArticleWriter and ArticleReviewer with mocked LLM responses
-   **Utility tests** (`tests/brown/utils/`): Testing helper functions
-   **Evaluation tests** (`tests/brown/evals/`): Testing evaluation metrics and dataset handling

The complete test suite runs in under a minute and requires no API keys. Every test is deterministic.

</details>

<details>
<summary>LLM evaluation for CI/CD pipelines</summary>

# LLM evaluation for CI/CD pipelines

**Source URL:** <https://www.deepchecks.com/llm-evaluation/ci-cd-pipelines/>

[https://deepchecks.com/wp-content/uploads/2025/10/cropped-img-yaron-friedman-96x96.jpg Yaron Friedman](https://deepchecks.com/author/yaron-friedman/)

\|
June 12, 2025

## Introduction

Large Language Models (LLMs) are transforming how we communicate with AI, from chatbots and virtual assistants to generating content and beyond. But with power comes responsibility. Getting these models to perform well and stay dependable is a major challenge. Over time, LLMs will produce incorrect, biased, or misleading results as they learn from new data. If no continuous tests are conducted, organizations will be at risk of deploying AI models with biased and inaccurate answers.

To keep [LLM](https://deepchecks.com/glossary/llm-parameters/) applications reliable, we require a mechanism that automatically monitors and enhances them. This is why integrating LLM evaluations in [Continuous Integration/Continuous Deployment (CI/CD)](https://deepchecks.com/glossary/ci-cd-for-machine-learning/) becomes necessary. CI/CD pipelines are the most significant part of software development. They make sure the code gets tested, integrated, and deployed without a glitch. Adding LLM tests to such pipelines enables us to identify issues early, maintain the quality of the model, and help our AI-based applications be trusted and ethical.

## Why do LLM Evaluations Matter in CI/CD Pipelines?

Integrating LLM evaluations into CI/CD pipelines is more than simply enhancing LLM model accuracy and performance. The main purpose is to ensure the quality, fairness, and robustness of AI solutions.

https://deepchecks.com/wp-content/uploads/2025/05/img-llm-evaluation-ci-cd-pipeliens.jpg

Figure: LLM Evaluation in CI/CD Pipeliens

[Source](https://www.willowtreeapps.com/craft/continuous-evaluation-of-generative-ai-using-ci-cd-pipelines)

There are several good reasons why incorporating LLM evaluations with CI/CD pipelines is essential:

### Ensuring Model Accuracy and Performance

LLMs are prone to model drift, where they become less accurate when learning from new data. At times, they begin providing incorrect or outdated responses. If monitored regularly, they enable the identification of such errors early enough so they can be corrected before they impact users.

https://deepchecks.com/wp-content/uploads/2025/05/img-ensuring-model-accuracy-performance.jpg

Figure: Calculating LLM Accuracy and Performance

[Source](https://www.confident-ai.com/blog/llm-evaluation-metrics-everything-you-need-for-llm-evaluation)

For instance, if an e-commerce website’s customer service chatbot starts providing outdated responses regarding return policies, an automated test can detect and correct the issue before it causes problems for the user.

### Automating Quality Control

Traditionally, every update is checked manually, which is time-consuming and inefficient. Automated evaluations can streamline this process, allowing us to quickly test models against a set of predefined benchmarks after every update. This saves effort and ensures the AI works well before it is deployed.

### Regulatory and Compliance Needs

Since AI is increasingly becoming part of our daily lives, most industries and governments have strict regulations. Regular assessments can ensure that organizations adhere to these regulations by continuously monitoring for bias and objectionable content in the responses, making models not just accurate but also fair and unbiased.

https://deepchecks.com/wp-content/uploads/2025/05/img-regulatory-compliance-needs.jpg

Figure: LLM Regulatory and Compliance Needs

[Source](https://big-agile.com/blog/regulatory-compliance-challenges-within-product-delivery)

### Real-world Impact

Poorly tested LLMs may cause severe issues. A medical chatbot delivering the wrong medical guidance or a recruitment AI biased toward some applicants can ruin reputations and give rise to legal problems. By including LLM tests in CI/CD pipelines, companies can manage these risks before they affect the users.

## Key Components of an LLM Pipeline in CI/CD

To successfully integrate LLM evaluations into CI/CD pipelines, a systematic strategy is necessary. An LLM has four components that work together to keep the model accurate, fair, and reliable for the long term.

### 1\. Data Preparation and Versioning

LLMs are limited to the quality of their training data. They need training data that is clean, consistent, high-quality, and well-organized. Tracking every version of a dataset across multiple iterations helps maintain data consistency while also providing a mechanism for your team to roll back changes if something was done incorrectly. This is a sign of a good data pipeline designed to scale to utilize large datasets and ensure that training and evaluation datasets stay current.

https://deepchecks.com/wp-content/uploads/2025/05/img-data-preparation-versioning.jpg

Figure: LLM Data Preparation and Versioning

[Source](https://tulsipatro29.medium.com/llmops-part-1-the-introduction-81fa77999f44)

### 2\. Model Training and Fine-Tuning

In order to keep LLMs current, you must either retrain them using new data or [fine-tune](https://deepchecks.com/glossary/llm-fine-tuning/) them so that the model generalizes well for the specific task. Moreover, by automating this testing within the CI/CD pipeline, you can ensure that the model continues to improve and produce outputs that are relevant and relatable to the outside world.

https://deepchecks.com/wp-content/uploads/2025/05/img-model-training-fine-tuning.jpg

Figure: LLM training and Fine Tuning

[Source](https://medium.com/mantisnlp/supervised-fine-tuning-customizing-llms-a2c1edbf22c3)

### 3\. Automated LLM Evaluations

[Automated assessments](https://deepchecks.com/llm-evaluation/) are the key part of this integration. These assessments should be ongoing, with every new model update subjected to testing for accuracy, bias, and robustness. Automated assessments identify possible issues in the earlier stages of model development, helping ensure the model remains safe and reliable.

https://deepchecks.com/wp-content/uploads/2025/05/img-automated-llm-evaluations.jpg

Figure: Automated LLM Evaluations

[Source](https://deepchecks.com/llm-evaluation/)

### 4\. Deployment and Monitoring

When the model has passed all its tests, it can be deployed with confidence. This is not, however, the end of the process. [Continuous monitoring](https://deepchecks.com/llm-monitoring-evaluation-for-production-applications/) is needed to spot any issues that emerge in production. You may even want to distinguish feedback loops in which user feedback is taken into account in further development of the model.

https://deepchecks.com/wp-content/uploads/2025/05/img-deployment-monitoring.jpg

Figure: LLM Deployment and Monitoring

[Source](https://www.fiddler.ai/blog/llm-monitoring-the-key-to-successful-llm-deployments)

## Integrating LLM Evaluations into CI/CD Pipelines

Now that we know about the most important components of an LLM pipeline, the next step is to integrate evaluations into CI/CD processes. This keeps models under testing, verification, and continuous development before they are made live.

### 1\. Define Evaluation Metrics

Before testing, you must determine what parts of the model need to be assessed. These metrics will guide the evaluation process so that you’re measuring the right things.

https://deepchecks.com/wp-content/uploads/2025/05/img-define-evaluation-metrics.jpg

Figure: LLM Evaluation Metrics

[Source](https://www.confident-ai.com/blog/llm-evaluation-metrics-everything-you-need-for-llm-evaluation)

The evaluation process must focus on several factors:

- **Performance Metrics:** Metrics such as [perplexity, BLEU, and ROUGE](https://deepchecks.com/question/what-metrics-are-commonly-used-in-llm-benchmarks/) assist in determining whether the model is producing quality responses.
- **Fairness & Bias Checks:** AI models should be unbiased and fair. Tests should identify and rectify biased or skewed answers.
- **Robustness & Safety:** The model should be tested against adversarial inputs to make sure it behaves correctly to unexpected or malicious queries.

### 2\. Automate Testing in CI/CD

Manually testing each update is not efficient. Instead, you can configure automated tests to run at various stages of the [pipeline](https://deepchecks.com/glossary/machine-learning-pipeline/) such that the model is tested thoroughly at each stage:

- **Unit Tests:** These tests verify small-scale outputs to identify early response generation errors.
- **Functional Tests:** They test how the model behaves under various scenarios to ensure its responses are as expected.
- **Load Testing:** This ensures the model stays stable and responsive even with a large number of queries.

https://deepchecks.com/wp-content/uploads/2025/05/img-automate-testing-ci-cd.jpg

Figure: Automate LLM Testing

[Source](https://www.lambdatest.com/blog/automation-testing-in-ci-cd-pipeline/)

For instance, an AI-based email generator can be tested by giving it various prompts and evaluating response accuracy before deployment. There are multiple tools available for creating CI/CD pipelines, including [Jenkins](https://www.jenkins.io/), [GitHub Actions](https://github.com/features/actions), [CircleCI](https://circleci.com/), etc., and you can choose any of these tools based on your preference and the organization’s needs. For example, a basic LLM evaluation pipeline in GitHub Actions might look something like this:

Plain text

Copy to clipboard

Open code in new window

EnlighterJS 3 Syntax Highlighter

```
jobs:
llm-evaluation:
runs-on: ubuntu-latest
steps:
- name: Checkout code
uses: actions/checkout@v3
- name: Install dependencies
run: pip install -r requirements.txt
- name: Run LLM evaluations
run: pytest tests/evaluation_tests.py
```

The above code starts with selecting a [runner](https://docs.github.com/en/actions/using-github-hosted-runners/using-github-hosted-runners/about-github-hosted-runners) for executing the jobs; in this case, it is _ubuntu-latest_. Then, the steps section defines all the steps that you will carry out for evaluating the LLMs. For example, the pipeline above first checks out the latest code from your GitHub repo, then installs all the necessary libraries, and finally uses pytest to run the unit tests.

### 3\. Integrate Evaluation Tools and Frameworks

To make testing and monitoring easier, you can utilize specialized tools.

- **Evaluation Platforms:** [Deepcheks](https://deepchecks.com/llm-evaluation/), [Arize AI](https://arize.com/), [OpenAI Evals](https://github.com/openai/evals), and [Hugging Face Evaluate](https://huggingface.co/docs/evaluate/en/index) are some of the tools that measure performance and identify inconsistencies. These platforms offer pre-configured evaluation metrics and can be directly incorporated into CI/CD pipelines.
- **Monitoring Tools:** [Grafana](https://grafana.com/) and [Prometheus](https://prometheus.io/) can be utilized to monitor model performance in real time and catch problems early.

https://deepchecks.com/wp-content/uploads/2025/05/img-integrate-evaluation-tools-frameworks.jpg

Figure: Integrate Automated Evaluation Tools

[Source](https://bestofai.com/tool/deepchecks-llm-evaluation)

### 4\. Deploy With Confidence

Making sure that all tests pass before automatically deploying the model is important. Some ways to improve deployment confidence include:

- **Utilize Feature Flags:** Deploying updates gradually rather than deploying them to everyone at once lowers the chances of surprise failures.
- **Have Rollback Mechanisms:** In case something goes wrong after deployment, teams must be able to roll back to a previously stable version immediately.

## Best Practices for Continuous LLM Evaluations

To maintain a high standard of evaluation, organizations can implement a variety of best practices:

### Use Real-World Feedback Loops

The AI models should be evaluated in real-world settings rather than in a lab-based test situation. Two useful strategies for collecting real-world feedback include:

- **A/B Testing:** Deploy multiple versions of the model and evaluate the model version that performs best during real interactions. For example, an e-commerce chatbot may deploy two versions of the model: one version that responds quickly and one version that provides more detailed responses. Depending on customer engagement and interaction, the better version can be used.
- **User Inputs & Feedback:** Provide users the ability to give feedback on the AI responses in real-time. If, for example, a virtual assistant continues to respond to questions regarding company policy with the wrong information, real-time user feedback could be applied to revise the virtual assistant’s responses.

https://deepchecks.com/wp-content/uploads/2025/05/img-use-real-world-feedback-loops.jpg

Figure: Real-World Feedback Loop

[Source](https://langwatch.ai/blog/the-ai-team-integrating-user-and-domain-expert-feedback-to-enhance-llm-powered-applications)

### Regularly Retrain and Update Models

Language models are dynamic, and they must be continuously updated for time-effectiveness. This can be automated within the CI/CD pipeline to retrain a model when:

- New information is made available, keeping the model current.
- User feedback shows areas of improvement.
- Performance statistics show a drop in accuracy or quality.

https://deepchecks.com/wp-content/uploads/2025/05/img-regularly-retrain-update-models.jpg

Figure: LLM Retraining

[Source](https://magazine.sebastianraschka.com/p/tips-for-llm-pretraining-and-evaluating-rms)

For example, if an AI finance tool is trained on historical stock market data, retraining the tool using current stock market data will keep its predictions current.

### Monitor Logs and Anomalies in Production

Even after deployment, issues can arise unexpectedly. Continuous monitoring helps detect problems such as:

- **Model drift:** When the model begins to generate incorrect or inconsistent results over time.
- **Anomalous Behavior:** If an AI-driven support chatbot begins providing inappropriate responses, automated logs may identify the problem before it affects users.

https://deepchecks.com/wp-content/uploads/2025/05/img-monitor-logs-anomalies-production.jpg

Figure: Types of LLM Anomalies

[Source](https://spotintelligence.com/2024/11/06/anomaly-detection-in-llms/)

Monitoring tools such as Grafana and Prometheus can monitor performance, identify outliers, and alert when there is a problem.

### Enforce Governance and Compliance Checks

AI models must follow ethical guidelines and industry regulations. Automated governance checks ensure that:

- Models do not produce biased or discriminatory output.
- Sensitive information is processed securely.
- The system follows legal frameworks such as [GDPR](https://gdpr-info.eu/) and [AI safety guidelines](https://www.nist.gov/aisi/guidelines).

https://deepchecks.com/wp-content/uploads/2025/05/img-enforce-governance-compliance-checks.jpg

Figure: LLM Governance

[Source](https://datasciencedojo.com/blog/ai-governance/)

For example, a hiring AI cannot discriminate against applicants on the grounds of gender, race, or background. Automated fairness checks can identify and correct such biases.

## Challenges and Ways to Overcome Them

Integrating LLM evaluations into CI/CD pipelines can have several advantages, but operational challenges need to be solved. Below are some operational challenges and suggestions for integrating LLM evaluations into CI/CD pipelines:

### Computational Costs

In many cases, continuous evaluation of large models represents a significant increased resource demand, which can be financially burdensome if you have limited on-premises infrastructure. In many situations, it is not feasible to run evaluations on local infrastructure.

- **Use cloud-based solutions:** Services such as AWS, Google Cloud, and Azure can provide scalable computing clusters that can be expanded and contracted on demand and can be considered more cost-efficient, given you are using just the infrastructure when needed.
- **Optimize model evaluations:** Do not evaluate the entire model each time; consider evaluating relative to the last model unit by target data sample, or previous data sample. This can greatly reduce the computational burden.
- **Utilize lightweight evaluation models:** Leveraging a mini or distill model of an LLM to quickly evaluate performance is a solid option.

https://deepchecks.com/wp-content/uploads/2025/05/img-computational-costs.jpg

Figure: Different Costs of LLMs

[Source](https://www.tensorops.ai/post/understanding-the-cost-of-large-language-models-llms)

### Evaluation Delays

Incorporating many evaluations in the CI/CD pipeline can dramatically lengthen the deployment process, pushing new updates beyond their original go-live date. It can be unreasonable to wait while tests run to completion before deploying.

How to overcome it:

- **Run parallel evaluations:** Instead of running evaluations sequentially, run multiple evaluations in parallel, as you can take advantage of the time saved by conducting multiple evaluations in parallel.
- **Use asynchronous testing:** Allow non-critical evaluations to run in the background while you continue deploying your essential updates.
- **Prioritize essential evaluations:** Start with evaluating the most critical test in order of deployment ease (effectiveness, safety, etc.) before running additional evaluations.

https://deepchecks.com/wp-content/uploads/2025/05/img-evaluation-delays.jpg

Figure: Run Parallel LLM Evaluations

[Source](https://www.confident-ai.com/blog/how-to-build-an-llm-evaluation-framework-from-scratch)

### Data Privacy and Security Risks

LLMs often operate with sensitive user data, creating security concerns if evaluation logs contain sensitive data that is not secured. Organizations are therefore presented with data breach management and possible data resolution issues.

How to overcome it:

- **Encrypt logs and data:** Use encryption standards to offer protection of the evaluation logs that will secure data at rest.
- **Apply differential privacy techniques:** Hide sensitive data that cannot be viewed, but can still provide a relevant evaluation of the methods.
- **Implement strict access controls:** Limit access to evaluation logs and model outputs to authorized individuals only.

https://deepchecks.com/wp-content/uploads/2025/05/img-data-privacy-security-risks.jpg

Figure: Encryption and Decryption of LLM Data

[Source](https://huggingface.co/blog/encrypted-llm)

Once the organization’s data issues are understood and remedied, they can quickly and cost-effectively run secure LLM evaluations as part of their CI/CD workflow methodology.

## Conclusion

Since AI is becoming a part of our everyday life, the need for strong models is also increasing. These AI models need regular maintenance to function properly, and integrating LLM evaluations in CI/CD pipelines can help with this. This process can easily become a part of the development cycle with a few proper strategies in place. This will ensure that the model performs better and is reliable and up-to-date. Teams that follow this method of automated testing will be able to identify and fix issues before they become a major problem. This will improve the performance of the model and help organizations build an AI that their users can actually trust. A loyal user base is what will help organizations stay ahead in this AI-driven future.

</details>

<details>
<summary>pre-commit</summary>

# pre-commit

**Source URL:** <https://pre-commit.com/>

The provided markdown content appears to be the full documentation page for the `pre-commit` tool, not the lesson content described in the `<article_guidelines>`. The guidelines explain *how to write* a lesson about CI for AI agents, which *uses* `pre-commit` as an example. The submitted markdown, however, is a comprehensive guide to `pre-commit` itself, likely scraped from its official documentation.

Following the critical rules:
- "Keep ALL substantive article content" - If this is considered the "article", then all of it is substantive documentation about `pre-commit`.
- "Do NOT filter or remove sections based on topic relevance." - Even if it's not the *exact lesson content*, it is a document about `pre-commit`, which is relevant to the *topic* of the lesson.
- "Do NOT summarize, condense, paraphrase, or rewrite."
- "When in doubt, **keep** the content."
- The `[¶](...)` elements are likely permalinks/anchor links within the documentation page, which serve a navigation purpose *on that page*. They are not part of the core informational text itself and can be considered boilerplate for the webpage's structure/navigation.

Therefore, the only elements to remove are the `[¶](...)` anchor links following each heading, as they are purely navigational boilerplate of the source webpage.

```markdown
# Introduction

Git hook scripts are useful for identifying simple issues before submission to
code review. We run our hooks on every commit to automatically point out
issues in code such as missing semicolons, trailing whitespace, and debug
statements. By pointing these issues out before code review, this allows a
code reviewer to focus on the architecture of a change while not wasting time
with trivial style nitpicks.

As we created more libraries and projects we recognized that sharing our
pre-commit hooks across projects is painful. We copied and pasted unwieldy
bash scripts from project to project and had to manually change the hooks to
work for different project structures.

We believe that you should always use the best industry standard linters.
Some of the best linters are written in languages that you do not use in your
project or have installed on your machine. For example scss-lint is a linter
for SCSS written in Ruby. If you’re writing a project in node you should be
able to use scss-lint as a pre-commit hook without adding a Gemfile to your
project or understanding how to get scss-lint installed.

We built pre-commit to solve our hook issues. It is a multi-language package
manager for pre-commit hooks. You specify a list of hooks you want and
pre-commit manages the installation and execution of any hook written in any
language before every commit. pre-commit is specifically designed to not
require root access. If one of your developers doesn’t have node installed
but modifies a JavaScript file, pre-commit automatically handles downloading
and building node to run eslint without root.

# Installation

Before you can run hooks, you need to have the pre-commit package manager
installed.

Using pip:

```
pip install pre-commit
```

In a python project, add the following to your requirements.txt (or
requirements-dev.txt):

```
pre-commit
```

As a 0-dependency [zipapp](https://docs.python.org/3/library/zipapp.html):

- locate and download the `.pyz` file from the [github releases](https://github.com/pre-commit/pre-commit/releases)
- run `python pre-commit-#.#.#.pyz ...` in place of `pre-commit ...`

## Quick start

### 1\. Install pre-commit

- follow the [install](https://pre-commit.com/#install) instructions above
- `pre-commit --version` should show you what version you're using

```
$ pre-commit --version
pre-commit 4.6.0
```

### 2\. Add a pre-commit configuration

- create a file named `.pre-commit-config.yaml`
- you can generate a very basic configuration using
[`pre-commit sample-config`](https://pre-commit.com/#pre-commit-sample-config)
- the full set of options for the configuration are listed [below](https://pre-commit.com/#plugins)
- this example uses a formatter for python code, however `pre-commit` works for
any programming language
- other [supported hooks](https://pre-commit.com/hooks.html) are available

```
repos:
-   repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v2.3.0
    hooks:
    -   id: check-yaml
    -   id: end-of-file-fixer
    -   id: trailing-whitespace
-   repo: https://github.com/psf/black
    rev: 22.10.0
    hooks:
    -   id: black
```

### 3\. Install the git hook scripts

- run `pre-commit install` to set up the git hook scripts

```
$ pre-commit install
pre-commit installed at .git/hooks/pre-commit
```

- now `pre-commit` will run automatically on `git commit`!

<h3>4\. (optional) Run against all the files</h3>

- it's usually a good idea to run the hooks against all of the files when adding
new hooks (usually `pre-commit` will only run on the changed files during
git hooks)

```
$ pre-commit run --all-files
[INFO] Initializing environment for https://github.com/pre-commit/pre-commit-hooks.
[INFO] Initializing environment for https://github.com/psf/black.
[INFO] Installing environment for https://github.com/pre-commit/pre-commit-hooks.
[INFO] Once installed this environment will be reused.
[INFO] This may take a few minutes...
[INFO] Installing environment for https://github.com/psf/black.
[INFO] Once installed this environment will be reused.
[INFO] This may take a few minutes...
Check Yaml...............................................................Passed
Fix End of Files.........................................................Passed
Trim Trailing Whitespace.................................................Failed
- hook id: trailing-whitespace
- exit code: 1

Files were modified by this hook. Additional output:

Fixing sample.py

black....................................................................Passed
```

- oops! looks like I had some trailing whitespace
- consider running that in [CI](https://pre-commit.com/#usage-in-continuous-integration) too

# Adding pre-commit plugins to your project

Once you have pre-commit installed, adding pre-commit plugins to your project
is done with the `.pre-commit-config.yaml` configuration file.

Add a file called `.pre-commit-config.yaml` to the root of your project. The
pre-commit config file describes what repositories and hooks are installed.

## .pre-commit-config.yaml - top level

|     |     |
| --- | --- |
| [`repos`](https://pre-commit.com/#top_level-repos) | A list of [repository mappings](https://pre-commit.com/#pre-commit-configyaml---repos). |
| [`default_install_hook_types`](https://pre-commit.com/#top_level-default_install_hook_types) | (optional: default `[pre-commit]`) a list of `--hook-type`s which will<br>be used by default when running<br>[`pre-commit install`](https://pre-commit.com/#pre-commit-install). |
| [`default_language_version`](https://pre-commit.com/#top_level-default_language_version) | (optional: default `{}`) a mapping from language to the default<br>[`language_version`](https://pre-commit.com/#config-language_version) that should be used for that language. This will<br>only override individual hooks that do not set [`language_version`](https://pre-commit.com/#config-language_version).<br>For example to use `python3.7` for `language: python` hooks:<br>```<br>default_language_version:<br>    python: python3.7<br>``` |
| [`default_stages`](https://pre-commit.com/#top_level-default_stages) | (optional: default (all stages)) a configuration-wide default for<br>the [`stages`](https://pre-commit.com/#config-stages) property of hooks. This will only override individual<br>hooks that do not set [`stages`](https://pre-commit.com/#config-stages).<br>For example:<br>```<br>default_stages: [pre-commit, pre-push]<br>``` |
| [`files`](https://pre-commit.com/#top_level-files) | (optional: default `''`) global file include pattern. |
| [`exclude`](https://pre-commit.com/#top_level-exclude) | (optional: default `^$`) global file exclude pattern. |
| [`fail_fast`](https://pre-commit.com/#top_level-fail_fast) | (optional: default `false`) set to `true` to have pre-commit stop<br>running hooks after the first failure. |
| [`minimum_pre_commit_version`](https://pre-commit.com/#top_level-minimum_pre_commit_version) | (optional: default `'0'`) require a minimum version of pre-commit. |

A sample top-level:

```
exclude: '^$'
fail_fast: false
repos:
-   ...
```

## .pre-commit-config.yaml - repos

The repository mapping tells pre-commit where to get the code for the hook
from.

|     |     |
| --- | --- |
| [`repo`](https://pre-commit.com/#repos-repo) | the repository url to `git clone` from<br>or one of the special sentinel values:<br>[`local`](https://pre-commit.com/#repository-local-hooks),<br>[`meta`](https://pre-commit.com/#meta-hooks). |
| [`rev`](https://pre-commit.com/#repos-rev) | the revision or tag to clone at. |
| [`hooks`](https://pre-commit.com/#repos-hooks) | A list of [hook mappings](https://pre-commit.com/#pre-commit-configyaml---hooks). |

A sample repository:

```
repos:
-   repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v1.2.3
    hooks:
    -   ...
```

## .pre-commit-config.yaml - hooks

The hook mapping configures which hook from the repository is used and allows
for customization. All optional keys will receive their default from the
repository's configuration.

|     |     |
| --- | --- |
| [`id`](https://pre-commit.com/#config-id) | which hook from the repository to use. |
| [`alias`](https://pre-commit.com/#config-alias) | (optional) allows the hook to be referenced using an additional id when<br>using `pre-commit run <hookid>`. |
| [`name`](https://pre-commit.com/#config-name) | (optional) override the name of the hook - shown during hook execution. |
| [`language_version`](https://pre-commit.com/#config-language_version) | (optional) override the language version for the<br>hook. See [Overriding Language Version](https://pre-commit.com/#overriding-language-version). |
| [`files`](https://pre-commit.com/#config-files) | (optional) override the default pattern for files to run on. |
| [`exclude`](https://pre-commit.com/#config-exclude) | (optional) file exclude pattern. |
| [`types`](https://pre-commit.com/#config-types) | (optional) override the default file types to run on (AND). See<br>[Filtering files with types](https://pre-commit.com/#filtering-files-with-types). |
| [`types_or`](https://pre-commit.com/#config-types_or) | (optional) override the default file types to run on (OR). See<br>[Filtering files with types](https://pre-commit.com/#filtering-files-with-types). |
| [`exclude_types`](https://pre-commit.com/#config-exclude_types) | (optional) file types to exclude. |
| [`args`](https://pre-commit.com/#config-args) | (optional) list of additional parameters to pass to the hook. |
| [`stages`](https://pre-commit.com/#config-stages) | (optional) selects which git hook(s) to run for.<br>See [Confining hooks to run at certain stages](https://pre-commit.com/#confining-hooks-to-run-at-certain-stages). |
| [`additional_dependencies`](https://pre-commit.com/#config-additional_dependencies) | (optional) a list of dependencies that will be installed in the<br>environment where this hook gets run. One useful application is to<br>install plugins for hooks such as `eslint`. |
| [`always_run`](https://pre-commit.com/#config-always_run) | (optional) if `true`, this hook will run even if there are no matching<br>files. |
| [`verbose`](https://pre-commit.com/#config-verbose) | (optional) if `true`, forces the output of the hook to be printed even when<br>the hook passes. |
| [`log_file`](https://pre-commit.com/#config-log_file) | (optional) if present, the hook output will additionally be written to<br>a file when the hook fails or [verbose](https://pre-commit.com/#config-verbose) is `true`. |

One example of a complete configuration:

```
repos:
-   repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v1.2.3
    hooks:
    -   id: trailing-whitespace
```

This configuration says to download the pre-commit-hooks project and run its
trailing-whitespace hook.

## Updating hooks automatically

You can update your hooks to the latest version automatically by running
[`pre-commit autoupdate`](https://pre-commit.com/#pre-commit-autoupdate). By default, this will
bring the hooks to the latest tag on the default branch.

# Usage

Run `pre-commit install` to install pre-commit into your git hooks. pre-commit
will now run on every commit. Every time you clone a project using pre-commit
running `pre-commit install` should always be the first thing you do.

If you want to manually run all pre-commit hooks on a repository, run
`pre-commit run --all-files`. To run individual hooks use
`pre-commit run <hook_id>`.

The first time pre-commit runs on a file it will automatically download,
install, and run the hook. Note that running a hook for the first time may be
slow. For example: If the machine does not have node installed, pre-commit
will download and build a copy of node.

```
$ pre-commit install
pre-commit installed at /home/asottile/workspace/pytest/.git/hooks/pre-commit
$ git commit -m "Add super awesome feature"
black....................................................................Passed
blacken-docs.........................................(no files to check)Skipped
Trim Trailing Whitespace.................................................Passed
Fix End of Files.........................................................Passed
Check Yaml...........................................(no files to check)Skipped
Debug Statements (Python)................................................Passed
Flake8...................................................................Passed
Reorder python imports...................................................Passed
pyupgrade................................................................Passed
rst ``code`` is two backticks........................(no files to check)Skipped
rst..................................................(no files to check)Skipped
changelog filenames..................................(no files to check)Skipped
[main 146c6c2c] Add super awesome feature
 1 file changed, 1 insertion(+)
```

# Creating new hooks

pre-commit currently supports hooks written in
[many languages](https://pre-commit.com/#supported-languages). As long as your git repo is an
installable package (gem, npm, pypi, etc.) or exposes an executable, it can be
used with pre-commit. Each git repo can support as many languages/hooks as you
want.

_new in 2.5.0_: `pre-commit` sets the `PRE_COMMIT=1` environment variable
during hook execution.

The hook must exit nonzero on failure or modify files.

A git repo containing pre-commit plugins must contain a `.pre-commit-hooks.yaml`
file that tells pre-commit:

|     |     |
| --- | --- |
| [`id`](https://pre-commit.com/#hooks-id) | the id of the hook - used in pre-commit-config.yaml. |
| [`name`](https://pre-commit.com/#hooks-name) | the name of the hook - shown during hook execution. |
| [`entry`](https://pre-commit.com/#hooks-entry) | the entry point - the executable to run. `entry` can also contain<br>arguments that will not be overridden such as `entry: autopep8 -i`. |
| [`language`](https://pre-commit.com/#hooks-language) | the language of the hook - tells pre-commit how to install the hook. |
| [`files`](https://pre-commit.com/#hooks-files) | (optional: default `''`) the pattern of files to run on. |
| [`exclude`](https://pre-commit.com/#hooks-exclude) | (optional: default `^$`) exclude files that were matched by [`files`](https://pre-commit.com/#hooks-files). |
| [`types`](https://pre-commit.com/#hooks-types) | (optional: default `[file]`) list of file types to run on (AND). See<br>[Filtering files with types](https://pre-commit.com/#filtering-files-with-types). |
| [`types_or`](https://pre-commit.com/#hooks-types_or) | (optional: default `[]`) list of file types to run on (OR). See<br>[Filtering files with types](https://pre-commit.com/#filtering-files-with-types). |
| [`exclude_types`](https://pre-commit.com/#hooks-exclude_types) | (optional: default `[]`) the pattern of files to exclude. |
| [`always_run`](https://pre-commit.com/#hooks-always_run) | (optional: default `false`) if `true` this hook will run even if there<br>are no matching files. |
| [`fail_fast`](https://pre-commit.com/#hooks-fail_fast) | (optional: default `false`) if `true` pre-commit will stop running<br>hooks if this hook fails. |
| [`verbose`](https://pre-commit.com/#hooks-verbose) | (optional: default `false`) if `true`, forces the output of the hook to be printed even when<br>the hook passes. |
| [`pass_filenames`](https://pre-commit.com/#hooks-pass_filenames) | (optional: default `true`) if `false` no filenames will be passed to<br>the hook. |
| [`require_serial`](https://pre-commit.com/#hooks-require_serial) | (optional: default `false`) if `true` this hook will execute using a<br>single process instead of in parallel. |
| [`description`](https://pre-commit.com/#hooks-description) | (optional: default `''`) description of the hook. used for metadata<br>purposes only. |
| [`language_version`](https://pre-commit.com/#hooks-language_version) | (optional: default `default`) see<br>[Overriding language version](https://pre-commit.com/#overriding-language-version). |
| [`minimum_pre_commit_version`](https://pre-commit.com/#hooks-minimum_pre_commit_version) | (optional: default `'0'`) allows one to indicate a minimum<br>compatible pre-commit version. |
| [`args`](https://pre-commit.com/#hooks-args) | (optional: default `[]`) list of additional parameters to pass to the hook. |
| [`stages`](https://pre-commit.com/#hooks-stages) | (optional: default (all stages)) selects which git hook(s) to run for.<br>See [Confining hooks to run at certain stages](https://pre-commit.com/#confining-hooks-to-run-at-certain-stages). |

For example:

```
-   id: trailing-whitespace
    name: Trim Trailing Whitespace
    description: This hook trims trailing whitespace.
    entry: trailing-whitespace-fixer
    language: python
    types: [text]
```

## Developing hooks interactively

Since the [`repo`](https://pre-commit.com/#repos-repo) property of `.pre-commit-config.yaml` can refer to anything
that `git clone ...` understands, it's often useful to point it at a local
directory while developing hooks.

[`pre-commit try-repo`](https://pre-commit.com/#pre-commit-try-repo) streamlines this process by
enabling a quick way to try out a repository. Here's how one might work
interactively:

_note_: you may need to provide `--commit-msg-filename` when using this
command with hook types `prepare-commit-msg` and `commit-msg`.

a commit is not necessary to `try-repo` on a local
directory. `pre-commit` will clone any tracked uncommitted changes.

```
~/work/hook-repo $ git checkout origin/main -b feature

# ... make some changes

# In another terminal or tab

~/work/other-repo $ pre-commit try-repo ../hook-repo foo --verbose --all-files
===============================================================================
Using config:
===============================================================================
repos:
-   repo: ../hook-repo
    rev: 84f01ac09fcd8610824f9626a590b83cfae9bcbd
    hooks:
    -   id: foo
===============================================================================
[INFO] Initializing environment for ../hook-repo.
Foo......................................................................Passed
- hook id: foo
- duration: 0.02s

Hello from foo hook!
```

## Supported languages

- [conda](https://pre-commit.com/#conda)
- [coursier](https://pre-commit.com/#coursier)
- [dart](https://pre-commit.com/#dart)
- [docker](https://pre-commit.com/#docker)
- [docker\_image](https://pre-commit.com/#docker_image)
- [dotnet](https://pre-commit.com/#dotnet)
- [fail](https://pre-commit.com/#fail)
- [golang](https://pre-commit.com/#golang)
- [haskell](https://pre-commit.com/#haskell)
- [julia](https://pre-commit.com/#julia)
- [lua](https://pre-commit.com/#lua)
- [node](https://pre-commit.com/#node)
- [perl](https://pre-commit.com/#perl)
- [python](https://pre-commit.com/#python)
- [r](https://pre-commit.com/#r)
- [ruby](https://pre-commit.com/#ruby)
- [rust](https://pre-commit.com/#rust)
- [swift](https://pre-commit.com/#swift)
- [pygrep](https://pre-commit.com/#pygrep)
- [unsupported](https://pre-commit.com/#unsupported)
- [unsupported\_script](https://pre-commit.com/#unsupported_script)

### conda

The hook repository must contain an `environment.yml` file which will be used
via `conda env create --file environment.yml ...` to create the environment.

The `conda` language also supports [`additional_dependencies`](https://pre-commit.com/#config-additional_dependencies)
and will pass any of the values directly into `conda install`. This language can therefore be
used with [local](https://pre-commit.com/#repository-local-hooks) hooks.

`mamba` or `micromamba` can be used to install instead via the
`PRE_COMMIT_USE_MAMBA=1` or `PRE_COMMIT_USE_MICROMAMBA=1` environment
variables.

**Support:**`conda` hooks work as long as there is a system-installed `conda`
binary (such as [`miniconda`](https://docs.conda.io/en/latest/miniconda.html)).
It has been tested on linux, macOS, and windows.

### coursier

The hook repository must have a `.pre-commit-channel` folder and that folder
must contain the coursier
[application descriptors](https://get-coursier.io/docs/2.0.0-RC6-10/cli-install.html#application-descriptor-reference)
for the hook to install. For configuring coursier hooks, your
[`entry`](https://pre-commit.com/#hooks-entry) should correspond to an executable installed from the
repository's `.pre-commit-channel` folder.

**Support:**`coursier` hooks are known to work on any system which has the
`cs` or `coursier` package manager installed. The specific coursier
applications you install may depend on various versions of the JVM, consult
the hooks' documentation for clarification. It has been tested on linux.

pre-commit also supports the `coursier` naming of the package manager
executable.

_new in 3.0.0_: `language: coursier` hooks now support `repo: local` and
`additional_dependencies`.

### dart

The hook repository must have a `pubspec.yaml` \-\- this must contain an
`executables` section which will list the binaries that will be available
after installation. Match the [`entry`](https://pre-commit.com/#hooks-entry) to an executable.

`pre-commit` will build each executable using `dart compile exe bin/{executable}.dart`.

`language: dart` also supports [`additional_dependencies`](https://pre-commit.com/#config-additional_dependencies).
to specify a version for a dependency, separate the package name by a `:`:

```
        additional_dependencies: ['hello_world_dart:1.0.0']
```

**Support:**`dart` hooks are known to work on any system which has the `dart`
sdk installed. It has been tested on linux, macOS, and windows.

### docker

The hook repository must have a `Dockerfile`. It will be installed via
`docker build .`.

Running Docker hooks requires a running Docker engine on your host. For
configuring Docker hooks, your [`entry`](https://pre-commit.com/#hooks-entry) should correspond to an executable
inside the Docker container, and will be used to override the default container
entrypoint. Your Docker `CMD` will not run when pre-commit passes a file list
as arguments to the run container command. Docker allows you to use any
language that's not supported by pre-commit as a builtin.

pre-commit will automatically mount the repository source as a volume using
`-v $PWD:/src:rw,Z` and set the working directory using `--workdir /src`.

**Support:** docker hooks are known to work on any system which has a working
`docker` executable. It has been tested on linux and macOS. Hooks that are
run via `boot2docker` are known to be unable to make modifications to files.

See [this repository](https://github.com/pre-commit/pre-commit-docker-flake8)
for an example Docker-based hook.

### docker\_image

A more lightweight approach to `docker` hooks. The `docker_image`
"language" uses existing docker images to provide hook executables.

`docker_image` hooks can be conveniently configured as [local](https://pre-commit.com/#repository-local-hooks)
hooks.

The [`entry`](https://pre-commit.com/#hooks-entry) specifies the docker tag to use. If an image has an
`ENTRYPOINT` defined, nothing special is needed to hook up the executable.
If the container does not specify an `ENTRYPOINT` or you want to change the
entrypoint you can specify it as well in your [`entry`](https://pre-commit.com/#hooks-entry).

For example:

```
-   id: dockerfile-provides-entrypoint
    name: ...
    language: docker_image
    entry: my.registry.example.com/docker-image-1:latest
-   id: dockerfile-no-entrypoint-1
    name: ...
    language: docker_image
    entry: --entrypoint my-exe my.registry.example.com/docker-image-2:latest
# Alternative equivalent solution
-   id: dockerfile-no-entrypoint-2
    name: ...
    language: docker_image
    entry: my.registry.example.com/docker-image-3:latest my-exe
```

### dotnet

dotnet hooks are installed using the system installation of the dotnet CLI.

Hook repositories must contain a dotnet CLI tool which can be `pack`ed and
`install`ed as per [this](https://docs.microsoft.com/en-us/dotnet/core/tools/global-tools-how-to-create)
example. The `entry` should match an executable created by building the
repository. Additional dependencies are not currently supported.

**Support:** dotnet hooks are known to work on any system which has the dotnet
CLI installed. It has been tested on linux and windows.

### fail

A lightweight [`language`](https://pre-commit.com/#hooks-language) to forbid files by filename. The `fail` language is
especially useful for [local](https://pre-commit.com/#repository-local-hooks) hooks.

The [`entry`](https://pre-commit.com/#hooks-entry) will be printed when the hook fails. It is suggested to provide
a brief description for [`name`](https://pre-commit.com/#hooks-name) and more verbose fix instructions in [`entry`](https://pre-commit.com/#hooks-entry).

Here's an example which prevents any file except those ending with `.rst` from
being added to the `changelog` directory:

```
-   repo: local
    hooks:
    -   id: changelogs-rst
        name: changelogs must be rst
        entry: changelog filenames must end in .rst
        language: fail
        files: 'changelog/.*(?<!\.rst)$'
```

### golang

The hook repository must contain go source code. It will be installed via
`go install ./...`. pre-commit will create an isolated `GOPATH` for each hook
and the [`entry`](https://pre-commit.com/#hooks-entry) should match an executable which will get installed into the
`GOPATH`'s `bin` directory.

This language supports `additional_dependencies` and will pass any of the values directly to `go install`. It can be used as a `repo: local` hook.

_changed in 2.17.0_: previously `go get ./...` was used

_new in 3.0.0_: pre-commit will bootstrap `go` if it is not present. `language: golang`
also now supports `language_version`

**Support:** golang hooks are known to work on any system which has go
installed. It has been tested on linux, macOS, and windows.

### haskell

_new in 3.4.0_

The hook repository must have one or more `*.cabal` files. Once installed
the `executable`s from these packages will be available to use with `entry`.

This language supports `additional_dependencies` so it can be used as a
`repo: local` hook.

**Support:** haskell hooks are known to work on any system which has `cabal`
installed. It has been tested on linux, macOS, and windows.

### julia

_new in 4.1.0_

For configuring julia hooks, your [`entry`](https://pre-commit.com/#hooks-entry) should be a path to a julia source
file relative to the hook repository (optionally with arguments).

Hooks run in an isolated package environment defined by a `Project.toml` file (optionally
with a `Manifest.toml` file) in the hook repository. If no `Project.toml` file is found the
hook is run in an empty environment.

Julia hooks support [`additional_dependencies`](https://pre-commit.com/#config-additional_dependencies) which can
be used to augment, or override, the existing environment in the hooks repository. This also
means that julia can be used as a `repo: local` hook. `additional_dependencies` are passed
to `pkg> add` and should be specified using
[Pkg REPL mode syntax](https://pkgdocs.julialang.org/v1/repl/#repl-add).

Examples:

```
- id: foo-without-args
  name: ...
  language: julia
  entry: bin/foo.jl
- id: bar-with-args
  name: ...
  language: julia
  entry: bin/bar.jl --arg1 --arg2
- id: baz-with-extra-deps
  name: ...
  language: julia
  entry: bin/baz.jl
  additional_dependencies:
   - 'ExtraDepA@1'
   - 'ExtraDepB@2.4'
```

**Support:** julia hooks are known to work on any system which has `julia` installed.

### lua

Lua hooks are installed with the version of Lua that is used by Luarocks.

**Support:** Lua hooks are known to work on any system which has Luarocks
installed. It has been tested on linux and macOS and _may_ work on windows.

### node

The hook repository must have a `package.json`. It will be installed via
`npm install .`. The installed package will provide an executable that will
match the [`entry`](https://pre-commit.com/#hooks-entry) – usually through `bin` in package.json.

**Support:** node hooks work without any system-level dependencies. It has
been tested on linux, windows, and macOS and _may_ work under cygwin.

### perl

Perl hooks are installed using the system installation of
[cpan](https://perldoc.perl.org/cpan), the CPAN package installer
that comes with Perl.

Hook repositories must have something that `cpan` supports, typically
`Makefile.PL` or `Build.PL`, which it uses to install an executable to
use in the [`entry`](https://pre-commit.com/#hooks-entry) definition for your hook. The repository will be installed
via `cpan -T .` (with the installed files stored in your pre-commit cache,
not polluting other Perl installations).

When specifying [`additional_dependencies`](https://pre-commit.com/#config-additional_dependencies) for Perl, you can use any of the
[install argument formats understood by `cpan`](https://perldoc.perl.org/CPAN#get%2c-make%2c-test%2c-install%2c-clean-modules-or-distributions).

**Support:** Perl hooks currently require a pre-existing Perl installation,
including the `cpan` tool in `PATH`. It has been tested on linux, macOS, and
Windows.

### python

The hook repository must be installable via `pip install .` (usually by either
`setup.py` or `pyproject.toml`). The installed package will provide an
executable that will match the [`entry`](https://pre-commit.com/#hooks-entry) – usually through `console_scripts` or
`scripts` in setup.py.

This language also supports `additional_dependencies`
so it can be used with [local](https://pre-commit.com/#repository-local-hooks) hooks.
The specified dependencies will be appended to the `pip install` command.

**Support:** python hooks work without any system-level dependencies. It
has been tested on linux, macOS, windows, and cygwin.

### r

This hook repository must have a `renv.lock` file that will be restored with
[`renv::restore()`](https://rstudio.github.io/renv/reference/restore.html) on
hook installation. If the repository is an R package (i.e. has `Type: Package`
in `DESCRIPTION`), it is installed. The supported syntax in [`entry`](https://pre-commit.com/#hooks-entry) is
`Rscript -e {expression}` or `Rscript path/relative/to/hook/root`. The
R Startup process is skipped (emulating `--vanilla`), as all configuration
should be exposed via [`args`](https://pre-commit.com/#hooks-args) for maximal transparency and portability.

When specifying [`additional_dependencies`](https://pre-commit.com/#config-additional_dependencies)
for R, you can use any of the install argument formats understood by
[`renv::install()`](https://rstudio.github.io/renv/reference/install.html#examples).

**Support:**`r` hooks work as long as [`R`](https://www.r-project.org/) is
installed and on `PATH`. It has been tested on linux, macOS, and windows.

### ruby

The hook repository must have a `*.gemspec`. It will be installed via
`gem build *.gemspec && gem install *.gem`. The installed package will
produce an executable that will match the [`entry`](https://pre-commit.com/#hooks-entry) – usually through
`executables` in your gemspec.

**Support:** ruby hooks work without any system-level dependencies. It has
been tested on linux and macOS and _may_ work under cygwin.

### rust

Rust hooks are installed using [Cargo](https://github.com/rust-lang/cargo),
Rust's official package manager.

Hook repositories must have a `Cargo.toml` file which produces at least one
binary ( [example](https://github.com/chriskuehl/example-rust-pre-commit-hook)),
whose name should match the [`entry`](https://pre-commit.com/#hooks-entry) definition for your hook. The repo will be
installed via `cargo install --bins` (with the binaries stored in your
pre-commit cache, not polluting your user-level Cargo installations).

When specifying [`additional_dependencies`](https://pre-commit.com/#config-additional_dependencies) for Rust, you can use the syntax
`{package_name}:{package_version}` to specify a new library dependency (used to
build _your_ hook repo), or the special syntax
`cli:{package_name}:{package_version}` for a CLI dependency (built separately,
with binaries made available for use by hooks).

pre-commit will bootstrap `rust` if it is not present.
`language: rust` also supports `language_version`

**Support:** It has been tested on linux, Windows, and macOS.

### swift

The hook repository must have a `Package.swift`. It will be installed via
`swift build -c release`. The [`entry`](https://pre-commit.com/#hooks-entry) should match an executable created by
building the repository.

**Support:** swift hooks are known to work on any system which has swift
installed. It has been tested on linux and macOS.

### pygrep

A cross-platform python implementation of `grep` – pygrep hooks are a quick
way to write a simple hook which prevents commits by file matching. Specify
the regex as the [`entry`](https://pre-commit.com/#hooks-entry). The [`entry`](https://pre-commit.com/#hooks-entry) may be any python
[regular expression](https://pre-commit.com/#regular-expression-syntax). For case insensitive regexes you
can apply the `(?i)` flag as the start of your entry, or use `args: [-i]`.

For multiline matches, use `args: [--multiline]`.

To require all files to match, use `args: [--negate]`.

**Support:** pygrep hooks are supported on all platforms which pre-commit runs
on.

### unsupported

_new in 4.4.0_: previously `language: system`. the alias will be removed in a
future version

System hooks provide a way to write hooks for system-level executables which
don't have a supported language above (or have special environment
requirements that don't allow them to run in isolation such as pylint).

This hook type will not be given a virtual environment to work with – if it
needs additional dependencies the consumer must install them manually.

### unsupported\_script

_new in 4.4.0_: previously `language: script`. the alias will be removed in a
future version

Script hooks provide a way to write simple scripts which validate files. The
[`entry`](https://pre-commit.com/#hooks-entry) should be a path relative to the root of the hook repository.

This hook type will not be given a virtual environment to work with – if it
needs additional dependencies the consumer must install them manually.

# Command line interface

All pre-commit commands take the following options:

- `--color {auto,always,never}`: whether to use color in output.
Defaults to `auto`. can be overridden by using
`PRE_COMMIT_COLOR={auto,always,never}` or disabled using `TERM=dumb`.
- `-c CONFIG`, `--config CONFIG`: path to alternate config file
- `-h`, `--help`: show help and available options.

`pre-commit` exits with specific codes:

- `1`: a detected / expected error
- `3`: an unexpected error
- `130`: the process was interrupted by `^C`

## pre-commit autoupdate \[options\]

Auto-update pre-commit config to the latest repos' versions.

Options:

- `--bleeding-edge`: update to the bleeding edge of the default branch instead
of the latest tagged version (the default behaviour).
- `--freeze`: Store "frozen" hashes in [`rev`](https://pre-commit.com/#repos-rev) instead of tag names.
- `--repo REPO`: Only update this repository. This option may be specified
multiple times.
- `-j` / `--jobs`: _new in 3.3.0_ Number of threads to use (default: 1).

Here are some sample invocations using this `.pre-commit-config.yaml`:

```
repos:
-   repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v2.1.0
    hooks:
    -   id: trailing-whitespace
-   repo: https://github.com/asottile/pyupgrade
    rev: v1.25.0
    hooks:
    -   id: pyupgrade
        args: [--py36-plus]
```

```
$ : default: update to latest tag on default branch
$ pre-commit autoupdate  # by default: pick tags
Updating https://github.com/pre-commit/pre-commit-hooks ... updating v2.1.0 -> v2.4.0.
Updating https://github.com/asottile/pyupgrade ... updating v1.25.0 -> v1.25.2.
$ grep rev: .pre-commit-config.yaml
    rev: v2.4.0
    rev: v1.25.2
```

```
$ : update a specific repository to the latest revision of the default branch
$ pre-commit autoupdate --bleeding-edge --repo https://github.com/pre-commit/pre-commit-hooks
Updating https://github.com/pre-commit/pre-commit-hooks ... updating v2.1.0 -> 5df1a4bf6f04a1ed3a643167b38d502575e29aef.
$ grep rev: .pre-commit-config.yaml
    rev: 5df1a4bf6f04a1ed3a643167b38d502575e29aef
    rev: v1.25.0
```

```
$ : update to frozen versions
$ pre-commit autoupdate --freeze
Updating https://github.com/pre-commit/pre-commit-hooks ... updating v2.1.0 -> v2.4.0 (frozen).
Updating https://github.com/asottile/pyupgrade ... updating v1.25.0 -> v1.25.2 (frozen).
$ grep rev: .pre-commit-config.yaml
    rev: 0161422b4e09b47536ea13f49e786eb3616fe0d7  # frozen: v2.4.0
    rev: 34a269fd7650d264e4de7603157c10d0a9bb8211  # frozen: v1.25.2
```

pre-commit will preferentially pick tags containing a `.` if there are ties.

## pre-commit clean \[options\]

Clean out cached pre-commit files.

Options: (no additional options)

## pre-commit gc \[options\]

Clean unused cached repos.

`pre-commit` keeps a cache of installed hook repositories which grows over
time. This command can be run periodically to clean out unused repos from
the cache directory.

Options: (no additional options)

## pre-commit init-templatedir DIRECTORY \[options\]

Install hook script in a directory intended for use with
`git config init.templateDir`.

Options:

- `-t HOOK_TYPE, --hook-type HOOK_TYPE`:
which hook type to install.

Some example useful invocations:

```
git config --global init.templateDir ~/.git-template
pre-commit init-templatedir ~/.git-template
```

For Windows cmd.exe use `%HOMEPATH%` instead of `~`:

```
pre-commit init-templatedir %HOMEPATH%\.git-template
```

For Windows PowerShell use `$HOME` instead of `~`:

```
pre-commit init-templatedir $HOME\.git-template
```

Now whenever a repository is cloned or created, it will have the hooks set up
already!

## pre-commit install \[options\]

Install the pre-commit script.

Options:

- `-f`, `--overwrite`: Replace any existing git hooks with the pre-commit
script.
- `--install-hooks`: Also install environments for all available hooks now
(rather than when they are first executed). See [`pre-commit install-hooks`](https://pre-commit.com/#pre-commit-install-hooks).
- `-t HOOK_TYPE, --hook-type HOOK_TYPE`:
Specify which hook type to install.
- `--allow-missing-config`: Hook scripts will permit a missing configuration
file.

Some example useful invocations:

- `pre-commit install`: Default invocation. Installs the hook scripts
alongside any existing git hooks.
- `pre-commit install --install-hooks --overwrite`: Idempotently replaces
existing git hook scripts with pre-commit, and also installs hook
environments.

`pre-commit install` will install hooks from
[`default_install_hook_types`](https://pre-commit.com/#top_level-default_install_hook_types) if
`--hook-type` is not specified on the command line.

## pre-commit install-hooks \[options\]

Install all missing environments for the available hooks. Unless this command or
`install --install-hooks` is executed, each hook's environment is created the
first time the hook is called.

Each hook is initialized in a separate environment appropriate to the language
the hook is written in. See [supported languages](https://pre-commit.com/#supported-languages).

This command does not install the pre-commit script. To install the script along with
the hook environments in one command, use `pre-commit install --install-hooks`.

Options: (no additional options)

## pre-commit migrate-config \[options\]

Migrate list configuration to the new map configuration format.

Options: (no additional options)

## pre-commit run \[hook-id\] \[options\]

Run hooks.

Options:

- `[hook-id]`: specify a single hook-id to run only that hook.
- `-a`, `--all-files`: run on all the files in the repo.
- `--files [FILES [FILES ...]]`: specific filenames to run hooks on.
- `--from-ref FROM_REF` \+ `--to-ref TO_REF`: run against the files changed
between `FROM_REF...TO_REF` in git.
- `--hook-stage STAGE`: select a [`stage` to run](https://pre-commit.com/#confining-hooks-to-run-at-certain-stages).
- `--show-diff-on-failure`: when hooks fail, run `git diff` directly afterward.
- `-v`, `--verbose`: produce hook output independent of success. Include hook
ids in output.

Some example useful invocations:

- `pre-commit run`: this is what pre-commit runs by default when committing.
This will run all hooks against currently staged files.
- `pre-commit run --all-files`: run all the hooks against all the files. This
is a useful invocation if you are using pre-commit in CI.
- `pre-commit run flake8`: run the `flake8` hook against all staged files.
- `git ls-files -- '*.py' | xargs pre-commit run --files`: run all hooks
against all `*.py` files in the repository.
- `pre-commit run --from-ref HEAD^^^ --to-ref HEAD`: run against the files that
have changed between `HEAD^^^` and `HEAD`. This form is useful when
leveraged in a pre-receive hook.

## pre-commit sample-config \[options\]

Produce a sample `.pre-commit-config.yaml`.

Options: (no additional options)

## pre-commit try-repo REPO \[options\]

Try the hooks in a repository, useful for developing new hooks.
`try-repo` can also be used for testing out a repository before adding it to
your configuration. `try-repo` prints a configuration it generates based on
the remote hook repository before running the hooks.

Options:

- `REPO`: required clonable hooks repository. Can be a local path on
disk.
- `--ref REF`: Manually select a ref to run against, otherwise the `HEAD`
revision will be used.
- `pre-commit try-repo` also supports all available options for
[`pre-commit run`](https://pre-commit.com/#pre-commit-run).

Some example useful invocations:

- `pre-commit try-repo https://github.com/pre-commit/pre-commit-hooks`: runs
all the hooks in the latest revision of `pre-commit/pre-commit-hooks`.
- `pre-commit try-repo ../path/to/repo`: run all the hooks in a repository on
disk.
- `pre-commit try-repo ../pre-commit-hooks flake8`: run only the `flake8` hook
configured in a local `../pre-commit-hooks` repository.
- See [`pre-commit run`](https://pre-commit.com/#pre-commit-run) for more useful `run` invocations
which are also supported by `pre-commit try-repo`.

## pre-commit uninstall \[options\]

Uninstall the pre-commit script.

Options:

- `-t HOOK_TYPE, --hook-type HOOK_TYPE`: which hook type to uninstall.

## pre-commit validate-config \[options\] \[filenames ...\]

Validate .pre-commit-config.yaml files

## pre-commit validate-manifest \[options\] \[filenames ...\]

Validate .pre-commit-hooks.yaml files

# Advanced features

## Running in migration mode

By default, if you have existing hooks `pre-commit install` will install in a
migration mode which runs both your existing hooks and hooks for pre-commit.
To disable this behavior, pass `-f` / `--overwrite` to the `install` command.
If you decide not to use pre-commit, `pre-commit uninstall` will
restore your hooks to the state prior to installation.

## Temporarily disabling hooks

Not all hooks are perfect so sometimes you may need to skip execution of one
or more hooks. pre-commit solves this by querying a `SKIP` environment
variable. The `SKIP` environment variable is a comma separated list of hook
ids. This allows you to skip a single hook instead of `--no-verify`ing the
entire commit.

```
$ SKIP=flake8 git commit -m "foo"
```

## Confining hooks to run at certain stages

pre-commit supports many different types of `git` hooks (not just
`pre-commit`!).

Providers of hooks can select which git hooks they run on by setting the
[`stages`](https://pre-commit.com/#hooks-stages) property in `.pre-commit-hooks.yaml` \-\- this can
also be overridden by setting [`stages`](https://pre-commit.com/#config-stages) in
`.pre-commit-config.yaml`. If `stages` is not set in either of those places
the default value will be pulled from the top-level
[`default_stages`](https://pre-commit.com/#top_level-default_stages) option (which defaults to _all_
stages). By default, tools are enabled for [every hook type](https://pre-commit.com/#supported-git-hooks)
that pre-commit supports.

_new in 3.2.0_: The values of `stages` match the hook names. Previously,
`commit`, `push`, and `merge-commit` matched `pre-commit`, `pre-push`, and
`pre-merge-commit` respectively.

The `manual` stage (via `stages: [manual]`) is a special stage which will not
be automatically triggered by any `git` hook -- this is useful if you want to
add a tool which is not automatically run, but is run on demand using
`pre-commit run --hook-stage manual [hookid]`.

If you are authoring a tool, it is usually a good idea to provide an appropriate
`stages` property. For example a reasonable setting for a linter or code
formatter would be `stages: [pre-commit, pre-merge-commit, pre-push, manual]`.

To install `pre-commit` for particular git hooks, pass `--hook-type` to
`pre-commit install`. This can be specified multiple times such as:

```
$ pre-commit install --hook-type pre-commit --hook-type pre-push
pre-commit installed at .git/hooks/pre-commit
pre-commit installed at .git/hooks/pre-push
```

Additionally, one can specify a default set of git hook types to be installed
for by setting the top-level [`default_install_hook_types`](https://pre-commit.com/#top_level-default_install_hook_types).

For example:

```
default_install_hook_types: [pre-commit, pre-push, commit-msg]
```

```
$ pre-commit  install
pre-commit installed at .git/hooks/pre-commit
pre-commit installed at .git/hooks/pre-push
pre-commit installed at .git/hooks/commit-msg
```

## Supported git hooks

- [commit-msg](https://pre-commit.com/#commit-msg)
- [post-checkout](https://pre-commit.com/#post-checkout)
- [post-commit](https://pre-commit.com/#post-commit)
- [post-merge](https://pre-commit.com/#post-merge)
- [post-rewrite](https://pre-commit.com/#post-rewrite)
- [pre-commit](https://pre-commit.com/#pre-commit)
- [pre-merge-commit](https://pre-commit.com/#pre-merge-commit)
- [pre-push](https://pre-commit.com/#pre-push)
- [pre-rebase](https://pre-commit.com/#pre-rebase)
- [prepare-commit-msg](https://pre-commit.com/#prepare-commit-msg)

### commit-msg

[git commit-msg docs](https://git-scm.com/docs/githooks#_commit_msg)

`commit-msg` hooks will be passed a single filename -- this file contains the
current contents of the commit message to be validated. The commit will be
aborted if there is a nonzero exit code.

### post-checkout

[git post-checkout docs](https://git-scm.com/docs/githooks#_post_checkout)

post-checkout hooks run _after_ a `checkout` has occurred and can be used to
set up or manage state in the repository.

`post-checkout` hooks do not operate on files so they must be set as
`always_run: true` or they will always be skipped.

environment variables:

- `PRE_COMMIT_FROM_REF`: the first argument to the `post-checkout` git hook
- `PRE_COMMIT_TO_REF`: the second argument to the `post-checkout` git hook
- `PRE_COMMIT_CHECKOUT_TYPE`: the third argument to the `post-checkout` git hook

### post-commit

[git post-commit docs](https://git-scm.com/docs/githooks#_post_commit)

`post-commit` runs after the commit has already succeeded so it cannot be used
to prevent the commit from happening.

`post-commit` hooks do not operate on files so they must be set as
`always_run: true` or they will always be skipped.

### post-merge

[git post-merge docs](https://git-scm.com/docs/githooks#_post_merge)

`post-merge` runs after a successful `git merge`.

`post-merge` hooks do not operate on files so they must be set as
`always_run: true` or they will always be skipped.

environment variables:

- `PRE_COMMIT_IS_SQUASH_MERGE`: the first argument to the `post-merge` git hook.

### post-rewrite

[git post-rewrite docs](https://git-scm.com/docs/githooks#_post_rewrite)

`post-rewrite` runs after a git command which modifies history such as
`git commit --amend` or `git rebase`.

`post-rewrite` hooks do not operate on files so they must be set as
`always_run: true` or they will always be skipped.

environment variables:

- `PRE_COMMIT_REWRITE_COMMAND`: the first argument to the `post-rewrite` git hook.

### pre-commit

[git pre-commit docs](https://git-scm.com/docs/githooks#_pre_commit)

`pre-commit` is triggered before the commit is finalized to allow checks on the
code being committed. Running hooks on unstaged changes can lead to both
false-positives and false-negatives during committing. pre-commit only runs
on the staged contents of files by temporarily stashing the unstaged changes
while running hooks.

### pre-merge-commit

[git pre-merge-commit docs](https://git-scm.com/docs/githooks#_pre_merge_commit)

`pre-merge-commit` fires after a merge succeeds but before the merge commit is
created. This hook runs on all staged files from the merge.

Note that you need to be using at least git 2.24 for this hook.

### pre-push

[git pre-push docs](https://git-scm.com/docs/githooks#_pre_push)

`pre-push` is triggered on `git push`.

environment variables:

- `PRE_COMMIT_FROM_REF`: the revision that is being pushed to.
- `PRE_COMMIT_TO_REF`: the local revision that is being pushed to the remote.
- `PRE_COMMIT_REMOTE_NAME`: which remote is being pushed to (for example `origin`)
- `PRE_COMMIT_REMOTE_URL`: the url of the remote that is being pushed to (for
example `git@github.com:pre-commit/pre-commit`)
- `PRE_COMMIT_REMOTE_BRANCH`: the name of the remote branch to which we are
pushing (for example `refs/heads/target-branch`)
- `PRE_COMMIT_LOCAL_BRANCH`: the name of the local branch that is being pushed
to the remote (for example `HEAD`)

### pre-rebase

_new in 3.2.0_

[git pre-rebase docs](https://git-scm.com/docs/githooks#_pre_rebase)

`pre-rebase` is triggered before a rebase occurs. A hook failure can cancel a
rebase from occurring.

`pre-rebase` hooks do not operate on files so they must be set as
`always_run: true` or they will always be skipped.

environment variables:

- `PRE_COMMIT_PRE_REBASE_UPSTREAM`: the first argument to the `pre-rebase` git hook
- `PRE_COMMIT_PRE_REBASE_BRANCH`: the second argument to the `pre-rebase` git hook.

### prepare-commit-msg

[git prepare-commit-msg docs](https://git-scm.com/docs/githooks#_prepare_commit_msg)

`prepare-commit-msg` hooks will be passed a single filename -- this file may
be empty or it could contain the commit message from `-m` or from other
templates. `prepare-commit-msg` hooks can modify the contents of this file to
change what will be committed. A hook may want to check for `GIT_EDITOR=:` as
this indicates that no editor will be launched. If a hook exits nonzero, the
commit will be aborted.

environment variables:

- `PRE_COMMIT_COMMIT_MSG_SOURCE`: the second argument to the
`prepare-commit-msg` git hook
- `PRE_COMMIT_COMMIT_OBJECT_NAME`: the third argument to the
`prepare-commit-msg` git hook

## Passing arguments to hooks

Sometimes hooks require arguments to run correctly. You can pass static
arguments by specifying the [`args`](https://pre-commit.com/#config-args) property in your `.pre-commit-config.yaml`
as follows:

```
-   repo: https://github.com/PyCQA/flake8
    rev: 4.0.1
    hooks:
    -   id: flake8
        args: [--max-line-length=131]
```

This will pass `--max-line-length=131` to `flake8`.

### Arguments pattern in hooks

If you are writing your own custom hook, your hook should expect to receive
the [`args`](https://pre-commit.com/#config-args) value and then a list of staged files.

For example, assuming a `.pre-commit-config.yaml`:

```
-   repo: https://github.com/path/to/your/hook/repo
    rev: badf00ddeadbeef
    hooks:
    -   id: my-hook-script-id
        args: [--myarg1=1, --myarg1=2]
```

When you next run `pre-commit`, your script will be called:

```
path/to/script-or-system-exe --myarg1=1 --myarg1=2 dir/file1 dir/file2 file3
```

If the [`args`](https://pre-commit.com/#config-args) property is empty or not defined, your script will be called:

```
path/to/script-or-system-exe dir/file1 dir/file2 file3
```

When creating local hooks, there's no reason to put command arguments
into [`args`](https://pre-commit.com/#config-args) as there is nothing which can override them --
instead put your arguments directly in the hook [`entry`](https://pre-commit.com/#hooks-entry).

For example:

```
-   repo: local
    hooks:
    -   id: check-requirements
        name: check requirements files
        language: unsupported
        entry: python -m scripts.check_requirements --compare
        files: ^requirements.*\.txt$
```

## Repository local hooks

Repository-local hooks are useful when:

- The scripts are tightly coupled to the repository and it makes sense to
distribute the hook scripts with the repository.
- Hooks require state that is only present in a built artifact of your
repository (such as your app's virtualenv for pylint).
- The official repository for a linter doesn't have the pre-commit metadata.

You can configure repository-local hooks by specifying the [`repo`](https://pre-commit.com/#repos-repo) as the
sentinel `local`.

local hooks can use any language which supports [`additional_dependencies`](https://pre-commit.com/#config-additional_dependencies)
or [`docker_image`](https://pre-commit.com/#docker_image) / [`fail`](https://pre-commit.com/#fail) / [`pygrep`](https://pre-commit.com/#pygrep) / [`unsupported`](https://pre-commit.com/#unsupported) / [`unsupported_script`](https://pre-commit.com/#unsupported_script).
This enables you to install things which previously would require a trivial
mirror repository.

A `local` hook must define [`id`](https://pre-commit.com/#hooks-id), [`name`](https://pre-commit.com/#hooks-name), [`language`](https://pre-commit.com/#hooks-language),
[`entry`](https://pre-commit.com/#hooks-entry), and [`files`](https://pre-commit.com/#hooks-files) / [`types`](https://pre-commit.com/#hooks-types)
as specified under [Creating new hooks](https://pre-commit.com/#new-hooks).

Here's an example configuration with a few `local` hooks:

```
-   repo: local
    hooks:
    -   id: pylint
        name: pylint
        entry: pylint
        language: unsupported
        types: [python]
        require_serial: true
    -   id: check-x
        name: Check X
        entry: ./bin/check-x.sh
        language: unsupported_script
        files: \.x$
    -   id: scss-lint
        name: scss-lint
        entry: scss-lint
        language: ruby
        language_version: 2.1.5
        types: [scss]
        additional_dependencies: ['scss_lint:0.52.0']
```

## meta hooks

`pre-commit` provides several hooks which are useful for checking the
pre-commit configuration itself. These can be enabled using `repo: meta`.

```
-   repo: meta
    hooks:
    -   id: ...
```

The currently available `meta` hooks:

|     |     |
| --- | --- |
| [`check-hooks-apply`](https://pre-commit.com/#meta-check_hooks_apply) | ensures that the configured hooks apply to at least one file in the<br>repository. |
| [`check-useless-excludes`](https://pre-commit.com/#meta-check_useless_excludes) | ensures that `exclude` directives apply to _any_ file in the<br>repository. |
| [`identity`](https://pre-commit.com/#meta-identity) | a simple hook which prints all arguments passed to it, useful for<br>debugging. |

## `pre-commit hazmat`

"hazardous materials"

pre-commit provides a few `entry` prefix "helpers" for unusual situations.

in case it's not clear, using these is _usually_ a bad idea.

_note_: hazmat helpers do not work on languages which adjust `entry` (`docker`
/ `docker_image` / `fail` / `julia` / `pygrep` / `r` / `unsupported_script`).

### `pre-commit hazmat cd`

_new in 4.5.0_

for "monorepo" usage one can use this to target a subdirectory.

this entry prefix will cd to the target subdir and adjust filename arguments

example usage:

```
# recommended:
# minimum_pre_commit_version: 4.5.0
repos:
-   repo: ...
    rev: ...
    hooks:
    -   id: example
        alias: example-repo1
        name: example (repo1)
        files: ^repo1/
        # important! ends with `--`
        # important! copy `args: [...]` to entry and blank out `args: []`
        entry: pre-commit hazmat cd repo1 example-bin --arg1 --
        args: []

    -   id: example
        alias: example-repo2
        name: example (repo2)
        files: ^repo2/
        entry: pre-commit hazmat cd repo2 example-bin --arg1 --
        args: []

    # ... etc.
```

### `pre-commit hazmat ignore-exit-code`

_new in 4.5.0_

it's a bad idea to introduce warning noise but this gives you a way to do it.

example:

```
# recommended:
# minimum_pre_commit_version: 4.5.0
repos:
-   repo: ...
    rev: ...
    hooks:
    -   id: example
        # important! copy `args: [...]` to entry and blank out `args: []`
        entry: pre-commit hazmat ignore-exit-code example-bin --arg1 --
        args: []
        # otherwise the output will always be hidden
        verbose: true
```

### `pre-commit hazmat n1`

_new in 4.5.0_

some hooks only take one filename argument. this runs them one at a time
(which is super slow!)

example:

```
# recommended:
# minimum_pre_commit_version: 4.5.0
repos:
-   repo: ...
    rev: ...
    hooks:
    -   id: example
        # important! ends with `--`
        # important! copy `args: [...]` to entry and blank out `args: []`
        entry: pre-commit hazmat n1 example-bin --arg1 --
        args: []
```

## usage with git 2.54+ hook configuration

_new in 4.6.0_: pre-commit improved support for `git config`-based hooks.
a later version will change `pre-commit install` to use this approach.

[git 2.54](https://github.blog/open-source/git/highlights-from-git-2-54/#h-config-based-hooks) introduced a new way to install git hook tools via `git config`.

the basic gist is the following enables a hook in a git repo:

```
git config set hook.<name>.event pre-push
git config set hook.<name>.command 'some command here'
```

an example setup with `pre-commit` might look like:

```
# note, the "hook" name here is `pre-commit.pre-commit`
# for the `pre-commit` "tool" and the `pre-commit` "event"
git config set hook.pre-commit.pre-commit.event pre-commit
git config set hook.pre-commit.pre-commit.command 'pre-commit hook-impl --hook-type pre-commit --'

# please follow that naming scheme for future compatibility with `pre-commit install`

# an example with pre-push:
#
# git config set hook.pre-commit.pre-push.event pre-push
# git config set hook.pre-commit.pre-push.command 'pre-commit hook-impl --hook-type pre-push --'
```

`pre-commit hook-impl` is a "hidden" implementation command with these options:

- `--hook-type ...`: the [hook type](https://pre-commit.com/#supported-git-hooks) to use
- `--config ...`: (optional) path to `.pre-commit-config.yaml`
- `--skip-on-missing-config`: silently pass when a config is missing

some interesting applications of this:

### "global" installation of pre-commit

with `git config set --global ...` this can automatically enable pre-commit
for all repositories:

```
git config set --global hook.pre-commit.pre-commit.event pre-commit
git config set --global hook.pre-commit.pre-commit.command 'pre-commit hook-impl --hook-type pre-commit --skip-on-missing-config --'
```

- this setup **not recommended** as it can lead to accidentally running hooks
when interacting with an untrusted repository.
- `--skip-on-missing-config` is recommended here as arbitrary git repositories
may not have a `.pre-commit-config.yaml`.

### always running a hook on all files

since you can configure pre-commit as many times as you want you _could_ invoke
pre-commit to run a particular hook always and on all files

```
git config set hook.pre-commit.pre-commit-always.event pre-commit
git config set hook.pre-commit.pre-commit-always.command 'pre-commit run hookid --hook-stage pre-commit --all-files'
```

_note_: this is not recommended as it has the tendancy to be slow and deviates
from the normal expectations of pre-commit.

## automatically enabling pre-commit on repositories

_note_: if you are on a new-enough version of `git` you may want to use
[this approach](https://pre-commit.com/#global-installation-of-pre-commit) instead.

* * *

`pre-commit init-templatedir` can be used to set up a skeleton for `git`'s
`init.templateDir` option. This means that any newly cloned repository will
automatically have the hooks set up without the need to run
`pre-commit install`.

To configure, first set `git`'s `init.templateDir` \-\- in this example I'm
using `~/.git-template` as my template directory.

```
$ git config --global init.templateDir ~/.git-template
$ pre-commit init-templatedir ~/.git-template
pre-commit installed at /home/asottile/.git-template/hooks/pre-commit
```

Now whenever you clone a pre-commit enabled repo, the hooks will already be
set up!

```
$ git clone -q git@github.com:asottile/pyupgrade
$ cd pyupgrade
$ git commit --allow-empty -m 'Hello world!'
Check docstring is first.............................(no files to check)Skipped
Check Yaml...........................................(no files to check)Skipped
Debug Statements (Python)............................(no files to check)Skipped
...
```

`init-templatedir` uses the `--allow-missing-config` option from
`pre-commit install` so repos without a config will be skipped:

```
$ git init sample
Initialized empty Git repository in /tmp/sample/.git/
$ cd sample
$ git commit --allow-empty -m 'Initial commit'
`.pre-commit-config.yaml` config file not found. Skipping `pre-commit`.
[main (root-commit) d1b39c1] Initial commit
```

To still require opt-in, but prompt the user to set up pre-commit use a
template hook as follows (for example in `~/.git-template/hooks/pre-commit`).

```
#!/usr/bin/env bash
if [ -f .pre-commit-config.yaml ]; then
    echo 'pre-commit configuration detected, but `pre-commit install` was never run' 1>&2
    exit 1
fi
```

With this, a forgotten `pre-commit install` produces an error on commit:

```
$ git clone -q https://github.com/asottile/pyupgrade
$ cd pyupgrade/
$ git commit -m 'foo'
pre-commit configuration detected, but `pre-commit install` was never run
```

## Filtering files with types

Filtering with `types` provides several advantages over traditional filtering
with `files`.

- no error-prone regular expressions
- files can be matched by their shebang (even when extensionless)
- symlinks / submodules can be easily ignored

`types` is specified per hook as an array of tags. The tags are discovered
through a set of heuristics by the
[identify](https://github.com/pre-commit/identify) library. `identify` was
chosen as it is a small portable pure python library.

Some of the common tags you'll find from identify:

- `file`
- `symlink`
- `directory` \- in the context of pre-commit this will be a submodule
- `executable` \- whether the file has the executable bit set
- `text` \- whether the file looks like a text file
- `binary` \- whether the file looks like a binary file
- [tags by extension / naming convention](https://github.com/pre-commit/identify/blob/main/identify/extensions.py)
- [tags by shebang (`#!`)](https://github.com/pre-commit/identify/blob/main/identify/interpreters.py)

To discover the type of any file on disk, you can use `identify`'s cli:

```
$ identify-cli setup.py
["file", "non-executable", "python", "text"]
$ identify-cli some-random-file
["file", "non-executable", "text"]
$ identify-cli --filename-only some-random-file; echo $?
1
```

If a file extension you use is not supported, please
[submit a pull request](https://github.com/pre-commit/identify)!

`types`, `types_or`, and `files` are evaluated together with `AND` when
filtering. Tags within `types` are also evaluated using `AND`.

Tags within `types_or` are evaluated using `OR`.

For example:

```
    files: ^foo/
    types: [file, python]
```

will match a file `foo/1.py` but will not match `setup.py`.

Another example:

```
    files: ^foo/
    types_or: [javascript, jsx, ts, tsx]
```

will match any of `foo/bar.js` / `foo/bar.jsx` / `foo/bar.ts` / `foo/bar.tsx`
but not `baz.js`.

If you want to match a file path that isn't included in a `type` when using an
existing hook you'll need to revert back to `files` only matching by overriding
the `types` setting. Here's an example of using `check-json` against non-json
files:

```
    -   id: check-json
        types: [file]  # override `types: [json]`
        files: \.(json|myext)$
```

Files can also be matched by shebang. With `types: python`, an `exe` starting
with `#!/usr/bin/env python3` will also be matched.

As with `files` and `exclude`, you can also exclude types if necessary using
`exclude_types`.

## Regular expressions

The patterns for `files` and `exclude` are python
[regular expressions](https://docs.python.org/3/library/re.html#regular-expression-syntax)
and are matched with [`re.search`](https://docs.python.org/3/library/re.html#re.search).

As such, you can use any of the features that python regexes support.

If you find that your regular expression is becoming unwieldy due to a long
list of excluded / included things, you may find a
[verbose](https://docs.python.org/3/library/re.html#re.VERBOSE) regular
expression useful. One can enable this with yaml's multiline literals and
the `(?x)` regex flag.

```
# ...
    -   id: my-hook
        exclude: |
            (?x)^(
                path/to/file1.py|
                path/to/file2.py|
                path/to/file3.py
            )$
```

## Overriding language version

Sometimes you only want to run the hooks on a specific version of the
language. For each language, they default to using the system installed
language (So for example if I’m running `python3.7` and a hook specifies
`python`, pre-commit will run the hook using `python3.7`). Sometimes you
don’t want the default system installed version so you can override this on a
per-hook basis by setting the [`language_version`](https://pre-commit.com/#config-language_version).

```
-   repo: https://github.com/pre-commit/mirrors-scss-lint
    rev: v0.54.0
    hooks:
    -   id: scss-lint
        language_version: 2.1.5
```

This tells pre-commit to use ruby `2.1.5` to run the `scss-lint` hook.

Valid values for specific languages are listed below:

- python: Whatever system installed python interpreters you have. The value of
this argument is passed as the `-p` to `virtualenv`.
  - on windows the
    [pep394](https://www.python.org/dev/peps/pep-0394/) name will be
    translated into a py launcher call for portability. So continue to use
    names like `python3` (`py -3`) or `python3.6` (`py -3.6`) even on
    windows.
- node: See [nodeenv](https://github.com/ekalinin/nodeenv#advanced).
- ruby: See [ruby-build](https://github.com/sstephenson/ruby-build/tree/master/share/ruby-build).
- rust: `language_version` is passed to `rustup`
- _new in 3.0.0_ golang: use the versions on [go.dev/dl](https://go.dev/dl/) such as `1.19.5`

you can set [`default_language_version`](https://pre-commit.com/#top_level-default_language_version)
at the [top level](https://pre-commit.com/#pre-commit-configyaml---top-level) in your configuration to
control the default versions across all hooks of a language.

```
default_language_version:
    # force all unspecified python hooks to run python3
    python: python3
    # force all unspecified ruby hooks to run ruby 2.1.5
    ruby: 2.1.5
```

## badging your repository

you can add a badge to your repository to show your contributors / users that
you use pre-commit!

[https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit](https://github.com/pre-commit/pre-commit)

- Markdown:



```
[https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit](https://github.com/pre-commit/pre-commit)
```

- HTML:



```
<a href="https://github.com/pre-commit/pre-commit"><img src="https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit" alt="pre-commit" style="max-width:100%;"></a>
```

- reStructuredText:



```
.. image:: https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit
     :target: https://github.com/pre-commit/pre-commit
     :alt: pre-commit
```

- AsciiDoc:



```
image:https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit[pre-commit, link=https://github.com/pre-commit/pre-commit]
```


## Usage in continuous integration

pre-commit can also be used as a tool for continuous integration. For
instance, adding `pre-commit run --all-files` as a CI step will ensure
everything stays in tip-top shape. To check only files which have changed,
which may be faster, use something like
`pre-commit run --from-ref origin/HEAD --to-ref HEAD`

## Managing CI Caches

`pre-commit` by default places its repository store in `~/.cache/pre-commit`
\-\- this can be configured in two ways:

- `PRE_COMMIT_HOME`: if set, pre-commit will use that location instead.
- `XDG_CACHE_HOME`: if set, pre-commit will use `$XDG_CACHE_HOME/pre-commit`
following the [XDG Base Directory Specification](https://specifications.freedesktop.org/basedir-spec/basedir-spec-latest.html).

### pre-commit.ci example

no additional configuration is needed to run in [pre-commit.ci](https://pre-commit.ci/)!

pre-commit.ci also has the following benefits:

- it's faster than other free CI solutions
- it will autofix pull requests
- it will periodically autoupdate your configuration

[https://raw.githubusercontent.com/pre-commit-ci-demo/demo/main/img/2020-12-15_noop.svg](https://github.com/pre-commit-ci-demo/demo#results)

### appveyor example

```
cache:
- '%USERPROFILE%\.cache\pre-commit'
```

### azure pipelines example

note: azure pipelines uses immutable caches so the python version and
`.pre-commit-config.yaml` hash must be included in the cache key. for a
repository template, see [asottile@job--pre-commit.yml](https://github.com/asottile/azure-pipeline-templates/blob/main/job--pre-commit.yml).

```
jobs:
- job: precommit

  # ...

  variables:
    PRE_COMMIT_HOME: $(Pipeline.Workspace)/pre-commit-cache

  steps:

  # ...

  - script: echo "##vso[task.setvariable variable=PY]$(python -VV)"
  - task: CacheBeta@0
    inputs:
      key: pre-commit | .pre-commit-config.yaml | "$(PY)"
      path: $(PRE_COMMIT_HOME)
```

### circleci example

like [azure pipelines](https://pre-commit.com/#azure-pipelines-example), circleci also uses immutable
caches:

```
  steps:
  - run:
    command: |
      cp .pre-commit-config.yaml pre-commit-cache-key.txt
      python --version --version >> pre-commit-cache-key.txt
  - restore_cache:
    keys:
    - v1-pc-cache-{{ checksum "pre-commit-cache-key.txt" }}

  # ...

  - save_cache:
    key: v1-pc-cache-{{ checksum "pre-commit-cache-key.txt" }}
    paths:
      - ~/.cache/pre-commit
```

(source: [@chriselion](https://github.com/Unity-Technologies/ml-agents/pull/3094/files#diff-1d37e48f9ceff6d8030570cd36286a61))

### github actions example

**see the [official pre-commit github action](https://github.com/pre-commit/action)**

like [azure pipelines](https://pre-commit.com/#azure-pipelines-example), github actions also uses
immutable caches:

```
    - name: set PY
      run: echo "PY=$(python -VV | sha256sum | cut -d' ' -f1)" >> $GITHUB_ENV
    - uses: actions/cache@v3
      with:
        path: ~/.cache/pre-commit
        key: pre-commit|${{ env.PY }}|${{ hashFiles('.pre-commit-config.yaml') }}
```

### gitlab CI example

See the [Gitlab caching best practices](https://docs.gitlab.com/ee/ci/caching/#good-caching-practices) to fine tune the cache scope.

```
my_job:
  variables:
    PRE_COMMIT_HOME: ${CI_PROJECT_DIR}/.cache/pre-commit
  cache:
    paths:
      - ${PRE_COMMIT_HOME}
```

pre-commit's cache requires to be served from a constant location between the different builds. This isn't the default when using k8s runners
on GitLab. In case you face the error `InvalidManifestError`, set `builds_dir` to something static e.g `builds_dir = "/builds"` in your `[[runner]]` config

### travis-ci example

```
cache:
  directories:
  - $HOME/.cache/pre-commit
```

## Usage with tox

[tox](https://tox.readthedocs.io/) is useful for configuring test / CI tools
such as pre-commit. One feature of `tox>=2` is it will clear environment
variables such that tests are more reproducible. Under some conditions,
pre-commit requires a few environment variables and so they must be
allowed to be passed through.

When cloning repos over ssh (`repo: git@github.com:...`), `git` requires the
`SSH_AUTH_SOCK` variable and will otherwise fail:

```
[INFO] Initializing environment for git@github.com:pre-commit/pre-commit-hooks.
An unexpected error has occurred: CalledProcessError: command: ('/usr/bin/git', 'fetch', 'origin', '--tags')
return code: 128
expected return code: 0
stdout: (none)
stderr:
    git@github.com: Permission denied (publickey).
    fatal: Could not read from remote repository.

    Please make sure you have the correct access rights
    and the repository exists.

Check the log at /home/asottile/.cache/pre-commit/pre-commit.log
```

Add the following to your tox testenv:

```
[testenv]
passenv = SSH_AUTH_SOCK
```

Likewise, when cloning repos over http / https
(`repo: https://github.com:...`), you might be working behind a corporate
http(s) proxy server, in which case `git` requires the `http_proxy`,
`https_proxy` and `no_proxy` variables to be set, or the clone may fail:

```
[testenv]
passenv = http_proxy https_proxy no_proxy
```

## Using the latest version for a repository

`pre-commit` configuration aims to give a repeatable and fast experience and
therefore intentionally doesn't provide facilities for "unpinned latest
version" for hook repositories.

Instead, `pre-commit` provides tools to make it easy to upgrade to the
latest versions with [`pre-commit autoupdate`](https://pre-commit.com/#pre-commit-autoupdate). If
you need the absolute latest version of a hook (instead of the latest tagged
version), pass the `--bleeding-edge` parameter to `autoupdate`.

`pre-commit` assumes that the value of [`rev`](https://pre-commit.com/#repos-rev) is an immutable ref (such as a
tag or SHA) and will cache based on that. Using a branch name (or `HEAD`) for
the value of [`rev`](https://pre-commit.com/#repos-rev) is not supported and will only represent the state of
that mutable ref at the time of hook installation (and will _NOT_ update
automatically).

# Contributing

We’re looking to grow the project and get more contributors especially to
support more languages/versions. We’d also like to get the
.pre-commit-hooks.yaml files added to popular linters without maintaining
forks / mirrors.

Feel free to submit bug reports, pull requests, and feature requests.

## Sponsoring

If you or your company would like to support the development of pre-commit one
can contribute in the following ways:

- [GitHub Sponsors (asottile)](https://github.com/sponsors/asottile)
- [Open Collective](https://opencollective.com/pre-commit)

## Getting help

There are several ways to get help for pre-commit:

- Ask a question on [stackoverflow tagged `pre-commit.com`](https://stackoverflow.com/questions/tagged/pre-commit.com)
- Create an issue on [pre-commit/pre-commit](https://github.com/pre-commit/pre-commit/issues/)
- Ask in the #pre-commit channel in [asottile's twitch discord](https://discord.gg/xDKGPaW)

## Contributors

- website by [Molly Finkle](https://github.com/mfnkl)
- created by [Anthony Sottile](https://github.com/asottile)
- core developers: [Ken Struys](https://github.com/struys),
[Chris Kuehl](https://github.com/chriskuehl)
- [framework contributors](https://github.com/pre-commit/pre-commit/graphs/contributors)
- [core hook contributors](https://github.com/pre-commit/pre-commit-hooks/graphs/contributors)
- and users like you!
```

</details>

<details>
<summary>Ruff Docs</summary>

# Ruff Docs

**Source URL:** <https://docs.astral.sh/ruff/>

[https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json](https://github.com/astral-sh/ruff)[https://img.shields.io/pypi/v/ruff.svg](https://pypi.python.org/pypi/ruff)[https://img.shields.io/pypi/l/ruff.svg](https://github.com/astral-sh/ruff/blob/main/LICENSE)[https://img.shields.io/pypi/pyversions/ruff.svg](https://pypi.python.org/pypi/ruff)[https://github.com/astral-sh/ruff/workflows/CI/badge.svg](https://github.com/astral-sh/ruff/actions)[https://img.shields.io/badge/Discord-%235865F2.svg?logo=discord&logoColor=white](https://discord.com/invite/astral-sh)

[**Docs**](https://docs.astral.sh/ruff/) | [**Playground**](https://play.ruff.rs/)

An extremely fast Python linter and code formatter, written in Rust.

https://user-images.githubusercontent.com/1309177/232603516-4fb4892d-585c-4b20-b810-3db9161831e4.svg#only-light

https://user-images.githubusercontent.com/1309177/232603514-c95e9b0f-6b31-43de-9a80-9e844173fd6a.svg#only-dark

_Linting the CPython codebase from scratch._

- ⚡️ 10-100x faster than existing linters (like Flake8) and formatters (like Black)
- 🐍 Installable via `pip`
- 🛠️ `pyproject.toml` support
- 🤝 Python 3.14 compatibility
- ⚖️ Drop-in parity with [Flake8](https://docs.astral.sh/ruff/faq/#how-does-ruffs-linter-compare-to-flake8), isort, and [Black](https://docs.astral.sh/ruff/faq/#how-does-ruffs-formatter-compare-to-black)
- 📦 Built-in caching, to avoid re-analyzing unchanged files
- 🔧 Fix support, for automatic error correction (e.g., automatically remove unused imports)
- 📏 Over [900 built-in rules](https://docs.astral.sh/ruff/rules/), with native re-implementations
of popular Flake8 plugins, like flake8-bugbear
- ⌨️ First-party [editor integrations](https://docs.astral.sh/ruff/editors/) for [VS Code](https://github.com/astral-sh/ruff-vscode) and [more](https://docs.astral.sh/ruff/editors/setup/)
- 🌎 Monorepo-friendly, with [hierarchical and cascading configuration](https://docs.astral.sh/ruff/configuration/#config-file-discovery)

Ruff aims to be orders of magnitude faster than alternative tools while integrating more
functionality behind a single, common interface.

Ruff can be used to replace [Flake8](https://pypi.org/project/flake8/) (plus dozens of plugins),
[Black](https://github.com/psf/black), [isort](https://pypi.org/project/isort/),
[pydocstyle](https://pypi.org/project/pydocstyle/), [pyupgrade](https://pypi.org/project/pyupgrade/),
[autoflake](https://pypi.org/project/autoflake/), and more, all while executing tens or hundreds of
times faster than any individual tool.

Ruff is extremely actively developed and used in major open-source projects like:

- [Apache Airflow](https://github.com/apache/airflow)
- [Apache Superset](https://github.com/apache/superset)
- [FastAPI](https://github.com/tiangolo/fastapi)
- [Hugging Face](https://github.com/huggingface/transformers)
- [Pandas](https://github.com/pandas-dev/pandas)
- [SciPy](https://github.com/scipy/scipy)

...and [many more](https://github.com/astral-sh/ruff#whos-using-ruff).

Ruff is backed by [Astral](https://astral.sh/), the creators of
[uv](https://github.com/astral-sh/uv) and [ty](https://github.com/astral-sh/ty).

Read the [launch\
post](https://astral.sh/blog/announcing-astral-the-company-behind-ruff), or the
original [project\
announcement](https://notes.crmarsh.com/python-tooling-could-be-much-much-faster).

## [Testimonials](https://docs.astral.sh/ruff/#testimonials)

[**Sebastián Ramírez**](https://twitter.com/tiangolo/status/1591912354882764802), creator
of [FastAPI](https://github.com/tiangolo/fastapi):

> Ruff is so fast that sometimes I add an intentional bug in the code just to confirm it's actually
> running and checking the code.

[**Nick Schrock**](https://twitter.com/schrockn/status/1612615862904827904), founder of [Elementl](https://www.elementl.com/),
co-creator of [GraphQL](https://graphql.org/):

> Why is Ruff a gamechanger? Primarily because it is nearly 1000x faster. Literally. Not a typo. On
> our largest module (dagster itself, 250k LOC) pylint takes about 2.5 minutes, parallelized across 4
> cores on my M1. Running ruff against our _entire_ codebase takes .4 seconds.

[**Bryan Van de Ven**](https://github.com/bokeh/bokeh/pull/12605), co-creator
of [Bokeh](https://github.com/bokeh/bokeh/), original author
of [Conda](https://docs.conda.io/en/latest/):

> Ruff is ~150-200x faster than flake8 on my machine, scanning the whole repo takes ~0.2s instead of
> ~20s. This is an enormous quality of life improvement for local dev. It's fast enough that I added
> it as an actual commit hook, which is terrific.

[**Timothy Crosley**](https://twitter.com/timothycrosley/status/1606420868514877440),
creator of [isort](https://github.com/PyCQA/isort):

> Just switched my first project to Ruff. Only one downside so far: it's so fast I couldn't believe
> it was working till I intentionally introduced some errors.

[**Tim Abbott**](https://github.com/zulip/zulip/pull/23431#issuecomment-1302557034), lead developer of [Zulip](https://github.com/zulip/zulip) (also [here](https://github.com/astral-sh/ruff/issues/465#issuecomment-1317400028)):

> This is just ridiculously fast... `ruff` is amazing.

</details>

<details>
<summary>Ruff Linter</summary>

# Ruff Linter

**Source URL:** <https://docs.astral.sh/ruff/linter/>

The Ruff Linter is an extremely fast Python linter designed as a drop-in replacement for [Flake8](https://pypi.org/project/flake8/)
(plus dozens of plugins), [isort](https://pypi.org/project/isort/), [pydocstyle](https://pypi.org/project/pydocstyle/),
[pyupgrade](https://pypi.org/project/pyupgrade/), [autoflake](https://pypi.org/project/autoflake/),
and more.

## [`ruff check`](https://docs.astral.sh/ruff/linter/#ruff-check)

`ruff check` is the primary entrypoint to the Ruff linter. It accepts a list of files or
directories, and lints all discovered Python files, optionally fixing any fixable errors.
When linting a directory, Ruff searches for Python files recursively in that directory
and all its subdirectories:

```
$ ruff check                  # Lint files in the current directory.
$ ruff check --fix            # Lint files in the current directory and fix any fixable errors.
$ ruff check --watch          # Lint files in the current directory and re-lint on change.
$ ruff check path/to/code/    # Lint files in `path/to/code`.
```

For the full list of supported options, run `ruff check --help`.

## [Rule selection](https://docs.astral.sh/ruff/linter/#rule-selection)

The set of enabled rules is controlled via the [`lint.select`](https://docs.astral.sh/ruff/settings/#lint_select),
[`lint.extend-select`](https://docs.astral.sh/ruff/settings/#lint_extend-select), and [`lint.ignore`](https://docs.astral.sh/ruff/settings/#lint_ignore) settings.

Ruff's linter mirrors Flake8's rule code system, in which each rule code consists of a one-to-three
letter prefix, followed by three digits (e.e.g., `F401`). The prefix indicates that "source" of the rule
(e.g., `F` for Pyflakes, `E` for pycodestyle, `ANN` for flake8-annotations).

Rule selectors like [`lint.select`](https://docs.astral.sh/ruff/settings/#lint_select) and [`lint.ignore`](https://docs.astral.sh/ruff/settings/#lint_ignore) accept either
a full rule code (e.g., `F401`) or any valid prefix (e.g., `F`). For example, given the following
configuration file:

[pyproject.toml](https://docs.astral.sh/ruff/linter/#__tabbed_1_1)[ruff.toml](https://docs.astral.sh/ruff/linter/#__tabbed_1_2)

```
[tool.ruff.lint]
select = ["E", "F"]
ignore = ["F401"]
```

```
[lint]
select = ["E", "F"]
ignore = ["F401"]
```

Ruff would enable all rules with the `E` (pycodestyle) or `F` (Pyflakes) prefix, with the exception
of `F401`. For more on configuring Ruff via `pyproject.toml`, see [_Configuring Ruff_](https://docs.astral.sh/ruff/configuration/).

As a special-case, Ruff also supports the `ALL` code, which enables all rules. Note that some
pydocstyle rules conflict (e.g., `D203` and `D211`) as they represent alternative docstring
formats. Ruff will automatically disable any conflicting rules when `ALL` is enabled.

If you're wondering how to configure Ruff, here are some **recommended guidelines**:

- Prefer [`lint.select`](https://docs.astral.sh/ruff/settings/#lint_select) over [`lint.extend-select`](https://docs.astral.sh/ruff/settings/#lint_extend-select) to make your rule set explicit.
- Use `ALL` with discretion. Enabling `ALL` will implicitly enable new rules whenever you upgrade.
- Start with a small set of rules (`select = ["E", "F"]`) and add a category at-a-time. For example,
you might consider expanding to `select = ["E", "F", "B"]` to enable the popular flake8-bugbear
extension.

For example, a configuration that enables some of the most popular rules (without being too
pedantic) might look like the following:

[pyproject.toml](https://docs.astral.sh/ruff/linter/#__tabbed_2_1)[ruff.toml](https://docs.astral.sh/ruff/linter/#__tabbed_2_2)

```
[tool.ruff.lint]
select = [\
    # pycodestyle\
    "E",\
    # Pyflakes\
    "F",\
    # pyupgrade\
    "UP",\
    # flake8-bugbear\
    "B",\
    # flake8-simplify\
    "SIM",\
    # isort\
    "I",\
]
```

```
[lint]
select = [\
    # pycodestyle\
    "E",\
    # Pyflakes\
    "F",\
    # pyupgrade\
    "UP",\
    # flake8-bugbear\
    "B",\
    # flake8-simplify\
    "SIM",\
    # isort\
    "I",\
]
```

To resolve the enabled rule set, Ruff may need to reconcile [`lint.select`](https://docs.astral.sh/ruff/settings/#lint_select) and
[`lint.ignore`](https://docs.astral.sh/ruff/settings/#lint_ignore) from a variety of sources, including the current `pyproject.toml`,
any inherited `pyproject.toml` files, and the CLI (e.g., [`--select`](https://docs.astral.sh/ruff/settings/#lint_select)).

In those scenarios, Ruff uses the "highest-priority" [`select`](https://docs.astral.sh/ruff/settings/#lint_select) as the basis for
the rule set, and then applies [`extend-select`](https://docs.astral.sh/ruff/settings/#lint_extend-select) and
[`ignore`](https://docs.astral.sh/ruff/settings/#lint_ignore) adjustments. CLI options are given higher priority than
`pyproject.toml` options, and the current `pyproject.toml` file is given higher priority than any
inherited `pyproject.toml` files.

For example, given the following configuration file:

[pyproject.toml](https://docs.astral.sh/ruff/linter/#__tabbed_3_1)[ruff.toml](https://docs.astral.sh/ruff/linter/#__tabbed_3_2)

```
[tool.ruff.lint]
select = ["E", "F"]
ignore = ["F401"]
```

```
[lint]
select = ["E", "F"]
ignore = ["F401"]
```

Running `ruff check --select F401` would result in Ruff enforcing `F401`, and no other rules.

Running `ruff check --extend-select B` would result in Ruff enforcing the `E`, `F`, and `B` rules,
with the exception of `F401`.

## [Fixes](https://docs.astral.sh/ruff/linter/#fixes)

Ruff supports automatic fixes for a variety of lint errors. For example, Ruff can remove unused
imports, reformat docstrings, rewrite type annotations to use newer Python syntax, and more.

To enable fixes, pass the `--fix` flag to `ruff check`:

```
$ ruff check --fix
```

By default, Ruff will fix all violations for which safe fixes are available; to determine
whether a rule supports fixing, see [_Rules_](https://docs.astral.sh/ruff/rules/).

### [Fix safety](https://docs.astral.sh/ruff/linter/#fix-safety)

Ruff labels fixes as "safe" and "unsafe". The meaning and intent of your code will be retained when
applying safe fixes, but the meaning could change when applying unsafe fixes.

Specifically, an unsafe fix could lead to a change in runtime behavior, the removal of comments, or both,
while safe fixes are intended to preserve runtime behavior and will only remove comments when deleting
entire statements or expressions (e.g., removing unused imports).

For example, [`unnecessary-iterable-allocation-for-first-element`](https://docs.astral.sh/ruff/rules/unnecessary-iterable-allocation-for-first-element/)
(`RUF015`) is a rule which checks for potentially unperformant use of `list(...)[0]`. The fix
replaces this pattern with `next(iter(...))` which can result in a drastic speedup:

```
$ python -m timeit "head = list(range(99999999))[0]"
1 loop, best of 5: 1.69 sec per loop
```

```
$ python -m timeit "head = next(iter(range(99999999)))"
5000000 loops, best of 5: 70.8 nsec per loop
```

However, when the collection is empty, this raised exception changes from an `IndexError` to `StopIteration`:

```
$ python -c 'list(range(0))[0]'
Traceback (most recent call last):
  File "<string>", line 1, in <module>
IndexError: list index out of range
```

```
$ python -c 'next(iter(range(0)))'
Traceback (most recent call last):
  File "<string>", line 1, in <module>
StopIteration
```

Since the change in exception type could break error handling upstream, this fix is categorized as unsafe.

Ruff only enables safe fixes by default. Unsafe fixes can be enabled by settings [`unsafe-fixes`](https://docs.astral.sh/ruff/settings/#unsafe-fixes) in your configuration file or passing the `--unsafe-fixes` flag to `ruff check`:

```
# Show unsafe fixes
ruff check --unsafe-fixes

# Apply unsafe fixes
ruff check --fix --unsafe-fixes
```

By default, Ruff will display a hint when unsafe fixes are available but not enabled. The suggestion can be silenced
by setting the [`unsafe-fixes`](https://docs.astral.sh/ruff/settings/#unsafe-fixes) setting to `false` or using the `--no-unsafe-fixes` flag.

The safety of fixes can be adjusted per rule using the [`lint.extend-safe-fixes`](https://docs.astral.sh/ruff/settings/#lint_extend-safe-fixes) and [`lint.extend-unsafe-fixes`](https://docs.astral.sh/ruff/settings/#lint_extend-unsafe-fixes) settings.

For example, the following configuration would promote unsafe fixes for `F601` to safe fixes and demote safe fixes for `UP034` to unsafe fixes:

[pyproject.toml](https://docs.astral.sh/ruff/linter/#__tabbed_4_1)[ruff.toml](https://docs.astral.sh/ruff/linter/#__tabbed_4_2)

```
[tool.ruff.lint]
extend-safe-fixes = ["F601"]
extend-unsafe-fixes = ["UP034"]
```

```
[lint]
extend-safe-fixes = ["F601"]
extend-unsafe-fixes = ["UP034"]
```

You may use prefixes to select rules as well, e.g., `F` can be used to promote fixes for all rules in Pyflakes to safe.

Note

All fixes will always be displayed by Ruff when using the `json` output format. The safety of each fix is available under the `applicability` field.

### [Disabling fixes](https://docs.astral.sh/ruff/linter/#disabling-fixes)

To limit the set of rules that Ruff should fix, use the [`lint.fixable`](https://docs.astral.sh/ruff/settings/#lint_fixable)
or [`lint.extend-fixable`](https://docs.astral.sh/ruff/settings/#lint_extend-fixable), and [`lint.unfixable`](https://docs.astral.sh/ruff/settings/#lint_unfixable) settings.

For example, the following configuration would enable fixes for all rules except
[`unused-imports`](https://docs.astral.sh/ruff/rules/unused-import/) (`F401`):

[pyproject.toml](https://docs.astral.sh/ruff/linter/#__tabbed_5_1)[ruff.toml](https://docs.astral.sh/ruff/linter/#__tabbed_5_2)

```
[tool.ruff.lint]
fixable = ["ALL"]
unfixable = ["F401"]
```

```
[lint]
fixable = ["ALL"]
unfixable = ["F401"]
```

Conversely, the following configuration would only enable fixes for `F401`:

[pyproject.toml](https://docs.astral.sh/ruff/linter/#__tabbed_6_1)[ruff.toml](https://docs.astral.sh/ruff/linter/#__tabbed_6_2)

```
[tool.ruff.lint]
fixable = ["F401"]
```

```
[lint]
fixable = ["F401"]
```

## [Error suppression](https://docs.astral.sh/ruff/linter/#error-suppression)

Ruff supports several mechanisms for suppressing lint errors, be they false positives or
permissible violations.

### [Configuration](https://docs.astral.sh/ruff/linter/#configuration)

To omit a lint rule everywhere, add it to the "ignore" list via the [`lint.ignore`](https://docs.astral.sh/ruff/settings/#lint_ignore)
setting, either on the command-line or in your `pyproject.toml` or `ruff.toml` file.

To omit a lint rule within specific files based on file path prefixes or patterns,
see the [`lint.per-file-ignores`](https://docs.astral.sh/ruff/settings/#lint_per-file-ignores) setting.

### [Comments](https://docs.astral.sh/ruff/linter/#comments)

Ruff supports multiple forms of suppression comments, including inline and file-level `noqa`
comments, and range suppressions.

#### [Line-level](https://docs.astral.sh/ruff/linter/#line-level)

Ruff supports a `noqa` system similar to [Flake8](https://flake8.pycqa.org/en/3.1.1/user/ignoring-errors.html).
To ignore an individual violation, add `# noqa: {code}` to the end of the line, like so:

```
# Ignore F841.
x = 1  # noqa: F841

# Ignore E741 and F841.
i = 1  # noqa: E741, F841

# Ignore _all_ violations.
x = 1  # noqa
```

For multi-line strings (like docstrings), the `noqa` directive should come at the end of the string
(after the closing triple quote), and will apply to the entire string, like so:

```
"""Lorem ipsum dolor sit amet.

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor.
"""  # noqa: E501
```

For import sorting, the `noqa` should come at the end of the first line in the import block, and
will apply to all imports in the block, like so:

```
import os  # noqa: I001
import abc
```

The full inline comment specification is as follows:

- An inline blanket `noqa` comment is given by a case-insensitive match for
`#noqa` with optional whitespace after the `#` symbol, followed by either: the
end of the comment, the beginning of a new comment (`#`), or whitespace
followed by any character other than `:`.
- An inline `noqa` suppression is given by first finding a case-insensitive match
for `#noqa` with optional whitespace after the `#` symbol, optional whitespace
after `noqa`, and followed by the symbol `:`. After this we are expected to
have a list of rule codes which is given by sequences of uppercase ASCII
characters followed by ASCII digits, separated by whitespace or commas. The
list ends at the last valid code. We will attempt to interpret rules with a
missing delimiter (e.g. `F401F841`), though a warning will be emitted in this
case.

_The following is currently only available in [preview mode](https://docs.astral.sh/ruff/linter/preview.md)._

To cover an entire "logical" line (a multi-line statement or suite header),
an "ignore" comment may be placed above the first line:

```
# ruff: ignore[unused-function-argument]  # Covers the entire function signature
def foo(
    arg1,
    arg2,
):
    pass

# ruff: ignore[line-too-long]  # Covers the entire list literal
things = [\
    "really long string literal ...",\
    "really long string literal ...",\
]
```

Alternately, placing the "ignore" comment inside of a multi-line statement, or
at the end of a line, will cover only a single "physical" line, leaving the rest
of the multi-line statement or header uncovered:

```
def foo(
    arg1,
    # ruff: ignore[unused-function-argument]  # Only covers `arg2`
    arg2,
):
    pass

things = [\
    "really long string literal ...",  # ruff: ignore[line-too-long]  # Only covers this line\
    "really long string literal ...",\
]
```

Ignore comments can also be "stacked" with other comments or pragmas, and will
still cover the next logical line:

```
# ruff: ignore[ambiguous-variable-name]
# ruff: ignore[unused-variable]
# I definitely know what I'm doing.
i = 1
```

The full line-level suppression comment specification is as follows:

- An own-line or trailing comment starting with case sensitive `#ruff:`, with
optional whitespace after the `#` symbol and `:` symbol, followed by `ignore[`,\
any rules to be suppressed, and ending with `]`.
- Rules to be suppressed must be separated by commas, with optional whitespace
before or after each rule name, and may be followed by an optional trailing comma
after the last rule name.

#### [Block-level](https://docs.astral.sh/ruff/linter/#block-level)

To ignore one or more violations within a range or block of code, a "disable" comment
followed by a matching "enable" comment can be used, like so:

```
# ruff: disable[E501]
VALUE_1 = "Lorem ipsum dolor sit amet ..."
VALUE_2 = "Lorem ipsum dolor sit amet ..."
VALUE_3 = "Lorem ipsum dolor sit amet ..."
# ruff: enable[E501]
```

To define a range, both the "disable" and "enable" comments must have matching codes,
in the same order, as well as matching indentation levels within a logical block of code:

```
def foo():
    # ruff: disable[E741, F841]
    i = 1
    # ruff: enable[E741, F841]
```

If no matching "enable" comment is found, Ruff will also treat this as an "implicit" range.
The implicit range is defined from the starting "disable" comment, until reaching
a logical scope indented less than the starting comment:

```
def foo():
    # ruff: disable[E741, F841]
    i = 1
    if True:
        O = 1
    l = 1

# implicit end of range
foo()
```

It is strongly suggested to use explicit range suppressions, in order to prevent
accidental suppressions of violations, especially at global module scope.
For this reason, a `RUF104` diagnostic will also be produced for any implicit range.
If implicit range suppressions are desired, the `RUF104` rule can be disabled,
or an inline `noqa` suppression can be added to the end of the "disable" comment.

Range suppressions cannot be used to enable or select rules that aren't already
selected by the project configuration or runtime flags. An "enable" comment can only
be used to terminate a preceding "disable" comment with identical codes.

Unlike `noqa` suppressions, range suppressions do not support "blanket" suppression
of all violations. At least one violation code must be listed.

In [`preview`](https://docs.astral.sh/ruff/preview/) mode, rule names (e.g. `unused-import`) can be used in these comments
instead of rule codes (e.g. `F401`).

The full range suppression comment specification is as follows:

- An own-line comment starting with case sensitive `#ruff:`, with optional whitespace
after the `#` symbol and `:` symbol, followed by either `disable` or `enable`
to start or end a range respectively, immediately followed by `[`, any codes to\
be suppressed, and ending with `]`.
- Codes to be suppressed must be separated by commas, with optional whitespace
before or after each code, and may be followed by an optional trailing comma
after the last code.

#### [File-level](https://docs.astral.sh/ruff/linter/#file-level)

To ignore all violations across an entire file, add the line `# ruff: noqa` anywhere in the file,
preferably towards the top, like so:

```
# ruff: noqa
```

To ignore a specific rule across an entire file, add the line `# ruff: noqa: {code}` anywhere in the
file, preferably towards the top, like so:

```
# ruff: noqa: F841
```

Global `noqa` comments must be on their own line to disambiguate from comments which ignore
violations on a single line.

Note that Ruff will also respect Flake8's `# flake8: noqa` directive, and will treat it as
equivalent to `# ruff: noqa`.

The file-level suppression comment specification is as follows:

- A file-level exemption comment is given by a case-sensitive match for `#ruff:`
or `#flake8:`, with optional whitespace after `#` and before `:`, followed by
optional whitespace and a case-insensitive match for `noqa`. After this, the
specification is as in the inline `noqa` suppressions above.

In [`preview`](https://docs.astral.sh/ruff/preview/) mode, one or more rules can be ignored across an
entire file with a `file-ignore` comment on its own line, at global module scope,
and preferably near the top of the file:

```
# ruff: file-ignore[unused-import, unused-function-argument]
```

The full-level suppression comment specification is as follows:

- An own-line comment starting with case sensitive `#ruff:`, with optional whitespace
after the `#` symbol and `:` symbol, followed by `file-ignore[`, any rules to\
be suppressed, and ending with `]`.
- Rules to be suppressed must be separated by commas, with optional whitespace
before or after each rule name, and may be followed by an optional trailing comma
after the last rule name.

### [Detecting unused suppressions](https://docs.astral.sh/ruff/linter/#detecting-unused-suppressions)

Ruff implements a special rule, [`unused-noqa`](https://docs.astral.sh/ruff/rules/unused-noqa/),
under the `RUF100` code, to enforce that your suppressions are "valid", in that the violations
they _say_ they ignore are actually being triggered and suppressed. To flag
unused suppression comments, run Ruff with `--extend-select RUF100`, like so:

```
$ ruff check /path/to/file.py --extend-select RUF100
```

Ruff can also _remove_ any unused suppression comments via its fix functionality.
To remove any unused suppressions, run Ruff with `--fix`, like so:

```
$ ruff check /path/to/file.py --extend-select RUF100 --fix
```

### [Inserting necessary suppression comments](https://docs.astral.sh/ruff/linter/#inserting-necessary-suppression-comments)

Ruff can _automatically add_`noqa` directives to all lines that contain violations, which is
useful when migrating a new codebase to Ruff. To automatically add `noqa` directives to all
relevant lines (with the appropriate rule codes), run Ruff with `--add-noqa`, like so:

```
$ ruff check /path/to/file.py --add-noqa
```

### [isort action comments](https://docs.astral.sh/ruff/linter/#isort-action-comments)

Ruff respects isort's [action comments](https://pycqa.github.io/isort/docs/configuration/action_comments.html)
(`# isort: skip_file`, `# isort: on`, `# isort: off`, `# isort: skip`, and `# isort: split`), which
enable selectively enabling and disabling import sorting for blocks of code and other inline
configuration.

Ruff will also respect variants of these action comments with a `# ruff:` prefix
(e.g., `# ruff: isort: skip_file`, `# ruff: isort: on`, and so on). These variants more clearly
convey that the action comment is intended for Ruff, but are functionally equivalent to the
isort variants.

Unlike isort, Ruff does not respect action comments within docstrings.

See the [isort documentation](https://pycqa.github.io/isort/docs/configuration/action_comments.html)
for more.

## [Exit codes](https://docs.astral.sh/ruff/linter/#exit-codes)

By default, `ruff check` exits with the following status codes:

- `0` if no violations were found, or if all present violations were fixed automatically.
- `1` if violations were found.
- `2` if Ruff terminates abnormally due to invalid configuration, invalid CLI options, or an
internal error.

This convention mirrors that of tools like ESLint, Prettier, and RuboCop.

`ruff check` supports two command-line flags that alter its exit code behavior:

- `--exit-zero` will cause Ruff to exit with a status code of `0` even if violations were found.
Note that Ruff will still exit with a status code of `2` if it terminates abnormally.
- `--exit-non-zero-on-fix` will cause Ruff to exit with a status code of `1` if violations were
found, _even if_ all such violations were fixed automatically. Note that the use of
`--exit-non-zero-on-fix` can result in a non-zero exit code even if no violations remain after
fixing.

</details>

<details>
<summary>Testing</summary>

# Testing

**Source URL:** <https://docs.langchain.com/oss/python/langchain/test>

Agentic applications let an LLM decide its own next steps to solve a problem. That flexibility is powerful, but the model’s black-box nature makes it hard to predict how a tweak in one part of your agent will affect the whole. To build production-ready agents, thorough testing is essential.There are a few approaches to testing your agents:

- **Unit tests** exercise small, deterministic pieces of your agent in isolation using in-memory fakes so you can assert exact behavior quickly and deterministically.
- **Integration tests** test the agent using real network calls to confirm that components work together, credentials and schemas line up, and latency is acceptable.
- **Evals** use evaluators to assess your agent’s execution trajectory, either via deterministic matching or an LLM judge.

Agentic applications tend to lean more on integration because they chain multiple components together and must deal with flakiness due to the nondeterministic nature of LLMs.

</details>

</golden_source>

<research_source type="guideline_exploitation" phase="exploitation" file="a-practical-guide-to-integrating-ai-evals-into-your-ci-cd-pi.md">
<details>
<summary>A practical guide to integrating AI evals into your CI/CD pipeline</summary>

Phase: [EXPLOITATION]

# A practical guide to integrating AI evals into your CI/CD pipeline

**Source URL:** <https://dev.to/kuldeep_paul/a-practical-guide-to-integrating-ai-evals-into-your-cicd-pipeline-3mlb>

Engineering teams shipping AI agents and LLM applications need the same confidence they expect from mature software delivery: repeatable tests, clear quality gates, and rapid iteration with guardrails. Automating AI evaluation—“AI evals”—inside CI/CD is how you catch regressions early, prevent silent failures in production, and scale responsible development across teams. This guide distills best practices and an actionable blueprint for CI/CD-integrated evals, grounded in current research and production patterns, and shows how to operationalize them with Maxim AI’s full-stack platform for simulation, evaluation, and observability.

## Why Evals Belong in CI/CD

Traditional unit and integration tests don’t capture AI quality dimensions such as factuality, faithfulness, instruction following, or multi-turn task completion. You need evaluators that score outputs and behaviors with quantitative thresholds and pass/fail gates. Academic work has highlighted that open-ended evaluation requires care—LLM-as-a-judge methods can align well with human preferences when designed thoughtfully, but reliability depends on rubric quality, sampling, and consistency strategies ( [Reliability of LLM-as-a-Judge](https://arxiv.org/abs/2412.12509), [Design Choices Impact Evaluation Reliability](https://arxiv.org/abs/2506.13639)). In parallel, standard MLOps guidance emphasizes CI/CD for ML to automate training, evaluation, and deployment with versioning and reproducibility ( [CI/CD for Machine Learning](https://www.datacamp.com/tutorial/ci-cd-for-machine-learning), [MLOps Guide: CI/CD](https://mlops-guide.github.io/MLOps/CICDML/)). Bringing these together enables “AI quality gates” that block releases on meaningful regressions across your core metrics.

## What “AI Evals in CI/CD” Looks Like

At its core, CI/CD-integrated evals run a representative test suite on every relevant change—prompt edits, model swaps, tool configurations, or agent logic. The pipeline:

- Builds datasets reflecting key scenarios (offline corpora, synthetic simulations, and samples curated from production logs).
- Executes workflows end-to-end, including retrieval (RAG), tool calling, and multi-turn conversations.
- Scores outputs with a mix of deterministic checks (JSON validity, PII detection), statistical metrics (similarity), and model-based evaluators (LLM-as-a-judge).
- Applies thresholds and fail-the-build rules, surfaces diffs on pull requests, and preserves lineage for analysis.

When practiced consistently, teams gain fast feedback loops, reduce rollout risk, and accelerate responsible iteration—all while maintaining observability and governance.

## A Blueprint: Metrics, Rubrics, and Quality Gates

Design evaluators around your application architecture and user outcomes. Common, high-signal dimensions include:

- Factuality and groundedness for RAG: Does the answer cite provided context and avoid hallucination? Pair deterministic checks (citation presence) with LLM-as-a-judge rubrics scoring faithfulness and relevance. See rubric reliability considerations in [LLM-as-a-Judge research](https://arxiv.org/abs/2412.12509).
- Instruction following and policy adherence: Enforce structured output (JSON schema validity) and rubric-based compliance to domain and safety guidelines.
- Task completion for agents: Verify multi-step goal achievement, correct tool selection, error recovery, and escalation logic.
- Tone, safety, and bias: Score for toxicity, bias, and sensitive content handling with a blend of automatic and human-in-the-loop reviews.
- Latency and cost: Treat performance as a first-class metric; quality must be measured alongside real-time efficiency to manage SLAs and budgets.

Use scoring bands to stabilize decisions. For LLM-as-a-judge, prefer explicit rubrics, reference answers or contexts, and sample multiple judge votes when reliability matters ( [Empirical Study of LLM-as-a-Judge](https://arxiv.org/abs/2506.13639)). For CI gates, define per-metric thresholds and aggregate pass rules (e.g., minimum average score plus per-case floors on critical scenarios).

## Operationalizing with Maxim AI: From Experiment to Observe

Maxim AI provides an end-to-end stack for agentic applications—covering experimentation, simulation and evals, observability, and data operations—so engineering and product can collaborate without glue code.

- Experimentation and prompt management: Side-by-side comparisons across prompts, models, and parameters in a workflow IDE, with structured output validation and versioning. Explore the capabilities on the [Experimentation](https://www.getmaxim.ai/products/experimentation) page.
- Simulation and multi-turn evaluation: Test agents across hundreds of personas and real-world scenarios, evaluate trajectory choices, and reproduce issues from any step. Learn more on [Agent Simulation & Evaluation](https://www.getmaxim.ai/products/agent-simulation-evaluation).
- Unified evaluation framework: Combine programmatic checks, statistical metrics, and LLM-as-a-judge rubrics. Mix automated pipelines with human review queues for high-stakes assessments. Details are covered in [Agent Simulation and Evaluation](https://www.getmaxim.ai/products/agent-simulation-evaluation).
- Observability and online evals: Capture production logs, distributed tracing, and run periodic quality checks on sampled traffic; alert on deviations in quality, cost, and latency. See [Agent Observability](https://www.getmaxim.ai/products/agent-observability).
- Data engine: Curate and evolve datasets from production logs for future evals and fine-tuning, including multimodal assets and human feedback workflows. Learn about the core data management capabilities on the product pages above.

## Reference Implementation: CI/CD Quality Gates with Maxim

Below is a concrete process that teams can drop into GitHub Actions, CircleCI, or Jenkins. It blends offline evals, agent simulations, and production-aware checks, aligned to the development cadence.

### Step 1: Define Your Test Suite

- Collect representative cases for each core scenario (customer intents, document types, voice utterances) and label expected behaviors (answers, tool use, escalation criteria).
- Create subsets for fast PR gates (smoke tests) and full suites for nightly runs.
- Source “hard cases” from production logs via observability, then promote them into datasets for regression prevention. Maxim’s data curation workflows are designed for this continuous loop; see [Agent Observability](https://www.getmaxim.ai/products/agent-observability) and tracing docs linked on the product page.

### Step 2: Author Evaluators and Rubrics

- Deterministic: JSON schema validity, PII redaction rules, citation presence, latency ceilings, and cost budgets.
- RAG tracing and faithfulness: Link retrieval spans to answer content and score groundedness with rubric-based evaluators.
- Agent debugging: Score tool correctness, recovery steps, and policy adherence across multi-turn traces.
- Safety, bias, tone: Use prebuilt evaluators for toxicity and bias, and supplement with human-in-the-loop for nuanced brand tone.

For rubric-based scoring, incorporate current reliability guidance—explicit criteria, multiple samples when needed, and calibration with human labels ( [Reliability of LLM-as-a-Judge](https://arxiv.org/abs/2412.12509), [Design Choices Impact Reliability](https://arxiv.org/abs/2506.13639)).

### Step 3: Wire Evals into CI

Use quality gates that fail builds when metrics drop below thresholds or when critical violations occur. A simplified GitHub Actions workflow might look like:

```
name: ai-evals
on:
  pull_request:
    paths:
      - "prompts/**"
      - "agent/**"
      - "retrieval/**"
      - ".github/workflows/ai-evals.yml"
  workflow_dispatch:

jobs:
  run-evals:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.11"

      - name: Install deps
        run: |
          pip install -r requirements.txt

      - name: Configure Bifrost gateway
        env:
          BIFROST_API_KEY: ${{ secrets.BIFROST_API_KEY }}
        run: |
          echo "Configured Bifrost API key for multi-provider evals."

      - name: Run offline evals (smoke)
        run: |
          python scripts/run_evals.py --suite smoke --fail-on-threshold

      - name: Post PR summary
        run: |
          python scripts/post_pr_summary.py --suite smoke
```

- Multi-provider reliability: Point SDK clients to Maxim’s **Bifrost** gateway for seamless provider switching, semantic caching, and automatic fallbacks. See the **Unified Interface** and **Automatic Fallbacks** docs: [Unified Interface](https://docs.getbifrost.ai/features/unified-interface), [Automatic Fallbacks](https://docs.getbifrost.ai/features/fallbacks).
- Budget and governance: Enforce per-team cost limits and rate controls during CI via Bifrost governance features: [Governance and Budget Management](https://docs.getbifrost.ai/features/governance).
- Caching for speed: Enable semantic caching to accelerate large eval runs while preserving correctness gates: [Semantic Caching](https://docs.getbifrost.ai/features/semantic-caching).

### Step 4: Simulate Agents Pre-Release

Before merging major changes, run scenario-based simulations to validate multi-turn behavior, tool usage, and failure recovery. Use persona diversity and environment perturbations (missing data, API delays). See [Agent Simulation & Evaluation](https://www.getmaxim.ai/products/agent-simulation-evaluation) for simulation design patterns.

### Step 5: Observe in Production and Run Online Evals

- Ingest production logs with distributed tracing to debug real interactions and build datasets from live traffic. See [Agent Observability](https://www.getmaxim.ai/products/agent-observability).
- Schedule periodic online evals on sampled traffic (e.g., 1–5%) with alerts on drift in quality, cost, or latency. Integrate Slack/PagerDuty notifications for rapid response.
- Use OpenTelemetry-compatible spans to unify visibility across code and LLM calls; forward metrics to your standard monitoring stack.

### Step 6: Close the Loop with Data Curation and Human Review

Continuously curate eval datasets from production failures and edge cases, enrich them with human feedback where needed, and re-run targeted evaluations. This “observe → curate → evaluate → ship” loop ensures your test suite stays representative of real usage over time. Maxim’s workflows support human + LLM-in-the-loop evals and dataset versioning across modalities; explore the product pages linked above for details.

## Reliability, Reproducibility, and Collaboration

Evals must be stable and repeatable across runs, branches, and environments:

- Version everything: prompts, evaluators, datasets, and model/provider configurations. Keep lineage and changelogs.
- Control randomness: For LLM-as-a-judge, prefer explicit rubrics, reference-based checks, and aggregate scores over single-shot evaluations when reliability is critical ( [Reliability of LLM-as-a-Judge](https://arxiv.org/abs/2412.12509)).
- Separate smoke vs. comprehensive: Fast PR gates prevent noisy failures; nightly runs catch subtle regressions.
- Make results legible to non-engineers: Summaries should surface pass/fail thresholds, top regressions, and qualitative notes. Maxim’s UI and dashboards are designed to align engineering and product workflows; see [Agent Simulation & Evaluation](https://www.getmaxim.ai/products/agent-simulation-evaluation) and [Agent Observability](https://www.getmaxim.ai/products/agent-observability).

## Governance, Security, and Cost Controls with Bifrost

As evals scale, you’ll run thousands of calls across multiple providers. Maxim’s Bifrost gateway centralizes control:

- Single OpenAI-compatible API across 12+ providers with **automatic failover** and **load balancing**: [Unified Interface](https://docs.getbifrost.ai/features/unified-interface), [Automatic Fallbacks](https://docs.getbifrost.ai/features/fallbacks).
- **Semantic caching** to cut cost and latency for repeat eval cases: [Semantic Caching](https://docs.getbifrost.ai/features/semantic-caching).
- **Governance and budget management** with virtual keys, rate limits, and per-team controls: [Governance and Budget Management](https://docs.getbifrost.ai/features/governance).
- **Observability** with native metrics and distributed tracing for auditability of eval runs: [Observability](https://docs.getbifrost.ai/features/observability).
- **SSO** and **Vault** integrations for secure key and identity management: [SSO Integration](https://docs.getbifrost.ai/features/sso-with-google-github), [Vault Support](https://docs.getbifrost.ai/enterprise/vault-support).

## Common Pitfalls and How to Avoid Them

- Thin test suites: If your dataset lacks tough cases, gates will pass while users still see failures. Mine production logs and simulate edge conditions.
- Over-reliance on single metrics: Combine correctness, faithfulness, instruction following, safety, and performance; avoid optimizing only for one metric.
- Unclear rubrics: Vague judge prompts lead to noisy scores. Use explicit, task-specific criteria and calibrate against human reviews ( [Empirical Study of LLM-as-a-Judge](https://arxiv.org/abs/2506.13639)).
- Ignoring multi-turn behavior: Single-turn checks miss tool orchestration, recovery, and escalation flow. Simulate entire journeys.
- No cost/latency tracking: Quality without performance isn’t production-ready. Gate on latency ceilings and budget adherence in CI.

## Putting It All Together

A robust CI/CD integration for AI evals looks like this:

1. Iterate prompts and workflows in an experimentation IDE with structured output checks. See [Experimentation](https://www.getmaxim.ai/products/experimentation).
2. Build scenario-rich test suites; author evaluators across correctness, faithfulness, instruction following, safety, and performance.
3. Run smoke evals on every PR; fail builds on threshold violations. Use Bifrost for provider reliability and governance controls ( [Unified Interface](https://docs.getbifrost.ai/features/unified-interface), [Governance](https://docs.getbifrost.ai/features/governance)).
4. Simulate multi-turn agents and tool use pre-release to validate trajectories and failure handling ( [Agent Simulation & Evaluation](https://www.getmaxim.ai/products/agent-simulation-evaluation)).
5. Observe in production with distributed tracing; schedule online evals on sampled traffic; alert on drift ( [Agent Observability](https://www.getmaxim.ai/products/agent-observability)).
6. Curate new datasets from production logs and human feedback; regress against them continuously.

With this loop, teams ship higher-quality AI applications faster—grounded by evals that reflect real user journeys and measurable outcomes.

</details>

</research_source>

<research_source type="guideline_exploitation" phase="exploitation" file="how-to-run-jobs-in-parallel-with-github-actions.md">
<details>
<summary>How to run jobs in parallel with GitHub Actions</summary>

Phase: [EXPLOITATION]

# How to run jobs in parallel with GitHub Actions

**Source URL:** <https://dev.to/cicube/how-to-run-jobs-in-parallel-with-github-actions-4png>

## Introduction

I will try to provide some insights on how parallel running jobs using GitHub Actions can be helpful in optimizing our CI/CD pipelines. Their parallel running jobs thus allow running independent jobs, which may save much precious time in our workflows. This is very helpful for larger projects because the overall build time will be reduced and debugging can get very easy since the jobs are separated themselves.

## Stop talking, show me the code!

```
name: (Compiler) Rust

on:
  push:
    branches: ["main"]

jobs:
  test: # Job 'test' starts same time as Job 'lint'
    name: Rust Test (${{ matrix.target.os }})
    strategy:
      matrix: # Parallelize jobs across different OS environments
        target:
          - target: ubuntu-latest
            os: ubuntu-latest
          - target: macos-latest
            os: macos-latest
          - target: windows-latest
    runs-on: ${{ matrix.target.os }}
    steps:
      - uses: actions/checkout@v4
      - uses: Swatinem/rust-cache@v2 # Cache Rust dependencies
      - name: cargo test
        run: cargo test

  lint: # Job 'lint' starts same time as Job 'test'
    name: Rust Lint
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions-rs/toolchain@v1
        with:
          toolchain: nightly-2023-08-01
          override: true
          components: rustfmt, clippy
      - uses: Swatinem/rust-cache@v2
      - name: rustfmt
        run: grep -r --include "*.rs" --files-without-match "@generated" crates | xargs rustup run nightly-2023-08-01 rustfmt --check --config="skip_children=true"
```

What’s going on here?

- Matrix Strategy: This is where things get interesting. The matrix section allows us to run the same job on different platforms or configurations, which in our case is just Ubuntu.
- Parallel Jobs - Note above that the test and the lint jobs run in parallel, reducing overall job runtime.
- Caching: This is done by leveraging the Rust cache, which increases build times in subsequent compilations by skipping superfluous downloads and recompilations.

## Depandent GitHub Actions Workflows

By using the dependencies between jobs, we don’t waste time and resources on work that doesn’t need to be done on the off-chance that earlier jobs may fail. In such a way, it makes sure that more efficiently run jobs will reduce debugging time when failures are caught earlier and later jobs are correctly skipped.

```
name: (Compiler) Rust

on:
  push:
    branches: ["main"]

jobs:
  test:
    name: Rust Test (${{ matrix.target.os }})
    strategy:
      matrix:
        target:
          - target: ubuntu-latest
            os: ubuntu-latest
          - target: macos-latest
            os: macos-latest
          - target: windows-latest
    runs-on: ${{ matrix.target.os }}
    steps:
      - uses: actions/checkout@v4
      - uses: Swatinem/rust-cache@v2
      - name: cargo test
        run: cargo test

  lint:
    name: Rust Lint
    runs-on: ubuntu-latest
    // highlight-next-line
    needs: [test] # Job 'lint' depends on Job 'test'
    steps:
      - uses: actions/checkout@v4
      - uses: actions-rs/toolchain@v1
        with:
          toolchain: nightly-2023-08-01
          override: true
          components: rustfmt, clippy
      - uses: Swatinem/rust-cache@v2 # Reuse cache from Job #1
      - name: rustfmt
        run: grep -r --include "*.rs" --files-without-match "@generated" crates | xargs rustup run nightly-2023-08-01 rustfmt --check --config="skip_children=true"
```

The important thing here is the use of setting `jobs.<job-id>.needs`, which defines dependences between jobs. In this way, we could be assured about the order of job execution, and also avoid spending resources on running useless jobs in case something in any critical task fails.

## Conclusion

This post explained the concept of parallel running jobs in GitHub Actions, which represents an efficiency increase since it reduces the build times and makes debugging easier. More optimization is possible with a matrix strategy-you can run a job on multiple platforms/configurations. There could also be a dependency between jobs introduced via the `jobs.<job_id>.needs` configuration; this would make sure resource-saving jobs are not executed when some key precedent jobs fail.

</details>

</research_source>

<research_source type="guideline_exploitation" phase="exploitation" file="pyproject-toml-explained.md">
<details>
<summary>pyproject.toml explained</summary>

Phase: [EXPLOITATION]

# pyproject.toml explained

**Source URL:** <https://betterstack.com/community/guides/scaling-python/pyproject-explained/>

Python

Stanley Ulili

Updated on March 6, 2025

###### Contents

- [Prerequisites](https://betterstack.com/community/guides/scaling-python/pyproject-explained/#prerequisites)
- [The history and purpose of `pyproject.toml`](https://betterstack.com/community/guides/scaling-python/pyproject-explained/#the-history-and-purpose-of-pyproject-toml)
- [Getting started with pyproject.toml](https://betterstack.com/community/guides/scaling-python/pyproject-explained/#getting-started-with-pyproject-toml)
- [Understanding the core sections in pyproject.toml](https://betterstack.com/community/guides/scaling-python/pyproject-explained/#understanding-the-core-sections-in-pyproject-toml)
- [Tool-specific configuration in pyproject.toml](https://betterstack.com/community/guides/scaling-python/pyproject-explained/#tool-specific-configuration-in-pyproject-toml)
- [Dynamic versioning with `pyproject.toml`](https://betterstack.com/community/guides/scaling-python/pyproject-explained/#dynamic-versioning-with-pyproject-toml)
- [Final thoughts](https://betterstack.com/community/guides/scaling-python/pyproject-explained/#final-thoughts)

[`pyproject.toml`](https://pip.pypa.io/en/stable/reference/build-system/pyproject-toml/) is a powerful configuration file format for Python projects that enhances project organization, build specifications, and dependency management.

It was introduced as part of [PEP 518](https://peps.python.org/pep-0518/) and has become the standard for modern Python projects, earning its place as the default in major tools like [Poetry](https://python-poetry.org/), [Hatch](https://hatch.pypa.io/), and [PDM](https://pdm.fming.dev/).

With its broad ecosystem support and clean, readable syntax, `pyproject.toml` offers a vastly improved configuration experience compared to the legacy setup.py approach.

This article will guide you using `pyproject.toml` to create a well-structured Python project. You'll learn how to leverage its features and customize configurations to build a project that adheres to industry best practices.

## Prerequisites

Before diving into the rest of this article, ensure you have a recent version of [Python](https://www.python.org/downloads/) (3.13+) and pip installed on your machine. This article also assumes a basic understanding of Python and dependency management.

## The history and purpose of `pyproject.toml`

For years, Python packaging was fragmented, relying on multiple configuration files like `setup.py`, `requirements.txt`, and tool-specific configs.

This led to inconsistencies, security risks, and maintenance challenges. In particular, the `setup.py` approach suffered from arbitrary code execution risks, bootstrapping issues, and lack of standardization.

To address these problems, PEP 518 introduced `pyproject.toml` in 2016, providing a standardized way to define build dependencies. Over time, additional PEPs refined its role, with significant tools like Poetry, Flit, and setuptools adopting it as a central configuration file.

Switching from `setup.py` to a declarative approach, `pyproject.toml` enhances security, simplifies dependency management, promotes consistency, and centralizes configuration for development tools.

## Getting started with pyproject.toml

To get the most out of this tutorial, create a new Python project to try out the concepts we'll discuss.

Start by initializing a new project structure using the commands below:

Copied!

```command
mkdir pyproject-demo && cd pyproject-demo
```

Create the virtual environment:

Copied!

```command
python3 -m venv venv
```

Activate the virtual environment:

Copied!

```command
source venv/bin/activate
```

Now, create a basic `pyproject.toml` file in the root of your project directory:

pyproject.toml

Copied!

```toml
[build-system]
requires = ["setuptools>=42", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "pyproject-demo"
version = "0.1.0"
description = "A sample Python project using pyproject.toml"
readme = "README.md"
authors = [\
    {name = "Your Name", email = "your.email@example.com"}\
]
requires-python = ">=3.7"
```

This snippet defines the build system requirements and basic project metadata. We'll explore all the different ways you can customize this configuration, but for now, let's set up a minimal package structure:

Copied!

```command
mkdir -p src/pyproject_demo
```

Create a simple module file:

src/pyproject\_demo/\_\_init\_\_.py

Copied!

```python
"""A sample Python package using pyproject.toml."""

__version__ = "0.1.0"

def hello():
    """Return a friendly greeting."""
    return "Hello, world!"
```

Now, verify your setup by installing the package in development mode:

Copied!

```command
pip install -e .
```

Output

```text
Obtaining file:///Users/stanley/pyproject-demo
  Installing build dependencies ... done
  Checking if build backend supports build_editable ... done
  Getting requirements to build editable ... done
  Preparing editable metadata (pyproject.toml) ... done
  ...
  Stored in directory: /private/var/folders/rr/372_1g9j1cbd1_zhrcc13s8m0000gn/T/pip-ephem-wheel-cache-25cy86ow/wheels/17/4b/2d/a93454a53e1a643831f489eb61407df39846d1d33d89c2428a
Successfully built pyproject-demo
Installing collected packages: pyproject-demo
Successfully installed pyproject-demo-0.1.0
...
```

Once installed, you can test the package in a Python interpreter. Open the shell with the following command:

Copied!

```command
python
```

Then, run the following code:

Copied!

```python
>>> from pyproject_demo import hello
>>> hello()
'Hello, world!'
```

The first thing you'll notice about `pyproject.toml` is that it uses [TOML](https://toml.io/), a minimal configuration file format designed to be easy to read and write.

Unlike `setup.py`, which is executable Python code, `pyproject.toml` is a declarative specification, which eliminates many potential security issues and makes project configurations more consistent.

## Understanding the core sections in pyproject.toml

Now that you've set up a basic project, let's explore the main sections of `pyproject.toml` in detail. Understanding these sections is crucial for effectively configuring your Python projects.

### The build-system section

The `[build-system]` section is mandatory according to [PEP 518](https://peps.python.org/pep-0518/). It specifies which build tools are required to build your package and which backend to use:

pyproject.toml

Copied!

```toml
[build-system]
requires = ["setuptools>=42", "wheel"]
build-backend = "setuptools.build_meta"
```

The `requires` field lists the packages needed for building (not running) your package. The `build-backend` specifies which tool will interpret your build instructions. While setuptools is the most common backend, alternatives like [Hatchling](https://hatch.pypa.io/), [Poetry](https://python-poetry.org/), or [Flit](https://flit.pypa.io/) can also be used.

### The project section

The `[project]` section contains metadata about your package and replaces the previous setuptools `setup()` call:

pyproject.toml

Copied!

```toml
[project]
name = "pyproject-demo"
version = "0.1.0"
description = "A sample Python project using pyproject.toml"
readme = "README.md"
authors = [\
    {name = "Your Name", email = "your.email@example.com"}\
]
requires-python = ">=3.7"
license = {text = "MIT"}
classifiers = [\
    "Development Status :: 3 - Alpha",\
    "Programming Language :: Python :: 3",\
    "Programming Language :: Python :: 3.7",\
    "Programming Language :: Python :: 3.8",\
    "Programming Language :: Python :: 3.9",\
    "License :: OSI Approved :: MIT License",\
    "Operating System :: OS Independent",\
]
```

This section includes package name, version, description, and other metadata that will be used when publishing to the Python Package Index (PyPI). The `requires-python` field helps users know which Python versions are supported by your package.

### Managing dependencies

One of the most significant improvements in `pyproject.toml` is how it handles dependencies. Dependencies are specified in the `[project.dependencies]` section:

pyproject.toml

Copied!

```toml
[project]
# ... other project metadata ...

dependencies = [\
    "requests>=2.28.0",\
    "pyyaml>=6.0",\
    "click>=8.1.0",\
]
```

For optional features or development dependencies, you can use the `[project.optional-dependencies]` section:

pyproject.toml

Copied!

```toml
[project.optional-dependencies]
dev = [\
    "pytest>=7.0.0",\
    "black>=22.3.0",\
    "flake8>=4.0.1",\
    "mypy>=0.950",\
]

docs = [\
    "sphinx>=4.5.0",\
    "sphinx-rtd-theme>=1.0.0",\
]
```

This approach lets users install extra dependencies only when needed:

Copied!

```command
pip install -e ".[dev]"  # Install with development dependencies
pip install -e ".[docs]"  # Install with documentation dependencies
pip install -e ".[dev,docs]"  # Install with both sets
```

### Entry points and scripts

To create command-line scripts that can be called directly after installation, use the `[project.scripts]` section:

pyproject.toml

Copied!

```toml
[project.scripts]
pyproject-demo = "pyproject_demo.cli:main"
```

This configuration makes a command called `pyproject-demo` available on the system path after installation, which calls the `main()` function in the `pyproject_demo.cli` module.

For more complex plugin registration or entry points that other packages can discover, use the `[project.entry-points]` section:

pyproject.toml

Copied!

```toml
[project.entry-points."console_scripts"]
pyproject-demo = "pyproject_demo.cli:main"

[project.entry-points."pytest11"]
pyproject-plugin = "pyproject_demo.pytest_plugin"
```

## Tool-specific configuration in pyproject.toml

Beyond the standard project metadata and dependency management, one of the most powerful features of `pyproject.toml` is its ability to house configuration for various development tools. This approach centralizes your project settings, eliminating the need for multiple configuration files scattered throughout your project directory.

### Black code formatter

[Black](https://black.readthedocs.io/) is a popular Python code formatter that enforces a consistent style across your codebase. You can configure Black directly in your `pyproject.toml` file:

pyproject.toml

Copied!

```toml
[tool.black]
line-length = 88
target-version = ["py37", "py38", "py39"]
include = '\.pyi?

exclude = '''
/(
    \.git
  | \.hg
  | \.mypy_cache
  | \.tox
  | \.venv
  | _build
  | buck-out
  | build
  | dist
)/
'''
```

This configuration sets the maximum line length to 88 characters (Black's default), specifies which Python versions to target, and defines patterns for files to include or exclude from formatting. Black's native support for `pyproject.toml` makes it a perfect example of how modern Python tools are embracing this configuration approach.

### MyPy type checking

[MyPy](https://mypy-lang.org/) is a static type checker for Python that helps catch type-related errors before runtime. Its configuration in `pyproject.toml` is straightforward:

pyproject.toml

Copied!

```toml
[tool.mypy]
python_version = "3.7"
warn_return_any = true
warn_unused_configs = true
disallow_untyped_defs = true
disallow_incomplete_defs = true

[[tool.mypy.overrides]]
module = ["tests.*"]
disallow_untyped_defs = false
```

This configuration enforces strict type checking for your project code while relaxing the requirements for test files. The `disallow_untyped_defs` option ensures all functions have type annotations, improving code quality and documentation. With the override section, you can apply different rules to specific modules, making it easier to adopt type checking in larger projects gradually.

### Ruff

[Ruff](https://github.com/charliermarsh/ruff) is a fast Python linter written in Rust that aims to replace multiple tools like Flake8, isort, and more. Its configuration in `pyproject.toml` is comprehensive:

pyproject.toml

Copied!

```toml
[tool.ruff]
# Enable flake8-bugbear (B) rules
select = ["E", "F", "B"]
# Ignore specific rules
ignore = ["E501"]
# Line length to target
line-length = 88
# Target Python version
target-version = "py37"
# Allow autofix for all enabled rules
fixable = ["ALL"]
# Allow unused variables with leading underscore
dummy-variable-rgx = "^(_+|(_+[a-zA-Z0-9_]*[a-zA-Z0-9]+?))$"

[tool.ruff.isort]
known-first-party = ["pyproject_demo"]
```

This configuration enables specific rule sets (E for style errors, F for flake8 rules, and B for bugbear rules), ignores certain rules (like E501 for line length), and configures import sorting behavior. Ruff's unified approach to linting demonstrates the value of having a single configuration file for all your development tools, as it can replace multiple separate linters with a single, faster implementation.

### Combining multiple tools

The real power of pyproject.toml comes from centralizing all these configurations in one place. Here's how they look together:

pyproject.toml

Copied!

```toml
[build-system]
requires = ["setuptools>=42", "wheel"]
build-backend = "setuptools.build_meta"

[project]
# ... project metadata ...

[tool.black]
line-length = 88
target-version = ["py37", "py38", "py39"]

[tool.mypy]
python_version = "3.7"
warn_return_any = true
disallow_untyped_defs = true

[tool.ruff]
select = ["E", "F", "B"]
line-length = 88
target-version = "py37"
```

This unified approach offers several advantages:

- Single source of truth: All configurations are in one file, making it easier to maintain consistency.
- Reduced cognitive load: Developers don't need to remember multiple file formats and locations.
- Easier onboarding: New team members can quickly understand the project's tooling setup.
- Version control efficiency: Changes to tool configurations are tracked together, simplifying code reviews.

Most modern Python development tools now support pyproject.toml configuration, reflecting a community-wide shift toward standardization and simplification.

As you develop your Python projects, leveraging this centralized configuration approach can significantly improve your development workflow and project maintainability.

## Dynamic versioning with `pyproject.toml`

One common challenge in Python projects is maintaining consistent version numbers across your package. Repeating the version in multiple places can lead to inconsistencies when one location is updated but others are forgotten.

Let's explore how to implement dynamic versioning with `pyproject.toml` to solve this problem.

### Using a dedicated version file

A good practice is to create a single source of truth for your version number:

src/pyproject\_demo/\_version.py

Copied!

```python
"""Version information."""

__version__ = "0.1.0"
```

Then reference this version in your `pyproject.toml` file:

pyproject.toml

Copied!

```toml
[project]
name = "pyproject-demo"
dynamic = ["version"]
# ... other project metadata ...

[tool.setuptools.dynamic]
version = {attr = "pyproject_demo._version.__version__"}
```

With this approach, you declare that the version is "dynamic" in the `[project]` section and specify its source in the `[tool.setuptools.dynamic]` section. This configuration tells setuptools to read the version from the `__version__` variable in the `pyproject_demo._version` module at build time.

The primary benefit of this method is that both your code and build system reference the same version string. Your package can access its version at runtime using:

Copied!

```python
from pyproject_demo._version import __version__

print(f"Running version {__version__}")
```

### Using SCM-based versioning

For more advanced projects, you can use tools like [setuptools-scm](https://github.com/pypa/setuptools_scm), which automatically derives your package version from git tags:

pyproject.toml

Copied!

```toml
[build-system]
requires = ["setuptools>=42", "wheel", "setuptools_scm[toml]>=6.2"]
build-backend = "setuptools.build_meta"

[project]
name = "pyproject-demo"
dynamic = ["version"]
# ... other project metadata ...

[tool.setuptools_scm]
write_to = "src/pyproject_demo/_version.py"
```

This configuration adds `setuptools_scm` to your build dependencies and tells it to write the version (derived from git tags and local changes) to a `_version.py` file.

When you tag a commit in your git repository (e.g., `git tag -a v0.2.0 -m "Version 0.2.0"`), setuptools-scm will use that tag as the version. For local development with uncommitted changes, it will add development suffixes (like `.dev1+g4f8e9d1.d20230315`), helping you track exactly which code version is being used.

The version file is generated during the build process, so it won't exist in the source repository but will be available in the installed package:

Copied!

```python
>>> import pyproject_demo
>>> pyproject_demo.__version__
'0.2.0'  # Or something like '0.2.0.dev1+g4f8e9d1.d20230315' for development builds
```

### Manually managing versions in `pyproject.toml`

For simpler projects, you might prefer to maintain the version directly in `pyproject.toml`:

pyproject.toml

Copied!

```toml
[project]
name = "pyproject-demo"
version = "0.1.0"
# ... other project metadata ...
```

However, you'll need a way for your package to access this version at runtime. One approach is to use the `importlib.metadata` module (available in Python 3.8+ or via the `importlib-metadata` backport):

src/pyproject\_demo/\_\_init\_\_.py

Copied!

```python
"""A sample Python package using pyproject.toml."""

try:
    from importlib.metadata import version, PackageNotFoundError
except ImportError:
    from importlib_metadata import version, PackageNotFoundError

try:
    __version__ = version("pyproject-demo")
except PackageNotFoundError:
    # Package is not installed
    __version__ = "unknown"

def hello():
    """Return a friendly greeting."""
    return "Hello, world!"
```

This method works well for installed packages but has limitations during development. It's best suited for simple projects or when integration with development tools that expect a static version number is not needed.

## Final thoughts

This article explored how `pyproject.toml` has transformed Python project management through centralized, declarative configuration.

The adoption of `pyproject.toml` by the Python ecosystem demonstrates a commitment to standardization that benefits developers with enhanced security, simplified workflows, and better dependency management.

Consider migrating your existing projects to `pyproject.toml`, starting simple and gradually incorporating more advanced features. Effective Python project management is an ongoing refinement process, and embracing this approach will serve you well as your projects evolve.

Happy coding!

</details>

</research_source>

<research_source type="guideline_exploitation" phase="exploitation" file="pytest-documentation.md">
<details>
<summary>pytest documentation</summary>

Phase: [EXPLOITATION]

# pytest documentation

**Source URL:** <https://docs.pytest.org/>

The `pytest` framework makes it easy to write small, readable tests, and can
scale to support complex functional testing for applications and libraries.

**PyPI package name**: [pytest](https://pypi.org/project/pytest)

## A quick example ¶

```
# content of test_sample.py
def inc(x):
    return x + 1

def test_answer():
    assert inc(3) == 5
```

To execute it:

```
$ pytest
=========================== test session starts ============================
platform linux -- Python 3.x.y, pytest-9.x.y, pluggy-1.x.y
rootdir: /home/sweet/project
collected 1 item

test_sample.py F                                                     [100%]

================================= FAILURES =================================
_______________________________ test_answer ________________________________

    def test_answer():
>       assert inc(3) == 5
E       assert 4 == 5
E        +  where 4 = inc(3)

test_sample.py:6: AssertionError
========================= short test summary info ==========================
FAILED test_sample.py::test_answer - assert 4 == 5
============================ 1 failed in 0.12s =============================
```

Due to `pytest`’s detailed assertion introspection, only plain `assert` statements are used.
See [Get started](https://docs.pytest.org/en/stable/getting-started.html#getstarted) for a basic introduction to using pytest.

## Features ¶

- Detailed info on failing [assert statements](https://docs.pytest.org/en/stable/how-to/assert.html#assert) (no need to remember `self.assert*` names)

- [Auto-discovery](https://docs.pytest.org/en/stable/explanation/goodpractices.html#test-discovery) of test modules and functions

- [Modular fixtures](https://docs.pytest.org/en/stable/reference/fixtures.html#fixture) for managing small or parametrized long-lived test resources

- Can run [unittest](https://docs.pytest.org/en/stable/how-to/unittest.html#unittest) (including trial) test suites out of the box

- Python 3.10+ or PyPy 3

- Rich plugin architecture, with over 1300+ [external plugins](https://docs.pytest.org/en/stable/reference/plugin_list.html#plugin-list) and thriving community


## Documentation ¶

- [Get started](https://docs.pytest.org/en/stable/getting-started.html#get-started) \- install pytest and grasp its basics in just twenty minutes

- [How-to guides](https://docs.pytest.org/en/stable/how-to/index.html#how-to) \- step-by-step guides, covering a vast range of use-cases and needs

- [Reference guides](https://docs.pytest.org/en/stable/reference/index.html#reference) \- includes the complete pytest API reference, lists of plugins and more

- [Explanation](https://docs.pytest.org/en/stable/explanation/index.html#explanation) \- background, discussion of key topics, answers to higher-level questions


## Bugs/Requests ¶

Please use the [GitHub issue tracker](https://github.com/pytest-dev/pytest/issues) to submit bugs or request features.

## Support pytest ¶

[Open Collective](https://opencollective.com/) is an online funding platform for open and transparent communities.
It provides tools to raise money and share your finances in full transparency.

It is the platform of choice for individuals and companies that want to make one-time or
monthly donations directly to the project.

See more details in the [pytest collective](https://opencollective.com/pytest).

## pytest for enterprise ¶

Available as part of the Tidelift Subscription.

The maintainers of pytest and thousands of other packages are working with Tidelift to deliver commercial support and
maintenance for the open source dependencies you use to build your applications.
Save time, reduce risk, and improve code health, while paying the maintainers of the exact dependencies you use.

[Learn more.](https://tidelift.com/subscription/pkg/pypi-pytest?utm_source=pypi-pytest&utm_medium=referral&utm_campaign=enterprise&utm_term=repo)

### Security ¶

If you have found an issue that you believe is a security vulnerability, please do not create an issue – instead, report it via a [new security advisory](https://github.com/pytest-dev/pytest/security/advisories/new).

</details>

</research_source>

<research_source type="guideline_exploitation" phase="exploitation" file="unit-testing-best-practices-13-ways-to-improve-your-tests.md">
<details>
<summary>Unit testing best practices: 13 ways to improve your tests</summary>

Phase: [EXPLOITATION]

# Unit testing best practices: 13 ways to improve your tests

**Source URL:** <https://brightsec.com/blog/unit-testing-best-practices/>

A unit test validates and verifies individual software units (or components) to ensure each unit works as intended. A unit may be a function, procedure, method, object, or module. Unit testing occurs during the coding phase of the software development lifecycle, and can help identify coding errors, code quality issues, and security issues.

https://brightsec.com/wp-content/uploads/2026/01/Frame-1000002646-2.jpg.webp

# Unit Testing Best Practices: 9 Ways to Make Unit Tests Shine

## What Is Unit Testing?

A unit test validates and verifies individual software units (or components) to ensure each unit works as intended. A unit may be a function, procedure, method, object, or module. Unit testing occurs during the coding phase of the software development lifecycle, and can help identify coding errors, code quality issues, and security issues.

While [unit testing](https://brightsec.com/blog/unit-testing/) are very useful, there are also many ways to get them wrong. Poorly written or designed unit tests can be difficult to maintain, execute, and interpret. We’ll provide a few best practices that will make your unit tests shine.

**In this article:**

- [Why Is Unit Testing Important?](https://brightsec.com/blog/unit-testing-best-practices/#importance)
- [Unit Testing Best Practices](https://brightsec.com/blog/unit-testing-best-practices/#best-practices)
  - [1\. Write Readable, Simple Tests](https://brightsec.com/blog/unit-testing-best-practices/#simple-tests)
  - [2\. Write Deterministic Tests](https://brightsec.com/blog/unit-testing-best-practices/#deterministic-tests)
  - [3\. Test One Scenario Per Test](https://brightsec.com/blog/unit-testing-best-practices/#one-scenario-per-test)
  - [4\. Unit Tests Should Be Automated](https://brightsec.com/blog/unit-testing-best-practices/#automate)
  - [5\. Write Isolated Tests](https://brightsec.com/blog/unit-testing-best-practices/#isolated-tests)
  - [6\. Avoid Test Interdependence](https://brightsec.com/blog/unit-testing-best-practices/#avoid-test-interdependence)
  - [7\. Avoid Active API Calls](https://brightsec.com/blog/unit-testing-best-practices/#avoid-active-api-calls)
  - [8\. Combine Unit and Integration Testing](https://brightsec.com/blog/unit-testing-best-practices/#combine-unit-and-integration)
  - [9\. Ensure Unit Tests are Repeatable and Scalable](https://brightsec.com/blog/unit-testing-best-practices/#repeatable-and-scalable-tests)
  - [10\. Test for Security Issues as Part of Your Unit Tests](https://brightsec.com/blog/unit-testing-best-practices/#bright)

## Why Is Unit Testing Important?

Unit testing enables you to exercise individual code units to verify and validate that it performs the intended software behavior. Unit testing solutions help ensure code security, reliability, and quality. These are typically automated tools that quickly build and auto-generate unit test cases to verify code quality across platforms, hosts, virtual environments, or hardware environments.

Unit testing is especially important for embedded development environments requiring software systems and hardware to work in sync and comply with exacting functional safety standards.

Once you set up an automated unit testing framework, it can transition into your regression test suites. It helps across the lifecycle as you implement software updates, new requirements, and patches. You can also automate regression and unit testing and integrate them with your CI/CD pipeline.

_Related content: Read our guide to [unit testing vs integration testing](https://brightsec.com/blog/unit-testing-vs-integration-testing-4-key-differences-and-how-to-choose/)._

## Unit Testing Best Practices

https://brightsec.com/wp-content/uploads/2025/03/Slide-16_9-79-1-969x1024.png.webp

The following best practices will help you make your unit tests more effective.

### 1\. Write Readable, Simple Tests

Unit testing helps ensure your code works as intended. However, you can learn why a unit fails to pass only if you write simple and readable tests. It is easier to write, maintain, and understand simple test cases. Additionally, simple tests are easier to refactor. If the test is complex and you need to refactor some code, the tests might break.

You can use the AAA structure to write unit tests:

- **Arrange** – configure the test by setting up the tested system and other mechanisms.
- **Act** – call an action to perform to test the unit.
- **Assert** – check the result of the performed operation to verify it worked as intended.

**_Related content: Read our guide to_** [**_unit testing examples_**](https://brightsec.com/blog/unit-testing-examples/)

### 2\. Write Deterministic Tests

A deterministic test presents the same behavior as long as the code remains unchanged. It enables you to understand the issue and fix it. Then, when you run another test after modifying the code, you should see different results that either pass or fail the test.

A non-deterministic test can fail or pass without any code change. It makes it difficult to isolate the issue and fix it, which is why it is also referred to as an unstable test. You can avoid non-deterministic testing by isolating the test case, making it completely independent of other cases.

### 3\. Test One Scenario Per Test

Manual testing typically involves testing various scenarios, for example, verifying a certain bug is resolved, and all related features work as intended. You can check many types of testing and variables, but you should always ensure each unit test covers one scenario.

Covering one scenario per unit test helps isolate specific program parts containing the issue when a test fails. However, running a single test to cover several scenarios can result in uncertainties – once the test fails, you need to invest time to identify the issue.

### 4\. Unit Tests Should Be Automated

You should set up an automated process for unit testing on a daily or hourly basis or through a CI/CD process. Configure the process to ensure all team members can access and view reports. It helps ensure teams can discuss the relevant metrics, including code coverage, number of test runs, modified code coverage, and performance.

### 5\. Write Isolated Tests

Isolated unit tests help verify specific components. This type of testing is faster to run and provides more stability, ensuring you only deal with one logic at a time. You can create isolated tests using test doubles – simulated substitutes for a real class. A test double provides a fake version of a component, helping you isolate its behavior within the unit test. You can also use a stuck or mock object as a test double.

### 6\. Avoid Test Interdependence

Unit testing does not require 100% test coverage. You should set up fewer, but high-quality unit tests than many tests configured only to reach the necessary code coverage. Unit tests aim to validate individual code units, which is why you should avoid test interdependence.

Test dependency occurs when one unit test depends on the outcome of another. When one test fails, the whole suite fails too. You can prevent this issue by avoiding test interdependence in unit tests. You should write individual, independent test methods and put related tests in a single test class.

### 7\. Avoid Active API Calls

You might often encounter API calls or other service calls to databases that you don’t need to include in your tests. However, if the tests don’t engage these calls, make sure they are inactive while the tests run. It is preferable to provide API stubs with the expected behavior and responses, restricting tests to specific units.

### 8\. Combine Unit and Integration Testing

The testing pyramid is a popular model for describing the desired distribution of test resources. Tests generally become more complex and fragile the higher the pyramid you go. The tests at the top are the hardest to build and the slowest to run and debug, while lower-level tests are faster and simpler to set up and debug. Automated unit tests, representing the lowest levels of the pyramid, should comprise most of the testing.

Use unit tests to validate all the details, including the boundary conditions and corner cases. Use other tests (component, UI, functional, and integration tests) sparingly to assess the overall behavior of an API or application. Manual tests should make up the smallest proportion of your testing pyramid – they are useful for investigative and release acceptance testing.

The pyramid model can guide you through your testing strategy to achieve extensive test coverage and automation. It should help you scale up your tests while minimizing the costs involved in building, maintaining, and running your test suites.

_Learn more in our detailed guide to [vue unit testing](https://brightsec.com/blog/vue-unit-testing/)._

### 9\. Ensure Unit Tests are Repeatable and Scalable

Make your unit tests repeatable and scalable to ensure the success of your testing strategy. Establish an organized set of practices to ensure everyone writes the unit tests simultaneously as writing the application code. You might even write tests before writing your application code, such as behavior- or test-driven programming. Either way, you must build the tests closely with the application code.

Assess the application code and tests together during the code review process. Reviews provide insights into the code and its behavior, allowing you to improve the tests. Writing tests together with the code is important for bug fixes, not just planned updates and changes. There should always be a test verifying every bug fix to ensure it remains fixed.

Take a zero-tolerance approach to test failures. Testing is useless if the team ignores the results – a test failure indicates a real issue, alerting the team to address it immediately before wasting more time on buggy code or releasing it to production.

### 10\. Test for Security Issues as Part of Your Unit Tests

Bright is a developer-first Dynamic Application Security Testing (DAST) scanner, the first of its kind to integrate into unit testing, revolutionizing the ability to shift security testing even further left. You can now start to test every component / function at the speed of unit tests, baking security testing across development and CI/CD pipelines to minimize security and technical debt, by scanning early and often, spearheaded by developers. With NO false positives, start trusting your scanner when testing your applications and APIs (SOAP, REST, GraphQL), built for modern technologies and architectures. **[Sign up now for a free account](http://app.neuralegion.com/signup) and read our [docs](https://docs.brightsecurdev.wpenginepowered.com/) to learn more.**

</details>

</research_source>

<research_source type="guideline_exploitation" phase="exploitation" file="why-python-developers-should-switch-to-uv.md">
<details>
<summary>Why Python developers should switch to uv</summary>

Phase: [EXPLOITATION]

# Why Python developers should switch to uv

**Source URL:** <https://devcenter.upsun.com/posts/why-python-developers-should-switch-to-uv/>

## [​](https://developer.upsun.com/posts/insights/why-python-developers-should-switch-to-uv#introduction)  Introduction

Python development has long been plagued by slow package installations and complex dependency management. Enter [uv](https://github.com/astral-sh/uv), a new package manager developed by [Astral](https://astral.sh/) (creators of [Ruff](https://astral.sh/ruff)) that’s transforming how Python developers handle projects.

## [​](https://developer.upsun.com/posts/insights/why-python-developers-should-switch-to-uv#what-is-uv)  What is uv?

uv is a super-fast Python package manager and project management tool that serves as a drop-in replacement for pip, but with dramatically enhanced capabilities.At its core, uv addresses the fundamental pain points that have frustrated Python developers for years: slow installations, manual virtual environment management, and complex project setup processes.

## [​](https://developer.upsun.com/posts/insights/why-python-developers-should-switch-to-uv#key-benefits-of-uv)  Key benefits of uv

### [​](https://developer.upsun.com/posts/insights/why-python-developers-should-switch-to-uv#speed-and-performance)  Speed and performance

The most striking feature of uv is its incredible speed. Where pip installations can take minutes, uv completes the same tasks in seconds:

- **Up to 100x faster** package installations compared to pip
- Near-instantaneous dependency resolution
- Dramatically reduced wait times for project setup

This speed improvement isn’t marginal. Tasks that previously interrupted your development flow now happen so quickly they become seamless.

### [​](https://developer.upsun.com/posts/insights/why-python-developers-should-switch-to-uv#comprehensive-project-management)  Comprehensive project management

uv goes far beyond simple package installation. It provides a complete project management solution:

- **Automatic project initialization** with proper boilerplate structure
- **Built-in virtual environment management** with no manual activation required
- **Intelligent dependency tracking** that separates production and development packages
- **Python version management** without needing separate tools
- **Automatic `.gitignore` generation** with Python-specific excludes

### [​](https://developer.upsun.com/posts/insights/why-python-developers-should-switch-to-uv#simplified-dependency-management)  Simplified dependency management

uv also changes the way you handle dependencies:

- **Clean dependency lists**: Only direct dependencies appear in `pyproject.toml`
- **Easy package management**: Simple `uv add` and `uv remove` commands
- **Development dependencies**: Separate development packages with `--dev` flag
- **Automatic synchronization**: Team members can instantly replicate environments

## [​](https://developer.upsun.com/posts/insights/why-python-developers-should-switch-to-uv#the-new-development-workflow)  The new development workflow

uv transforms project setup from a multi-step manual process into a streamlined workflow:

### [​](https://developer.upsun.com/posts/insights/why-python-developers-should-switch-to-uv#traditional-workflow-pain-points)  Traditional workflow pain points

```
# The old way - multiple steps, slow process
mkdir new-project && cd new-project
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install package1 package2 package3
# Wait... and wait... for slow installations
pip freeze > requirements.txt
```

### [​](https://developer.upsun.com/posts/insights/why-python-developers-should-switch-to-uv#the-uv-way)  The uv way

```
# Initialize project with everything configured
uv init "new-ai-project"

cd "new-ai-project"

# Add dependencies instantly
uv add openai pydantic fastapi

# Add development tools separately
uv add ipykernel pytest --dev

# Run your code
uv run hello.py
```

This workflow reduces project setup time from minutes to approximately **15 seconds**.

## [​](https://developer.upsun.com/posts/insights/why-python-developers-should-switch-to-uv#essential-uv-commands)  Essential uv commands

### [​](https://developer.upsun.com/posts/insights/why-python-developers-should-switch-to-uv#project-initialization)  Project initialization

```
# Create new project with boilerplate
uv init "project-name"
```

This command automatically creates:

- Project directory structure
- `.gitignore` file with Python excludes
- `pyproject.toml` configuration
- Sample `hello.py` file
- README template
- Virtual environment

### [​](https://developer.upsun.com/posts/insights/why-python-developers-should-switch-to-uv#dependency-management)  Dependency management

```
# Add production dependencies
uv add requests pandas numpy

# Add development dependencies
uv add pytest black flake8 --dev

# Remove packages
uv remove pandas

# Sync environment from pyproject.toml
uv sync
```

### [​](https://developer.upsun.com/posts/insights/why-python-developers-should-switch-to-uv#running-code)  Running code

```
# Execute Python files directly
uv run script.py

# Run with environment automatically activated
uv run python -m pytest
```

## [​](https://developer.upsun.com/posts/insights/why-python-developers-should-switch-to-uv#comparison-with-traditional-tools)  Comparison with traditional tools

### [​](https://developer.upsun.com/posts/insights/why-python-developers-should-switch-to-uv#uv-vs-pip)  uv vs pip

| Feature | pip | uv |
| --- | --- | --- |
| **Installation Speed** | Slow (minutes) | Ultra-fast (seconds) |
| **Dependency Resolution** | Basic | Advanced |
| **Virtual Environments** | Manual management | Automatic |
| **Project Structure** | Manual setup | Auto-generated |
| **Clean Dependencies** | Bloated requirements.txt | Clean pyproject.toml |

### [​](https://developer.upsun.com/posts/insights/why-python-developers-should-switch-to-uv#uv-vs-poetry)  uv vs Poetry

While Poetry provides excellent dependency management, uv combines Poetry’s capabilities with superior speed and simpler workflows. uv’s faster installation and automatic environment handling make it more suitable for rapid development cycles.

### [​](https://developer.upsun.com/posts/insights/why-python-developers-should-switch-to-uv#uv-vs-pipenv)  uv vs Pipenv

uv surpasses Pipenv in both speed and reliability. Where Pipenv sometimes struggles with dependency resolution, uv handles complex dependencies effortlessly while maintaining its performance advantage.

## [​](https://developer.upsun.com/posts/insights/why-python-developers-should-switch-to-uv#getting-started-with-uv)  Getting started with uv

### [​](https://developer.upsun.com/posts/insights/why-python-developers-should-switch-to-uv#installation)  Installation

Choose your preferred installation method:**macOS (recommended):**

```
brew install uv
```

**macOS/Linux (curl):**

```
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**Windows:**
Follow the official installation guide at [docs.astral.sh/uv](https://docs.astral.sh/uv)Verify installation:

```
uv --help
```

### [​](https://developer.upsun.com/posts/insights/why-python-developers-should-switch-to-uv#migrating-existing-projects)  Migrating existing projects

uv maintains backward compatibility with existing Python projects:**From requirements.txt:**

```
uv pip install -r requirements.txt
```

**Convert to uv project:**

```
uv init --existing-project
uv add $(cat requirements.txt | grep -v '^#' | tr '\n' ' ')
```

## [​](https://developer.upsun.com/posts/insights/why-python-developers-should-switch-to-uv#advanced-features)  Advanced features

### [​](https://developer.upsun.com/posts/insights/why-python-developers-should-switch-to-uv#python-version-management)  Python version management

uv can manage Python installations directly:

```
# List available Python versions
uv python list

# Install specific Python version
uv python install 3.12

# Use specific version for project
uv init --python 3.12 my-project
```

### [​](https://developer.upsun.com/posts/insights/why-python-developers-should-switch-to-uv#team-collaboration)  Team collaboration

uv makes team collaboration seamless:

1. **Share project**: Simply commit `pyproject.toml` to version control
2. **Setup for teammates**: `uv sync` creates identical environments instantly
3. **No configuration drift**: Locked dependencies ensure consistency

## [​](https://developer.upsun.com/posts/insights/why-python-developers-should-switch-to-uv#integration-with-development-tools)  Integration with development tools

uv works seamlessly with modern development environments:

- **IDEs**: VS Code, PyCharm, Cursor automatically detect uv environments
- **CI/CD**: Simple integration with GitHub Actions, GitLab CI
- **Docker**: Excellent containerization support
- **Version Control**: Clean `pyproject.toml` files work perfectly with Git

## [​](https://developer.upsun.com/posts/insights/why-python-developers-should-switch-to-uv#deploying-python-applications-with-uv-on-upsun)  Deploying Python applications with uv on Upsun

uv’s speed advantages make it perfect for cloud deployments. Here’s how to deploy Python applications using uv on Upsun’s platform:

### [​](https://developer.upsun.com/posts/insights/why-python-developers-should-switch-to-uv#project-structure)  Project structure

Your uv-based project should have this structure:

```
my-python-app/
├── .upsun/
│   └── config.yaml
├── pyproject.toml  # Created by uv
├── main.py
└── src/
```

### [​](https://developer.upsun.com/posts/insights/why-python-developers-should-switch-to-uv#essential-upsun-configuration)  Essential Upsun configuration

Create `.upsun/config.yaml` with uv-optimized settings:

```
applications:
  app:
    source:
      root: "/"

    type: "python:3.12"

    # Use uv for dependency management
    dependencies:
      python3:
        uv: "*"

    # uv build process
    hooks:
      build: |
        # Use uv for fast dependency installation
        uv sync --frozen

        # Optional: compile Python files for better performance
        # python -m compileall .

    # Web server configuration
    web:
      commands:
        # We add --no-sync to prevent uv from trying to write the uv.lock at runtime
        start: "uv run --no-sync uvicorn app:app --reload --host 0.0.0.0 --port $PORT"

    # uv cache optimization
    variables:
      env:
        uv_CACHE_DIR: "/tmp/uv-cache"
        PYTHONPATH: "."

routes:
  "https://{default}/":
    type: upstream
    upstream: "app:http"
```

### [​](https://developer.upsun.com/posts/insights/why-python-developers-should-switch-to-uv#key-configuration-benefits)  Key configuration benefits

**Fast builds**: uv’s speed dramatically reduces deployment time compared to pip-based builds.**Dependency optimization**: The `uv sync --frozen` command ensures reproducible builds with locked dependencies.**Cache efficiency**: uv’s intelligent caching works perfectly with Upsun’s build process.

### [​](https://developer.upsun.com/posts/insights/why-python-developers-should-switch-to-uv#deployment-workflow)  Deployment workflow

1. **Initialize your project locally:**

```
uv init my-app
cd my-app
uv add fastapi gunicorn
```

2. **Create your application:**

```
# main.py
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello from uv on Upsun!"}
```

3. **Deploy to Upsun:**

```
git add .
git commit -m "Setup FastAPI with uv"
upsun push
```

The uv-powered build process will install dependencies in seconds rather than minutes, making your deployment pipeline significantly faster.

**Compatibility**: Most Python packages work seamlessly with uv, but complex enterprise environments may require testing.

## [​](https://developer.upsun.com/posts/insights/why-python-developers-should-switch-to-uv#conclusion)  Conclusion

uv transforms Python development from a series of manual, time-consuming tasks into a streamlined, efficient workflow. The dramatic speed improvements alone justify adoption, but uv’s comprehensive project management capabilities make it essential for modern Python development.The question isn’t whether you should try uv, it’s how quickly you can integrate it into your development workflow. With its backward compatibility, minimal learning curve, and transformative performance benefits, uv represents the future of Python package management.

</details>

</research_source>

<golden_source type="local_files">
## Local File Sources (from Article Guidelines)

_No local file sources found._

</golden_source>