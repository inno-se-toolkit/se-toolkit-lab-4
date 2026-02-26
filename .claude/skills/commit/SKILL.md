---
name: commit
description: Create a git commit following this project's conventions
disable-model-invocation: true
argument-hint: "[files...]"
---

Create a git commit following this project's commit conventions.

## Conventions

Read `docs/contributing/conventions/commits.md` for the full reference
(types, scopes, subject line, body rules, examples).

## AI co-authorship

Always append this trailer:

```text
Co-Authored-By: <your current model name> <noreply@anthropic.com>
```

Use your actual model name (e.g. `Claude Opus 4.6`, `Claude Sonnet 4.6`).

## Staging and committing

- If the user specifies files via $ARGUMENTS, stage only those files. If `$ARGUMENTS` is literally `staged`, skip staging and commit whatever is already in the index
- If a file lives inside a **git submodule**, run `git add` / `git commit` from inside the submodule's root directory. Detect by running `git rev-parse --show-toplevel` from the file's directory — if it differs from the parent repo root, the file is in a submodule. Before staging and committing, run `cd "$(git rev-parse --show-toplevel)"` to land at the submodule root regardless of where the working directory currently is (the Bash tool's working directory persists between calls, so you may already be inside the submodule from a previous command)
- Make exactly **one commit** per invocation. If the user passes specific files, commit only those. If changes span unrelated areas, the user will invoke the skill multiple times
