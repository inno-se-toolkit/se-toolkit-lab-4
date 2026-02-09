# Practice the `Git workflow`

**Time:** ~15 min

**Purpose:** Practice the [`Git workflow`](../git-workflow.md) before working on the main tasks.

**Context:** This task is an opportunity to practice the full cycle (Issue → Branch → Commits → PR → Review → Merge).

- [0. Follow the `Git workflow`](#0-follow-the-git-workflow)
- [1. Create an issue](#1-create-an-issue)
- [2. Create a branch](#2-create-a-branch)
- [3. Add your name](#3-add-your-name)
- [4. Commit and push](#4-commit-and-push)
- [5. Create a Pull Request (PR)](#5-create-a-pull-request-pr)
- [Acceptance criteria](#acceptance-criteria)

## 0. Follow the `Git workflow`

Follow the [`Git workflow`](../git-workflow.md) to complete this task.

## 1. Create an issue

Title: `[Task] Add my name to contributors`

## 2. Create a branch

See [Create a branch](../git-workflow.md#create-a-branch).

Use `<add-contributor>` instead of the `<branch-name>`.

## 3. Add your name

1. Open [`CONTRIBUTORS.md`](../../../CONTRIBUTORS.md).
2. Replace `@johndoe` with `@<your-username>`.
3. Save the file.

## 4. Commit and push

[Commit changes](../git-workflow.md#commit).

Note that:

- You should stage changes in `CONTRIBUTORS.md`.
- The commit message should be like `docs: add @johndoe to contributors`. Replace `@johndoe` with `@<your-username>`.

## 5. Create a Pull Request (PR)

> [!IMPORTANT]
> Use the title `Add @<your-username> to contributors` but replace `@<your-username>`.
> Example: `Add @johndoe to contributors`

[Create a PR](../git-workflow.md#create-a-pr) and continue following the `Git workflow` from there.

## Acceptance criteria

- [ ] Issue created
- [ ] Username added to `CONTRIBUTORS.md`
- [ ] Commit message follows `type: description` format
- [ ] PR created and linked to issue
- [ ] Partner reviewed and approved
- [ ] PR merged
