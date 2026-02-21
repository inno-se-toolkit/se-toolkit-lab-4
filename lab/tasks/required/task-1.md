# Explore the API

<h4>Time</h4>

~30 min

<h4>Purpose</h4>

Learn to explore an API using `Swagger UI` and authenticate with an API key.

<h4>Context</h4>

The service is running. Only `items` endpoints are active — `/interactions` and `/learners` aren't enabled yet.
You will explore the API using `Swagger UI`, discover the API key mechanism, and observe how the service responds to different requests.

<h4>Table of contents</h4>

- [1. Steps](#1-steps)
  - [1.1. Follow the `Git workflow`](#11-follow-the-git-workflow)
  - [1.2. Create a `Lab Task` issue](#12-create-a-lab-task-issue)
  - [1.3. Set up](#13-set-up)
    - [1.3.1. Start the services](#131-start-the-services)
    - [1.3.2. Open `Swagger UI`](#132-open-swagger-ui)
  - [1.4. Discover authentication](#14-discover-authentication)
    - [1.4.1. Try `GET /items` without authentication](#141-try-get-items-without-authentication)
    - [1.4.2. Find the `API_TOKEN` value](#142-find-the-api_token-value)
    - [1.4.3. Authorize in `Swagger UI`](#143-authorize-in-swagger-ui)
    - [1.4.4. Try `GET /items` with authorization](#144-try-get-items-with-authorization)
  - [1.5. Try the endpoints](#15-try-the-endpoints)
    - [1.5.1. Try `GET /items/{item_id}`](#151-try-get-itemsitem_id)
    - [1.5.2. Try `POST /items`](#152-try-post-items)
    - [1.5.3. Try `PUT /items/{item_id}`](#153-try-put-itemsitem_id)
  - [1.6. Experiment with the token](#16-experiment-with-the-token)
  - [1.7. Fill in the questionnaire](#17-fill-in-the-questionnaire)
  - [1.8. Commit the questionnaire](#18-commit-the-questionnaire)
  - [1.9. Finish the task](#19-finish-the-task)
- [2. Acceptance criteria](#2-acceptance-criteria)

## 1. Steps

### 1.1. Follow the `Git workflow`

Follow the [`Git workflow`](../git-workflow.md) to complete this task.

### 1.2. Create a `Lab Task` issue

Title: `[Task] Explore the API`

### 1.3. Set up

#### 1.3.1. Start the services

1. [Stop the services](../setup.md#115-new-stop-the-services).
2. [Open a new `VS Code Terminal`](../../appendix/vs-code.md#open-a-new-vs-code-terminal).
3. Start the `postgres` service:

   [Run using the `VS Code Terminal`](../../appendix/vs-code.md#run-a-command-using-the-vs-code-terminal):

   ```terminal
   docker compose --env-file .env.docker.secret up postgres --build
   ```

4. [Open a new `VS Code Terminal`](../../appendix/vs-code.md#open-a-new-vs-code-terminal).
5. Start the `app` service:

   [Run using the `VS Code Terminal`](../../appendix/vs-code.md#run-a-command-using-the-vs-code-terminal):

   ```terminal
   docker compose --env-file .env.docker.secret up app --build
   ```

6. [Open a new `VS Code Terminal`](../../appendix/vs-code.md#open-a-new-vs-code-terminal).

#### 1.3.2. Open `Swagger UI`

1. Open in a browser: <http://127.0.0.1:42001/docs>.
2. You should see the auto-generated API documentation with the available [endpoints](../../appendix/web-development.md#endpoint).

   <img alt="Swagger UI" src="../../images/tasks/required/task-1/swagger-ui.png" style="width:400px">

### 1.4. Discover authentication

#### 1.4.1. Try `GET /items` without authentication

1. In the `Swagger UI`, expand (click) the `GET /items` endpoint.

   <img alt="Swagger UI" src="../../images/tasks/required/task-1/swagger-ui-items.png" style="width:400px">

   **Note:** The `Responses` section contains the description of possible responses of the endpoint.
2. Click `Try it out`.
3. Click `Execute`.
4. Observe the `Server response`:

   - The [`401`](../../appendix/http.md#401-unauthorized) status code.
   - The `Details` should be `Error: Unauthorized`.

> [!NOTE]
> The `401` response means the server rejected your request because you haven't [authenticated](../../appendix/swagger.md#authorize-in-swagger-ui) using an API key.
>
> The service uses the `Authorization: Bearer <token>` [header](../../appendix/http.md) for authentication.

#### 1.4.2. Find the `API_TOKEN` value

1. [Open the file](../../appendix/vs-code.md#open-the-file):
   `.env.docker.secret`.
2. Find the `API_TOKEN` variable.

   We'll refer to its value as [`<api-token>`](../../appendix/web-development.md#api-token).

   The default value is `my-secret-api-key`.

#### 1.4.3. Authorize in `Swagger UI`

1. In `Swagger UI`, click the `Authorize` button (the lock icon at the top).
2. In the `Value` field, enter the [`<api-token>`](../../appendix/web-development.md#api-token) that you [found](#142-find-the-api_token-value).
3. Click `Authorize`.
4. Click `Close`.

#### 1.4.4. Try `GET /items` with authorization

1. In `Swagger UI`, expand the `GET /items` endpoint.
2. Click `Try it out`.
3. Click `Execute`.
4. Observe the `Server response`:
   - The [`200`](../../appendix/http.md#200-ok) status code;
   - The `Response body` with a list of items.

### 1.5. Try the endpoints

#### 1.5.1. Try `GET /items/{item_id}`

1. In `Swagger UI`, expand the `GET /items/{item_id}` endpoint.
2. Click `Try it out`.
3. Enter `1` as the `item_id`.
4. Click `Execute`.
5. Observe the `Server response`:
   - The [`200`](../../appendix/http.md#200-ok) status code;
   - The `Response body` with the item data.

   <img alt="Get item by id - 200" src="../../images/tasks/required/task-1/get-item-by-id-200.png" style="width:400px">
6. Try entering `999` as the `item_id`.
7. Click `Execute`.
8. Observe the `Server response`:
   - you should see the [`404` (Not Found)](../../appendix/http.md#404-not-found) error.

#### 1.5.2. Try `POST /items`

1. In `Swagger UI`, expand the `POST /items` endpoint.
2. Click `Try it out` to make a request with the default body.
3. Observe the `Server response`:
   - The [`422` (Unprocessable Content)](../../appendix/http.md#422-unprocessable-entity) error.
4. Enter another request body as [`JSON`](../../appendix/file-formats.md#json), for example:

   ```json
   {
     "type": "step",
     "parent_id": 5,
     "title": "Try POST /items using Swagger",
     "description": "Open Swagger in browser and execute POST /items"
   }
   ```

   **Note:** `"parent_id": 5` means that the parent item of this step is the task with the `"id"` equal to `5` (created in the [`init.sql`](../../../src/app/data/init.sql)).

5. Click `Execute`.
6. Observe the `Server response`:
   - The [`201` (Created)](../../appendix/http.md#201-created) response status code;
   - The `Response body` with the newly created item data in `JSON` format.

#### 1.5.3. Try `PUT /items/{item_id}`

1. In `Swagger UI`, expand the `PUT /items/{item_id}` endpoint.
2. Click `Try it out`.
3. Enter the `item_id` of the item you just created.
4. Enter a request body with updated values in `JSON` format, for example:

   ```json
   {
     "title": "Execute `POST /items` using Swagger",
     "description": "1. Open Swagger in a browser.\n2. Execute POST /items."
   }
   ```

5. Click `Execute`.
6. Observe the `Server response`:
   - The [`200`](../../appendix/http.md#200-ok) status code.
   - The `Response body` with the updated item data.

### 1.6. Experiment with the token

1. [Open the file](../../appendix/vs-code.md#open-the-file):
   `.env.docker.secret`.
2. Change the `API_TOKEN` value to something different, for example: `my-new-secret-key`.
3. Stop the `app` service:

   [Run using the `VS Code Terminal`](../../appendix/vs-code.md#run-a-command-using-the-vs-code-terminal):

   ```terminal
   docker compose --env-file .env.docker.secret down app
   ```

4. Start the `app` service:

   [Run using the `VS Code Terminal`](../../appendix/vs-code.md#run-a-command-using-the-vs-code-terminal):

   ```terminal
   docker compose --env-file .env.docker.secret up app --build
   ```

5. Go back to `Swagger UI`.
6. Try `GET /items`.
7. Observe: the old key no longer works (you get a `401` Unauthorized error).

   **Note:** This is `401`, not `403`. In step [1.4.1](#141-try-get-items-without-authentication) you sent no `Authorization` header at all, so the server returned `401`. Here, `Swagger UI` is still sending the old key as `Authorization: Bearer <old-key>` — the header is present, but the token is wrong, so the server returns `401` instead.

8. Click `Authorize` again.
9. Enter the new key (`my-new-secret-key`).
10. Try `GET /items`.
11. Observe: the new key works (you get a `200` response).

### 1.7. Fill in the questionnaire

1. [Open the file](../../appendix/vs-code.md#open-the-file):
   [`lab/tasks/required/questionnaire.md`](./questionnaire.md).
2. Fill in each answer based on what you observed.

### 1.8. Commit the questionnaire

1. [Commit](../git-workflow.md#commit) your changes.

   Use the following commit message:

   ```text
   docs: fill in the API exploration questionnaire
   ```

### 1.9. Finish the task

1. [Create a PR](../git-workflow.md#create-a-pr-to-main-in-your-fork) with your questionnaire.
2. [Get a PR review](../git-workflow.md#get-a-pr-review) and complete the subsequent steps in the `Git workflow`.

---

## 2. Acceptance criteria

- [ ] Issue has the correct title.
- [ ] The questionnaire file is filled in with correct answers.
- [ ] PR is approved.
- [ ] PR is merged.
