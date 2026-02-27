# Wiki conventions — applies to `wiki/` only

Full source: `instructors/context/lab-conventions/lab-conventions.md` §7, §12.13

Also read: `instructors/context/lab-conventions/conventions-common.md`

## 7. Wiki documents

**Purpose:** Reference documents, one file per tool or concept. Linked from task docs on first mention.

**Naming:** `vs-code.md`, `git.md`, `docker.md` — lowercase with hyphens. One file per tool/concept.

**File template:**

```markdown
# <Tool or Concept Name>

<h2>Table of contents</h2>

- [What is `<Tool or Concept Name>`](#what-is-tool-or-concept-name)
- [Section 2](#section-2)
- ...

## What is `<Tool or Concept Name>`

<1–3 sentences explaining what this tool/concept is and how it is used in this project.>

Docs:

- [Official docs](https://...)

## Section 2

<Explanation and/or step-by-step instructions.>
```

**Key rules:**

- Each section is self-contained and linkable (`wiki/<file>.md#<section>`).
- Every wiki file starts with `## What is <Tool>` — 1–3 sentence definition + official docs link.
- Use `<h2>Table of contents</h2>` (HTML) so the heading is excluded from the auto-generated ToC.
- Link to other wiki sections on first mention within each section (see conventions-common.md §4.8).
- Multiple methods → list as options: "Use any of the following methods:"
- Provide fallback methods when one method may not work for all students.
- Cross-reference other wiki files freely.

## 12.13 Wiki section structure pattern

Each section covering a VS Code feature or tool follows this pattern:

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

Provides: what it is, where to find it, official docs, and how to use it.

## Pre-publish checklist

See `instructors/context/lab-conventions/conventions-lab.md` §17.

## Standard wiki topics

Consider including (depends on the lab):
`vs-code.md`, `git.md`, `git-vscode.md`, `github.md`, `gitlens.md`, `shell.md`, `linux.md`,
`docker.md`, `environments.md`, `ssh.md`, `python.md`, `testing.md`, `web-development.md`,
`file-system.md`, `file-formats.md`, `vm.md`, `operating-system.md`, `computer-networks.md`,
`placeholders.md`.
