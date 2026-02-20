---
name: pr
description: Create a pull request using this project's PR template
disable-model-invocation: true
argument-hint: "[issue-number]"
---

Create a pull request following the project's PR template at `.github/pull_request_template.md`.

## Rules

- Run `git log` and `git diff main...HEAD` to understand what changes will be included.
- Write a concise PR title summarizing the changes (under 72 characters).
- Fill in the Summary section with a brief description of what the PR does.
- If `$ARGUMENTS` contains an issue number, include `- Closes #<issue-number>` in the Summary section; otherwise omit that line entirely.
- Use `gh pr create` with `--title` and `--body` to open the PR.
- Target the `main` branch (`--base main`).
- Do not push or create the PR without showing the user the title and body first and asking for confirmation.
