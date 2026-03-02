---
name: fix-via-conventions
description: Fix convention violations found by /review-via-conventions
argument-hint: "<path>"
---

Fix convention violations in a task file using the report produced by `/review-via-conventions`.

## Steps

1. Parse `$ARGUMENTS` to get the file path. Accept paths like `lab/tasks/setup.md`, `lab/tasks/required/task-2.md`, or `lab/tasks/optional/task-1.md`. If the path is missing or does not point to a file under `lab/tasks/`, ask the user.
2. Derive the report path: `tmp/<filename>-review-via-conventions-report.md`, where `<filename>` is the basename of the target file without the `.md` extension. If the report file does not exist, tell the user to run `/review-via-conventions <path>` first and stop.
3. Read the report file.
4. Read the target task file.
5. Read the convention files referenced in the report header so every fix is grounded in the actual convention text:
   - `instructors/context/conventions/common.md`
   - `instructors/context/conventions/tasks.md`
6. Work through the report findings **one group at a time**. For each violation, apply the minimal edit that resolves it. Use line numbers from the report as a starting guide, but always verify against the current file content (earlier fixes may shift lines).

## Rules

- The report is the single source of truth for *what* to fix. Do not look for additional violations beyond those listed in the report.
- Each fix must satisfy the convention cited in the report. When in doubt, re-read the convention text.
- Make the smallest change that resolves each violation. Do not rewrite surrounding text, reorder sections, or make stylistic changes unrelated to a reported violation.
- Preserve the author's voice and intent. Rephrase only when required by a convention.
- If a reported violation is ambiguous or cannot be fixed without changing the meaning of the content, skip it and note it in the summary.

## Output

After all fixes are applied, print a short summary listing:
- Number of violations fixed.
- Number of violations skipped (if any), with reasons.
