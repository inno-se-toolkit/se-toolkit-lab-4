# Lab creation conventions

- [1. Repository structure](#1-repository-structure)
- [2. `README.md` — Main entry point](#2-readmemd--main-entry-point)
  - [Key rules for `README.md`](#key-rules-for-readmemd)
- [5. `lab/setup.md` — Lab setup](#5-labsetupmd--lab-setup)
  - [Key rules for setup](#key-rules-for-setup)
- [6. `wiki/git-workflow.md` — Reusable Git workflow](#6-wikigit-workflowmd--reusable-git-workflow)
  - [Key rules for git workflow](#key-rules-for-git-workflow)
- [8. GitHub templates](#8-github-templates)
  - [Issue templates](#issue-templates)
    - [`01-task.yml` — Lab Task](#01-taskyml--lab-task)
    - [`02-bug-report.yml` — Bug Report](#02-bug-reportyml--bug-report)
    - [`config.yml`](#configyml)
  - [PR template (`pull_request_template.md`)](#pr-template-pull_request_templatemd)
- [9. VS Code settings (`.vscode/settings.json`)](#9-vs-code-settings-vscodesettingsjson)
- [10. VS Code recommended extensions (`.vscode/extensions.json`)](#10-vs-code-recommended-extensions-vscodeextensionsjson)
  - [Rules for extensions](#rules-for-extensions)
- [11. Task runner and package manager config](#11-task-runner-and-package-manager-config)
  - [Rules for task runner](#rules-for-task-runner)
- [13. Lab story and narrative](#13-lab-story-and-narrative)
- [14. Docker and deployment pattern](#14-docker-and-deployment-pattern)
- [16. `CONTRIBUTORS.md` pattern](#16-contributorsmd-pattern)
- [17. Checklist before publishing](#17-checklist-before-publishing)
- [18. Security integration pattern](#18-security-integration-pattern)
- [19. Database naming conventions](#19-database-naming-conventions)

Use this file when creating or restructuring a lab repository.

## 1. Repository structure

Create the following directory and file layout. Items marked *(conditional)* are included only when the lab needs them.

```text
<repo-root>/
├── README.md                          # Main entry point
├── CONTRIBUTING.md                    # Docs style guide (reuse as-is)
├── CONTRIBUTORS.md                    # List of student contributors
├── lab/
│   ├── setup.md                       # Lab setup instructions
│   ├── tasks/
│   │   ├── git-workflow.md            # Reusable Git workflow procedure
│   │   ├── required/
│   │   │   ├── task-1.md
│   │   │   ├── task-2.md
│   │   │   └── ...
│   │   └── optional/
│   │       ├── task-1.md
│   │       └── ...
│   ├── wiki/                      # Reference docs for tools & concepts
│   │   ├── vs-code.md
│   │   ├── git.md
│   │   ├── git-vscode.md
│   │   ├── github.md
│   │   ├── shell.md
│   │   └── ...                        # One file per tool/concept
│   ├── design/                        # Internal design notes (not student-facing)
│   │   ├── lab-plan.md
│   │   ├── feedback.md
│   │   ├── formatting.md
│   │   └── todo.md
│   └── images/                        # Screenshots and diagrams
│       ├── wiki/
│       │   ├── vs-code/
│       │   ├── gitlens/
│       │   └── ...
│       └── git-workflow.drawio.svg
├── .github/
│   ├── ISSUE_TEMPLATE/
│   │   ├── 01-task.yml                # Lab Task issue form
│   │   ├── 02-bug-report.yml          # Bug Report issue form
│   │   └── config.yml                 # blank_issues_enabled: false
│   ├── pull_request_template.md       # PR template with checklist
│   └── workflows/                     # GitHub Actions (optional)
├── .vscode/
│   ├── settings.json                  # Editor, formatter, ToC settings
│   └── extensions.json                # Recommended VS Code extensions
├── src/                               # Application source code (conditional)
├── tests/                             # Test suite (conditional)
├── .gitignore
├── .env.example                       # Template for local env vars (conditional)
├── .env.docker.example                # Template for Docker env vars (conditional)
├── .dockerignore                      # (conditional — only if using Docker)
├── Dockerfile                         # (conditional — only if using Docker)
├── docker-compose.yml                 # (conditional — only if using Docker)
└── <package-manager-config>           # e.g., pyproject.toml, package.json
```

----

## 2. `README.md` — Main entry point

Structure the `README.md` exactly as follows:

```markdown
# Lab <N> — <Short title summarizing the lab>

<h2>Table of contents</h2>

- [Lab story](#lab-story)
- [Learning advice](#learning-advice)
- [Learning outcomes](#learning-outcomes)
- [Tasks](#tasks)
  - [Prerequisites](#prerequisites)
  - [Required](#required)
  - [Optional](#optional)

## Lab story

<!-- A narrative scenario that gives students a realistic context.
     Example: "You were hired by a company that develops a novel e-learning system." -->

## Learning advice

Read the tasks and complete them by yourself.

When stuck or not sure, ask an LLM:

> Give me directions on how to solve this task. I want to maximize learning.

> Why is this task important? What exactly do I need to do?

Provide enough context by giving it the whole file, not one or two lines.

Remember: Use the LLM to enhance your understanding, not replace it.

Evaluate LLM answers critically, and verify them against credible sources such as official documentation, course materials, and what you observe in reality.

## Learning outcomes

By the end of this lab, you should be able to:

- <Outcome 1>
- <Outcome 2>
- ...

In simple words, you should be able to say:
>
> 1. <Simple statement 1>
> 2. <Simple statement 2>
> ...

## Tasks

### Prerequisites

1. [Lab setup](./lab/setup.md).

### Required

1. [<Task 1 title>](./lab/tasks/required/task-1.md)
2. [<Task 2 title>](./lab/tasks/required/task-2.md)
...

### Optional

1. [<Optional task 1 title>](./lab/tasks/optional/task-1.md)
...
```

### Key rules for `README.md`

- The `<h2>Table of contents</h2>` uses an HTML tag so it doesn't appear in its own ToC.
- The ToC is generated by the `Markdown All in One` VS Code extension.
- Learning outcomes are a bullet list of concrete, observable skills.
- The "In simple words" block restates outcomes as first-person statements.
- Required tasks build on each other sequentially.
- Optional tasks are independent extensions.

----

## 5. `lab/setup.md` — Lab setup

Structure:

```markdown
# Lab setup

- [Steps](#steps)
  - [1. Find a partner](#1-find-a-partner)
  - [2. <Setup step>](#2-setup-step)
  - ...
- [Optional steps](#optional-steps)
  - [1. <Optional setup>](#1-optional-setup)
  - ...

## Steps

### 1. Find a partner

1. Find a partner for this lab.
2. Sit next to them.

> [!IMPORTANT]
> You work on tasks independently from your partner.
>
> You and your partner work together when reviewing each other's work.

### 2. <Setup step>
...

----

## Optional steps

These enhancements can make your life easier:

- [1. <Enhancement>](#1-enhancement)
- ...
```

### Key rules for setup

- Setup is the prerequisite for all tasks.
- Includes: forking the repo, cloning, installing tools, configuring the environment.
- Separate required steps from optional enhancements with `---`.
- Partner setup is always step 1 (students review each other's PRs).
- Each step links to wiki docs for detailed instructions.

----

## 6. `wiki/git-workflow.md` — Reusable Git workflow

This file describes the workflow students follow for every task that produces code changes:

```text
Issue → Branch → Commits → PR → Review → Merge
```

Structure:

```markdown
# `Git workflow` for tasks

> [!NOTE]
> This procedure is based on the [`GitHub flow`](../../wiki/github.md#github-flow).

Outline:

- [Create a `Lab Task` issue](#create-a-lab-task-issue)
- [Switch to the `main` branch](#switch-to-the-main-branch)
- [Switch to a new branch](#switch-to-a-new-branch)
- [Edit files](#edit-files)
- [Commit](#commit)
- [Publish the branch](#publish-the-branch)
- [Create a PR to `main` in your fork](#create-a-pr-to-main-in-your-fork)
- [Get a PR review](#get-a-pr-review)
- [Merge the PR](#merge-the-pr)
- [Clean up](#clean-up)
```

### Key rules for git workflow

- Every section links to the relevant wiki doc for the detailed how-to.
- Task documents reference this file via `` [`Git workflow`](../git-workflow.md) ``.
- The workflow is fork-based: students fork the course repo, work in branches, create PRs to their own fork's `main`.
- PR review rules are included: reviewer checks acceptance criteria, leaves comments, approves.

----

## 8. GitHub templates

> The templates below are the canonical starting point. The actual files in `.github/` may include lab-specific additions.

### Issue templates

#### `01-task.yml` — Lab Task

```yaml
name: Lab Task
description: Track work for a specific lab task
title: "[Task] <short title>"
labels: ["task"]
body:
  - type: textarea
    id: description
    attributes:
      label: Description
      description: Summarize what this task is about in your own words.
      placeholder: |
        Make X work with Y ...
    validations:
      required: true
  - type: textarea
    id: steps
    attributes:
      label: Plan
      description: What do you plan to do to complete this task?
      placeholder: |
        - [ ] Step 1
        - [ ] Step 2
        ...
    validations:
      required: true
```

#### `02-bug-report.yml` — Bug Report

Same structure as `01-task.yml`. Required fields:

- `Brief problem description`
- `Steps to Reproduce`
- `Expected Result`
- `Actual Result`

#### `config.yml`

```yaml
blank_issues_enabled: false
```

### PR template (`pull_request_template.md`)

```markdown
## Summary

- Closes #<issue-number>

----

## Checklist

- [ ] I made this PR to the `main` branch **of my fork (NOT the course instructors' repo)**.
- [ ] I see `base: main` <- `compare: <branch-name>` above the PR title.
- [ ] I edited the line `- Closes #<issue-number>`.
- [ ] I wrote clear commit messages.
- [ ] I reviewed my own diff before requesting review.
- [ ] I understand the changes I'm submitting.
```

----

## 9. VS Code settings (`.vscode/settings.json`)

> The template below is the canonical starting point. The actual file in `.vscode/` may include lab-specific additions.

```json
{
  "git.autofetch": true,
  "files.autoSave": "afterDelay",
  "files.autoSaveDelay": 500,
  "editor.formatOnSave": true,
  "[markdown]": {
    "editor.defaultFormatter": "DavidAnson.vscode-markdownlint"
  },
  "markdown.extension.toc.levels": "2..6",
  "workbench.sideBar.location": "right",
  "markdown.preview.scrollEditorWithPreview": false,
  "markdown.preview.scrollPreviewWithEditor": false
}
```

Add language-specific formatter settings as needed (e.g., Python with Ruff, JS with Prettier).

----

## 10. VS Code recommended extensions (`.vscode/extensions.json`)

> The template below is the canonical starting point. The actual file in `.vscode/` may include lab-specific additions.

Provide a curated list of recommended extensions so students can install them all at once:

```json
{
  "recommendations": [
    // Language support (adjust per lab): Python, Node.js, Go, Rust, etc.

    // Git
    "eamodio.gitlens",

    // Remote development (if lab uses SSH/VMs/containers)
    "ms-vscode-remote.remote-ssh",

    // Markdown authoring and preview
    "DavidAnson.vscode-markdownlint",
    "yzhang.markdown-all-in-one",

    // GitHub integration
    "github.vscode-pull-request-github",

    // File format support (include what the lab uses)
    "tamasfe.even-better-toml",

    // Useful utilities
    "usernamehw.errorlens",
    "gruntfuggly.todo-tree",
    "ms-vsliveshare.vsliveshare"
  ]
}
```

### Rules for extensions

- Group extensions by purpose with `//` comments.
- Include extensions for: the lab's programming language, Git, remote development, Markdown, GitHub, and relevant file formats.
- The setup doc instructs students to install these via `Extensions` > `Filter` > `Recommended` > `Install Workspace Recommended extensions`.

----

## 11. Task runner and package manager config

Define common project commands using a task runner so students run simple commands rather than remembering complex CLI invocations.

Choose a task runner appropriate for the lab's ecosystem:

- **Python**: `pyproject.toml` + [`poethepoet`](https://poethepoet.natn.io/) (run via `uv run poe <task>`)
- **Node.js**: `package.json` scripts (run via `npm run <task>`)
- **Go / Rust / other**: `Makefile` or `Taskfile.yml` (run via `make <task>` or `task <task>`)

Example with `pyproject.toml` + `poethepoet`:

```toml
[tool.poe.tasks.dev]
help = "Run server after static analysis"
sequence = ["check", "start"]

[tool.poe.tasks.test]
help = "Run pytest"
cmd = "pytest"
```

Example with `package.json`:

```json
{
  "scripts": {
    "dev": "npm run check && npm run start",
    "start": "node src/index.js",
    "check": "npm run format && npm run lint",
    "test": "jest"
  }
}
```

### Rules for task runner

- Students run a single short command (e.g., `uv run poe dev`, `npm run dev`) — no need to memorize raw commands.
- Document task runner commands in `> [!NOTE]` blocks the first time they appear:

  ```markdown
  > [!NOTE]
  > `<runner>` can run tasks specified in the `<config-file>`.
  ```

----

## 13. Lab story and narrative

- Frame the lab as a realistic work scenario (e.g., "You were hired by a company...", "Your team was asked to...").
- Introduce a senior engineer (or team lead) giving the assignment.
- Use blockquotes for the senior engineer's words. The quoted tasks should mirror the actual required tasks:

  ```markdown
  A senior engineer explains your first assignment:

  > 1. <High-level description of task 1>.
  > 2. <High-level description of task 2>.
  > 3. <High-level description of task 3>.
  > ...

  > [!IMPORTANT]
  > Communicate through issues and PRs and deliver <the expected outcome>.
  ```

- The story should make the tasks feel purposeful, not academic.
- Adapt the scenario to the lab's domain (web development, data processing, CLI tools, infrastructure, etc.).
- **Cross-lab continuity:** When a course has multiple labs, keep one product across labs and grow the data model incrementally. Example: Lab 2 deploys the service, Lab 3 adds endpoints and security, Lab 4 adds outcomes and verification. Each lab picks up where the previous one left off. This gives students a sense of building something real over time.

----

## 14. Docker and deployment pattern

> Include this section only if the lab involves containerization or remote deployment. Omit the Docker/deployment files from the repository structure if not needed.

If the lab involves deployment:

1. Provide `.env.example` and `.env.docker.example` as templates.
2. Students copy them to `.env.secret` and `.env.docker.secret` (which are `.gitignore`d via the `*.secret` pattern in `.gitignore`).
3. Use `docker-compose.yml` with environment variable substitution from the `.env.docker.secret` file:

   ```yaml
   services:
     app:
       build: .
       ports:
         - ${APP_HOST_ADDRESS}:${APP_HOST_PORT}:${APP_CONTAINER_PORT}
       environment:
         - PORT=${APP_CONTAINER_PORT}
     caddy:
       image: caddy:2-alpine
       depends_on:
         - app
       ports:
         - ${CADDY_HOST_ADDRESS}:${CADDY_HOST_PORT}:${CADDY_CONTAINER_PORT}
       volumes:
         - ./caddy/Caddyfile:/etc/caddy/Caddyfile
   ```

4. Include a reverse proxy service (e.g., Caddy) in `docker-compose.yml`.
5. Use a multi-stage `Dockerfile` for production builds (builder stage + slim runtime).
6. Deployment task flow: SSH into VM → clone repo → create `.env.docker.secret` → `docker compose up --build -d`.
7. Distinguish local vs remote env differences:
   - Local: `APP_HOST_ADDRESS=127.0.0.1` (localhost only).
   - Remote: `CADDY_HOST_ADDRESS=0.0.0.0` (accessible from outside).
8. **Use an institutional container registry** (e.g., Harbor cache proxy) for base images to avoid Docker Hub rate limits ("too many requests" errors). Reference the registry in `docker-compose.yml` image fields instead of pulling directly from Docker Hub.

----

## 16. `CONTRIBUTORS.md` pattern

Include a `CONTRIBUTORS.md` file where students add their GitHub username via a PR:

```markdown
# Contributors

Students who contributed changes to this repository:

<!--
johndoe is an example of a GitHub username.

Replace @johndoe with @<your-username> where
<your-username> is your GitHub username.
-->

- @johndoe
```

----

## 17. Checklist before publishing

**Always required:**

- [ ] `README.md` has: story, learning advice, learning outcomes, task list.
- [ ] Every task file has: Time, Purpose, Context, ToC, Steps, Acceptance criteria.
- [ ] Every terminal command has a `` [Run using the `VS Code Terminal`] `` link prefix.
- [ ] Every Command Palette command has a `` [Run using the `Command Palette`] `` link prefix.
- [ ] All cross-references use relative paths and are valid.
- [ ] Wiki docs exist for every tool/concept linked from tasks.
- [ ] Issue templates (`01-task.yml`, `02-bug-report.yml`) are configured.
- [ ] PR template has a checklist.
- [ ] `.vscode/settings.json` and `.vscode/extensions.json` are configured.
- [ ] `.gitignore` excludes generated files and secrets for the lab's ecosystem.
- [ ] Ordered lists use `1. 2. 3.` (not `1. 1. 1.`).
- [ ] Compound instructions are split into separate steps.
- [ ] All sentences end with `.`.
- [ ] Options and steps are clearly differentiated.
- [ ] Tool/concept names are wrapped in backticks: `` `VS Code` ``, `` `Git` ``, `` `Docker` ``.
- [ ] `Git workflow` is referenced from tasks that produce code changes.
- [ ] Acceptance criteria are concrete and verifiable.
- [ ] Commit message format is documented (conventional commits).
- [ ] Setup instructions cover: fork, clone, install tools, configure environment.
- [ ] Branch protection rules are documented.
- [ ] Partner/collaborator setup is documented.
- [ ] `CONTRIBUTORS.md` exists with placeholder entry.
- [ ] Diagrams use `.drawio.svg` format.
- [ ] `<!-- TODO -->` markers exist for unfinished sections.

**Conditional (include when applicable):**

- [ ] `.env.example` files are provided; `.env.secret` files are gitignored (if the lab uses environment variables).
- [ ] `.dockerignore` excludes tests, docs, `.git/`, build caches, markdown files (if the lab uses Docker).
- [ ] At least one test intentionally fails for the debugging task (if the lab has a testing/debugging task).
- [ ] Task runner commands are documented in the config file (if the lab uses a task runner).
- [ ] Seed project has three tiers: reference (working), debug (commented out with bugs), implement (placeholder templates) (if the lab uses the seed project pattern).
- [ ] Placeholder templates include `# Reference:` comments mapping new resources to reference counterparts (if the lab uses placeholder-based implementation).
- [ ] All tasks are completable without LLMs.
- [ ] Docker images use an institutional container registry (if the lab uses Docker in an institutional setting).
- [ ] API key or auth mechanism is set via environment variable and encountered naturally during exploration (if the lab includes security).

----

## 18. Security integration pattern

> Include this section only if the lab involves API authentication or server hardening. Omit for labs without security concerns.

Introduce security as something students encounter naturally, not as a standalone lecture:

1. **Simple API key via environment variable.** Use one shared key set via an `API_TOKEN` (or similar) environment variable. No user accounts, no roles, no permissions matrix. Students discover the mechanism when they try an endpoint and get `401 Unauthorized`.
2. **Natural discovery.** Place the API key requirement on endpoints students will use in the exploration task. They encounter auth organically rather than being told about it in isolation.
3. **Environment-based configuration.** The key lives in `.env.secret` (local) and `.env.docker.secret` (Docker/deployment). Students learn to set different keys per environment.
4. **Server hardening (optional advanced task).** For deployment labs, consider including VM hardening as a separate task: non-root SSH user, firewall (`ufw`), `fail2ban`, disable root login and password authentication. This is infrastructure security, distinct from application-level auth.

----

## 19. Database naming conventions

Only include when the lab has a relational database layer.

Name tables according to their role in the schema:

- **Entity tables** — singular noun (e.g., `learner`, `item`).
- **Relationship tables** — verb (e.g., `interacts`).

| Role         | Convention    | Example           |
| ------------ | ------------- | ----------------- |
| Entity       | singular noun | `learner`, `item` |
| Relationship | verb          | `interacts`       |
