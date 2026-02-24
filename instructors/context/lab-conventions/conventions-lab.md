# Lab creation conventions

- [1. Repository structure](#1-repository-structure)
- [2. `README.md`](#2-readmemd)
- [5. `lab/setup.md`](#5-labsetupmd)
- [6. `lab/tasks/git-workflow.md`](#6-labtasksgit-workflowmd)
- [8. GitHub templates](#8-github-templates)
  - [`01-task.yml` — Lab Task](#01-taskyml--lab-task)
  - [`02-bug-report.yml` — Bug Report](#02-bug-reportyml--bug-report)
  - [`config.yml`](#configyml)
  - [`pull_request_template.md`](#pull_request_templatemd)
- [9. `.vscode/settings.json`](#9-vscodesettingsjson)
- [10. `.vscode/extensions.json`](#10-vscodeextensionsjson)
- [11. Task runner config](#11-task-runner-config)
- [13. Lab story and narrative](#13-lab-story-and-narrative)
- [14. Docker and deployment pattern](#14-docker-and-deployment-pattern)
- [16. `CONTRIBUTORS.md`](#16-contributorsmd)
- [17. Checklist before publishing](#17-checklist-before-publishing)
- [18. Security integration pattern](#18-security-integration-pattern)
- [19. Database naming conventions](#19-database-naming-conventions)

Full source: `instructors/context/lab-conventions/lab-conventions.md` §1, §2, §5, §6, §8–11, §13–14, §16–19

Use this file when creating or restructuring a lab repository.

## 1. Repository structure

```text
<repo-root>/
├── README.md
├── CONTRIBUTING.md
├── CONTRIBUTORS.md
├── lab/
│   ├── setup.md
│   ├── tasks/
│   │   ├── git-workflow.md
│   │   ├── required/
│   │   │   ├── task-1.md
│   │   │   └── ...
│   │   └── optional/
│   │       └── ...
│   ├── wiki/
│   │   ├── vs-code.md
│   │   ├── git.md
│   │   └── ...
│   ├── design/                    # Internal (not student-facing)
│   │   ├── lab-plan.md
│   │   ├── feedback.md
│   │   └── todo.md
│   └── images/
│       ├── wiki/
│       └── git-workflow.drawio.svg
├── .github/
│   ├── ISSUE_TEMPLATE/
│   │   ├── 01-task.yml
│   │   ├── 02-bug-report.yml
│   │   └── config.yml
│   ├── pull_request_template.md
│   └── workflows/                 # (conditional)
├── .vscode/
│   ├── settings.json
│   └── extensions.json
├── src/                           # (conditional)
├── tests/                         # (conditional)
├── .gitignore
├── .env.example                   # (conditional)
├── .env.docker.example            # (conditional)
├── .dockerignore                  # (conditional)
├── Dockerfile                     # (conditional)
├── docker-compose.yml             # (conditional)
└── <package-manager-config>
```

## 2. `README.md`

```markdown
# Lab <N> — <Short title>

<h2>Table of contents</h2>

- [Lab story](#lab-story)
- [Learning advice](#learning-advice)
- [Learning outcomes](#learning-outcomes)
- [Tasks](#tasks)
  - [Prerequisites](#prerequisites)
  - [Required](#required)
  - [Optional](#optional)

## Lab story

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

In simple words, you should be able to say:
>
> 1. <Simple statement 1>

## Tasks

### Prerequisites

1. [Lab setup](./lab/setup.md).

### Required

1. [<Task 1 title>](./lab/tasks/required/task-1.md)

### Optional

1. [<Optional task 1 title>](./lab/tasks/optional/task-1.md)
```

Key rules:

- `<h2>Table of contents</h2>` uses an HTML tag so it doesn't appear in its own ToC.
- Learning outcomes are a bullet list of concrete, observable skills.
- The "In simple words" block restates outcomes as first-person statements.
- Required tasks build sequentially; optional tasks are independent.

## 5. `lab/setup.md`

```markdown
# Lab setup

- [Steps](#steps)
  - [1. Find a partner](#1-find-a-partner)
  - [2. <Setup step>](#2-setup-step)
- [Optional steps](#optional-steps)

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
```

Key rules:

- Step 1 is always "Find a partner" (students review each other's PRs).
- Includes: forking the repo, cloning, installing tools, configuring the environment.
- Separate required steps from optional enhancements with `----`.
- Each step links to wiki docs for detailed instructions.

## 6. `lab/tasks/git-workflow.md`

Outline (every section links to the relevant wiki doc):

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

Key rules:

- The workflow is fork-based: students fork the course repo, work in branches, create PRs to their own fork's `main`.
- Task documents reference this file via `` [`Git workflow`](../git-workflow.md) ``.
- PR review rules are included: reviewer checks acceptance criteria, leaves comments, approves.

## 8. GitHub templates

### `01-task.yml` — Lab Task

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
    validations:
      required: true
```

### `02-bug-report.yml` — Bug Report

Same structure as `01-task.yml`. Required fields: `Brief problem description`, `Steps to Reproduce`, `Expected Result`, `Actual Result`.

### `config.yml`

```yaml
blank_issues_enabled: false
```

### `pull_request_template.md`

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

## 9. `.vscode/settings.json`

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

## 10. `.vscode/extensions.json`

```json
{
  "recommendations": [
    // Language support (adjust per lab)

    // Git
    "eamodio.gitlens",

    // Remote development (if lab uses SSH/VMs/containers)
    "ms-vscode-remote.remote-ssh",

    // Markdown
    "DavidAnson.vscode-markdownlint",
    "yzhang.markdown-all-in-one",

    // GitHub integration
    "github.vscode-pull-request-github",

    // File format support
    "tamasfe.even-better-toml",

    // Utilities
    "usernamehw.errorlens",
    "gruntfuggly.todo-tree",
    "ms-vsliveshare.vsliveshare"
  ]
}
```

Key rules:

- Group extensions by purpose with `//` comments.
- Setup doc instructs students to install via `Extensions` > `Filter` > `Recommended` > `Install Workspace Recommended extensions`.

## 11. Task runner config

Choose a task runner for the lab's ecosystem:

- **Python:** `pyproject.toml` + `poethepoet` → `uv run poe <task>`
- **Node.js:** `package.json` scripts → `npm run <task>`
- **Go / Rust / other:** `Makefile` or `Taskfile.yml` → `make <task>` or `task <task>`

Key rules:

- Students run one short command — no raw CLI invocations to memorize.
- Document task runner commands in `> [!NOTE]` blocks on first use:

  ```markdown
  > [!NOTE]
  > `<runner>` can run tasks specified in the `<config-file>`.
  ```

## 13. Lab story and narrative

- Frame the lab as a realistic work scenario ("You were hired by a company...", "Your team was asked to...").
- Introduce a senior engineer giving the assignment. Use blockquotes for their words:

  ```markdown
  A senior engineer explains your first assignment:

  > 1. <High-level description of task 1>.
  > 2. <High-level description of task 2>.

  > [!IMPORTANT]
  > Communicate through issues and PRs and deliver <the expected outcome>.
  ```

- The quoted tasks should mirror the actual required tasks.
- **Cross-lab continuity:** Keep one product across multiple labs, growing the data model incrementally. Each lab picks up where the previous one left off.

## 14. Docker and deployment pattern

Only include when the lab involves containerization or remote deployment.

1. Provide `.env.example` and `.env.docker.example` as templates.
2. Students copy them to `.env.secret` and `.env.docker.secret` (gitignored via `*.secret`).
3. Use `docker-compose.yml` with environment variable substitution from `.env.docker.secret`.
4. Include a reverse proxy service (e.g., Caddy) in `docker-compose.yml`.
5. Use a multi-stage `Dockerfile` (builder stage + slim runtime).
6. Deployment flow: SSH into VM → clone repo → create `.env.docker.secret` → `docker compose up --build -d`.
7. Distinguish local vs remote: local uses `APP_HOST_ADDRESS=127.0.0.1`; remote uses `CADDY_HOST_ADDRESS=0.0.0.0`.
8. Use an institutional container registry for base images to avoid Docker Hub rate limits.

## 16. `CONTRIBUTORS.md`

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

Students add their GitHub username via a PR.

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
- [ ] All sentences end with `.`
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

- [ ] `.env.example` files are provided; `.env.secret` files are gitignored.
- [ ] `.dockerignore` excludes tests, docs, `.git/`, build caches, markdown files.
- [ ] At least one test intentionally fails for the debugging task.
- [ ] Task runner commands are documented in the config file.
- [ ] Seed project has three tiers: reference (working), debug (commented out with bugs), implement (placeholder templates).
- [ ] Placeholder templates include `# Reference:` comments.
- [ ] All tasks are completable without LLMs.
- [ ] Docker images use an institutional container registry.
- [ ] API key or auth mechanism is set via environment variable and encountered naturally during exploration.

## 18. Security integration pattern

Only include when the lab involves API authentication or server hardening.

1. **Simple API key via environment variable.** One shared key in `API_TOKEN` (or similar). No user accounts or roles. Students encounter `401 Unauthorized` naturally during exploration.
2. **Natural discovery.** Place the API key requirement on endpoints students use in the exploration task. Auth is discovered organically, not announced upfront.
3. **Environment-based configuration.** Key lives in `.env.secret` (local) and `.env.docker.secret` (Docker). Students learn to set different keys per environment.
4. **Server hardening (optional advanced task).** For deployment labs: non-root SSH user, firewall (`ufw`), `fail2ban`, disable root login and password authentication.

## 19. Database naming conventions

Only include when the lab has a relational database layer.

Name tables according to their role in the schema:

- **Entity tables** — singular noun (e.g., `learner`, `item`).
- **Relationship tables** — verb (e.g., `interacts`).

| Role | Convention | Example |
|------|-----------|---------|
| Entity | singular noun | `learner`, `item` |
| Relationship | verb | `interacts` |
