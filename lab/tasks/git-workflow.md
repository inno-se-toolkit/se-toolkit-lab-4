# `Git workflow` for tasks

> [!NOTE]
> This procedure is based on the [`GitHub flow`](../appendix/github.md#github-flow).

```text
Issue ➜ Branch ➜ Commits ➜ PR ➜ Review ➜ Merge
```

The following diagram shows this workflow in the context of repositories:

![Git workflow](../images/git-workflow.drawio.svg)

Outline:

<!-- no toc -->
- [Create a `Lab Task` issue](#create-a-lab-task-issue)
- [Switch to the `main` branch](#switch-to-the-main-branch)
- [Detect conflicts](#detect-conflicts)
- [Pull changes from `origin/main`](#pull-changes-from-originmain)
- [Pull changes from `origin/main` and rebase](#pull-changes-from-originmain-and-rebase)
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

[Switch to the `main` branch](../appendix/git-vscode.md#switch-to-the-branch-name-branch) in `VS Code`.

## Detect conflicts

[Detect conflicts with the `origin/main`](../appendix/git-vscode.md#detect-conflicts).

## Pull changes from `origin/main`

[Pull changes from the `main` branch in your fork on `GitHub`](../appendix/git-vscode.md#pull-changes-from-originbranch-name).

## Pull changes from `origin/main` and rebase

You may see errors and messages about conflicts after pulling.

Rebasing places your local commits on top of the commits from `origin/main`. Conflicts occur when commits from `origin/main` modified the same lines in the same files as your local commits.

Complete the following steps:

1. [Pull and rebase using `GitLens`](#pull-and-rebase-using-gitlens).
2. [Resolve conflicts using `GitLens`](#resolve-conflicts-using-gitlens) (only if conflicts occur).

### Pull and rebase using `GitLens`

1. [Run using the `Command Palette`](../appendix/vs-code.md#run-a-command-using-the-command-palette):
   `GitLens: Pull`
2. [Select](../appendix/vs-code.md#select-an-option-from-a-list)
   `Pull with Rebase`.
3. If `GitLens` does not show any error, the rebase is complete.

### Resolve conflicts using `GitLens`

If you see an error like the one below, resolve the conflicts:

<img alt="Pull Error" src="../images/appendix/gitlens/pull-error.png" style="width:400px"></img>

For each conflicting file, complete the following steps:

1. [Open the `Source Control`](../appendix/vs-code.md#open-the-source-control).
2. Go to `Merge Changes`.
3. Click a conflicting file.
4. Click `Resolve in Merge Editor`.
5. Accept the changes that you want to keep.
6. Click `Complete Merge`.
7. [Open the `Source Control`](../appendix/vs-code.md#open-the-source-control).
8. Click `Continue`.

> **Note:** If there are more conflicts, `VS Code` shows `Rebasing (1/3)` (or similar). Repeat the steps above for each remaining conflict.

<!-- TODO what does VS Code show actually -->

## Switch to a new branch

[Create a new branch and switch to it](../appendix/git-vscode.md#switch-to-a-new-branch).

The name of this branch is referred to as `<branch-name>` throughout the docs.

## Edit files

[Edit files](../appendix/vs-code.md#editor) using `VS Code` to produce changes.

## Commit

[Commit changes](../appendix/git-vscode.md#commit-changes) to the `<branch-name>` to complete the task.

## (Optional) Undo commits

[Undo commits](../appendix/git-vscode.md#undo-commits) if necessary.

## Publish the branch

[Publish the branch](../appendix/git-vscode.md#publish-the-branch) with your changes.

## Push more commits

[Push more commits](../appendix/git-vscode.md#push-more-commits) to the published branch if necessary.

## Create a PR to `main` in your fork

[Create a PR](../appendix/github.md#create-a-pull-request) replacing:

- `<repo-owner-github-username>` with `inno-se-toolkit`;
- `<repo-name>` with `se-toolkit-lab-3`;
- `<your-github-username>` with your `GitHub` username;
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
