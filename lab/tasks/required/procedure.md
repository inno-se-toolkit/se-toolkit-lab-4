# `Git workflow` for tasks

> [!NOTE]
> This procedure is based on the [`GitHub flow`](https://docs.github.com/en/get-started/using-github/github-flow).

```text
┌───────┐    ┌────────┐    ┌─────────┐    ┌────┐    ┌────────┐    ┌───────┐
│ Issue │ →  │ Branch │ →  │ Commits │ →  │ PR │ →  │ Review │ →  │ Merge │
└───────┘    └────────┘    └─────────┘    └────┘    └────────┘    └───────┘
```

## Create an issue

[Create](https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/creating-an-issue) a `GitHub` issue in your forked repo using the `Lab Task` [issue form](https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/configuring-issue-templates-for-your-repository#creating-issue-forms) (defined in [`.github/ISSUE_TEMPLATE/01-task.yml`](../../../.github/ISSUE_TEMPLATE/01-task.yml)).

## Create a branch

Create a new branch for the issue using one of these ways:

### Using `GitHub`

1. [Create a branch](https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/creating-a-branch-for-an-issue).
1. Copy the command.
1. [Open the `Terminal`](../../appendix/vs-code.md#open-the-terminal).
1. Paste the command to the `Terminal`.
1. Press `Enter` to run the command.

### Using `Terminal`

1. [Open the `Terminal`](../../appendix/vs-code.md#open-the-terminal).
2. [Run](../../appendix/vs-code.md#run-a-command-using-the-terminal):

    ```console
    git checkout -b <branch-name>
    ```

### Using `VS Code`

1. [Open the `Command Palette`](../../appendix/vs-code.md#open-the-command-palette).
2. Run `GitLens: Git Create Branch...`.

## Make commits

Make commits to that branch to complete the task.

### Commit message format

Format: `type: short description`

Common types:

- `docs:` — documentation changes (most common in this lab)
- `feat:` — new functionality
- `fix:` — bug fixes

### Commit using the `Terminal`

1. Open the [`Terminal`](../../appendix/vs-code.md#open-the-terminal).
2. Run:

  ```console
  git add <file>                                 # e.g., git add docs/architecture.md
  git commit -m "<type>: <short description>"    # e.g., git commit -m "docs: add architecture diagram"
  ```

### Commit using `Source Control`

1. [Open the `Source Control`](../../appendix/vs-code.md#open-the-source-control).
2. Click `+` next to changed files to stage them.
3. Type commit message, e.g., `docs: add architecture diagram`.
4. Click `Commit`.

### Commit using `Source Control` (specific changes)

1. [Open the `Source Control`](../../appendix/vs-code.md#open-the-source-control).
2. Go to `Changes`.
3. Click a file.
4. Select changed lines in the editor (red-green).
5. Right mouse click the selected lines.
6. Click `Stage Selected Ranges`.
7. Go to `Changes`.
8. Write a commit message.
9. Click `Commit`.

## Push the branch

Push the branch to your forked repo:

```console
git push -u origin <branch-name>
```

## Create a PR

Create a PR to the `main` branch via [`GitHub`](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request#creating-the-pull-request) or via the [`GitHub Pull Requests` extension](https://code.visualstudio.com/docs/sourcecontrol/github#_pull-requests).

Write an appropriate PR description following the PR template.

[Link the PR](https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/linking-a-pull-request-to-an-issue#linking-a-pull-request-to-an-issue-using-a-keyword) to the issue, e.g. `Closes #<issue number>`.

## Get a PR review

[Request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/requesting-a-pull-request-review#requesting-reviews-from-collaborators-and-organization-members) a review of the PR from the collaborator (see [PR review rules](#pr-review-rules)).

Get the collaborator's comments and address them, e.g., make fixes or ask to clarify the comment.

Get the collaborator to approve the PR.

### PR review rules

#### As a PR reviewer

1. Check the task's **Acceptance criteria**.
2. Leave at least one [comment](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/reviewing-changes-in-pull-requests/commenting-on-a-pull-request#adding-comments-to-a-pull-request) — point out problems or confirm that items look good.
3. Approve the PR when all relevant acceptance criteria are met.

#### As a PR author

- Address reviewer comments (fix issues or explain your reasoning).
- Reply to comments, e.g., "Fixed in d0d5aeb".

## Merge the PR

Merge the PR to the `main` branch.

## Clean up

Close the issue.

Delete the PR branch.

## Pull changes

In the repository on your computer, switch to `main` and pull changes:

```console
git switch main
git pull
```
