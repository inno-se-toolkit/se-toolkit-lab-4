# Resolve a merge conflict

**Time:** ~15-20 min

**Purpose:** Learn how to resolve merge conflicts — a common situation when working with Git.

**Context:** In team environments, multiple developers often work on the same codebase simultaneously. They might edit the same lines of code, leading to situations where changes conflict with each other. Understanding how to resolve these conflicts is essential for maintaining a healthy codebase.

- [0. Follow the `Git workflow`](#0-follow-the-git-workflow)
- [1. Create an issue](#1-create-an-issue)
- [2. Switch to `main`](#2-switch-to-main)
- [3. Switch to `conflict-branch-1`](#3-switch-to-conflict-branch-1)
- [4. Edit `CONTRIBUTORS.md` on `conflict-branch-1`](#4-edit-contributorsmd-on-conflict-branch-1)
- [5. Commit changes to `conflict-branch-1`](#5-commit-changes-to-conflict-branch-1)
- [6. Switch to `main`](#6-switch-to-main)
- [7. Switch to the `conflict-branch-2`](#7-switch-to-the-conflict-branch-2)
- [8. Make a conflicting change on `conflict-branch-2`](#8-make-a-conflicting-change-on-conflict-branch-2)
- [8. Commit changes to `conflict-branch-2`](#8-commit-changes-to-conflict-branch-2)
- [9. Merge `conflict-branch-1` into `conflict-branch-2`](#9-merge-conflict-branch-1-into-conflict-branch-2)
- [10. Resolve a conflict](#10-resolve-a-conflict)
  - [Resolve the conflict without the merge editor](#resolve-the-conflict-without-the-merge-editor)
  - [Resolve the conflict using the merge editor](#resolve-the-conflict-using-the-merge-editor)
- [11. Create a PR](#11-create-a-pr)
- [12. Switch to `main`](#12-switch-to-main)
- [13. Delete conflict branches](#13-delete-conflict-branches)
- [Acceptance criteria](#acceptance-criteria)

## 0. Follow the `Git workflow`

Follow the [`Git workflow`](../git-workflow.md) to complete this task.

The task specifies what to do not as in the `Git workflow`.

## 1. Create an issue

Title: `[Task] Resolve a merge conflict`

## 2. Switch to `main`

1. [Switch to the `main` branch](../git-workflow.md#switch-to-the-main-branch).

## 3. Switch to `conflict-branch-1`

1. [Switch to the new branch](../git-workflow.md#switch-to-a-new-branch) `conflict-branch-1`.

## 4. Edit `CONTRIBUTORS.md` on `conflict-branch-1`

1. Edit [`CONTRIBUTORS.md`](../../../CONTRIBUTORS.md). For example, add `- @johndoe` on the next line after `- @<your-username>`.

## 5. Commit changes to `conflict-branch-1`

[Commit](../git-workflow.md#commit) changes in `CONTRIBUTORS.md` to `conflict-branch-1`.

The commit message should be `docs: add @johndoe to contributors`.

## 6. Switch to `main`

1. [Switch to the `main` branch](../git-workflow.md#switch-to-the-main-branch).

## 7. Switch to the `conflict-branch-2`

1. [Switch to the new branch](../git-workflow.md#switch-to-a-new-branch) `conflict-branch-2`.

## 8. Make a conflicting change on `conflict-branch-2`

1. Edit [`CONTRIBUTORS.md`](../../../CONTRIBUTORS.md) in a different way than before. For example, add `- @janedoe` on the next line after `- @<your-username>`.

## 8. Commit changes to `conflict-branch-2`

[Commit](../git-workflow.md#commit) changes in `CONTRIBUTORS.md` to `conflict-branch-2`.

The commit message should be `docs: add @janedoe to contributors`.

## 9. Merge `conflict-branch-1` into `conflict-branch-2`

[Run using the `Terminal`](../../appendix/vs-code.md#run-a-command-using-the-terminal):

```terminal
git merge conflict-branch-1
```

## 10. Resolve a conflict

`Git` will report a conflict.

Resolve it using one of the following methods:

- [Resolve the conflict without the merge editor](#resolve-the-conflict-without-the-merge-editor)
- [Resolve the conflict using the merge editor](#resolve-the-conflict-using-the-merge-editor)

### Resolve the conflict without the merge editor

Open [`CONTRIBUTORS.md`](../../../CONTRIBUTORS.md) — you'll see conflict markers:

```console
<<<<<<< HEAD
<!-- Write your name below -->
=======
<!-- Add your name here -->
>>>>>>> conflict-practice
```

Edit the file to keep one version (or combine them). Remove the conflict markers.

Then complete the merge:

```terminal
git add CONTRIBUTORS.md
git commit -m 'docs: resolve merge conflict in contributors'
```

### Resolve the conflict using the merge editor

1. [Open the `Source Control`](../../appendix/vs-code.md#open-the-source-control).
2. Go to `Merge Changes`.
3. Click the file that you changed.
4. The file will open.
5. Click inside that file.
6. Click `Resolve in Merge Editor` to resolve the merge conflict in the [3-way merge editor](https://code.visualstudio.com/docs/sourcecontrol/merge-conflicts#_use-the-3way-merge-editor).
7. Accept a change that you like more.
8. Click `Complete Merge`.
9. [Open the `Source Control`](../../appendix/vs-code.md#open-the-source-control).
10. Go to `Staged Changes`.
11. Click the file to see changes that you applied.
12. Click `Continue`.

## 11. Create a PR

[Create a PR](../git-workflow.md#create-a-pr) from `conflict-branch-2` to `main`.

Don't merge it.

Link the issue as usually.

Close the issue.

Close the PR.

## 12. Switch to `main`

1. [Switch to the `main` branch](../git-workflow.md#switch-to-the-main-branch).

## 13. Delete conflict branches

Delete the practice branches using one of the following methods.

Method 1:

1. [Run using the `Terminal`](../../appendix/vs-code.md#run-a-command-using-the-terminal):

    ```terminal
    git branch -d conflict-branch-1
    git branch -d conflict-branch-2
    ```

Method 2:

1. [Run using the `Command Palette`](../../appendix/vs-code.md#run-a-command-using-the-command-palette):
   `GitLens: Git Delete Branch..`.
2. Select `conflict-branch-1` and `conflict-branch-2` to delete them.
3. Click `OK`.
4. Click `Delete Branches`.

## Acceptance criteria

- [ ] Issue created
- [ ] Successfully created and resolved a merge conflict
- [ ] Closed the issue
- [ ] PR is not merged
