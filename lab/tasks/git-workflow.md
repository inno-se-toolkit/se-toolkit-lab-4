# `Git workflow` for tasks

> [!NOTE]
> This procedure is based on the [`GitHub flow`](../appendix/github.md#github-flow).

```text
Issue ➜ Branch ➜ Commits ➜ PR ➜ Review ➜ Merge
```

Here's this workflow in the context of repos:

![Git workflow](../images/git-workflow.drawio.svg)

Outline:

- [Create a `Lab Task` issue](#create-a-lab-task-issue)
- [Switch to the `main` branch](#switch-to-the-main-branch)
  - [Switch to the `main` branch using the `VS Code Terminal`](#switch-to-the-main-branch-using-the-vs-code-terminal)
  - [Switch to the `main` branch using `GitLens`](#switch-to-the-main-branch-using-gitlens)
- [Pull changes from `origin/main`](#pull-changes-from-originmain)
  - [Pull changes from `origin/main` using the `VS Code Terminal`](#pull-changes-from-originmain-using-the-vs-code-terminal)
  - [Pull changes from `origin/main` using `GitLens`](#pull-changes-from-originmain-using-gitlens)
- [Resolve conflicts](#resolve-conflicts)
  - [Pull and rebase using `GitLens`](#pull-and-rebase-using-gitlens)
  - [Resolve conflicts using `GitLens`](#resolve-conflicts-using-gitlens)
- [Switch to a new branch](#switch-to-a-new-branch)
- [Edit files](#edit-files)
- [Commit](#commit)
- [(Optional) Undo commits](#optional-undo-commits)
- [Publish the branch](#publish-the-branch)
- [Push more commits](#push-more-commits)
- [Create a PR to `main` in your fork](#create-a-pr-to-main-in-your-fork)
- [Get a PR review](#get-a-pr-review)
  - [PR review rules](#pr-review-rules)
    - [As a PR reviewer](#as-a-pr-reviewer)
    - [As a PR author](#as-a-pr-author)
- [Merge the PR](#merge-the-pr)
- [Clean up](#clean-up)

## Create a `Lab Task` issue

[Create an issue](../appendix/github.md#create-an-issue) using the `Lab Task` [issue form](../appendix/github.md#issue-form).

## Switch to the `main` branch

Go to `VS Code`.

Switch to the `main` branch using any of the following methods:

- [Switch to the `main` branch using the `VS Code Terminal`](#switch-to-the-main-branch-using-the-vs-code-terminal)
- [Switch to the `main` branch using `GitLens`](#switch-to-the-main-branch-using-gitlens)

### Switch to the `main` branch using the `VS Code Terminal`

1. [Run using the `VS Code Terminal`](../appendix/vs-code.md#run-a-command-using-the-vs-code-terminal):

   ```terminal
   git switch main
   ```

### Switch to the `main` branch using `GitLens`

1. [Run using the `Command Palette`](../appendix/vs-code.md#run-a-command-using-the-command-palette):
   `GitLens: Git Switch to..`.
2. [Select](../appendix/vs-code.md#select-an-option-from-a-list) the `main` branch.

## Pull changes from `origin/main`

Pull changes from the `main` branch in your fork on `GitHub`.

We call that branch `origin/main`.

### Pull changes from `origin/main` using the `VS Code Terminal`

1. [Run using the `VS Code Terminal`](../appendix/vs-code.md#run-a-command-using-the-vs-code-terminal):

   ```terminal
   git pull origin main
   ```

### Pull changes from `origin/main` using `GitLens`

1. [Run using the `Command Palette`](../appendix/vs-code.md#run-a-command-using-the-command-palette): `GitLens: Pull`

## Resolve conflicts

You may see some errors and messages about conflicts after pulling.

It may happen that commits on your `origin/main` are different from commits on your local `main` branch in your cloned repo on your computer.

You can see that in the [`Status Bar`](../appendix/vs-code.md#status-bar).

<img alt="Commit Conflict" src="../images/appendix/vs-code/status-bar-commit-conflict.png" style="width:400px"></img>

You need to pull commits from `origin/main` into your local `main`.

These commits from `origin/main` will find a place somewhere among the commits on your local `main`.

However, you can get conflicts if commits from `origin/main` modified the same lines of text in files as your local commits but in a different way.

In this case, you should rebase your local branch and resolve conflicts:

- [Pull and rebase using `GitLens`](#pull-and-rebase-using-gitlens)
- [Resolve conflicts using `GitLens`](#resolve-conflicts-using-gitlens)

### Pull and rebase using `GitLens`

When you rebase, your local commits are placed on top of the commits from `origin/main`.

1. [Run using the `Command Palette`](../appendix/vs-code.md#run-a-command-using-the-command-palette):
   `GitLens: Pull`
2. [Select](../appendix/vs-code.md#select-an-option-from-a-list) `Pull with Rebase` (e.g., using `UpArrow` and `DownArrow` on your keyboard).
3. You're done if `GitLens` doesn't show any error.

### Resolve conflicts using `GitLens`

Continue resolving conflicts if you see an error like this:

<img alt="Pull Error" src="../images/appendix/gitlens/pull-error.png" style="width:400px"></img>

1. [Open the `Source Control`](../appendix/vs-code.md#open-the-source-control).
2. Go to `Merge Changes`.
3. Click a file.
4. Click `Resolve in Merge Editor`.
5. Accept changes that you like more.
6. Click `Complete Merge`.
7. [Open the `Source Control`](../appendix/vs-code.md#open-the-source-control).
8. Click `Continue`.
9. This should be resolved.
10. There may be other conflicts.
11. `VS Code` can show something like `Rebasing (1/3)` and `Cancel`.
12. Click that `Cancel`.
13. Repeat steps.

## Switch to a new branch

[Create a new branch and switch to it](../appendix/git-vscode.md#switch-to-a-new-branch).

We'll refer to the name of this branch as `<branch-name>`.

## Edit files

Edit files in the [`Editor`](../appendix/vs-code.md#editor) to produce changes.

## Commit

[Commit changes](../appendix/git-vscode.md#commit-changes) to the `<branch-name>` to complete the task.

## (Optional) Undo commits

[Undo commits](../appendix/git-vscode.md#undo-commits) if necessary.

## Publish the branch

[Publish the branch](../appendix/git-vscode.md#publish-the-branch) with your changes.

## Push more commits

[Push more commits](../appendix/git-vscode.md#push-more-commits) to the published branch if necessary.

## Create a PR to `main` in your fork

[Create a PR](../appendix/github.md#create-a-pr) replacing:

- `<repo-owner-username>` with `inno-se-toolkit`;
- `<repo-name>` with `se-toolkit-lab-2`;
- `<your-username>` with your `GitHub` username;
- `<branch-name>` with the name of the branch that you want to merge in the PR.

## Get a PR review

[Request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/requesting-a-pull-request-review#requesting-reviews-from-collaborators-and-organization-members) a review of the PR from the collaborator (see [PR review rules](#pr-review-rules)).

Get the collaborator's comments and address them, e.g., make fixes or ask to clarify the comment.

Get the collaborator to approve the PR.

### PR review rules

#### As a PR reviewer

1. Check the task's **Acceptance criteria**.
2. Leave at least one [comment](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/reviewing-changes-in-pull-requests/commenting-on-a-pull-request#adding-comments-to-a-pull-request) — point out problems or confirm that items look good.
3. [Approve](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/reviewing-changes-in-pull-requests/reviewing-proposed-changes-in-a-pull-request#submitting-your-review) the PR when all relevant acceptance criteria are met.

#### As a PR author

- Address reviewer comments (fix issues or explain your reasoning).
- Reply to comments, e.g., "Fixed in d0d5aeb".

## Merge the PR

Click `Merge pull request`.

## Clean up

Close the issue.

Delete the PR branch.
