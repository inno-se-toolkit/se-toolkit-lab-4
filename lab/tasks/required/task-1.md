# Observe System Component Interaction

<h4>Time</h4>

~25 min

<h4>Purpose</h4>

Trace a request from `Swagger` through the API to the database using the browser developer tools and `pgAdmin`.

<h4>Context</h4>

Before adding new features, you will redeploy the system from Lab 3 and confirm it still works.
Then you will send requests and observe how data flows through the components: browser → API → database.

<h4>Table of contents</h4>

- [1. Steps](#1-steps)
  - [1.1. Create a `Lab Task` issue](#11-create-a-lab-task-issue)
  - [1.2. Deploy the back-end to the VM](#12-deploy-the-back-end-to-the-vm)
  - [1.3. Open `Swagger UI`](#13-open-swagger-ui)
  - [1.4. Open the browser developer tools](#14-open-the-browser-developer-tools)
  - [1.5. Send a request and observe](#15-send-a-request-and-observe)
  - [1.6. Verify in `pgAdmin`](#16-verify-in-pgadmin)
  - [1.7. Send another request and check the database](#17-send-another-request-and-check-the-database)
  - [1.8. Write a comment for the issue](#18-write-a-comment-for-the-issue)
- [2. Acceptance criteria](#2-acceptance-criteria)

## 1. Steps

### 1.1. Create a `Lab Task` issue

Title: `[Task] Observe System Component Interaction`

### 1.2. Deploy the back-end to the VM

<!-- TODO: add specific deployment steps referencing the Lab 3 deployment wiki page or process once finalized -->

1. Deploy the back-end to your VM using the same process as in Lab 3.

> [!Important]
> Remember to expose your services to connections from other machines by setting relevant `HOST_ADDRESS`es to `0.0.0.0`.
> `0.0.0.0` means the server listens on **all network interfaces**.
> This makes the service accessible from outside the VM (e.g., from your laptop).

> [!NOTE]
> This is a recap of the Lab 3 deployment. If you need a reminder, see the [Lab 3 Task 4](https://github.com/inno-se-toolkit/se-toolkit-lab-3/blob/main/lab/tasks/required/task-4.md). Importantly you need to adjust those instructions to this lab number.

### 1.3. Open `Swagger UI`

1. Open in a browser: `http://<your-vm-ip-address>:42002/docs`.

   Replace [`<your-vm-ip-address>`](../../../wiki/vm.md#your-vm-ip-address) with the IP address of your VM.

2. [Authorize](../../../wiki/swagger.md#authorize-in-swagger-ui) with the API key.

### 1.4. Open the browser developer tools

> [!NOTE]
> The browser developer tools let you inspect [HTTP](../../../wiki/http.md) requests and responses that your browser sends and receives.

1. Open the browser developer tools. Complete the following steps:

   Method 1: press `F12`.

   Method 2: press `Ctrl+Shift+I` (or `Cmd+Option+I` on macOS).

2. Go to the `Network` tab.

### 1.5. Send a request and observe

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
5. In the browser developer tools `Network` tab, find the request to `/interactions`.
6. Click on the request to open its details.
7. Observe the following:
   - The `Headers` tab: the [HTTP method](../../../wiki/http.md#http-method) and the request URL.
   - The `Payload` tab: the request body you sent.
   - The `Response` tab: the [status code](../../../wiki/http.md#http-response-status-code) and response body.

> [!NOTE]
> The request travels from your browser to the API running on the VM, which stores the data in the `PostgreSQL` database.

### 1.6. Verify in `pgAdmin`

1. [Open `pgAdmin`](../../../wiki/pgadmin.md#open-pgadmin).
2. [Run a query](../../../wiki/pgadmin.md#run-a-query) on the `interacts` table:

   ```sql
   SELECT * FROM interacts ORDER BY id DESC LIMIT 5;
   ```

3. Verify that the row you just created appears in the results.

### 1.7. Send another request and check the database

1. In `Swagger UI`, send another `POST /interactions` request with different values.
2. In `pgAdmin`, run the query again and verify the new row appears.

### 1.8. Write a comment for the issue

1. Take a screenshot of the browser developer tools `Network` tab showing the `POST /interactions` request and response.
2. Take a screenshot of `pgAdmin` showing the corresponding row in the database.
3. Write a comment on the issue and paste both screenshots.
4. Close the issue.

---

## 2. Acceptance criteria

- [ ] Issue has the correct title.
- [ ] Issue comment includes a screenshot of the browser developer tools showing the HTTP request and response.
- [ ] Issue comment includes a screenshot of `pgAdmin` showing the corresponding database row.
- [ ] Issue is closed.
