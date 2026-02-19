# Lab setup

- [Steps](#steps)
  - [1. Find a partner](#1-find-a-partner)
  - [2. Start creating a VM](#2-start-creating-a-vm)
  - [3. Set up your fork](#3-set-up-your-fork)
    - [3.1. Sign in on `GitHub`](#31-sign-in-on-github)
    - [3.2. Fork the course instructors' repo](#32-fork-the-course-instructors-repo)
    - [3.3. Go to your fork](#33-go-to-your-fork)
    - [3.4. Enable issues](#34-enable-issues)
    - [3.5. Add a classmate as a collaborator](#35-add-a-classmate-as-a-collaborator)
    - [3.6. Protect your `main` branch](#36-protect-your-main-branch)
  - [4. Install programs](#4-install-programs)
    - [4.1. Install `VS Code`](#41-install-vs-code)
    - [4.2. Install `Git`](#42-install-git)
    - [4.3. Install `Docker`](#43-install-docker)
    - [4.4. (`Windows` only) Install `Ubuntu 24.04` using WSL](#44-windows-only-install-ubuntu-2404-using-wsl)
  - [5. Open in `VS Code` the `software-engineering-toolkit` directory](#5-open-in-vs-code-the-software-engineering-toolkit-directory)
  - [6. Set up `Git`](#6-set-up-git)
    - [6.1. Check your `Git` config](#61-check-your-git-config)
    - [6.2. Configure `Git`](#62-configure-git)
  - [7. Clone your fork and open it in `VS Code`](#7-clone-your-fork-and-open-it-in-vs-code)
    - [7.1. Copy your fork `URL`](#71-copy-your-fork-url)
    - [7.2. Clone your fork](#72-clone-your-fork)
    - [7.3. Open the cloned repo in `VS Code`](#73-open-the-cloned-repo-in-vs-code)
  - [8. (`Windows` only) Set the default shell](#8-windows-only-set-the-default-shell)
  - [9. Continue creating a VM](#9-continue-creating-a-vm)
  - [10. Set up `Python` in `VS Code`](#10-set-up-python-in-vs-code)
    - [10.1. Install `uv`](#101-install-uv)
    - [10.2. Install `Python` and dependencies](#102-install-python-and-dependencies)
    - [10.3. Select the `Python` interpreter](#103-select-the-python-interpreter)
    - [10.4. Check that `Python` works](#104-check-that-python-works)
  - [11. Set up the `Docker` environment](#11-set-up-the-docker-environment)
  - [12. Start the services](#12-start-the-services)
  - [13. Open `pgAdmin`](#13-open-pgadmin)
- [Optional steps](#optional-steps)
  - [1. Set up a coding agent](#1-set-up-a-coding-agent)
  - [2. Set up the shell prompt](#2-set-up-the-shell-prompt)
  - [3. Customize the `Source Control`](#3-customize-the-source-control)
  - [4. Get familiar with `GitLens`](#4-get-familiar-with-gitlens)
  - [5. Create a label for tasks](#5-create-a-label-for-tasks)
  - [6. View `README.md` in `VS Code`](#6-view-readmemd-in-vs-code)

## Steps

### 1. Find a partner

1. Find a partner for this lab.
2. Sit next to them.

> [!IMPORTANT]
> You work on tasks independently from your partner.
>
> You and your partner work together when reviewing each other's work.

### 2. Start creating a VM

[Create a subscription](./appendix/vm.md#create-a-subscription) to be able to create a VM.

### 3. Set up your fork

#### 3.1. Sign in on `GitHub`

1. Sign in on [`GitHub`](https://github.com/).
2. [Find `<your-github-username>`](./appendix/github.md#find-your-github-username).

#### 3.2. Fork the course instructors' repo

1. [Fork](./appendix/github.md#fork-a-repo) the course instructors' repo.

   The course instructors' repo [URL](./appendix/web-development.md#url) is <https://github.com/inno-se-toolkit/se-toolkit-lab-3>

#### 3.3. Go to your fork

1. [Go to your fork](./appendix/github.md#go-to-your-fork).

   The [URL](./appendix/web-development.md#url) of your fork should look like `https://github.com/<your-github-username>/se-toolkit-lab-3`.

#### 3.4. Enable issues

1. [Enable issues](./appendix/github.md#enable-issues).

#### 3.5. Add a classmate as a collaborator

1. [Add a collaborator](./appendix/github.md#add-a-collaborator) — your partner.
2. Your partner should add you as a collaborator in their repo.
3. It's OK if your collaborator can't change `Settings` in your repo.

#### 3.6. Protect your `main` branch

> [!NOTE]
> Branch protection prevents accidental pushes directly to `main`.
> This enforces the PR workflow and ensures all changes are reviewed.

1. [Protect a branch](./appendix/github.md#protect-a-branch).

### 4. Install programs

#### 4.1. Install `VS Code`

1. Install [`VS Code`](https://code.visualstudio.com/) if not installed.

2. (Optional) [Learn more](./appendix/vs-code.md) about `VS Code`.

#### 4.2. Install `Git`

1. [Install `Git`](https://git-scm.com/install/) if not installed.

2. (Optional) [Learn more](./appendix/git.md) about `Git`.

#### 4.3. Install `Docker`

1. [Install `Docker`](./appendix/docker.md#install-docker) if not installed.

2. (Optional) [Learn more](./appendix/docker.md) about `Docker`.

#### 4.4. (`Windows` only) Install `Ubuntu 24.04` using WSL

1. [Check the current shell in the `VS Code Terminal`](./appendix/vs-code.md#check-the-current-shell-in-the-vs-code-terminal).
2. [Set up running `VS Code` using `WSL`](./appendix/vs-code.md#windows-only-set-up-running-vs-code-in-wsl) if the shell is not `bash` or `zsh`.

### 5. Open in `VS Code` the `software-engineering-toolkit` directory

1. Inside the [`Desktop` directory](./appendix/file-system.md#desktop-directory),
   create the directory `software-engineering-toolkit`.

   Skip this step if this directory exists.

2. [Open in `VS Code` the directory](./appendix/git-vscode.md#open-in-vs-code-the-directory):
   `software-engineering-toolkit`.

### 6. Set up `Git`

#### 6.1. Check your `Git` config

1. [Check your Git config](./appendix/git.md#check-your-git-config).

#### 6.2. Configure `Git`

[Configure Git](./appendix/git.md#configure-git) if you want to change the values that you saw while [checking your `Git` config](#61-check-your-git-config).

### 7. Clone your fork and open it in `VS Code`

#### 7.1. Copy your fork `URL`

1. [Go to your fork](#33-go-to-your-fork).
2. Copy [`<your-fork-url>`](./appendix/github.md#your-fork-url).

   It should look like `https://github.com/<your-github-username>/se-toolkit-lab-3`.

> [!NOTE]
> Here, the `<repo-name>` is `se-toolkit-lab-3`.

#### 7.2. Clone your fork

1. [Clone your fork](./appendix/git-vscode.md#clone-the-repo):

   - Replace `<repo-url>` with [`<your-fork-url>`](./appendix/github.md#your-fork-url).
   - Replace `<repo-name>` with `se-toolkit-lab-3`.

#### 7.3. Open the cloned repo in `VS Code`

1. [Open in `VS Code` the directory](./appendix/git-vscode.md#open-in-vs-code-the-directory):
   `se-toolkit-lab-3`.
2. [Install recommended extensions](./appendix/vs-code.md#install-recommended-extensions).

### 8. (`Windows` only) Set the default shell

1. [Check the current shell in the `VS Code Terminal`](./appendix/vs-code.md#check-the-current-shell-in-the-vs-code-terminal).
2. [Set the default shell](./appendix/vs-code.md#windows-only-set-the-default-shell-for-the-vs-code-terminal) if the shell is not `bash` or `zsh`.

### 9. Continue creating a VM

1. [Set up `SSH`](./appendix/ssh.md#set-up-ssh).
2. [Create a VM using the subscription](./appendix/vm.md#create-a-vm-using-the-subscription).

### 10. Set up `Python` in `VS Code`

#### 10.1. Install `uv`

> [!NOTE]
> [`uv`](./appendix/python.md#uv) is a package manager for [`Python`](./appendix/python.md).

1. [Install `uv`](./appendix/python.md#install-uv).

#### 10.2. Install `Python` and dependencies

1. [Install `Python` and dependencies](./appendix/python.md#install-python-and-dependencies).

#### 10.3. Select the `Python` interpreter

1. [Select the `Python` interpreter](./appendix/python.md#select-the-python-interpreter).

#### 10.4. Check that `Python` works

1. [Check that `Python` works](./appendix/python.md#check-that-python-works).

### 11. Set up the `Docker` environment

1. [Run using the `VS Code Terminal`](./appendix/vs-code.md#run-a-command-using-the-vs-code-terminal):

   ```terminal
   cp .env.docker.example .env.docker.secret
   ```

> [!NOTE]
> The `.env.docker.secret` file contains environment variables for the `Docker` containers.
>
> It was added to [`.gitignore`](../.gitignore) because you may specify there
> [secrets](./appendix/environments.md#secrets) such as the API key or the address of your VM.

> [!TIP]
> No edits are needed for local development. The default values in [`.env.docker.example`](../.env.docker.example) work out of the box.

### 12. Start the services

1. [Run using the `VS Code Terminal`](./appendix/vs-code.md#run-a-command-using-the-vs-code-terminal):

   ```terminal
   docker compose --env-file .env.docker.secret up --build
   ```

2. Wait for the services to start. You should see log output from the `app`, `postgres`, `pgadmin`, and `caddy` containers.

   > [!TIP]
   > The database is initialized from [`src/app/data/init.sql`](../src/app/data/init.sql) only on the **first** start of the `PostgreSQL` container.
   > If you need to re-initialize the database (e.g., after pulling upstream changes to `init.sql`), see [Resetting the database](./appendix/database.md#resetting-the-database).

3. Open in a browser: <http://127.0.0.1:42001/docs>.

4. You should see the `Swagger UI` page with the API documentation.

   > [!NOTE]
   > [`Docker Compose`](./appendix/docker.md#docker-compose) reads environment variables from `.env.docker.secret`
   > and uses them to configure the containers defined in [`docker-compose.yml`](../docker-compose.yml).

   > [!TIP]
   > To stop the services, press `Ctrl+C` in the terminal where they are running.
   > Alternatively, run `docker compose down` in a new terminal.

### 13. Open `pgAdmin`

1. [Open `pgAdmin`](./appendix/pgadmin.md#open-pgadmin).
2. [Add a server in `pgAdmin`](./appendix/pgadmin.md#add-a-server-in-pgadmin).
3. [Browse tables](./appendix/pgadmin.md#browse-tables).
4. Verify that the following tables exist and contain data:
   - `items`
   - `learners`
   - `interaction_logs`

> [!TIP]
> To view the data in a table, right-click the table and select `View/Edit Data` -> `All Rows`.

---

## Optional steps

These enhancements can make your life easier:

- [1. Set up a coding agent](#1-set-up-a-coding-agent)
- [2. Set up the shell prompt](#2-set-up-the-shell-prompt)
- [3. Customize the `Source Control`](#3-customize-the-source-control)
- [4. Get familiar with `GitLens`](#4-get-familiar-with-gitlens)
- [5. Create a label for tasks](#5-create-a-label-for-tasks)

### 1. Set up a coding agent

A coding agent can help you write code, explain concepts, and debug issues.

See [Coding agents](./appendix/coding-agents.md).

### 2. Set up the shell prompt

`Starship` shows your current `Git` branch, status, and other useful info directly in your [shell prompt](https://en.wikibooks.org/wiki/Guide_to_Unix/Explanations/Shell_Prompt) in almost any terminal, including the [`VS Code Terminal`](./appendix/vs-code.md#terminal).

Complete these steps:

1. Install [`Starship`](https://github.com/starship/starship#-installation).
2. [Open the `VS Code Terminal`](./appendix/vs-code.md#open-the-vs-code-terminal).
3. You should see something similar to `se-toolkit-lab-3 on main`.

### 3. Customize the `Source Control`

1. [Open the `Source Control`](./appendix/vs-code.md#open-the-source-control).
2. Click three dots to the right of `SOURCE CONTROL`.
3. Put checkmarks only near `Changes` and `GitLens` to see only these views.

   <img alt="Changes and GitLens" src="./images/appendix/vs-code/source-control-allowed-views.png" style="width:400px"></img>

### 4. Get familiar with `GitLens`

[`GitLens`](./appendix/gitlens.md) helps you work with `Git` in `VS Code`.

Complete these steps:

1. [See all branches](./appendix/gitlens.md#see-all-branches)
2. [Look at the commit graph](./appendix/gitlens.md#look-at-the-commit-graph)
3. [Inspect the current branch](./appendix/gitlens.md#inspect-the-current-branch)
4. [Inspect the remotes](./appendix/gitlens.md#inspect-the-remotes)

### 5. Create a label for tasks

[Labels](./appendix/github.md#label) help you filter and organize issues.

With a `task` label, you can see in one view all issues created for lab tasks.

> [!TIP]
> If you create the `task` label before creating issues, your issues will have this label automatically as configured in the [issue form](../.github/ISSUE_TEMPLATE/01-task.yml).

Complete these steps:

1. [Create](./appendix/github.md#create-a-label) the `task` label.
2. [Add the label to issues](./appendix/github.md#add-a-label-to-issues).
3. [See all issues with the label](./appendix/github.md#see-all-issues-with-a-label).

### 6. View `README.md` in `VS Code`

If you want to view `README.md` in `VS Code` instead of on `GitHub`:

1. [Install recommended `VS Code` extensions](./appendix/vs-code.md#install-recommended-extensions).
2. [Open the file](./appendix/vs-code.md#open-the-file):
   [`README.md`](../README.md).
3. [Open the `Markdown` preview](./appendix/vs-code.md#open-the-markdown-preview).
