# Resolve a merge conflict

**Time:** ~20-30 min

**Purpose:** Learn how to handle merge conflicts in Git, a common challenge in collaborative software development.

**Context:** In team environments, multiple developers often work on the same codebase simultaneously, leading to situations where changes conflict with each other. Understanding how to resolve these conflicts is essential for maintaining a healthy codebase.

## Steps

### 1. Create an issue

Title: `[Task] Resolve a merge conflict`

### 2. Learn `Git` basics (Optional)

Complete the first three tasks in `Introduction Sequence` on [Learn Git Branching](https://learngitbranching.js.org/).

### 3. Prepare your environment

Open your cloned fork in `VS Code`.

### 4. Switch to the `main` branch

```console
git switch main
```

Alternatively, use [`Command Palette`](https://code.visualstudio.com/docs/getstarted/getting-started#_access-commands-with-the-command-palette) -> `GitLens: Git Switch to...`.

### 5. Create two branches from `main`

```console
git branch feature-1
git branch feature-2
```

Alternatively, use `Command Palette` -> `GitLens: Git Create Branch...`.

### 6. Modify the same file on `feature-1` branch

On `feature-1` branch:

- Edit a file (e.g., change the first line in `README.md`).
- Commit your changes.

### 7. Modify the same lines on `feature-2` branch

On `feature-2` branch:

- Edit the **same lines** in the same file that you edited on the `feature-1` branch.
- Note that the changes on `feature-2` must differ from changes on `feature-1`.
- Commit your changes.

### 8. Merge `feature-2` into `feature-1`

```console
git switch feature-1
git merge feature-2
```

This will create a merge conflict since both branches modified the same lines.

### 9. Resolve the merge conflict

- In the `Primary Sidebar` -> `Merge Changes` -> Click the file that you changed. The file will open.

- Click inside that file.

- Click `Resolve in Merge Editor` to resolve the merge conflict in the [3-way merge editor](https://code.visualstudio.com/docs/sourcecontrol/merge-conflicts#_use-the-3way-merge-editor).

- Accept a change that you like more.

- Click `Complete Merge`.

### 10. Review your changes

- In the `Primary Sidebar` -> `Source Control` -> `Staged Changes` -> Click the file to see changes that you applied.

- Click `Continue`.

### 11. Push your branch

Click `Publish Branch` to push `feature-1` to `GitHub`.

### 12. Create a pull request

Create a PR from `feature-1` to `main`.

### 13. Document your resolution

In the PR summary, explain:

- What conflicted (1–2 sentences).
- How you resolved the conflict (1–2 sentences).

### 14. Complete the task

- Provide a link to the PR in the issue description.
- Close the PR. Don't merge it.
- Close the issue.

## Acceptance criteria

- [ ] Issue created
- [ ] Successfully resolved a merge conflict
- [ ] Created a pull request with explanation of the conflict and resolution
- [ ] Provided link to the PR in the issue description
- [ ] Closed the PR without merging
- [ ] Closed the issue
