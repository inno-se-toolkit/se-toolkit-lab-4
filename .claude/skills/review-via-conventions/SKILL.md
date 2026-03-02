---
name: review-via-conventions
description: Review a task file for convention violations
argument-hint: "<path>"
---

Review a single task file for violations of the lab authoring conventions. The file must be under `lab/tasks/` (setup, required, or optional).

## Steps

1. Parse `$ARGUMENTS` to get the file path. Accept paths like `lab/tasks/setup.md`, `lab/tasks/required/task-2.md`, or `lab/tasks/optional/task-1.md`. If the path is missing or does not point to a file under `lab/tasks/`, ask the user.
2. Read the target file.
3. Read the convention files that apply to task files:
   - `instructors/context/conventions/common.md` — writing conventions (4.1–4.23)
   - `instructors/context/conventions/tasks.md` — task structure (Section 3) and design principles (Section 12)
4. Go through the target file **line by line**. Check it against **every** convention in both files. Flag each violation with its line number.

## Rules

- The convention files are the single source of truth. Check every rule they contain — do not skip any.
- Do not invent rules beyond what the convention files state.
- Be strict: flag every violation, no matter how small.
- Do not fix anything — only report.
- If a convention does not apply to the file (e.g., the file has no Docker commands), skip that category and note "Not applicable."
- For `setup.md`: skip task-only conventions (Section 3 template, acceptance criteria format). Apply all `common.md` conventions.

## Output format

Write the report to `tmp/review-via-conventions/<relative-path>`, where `<relative-path>` is the file's path relative to `lab/tasks/` (e.g., `tmp/review-via-conventions/setup.md` for `lab/tasks/setup.md`, `tmp/review-via-conventions/required/task-1.md` for `lab/tasks/required/task-1.md`). Create intermediate directories if they do not exist.

The report must be self-contained so another session or agent can act on it without extra context. Structure:

1. **Header** — file path reviewed, date, convention files used.
2. **Findings** — grouped by convention number (e.g., "4.2. Terminal commands", "Section 3. Task document structure"). Under each group, list findings as numbered items with line numbers. If a group has no findings, write "No issues found."
3. **Summary** — total violation count and a short overall assessment.

After writing the file, print its path in the conversation so the user can find it.
