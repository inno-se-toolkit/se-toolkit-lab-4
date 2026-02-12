# Identify, report, and fix a bug

<h4>Time</h4>

~40-50 min

<h4>Purpose</h4>

Learn to identify a bug using tests, document it using a `GitHub` issue, and deliver a fix using the `Git workflow`.

<h4>Context</h4>

The web server has a bug in one of its endpoints.
The tests catch this bug.
Your job is to run the tests, understand the failure, find the root cause in the source code, and fix it.

<h4>Table of contents</h4>

- [Steps](#steps)
  - [1. Run the tests](#1-run-the-tests)
  - [2. Read the test output](#2-read-the-test-output)
  - [3. Read the failing test](#3-read-the-failing-test)
  - [4. Find the bug](#4-find-the-bug)
  - [5. Create a bug report issue](#5-create-a-bug-report-issue)
  - [6. Fix the bug](#6-fix-the-bug)
- [Acceptance criteria](#acceptance-criteria)

## Steps

### 1. Run the tests

> [!NOTE]
> [`pytest`](https://docs.pytest.org/) is a testing framework for `Python`.
>
> The tests are in the [`tests/`](../../../tests/) directory.

1. [Run using the `VS Code Terminal`](../../appendix/vs-code.md#run-a-command-using-the-vs-code-terminal):

   ```terminal
   uv run poe test
   ```

2. You should see that one of the tests **fails**.

### 2. Read the test output

1. Look at the test output in the `VS Code Terminal`.
2. Find the name of the failing test.
3. Find the line that says `assert ... == 200`.
4. Notice that the test expected a `200` response but got a `404`.
5. This means the endpoint returned `"Not Found"` when it should have returned an item.

### 3. Read the failing test

1. [Open the file using the `Command Palette`](../../appendix/vs-code.md#open-a-file-using-the-command-palette): [`tests/test_items.py`](../../../tests/test_items.py).
2. Find the failing test function.
3. Read the test to understand:
   - Which endpoint does the test call?
   - What `item_id` does it search for?
   - What does it expect to get back?

### 4. Find the bug

1. The test calls an endpoint that searches for an item by its `id`.
2. [Open the file using the `Command Palette`](../../appendix/vs-code.md#open-a-file-using-the-command-palette): [`src/app/routers/items.py`](../../../src/app/routers/items.py).
3. Find the endpoint that the test calls.
4. Follow the code from the endpoint to the function that performs the search.
5. [Open the file using the `Command Palette`](../../appendix/vs-code.md#open-a-file-using-the-command-palette): [`src/app/services/item_service.py`](../../../src/app/services/item_service.py).
6. Read the search function carefully.
7. Look at each level of the nested loop.
8. Check: does each level compare the correct variable to `item_id`?

### 5. Create a bug report issue

1. Go to your fork on `GitHub`.
2. [Create](https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/creating-an-issue) an issue.
3. Click `Bug Report` when asked about the issue type.
4. Fill in all the fields:
   - **Brief problem description**: describe the bug you found.
   - **Steps to Reproduce**: explain how to reproduce the bug (e.g., run which command).
   - **Expected Result**: what should happen.
   - **Actual Result**: what actually happens.

### 6. Fix the bug

Follow the [`Git workflow`](../git-workflow.md) to complete this step:

1. [Switch to the `main` branch](../git-workflow.md#switch-to-the-main-branch).
2. [Pull changes from `origin/main`](../git-workflow.md#pull-changes-from-originmain).
3. [Switch to a new branch](../git-workflow.md#switch-to-a-new-branch).
4. Fix the bug in the source code.
5. Run the tests again to verify the fix:

   [Run using the `VS Code Terminal`](../../appendix/vs-code.md#run-a-command-using-the-vs-code-terminal):

   ```terminal
   uv run poe test
   ```

6. All tests should pass.
7. [Commit](../git-workflow.md#commit) the fix.
8. [Publish the branch](../git-workflow.md#publish-the-branch).
9. [Create a PR](../git-workflow.md#create-a-pr).
10. [Link the PR](https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/linking-a-pull-request-to-an-issue#linking-a-pull-request-to-an-issue-using-a-keyword) to the bug report issue.
11. [Get a PR review](../git-workflow.md#get-a-pr-review).
12. [Merge the PR](../git-workflow.md#merge-the-pr).
13. [Clean up](../git-workflow.md#clean-up).

---

## Acceptance criteria

- [ ] Bug report issue exists with all fields filled in.
- [ ] The fix branch has a commit that fixes the bug.
- [ ] All tests pass after the fix.
- [ ] PR is linked to the bug report issue.
- [ ] PR is approved.
- [ ] PR is merged.
