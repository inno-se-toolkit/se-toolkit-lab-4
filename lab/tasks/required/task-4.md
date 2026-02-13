# Deploy the web server to the VM

<h4>Time</h4>

~30-40 min

<h4>Purpose</h4>

Learn to deploy the web server to a remote [VM](../../appendix/vm.md#your-vm) using `Docker Compose`.

<h4>Context</h4>

You have already run the web server [locally](./task-1.md) and using [`Docker Compose` on your computer](./task-3.md).

Now you will deploy it to the university VM so that it is accessible over the network.

<h4>Table of contents</h4>

- [Steps](#steps)
  - [1. Create an issue](#1-create-an-issue)
  - [2. Connect to the VM](#2-connect-to-the-vm)
  - [3. Clone the fork on the VM](#3-clone-the-fork-on-the-vm)
  - [4. Create the file `.env.docker.secret`](#4-create-the-file-envdockersecret)
  - [5. View the file `.env.docker.secret`](#5-view-the-file-envdockersecret)
  - [6. Run the web server using `Docker Compose`](#6-run-the-web-server-using-docker-compose)
  - [7. Check `/status` from the VM](#7-check-status-from-the-vm)
  - [8. Check `/status` from your laptop](#8-check-status-from-your-laptop)
  - [9. Write a comment for the issue](#9-write-a-comment-for-the-issue)
- [Acceptance criteria](#acceptance-criteria)

## Steps

### 1. Create an issue

Title: `[Task] Deploy the web server to the VM`

### 2. Connect to the VM

> [!NOTE]
> If you haven't set up `SSH` yet, follow the steps in the [`SSH` appendix](../../appendix/ssh.md).

1. [Run using the `VS Code Terminal`](../../appendix/vs-code.md#run-a-command-using-the-vs-code-terminal):

   ```terminal
   ssh se-toolkit-vm
   ```

2. You should see the remote shell prompt (e.g., `root@<your-vm-name>:~#`).

### 3. Clone the fork on the VM

1. Run on the VM:

   ```terminal
   git clone <fork-url>
   ```

   Note: replace `<fork-url>` with the URL of your fork (e.g., `https://github.com/<your-username>/se-toolkit-lab-2`).

2. Run on the VM:

   ```terminal
   cd se-toolkit-lab-2
   ```

### 4. Create the file `.env.docker.secret`

1. Run on the VM:

   ```terminal
   cp .env.docker.example .env.docker.secret
   ```

### 5. View the file `.env.docker.secret`

1. Run on the VM:

   ```terminal
   cat .env.docker.secret
   ```

2. Notice that `CADDY_HOST_ADDRESS` is set to `0.0.0.0`.

> [!NOTE]
> `0.0.0.0` means the server listens on **all network interfaces**.
> This makes the web server accessible from outside the VM (e.g., from your laptop).
>
> Compare this with `127.0.0.1` (localhost), which only allows connections from the VM itself.

### 6. Run the web server using `Docker Compose`

1. Run on the VM:

   ```terminal
   docker compose --env-file .env.docker.secret up --build -d
   ```

> [!NOTE]
> The `-d` flag runs the containers in the background (detached mode).
> This is useful on a remote server because the containers keep running after you close the terminal.

2. Check that the containers are running:

   ```terminal
   docker compose ps
   ```

3. You should see two containers with the status `Up`.

### 7. Check `/status` from the VM

1. Run on the VM:

   ```terminal
   curl http://127.0.0.1:42002/status | jq .
   ```

2. You should see the `JSON` response from the web server:

   ```json
   {
     "status": "ok",
     "service": "course-materials"
   }
   ```

### 8. Check `/status` from your laptop

> [!NOTE]
> You can find the IP address of your VM on the [VM page](../../appendix/vm.md#get-the-ip-address-of-the-vm).

1. Open a new terminal **on your laptop** (not on the VM).
2. Run:

   ```terminal
   curl http://<vm-ip>:42002/status | jq .
   ```

   Note: replace `<vm-ip>` with the IP address of your VM (e.g., `10.93.24.98`).

3. You should see the same `JSON` response as in the previous step.

> [!IMPORTANT]
> Keep the web server running on the VM. Do not run `docker compose down`.
>
> The deployment will be checked automatically.

### 9. Write a comment for the issue

1. Go to the issue that you created for this task.
2. Scroll down.
3. Go to `Add a comment`.
4. Write one of the responses that you got when the web server was running.
5. Click `Close with comment`.

---

## Acceptance criteria

- [ ] Issue has the correct title
- [ ] The comment with the `JSON` response of the `/status` endpoint exists.
