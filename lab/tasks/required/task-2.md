# Enable and debug a broken endpoint

<h4>Time</h4>

~40-50 min

<h4>Purpose</h4>

Learn to debug a broken endpoint by tracing code and examining the database using `pgAdmin`.

<h4>Context</h4>

The `/interactions` endpoint code exists but is disabled by a feature flag. It contains two bugs: a schema-database mismatch and a logic error.

Your job is to enable the endpoint, discover the bugs, and fix them.

<h4>Table of contents</h4>

- [1. Steps](#1-steps)
  - [1.1. Follow the `Git workflow`](#11-follow-the-git-workflow)
  - [1.2. Create a `Lab Task` issue](#12-create-a-lab-task-issue)
  - [1.3. Restart the services](#13-restart-the-services)
  - [1.4. Examine the database using `pgAdmin`](#14-examine-the-database-using-pgadmin)
  - [1.5. Enable the `/interactions` endpoint](#15-enable-the-interactions-endpoint)
  - [1.6. Restart the services](#16-restart-the-services)
  - [1.7. Try `GET /interactions`](#17-try-get-interactions)
  - [1.8. Read the error](#18-read-the-error)
  - [1.9. Trace the bug](#19-trace-the-bug)
  - [1.10. Fix Bug 1: rename `timestamp` to `created_at`](#110-fix-bug-1-rename-timestamp-to-created_at)
  - [1.11. Verify `GET /interactions` works](#111-verify-get-interactions-works)
  - [1.12. Commit Bug 1 fix](#112-commit-bug-1-fix)
  - [1.13. Try `GET /interactions?item_id=2`](#113-try-get-interactionsitem_id2)
  - [1.14. Compare with the database](#114-compare-with-the-database)
  - [1.15. Find Bug 2 in the code](#115-find-bug-2-in-the-code)
  - [1.16. Fix Bug 2: filter by `item_id`](#116-fix-bug-2-filter-by-item_id)
  - [1.17. Commit Bug 2 fix](#117-commit-bug-2-fix)
  - [1.18. Finish the task](#118-finish-the-task)
- [2. Acceptance criteria](#2-acceptance-criteria)

## 1. Steps

### 1.1. Follow the `Git workflow`

Follow the [`Git workflow`](../git-workflow.md) to complete this task.

### 1.2. Create a `Lab Task` issue

Title: `[Task] Enable and debug the interactions endpoint`

### 1.3. Restart the services

1. [Stop the running services](../setup.md#115-new-stop-the-services).
2. [Run using the `VS Code Terminal`](../../appendix/vs-code.md#run-a-command-using-the-vs-code-terminal):

   ```terminal
   docker compose --env-file .env.docker.secret up --build
   ```

3. Wait until the services are ready (2-3 minutes). You should see log output from the application and database containers.
4. [Open a new `VS Code Terminal`](../../appendix/vs-code.md#open-a-new-vs-code-terminal) to run commands while the services are running.

### 1.4. Examine the database using `pgAdmin`

1. Make sure you have [set up `pgAdmin`](../setup.md#1142-new-set-up-pgadmin).
2. [Inspect columns](../../appendix/pgadmin.md#inspect-columns) of the `interaction_logs` table.
3. Note the column names: `id`, `learner_id`, `item_id`, `kind`, `created_at`.

> [!NOTE]
> Pay attention to the column name `created_at`. You will need it later.

### 1.5. Enable the `/interactions` endpoint

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

### 1.6. Restart the services

1. Stop the `app` service:

   [Run using the `VS Code Terminal`](../../appendix/vs-code.md#run-a-command-using-the-vs-code-terminal):

   ```terminal
   docker compose --env-file .env.docker.secret down app
   ```

2. Start the `app` service:

   [Run using the `VS Code Terminal`](../../appendix/vs-code.md#run-a-command-using-the-vs-code-terminal):

   ```terminal
   docker compose --env-file .env.docker.secret up app --build
   ```

### 1.7. Try `GET /interactions`

1. Open in a browser: <http://127.0.0.1:42001/docs>.
2. [Authorize](./task-1.md#143-authorize-in-swagger-ui) with the API key.
3. Expand the `GET /interactions` endpoint.
4. Click `Try it out`.
5. Click `Execute`.
6. Observe the response: you should see a `500` Internal Server Error.

### 1.8. Read the error

1. Look at the error response in `Swagger UI`.
2. Look at the application logs in the terminal where `Docker Compose` is running.
3. The error mentions a missing or mismatched field: `timestamp`.

### 1.9. Trace the bug

1. [Open the file](../../appendix/vs-code.md#open-the-file):
   [`src/app/routers/interactions.py`](../../../src/app/routers/interactions.py).
2. Look at the endpoint definition:

   ```python
   @router.get("/", response_model=list[InteractionModel])
   async def get_interactions(...)
   ```

   **Note:** The path `"/"` is local to this router file.

   `FastAPI` combines it with the `prefix="/interactions"` set in [`src/app/main.py`](../../../src/app/main.py) to produce the full path `/interactions`.

   The `response_model` parameter tells `FastAPI` which schema to use when serializing the response. It is `InteractionModel`.
3. [Open the file](../../appendix/vs-code.md#open-the-file):
   [`src/app/models/interaction.py`](../../../src/app/models/interaction.py).
4. Look at the `InteractionModel` class (the response schema).
5. The response schema has a field called `timestamp`.
6. [Recall](#14-examine-the-database-using-pgadmin) that
   the database table `interaction_logs` has a column called `created_at`, not `timestamp`.
7. The `InteractionLog` class (the database model) has `created_at`, but the `InteractionModel` class (the response schema) has `timestamp`.
8. This mismatch causes the error.

### 1.10. Fix Bug 1: rename `timestamp` to `created_at`

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

### 1.11. Verify `GET /interactions` works

1. [Restart the services](#16-restart-the-services).
2. Open `Swagger UI` and [authorize](./task-1.md#143-authorize-in-swagger-ui).
3. Try `GET /interactions`.
4. Observe: you should see a `200` status code with interaction data.

### 1.12. Commit Bug 1 fix

1. [Commit](../git-workflow.md#commit) your changes.

   Use the following commit message:

   ```text
   fix: rename timestamp to created_at in InteractionModel
   ```

### 1.13. Try `GET /interactions?item_id=2`

1. In `Swagger UI`, expand the `GET /interactions` endpoint.
2. Click `Try it out`.
3. Enter `2` in the `item_id` field.
4. Click `Execute`.
5. Note the results that are returned.

### 1.14. Compare with the database

1. [Open `pgAdmin`](../../appendix/pgadmin.md#open-pgadmin).
2. [Run a query](../../appendix/pgadmin.md#run-a-query) on the `interaction_logs` table:

   ```sql
   SELECT * FROM interaction_logs WHERE item_id = 2;
   ```

3. Compare the query results with the response from `Swagger UI`.
4. Notice that the results don't match — the API returns different interactions than what the database query shows.

### 1.15. Find Bug 2 in the code

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

### 1.16. Fix Bug 2: filter by `item_id`

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
3. [Restart the services](#16-restart-the-services).
4. Verify in `Swagger UI` that `GET /interactions?item_id=2` now returns the correct results matching the database query.

### 1.17. Commit Bug 2 fix

1. [Commit](../git-workflow.md#commit) your changes.

   Use the following commit message:

   ```text
   fix: filter interactions by item_id instead of learner_id
   ```

> [!IMPORTANT]
> Each fix must be a **separate commit**. Do not combine them into one.

### 1.18. Finish the task

1. [Create a PR](../git-workflow.md#create-a-pr-to-main-in-your-fork) with your fixes.
2. [Get a PR review](../git-workflow.md#get-a-pr-review) and complete the subsequent steps in the `Git workflow`.

---

## 2. Acceptance criteria

- [ ] Issue has the correct title.
- [ ] `GET /interactions` returns interaction data.
- [ ] `GET /interactions?item_id=2` returns only interactions for item 2.
- [ ] Each fix is a separate commit.
- [ ] PR is approved.
- [ ] PR is merged.
