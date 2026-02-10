# Run the web server

<h4>Time</h4>

~30-40 min

<h4>Purpose</h4>

Learn to run the web server written in `Python`.

<h4>Context</h4>

You should be able to run the web server on your computer.
Then, you can check whether the web server works before the web server is deployed.

<h4>Table of contents</h4>

- [1. Create an issue](#1-create-an-issue)
- [2. Learn about environments](#2-learn-about-environments)
- [Open the file `.env.no-docker.example`](#open-the-file-envno-dockerexample)
  - [Copy the `.env.example` file](#copy-the-envexample-file)
  - [Run the web server using `uv` and `poe`](#run-the-web-server-using-uv-and-poe)
- [Check `/status`](#check-status)
  - [Check `/status` using a browser](#check-status-using-a-browser)
  - [Check `/status` using `curl`](#check-status-using-curl)
- [Stop the web server](#stop-the-web-server)
- [Check `/status` again](#check-status-again)
- [Write a comment for the issue](#write-a-comment-for-the-issue)
- [Acceptance criteria](#acceptance-criteria)

## 1. Create an issue

Title: `[Task] Run the web server`

## 2. Learn about environments

Read these sections:

1. [Environment variables](../../appendix/environments.md#environment-variables)
2. [`.env` file](../../appendix/environments.md#env-file)

## Open the file `.env.no-docker.example`

1. [Open the file using the `Command Palette`](../../appendix/vs-code.md#open-a-file-using-the-command-palette): [`.env.no-docker.example`](../../../.env.no-docker.example).

### Copy the `.env.example` file

1. [Run using the `Terminal`](../../appendix/vs-code.md#run-a-command-using-the-terminal):

   ```terminal
   cp .env.no-docker.example .env.no-docker
   ```

> [!NOTE]
> The `.env.no-docker` file is added to [`.gitignore`](../../../.gitignore) because you may specify there
> [secrets](../../appendix/environments.md#secrets) such as the address of your VM.

### Run the web server using `uv` and `poe`

> [!NOTE]
> [`poe`](https://poethepoet.natn.io/) can run tasks
> specified in the [`pyproject.toml`](../../../pyproject.toml) in the `[tool.poe.tasks]` section.

1. [Run using the `Terminal`](../../appendix/vs-code.md#run-a-command-using-the-terminal):

   ```terminal
   uv run poe dev
   ```

2. The web server will automatically read the [environment variables](../../appendix/environments.md#environment-variables) from the `.env.no-docker` file.

> [!NOTE]
> You will see in the output a key shortcut to stop the server such as `Ctrl+C`.

## Check `/status`

> [!NOTE]
> `/status` is an [endpoint](../../appendix/web-development.md#endpoint) of the web server.

### Check `/status` using a browser

1. Open in a browser: `http://127.0.0.1:42000/status`
2. You should see the response from the web server like:

    ```text
    status: "ok"
    service: "course-material"
    ```

<!-- TODO view JSON -->

### Check `/status` using `curl`

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

## Stop the web server

1. [Switch to the old `Terminal`](../../appendix/vs-code.md#switch-to-another-terminal) where the web server runs.
2. Run the key shortcut that you saw when running the server to stop the server.

## Check `/status` again

The server has stopped. Therefore, it should not respond to requests.

[Check `/status`](#check-status) again to ensure that.

You shouldn't see the response that you got before.

## Write a comment for the issue

1. Go to the issue that you created for this task.
2. Scroll down.
3. Go to `Add a comment`.
4. Write one of the responses that you got when the web server was running.
5. Click `Close with comment`.

## Acceptance criteria

- [ ] Issue has the correct title
- [ ] The comment with the `JSON` response of the `/status` endpoint exists.
