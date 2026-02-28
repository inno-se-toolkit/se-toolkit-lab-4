# Wiki conventions — applies to `wiki/` only

- [7. Wiki documents (`wiki/`)](#7-wiki-documents-wiki)
  - [Purpose](#purpose)
  - [Naming](#naming)
  - [Structure of a wiki file](#structure-of-a-wiki-file)
  - [Key rules](#key-rules)
  - [Standard wiki topics to include](#standard-wiki-topics-to-include)
- [12.13. Wiki section structure pattern](#1213-wiki-section-structure-pattern)
- [17. Checklist before publishing](#17-checklist-before-publishing)

## 7. Wiki documents (`wiki/`)

### Purpose

Wiki files are **reference documents** — one file per tool or concept. They are linked from task docs whenever a concept or operation is first mentioned.

### Naming

- One file per tool/concept: `vs-code.md`, `git.md`, `docker.md`, `python.md`, `shell.md`, etc.
- Use lowercase with hyphens.

### Structure of a wiki file

```markdown
# <Tool or Concept Name>

<h2>Table of contents</h2>

- [What is `<tool or concept name>`](#what-is-tool-or-concept-name)
- [Section 2](#section-2)
- ...

## What is `<tool or concept name>`

<1–3 sentences explaining what this tool or concept is and how it is used in this project.>

Docs:

- [Official docs](https://...)

## Section 2

<Explanation and/or step-by-step instructions.>

...
```

### Key rules

- Each section is self-contained and linkable (task docs link to `wiki/<file>.md#<section>`).
- Start every wiki file with a `## What is <tool or concept>` section that defines the tool/concept in 1–3 sentences and includes a link to official docs. The heading may use natural phrasing (articles, singular/plural) that differs from the H1 title — e.g., `# Computer Networks` → `## What is a computer network`.
- Provide both explanation and how-to instructions.
- Link to other wiki sections whenever a concept appears for the first time in a section (see [Links and cross-references](./common.md#48-links-and-cross-references)).
- Use `<h2>Table of contents</h2>` (HTML) so the ToC heading itself doesn't appear in the auto-generated ToC.
- When an operation can be done multiple ways, list them as options: "Use any of the following methods:"
- Vendor instructions that aren't good enough anywhere else (e.g., rewrite unclear official docs).
- Provide fallback methods when one method may not work for all students.

### Standard wiki topics to include

Depending on the lab, consider creating wiki files for:

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
- `placeholders.md` — Index of all placeholders used in the lab, each linking to its definition in the relevant wiki doc.

----

## 12.13. Wiki section structure pattern

Each wiki section for a VS Code feature or tool should follow this pattern:

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
