# Set up CI with `GitHub Actions`

<h4>Time</h4>

~30 min

<h4>Purpose</h4>

Practice setting up continuous integration so that every pull request is automatically checked for correctness.

<h4>Context</h4>

Currently, tests and code quality checks are run manually on each developer's machine.

You will create a `GitHub Actions` workflow that runs tests and static checks (`ruff`, type checking) on each pull request. Then you will add a branch protection rule requiring CI to pass before merging.

<h4>Table of contents</h4>

- [Steps](#steps)
  - [0. Follow the `Git workflow`](#0-follow-the-git-workflow)
  - [1. Create a `Lab Task` issue](#1-create-a-lab-task-issue)
  - [2. Study `GitHub Actions`](#2-study-github-actions)
  - [3. Create the workflow file](#3-create-the-workflow-file)
  - [4. Define the workflow](#4-define-the-workflow)
  - [5. Push and verify](#5-push-and-verify)
  - [6. Add branch protection](#6-add-branch-protection)
  - [7. Finish the task](#7-finish-the-task)
- [Acceptance criteria](#acceptance-criteria)

## Steps

### 0. Follow the `Git workflow`

Follow the [`Git workflow`](../../../wiki/git-workflow.md) to complete this task.

### 1. Create a `Lab Task` issue

Title: `[Task] Set up CI with GitHub Actions`

### 2. Study `GitHub Actions`

1. Read the [`GitHub Actions` quickstart](https://docs.github.com/en/actions/writing-workflows/quickstart).
2. Understand the concepts: workflow, job, step, trigger.

### 3. Create the workflow file

1. Create the file `.github/workflows/ci.yml`.

> [!NOTE]
> `GitHub Actions` workflows are defined as `YAML` files inside the `.github/workflows/` directory.

### 4. Define the workflow

1. The workflow should be triggered on pull requests to the `main` branch.
2. The workflow should contain a job that:
   1. Checks out the repository.
   2. Installs `uv`.
   3. Installs dependencies using `uv sync`.
   4. Runs the linter (`uv run poe lint`).
   5. Runs the type checker (`uv run poe typecheck`).
   6. Starts the server in one [process](../../../wiki/linux.md#process) (`uv run poe dev`).
   7. Runs the tests in another process (`uv run poe test`).

> [!TIP]
> Use the `astral-sh/setup-uv` action to install `uv` in the CI environment.

### 5. Push and verify

1. Commit your changes.
2. Push the branch.
3. Create a PR to `main`.
4. Verify that the `GitHub Actions` workflow runs and passes on the PR.

> [!TIP]
> You can see the workflow status in the `Checks` tab of the PR on `GitHub`.

### 6. Add branch protection

1. [Go to your fork](../../../wiki/github.md#go-to-your-fork).
2. Go to `Settings` -> `Rules` -> `Rulesets`.
3. Edit the existing `push` ruleset.
4. Add the rule:
   - [x] `Require status checks to pass`:
      - Add the CI job name as a required status check.

### 7. Finish the task

1. [Get a PR review](../../../wiki/git-workflow.md#get-a-pr-review) on the PR you created in [Step 5](#5-push-and-verify) and complete the subsequent steps in the `Git workflow`.

---

## Acceptance criteria

- [ ] Issue has the correct title.
- [ ] The workflow file `.github/workflows/ci.yml` exists.
- [ ] The workflow runs on pull requests to `main`.
- [ ] The workflow runs linting, type checking, and tests.
- [ ] The workflow passes on the PR.
- [ ] Branch protection requires the CI check to pass.
- [ ] PR is approved.
- [ ] PR is merged.
