# Task conventions — applies to `lab/tasks/` only

Full source: `instructors/context/lab-conventions/lab-conventions.md` §3, §12, §15

Also read: `instructors/context/lab-conventions/conventions-common.md`

## 3. Task document template

Required structure for every `task-N.md`:

```markdown
# <Task title>

<h4>Time</h4>
~<estimate> min

<h4>Purpose</h4>
<One sentence: what the student will learn.>

<h4>Context</h4>
<1–3 sentences: why this task matters.>

<h4>Table of contents</h4>
- [1. Steps](#1-steps)
  - [1.1. Follow the `Git workflow`](#11-follow-the-git-workflow)
  - [1.2. Create an issue](#12-create-an-issue)
  ...
- [2. Acceptance criteria](#2-acceptance-criteria)

## 1. Steps

### 1.1. Follow the `Git workflow`
### 1.2. Create a `Lab Task` issue
Title: `[Task] <Task title>`
...
### 1.N. Finish the task
1. [Create a PR](../git-workflow.md#create-a-pr) with your changes.
2. [Get a PR review](../git-workflow.md#get-a-pr-review) ...

----

## 2. Acceptance criteria
- [ ] <Criterion 1>
```

Key rules:

- `Time`, `Purpose`, `Context`, `Table of contents` use `<h4>` HTML tags (excluded from auto-ToC).
- Top-level sections are numbered: `## 1. Steps`, `## 2. Acceptance criteria`.
- Steps are `### 1.1.`, `### 1.2.`; sub-steps are `#### 1.3.1.`, `#### 1.3.2.`.
- Step 1.1 ("Follow the Git workflow") is omitted for tasks that don't produce commits.
- Step 1.2 is always "Create an issue". When 1.1 is omitted, it becomes step 1.1.
- Last step: "Finish the task" (PR + review) OR "Write a comment for the issue" (evidence + close).
- Acceptance criteria use `- [ ]` checkboxes; must be concrete and verifiable.

## 4.12 Commit message format (tasks only)

Use [conventional commits](https://www.conventionalcommits.org/): `<type>: <description>`.
Common types: `fix:`, `feat:`, `docs:`.
When a task specifies a commit message, provide it in a ` ```text ``` ` code block.

## 4.19 Steps with sub-steps (tasks)

When multiple actions serve one logical goal, group under one step with "Complete the following steps:":

```markdown
1. Configure the environment. Complete the following steps:
   1. Open `.env.example`.
   2. Copy it to `.env.secret`.
```

When actions don't share a goal, flatten into separate top-level steps.

## 12. Task design principles

**12.1 Progressive complexity** — Required tasks increase in complexity: observe → debug/fix → implement/deploy. Optional tasks are independent. Start with observation, not coding.

**12.2 Every task teaches something** — Each task has a clear Purpose and Context. Assign domain entities distinct roles: Reference (study), Debug (fix), Implement (build from template).

**12.3 High-level + low-level fallbacks** — Write high-level steps in the task; link to wiki for detailed breakdowns. Experienced students move fast; beginners follow the wiki.

**12.4 Fallback methods** — When a step may not work for all students (OS-specific, tool-specific), provide alternatives using `Method N:` format.

**12.5 Localize instructions** — Keep instructions in the task file. Don't make students jump between 5 files to understand one step.

**12.6 Git workflow integration** — Tasks producing code start with "Follow the `Git workflow`" (step 1.1). First step is "Create an issue" with `[Task] <title>` format. Last step is PR or issue comment.

**12.7 Acceptance criteria** — Every task ends with `## Acceptance criteria`. Criteria are concrete, binary, verifiable. Use `- [ ]` checkboxes. Good examples: "All tests pass", "PR is merged", "Issue has correct title".

**12.8 Hints and solutions** — For debugging tasks, provide collapsible `<details>` hints/solutions.

**12.9 Expected output** — After commands that produce output, show what the student should expect:

~~~markdown
2. The output should be similar to this:
   ```terminal
   <expected output>
   ```

~~~

**12.10 Notes explain "why"** — Use `> [!NOTE]` blocks inline to explain concepts without breaking step flow.

**12.11 Three kinds of task endings:**

- Code tasks → "Finish the task" (PR + review + merge). Criteria: PR approved, PR merged, tests pass.
- Non-code tasks → "Write a comment for the issue" (paste evidence, close issue). Criteria: correct title, comment exists.
- Auto-checked tasks → "Commit the deliverable file" (structured file checked by regex/script). Criteria: file exists, answers match format.

**12.12 Cross-task references** — Reference earlier task steps instead of repeating:

```markdown
1. [Run the web server](./task-1.md#8-run-the-web-server).
```

**12.14 Placeholder-based implementation templates** — Provide commented-out placeholder templates in the seed project. Students uncomment the code and replace placeholders with correct values, using an existing reference implementation as a guide.

Key rules:

- Placeholders use `<angle_brackets>` to indicate values students must fill in.
- Each placeholder template includes a `# Reference:` comment mapping the new resource to its reference counterpart.
- The reference implementation (e.g., `items` endpoint) must be fully working so students can study it.
- Each placeholder template should be a separate commit when implemented.

**12.15 Seed project design** — Design the starting codebase with three tiers of completeness:

1. **Fully implemented (reference):** One resource is complete and working. Students study it to understand the pattern. Example: `items` endpoints with all CRUD operations.
2. **Commented out with bugs (debug):** Code exists but is disabled. Students uncomment it, discover it fails, and debug. Example: `interactions` endpoint with a schema–database mismatch.
3. **Placeholder templates (implement):** Commented-out code with `<placeholders>` that students fill in by following the reference. Example: `learners` endpoint with `<method>`, `<resource_name>`, `<resource_schema>`.

For each tier, both the route code and its router registration (e.g., `app.include_router(...)`) must be in the same state — commented out or active. Students uncomment both to enable the route.

**12.16 Holistic task design** — Combine related concerns into a single task when they share the same learning objective. A debugging task should include everything needed to understand the failure: reading code, examining the database, and fixing the bug — not three separate tasks.

Separate concerns into different tasks only when they produce fundamentally different artifacts or teach distinct skills. Example: API exploration via Swagger (produces a questionnaire) and database exploration via PgAdmin (produces a bug fix) belong in different tasks even though both involve the same system.

**12.17 LLM-independence** — Tasks must be completable without LLMs. Provide templates, examples, and fallback methods.

**12.18 Multi-bug debugging tasks** — Include bugs at different layers (schema, DB, logic). Structure so first fix unblocks and reveals the next bug.

## 15. Testing pattern

- Include a `tests/` directory; use the project's test runner (`pytest`, `jest`, `go test`, etc.).
- At least one test should **intentionally fail** so students practice debugging.
- After the run command, show the expected failing output and guide students through reading it step-by-step. Break the failure message into its components:

  ```markdown
  1. Look at the test summary.
  2. You should see `FAILED <test-file>::<test-name> - assert <actual> == <expected>`.

     This line means the following:
     - The test failed (`FAILED`).
     - The test is in the file `<test-file>`.
     - The name of the failing test is `<test-name>`.
     - The assert that failed is `<actual> == <expected>`.
  ```

- Acceptance criteria must include "All tests pass."
- **Vary bug types across the request path.** Place bugs at different layers (e.g., schema–database mismatch at the data layer, logic error at the processing layer). Teaches students to trace failures across the full stack, not just look for one kind of mistake.

## Pre-publish checklist

See `instructors/context/lab-conventions/conventions-lab.md` §17.
