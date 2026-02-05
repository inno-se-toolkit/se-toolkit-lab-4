# Resolve a merge conflict

**Time:** ~15-20 min

**Purpose:** Learn how to resolve merge conflicts — a common situation when working with Git.

**Context:** In team environments, multiple developers often work on the same codebase simultaneously. They might edit the same lines of code, leading to situations where changes conflict with each other. Understanding how to resolve these conflicts is essential for maintaining a healthy codebase.

## Steps

### 1. Create an issue

Title: `[Task] Resolve a merge conflict`

### 2. Create practice branches

```console
git switch main
git branch conflict-branch-1
git branch conflict-branch-2
```

Alternatively:

1. Open [`Command Palette`](../../appendix/vs-code.md#command-palette).
2. Start typing and select `GitLens: Git Create Branch...`.
3. Press `Enter`.
4. Select `main`.
5. Enter `conflict-branch-1`.
6. Press `Create Branch`.
7. Repeat for another branch.

### 3. Make a change on the `conflict-branch-1`

```console
git switch conflict-branch-1
```

Alternatively:

1. Open [`Command Palette`](../../appendix/vs-code.md#command-palette).
2. Start typing and select `GitLens: Git Switch to...`.
3. Press `Enter`.
4. Start typing and select `conflict-branch-1`.
5. Press `Enter`.

Edit [`CONTRIBUTORS.md`](../../../CONTRIBUTORS.md) — change the comment text to something else (e.g., "Add your name here").

Commit:

```console
git add CONTRIBUTORS.md
git commit -m "docs: update contributors instructions"
```

### 4. Make a conflicting change on `conflict-branch-2`

```console
git switch conflict-branch-2
```

Edit `CONTRIBUTORS.md` — change the same comment to something different (e.g., "Write your name below").

Commit:

```console
git add CONTRIBUTORS.md
git commit -m "docs: update contributors comment"
```

### 5. Merge and resolve the conflict

You're currently on the branch `conflict-branch-2`.

```console
git merge conflict-branch-1
```

#### Resolve the conflict using without the merge editor

Git will report a conflict.

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

```console
git add CONTRIBUTORS.md
git commit -m "docs: resolve merge conflict in contributors"
```

#### Resolve the conflict using the merge editor

- In the `Primary Sidebar` -> `Merge Changes` -> Click the file that you changed. The file will open.

- Click inside that file.

- Click `Resolve in Merge Editor` to resolve the merge conflict in the [3-way merge editor](https://code.visualstudio.com/docs/sourcecontrol/merge-conflicts#_use-the-3way-merge-editor).

- Accept a change that you like more.

- Click `Complete Merge`.

- In the `Primary Sidebar` -> `Source Control` -> `Staged Changes` -> Click the file to see changes that you applied.

- Click `Continue`.

### 6. Create a PR

Create a PR from `conflict-branch-2` to `main`.

Don't merge it.

Link the issue as usually.

### 7. Clean up

Delete the practice branches:

```console
git branch -d conflict-branch-1
git branch -d conflict-branch-2
```

Alternatively:

1. Open [`Command Palette`](../../appendix/vs-code.md#command-palette).
2. Start typing and select `GitLens: Git Delete Branch...`.
3. Press `Enter`.
4. Select `conflict-branch-1` and `conflict-branch-2`.
5. Press `Enter`.
6. Select `Delete Branches`.
7. Press `Enter`.

Close the issue.

## Acceptance criteria

- [ ] Issue created
- [ ] Successfully created and resolved a merge conflict
- [ ] Closed the issue
- [ ] PR is not merged
