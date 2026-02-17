# Implement the `/outcomes` endpoint

<h4>Time</h4>

~60 min

<h4>Purpose</h4>

Practice modifying the database schema and adding a new endpoint by following the existing reference implementation.

<h4>Context</h4>

The Learning Management Service tracks items and learners but does not yet track learning outcomes.

A learning outcome links a learner to an item and records their achievement (e.g., passed, failed, in progress).

You will add an `outcomes` table, create the corresponding Pydantic models, implement the database functions, wire up a new router, and write tests.

<h4>Table of contents</h4>

- [Steps](#steps)
  - [0. Follow the `Git workflow`](#0-follow-the-git-workflow)
  - [1. Create a `Lab Task` issue](#1-create-a-lab-task-issue)
  - [2. Study the reference implementation](#2-study-the-reference-implementation)
  - [3. Modify the database](#3-modify-the-database)
  - [4. Add Pydantic models](#4-add-pydantic-models)
  - [5. Add database functions](#5-add-database-functions)
  - [6. Add the router](#6-add-the-router)
  - [7. Register the router](#7-register-the-router)
  - [8. Add tests](#8-add-tests)
  - [9. Run the tests](#9-run-the-tests)
  - [10. Finish the task](#10-finish-the-task)
- [Acceptance criteria](#acceptance-criteria)

## Steps

### 0. Follow the `Git workflow`

Follow the [`Git workflow`](../git-workflow.md) to complete this task.

### 1. Create a `Lab Task` issue

Title: `[Task] Implement the /outcomes endpoint`

### 2. Study the reference implementation

Study how the `items` endpoint is implemented:

1. Database schema: [`src/app/data/init.sql`](../../../src/app/data/init.sql) (the `items` table).
2. Pydantic models: [`src/app/models/item.py`](../../../src/app/models/item.py).
3. Database functions: [`src/app/db/items.py`](../../../src/app/db/items.py).
4. Router: [`src/app/routers/items.py`](../../../src/app/routers/items.py).

> [!TIP]
> Use the `items` implementation as a template for every step below.

### 3. Modify the database

1. Add an `outcomes` table to [`src/app/data/init.sql`](../../../src/app/data/init.sql).
2. The table should contain at least:
   - `id` (primary key).
   - `learner_id` (foreign key to `learners`).
   - `item_id` (foreign key to `items`).
   - `status` (e.g., `passed`, `failed`, `in_progress`).
   - `created_at` (timestamp).

### 4. Add Pydantic models

1. Create a new file `src/app/models/outcome.py` with Pydantic models for the `/outcomes` endpoint:
   - A model for creating an outcome (see `ItemCreate` in [`src/app/models/item.py`](../../../src/app/models/item.py)).
   - A model for the outcome response (see `Item` in [`src/app/models/item.py`](../../../src/app/models/item.py)).

### 5. Add database functions

1. Create a new file `src/app/db/outcomes.py` with CRUD functions for the `outcomes` table (see [`src/app/db/items.py`](../../../src/app/db/items.py)):
   - Create an outcome.
   - Get all outcomes.
   - Get an outcome by ID.

### 6. Add the router

1. Create a new file `src/app/routers/outcomes.py` (see [`src/app/routers/items.py`](../../../src/app/routers/items.py)).
2. Implement the following endpoints:
   - `POST /outcomes` — create a new outcome.
   - `GET /outcomes` — list all outcomes.
   - `GET /outcomes/{outcome_id}` — get a single outcome by ID.

### 7. Register the router

1. Register the new router in [`src/app/main.py`](../../../src/app/main.py) so the endpoints are available.

### 8. Add tests

1. Write tests for the new endpoints.
2. Test at least:
   - Creating an outcome.
   - Listing outcomes.
   - Getting an outcome by ID.
   - Getting a non-existent outcome (should return `404`).

### 9. Run the tests

1. [Run using the `VS Code Terminal`](../../appendix/vs-code.md#run-a-command-using-the-vs-code-terminal):

   ```terminal
   uv run poe test
   ```

2. All tests should pass.

### 10. Finish the task

1. [Commit](../git-workflow.md#commit) your changes.

   Use the following commit message:

   ```text
   feat: implement /outcomes endpoint
   ```

2. [Create a PR](../git-workflow.md#create-a-pr-to-main-in-your-fork) with your implementation.
3. [Get a PR review](../git-workflow.md#get-a-pr-review) and complete the subsequent steps in the `Git workflow`.

---

## Acceptance criteria

- [ ] Issue has the correct title.
- [ ] The `outcomes` table exists in the database.
- [ ] `POST /outcomes`, `GET /outcomes`, and `GET /outcomes/{outcome_id}` endpoints work.
- [ ] All tests pass.
- [ ] PR is approved.
- [ ] PR is merged.
