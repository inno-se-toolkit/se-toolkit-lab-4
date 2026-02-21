# Lab setup

- [1. Required steps](#1-required-steps)
  - [1.1. (NEW) Find a partner](#11-new-find-a-partner)
  - [1.2. Start creating a VM](#12-start-creating-a-vm)
  - [1.3. Set up your fork](#13-set-up-your-fork)
    - [1.3.1. Sign in on `GitHub`](#131-sign-in-on-github)
    - [1.3.2. (NEW) Fork the course instructors' repo](#132-new-fork-the-course-instructors-repo)
    - [1.3.3. (NEW) Go to your fork](#133-new-go-to-your-fork)
    - [1.3.4. (NEW) Enable issues](#134-new-enable-issues)
    - [1.3.5. (NEW) Add a classmate as a collaborator](#135-new-add-a-classmate-as-a-collaborator)
    - [1.3.6. (NEW) Protect your `main` branch](#136-new-protect-your-main-branch)
  - [1.4. Install programs](#14-install-programs)
    - [1.4.1. Install `VS Code`](#141-install-vs-code)
    - [1.4.2. Install `Git`](#142-install-git)
    - [1.4.3. Install `Docker`](#143-install-docker)
    - [1.4.4. (`Windows` only) Install `Ubuntu 24.04` using WSL](#144-windows-only-install-ubuntu-2404-using-wsl)
  - [1.5. (NEW) Open in `VS Code` the `software-engineering-toolkit` directory](#15-new-open-in-vs-code-the-software-engineering-toolkit-directory)
  - [1.6. Set up `Git`](#16-set-up-git)
    - [1.6.1. Check your `Git` config](#161-check-your-git-config)
    - [1.6.2. Configure `Git`](#162-configure-git)
  - [1.7. (NEW) Clone your fork and open it in `VS Code`](#17-new-clone-your-fork-and-open-it-in-vs-code)
    - [1.7.1. (NEW) Copy your fork `URL`](#171-new-copy-your-fork-url)
    - [1.7.2. (NEW) Clone your fork](#172-new-clone-your-fork)
    - [1.7.3. (NEW) Open the cloned repo in `VS Code`](#173-new-open-the-cloned-repo-in-vs-code)
  - [1.8. (NEW) (`Windows` only) Set the default shell](#18-new-windows-only-set-the-default-shell)
  - [1.9. Continue creating a VM](#19-continue-creating-a-vm)
  - [1.10. Set up `Python` in `VS Code`](#110-set-up-python-in-vs-code)
    - [1.10.1. Install `uv`](#1101-install-uv)
    - [1.10.2. (NEW) Install `Python` and dependencies](#1102-new-install-python-and-dependencies)
    - [1.10.3. (NEW) Select the `Python` interpreter](#1103-new-select-the-python-interpreter)
    - [1.10.4. (NEW) Check that `Python` works](#1104-new-check-that-python-works)
  - [1.11. (NEW) Start the services](#111-new-start-the-services)
    - [1.11.1. (NEW) Set up the `Docker` environment](#1111-new-set-up-the-docker-environment)
    - [1.11.2. (NEW) Start the services using `Docker Compose`](#1112-new-start-the-services-using-docker-compose)
  - [1.12. (NEW) Open a new terminal](#112-new-open-a-new-terminal)
  - [1.13. (NEW) Observe containers and services](#113-new-observe-containers-and-services)
    - [1.13.1. (NEW) List running containers](#1131-new-list-running-containers)
    - [1.13.2. (NEW) See logs of the running services](#1132-new-see-logs-of-the-running-services)
  - [1.14. (NEW) Set up the services](#114-new-set-up-the-services)
    - [1.14.1. (NEW) Open `Swagger UI`](#1141-new-open-swagger-ui)
    - [1.14.2. (NEW) Set up `pgAdmin`](#1142-new-set-up-pgadmin)
  - [1.15. (NEW) Stop the services](#115-new-stop-the-services)
  - [1.16. (NEW) Add SSH key for the autochecker](#116-new-add-ssh-key-for-the-autochecker)
- [2. Optional steps](#2-optional-steps)
  - [2.1. (NEW) Learn to go back after clicking a link](#21-new-learn-to-go-back-after-clicking-a-link)
  - [2.2. Set up a coding agent](#22-set-up-a-coding-agent)
  - [2.3. Set up the shell prompt](#23-set-up-the-shell-prompt)
  - [2.4. Customize the `Source Control`](#24-customize-the-source-control)
  - [2.5. Get familiar with `GitLens`](#25-get-familiar-with-gitlens)
  - [2.6. Create a label for tasks](#26-create-a-label-for-tasks)
  - [2.7. View `Markdown` files in `VS Code`](#27-view-markdown-files-in-vs-code)

## 1. Required steps

> [!NOTE]
> We provide all of the hardest steps in the lab setup
> so that TAs can help you get the right setup during the lab.
>
> Tasks are more or less easy when you have the right setup.

> [!NOTE]
> Some steps have the `(NEW)` label.
>
> These steps must be completed to get the right setup for this lab,
> even if you have completed similar steps in the previous lab.

### 1.1. (NEW) Find a partner

1. Find a partner for this lab.
2. Sit next to them.

> [!IMPORTANT]
> You work on tasks independently from your partner.
>
> You and your partner work together when reviewing each other's work.

### 1.2. Start creating a VM

> [!NOTE]
> Skip this step if you can [connect to your VM](../appendix/vm.md#connect-to-the-vm).

[Create a subscription](../appendix/vm.md#create-a-subscription) to be able to create a VM.

### 1.3. Set up your fork

#### 1.3.1. Sign in on `GitHub`

1. Sign in on [`GitHub`](https://github.com/).
2. [Find `<your-github-username>`](../appendix/github.md#find-your-github-username).

#### 1.3.2. (NEW) Fork the course instructors' repo

1. [Fork the course instructors' repo](../appendix/github.md#fork-a-repo).

   The course instructors' repo [URL](../appendix/web-development.md#url) is <https://github.com/inno-se-toolkit/se-toolkit-lab-3>

#### 1.3.3. (NEW) Go to your fork

1. [Go to your fork](../appendix/github.md#go-to-your-fork).

   The [URL](../appendix/web-development.md#url) of your fork should look like `https://github.com/<your-github-username>/se-toolkit-lab-3`.

#### 1.3.4. (NEW) Enable issues

1. [Enable issues](../appendix/github.md#enable-issues).

#### 1.3.5. (NEW) Add a classmate as a collaborator

1. [Add a collaborator](../appendix/github.md#add-a-collaborator) — your partner.
2. Your partner should add you as a collaborator in their repo.
3. It's OK if your collaborator can't change `Settings` in your repo.

#### 1.3.6. (NEW) Protect your `main` branch

> [!NOTE]
> Branch protection prevents accidental pushes directly to `main`.
> This enforces the PR workflow and ensures all changes are reviewed.

1. [Protect a branch](../appendix/github.md#protect-a-branch).

### 1.4. Install programs

#### 1.4.1. Install `VS Code`

1. Install [`VS Code`](https://code.visualstudio.com/) if not installed.
2. (Optional) [Learn more](../appendix/vs-code.md) about `VS Code`.

#### 1.4.2. Install `Git`

1. [Install `Git`](https://git-scm.com/install/) if not installed.

2. (Optional) [Learn more](../appendix/git.md) about `Git`.

#### 1.4.3. Install `Docker`

1. [Install `Docker`](../appendix/docker.md#install-docker) if not installed.

2. (Optional) [Learn more](../appendix/docker.md#what-is-docker) about `Docker`.

#### 1.4.4. (`Windows` only) Install `Ubuntu 24.04` using WSL

1. [Check the current shell in the `VS Code Terminal`](../appendix/vs-code.md#check-the-current-shell-in-the-vs-code-terminal).
2. [Set up running `VS Code` using `WSL`](../appendix/vs-code.md#windows-only-set-up-running-vs-code-in-wsl) if the shell is not `bash` or `zsh`.

### 1.5. (NEW) Open in `VS Code` the `software-engineering-toolkit` directory

1. Inside the [`Desktop` directory](../appendix/file-system.md#desktop-directory),
   create the directory `software-engineering-toolkit`.

   Skip this step if this directory exists.

2. [Open in `VS Code` the directory](../appendix/git-vscode.md#open-in-vs-code-the-directory):
   `software-engineering-toolkit`.

### 1.6. Set up `Git`

#### 1.6.1. Check your `Git` config

1. [Check your Git config](../appendix/git.md#check-your-git-config).

#### 1.6.2. Configure `Git`

[Configure Git](../appendix/git.md#configure-git) if you want to change the values that you saw while [checking your `Git` config](#161-check-your-git-config).

### 1.7. (NEW) Clone your fork and open it in `VS Code`

#### 1.7.1. (NEW) Copy your fork `URL`

1. [Go to your fork](#133-new-go-to-your-fork).
2. Copy [`<your-fork-url>`](../appendix/github.md#your-fork-url).

   It should look like `https://github.com/<your-github-username>/se-toolkit-lab-3`.

> [!NOTE]
> Here, the `<repo-name>` is `se-toolkit-lab-3`.

#### 1.7.2. (NEW) Clone your fork

1. [Clone your fork](../appendix/git-vscode.md#clone-the-repo):

   - Replace `<repo-url>` with [`<your-fork-url>`](../appendix/github.md#your-fork-url).
   - Replace `<repo-name>` with `se-toolkit-lab-3`.

#### 1.7.3. (NEW) Open the cloned repo in `VS Code`

1. [Open in `VS Code` the directory](../appendix/git-vscode.md#open-in-vs-code-the-directory):
   `se-toolkit-lab-3`.
2. [Install recommended extensions](../appendix/vs-code.md#install-recommended-extensions).

### 1.8. (NEW) (`Windows` only) Set the default shell

1. [Check and set the current shell in the `VS Code Terminal`](../appendix/vs-code.md#check-the-current-shell-in-the-vs-code-terminal).

### 1.9. Continue creating a VM

1. [Set up `SSH`](../appendix/ssh.md#set-up-ssh).
2. [Create a VM using the subscription](../appendix/vm.md#create-a-vm-using-the-subscription).

### 1.10. Set up `Python` in `VS Code`

#### 1.10.1. Install `uv`

> [!NOTE]
> [`uv`](../appendix/python.md#uv) is a package manager for [`Python`](../appendix/python.md).

1. [Install `uv`](../appendix/python.md#install-uv).

#### 1.10.2. (NEW) Install `Python` and dependencies

> [!NOTE]
> The dependencies have been updated in this project version.

1. [Install `Python` and dependencies](../appendix/python.md#install-python-and-dependencies).

#### 1.10.3. (NEW) Select the `Python` interpreter

1. [Select the `Python` interpreter](../appendix/python.md#select-the-python-interpreter).

#### 1.10.4. (NEW) Check that `Python` works

1. [Check that `Python` works](../appendix/python.md#check-that-python-works).

### 1.11. (NEW) Start the services

> [!NOTE]
> A [service](../appendix/docker.md#service) in [`Docker Compose`](../appendix/docker-compose.md) defines how to run a [container](../appendix/docker.md#container).
>
> `Docker Compose` lets you start multiple containers at once.

#### 1.11.1. (NEW) Set up the `Docker` environment

1. [Run using the `VS Code Terminal`](../appendix/vs-code.md#run-a-command-using-the-vs-code-terminal):

   ```terminal
   cp .env.docker.example .env.docker.secret
   ```

> [!NOTE]
> The `.env.docker.secret` file contains environment variables for the `Docker` containers.
>
> It was added to [`.gitignore`](../../.gitignore) because you may specify there
> [secrets](../appendix/environments.md#secrets) such as the API key or the address of your VM.

> [!TIP]
> No edits are needed for local development.
> The default values in [`.env.docker.example`](../../.env.docker.example) work out of the box.

#### 1.11.2. (NEW) Start the services using `Docker Compose`

1. [Run using the `VS Code Terminal`](../appendix/vs-code.md#run-a-command-using-the-vs-code-terminal):

   ```terminal
   docker compose --env-file .env.docker.secret up --build
   ```

   > **NOTE**
   >
   > [`Docker Compose`](../appendix/docker-compose.md) reads environment variables from `.env.docker.secret`
   > and uses them to configure the containers defined in [`docker-compose.yml`](../../docker-compose.yml).

2. Wait for the services to start. You should see log output from the `app`, `postgres`, `pgadmin`, and `caddy` containers.

   > **NOTE**
   >
   > The database is initialized from [`src/app/data/init.sql`](../../src/app/data/init.sql) only on the **first** start of the `PostgreSQL` container.
   >
   > If you need to re-initialize the database (e.g., after pulling upstream changes to `init.sql`), see [Resetting the database](../appendix/docker-postgres.md#resetting-the-database).

### 1.12. (NEW) Open a new terminal

1. [Open a new `VS Code Terminal`](../appendix/vs-code.md#open-a-new-vs-code-terminal).

### 1.13. (NEW) Observe containers and services

#### 1.13.1. (NEW) List running containers

1. [Run using the `VS Code Terminal`](../appendix/vs-code.md#run-a-command-using-the-vs-code-terminal):

   ```terminal
   docker compose --env-file .env.docker.secret ps
   ```

#### 1.13.2. (NEW) See logs of the running services

1. See logs for all services:

   [Run using the `VS Code Terminal`](../appendix/vs-code.md#run-a-command-using-the-vs-code-terminal):

   ```terminal
   docker compose --env-file .env.docker.secret logs
   ```

2. [See logs for a specific service](../appendix/docker-compose.md#docker-compose-logs-for-a-specific-service):

   ```terminal
   docker compose --env-file .env.docker.secret logs postgres
   ```

### 1.14. (NEW) Set up the services

#### 1.14.1. (NEW) Open `Swagger UI`

1. Open in a browser: <http://127.0.0.1:42001/docs>.

   You should see the [`Swagger UI`](../appendix/swagger.md#swagger-ui) page with the [API](../appendix/web-development.md#api) documentation.

#### 1.14.2. (NEW) Set up `pgAdmin`

> [!NOTE]
> [`pgAdmin`](../appendix/pgadmin.md#what-is-pgadmin) takes 2-3 minutes to start after you have [started the services](#111-new-start-the-services).

1. [Open `pgAdmin`](../appendix/pgadmin.md#open-pgadmin).
2. [Add a server in `pgAdmin`](../appendix/pgadmin.md#add-a-server-in-pgadmin).
3. [Browse tables](../appendix/pgadmin.md#browse-tables).
4. Verify that the following tables exist and contain data:
   - `items`
   - `learners`
   - `interaction_logs`

> [!TIP]
> To view the data in a table, right-click the table and select `View/Edit Data` -> `All Rows`.

### 1.15. (NEW) Stop the services

1. [Check that the current directory is `se-toolkit-lab-3`](../appendix/shell.md#check-the-current-directory-is-directory-name).
2. [Run using the `VS Code Terminal`](../appendix/vs-code.md#run-a-command-using-the-vs-code-terminal):

   ```terminal
   docker compose --env-file .env.docker.secret down
   ```

### 1.16. (NEW) Add SSH key for the autochecker

1. [Connect to your VM](../appendix/vm.md#connect-to-the-vm).
2. [Create the `autochecker` user](../appendix/vm-autochecker.md#create-the-autochecker-user).
3. [Add the instructor's SSH public key to the `autochecker` user](../appendix/vm-autochecker.md#add-an-ssh-public-key-to-the-autochecker-user):

---

## 2. Optional steps

These enhancements can make your life easier:

- [(NEW)Learn to go back after clicking a link](#21-new-learn-to-go-back-after-clicking-a-link)
- [Set up a coding agent](#22-set-up-a-coding-agent)
- [Set up the shell prompt](#23-set-up-the-shell-prompt)
- [Customize the `Source Control`](#24-customize-the-source-control)
- [Get familiar with `GitLens`](#25-get-familiar-with-gitlens)
- [Create a label for tasks](#26-create-a-label-for-tasks)

### 2.1. (NEW) Learn to go back after clicking a link

> [!NOTE]

- `VS Code` - see the [shortcut](../appendix/vs-code.md#shortcut-go-back)
- Browsers:
  - `Firefox`: `Alt+ArrowLeft`
  - Other browsers: google

### 2.2. Set up a coding agent

A coding agent can help you write code, explain concepts, and debug issues.

See [Coding agents](../appendix/coding-agents.md).

<div style="display:flex;flex-wrap:wrap;gap:10px">
  <img alt="Qwen request" src="../images/tasks/setup/qwen-request.png" style="width:300px">
  <img alt="Qwen response" src="../images/tasks/setup/qwen-response.png" style="width:300px">
</div>

### 2.3. Set up the shell prompt

`Starship` shows your current `Git` branch, status, and other useful info directly in your [shell prompt](../appendix/shell.md#shell-prompt) in almost any terminal, including the [`VS Code Terminal`](../appendix/vs-code.md#vs-code-terminal).

Complete these steps:

1. [Install `Starship`](https://github.com/starship/starship#-installation).
2. [Open the `VS Code Terminal`](../appendix/vs-code.md#open-the-vs-code-terminal).

   You should see something similar to this:

   <img alt="Starship in the VS Code Terminal" src="../images/appendix/starship/terminal-prompt.png" style="width:400px"></img>

### 2.4. Customize the `Source Control`

1. [Open the `Source Control`](../appendix/vs-code.md#open-the-source-control).
2. Click three dots to the right of `SOURCE CONTROL`.
3. Put checkmarks only near `Changes` and `GitLens` to see only these views.

   <img alt="Changes and GitLens" src="../images/appendix/vs-code/source-control-allowed-views.png" style="width:400px"></img>

### 2.5. Get familiar with `GitLens`

[`GitLens`](../appendix/gitlens.md) helps you work with `Git` in `VS Code`.

Complete these steps:

1. [See all branches](../appendix/gitlens.md#see-all-branches)
2. [Look at the commit graph](../appendix/gitlens.md#look-at-the-commit-graph)
3. [Inspect the current branch](../appendix/gitlens.md#inspect-the-current-branch)
4. [Inspect the remotes](../appendix/gitlens.md#inspect-the-remotes)

### 2.6. Create a label for tasks

[Labels](../appendix/github.md#label) help you filter and organize issues.

With a `task` label, you can see in one view all issues created for lab tasks.

> [!TIP]
> If you create the `task` label before creating issues, your issues will have this label automatically as configured in the [issue form](../../.github/ISSUE_TEMPLATE/01-task.yml).

Complete these steps:

1. [Create](../appendix/github.md#create-a-label) the `task` label.
2. [Add the label to issues](../appendix/github.md#add-a-label-to-issues).
3. [See all issues with the label](../appendix/github.md#see-all-issues-with-a-label).

### 2.7. View `Markdown` files in `VS Code`

If you want to view [`README.md`](../../README.md) and other `Markdown` files in `VS Code` instead of on `GitHub`:

1. [Install recommended `VS Code` extensions](../appendix/vs-code.md#install-recommended-extensions).
2. [Open the file](../appendix/vs-code.md#open-the-file):
   [`README.md`](../../README.md).
3. [Open the `Markdown` preview](../appendix/vs-code.md#open-the-markdown-preview).
