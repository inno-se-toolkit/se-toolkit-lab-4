# `Git workflow` for tasks

> [!NOTE]
> This procedure is based on the [`GitHub flow`](https://docs.github.com/en/get-started/using-github/github-flow).

```text
┌───────┐    ┌────────┐    ┌─────────┐    ┌────┐    ┌────────┐    ┌───────┐
│ Issue │ →  │ Branch │ →  │ Commits │ →  │ PR │ →  │ Review │ →  │ Merge │
└───────┘    └────────┘    └─────────┘    └────┘    └────────┘    └───────┘
```

1. [Create](https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/creating-an-issue) a `GitHub` issue in your forked repo using the `Lab Task` [issue form](https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/configuring-issue-templates-for-your-repository#creating-issue-forms).
2. Create a new branch for the issue via [`GitHub`](https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/creating-a-branch-for-an-issue) or via `git checkout -b <branch-name>`.
3. Make commits to that branch to complete the task. You can use either terminal or VS Code.

   **Commit message format:** `type: short description`

   Common types:
   - `docs:` — documentation changes (most common in this lab)
   - `feat:` — new functionality
   - `fix:` — bug fixes

   **Using terminal:**

   ```console
   git add <file>                                 # e.g., git add docs/architecture.md
   git commit -m "<type>: <short description>"    # e.g., git commit -m "docs: add architecture diagram"
   ```

   **Using `VS Code`:**

   1. Open [`Source Control`](../../appendix/vs-code.md#source-control).
   2. Click `+` next to changed files to stage them.
   3. Type commit message, e.g., `docs: add architecture diagram`.
   4. Click `Commit`.

   **Using `VS Code` (commit specific parts of a file):**

   1. Open [`Source Control`](../../appendix/vs-code.md#source-control).
   2. Go to `Changes`.
   3. Click a file.
   4. Select changed lines in the editor (red-green).
   5. Right mouse click the selected lines.
   6. Click `Stage Selected Ranges`.
   7. Go to `Changes`.
   8. Write a commit message.
   9. Click `Commit`.

4. Push the branch to your forked repo:

    ```console
    git push -u origin <branch-name>
    ```

5. Create a PR to the `main` branch via [`GitHub`](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request) ([tutorial](https://www.geeksforgeeks.org/git/creating-a-pull-request-on-any-public-repository-from-github-using-vs-code/)) or via the [`GitHub Pull Requests` extension](https://code.visualstudio.com/docs/sourcecontrol/github#_pull-requests).
6. Write an appropriate PR description following the PR template.
7. [Link the PR](https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/linking-a-pull-request-to-an-issue#linking-a-pull-request-to-an-issue-using-a-keyword) to the issue, e.g. `Closes #<issue number>`.
8. [Request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/requesting-a-pull-request-review#requesting-reviews-from-collaborators-and-organization-members) a review of the PR from the collaborator (see [PR reviews](#pr-reviews)).
9. Get the collaborator's comments and address them, e.g., make fixes or ask to clarify the comment.
10. Get the collaborator to approve the PR.
11. Merge the PR to the `main` branch.
12. Close the issue.
13. Delete the PR branch.

## PR reviews

As a PR reviewer:

1. Check the task's **Acceptance criteria**.
2. Leave at least one [comment](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/reviewing-changes-in-pull-requests/commenting-on-a-pull-request#adding-comments-to-a-pull-request) — point out problems or confirm that items look good.
3. Approve the PR when all relevant acceptance criteria are met.

As a PR author:

- Address reviewer comments (fix issues or explain your reasoning).
- Reply to comments, e.g., "Fixed in d0d5aeb".
