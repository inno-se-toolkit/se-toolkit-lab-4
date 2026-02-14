# Run the web server using `Docker Compose`

<h4>Time</h4>

~30-40 min

<h4>Purpose</h4>

Learn to run the web server using `Docker Compose`.

<h4>Context</h4>

You should be able to run the web server using `Docker Compose` on your computer.
Then, you can check whether the web server works before the web server is deployed.

<h4>Table of contents</h4>

- [Steps](#steps)
  - [1. Create an issue](#1-create-an-issue)
  - [2. Revise environments](#2-revise-environments)
  - [3. View the file `.env.docker.example`](#3-view-the-file-envdockerexample)
  - [4. Create the file `.env.docker.secret`](#4-create-the-file-envdockersecret)
  - [5. View the file `.env.docker.secret`](#5-view-the-file-envdockersecret)
  - [Edit the file `.env.docker.secret`](#edit-the-file-envdockersecret)
  - [6. Run the web server using `Docker Compose`](#6-run-the-web-server-using-docker-compose)
  - [7. Check `/status`](#7-check-status)
    - [Check `/status` using a browser](#check-status-using-a-browser)
    - [Check `/status` using `curl`](#check-status-using-curl)
    - [Check `/status` using another address](#check-status-using-another-address)
  - [8. Stop the web server](#8-stop-the-web-server)
  - [9. Check `/status` again](#9-check-status-again)
  - [10. Write a comment for the issue](#10-write-a-comment-for-the-issue)
- [Acceptance criteria](#acceptance-criteria)

## Steps

### 1. Create an issue

Title: `[Task] Run the web server using Docker Compose`

### 2. Revise environments

You have already learned about environments in [Task 1](./task-1.md#2-learn-about-environments).

Now you will configure environment variables specific to the deployment when using `Docker Compose`.

### 3. View the file `.env.docker.example`

1. [Open the file](../../appendix/vs-code.md#open-the-file):
   [`.env.docker.example`](../../../.env.docker.example).

### 4. Create the file `.env.docker.secret`

> [!NOTE]
> The `.env.docker.secret` file contains environment variables for the Docker containers.
>
> It was added to [`.gitignore`](../../../.gitignore) because you may specify there
> [secrets](../../appendix/environments.md#secrets) such as the address of your VM.

1. [Run using the `VS Code Terminal`](../../appendix/vs-code.md#run-a-command-using-the-vs-code-terminal):

   ```terminal
   cp .env.docker.example .env.docker.secret
   ```

### 5. View the file `.env.docker.secret`

View the file using one of the following methods.

Method 1:

1. [Run using the `VS Code Terminal`](../../appendix/vs-code.md#run-a-command-using-the-vs-code-terminal):

   ```terminal
   cat .env.docker.secret
   ```

Method 2:

1. [Open the file](../../appendix/vs-code.md#open-the-file):
   [`.env.secret`](../../../.env.secret).

### Edit the file `.env.docker.secret`

### 6. Run the web server using `Docker Compose`

> [!NOTE]
> [`Docker Compose`](../../appendix/docker.md#docker-compose) can run multi-container `Docker` applications
> defined in the [`docker-compose.yml`](../../../docker-compose.yml) file.

1. [Run using the `VS Code Terminal`](../../appendix/vs-code.md#run-a-command-using-the-vs-code-terminal):

   ```terminal
   docker compose --env-file .env.docker.secret up --build
   ```

> [!NOTE]
> `Docker Compose` will provide use environment variables from the `.env.docker.secret` file and map them to variables that as specified in the `docker-compose.yml`.
>
> `Docker Compose` will then make these constructed environment variables available to the applications running in [containers](../../appendix/docker.md#container).

### 7. Check `/status`

> [!NOTE]
> `/status` is an [endpoint](../../appendix/web-development.md#endpoint) of the web server.

#### Check `/status` using a browser

1. Open in a browser: `http://127.0.0.1:42001/status`
2. You should see the response from the web server like:

    ```text
    status: "ok"
    service: "course-materials"
    ```

<!-- TODO view JSON -->

#### Check `/status` using `curl`

1. [Open a new `VS Code Terminal`](../../appendix/vs-code.md#open-a-new-terminal).
2. [Run using the `VS Code Terminal`](../../appendix/vs-code.md#run-a-command-using-the-vs-code-terminal):

    ```text
    curl http://127.0.0.1:42001/status
    ```

3. You should see the `JSON` response from the web server:

    ```json
    {"status":"ok","service":"course-materials"}
    ```

#### Check `/status` using another address

1. Go to [`docker-compose.yml`](../../docker-compose.yml).
2. Find the service `caddy`.

   **Note:** this service is running `Caddy` in a container at the port `CADDY_HOST_PORT` specified in the file `.env.docker.secret`.
3. [Open the file](../../appendix/vs-code.md#open-the-file):
   `.env.docker.secret`.
4. Find there the value of `CADDY_HOST_PORT`.
5. By default it's `42002`.
6. Open in a browser: `http://127.0.0.1:42002/status`
7. You should see the same response as you got [before](#check-status-using-a-browser).
8. `Caddy` redirected your request from this new address to the web server and returned the response from the web server back to you.

### 8. Stop the web server

Method 1:

1. [Switch to the old `VS Code Terminal`](../../appendix/vs-code.md#switch-to-another-terminal) where the web server runs.
2. Press `Ctrl+C` to stop the `Docker Compose` services.
3. You should see logs indicating that the containers are stopping.

Method 2:

1. [Run using the `VS Code Terminal`](../../appendix/vs-code.md#run-a-command-using-the-vs-code-terminal):

   ```terminal
   docker compose down
   ```

### 9. Check `/status` again

The server has stopped. Therefore, it should not respond to requests.

[Check `/status`](#7-check-status) again to ensure that.

You shouldn't see the response that you got before.

### 10. Write a comment for the issue

1. Go to the issue that you created for this task.
2. Scroll down.
3. Go to `Add a comment`.
4. Write one of the responses that you got when the web server was running.
5. Click `Close with comment`.

---

## Acceptance criteria

- [ ] Issue has the correct title
- [ ] The comment with the `JSON` response of the `/status` endpoint exists.
