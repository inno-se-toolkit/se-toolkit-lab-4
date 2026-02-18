# Explore the API

<h4>Time</h4>

~30 min

<h4>Purpose</h4>

Learn to explore an API using `Swagger UI` and authenticate with an API key.

<h4>Context</h4>

The service is running. Only `items` endpoints are active — `/interactions` and `/learners` don't exist yet.
You will explore the API using `Swagger UI`, discover the API key mechanism, and observe how the service responds to different requests.

<h4>Table of contents</h4>

- [Steps](#steps)
  - [0. Follow the `Git workflow`](#0-follow-the-git-workflow)
  - [1. Create a `Lab Task` issue](#1-create-a-lab-task-issue)
  - [2. Start the services](#2-start-the-services)
  - [3. Open `Swagger UI`](#3-open-swagger-ui)
  - [4. Try `GET /items` without authentication](#4-try-get-items-without-authentication)
  - [5. Find the `API_TOKEN` value](#5-find-the-api_token-value)
  - [6. Authorize in `Swagger UI`](#6-authorize-in-swagger-ui)
  - [7. Try `GET /items` with authentication](#7-try-get-items-with-authentication)
  - [8. Try `GET /items/{item_id}`](#8-try-get-itemsitem_id)
  - [9. Try `POST /items`](#9-try-post-items)
  - [10. Try `PUT /items/{item_id}`](#10-try-put-itemsitem_id)
  - [11. Change the `API_TOKEN`](#11-change-the-api_token)
  - [12. Fill in the questionnaire](#12-fill-in-the-questionnaire)
  - [13. Commit the questionnaire](#13-commit-the-questionnaire)
  - [14. Finish the task](#14-finish-the-task)
- [Acceptance criteria](#acceptance-criteria)

## Steps

### 0. Follow the `Git workflow`

Follow the [`Git workflow`](../git-workflow.md) to complete this task.

### 1. Create a `Lab Task` issue

Title: `[Task] Explore the API`

### 2. Start the services

> [!NOTE]
> If you already started the services during the setup, they should still be running.
> You can skip this step.

1. [Run using the `VS Code Terminal`](../../appendix/vs-code.md#run-a-command-using-the-vs-code-terminal):

   ```terminal
   docker compose --env-file .env.docker.secret up --build
   ```

### 3. Open `Swagger UI`

1. Open in a browser: `http://127.0.0.1:42001/docs`.
2. You should see the auto-generated API documentation with the available endpoints.

### 4. Try `GET /items` without authentication

1. In `Swagger UI`, expand the `GET /items` endpoint.
2. Click `Try it out`.
3. Click `Execute`.
4. Observe the response: you should see a `403` Forbidden error.

> [!NOTE]
> The `403` response means the server rejected your request because you did not provide an API key.
> The service uses the `Authorization: Bearer <token>` header for authentication.

### 5. Find the `API_TOKEN` value

1. [Open the file](../../appendix/vs-code.md#open-the-file):
   `.env.docker.secret`.
2. Find the `API_TOKEN` variable.
3. The default value is `my-secret-api-key`.

### 6. Authorize in `Swagger UI`

1. In `Swagger UI`, click the `Authorize` button (the lock icon at the top).
2. In the `Value` field, enter: `my-secret-api-key`.
3. Click `Authorize`.
4. Click `Close`.

### 7. Try `GET /items` with authentication

1. In `Swagger UI`, expand the `GET /items` endpoint.
2. Click `Try it out`.
3. Click `Execute`.
4. Observe the response: you should see a `200` status code with a list of items.

### 8. Try `GET /items/{item_id}`

1. In `Swagger UI`, expand the `GET /items/{item_id}` endpoint.
2. Click `Try it out`.
3. Enter `1` as the `item_id`.
4. Click `Execute`.
5. Observe the response: you should see a `200` status code with the item data.
6. Try entering `999` as the `item_id`.
7. Click `Execute`.
8. Observe the response: you should see a `404` Not Found error.

### 9. Try `POST /items`

1. In `Swagger UI`, expand the `POST /items` endpoint.
2. Click `Try it out`.
3. Enter a request body, for example:

   ```json
   {
     "title": "My New Item",
     "description": "A test item."
   }
   ```

4. Click `Execute`.
5. Observe the response: you should see a `201` Created status code with the newly created item.

### 10. Try `PUT /items/{item_id}`

1. In `Swagger UI`, expand the `PUT /items/{item_id}` endpoint.
2. Click `Try it out`.
3. Enter the `item_id` of the item you just created.
4. Enter a request body with updated values, for example:

   ```json
   {
     "title": "Updated Item",
     "description": "An updated description."
   }
   ```

5. Click `Execute`.
6. Observe the response: you should see a `200` status code with the updated item data.

### 11. Change the `API_TOKEN`

1. [Open the file](../../appendix/vs-code.md#open-the-file):
   `.env.docker.secret`.
2. Change the `API_TOKEN` value to something different, for example: `my-new-secret-key`.
3. Restart the services:

   [Run using the `VS Code Terminal`](../../appendix/vs-code.md#run-a-command-using-the-vs-code-terminal):

   ```terminal
   docker compose --env-file .env.docker.secret up --build
   ```

   > **Tip:** If the services are still running, press `Ctrl+C` first to stop them, then run the command above.

4. Go back to `Swagger UI`.
5. Try `GET /items`.
6. Observe: the old key no longer works (you get a `401` Unauthorized error).

   > **Note:** This is `401`, not `403`. In step 4 you sent no `Authorization` header at all, so the server returned `403`.
   > Here, `Swagger UI` is still sending the old key as `Authorization: Bearer <old-key>` — the header is present, but the token is wrong, so the server returns `401` instead.

7. Click `Authorize` again.
8. Enter the new key (`my-new-secret-key`).
9. Try `GET /items`.
10. Observe: the new key works (you get a `200` response).

> [!IMPORTANT]
> After you are done, change the `API_TOKEN` back to `my-secret-api-key` so that subsequent tasks work with the default value.

### 12. Fill in the questionnaire

1. [Open the file](../../appendix/vs-code.md#open-the-file):
   [`lab/tasks/required/questionnaire.md`](./questionnaire.md).
2. Fill in each answer based on what you observed.

### 13. Commit the questionnaire

1. [Commit](../git-workflow.md#commit) your changes.

   Use the following commit message:

   ```text
   docs: fill in the API exploration questionnaire
   ```

### 14. Finish the task

1. [Create a PR](../git-workflow.md#create-a-pr-to-main-in-your-fork) with your questionnaire.
2. [Get a PR review](../git-workflow.md#get-a-pr-review) and complete the subsequent steps in the `Git workflow`.

---

## Acceptance criteria

- [ ] Issue has the correct title.
- [ ] The questionnaire file is filled in with correct answers.
- [ ] PR is approved.
- [ ] PR is merged.
