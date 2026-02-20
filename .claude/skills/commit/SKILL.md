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

Co-Authored-By: <your current model name> <noreply@anthropic.com>
```

## Rules

- **type**: `feat` (new content/feature), `fix` (correction/improvement), `docs` (documentation-only), `refactor`, `test`, `chore`
- **scope**: area of change, e.g. `docs`, `lab`, `config`
- **subject**: lowercase, present tense, imperative mood, no period at the end
- Keep the subject line concise (under 72 characters)
- Always include the `Co-Authored-By` trailer with your current model name (e.g. `Claude Opus 4.6`, `Claude Sonnet 4.6`)
- If the user specifies files via $ARGUMENTS, stage only those files
- If changes are unrelated, make **separate commits** — one per logical group. Never bundle unrelated changes into a single commit

## Examples from this project

- `feat(docs): add Service section to Docker appendix and link from setup`
- `fix(docs): replace TODO with explanation of services and containers`
- `fix(docs): display Qwen images side by side with responsive wrap`
- `feat(docs): add screenshots`
- `chore(config): update vscode settings`
