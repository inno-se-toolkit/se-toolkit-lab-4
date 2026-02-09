# Resolve a merge conflict

**Time:** ~15-20 min

**Purpose:** Learn how to resolve merge conflicts — a common situation when working with Git.

**Context:** In team environments, multiple developers often work on the same codebase simultaneously. They might edit the same lines of code, leading to situations where changes conflict with each other. Understanding how to resolve these conflicts is essential for maintaining a healthy codebase.

- [Steps](#steps)
  - [1. Create an issue](#1-create-an-issue)
  - [2. Create practice branches](#2-create-practice-branches)
  - [3. Make a change on the `conflict-branch-1`](#3-make-a-change-on-the-conflict-branch-1)
  - [4. Make a conflicting change on `conflict-branch-2`](#4-make-a-conflicting-change-on-conflict-branch-2)
  - [5. Merge and resolve the conflict](#5-merge-and-resolve-the-conflict)
    - [Resolve the conflict using without the merge editor](#resolve-the-conflict-using-without-the-merge-editor)
    - [Resolve the conflict using the merge editor](#resolve-the-conflict-using-the-merge-editor)
  - [6. Create a PR](#6-create-a-pr)
  - [7. Clean up](#7-clean-up)
- [Acceptance criteria](#acceptance-criteria)

## Steps

### 1. Create an issue

Title: `[Task] Resolve a merge conflict`

### 2. Create practice branches

```terminal
git switch main
git branch conflict-branch-1
git branch conflict-branch-2
```

Alternatively:

1. [Run using the `Command Palette`](../../appendix/vs-code.md#run-a-command-using-the-command-palette): `GitLens: Git Create Branch...`.
2. Select `main`.
3. Enter `conflict-branch-1`.
4. Press `Create Branch`.
5. Repeat for another branch.

### 3. Make a change on the `conflict-branch-1`

```terminal
git switch conflict-branch-1
```

Alternatively:

1. [Run using the `Command Palette`](../../appendix/vs-code.md#run-a-command-using-the-command-palette): `GitLens: Git Switch to...`.
2. Start typing and select `conflict-branch-1`.
3. Press `Enter`.

Edit [`CONTRIBUTORS.md`](../../../CONTRIBUTORS.md) — change the comment text to something else (e.g., "Add your name here").

Commit:

```terminal
git add CONTRIBUTORS.md
git commit -m 'docs: update contributors instructions'
```

### 4. Make a conflicting change on `conflict-branch-2`

```terminal
git switch conflict-branch-2
```

Edit `CONTRIBUTORS.md` — change the same comment to something different (e.g., "Write your name below").

Commit:

```terminal
git add CONTRIBUTORS.md
git commit -m 'docs: update contributors comment'
```

### 5. Merge and resolve the conflict

You're currently on the branch `conflict-branch-2`.

```terminal
git merge conflict-branch-1
```

#### Resolve the conflict using without the merge editor

`Git` will report a conflict.

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

#### Resolve the conflict using the merge editor

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

### 6. Create a PR

Create a PR from `conflict-branch-2` to `main`.

Don't merge it.

Link the issue as usually.

### 7. Clean up

Delete the practice branches:

```terminal
git branch -d conflict-branch-1
git branch -d conflict-branch-2
```

Alternatively:

1. [Run using the `Command Palette`](../../appendix/vs-code.md#run-a-command-using-the-command-palette): `GitLens: Git Delete Branch...`.
2. Select `conflict-branch-1` and `conflict-branch-2` to delete them.
3. Click `OK`.
4. Click `Delete Branches`.

Close the issue.

Close the PR.

## Acceptance criteria

- [ ] Issue created
- [ ] Successfully created and resolved a merge conflict
- [ ] Closed the issue
- [ ] PR is not merged
