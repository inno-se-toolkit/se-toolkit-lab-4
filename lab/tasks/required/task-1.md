# Run the web server

<h4>Time</h4>

~30-40 min

<h4>Purpose</h4>

Learn to run the web server written in `Python`.

<h4>Context</h4>

You should be able to run the web server on your computer.
Then, you can check whether the web server works before the web server is deployed.

<h4>Table of contents</h4>

- [Steps](#steps)
  - [1. Create an issue](#1-create-an-issue)
  - [2. Learn about environments](#2-learn-about-environments)
  - [3. View the file `.env.no-docker.example`](#3-view-the-file-envno-dockerexample)
  - [4. Create the file `.env.secret`](#4-create-the-file-envsecret)
  - [5. View the file `.env.secret`](#5-view-the-file-envsecret)
  - [6. Use a free `$PORT`](#6-use-a-free-port)
  - [7. Run the web server using `uv` and `poe`](#7-run-the-web-server-using-uv-and-poe)
  - [8. Check `/status`](#8-check-status)
    - [Check `/status` using a browser](#check-status-using-a-browser)
    - [Check `/status` using `curl`](#check-status-using-curl)
  - [9. Stop the web server](#9-stop-the-web-server)
  - [10. Force stop the web server](#10-force-stop-the-web-server)
  - [11. Check `/status` again](#11-check-status-again)
  - [12. Write a comment for the issue](#12-write-a-comment-for-the-issue)
- [Acceptance criteria](#acceptance-criteria)

## Steps

### 1. Create an issue

Title: `[Task] Run the web server`

### 2. Learn about environments

Read the following sections:

1. [Environment variables](../../appendix/environments.md#environment-variables)
2. [`.env` file](../../appendix/environments.md#env-file)

### 3. View the file `.env.no-docker.example`

1. [Open the file using the `Command Palette`](../../appendix/vs-code.md#open-a-file-using-the-command-palette): [`.env.no-docker.example`](../../../.env.no-docker.example).

### 4. Create the file `.env.secret`

1. [Run using the `Terminal`](../../appendix/vs-code.md#run-a-command-using-the-terminal):

   ```terminal
   cp .env.no-docker.example .env.secret
   ```

### 5. View the file `.env.secret`

> [!NOTE]
> The `.env.secret` file was added to [`.gitignore`](../../../.gitignore) because you may specify there
> [secrets](../../appendix/environments.md#secrets) such as the address of your VM.

View the file using one of the following methods.

Method 1:

1. [Run using the `Terminal`](../../appendix/vs-code.md#run-a-command-using-the-terminal):

   ```terminal
   cat .env.secret
   ```

Method 2:

1. [Open the file using the `Command Palette`](../../appendix/vs-code.md#open-a-file-using-the-command-palette): [`.env.secret`](../../../.env.no-docker.example).

### 6. Use a free `$PORT`

> [!NOTE]
> `$PORT` here will be substituted with the value of the `PORT` environment variable from the `.env.secret` file.
>
> The `kport inspect $PORT` command will be run in the [`bash`](../../appendix/linux.md#bash) shell.

1. Inspect what's running on `$PORT`:

   [Run using the `Terminal`](../../appendix/vs-code.md#run-a-command-using-the-terminal):

   ```terminal
   uv run --env-file .env.secret bash -c 'kport inspect $PORT'
   ```

2. You should see something like `Port 42000 is free`.
3. If you see `Process: python3`:
   1. It's probably the web server running if you tried running it before.
   2. You can safely [force stop it](#10-force-stop-the-web-server).
4. Otherwise:
   1. Go to the `.env.secret` file.
   2. Write another value for `PORT`, e.g., `41000`.
   3. Inspect what's running on the new `$PORT` (`41000`) as explained above.

### 7. Run the web server using `uv` and `poe`

> [!NOTE]
> [`poe`](https://poethepoet.natn.io/) can run tasks
> specified in the [`pyproject.toml`](../../../pyproject.toml) in the `[tool.poe.tasks]` section.

1. [Run using the `Terminal`](../../appendix/vs-code.md#run-a-command-using-the-terminal):

   ```terminal
   uv run poe dev
   ```

2. The web server will automatically read the [environment variables](../../appendix/environments.md#environment-variables) from the `.env.secret` file.

> [!NOTE]
> You will see in the output a key shortcut to stop the server such as `Ctrl+C`.

### 8. Check `/status`

> [!NOTE]
> `/status` is an [endpoint](../../appendix/web-development.md#endpoint) of the web server.

#### Check `/status` using a browser

1. Open in a browser: `http://127.0.0.1:42000/status`
2. You should see the response from the web server like:

    ```text
    status: "ok"
    service: "course-material"
    ```

<!-- TODO view JSON -->

#### Check `/status` using `curl`

1. [Open a new `Terminal`](../../appendix/vs-code.md#open-a-new-terminal).
2. [Run using the `Terminal`](../../appendix/vs-code.md#run-a-command-using-the-terminal):

    ```text
    curl http://127.0.0.1:42000/status
    ```

3. You should see the `JSON` response from the web server:

    ```json
    {"status":"ok","service":"course-material"}
    ```

<!-- TODO add check status using the /docs -->

### 9. Stop the web server

1. [Switch to the old `Terminal`](../../appendix/vs-code.md#switch-to-another-terminal) where the web server runs.
2. Press the key shortcut that you saw when running the server to stop the server.
3. You should see `INFO:     Waiting for application shutdown.`

### 10. Force stop the web server

1. [Run using the `Terminal`](../../appendix/vs-code.md#run-a-command-using-the-terminal):

   ```terminal
   uv run --env-file .env.secret bash -c 'kport kill $PORT'
   ```

2. Confirm suggested actions.
3. Rerun using the `Terminal` the command provided above until you see something like `Port 42000 is free`.

### 11. Check `/status` again

The server has stopped. Therefore, it should not respond to requests.

[Check `/status`](#8-check-status) again to ensure that.

You shouldn't see the response that you got before.

### 12. Write a comment for the issue

1. Go to the issue that you created for this task.
2. Scroll down.
3. Go to `Add a comment`.
4. Write one of the responses that you got when the web server was running.
5. Click `Close with comment`.

---

## Acceptance criteria

- [ ] Issue has the correct title
- [ ] The comment with the `JSON` response of the `/status` endpoint exists.
