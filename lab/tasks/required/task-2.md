# Enable and debug a broken endpoint

<h4>Time</h4>

~40-50 min

<h4>Purpose</h4>

Learn to debug a broken endpoint by tracing code and examining the database using `PgAdmin`.

<h4>Context</h4>

The `/interactions` endpoint code exists but is disabled by a feature flag. It contains two bugs: a schema-database mismatch and a logic error.
Your job is to enable the endpoint, discover the bugs, and fix them.

<h4>Table of contents</h4>

- [Steps](#steps)
  - [0. Follow the `Git workflow`](#0-follow-the-git-workflow)
  - [1. Create a `Lab Task` issue](#1-create-a-lab-task-issue)
  - [2. Examine the database using `PgAdmin`](#2-examine-the-database-using-pgadmin)
  - [3. Enable the interactions endpoint](#3-enable-the-interactions-endpoint)
  - [4. Restart the services](#4-restart-the-services)
  - [5. Try `GET /interactions`](#5-try-get-interactions)
  - [6. Read the error](#6-read-the-error)
  - [7. Trace the bug](#7-trace-the-bug)
  - [8. Fix Bug 1: rename `timestamp` to `created_at`](#8-fix-bug-1-rename-timestamp-to-created_at)
  - [9. Verify `GET /interactions` works](#9-verify-get-interactions-works)
  - [10. Commit Bug 1 fix](#10-commit-bug-1-fix)
  - [11. Try `GET /interactions?item_id=2`](#11-try-get-interactionsitem_id2)
  - [12. Compare with the database](#12-compare-with-the-database)
  - [13. Find Bug 2 in the code](#13-find-bug-2-in-the-code)
  - [14. Fix Bug 2: filter by `item_id`](#14-fix-bug-2-filter-by-item_id)
  - [15. Commit Bug 2 fix](#15-commit-bug-2-fix)
  - [16. Finish the task](#16-finish-the-task)
- [Acceptance criteria](#acceptance-criteria)

## Steps

### 0. Follow the `Git workflow`

Follow the [`Git workflow`](../git-workflow.md) to complete this task.

### 1. Create a `Lab Task` issue

Title: `[Task] Enable and debug the interactions endpoint`

### 2. Examine the database using `PgAdmin`

1. [Open `PgAdmin`](../../appendix/pgadmin.md#open-pgadmin).
2. [Add a server in `PgAdmin`](../../appendix/pgadmin.md#add-a-server-in-pgadmin).
3. [Inspect columns](../../appendix/pgadmin.md#inspect-columns) of the `interaction_logs` table.
4. Note the column names: `id`, `learner_id`, `item_id`, `kind`, `created_at`.

> [!NOTE]
> Pay attention to the column name `created_at`. You will need it later.

### 3. Enable the interactions endpoint

1. [Open the file](../../appendix/vs-code.md#open-the-file):
   `.env.docker.secret`.
2. Change:

   ```text
   ENABLE_INTERACTIONS=false
   ```

   to:

   ```text
   ENABLE_INTERACTIONS=true
   ```

3. Save the file.

> [!NOTE]
> `.env.docker.secret` is listed in `.gitignore` and will not be committed.
> The flag tells the application to register the `/interactions` route at startup.

### 4. Restart the services

1. [Run using the `VS Code Terminal`](../../appendix/vs-code.md#run-a-command-using-the-vs-code-terminal):

   ```terminal
   docker compose --env-file .env.docker.secret up --build
   ```

> **Tip:** If the services are still running, press `Ctrl+C` first to stop them, then run the command above.

### 5. Try `GET /interactions`

1. Open `Swagger UI` at `http://127.0.0.1:42001/docs`.
2. [Authorize](./task-1.md#6-authorize-in-swagger-ui) with the API key.
3. Expand the `GET /interactions` endpoint.
4. Click `Try it out`.
5. Click `Execute`.
6. Observe the response: you should see a `500` Internal Server Error.

### 6. Read the error

1. Look at the error response in `Swagger UI`.
2. Look at the application logs in the terminal where `Docker Compose` is running.
3. The error mentions a missing or mismatched field: `timestamp`.

### 7. Trace the bug

1. [Open the file](../../appendix/vs-code.md#open-the-file):
   [`src/app/models/interaction.py`](../../../src/app/models/interaction.py).
2. Look at the `InteractionModel` class (the response schema):

   ```python
   class InteractionModel(SQLModel):
       id: int
       learner_id: int
       item_id: int
       kind: str
       timestamp: datetime
   ```

3. The response schema has a field called `timestamp`.
4. Recall from [Step 2](#2-examine-the-database-using-pgadmin): the database table `interaction_logs` has a column called `created_at`, not `timestamp`.
5. The `InteractionLog` class (the database model) has `created_at`, but the `InteractionModel` class (the response schema) has `timestamp`.
6. This mismatch causes the error.

### 8. Fix Bug 1: rename `timestamp` to `created_at`

1. In [`src/app/models/interaction.py`](../../../src/app/models/interaction.py), change the `InteractionModel` class:

   **Before:**

   ```python
   timestamp: datetime
   ```

   **After:**

   ```python
   created_at: datetime
   ```

2. Save the file.

<details><summary>Hint: what to look for</summary>

The field name in the response schema (`InteractionModel`) must match the field name in the database model (`InteractionLog`). The database column is `created_at`, so the response schema must also use `created_at`.

</details>

### 9. Verify `GET /interactions` works

1. Restart the services ([Step 4](#4-restart-the-services)).
2. Open `Swagger UI` and [authorize](./task-1.md#6-authorize-in-swagger-ui).
3. Try `GET /interactions`.
4. Observe: you should see a `200` status code with interaction data.

### 10. Commit Bug 1 fix

1. [Commit](../git-workflow.md#commit) your changes.

   Use the following commit message:

   ```text
   fix: rename timestamp to created_at in InteractionModel
   ```

### 11. Try `GET /interactions?item_id=2`

1. In `Swagger UI`, expand the `GET /interactions` endpoint.
2. Click `Try it out`.
3. Enter `2` in the `item_id` field.
4. Click `Execute`.
5. Note the results that are returned.

### 12. Compare with the database

1. [Open `PgAdmin`](../../appendix/pgadmin.md#open-pgadmin).
2. [Run a query](../../appendix/pgadmin.md#run-a-query) on the `interaction_logs` table:

   ```sql
   SELECT * FROM interaction_logs WHERE item_id = 2;
   ```

3. Compare the query results with the response from `Swagger UI`.
4. Notice that the results don't match — the API returns different interactions than what the database query shows.

### 13. Find Bug 2 in the code

1. [Open the file](../../appendix/vs-code.md#open-the-file):
   [`src/app/routers/interactions.py`](../../../src/app/routers/interactions.py).
2. Look at the filtering code:

   ```python
   interactions = [i for i in interactions if i.learner_id == item_id]
   ```

3. The code filters by `i.learner_id` instead of `i.item_id`.
4. This means the endpoint returns interactions for a specific **learner**, not for a specific **item**.

<details><summary>Hint: what to look for</summary>

The query parameter is called `item_id`, so the filter should compare `i.item_id == item_id`, not `i.learner_id == item_id`.

</details>

### 14. Fix Bug 2: filter by `item_id`

1. In [`src/app/routers/interactions.py`](../../../src/app/routers/interactions.py), change the filtering line:

   **Before:**

   ```python
   interactions = [i for i in interactions if i.learner_id == item_id]
   ```

   **After:**

   ```python
   interactions = [i for i in interactions if i.item_id == item_id]
   ```

2. Save the file.
3. Restart the services ([Step 4](#4-restart-the-services)).
4. Verify in `Swagger UI` that `GET /interactions?item_id=2` now returns the correct results matching the database query.

### 15. Commit Bug 2 fix

1. [Commit](../git-workflow.md#commit) your changes.

   Use the following commit message:

   ```text
   fix: filter interactions by item_id instead of learner_id
   ```

> [!IMPORTANT]
> Each fix must be a **separate commit**. Do not combine them into one.

### 16. Finish the task

1. [Create a PR](../git-workflow.md#create-a-pr-to-main-in-your-fork) with your fixes.
2. [Get a PR review](../git-workflow.md#get-a-pr-review) and complete the subsequent steps in the `Git workflow`.

---

## Acceptance criteria

- [ ] Issue has the correct title.
- [ ] `GET /interactions` returns interaction data.
- [ ] `GET /interactions?item_id=2` returns only interactions for item 2.
- [ ] Each fix is a separate commit.
- [ ] PR is approved.
- [ ] PR is merged.
