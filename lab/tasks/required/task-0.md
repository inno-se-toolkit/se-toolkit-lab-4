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

On the issue page, click `Create a branch` in the right sidebar.

Alternatively, use the terminal:

```terminal
git checkout -b add-contributor
```

## 3. Add your name

1. Open [`CONTRIBUTORS.md`](../../../CONTRIBUTORS.md).
2. Replace `@johndoe` with `@<your-username>`.
3. Save the file.

## 4. Commit and push

```bash
git add CONTRIBUTORS.md
git commit -m 'docs: add <your-username> to contributors'
git push -u origin add-contributor
```

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
