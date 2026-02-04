# Procedure for each task

> [!NOTE]
> This procedure is based on the [`GitHub flow`](https://docs.github.com/en/get-started/using-github/github-flow).

```text
┌───────┐    ┌────────┐    ┌─────────┐    ┌────┐    ┌────────┐    ┌───────┐
│ Issue │ →  │ Branch │ →  │ Commits │ →  │ PR │ →  │ Review │ →  │ Merge │
└───────┘    └────────┘    └─────────┘    └────┘    └────────┘    └───────┘
```

1. [Create](https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/creating-an-issue) a `GitHub` issue in your forked repo using the `Lab Task` [issue form](https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/configuring-issue-templates-for-your-repository#creating-issue-forms).
2. Create a new branch for the issue via [`GitHub`](https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/creating-a-branch-for-an-issue) or via `git checkout -b <branch-name>`.
3. <details><summary> Make <a href="https://smartprogramming.in/tutorials/git-and-github/git-commit">commits</a> to that branch to complete the task (click to expand).</summary>

     - Commit messages should (not must) follow the [`Conventional Commits`](https://www.conventionalcommits.org/en/v1.0.0/) format.
     - Commit to the branch using one of these approaches:
       1. Using `VS Code` (see [docs](https://code.visualstudio.com/docs/sourcecontrol/staging-commits)): `Activity Bar` -> `Source Control` -> `Changes` -> Click a file -> Select changed lines in the editor (red-green) -> Right mouse click the selected lines -> Click `Stage Selected Ranges` -> Write a commit message -> Click `Commit`.
       2. Using a terminal (adds all changes in specified files to the [staging area](https://smartprogramming.in/tutorials/git-and-github/git-add-files-to-staging)):

          ```console
          git add <file 1> <file 2> ... <file n>
          git commit -m "<message>"
          ```

   </details>

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

As a PR reviewer, you must:

- Review the assigned PR.
- Leave at least 2 meaningful comments highlighting [particular lines](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/reviewing-changes-in-pull-requests/commenting-on-a-pull-request#adding-comments-to-a-pull-request). It's enough to select line(s), write a comment and click `Comment`.
- Click `Submit review` if you clicked `Start a review` before.
- Approve the PR if you're satisfied with the PR.

As a PR author, you must:

- Reply to comments in a meaningful way, e.g., write “Fixed in d0d5aeb” (`d0d5aeb` being the id of commit where you addressed the comment), ask to clarify the comment, or explain why you disagree.
- Make necessary changes based on the review.
