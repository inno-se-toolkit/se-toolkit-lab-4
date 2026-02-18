# Implement the learners endpoint

<h4>Time</h4>

~40-50 min

<h4>Purpose</h4>

Learn to implement a new endpoint using an existing one as a reference.

<h4>Context</h4>

The `/learners` endpoint doesn't exist yet. Placeholder templates are provided in the code.
The database functions for learners (`read_learners`, `create_learner`) are already implemented.
You will implement the endpoint layer by studying the `items` reference implementation and filling in the placeholders.

<h4>Table of contents</h4>

- [Steps](#steps)
  - [0. Follow the `Git workflow`](#0-follow-the-git-workflow)
  - [1. Create a `Lab Task` issue](#1-create-a-lab-task-issue)
  - [2. Study the reference implementation](#2-study-the-reference-implementation)
  - [3. Part A: Implement the `GET` endpoint](#3-part-a-implement-the-get-endpoint)
    - [3.1. Enable the learners endpoint](#31-enable-the-learners-endpoint)
    - [3.2. Uncomment the imports](#32-uncomment-the-imports)
    - [3.3. Uncomment and fill in the `GET` placeholder](#33-uncomment-and-fill-in-the-get-placeholder)
    - [3.4. Restart and verify](#34-restart-and-verify)
    - [3.5. Verify the query parameter](#35-verify-the-query-parameter)
    - [3.6. Commit Part A](#36-commit-part-a)
  - [4. Part B: Implement the `POST` endpoint](#4-part-b-implement-the-post-endpoint)
    - [4.1. Uncomment and fill in the `POST` placeholder](#41-uncomment-and-fill-in-the-post-placeholder)
    - [4.2. Restart and verify](#42-restart-and-verify)
    - [4.3. Commit Part B](#43-commit-part-b)
  - [5. Finish the task](#5-finish-the-task)
- [Acceptance criteria](#acceptance-criteria)

## Steps

### 0. Follow the `Git workflow`

Follow the [`Git workflow`](../git-workflow.md) to complete this task.

### 1. Create a `Lab Task` issue

Title: `[Task] Implement the learners endpoint`

### 2. Study the reference implementation

Before writing any code, study the existing `items` implementation to understand the pattern.

1. [Open the file](../../appendix/vs-code.md#open-the-file):
   [`src/app/routers/items.py`](../../../src/app/routers/items.py).
2. Study the `GET /` endpoint:
   - What decorator is used? (`@router.get`)
   - What is the `response_model`?
   - What parameters does the function accept?
   - What database function does it call?
3. Study the `POST /` endpoint:
   - What decorator is used? (`@router.post`)
   - What is the `status_code`?
   - What is the request body schema?
   - What database function does it call?
4. [Open the file](../../appendix/vs-code.md#open-the-file):
   [`src/app/db/items.py`](../../../src/app/db/items.py).
5. Study the `read_items` and `create_item` functions.
6. [Open the file](../../appendix/vs-code.md#open-the-file):
   [`src/app/db/learners.py`](../../../src/app/db/learners.py).
7. Study the `read_learners` and `create_learner` functions.
8. Notice that `read_learners` accepts an optional `enrolled_after` parameter for filtering.

### 3. Part A: Implement the `GET` endpoint

#### 3.1. Enable the learners endpoint

1. [Open the file](../../appendix/vs-code.md#open-the-file):
   `.env.docker.secret`.
2. Change:

   ```text
   ENABLE_LEARNERS=false
   ```

   to:

   ```text
   ENABLE_LEARNERS=true
   ```

3. Save the file.

> **Note:** `.env.docker.secret` is listed in `.gitignore` and will not be committed.
> The flag tells the application to register the `/learners` route at startup.

#### 3.2. Uncomment the imports

1. [Open the file](../../appendix/vs-code.md#open-the-file):
   [`src/app/routers/learners.py`](../../../src/app/routers/learners.py).
2. Uncomment the import lines at the top of the file:

   ```python
   from datetime import datetime

   from fastapi import Depends
   from sqlmodel.ext.asyncio.session import AsyncSession

   from app.database import get_session
   from app.db.learners import read_learners, create_learner
   from app.models.learner import Learner, LearnerCreate
   ```

#### 3.3. Uncomment and fill in the `GET` placeholder

1. In [`src/app/routers/learners.py`](../../../src/app/routers/learners.py), find the `PART A: GET endpoint` section.
2. Uncomment the placeholder code.
3. Replace each `<placeholder>` with the correct value.

> [!TIP]
> Use the `items` `GET` endpoint as a reference. The learners `GET` endpoint follows the same pattern but:
>
> - Uses `Learner` instead of `Item`.
> - Uses `read_learners` instead of `read_items`.
> - Has an `enrolled_after` query parameter of type `datetime | None` instead of no query parameter.

<details><summary>Hint: what the completed code looks like</summary>

```python
@router.get("/", response_model=list[Learner])
async def get_learners(
    enrolled_after: datetime | None = None,
    session: AsyncSession = Depends(get_session),
):
    """Get all learners, optionally filtered by enrollment date."""
    return await read_learners(session, enrolled_after)
```

</details>

#### 3.4. Restart and verify

1. Restart the services:

   [Run using the `VS Code Terminal`](../../appendix/vs-code.md#run-a-command-using-the-vs-code-terminal):

   ```terminal
   docker compose --env-file .env.docker.secret up --build
   ```

2. Open `Swagger UI` at `http://127.0.0.1:42001/docs`.
3. [Authorize](./task-1.md#6-authorize-in-swagger-ui) with the API key.
4. Try `GET /learners`.
5. Observe: you should see a `200` status code with a list of all learners.

#### 3.5. Verify the query parameter

1. In `Swagger UI`, expand the `GET /learners` endpoint.
2. Click `Try it out`.
3. Enter `2025-10-01` in the `enrolled_after` field.
4. Click `Execute`.
5. Observe: the response should contain only Diana and Eve (learners enrolled on or after `2025-10-01`).

#### 3.6. Commit Part A

1. [Commit your change using the `Source Control`](../git-workflow.md#commit).

   Use the following commit message:

   ```text
   feat: implement GET /learners endpoint
   ```

### 4. Part B: Implement the `POST` endpoint

#### 4.1. Uncomment and fill in the `POST` placeholder

1. In [`src/app/routers/learners.py`](../../../src/app/routers/learners.py), find the `PART B: POST endpoint` section.
2. Uncomment the placeholder code.
3. Replace each `<placeholder>` with the correct value.

> [!TIP]
> Use the `items` `POST` endpoint as a reference. The learners `POST` endpoint follows the same pattern but:
>
> - Uses `Learner` and `LearnerCreate` instead of `Item` and `ItemCreate`.
> - Uses `create_learner` instead of `create_item`.
> - Passes `name` and `email` instead of `title` and `description`.

<details><summary>Hint: what the completed code looks like</summary>

```python
@router.post("/", response_model=Learner, status_code=201)
async def post_learner(
    body: LearnerCreate,
    session: AsyncSession = Depends(get_session),
):
    """Create a new learner."""
    return await create_learner(session, name=body.name, email=body.email)
```

</details>

#### 4.2. Restart and verify

1. Restart the services ([Step 3.4](#34-restart-and-verify)).
2. Open `Swagger UI` and [authorize](./task-1.md#6-authorize-in-swagger-ui).
3. Try `POST /learners` with a request body:

   ```json
   {
     "name": "Frank Castle",
     "email": "frank@example.com"
   }
   ```

4. Observe: you should see a `201` Created status code with the newly created learner.

#### 4.3. Commit Part B

1. [Commit your change using the `Source Control`](../git-workflow.md#commit).

   Use the following commit message:

   ```text
   feat: implement POST /learners endpoint
   ```

> [!IMPORTANT]
> Part A and Part B must be **separate commits**. Do not combine them into one.

### 5. Finish the task

1. [Create a PR](../git-workflow.md#create-a-pr-to-main-in-your-fork) with your implementation.
2. [Get a PR review](../git-workflow.md#get-a-pr-review) and complete the subsequent steps in the `Git workflow`.

---

## Acceptance criteria

- [ ] Issue has the correct title.
- [ ] `GET /learners` returns learner data.
- [ ] `GET /learners?enrolled_after=2025-10-01` returns only learners enrolled after that date.
- [ ] `POST /learners` creates a new learner and returns `201`.
- [ ] Part A and Part B are separate commits.
- [ ] PR is approved.
- [ ] PR is merged.
