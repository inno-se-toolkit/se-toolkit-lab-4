# Add a CI check

1. Create the issue `[Task] Add a CI check`.
2. Read [Quickstart for `GitHub Actions`](https://docs.github.com/en/actions/get-started/quickstart).
3. Enable [`GitHub Actions`](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/enabling-features-for-your-repository/managing-github-actions-settings-for-a-repository) for your fork.
4. Search for `markdownlint` on [GitHub Actions Marketplace](https://github.com/marketplace?type=actions).
5. Write a workflow that uses the [`DavidAnson/markdownlint-cli2-action`](https://github.com/DavidAnson/markdownlint-cli2-action) and runs on each push to PR.
6. Commit changes and publish the branch.
7. Open a PR to `main` and make sure the workflow passes without warnings.
8. Provide a link to the PR in the issue description.
9. Close the PR. Don't merge it.
10. Close the issue.
