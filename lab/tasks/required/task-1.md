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
  - [3. View the file `.env.example`](#3-view-the-file-envexample)
  - [4. Create the file `.env.secret`](#4-create-the-file-envsecret)
  - [5. View the file `.env.secret`](#5-view-the-file-envsecret)
  - [6. Check that the port `$PORT` is free](#6-check-that-the-port-port-is-free)
  - [7. Use a free port](#7-use-a-free-port)
  - [8. Run the web server](#8-run-the-web-server)
  - [9. Check `/status`](#9-check-status)
  - [10. Stop the web server](#10-stop-the-web-server)
  - [11. Force stop the web server](#11-force-stop-the-web-server)
  - [12. Check `/status` again](#12-check-status-again)
  - [13. Write a comment for the issue](#13-write-a-comment-for-the-issue)
- [Acceptance criteria](#acceptance-criteria)

## Steps

### 1. Create an issue

Title: `[Task] Run the web server`

### 2. Learn about environments

Read the following sections:

1. [Environment variables](../../appendix/environments.md#environment-variables)
2. [`.env` file](../../appendix/environments.md#env-file)

### 3. View the file `.env.example`

1. [Open the file](../../appendix/vs-code.md#open-the-file):
   [`.env.example`](../../../.env.example).

### 4. Create the file `.env.secret`

1. [Run using the `VS Code Terminal`](../../appendix/vs-code.md#run-a-command-using-the-vs-code-terminal):

   ```terminal
   cp .env.example .env.secret
   ```

### 5. View the file `.env.secret`

> [!NOTE]
> The `.env.secret` file was added to [`.gitignore`](../../../.gitignore) because you may specify there
> [secrets](../../appendix/environments.md#secrets) such as the address of your VM.

View the file using one of the following methods.

Method 1:

1. [Run using the `VS Code Terminal`](../../appendix/vs-code.md#run-a-command-using-the-vs-code-terminal):

   ```terminal
   cat .env.secret
   ```

Method 2:

1. [Open the file](../../appendix/vs-code.md#open-the-file):
   `.env.secret`.

### 6. Check that the port `$PORT` is free

> [!NOTE]
> The `PORT` variable from the `.env.secret` is the [port number](../../appendix/linux.md#port)
> at which the web server will run.
>
> The expression `$PORT` in the command below will be substituted with the value
> of the `PORT` environment variable loaded from the `.env.secret` file via [`source`](../../appendix/useful-programs.md#source).

1. Inspect what's [listening](../../appendix/linux.md#listen-on-port) on the port `$PORT`:

   [Run using the `VS Code Terminal`](../../appendix/vs-code.md#run-a-command-using-the-vs-code-terminal):

   ```terminal
   source .env.secret && lsof -i :$PORT
   ```

2. If the command produces **no output**, the port is free.
3. Otherwise, you need to use a [free port](#7-use-a-free-port).

### 7. Use a free port

1. If you see output with `python`:
   1. It's probably the web server running if you tried running it before.
   2. You can safely [force stop it](#11-force-stop-the-web-server).
2. Otherwise:
   1. [Open the file](../../appendix/vs-code.md#open-the-file):
      `.env.secret`
   2. Write another value for `PORT`, e.g., `41000`.
   3. [Check](#6-check-that-the-port-port-is-free) that the new `$PORT` (`41000`) is free.

### 8. Run the web server

> [!NOTE]
> [`poe`](https://poethepoet.natn.io/) can run tasks
> specified in the [`pyproject.toml`](../../../pyproject.toml) in the `[tool.poe.tasks]` section.

1. [Run using the `VS Code Terminal`](../../appendix/vs-code.md#run-a-command-using-the-vs-code-terminal):

   ```terminal
   uv run poe dev
   ```

2. The web server will automatically read the [environment variables](../../appendix/environments.md#environment-variables) from the `.env.secret` file.

> [!NOTE]
> You will see in the output a key shortcut to stop the server such as `Ctrl+C`.

### 9. Check `/status`

> [!NOTE]
> `/status` is an [endpoint](../../appendix/web-development.md#endpoint) of the web server.

1. [Send a `GET` query](../../appendix/web-development.md#send-a-get-query)
   to `http://127.0.0.1:42000/status`.
2. [Pretty-print the `JSON` response](../../appendix/web-development.md#pretty-print-the-json-response).

> [!TIP]
> You can also check the `/status` endpoint using the auto-generated API documentation
> at <http://127.0.0.1:42000/docs>.

### 10. Stop the web server

1. [Switch to the old `VS Code Terminal`](../../appendix/vs-code.md#switch-to-another-terminal) where the web server runs.
2. Press the key shortcut (`Ctrl+C`) to stop the server.
3. You should see `INFO:     Waiting for application shutdown.`

### 11. Force stop the web server

> [!NOTE]
> Run if you see the `Address already in use` error after trying to run the web server.

1. [Run using the `VS Code Terminal`](../../appendix/vs-code.md#run-a-command-using-the-vs-code-terminal):

   ```terminal
   source .env.secret && kill $(lsof -ti :$PORT)
   ```

2. [Check that the port is free](#6-check-that-the-port-port-is-free).

### 12. Check `/status` again

The server has stopped. Therefore, it should not respond to requests.

[Check `/status`](#9-check-status) again to ensure that.

You shouldn't see the response that you got before.

### 13. Write a comment for the issue

1. Go to the issue that you created for this task.
2. Scroll down.
3. Go to `Add a comment`.
4. Write one of the responses that you got when the web server was running.
5. Click `Close with comment`.

---

## Acceptance criteria

- [ ] Issue has the correct title.
- [ ] The comment with the `JSON` response of the `/status` endpoint exists.
