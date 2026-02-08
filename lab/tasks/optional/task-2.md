# Add a CI check

**Time:** ~30-40 min

**Purpose:** Learn how to set up continuous integration checks to ensure code quality and catch issues early in the development process.

**Context:** As a software engineer, you'll often need to set up automated checks that run on every pull request to maintain code quality standards.

- [Steps](#steps)
  - [1. Create an issue](#1-create-an-issue)
  - [2. Read documentation](#2-read-documentation)
  - [3. Enable GitHub Actions](#3-enable-github-actions)
  - [4. Create the workflow file](#4-create-the-workflow-file)
  - [5. Add the check job](#5-add-the-check-job)
  - [6. Commit and publish](#6-commit-and-publish)
  - [7. Open a PR](#7-open-a-pr)
  - [8. Document the PR](#8-document-the-pr)
  - [9. Close the PR](#9-close-the-pr)
  - [10. Close the issue](#10-close-the-issue)
- [Acceptance criteria](#acceptance-criteria)

## Steps

### 1. Create an issue

Title: `[Task] Add a CI check`

### 2. Read documentation

Read [Quickstart for `GitHub Actions`](https://docs.github.com/en/actions/get-started/quickstart).

### 3. Enable GitHub Actions

Enable [`GitHub Actions`](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/enabling-features-for-your-repository/managing-github-actions-settings-for-a-repository) for your fork.

### 4. Create the workflow file

In `.github/workflows/ci.yml`, write a `GitHub Actions` workflow that runs on PRs and on push.

### 5. Add the check job

Add the `check` job that runs these checks:

1. Check `Markdown` files using a linter - [`DavidAnson/markdownlint-cli2-action`](https://github.com/DavidAnson/markdownlint-cli2-action).
2. Check links in `Markdown` files - [`tcort/github-action-markdown-link-check`](https://github.com/tcort/github-action-markdown-link-check#how-to-use).

### 6. Commit and publish

Commit changes and publish the branch.

### 7. Open a PR

Open a PR to `main` and make sure the workflow passes without warnings.

### 8. Document the PR

Provide a link to the PR in the issue description.

### 9. Close the PR

Close the PR. Don't merge it.

### 10. Close the issue

Close the issue.

## Acceptance criteria

- [ ] Issue created with a correct title
- [ ] `.github/workflows/ci.yml` created with proper workflow
- [ ] Workflow runs on PRs and push
- [ ] `Markdown` linter check is included
- [ ] `Markdown` link checker is included
- [ ] PR opened and workflow passes without warnings
- [ ] Link to PR added to issue description
- [ ] PR closed without merging
- [ ] Issue closed
