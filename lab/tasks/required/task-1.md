# Observe the interaction of system components

<h4>Time</h4>

~25 min

<h4>Purpose</h4>

Trace a request from [`Swagger UI`](../../../wiki/swagger.md#what-is-swagger-ui) through the [`API`](../../../wiki/web-development.md#api) to the [database](../../../wiki/database.md#what-is-a-database) using the browser developer tools and [`pgAdmin`](../../../wiki/pgadmin.md#what-is-pgadmin).

<h4>Context</h4>

Before adding new features, you will deploy the system to your VM and confirm it works.
Then you will send requests and observe how data flows through the components: browser → `API` → database.

<!-- TODO add sequence diagram -->

<h4>Table of contents</h4>

- [1. Steps](#1-steps)
  - [1.1. Create a `Lab Task` issue](#11-create-a-lab-task-issue)
  - [1.2. Deploy the back-end to the VM](#12-deploy-the-back-end-to-the-vm)
    - [1.2.1. Connect and get the code](#121-connect-and-get-the-code)
    - [1.2.2. Prepare the environment](#122-prepare-the-environment)
    - [1.2.3. Start the services](#123-start-the-services)
  - [1.3. Open `Swagger UI`](#13-open-swagger-ui)
  - [1.4. Open the browser developer tools](#14-open-the-browser-developer-tools)
  - [1.5. Send a request using `Swagger UI`](#15-send-a-request-using-swagger-ui)
  - [1.6. Inspect the request using browser developer tools](#16-inspect-the-request-using-browser-developer-tools)
  - [1.7. Verify in `pgAdmin`](#17-verify-in-pgadmin)
  - [1.8. Send another request and check the database](#18-send-another-request-and-check-the-database)
  - [1.9. Write comments for the issue](#19-write-comments-for-the-issue)
    - [1.9.1. Comment 1: write the request as `fetch` code](#191-comment-1-write-the-request-as-fetch-code)
    - [1.9.2. Comment 2: write the response](#192-comment-2-write-the-response)
    - [1.9.3. Comment 3: write the data output from `pgAdmin`](#193-comment-3-write-the-data-output-from-pgadmin)
    - [1.9.4. Comment 4: paste the ERD from `pgAdmin`](#194-comment-4-paste-the-erd-from-pgadmin)
  - [1.10. Close the issue](#110-close-the-issue)
- [2. Acceptance criteria](#2-acceptance-criteria)

## 1. Steps

### 1.1. Create a `Lab Task` issue

Title: `[Task] Observe System Component Interaction`

### 1.2. Deploy the back-end to the VM

#### 1.2.1. Connect and get the code

1. [Connect to your VM](../../../wiki/vm.md#connect-to-the-vm).
2. To clone your fork on the VM (skip this step if already cloned),

   [run in the `VS Code Terminal`](../../../wiki/vs-code.md#run-a-command-in-the-vs-code-terminal):

   ```terminal
   git clone <your-fork-url> se-toolkit-lab-4
   ```

   Replace [`<your-fork-url>`](../../../wiki/github.md#your-fork-url).

3. To navigate to the project directory,

   [run in the `VS Code Terminal`](../../../wiki/vs-code.md#run-a-command-in-the-vs-code-terminal):

   ```terminal
   cd se-toolkit-lab-4
   ```

4. To pull the changes from your fork,

   [run in the `VS Code Terminal`](../../../wiki/vs-code.md#run-a-command-in-the-vs-code-terminal):

   ```terminal
   git pull
   ```

#### 1.2.2. Prepare the environment

1. To create the [`.env.docker.secret`](../../../wiki/dotenv-docker-secret.md#what-is-envdockersecret) file (if it does not exist),

   [run in the `VS Code Terminal`](../../../wiki/vs-code.md#run-a-command-in-the-vs-code-terminal):

   ```terminal
   cp .env.docker.example .env.docker.secret
   ```

2. [Clean up `Docker`](../../../wiki/docker.md#clean-up-docker).

#### 1.2.3. Start the services

1. To start the services,

   [run in the `VS Code Terminal`](../../../wiki/vs-code.md#run-a-command-in-the-vs-code-terminal):

   ```terminal
   docker compose --env-file .env.docker.secret up --build -d
   ```

2. To check that the containers are running,

   [run in the `VS Code Terminal`](../../../wiki/vs-code.md#run-a-command-in-the-vs-code-terminal):

   ```terminal
   docker compose --env-file .env.docker.secret ps
   ```

### 1.3. Open `Swagger UI`

1. Open in a browser: `http://<your-vm-ip-address>:<caddy-port>/docs`. Replace:

   - [`<your-vm-ip-address>`](../../../wiki/vm.md#your-vm-ip-address)
   - [`<caddy-port>`](../../../wiki/caddy.md#caddy-port)

2. [Authorize](../../../wiki/swagger.md#authorize-in-swagger-ui) with [`API_KEY`](../../../wiki/dotenv-docker-secret.md#api_key) from [`.env.docker.secret`](../../../wiki/dotenv-docker-secret.md#what-is-envdockersecret).

### 1.4. Open the browser developer tools

> [!NOTE]
> See [What are browser developer tools](../../../wiki/browser-developer-tools.md).

1. [Open the `Network` tab](../../../wiki/browser-developer-tools.md#open-the-network-tab).

### 1.5. Send a request using `Swagger UI`

1. In `Swagger UI`, expand the `POST /interactions` endpoint.
2. Click `Try it out`.
3. Enter a request body in [`JSON`](../../../wiki/file-formats.md#json) format, for example:

   ```json
   {
     "learner_id": 1,
     "item_id": 1,
     "kind": "attempt"
   }
   ```

4. Click `Execute`.

   In `Server response`, you should see:
   - `Code`: 201
   - `Details`: `Response body`:

     ```json
     {
        "id": 24,
        "kind": "attempt",
        "learner_id": 1,
        "item_id": 1,
        "created_at": "2026-02-28T15:47:19.979099"
     }
     ```

### 1.6. Inspect the request using browser developer tools

1. [Inspect the request to `/interactions`](../../../wiki/browser-developer-tools.md#inspect-a-request).

   **Note:** you've already completed the initial steps.

   You should see headers, payload, response.

### 1.7. Verify in `pgAdmin`

> [!NOTE]
> The API transformed the `JSON` from your request into a row in the `interacts` table.

1. [Open `pgAdmin`](../../../wiki/pgadmin.md#open-pgadmin).
2. [Run a query](../../../wiki/pgadmin.md#run-the-query) on the `interacts` table:

   ```sql
   SELECT * FROM interacts ORDER BY id DESC LIMIT 5;
   ```

3. Verify that the data that you sent via [`Swagger UI`](../../../wiki/swagger.md#what-is-swagger-ui) appears as a row in the `Data Output` tab.

### 1.8. Send another request and check the database

1. In [`Swagger UI`](../../../wiki/swagger.md#what-is-swagger-ui), send another `POST /interactions` request with different values.
2. In [`pgAdmin`](../../../wiki/pgadmin.md#what-is-pgadmin), run the query again and verify the new row appears.

### 1.9. Write comments for the issue

> [!NOTE]
> Select the last successful `POST /interactions` request.

- [Comment 1: write the request as `fetch` code](#191-comment-1-write-the-request-as-fetch-code)
- [Comment 2: write the response](#192-comment-2-write-the-response)
- [Comment 3: write the data output from `pgAdmin`](#193-comment-3-write-the-data-output-from-pgadmin)
- [Comment 4: paste the ERD from `pgAdmin`](#194-comment-4-paste-the-erd-from-pgadmin)

#### 1.9.1. Comment 1: write the request as `fetch` code

1. [Copy the selected request as `fetch` code](../../../wiki/browser-developer-tools.md#copy-the-request-as-fetch-code).
2. Paste this [`JavaScript`](../../../wiki/programming-language.md#javascript) code in a [`Markdown` code block](../../../wiki/file-formats.md#markdown-code-block).

   Format of the block (see in [`Markdown` preview](../../../wiki/vs-code.md#open-the-markdown-preview) if you read in `VS Code`):

   ~~~
   ```js
   <fetch-code>
   ```
   ~~~

   Example:

   ~~~
   ```js
   fetch("http://10.93.24.1:42002/interactions/", {
      "headers": {
         "accept": "application/json",
   ...
   ```
   ~~~

#### 1.9.2. Comment 2: write the response

1. [Copy the response](../../../wiki/browser-developer-tools.md#copy-the-response) to the selected request.
2. Paste the response as [`JSON`](../../../wiki/file-formats.md#json) in a [`Markdown` code block](../../../wiki/file-formats.md#markdown-code-block).

   Format of the block (see in [`Markdown` preview](../../../wiki/vs-code.md#open-the-markdown-preview) if you read in `VS Code`):

   ~~~
   ```json
   <response>
   ```
   ~~~

   Example:

   ~~~
   ```json
   {"id":31,"kind":"attempt","learner_id":1,"item_id":1,"created_at":"2026-03-01 05:47:52.411701"}
   ```
   ~~~

#### 1.9.3. Comment 3: write the data output from `pgAdmin`

1. [Copy the full data output](../../../wiki/pgadmin.md#copy-the-query-data-output) that you got when verifying in the `pgAdmin` that a new row appeared.
2. Paste the output as [`CSV`](../../../wiki/file-formats.md#csv) in a [`Markdown` code block](../../../wiki/file-formats.md#markdown-code-block).

   Format of the block (see in [`Markdown` preview](../../../wiki/vs-code.md#open-the-markdown-preview) if you read in `VS Code`):

   ~~~
   ```csv
   <data-output>
   ```
   ~~~

   Example:

   ~~~
   ```csv
   31	1	1	"attempt"	"2026-03-01 05:47:52.411701"
   30	1	1	"attempt"	"2026-03-01 05:42:03.81748"
   29	1	1	"attempt"	"2026-03-01 05:25:17.542977"
   28	1	1	"attempt"	"2026-03-01 04:12:30.760001"
   27	1	1	"attempt"	"2026-02-28 19:00:21.273761"
   ```
   ~~~

#### 1.9.4. Comment 4: paste the ERD from `pgAdmin`

1. [View the ERD in Chen notation](../../../wiki/pgadmin.md#view-the-erd-in-chen-notation).
2. Make a screenshot where all three tables are fully visible.
3. Paste the screenshot.

### 1.10. Close the issue

Close the issue.

---

## 2. Acceptance criteria

- [ ] Issue has the correct title.
- [ ] Comment 1 includes the request as `fetch` code.
- [ ] Comment 2 includes the response as `JSON` code.
- [ ] Comment 3 includes a `CSV` table with tabs as separators.
- [ ] Comment 4 includes a screenshot of the ERD.
- [ ] Issue is closed.
