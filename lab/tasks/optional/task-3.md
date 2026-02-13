# Implement the post-order traversal

<h4>Time</h4>

~30-40 min

<h4>Purpose</h4>

Learn to implement a tree traversal algorithm.

<h4>Context</h4>

The function `get_item_by_id_dfs_iterative` in [`src/app/services/item_service.py`](../../../src/app/services/item_service.py) uses
[depth-first search](https://en.wikipedia.org/wiki/Tree_traversal#Depth-first_search) to find an item by its id.

The [pre-order](https://en.wikipedia.org/wiki/Tree_traversal#Pre-order,_NLR) traversal is already implemented.
The [post-order](https://en.wikipedia.org/wiki/Tree_traversal#Post-order,_LRN) traversal is not.

<h4>Table of contents</h4>

- [0. Follow the `Git workflow`](#0-follow-the-git-workflow)
- [Steps](#steps)
  - [1. Create an issue](#1-create-an-issue)
  - [2. Study the pre-order implementation](#2-study-the-pre-order-implementation)
  - [3. Study the post-order definition](#3-study-the-post-order-definition)
  - [4. Implement the post-order traversal](#4-implement-the-post-order-traversal)
  - [5. Add tests](#5-add-tests)
  - [6. Run the tests](#6-run-the-tests)
  - [7. Finish the task](#7-finish-the-task)
- [Acceptance criteria](#acceptance-criteria)

## 0. Follow the `Git workflow`

Follow the [`Git workflow`](../git-workflow.md) to complete this task.

## Steps

### 1. Create an issue

Title: `[Task] Implement the post-order traversal`

### 2. Study the pre-order implementation

1. Open [`src/app/services/item_service.py`](../../../src/app/services/item_service.py).
2. Find the function `get_item_by_id_dfs_iterative`.
3. Study the `PreOrder()` case.

   In pre-order traversal, the node is visited **before** its children.

### 3. Study the post-order definition

1. Read about [post-order traversal](https://en.wikipedia.org/wiki/Tree_traversal#Post-order,_LRN).

   In post-order traversal, the node is visited **after** its children.

### 4. Implement the post-order traversal

1. Find the `PostOrder()` case in the `get_item_by_id_dfs_iterative` function.
2. You should see:

   ```python
   case PostOrder():
       # TODO implement
       pass
   ```

3. Replace it with the post-order traversal logic.

> [!TIP]
> You can study the recursive implementation of post-order in `get_item_by_id_dfs_recursive`
> in the same file for reference.

### 5. Add tests

1. Open [`tests/test_items.py`](../../../tests/test_items.py).
2. Add a test that calls the endpoint with `?order=post` and verifies the response.

### 6. Run the tests

1. [Run using the `VS Code Terminal`](../../appendix/vs-code.md#run-a-command-using-the-vs-code-terminal):

   ```terminal
   uv run poe test
   ```

2. All tests should pass.

### 7. Finish the task

1. Commit your changes.
2. [Create a PR](../git-workflow.md#create-a-pr) and [get a review](../git-workflow.md#get-a-pr-review).

---

## Acceptance criteria

- [ ] Issue has the correct title
- [ ] Post-order traversal is implemented in `get_item_by_id_dfs_iterative`
- [ ] Tests for post-order traversal are added
- [ ] All tests pass
- [ ] PR is approved
- [ ] PR is merged
