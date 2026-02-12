# Identify, report, and fix a bug

<h4>Time</h4>

~40-50 min

<h4>Purpose</h4>

Learn to identify a bug using tests, document it using a `GitHub` issue, and deliver a fix using the `Git workflow`.

<h4>Context</h4>

The web server has a bug in one of its [endpoints](../../appendix/web-development.md#endpoint).
The tests catch this bug.
Your job is to run the tests, understand the failure, find the root cause in the source code, and fix it.

<h4>Table of contents</h4>

- [Steps](#steps)
  - [0. Follow the `Git workflow`](#0-follow-the-git-workflow)
  - [1. Create a `Lab Task` issue](#1-create-a-lab-task-issue)
  - [2. Run the web server](#2-run-the-web-server)
  - [3. Run the tests](#3-run-the-tests)
  - [4. Create a bug report issue](#4-create-a-bug-report-issue)
  - [5. Read the test output](#5-read-the-test-output)
  - [6. Find the test code](#6-find-the-test-code)
  - [7. Inspect the test code](#7-inspect-the-test-code)
  - [8. Understand the response](#8-understand-the-response)
  - [9. Determine the endpoint](#9-determine-the-endpoint)
  - [10. Find the code for that endpoint](#10-find-the-code-for-that-endpoint)
  - [11. Inspect the `get_item` function](#11-inspect-the-get_item-function)
  - [12. Inspect the `get_item_by_id` function](#12-inspect-the-get_item_by_id-function)
  - [13. Inspect the `get_item_by_id_dfs_iterative` function](#13-inspect-the-get_item_by_id_dfs_iterative-function)
  - [14. Find the bug](#14-find-the-bug)
  - [15. Fix the bug](#15-fix-the-bug)
  - [16. Commit the change](#16-commit-the-change)
  - [17. Finish the task](#17-finish-the-task)
- [Acceptance criteria](#acceptance-criteria)

## Steps

### 0. Follow the `Git workflow`

Follow the [`Git workflow`](../git-workflow.md) to complete this task.

### 1. Create a `Lab Task` issue

Title: `[Task] Identify, report, and fix a bug`.

### 2. Run the web server

1. [Run the web server](./task-1.md#7-run-the-web-server).
2. [Send a `GET` query](../../appendix/web-development.md#send-a-get-query)
   to [`http://127.0.0.1:42000/items/item/lab-02-run-local-venv`](http://127.0.0.1:42000/items/item/lab-02-run-local-venv).
3. [Pretty-print the `JSON` response](../../appendix/web-development.md#pretty-print-a-json-response).

### 3. Run the tests

> [!NOTE]
> [`pytest`](https://docs.pytest.org/) is a testing framework for `Python`.
>
> The tests are in the [`tests/`](../../../tests/) directory.

1. [Open a new `VS Code Terminal`](../../appendix/vs-code.md#open-a-new-vs-code-terminal).
2. [Run using the `VS Code Terminal`](../../appendix/vs-code.md#run-a-command-using-the-vs-code-terminal):

   ```terminal
   uv run poe test
   ```

3. You should see that one of the tests **fails**.

### 4. Create a bug report issue

1. [Create a `Bug Report` issue](../../appendix/github.md#create-an-issue).
2. Describe what you did, what you expected to see and what you got.

### 5. Read the test output

1. Look at the test output in the [`VS Code Terminal`](../../appendix/vs-code.md#vs-code-terminal).
2. Look at the `short test summary info`.
3. You should see `FAILED tests/test_items.py::test_get_item_1 - assert 404 == 200`.

   This line means the following:
   - The test failed (`FAILED`).
   - The test is in the file [`tests/test_items.py`](../../../tests/test_items.py).
   - The name of the failing test is `test_get_item_1`.
   - The [assert](../../appendix/testing.md#assert-statements) that failed is `404 == 200`.

### 6. Find the test code

1. Go to [`tests/test_items.py`](../../../tests/test_items.py).
2. Go to the function `test_get_item_1`.
3. Go to the helper function `get_task_by_id` called by `test_get_item_1`.

### 7. Inspect the test code

1. The test makes a request to the web server [endpoint](../../appendix/web-development.md#endpoint) (`client.get(<endpoint>)`).
2. The test asserts that the [response status code](../../appendix/web-development.md#http-response-status-code) is `200`.
3. The web server, however, returns the `404` [response status code](../../appendix/web-development.md#http-response-status-code).
4. Hence, the assert fails.

### 8. Understand the response

1. Read about the [`404` response status code](../../appendix/web-development.md#404-response-status-code).
2. This code means that the web server couldn't find the requested resource.

### 9. Determine the endpoint

1. The request is to the endpoint `/items/item/{task_id}`.

   This endpoint should return a task information by the `task_id`.

   **Note:** The [query parameter](../../appendix/web-development.md#query-parameter) `?order={order}` doesn't matter if the web server can't find the endpoint.

### 10. Find the code for that endpoint

1. Go to [`src/app/routers/items.py`](../../../src/app/routers/items.py).
2. Go to the function `get_item`.

### 11. Inspect the `get_item` function

1. Look at the last line of the function `get_item`:

   ```python
   raise HTTPException(status_code=404, detail="Item not found")
   ```

   This line is executed if the function didn't return any value before.

   The response of the web server was `404`.

   This means that this line was executed.

2. Look at the line where the `item` variable gets a value:

   ```python
   item = get_item_by_id(item_id, order=order_parsed)
   ```

   The function `get_item_by_id` searches for an item in a given order.

3. Look at where `get_item` can return:

   ```python
   if item is not None:
      return item
   ```

   Since the function didn't return, the value of `item` was `None`.

   This means that the function `get_item_by_id` returned `None`.

### 12. Inspect the `get_item_by_id` function

1. [Hover over the `get_item_by_id` function name to see its type](../../appendix/vs-code.md#type-on-hover):

   <img alt="Type on Hover" src="../../images/appendix/vs-code/hover-type.png" style="width:400px"></img>

   The  `-> (FoundItem | None)` means that the function returns either a `FoundItem` or `None`.

2. [Go to the `get_item_by_id` function definition](../../appendix/vs-code.md#go-to-the-definition).

3. Inspect the `courses` variable:

   ```python
   courses: list[Course] = read_courses()
   ```

   The variable `courses` contains a list of objects of the class `Course`.

   This list is produced by the call of to the function `read_courses()`.

   Assume for now that the `read_courses()` correctly reads all available data
   from the [`course_items.json`](../../../src/app/data/course_items.json) `JSON` document.

4. Inspect the `return` statement:

   ```python
   return get_item_by_id_dfs_iterative(courses=courses, item_id=item_id, order=order)
   ```

   The function `get_item_by_id` returns the result of the call to the function `get_item_by_id_dfs_iterative`.

   Since the `get_item_by_id` returned `None`, the `get_item_by_id_dfs_iterative` should also have returned `None`.

### 13. Inspect the `get_item_by_id_dfs_iterative` function

1. [Go to the definition](../../appendix/vs-code.md#go-to-the-definition) of `get_item_by_id_dfs_iterative`.
2. Study the function [docstring](../../appendix/python.md#docstring).
3. [Hover over the `get_item_by_id_dfs_iterative` function name to see the docs](../../appendix/vs-code.md#docs-on-hover).
4. The function uses the [depth-first search](https://en.wikipedia.org/wiki/Tree_traversal#Depth-first_search) to find an item.

### 14. Find the bug

1. Try to find the bug in the function.

   As [mentioned before](#9-determine-the-endpoint), the function can't find a task by the `item_id`.

2. <details><summary>Click to open a hint</summary>

   The bug can be here:

   ```python
   for task in lab.tasks:
      counter += 1
      if lab.id == item_id:
            return FoundItem(task, counter)
   ```

   </details>

3. <details><summary>Click to open the solution</summary>

   The problem is in the `if`-condition.

   It never checks that the `task.id == item_id`.

   Therefore, the function can never find a task by its id.

   </details>

### 15. Fix the bug

1. Write the correct code.
2. [Run the tests](#3-run-the-tests) again to see that all tests pass.

### 16. Commit the change

1. [Commit your change using the `Source Control`](../../tasks/git-workflow.md#commit-using-source-control).

   Use a multi-line message:

   ```text
   fix: bug in the dfs logic
   
   - task.id was never checked
   ```

### 17. Finish the task

1. [Create a PR](../../tasks/git-workflow.md#create-a-pr) with your fix.

   **Note:** the PR closes the `Bug Report` issue, not the `Lab Task` issue.

   Keep that in mind when editing the `- Closes #<issue-number>` line.
2. Provide a link to the `Bug Report` in the `Lab Task` issue.
3. [Get a PR review](../../tasks/git-workflow.md#get-a-pr-review) and complete the subsequent steps in the `Git workflow`.

---

## Acceptance criteria

- [ ] `Lab Task` issue description has a link to the `Bug Report` issue.
- [ ] `Bug Report` issue has a `bug` label.
- [ ] The fix branch has a commit with the [specified message](#16-commit-the-change).
- [ ] All tests pass after the fix.
- [ ] PR is linked to the bug report issue.
- [ ] PR is approved.
- [ ] PR is merged.
