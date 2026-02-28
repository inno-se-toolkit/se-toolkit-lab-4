# `Git workflow` for tasks

> [!NOTE]
> This procedure is based on the [`GitHub flow`](./github.md#github-flow).

```text
Issue ➜ Branch ➜ Commits ➜ PR ➜ Review ➜ Merge
```

The following diagram shows this workflow in the context of repositories:

<img alt="Git workflow" src="./images/git-workflow/git-workflow.drawio.svg" style="width:100%"></img>

Outline:

- [Create a `Lab Task` issue](#create-a-lab-task-issue)
- [Switch to the `main` branch](#switch-to-the-main-branch)
- [Detect conflicts](#detect-conflicts)
- [Pull changes from `origin/main`](#pull-changes-from-originmain)
- [Pull changes from `origin/main` and rebase](#pull-changes-from-originmain-and-rebase)
- [Switch to a new branch](#switch-to-a-new-branch)
  - [`<task-branch-name>`](#task-branch-name)
- [Edit files](#edit-files)
- [Commit](#commit)
- [(Optional) Undo commits](#optional-undo-commits)
- [Publish the branch](#publish-the-branch)
- [Push more commits](#push-more-commits)
- [Create a PR to the `main` branch in your fork](#create-a-pr-to-the-main-branch-in-your-fork)
- [Get a PR review](#get-a-pr-review)
  - [PR review rules](#pr-review-rules)
    - [As a PR reviewer](#as-a-pr-reviewer)
    - [As a PR author](#as-a-pr-author)
- [Merge the PR](#merge-the-pr)
- [Clean up](#clean-up)

## Create a `Lab Task` issue

[Create an issue](./github.md#create-an-issue) using the `Lab Task` [issue form](./github.md#issue-form).

## Switch to the `main` branch

[Switch to the `main` branch](./git-vscode.md#switch-to-the-branch-name-branch) in `VS Code`.

## Detect conflicts

[Detect conflicts with the `origin/main`](./git-vscode.md#detect-conflicts).

## Pull changes from `origin/main`

[Pull changes from the `main` branch in your fork on `GitHub`](./git-vscode.md#pull-changes-from-originbranch-name).

## Pull changes from `origin/main` and rebase

You may see errors and messages about conflicts after pulling.

Rebasing places your local commits on top of the commits from `origin/main`. Conflicts occur when commits from `origin/main` modified the same lines in the same files as your local commits.

Complete the following steps:

1. [Pull and rebase from `origin/main`](./git-vscode.md#pull-changes-from-originbranch-name-and-rebase).
2. If conflicts occur, [resolve them](./git-vscode.md#resolve-a-merge-conflict).

## Switch to a new branch

[Create a new branch and switch to it](./git-vscode.md#switch-to-a-new-branch).

### `<task-branch-name>`

We'll refer to the new branch as `<task-branch-name>`.

## Edit files

[Edit files](./vs-code.md#editor) using `VS Code` to produce changes.

## Commit

[Commit changes](./git-vscode.md#commit-changes) to the [`<task-branch-name>`](#task-branch-name) to complete the task.

## (Optional) Undo commits

[Undo commits](./git-vscode.md#undo-commits) if necessary.

## Publish the branch

[Publish the branch](./git-vscode.md#publish-the-branch) with your changes.

## Push more commits

[Push more commits](./git-vscode.md#push-more-commits) to the published branch if necessary.

## Create a PR to the `main` branch in your fork

[Create a PR](./github.md#create-a-pull-request-in-your-fork) from the branch [`<task-branch-name>`](#task-branch-name) to the branch `<main>`.
Placeholder values:

- `<repo-name>` is `se-toolkit-lab-<N>` where `<N>` is the number of the lab.
- `<branch-name>` is `<task-branch-name>`.
- [`<repo-owner-github-username>`] is `inno-se-toolkit`.
- [`<your-github-username>`](./github.md#your-github-username) is your `GitHub` username.

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

<!-- What should you see? -->
<!-- make prs in your fork should be not ok -->

## Clean up

Close the issue.

Delete the PR branch.
