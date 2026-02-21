# SE Toolkit lab conventions

- [1. Repository structure](#1-repository-structure)
- [2. `README.md` — Main entry point](#2-readmemd--main-entry-point)
  - [Key rules for `README.md`](#key-rules-for-readmemd)
- [3. Task document template](#3-task-document-template)
  - [Key rules for task documents](#key-rules-for-task-documents)
- [4. Writing conventions](#4-writing-conventions)
  - [4.1. Instructions wording](#41-instructions-wording)
  - [4.2. Terminal commands](#42-terminal-commands)
  - [4.3. Command Palette commands](#43-command-palette-commands)
  - [4.4. Options vs steps](#44-options-vs-steps)
  - [4.5. Ordered lists](#45-ordered-lists)
  - [4.6. Little ToC](#46-little-toc)
  - [4.7. Table of contents](#47-table-of-contents)
  - [4.8. Links and cross-references](#48-links-and-cross-references)
  - [4.9. Notes, tips, warnings](#49-notes-tips-warnings)
  - [4.10. Images](#410-images)
  - [4.11. Collapsible hints and solutions](#411-collapsible-hints-and-solutions)
  - [4.12. Commit message format](#412-commit-message-format)
  - [4.13. Diagrams](#413-diagrams)
  - [4.14. `<!-- TODO -->` comments](#414----todo----comments)
  - [4.15. `<!-- no toc -->` comments](#415----no-toc----comments)
  - [4.16. Code snippets in explanations](#416-code-snippets-in-explanations)
  - [4.17. Heading levels in section titles](#417-heading-levels-in-section-titles)
  - [4.18. Inline formatting of technical terms](#418-inline-formatting-of-technical-terms)
  - [4.19. Steps with sub-steps](#419-steps-with-sub-steps)
  - [4.20. Placeholders in docs](#420-placeholders-in-docs)
- [5. `lab/setup.md` — Lab setup](#5-labsetupmd--lab-setup)
  - [Key rules for setup](#key-rules-for-setup)
- [6. `lab/tasks/git-workflow.md` — Reusable Git workflow](#6-labtasksgit-workflowmd--reusable-git-workflow)
  - [Key rules for git workflow](#key-rules-for-git-workflow)
- [7. Appendix documents (`lab/appendix/`)](#7-appendix-documents-labappendix)
  - [Purpose](#purpose)
  - [Naming](#naming)
  - [Structure of an appendix file](#structure-of-an-appendix-file)
  - [Key rules](#key-rules)
  - [Standard appendix topics to include](#standard-appendix-topics-to-include)
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
- [12. Task design principles](#12-task-design-principles)
  - [12.1. Progressive complexity](#121-progressive-complexity)
  - [12.2. Every task teaches something](#122-every-task-teaches-something)
  - [12.3. High-level instructions with low-level fallbacks](#123-high-level-instructions-with-low-level-fallbacks)
  - [12.4. Provide fallback methods](#124-provide-fallback-methods)
  - [12.5. Localize instructions](#125-localize-instructions)
  - [12.6. Git workflow integration](#126-git-workflow-integration)
  - [12.7. Acceptance criteria](#127-acceptance-criteria)
  - [12.8. Hints and solutions](#128-hints-and-solutions)
  - [12.9. Expected output](#129-expected-output)
  - [12.10. Notes explain "why"](#1210-notes-explain-why)
  - [12.11. Three kinds of task endings](#1211-three-kinds-of-task-endings)
  - [12.12. Cross-task references](#1212-cross-task-references)
  - [12.13. Appendix section structure pattern](#1213-appendix-section-structure-pattern)
  - [12.14. Placeholder-based implementation templates](#1214-placeholder-based-implementation-templates)
  - [12.15. Seed project design](#1215-seed-project-design)
  - [12.16. Holistic task design](#1216-holistic-task-design)
  - [12.17. LLM-independence](#1217-llm-independence)
  - [12.18. Multi-bug debugging tasks](#1218-multi-bug-debugging-tasks)
- [13. Lab story and narrative](#13-lab-story-and-narrative)
- [14. Docker and deployment pattern](#14-docker-and-deployment-pattern)
- [15. Testing pattern](#15-testing-pattern)
- [16. `CONTRIBUTORS.md` pattern](#16-contributorsmd-pattern)
- [17. Checklist before publishing](#17-checklist-before-publishing)
- [18. Security integration pattern](#18-security-integration-pattern)

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
│   ├── appendix/                      # Reference docs for tools & concepts
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
│       ├── appendix/
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

## 3. Task document template

Every task file (`task-N.md`) must follow this structure:

```markdown
# <Task title>

<h4>Time</h4>

~<estimate> min

<h4>Purpose</h4>

<One sentence: what the student will learn.>

<h4>Context</h4>

<1–3 sentences: why this task matters and what background the student needs.>

<h4>Table of contents</h4>

- [Steps](#steps)
  - [0. Follow the `Git workflow`](#0-follow-the-git-workflow)
  - [1. Create an issue](#1-create-an-issue)
  - [2. <Step title>](#2-step-title)
  - ...
- [Acceptance criteria](#acceptance-criteria)

## Steps

### 0. Follow the `Git workflow`

Follow the [`Git workflow`](../git-workflow.md) to complete this task.

### 1. Create a `Lab Task` issue

Title: `[Task] <Task title>`

### 2. <Step title>

<Step-by-step instructions>

### ...

### N. Finish the task

1. [Create a PR](../git-workflow.md#create-a-pr) with your changes.
2. [Get a PR review](../git-workflow.md#get-a-pr-review) and complete the subsequent steps in the `Git workflow`.

----

## Acceptance criteria

- [ ] <Criterion 1>
- [ ] <Criterion 2>
- ...
```

### Key rules for task documents

- **Time, Purpose, Context, Table of contents** use `<h4>` HTML tags so they don't appear in the document's auto-generated ToC.
- **Step 0** ("Follow the Git workflow") is present in tasks that require a branch + PR. Omit for tasks that don't produce commits (e.g., "Run the web server").
- **Step 1** is always "Create an issue" (either a `Lab Task` or specific issue type).
- The **last step** is either "Finish the task" (create PR, get review) or "Write a comment for the issue" (close with evidence).
- **Acceptance criteria** use `- [ ]` checkboxes. Reviewers check them during PR review.
- Acceptance criteria are concrete and verifiable: issue titles, passing tests, merged PRs, specific comments.

----

## 4. Writing conventions

### 4.1. Instructions wording

| Action             | Wording                             |
| ------------------ | ----------------------------------- |
| Navigate somewhere | `Go to X.`                          |
| Click something    | `Click X.`                          |
| Choose an option   | `Use any of the following methods:` |
| Complete all steps | `Complete the following steps:`     |

- **Split compound instructions.** Never write "Do A and do B." Instead, split into two numbered steps.
- **Finish complete sentences with a `.`**

### 4.2. Terminal commands

Write each command for the `VS Code Terminal` in a multi-line code block with the type `terminal`. Always precede with a link to the appendix:

~~~markdown
1. [Run using the `VS Code Terminal`](../../appendix/vs-code.md#run-a-command-using-the-vs-code-terminal):

   ```terminal
   <command>
   ```
~~~

### 4.3. Command Palette commands

~~~markdown
1. [Run using the `Command Palette`](../../appendix/vs-code.md#run-a-command-using-the-command-palette):
   `<command>`
~~~

### 4.4. Options vs steps

Clearly differentiate:

- **Options:** "Use any of the following methods:" (then list methods)
- **Steps:** "Complete the following steps:" (then list steps in order)

### 4.5. Ordered lists

Each ordered list must use `1. 2. 3.`, **not** `1. 1. 1.`.

### 4.6. Little ToC

Provide a little table of contents when the list of options or steps is long:

```markdown
Use any of the following methods:

- [Method 1](#method-1)
- [Method 2](#method-2)

### Method 1

### Method 2
```

Don't provide a little ToC when all lists of items are short.

### 4.7. Table of contents

- Insert a ToC right after the document title.
- Use `Markdown All in One: Create Table of Contents` in VS Code.
- To skip a section from the ToC, use HTML tags for the title: `<h2>Heading</h2>`.
- To control which heading levels appear in the ToC, edit `"markdown.extension.toc.levels"` in [`.vscode/settings.json`](#9-vs-code-settings-vscodesettingsjson).

### 4.8. Links and cross-references

- Link to appendix sections whenever a concept or tool is mentioned for the first time in a section. Don't link when it's mentioned second time. This applies to both task docs and appendix docs. This ensures readers who jump to a specific section can still find relevant references.
- Appendix files can and should cross-reference other appendix files: `[concept name](./other-appendix.md#<section>)`.
- Use relative paths for all links.
- Provide a link to each file that exists in the repo.
- Link format for appendix references from tasks: `[concept name](../../appendix/<file>.md#<section>)`.
- Tasks can reference steps in other tasks: `[Run the web server](./task-1.md#8-run-the-web-server)`.
- **Compound phrases:** When a tool name and a concept naturally form a single phrase (e.g., `` `GitHub` pull request ``, `` `VS Code` Terminal ``), link the whole phrase to the concept's section rather than creating two adjacent links. Good: `` [`GitHub` pull request](./github.md#pull-request) ``. Bad: `` [`GitHub`](./github.md) [pull request](./github.md#pull-request) ``.

### 4.9. Notes, tips, warnings

Use GitHub-flavored Markdown alerts:

```markdown
> [!NOTE]
> Explanatory information.

> [!TIP]
> Helpful suggestion.

> [!IMPORTANT]
> Critical information.
```

- **Do not indent alerts.** GitHub-flavored Markdown alerts (`> [!NOTE]`, etc.) do not render correctly when indented (e.g., inside a list item). If you need an alert inside a list, restructure the content to place the alert at the top indentation level, or use bold text (e.g., **Note:**) as a fallback.

### 4.10. Images

Use HTML `<img>` tags with a `style` attribute for width control:

```markdown
<img alt="Description" src="../../images/appendix/vs-code/example.png" style="width:400px"></img>
```

### 4.11. Collapsible hints and solutions

Use `<details>` and `<summary>` for hints and solutions:

```markdown
1. <details><summary>Click to open a hint</summary>

   The hint text here.

   </details>

2. <details><summary>Click to open the solution</summary>

   The solution text here.

   </details>
```

### 4.12. Commit message format

Use [conventional commits](https://www.conventionalcommits.org/):

```text
<type>: <short description>

- <detail 1>
- <detail 2>
```

Common types:

- `fix:` — bug fixes
- `feat:` — new features or additions
- `docs:` — documentation changes

When a task specifies a commit message, provide it in a code block:

```markdown
   Use a multi-line message:

   \`\`\`text
   <type>: <short description>

   - <detail 1>
   - <detail 2>
   \`\`\`
```

### 4.13. Diagrams

- Use `.drawio.svg` format for editable diagrams (created with [draw.io](https://app.diagrams.net/)).
- Store diagrams in `lab/images/`.
- Reference them with standard Markdown image syntax: `![Alt text](../images/diagram.drawio.svg)`.

### 4.14. `<!-- TODO -->` comments

Use `<!-- TODO description -->` HTML comments for work-in-progress sections. These are invisible to students but trackable by authors using the `Todo Tree` VS Code extension.

### 4.15. `<!-- no toc -->` comments

Use `<!-- no toc -->` before a list to prevent `Markdown All in One` from including it in the auto-generated ToC:

```markdown
<!-- no toc -->
- [Method 1](#method-1)
- [Method 2](#method-2)
```

### 4.16. Code snippets in explanations

When walking students through code (e.g., debugging a bug), show the relevant code snippet in a fenced code block with the language specified:

~~~markdown
1. Look at the line where the `result` variable gets a value:

   ```<language>
   result = find_by_id(item_id, collection=data)
   ```

   The function `find_by_id` searches for an item in a given collection.
~~~

### 4.17. Heading levels in section titles

When asking to write particular sections in a file, provide file section headings in section titles:

```markdown

Create the file `docs.md` with the following sections:

1. [## Section 1](#-section-1)
2. [## Section 2](#-section-2)

## ## Section 1

## ## Section 2
```

### 4.18. Inline formatting of technical terms

Wrap tool names, technical terms, and acronyms in backticks: `` `VS Code` ``, `` `Git` ``, `` `Docker` ``, `` `Python` ``, `` `SQL` ``, `` `WSL` ``, `` `SSH` ``.

### 4.19. Steps with sub-steps

When multiple actions serve a single logical goal, group them under one step. Write the step as a complete sentence followed by "Complete the following steps:", then list the sub-steps as a nested ordered list:

```markdown
1. Configure the environment. Complete the following steps:
   1. Open `.env.example`.
   2. Copy it to `.env.secret`.
   3. Fill in the values.
```

When actions don't share a logical goal, flatten them into separate top-level steps (see [4.1. Instructions wording](#41-instructions-wording)).

### 4.20. Placeholders in docs

Use placeholders instead of hardcoded environment-specific values (e.g., URLs, ports from `.env`). This keeps docs accurate when students change their configuration.

Bad: `` Open <http://127.0.0.1:5050> in a browser. ``

Good: `` Open <pgadmin-url> in a browser. ``

Define every placeholder in `lab/appendix/placeholders.md`. Each placeholder gets its own section that links to its definition in the relevant appendix doc.

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
- Each step links to appendix docs for detailed instructions.

----

## 6. `lab/tasks/git-workflow.md` — Reusable Git workflow

This file describes the workflow students follow for every task that produces code changes:

```text
Issue → Branch → Commits → PR → Review → Merge
```

Structure:

```markdown
# `Git workflow` for tasks

> [!NOTE]
> This procedure is based on the [`GitHub flow`](../appendix/github.md#github-flow).

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

- Every section links to the relevant appendix doc for the detailed how-to.
- Task documents reference this file via `[`Git workflow`](../git-workflow.md)`.
- The workflow is fork-based: students fork the course repo, work in branches, create PRs to their own fork's `main`.
- PR review rules are included: reviewer checks acceptance criteria, leaves comments, approves.

----

## 7. Appendix documents (`lab/appendix/`)

### Purpose

Appendix files are **reference documents** — one file per tool or concept. They are linked from task docs whenever a concept or operation is first mentioned.

### Naming

- One file per tool/concept: `vs-code.md`, `git.md`, `docker.md`, `python.md`, `shell.md`, etc.
- Use lowercase with hyphens.

### Structure of an appendix file

```markdown
# <Tool or Concept Name>

<h2>Table of contents</h2>

- [What is `<Tool or Concept Name>`](#what-is-tool-or-concept-name)
- [Section 2](#section-2)
- ...

## What is `<Tool or Concept Name>`

<1–3 sentences explaining what this tool or concept is and how it is used in this project.>

Docs:

- [Official docs](https://...)

## Section 2

<Explanation and/or step-by-step instructions.>

...
```

### Key rules

- Each section is self-contained and linkable (task docs link to `appendix/<file>.md#<section>`).
- Start every appendix file with a `## What is <Tool>` section that defines the tool/concept in 1–3 sentences and includes a link to official docs.
- Provide both explanation and how-to instructions.
- Link to other appendix sections whenever a concept appears for the first time in a section (see [4.8. Links and cross-references](#48-links-and-cross-references)).
- Use `<h2>Table of contents</h2>` (HTML) so the ToC heading itself doesn't appear in the auto-generated ToC.
- When an operation can be done multiple ways, list them as options: "Use any of the following methods:"
- Vendor instructions that aren't good enough anywhere else (e.g., rewrite unclear official docs).
- Provide fallback methods when one method may not work for all students.

### Standard appendix topics to include

Depending on the lab, consider creating appendix files for:

- `vs-code.md` — VS Code basics: terminal, Command Palette, editor, extensions, layout.
- `git.md` — Git concepts: commits, branches, merging, rebasing.
- `git-vscode.md` — Git operations in VS Code: clone, commit, push, pull, switch branches.
- `github.md` — GitHub: forks, issues, PRs, GitHub flow.
- `gitlens.md` — GitLens extension usage.
- `shell.md` — Shell basics: commands, arguments, environment variables.
- `linux.md` — Linux basics: ports, processes, package management.
- `docker.md` — Docker and Docker Compose concepts.
- `environments.md` — Environment variables, `.env` files, secrets.
- `ssh.md` — SSH setup and usage.
- `python.md` — Python, virtual environments, package managers (`uv`).
- `testing.md` — Testing concepts, `pytest`, assertions.
- `web-development.md` — HTTP, endpoints, status codes, URLs, JSON, APIs.
- `file-system.md` — Files, directories, paths.
- `file-formats.md` — JSON, YAML, TOML, Markdown.
- `vm.md` — Virtual machines: creation, access, IP addresses.
- `operating-system.md` — OS concepts.
- `computer-networks.md` — Networking basics.
- `placeholders.md` — Index of all placeholders used in the lab, each linking to its definition in the relevant appendix doc.

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

## 12. Task design principles

### 12.1. Progressive complexity

- **Required tasks** build on each other and increase in complexity. A typical progression:
  - Early tasks: Run/explore something locally (minimal setup).
  - Middle tasks: Find and fix a problem, add a feature (debugging, testing, Git workflow).
  - Later tasks: Add infrastructure, containerize, or deploy (Docker, CI/CD, VM, cloud).
- **Start with observation, not coding.** The first tasks should be observation-only: explore the system, query endpoints, record what you see. Students should understand the system from all angles before implementing anything.
- Adapt the progression to the lab's topic. Not every lab needs Docker or deployment — the principle is that complexity increases across tasks.
- **Optional tasks** extend the lab with independent challenges.

### 12.2. Every task teaches something

Each task has a clear **Purpose** (what the student learns) and **Context** (why it matters). Tasks are not busywork — they simulate real engineering workflows.

When the lab has multiple domain entities (e.g., resources, models, tables), assign each entity a distinct learning role:

| Role      | What students do              | Example                                                |
| --------- | ----------------------------- | ------------------------------------------------------ |
| Reference | Study existing implementation | `items` endpoints (fully implemented)                  |
| Debug     | Enable and fix broken code    | `interactions` endpoint (commented out, contains bugs) |
| Implement | Build from a template         | `learners` endpoint (placeholder-based template)       |

This prevents overlap and ensures each task has a unique learning objective.

### 12.3. High-level instructions with low-level fallbacks

- Write high-level instructions in the task document.
- Link to appendix sections for detailed, step-by-step breakdowns.
- This way, experienced students move fast while beginners can follow detailed guides.

### 12.4. Provide fallback methods

When one method to complete a step may not work (e.g., OS-specific), provide alternatives:

```markdown
View the file using one of the following methods.

Method 1:

1. [Run using the `VS Code Terminal`](...)

Method 2:

1. [Open the file](...)
```

### 12.5. Localize instructions

Provide instructions where they're easy to keep in mind. Don't make students jump between 5 different files to understand one step.

### 12.6. Git workflow integration

- Tasks that produce code changes always start with "Follow the `Git workflow`" (Step 0).
- The first step is always "Create an issue" with a specific title format: `[Task] <title>`.
- The last step is always finishing via PR or closing the issue with a comment.
- This teaches students the real-world cycle: Issue → Branch → Commits → PR → Review → Merge.

### 12.7. Acceptance criteria

- Every task ends with `## Acceptance criteria`.
- Criteria are concrete, binary, and verifiable by a PR reviewer.
- Use `- [ ]` checkbox format.
- Examples of good criteria:
  - `Issue has the correct title.`
  - `All tests pass after the fix.`
  - `PR is approved.`
  - `PR is merged.`
  - `The comment with the JSON response exists.`

### 12.8. Hints and solutions

For debugging/problem-solving tasks, provide collapsible hints and solutions using `<details>` tags. Let students try first, then peek if stuck.

### 12.9. Expected output

After commands that produce output, show what the student should expect to see:

~~~markdown
2. The output should be similar to this:

   ```terminal
   <expected output>
   ```
~~~

### 12.10. Notes explain "why"

Use `> [!NOTE]` blocks to explain concepts inline without breaking the step flow:

```markdown
> [!NOTE]
> The `.venv` directory contains the virtual environment.
> That is, files and dependencies that are necessary to run the web server.
```

### 12.11. Three kinds of task endings

**Tasks that produce code** (bug fixes, new features):

- End with "Finish the task" → create PR, get review, merge.
- Acceptance criteria include: PR approved, PR merged, all tests pass.

**Tasks that don't produce code** (run server, deploy):

- End with "Write a comment for the issue" → paste evidence (e.g., JSON response), close issue.
- Acceptance criteria include: issue has correct title, comment with evidence exists.

**Tasks with auto-checked deliverables** (exploration, questionnaires):

- End with "Commit the deliverable file" → student fills in a structured file (e.g., questionnaire with single-value answers), checked automatically by regex or a script.
- Acceptance criteria include: deliverable file exists, all answers match the expected format, auto-checker passes.

### 12.12. Cross-task references

Later tasks can reference steps from earlier tasks instead of repeating them:

```markdown
1. [Run the web server](./task-1.md#8-run-the-web-server).
```

### 12.13. Appendix section structure pattern

Each appendix section for a VS Code feature or tool should follow this pattern:

```markdown
## <Feature Name>

<1-2 sentence explanation.>

Location: see [`Basic Layout`](#basic-layout).

Docs:

- [Official docs link](https://...)

Actions:

- [Action 1](#action-1)
- [Action 2](#action-2)

### Action 1

<Step-by-step instructions.>
```

This provides: what it is, where to find it, official docs, and how to use it.

### 12.14. Placeholder-based implementation templates

When a task requires students to implement new code (e.g., a new endpoint), provide commented-out placeholder templates in the seed project. Students uncomment the code and replace placeholders with correct values, using an existing reference implementation as a guide.

~~~markdown
Placeholder template (in `src/app/routers/learners.py`):

```python
# UNCOMMENT AND FILL IN

# @router.<method>("/<resource_name>", response_model=List[<resource_schema>])
# def <function_name>(<query_param>: <type> = None):
#     """<docstring>"""
#     return <db_read_function>(<query_param>)

# Reference:
# items -> items_table (in db), ItemModel
# learners -> learners_table (in db), LearnerModel
```
~~~

Key rules:

- Placeholders use `<angle_brackets>` to indicate values students must fill in.
- Each placeholder template includes a `# Reference:` comment mapping the new resource to its reference counterpart.
- The reference implementation (e.g., `items` endpoint) must be fully working so students can study it.
- Each placeholder template should be a separate commit when implemented.

### 12.15. Seed project design

The seed project is the starting codebase students receive. Design it with three tiers of completeness:

1. **Fully implemented (reference):** One resource is complete and working. Students study it to understand the pattern. Example: `items` endpoints with all CRUD operations.
2. **Commented out with bugs (debug):** Code exists but is disabled. Students uncomment it, discover it fails, and debug. Example: `interactions` endpoint with a schema-database mismatch.
3. **Placeholder templates (implement):** Commented-out code with `<placeholders>` that students fill in by following the reference. Example: `learners` endpoint with `<method>`, `<resource_name>`, `<resource_schema>`.

For each tier, both the route code and its router registration (e.g., `app.include_router(...)`) must be in the same state — commented out or active. Students uncomment both to enable the route.

### 12.16. Holistic task design

Combine related concerns into a single task when they share the same learning objective. A debugging task should include everything needed to understand the failure: reading code, examining the database, and fixing the bug — not three separate tasks.

Separate concerns into different tasks only when they produce fundamentally different artifacts or teach distinct skills. Example: API exploration via Swagger (produces a questionnaire) and database exploration via PgAdmin (produces a bug fix) belong in different tasks even though both involve the same system.

### 12.17. LLM-independence

All tasks must be completable without LLMs. This means:

- Provide placeholder templates, clear examples, and explicit step-by-step guidance.
- Use simple, direct language in student-facing materials.
- Provide fallback methods for every major operation.
- The "Learning advice" section encourages LLM use for understanding, but tasks must not require it.

### 12.18. Multi-bug debugging tasks

When designing debugging tasks, include multiple bugs at different layers of the request path so students learn to trace failures across the stack:

- **Schema–database mismatch:** A field name in the Pydantic model doesn't match the database column. Students discover this by comparing the model to the table schema (e.g., in PgAdmin).
- **Logic error:** A variable name or condition is wrong in the data processing code. Students discover this by reading the function and tracing its behavior.

Structure the task so each bug is discovered sequentially: the first fix unblocks progress but reveals the next failure. Provide collapsible hints for each bug.

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

## 15. Testing pattern

> Include this section if the lab has application code with tests. Omit for labs that are purely documentation- or configuration-focused.

- Include a `tests/` directory with test files.
- Use the project's test runner (e.g., `pytest`, `jest`, `go test`) configured in the package manager config.
- At least one test should **intentionally fail** so students can practice debugging.
- Tasks should instruct students to run tests and interpret output.
- Guide students through reading test output step-by-step. Break down the failure message into its components (test file, test name, assertion, expected vs. actual values):

  ```markdown
  1. Look at the test summary.
  2. You should see `FAILED <test-file>::<test-name> - assert <actual> == <expected>`.

     This line means the following:
     - The test failed (`FAILED`).
     - The test is in the file `<test-file>`.
     - The name of the failing test is `<test-name>`.
     - The assert that failed is `<actual> == <expected>`.
  ```

- Adapt the output format to the lab's test runner. The principle is the same: teach students to read and understand test output.
- Acceptance criteria should include "All tests pass."
- **Vary bug types across the request path.** When a lab includes multiple bugs, place them at different layers (e.g., schema–database mismatch at the data layer, logic error at the processing layer). This teaches students to trace failures across the full stack, not just look for one kind of mistake.

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
- [ ] Appendix docs exist for every tool/concept linked from tasks.
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
