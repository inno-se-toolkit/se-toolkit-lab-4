---
name: commit
description: Create a git commit following this project's conventions
disable-model-invocation: true
argument-hint: "[files...]"
---

Create a git commit following Conventional Commits.

## Format

```
type(scope): subject

Optional body — use when additional context helps reviewers understand
why the change was made. Write in imperative mood. Wrap at 72 characters.
IMPORTANT: If the body covers 2+ points, use a bullet list.

Co-Authored-By: <your current model name> <noreply@anthropic.com>
```

## Rules

- **type**: `feat` (new content/feature), `fix` (correction/improvement), `docs` (documentation-only), `refactor`, `test`, `chore`
- **scope**: area of change, e.g. `docs`, `lab`, `config`
- **subject**: lowercase, present tense, imperative mood, no period at the end
- Keep the subject line concise (under 72 characters)
- Add a body when the subject alone doesn't fully explain the change — e.g. non-obvious decisions, side effects, or grouped changes. Separate from the subject with a blank line. Write in imperative mood
- **Body with 2+ points → always use a bullet list.** Never write multiple points as separate sentences or paragraphs
- Always include the `Co-Authored-By` trailer with your current model name (e.g. `Claude Opus 4.6`, `Claude Sonnet 4.6`)
- If the user specifies files via $ARGUMENTS, stage only those files. If `$ARGUMENTS` is literally `staged`, skip staging and commit whatever is already in the index
- If a file lives inside a **git submodule**, run `git add` / `git commit` from inside the submodule's root directory. Detect by running `git rev-parse --show-toplevel` from the file's directory — if it differs from the parent repo root, the file is in a submodule. Before staging and committing, run `cd "$(git rev-parse --show-toplevel)"` to land at the submodule root regardless of where the working directory currently is (the Bash tool's working directory persists between calls, so you may already be inside the submodule from a previous command)
- Make exactly **one commit** per invocation. If the user passes specific files, commit only those. If changes span unrelated areas, the user will invoke the skill multiple times

## Examples from this project

- `feat(docs): add Service section to Docker appendix and link from setup`
- `fix(docs): replace TODO with explanation of services and containers`
- `fix(docs): display Qwen images side by side with responsive wrap`
- `feat(docs): add screenshots`
- `chore(config): update vscode settings`
