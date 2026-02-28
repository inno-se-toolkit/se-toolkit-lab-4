# Lab setup

- [1. Required steps](#1-required-steps)
  - [1.1. (UPD) Find a partner](#11-upd-find-a-partner)
  - [1.2. Start creating a VM](#12-start-creating-a-vm)
  - [1.3. Set up your fork](#13-set-up-your-fork)
    - [1.3.1. Sign in on `GitHub`](#131-sign-in-on-github)
    - [1.3.2. (UPD) Fork the course instructors' repo](#132-upd-fork-the-course-instructors-repo)
    - [1.3.3. (UPD) Go to your fork](#133-upd-go-to-your-fork)
    - [1.3.4. (UPD) Enable issues](#134-upd-enable-issues)
    - [1.3.5. (UPD) Add a classmate as a collaborator](#135-upd-add-a-classmate-as-a-collaborator)
    - [1.3.6. (UPD) Protect your `main` branch](#136-upd-protect-your-main-branch)
  - [1.4. Set up programs](#14-set-up-programs)
    - [1.4.1. Set up `VS Code`](#141-set-up-vs-code)
    - [1.4.2. (UPD) Set up `Docker`](#142-upd-set-up-docker)
    - [1.4.3. (UPD) (`Windows` only) Set the default shell for the `VS Code Terminal`](#143-upd-windows-only-set-the-default-shell-for-the-vs-code-terminal)
    - [1.4.4. Set up `Git`](#144-set-up-git)
  - [1.5. (UPD) Open in `VS Code` the `software-engineering-toolkit` directory](#15-upd-open-in-vs-code-the-software-engineering-toolkit-directory)
  - [1.6. (UPD) Clone your fork](#16-upd-clone-your-fork)
    - [1.6.1. (UPD) Copy your fork `URL`](#161-upd-copy-your-fork-url)
    - [1.6.2. (UPD) Clone your fork](#162-upd-clone-your-fork)
  - [1.7. (UPD) Open the cloned repo and set up `VS Code`](#17-upd-open-the-cloned-repo-and-set-up-vs-code)
  - [1.8. Continue creating a VM](#18-continue-creating-a-vm)
  - [1.9. Set up `Python`](#19-set-up-python)
    - [1.9.1. Install `uv`](#191-install-uv)
    - [1.9.2. (UPD) Set up `Python` in `VS Code`](#192-upd-set-up-python-in-vs-code)
  - [1.10. (NEW) Clean up `Docker`](#110-new-clean-up-docker)
  - [1.11. Start the services](#111-start-the-services)
    - [1.11.1. (UPD) Set up the `Docker` environment](#1111-upd-set-up-the-docker-environment)
    - [1.11.2. (UPD) Prepare `Docker`](#1112-upd-prepare-docker)
    - [1.11.3. (UPD) Start the services using `Docker Compose`](#1113-upd-start-the-services-using-docker-compose)
  - [1.12. (UPD) Open a new terminal](#112-upd-open-a-new-terminal)
  - [1.13. (UPD) Observe containers and services](#113-upd-observe-containers-and-services)
    - [1.13.1. (UPD) List running containers](#1131-upd-list-running-containers)
    - [1.13.2. (UPD) See logs of the running services](#1132-upd-see-logs-of-the-running-services)
  - [1.14. (UPD) Set up the services](#114-upd-set-up-the-services)
    - [1.14.1. (UPD) Open `Swagger UI`](#1141-upd-open-swagger-ui)
    - [1.14.2. (UPD) Set up `pgAdmin`](#1142-upd-set-up-pgadmin)
  - [1.15. (UPD) Stop the services](#115-upd-stop-the-services)
  - [1.16. (UPD) Add SSH key for the autochecker](#116-upd-add-ssh-key-for-the-autochecker)
  - [1.17. (UPD) Set up a coding agent](#117-upd-set-up-a-coding-agent)
  - [1.18. (UPD) Log in to the autochecker](#118-upd-log-in-to-the-autochecker)
- [2. Optional steps](#2-optional-steps)
  - [2.4. Set up a coding agent](#24-set-up-a-coding-agent)
  - [2.1. (NEW) Set up `Nix`](#21-new-set-up-nix)
  - [2.2. (NEW) Set up `direnv`](#22-new-set-up-direnv)
  - [2.3. (UPD) Learn to go back after clicking a link](#23-upd-learn-to-go-back-after-clicking-a-link)
  - [2.5. Set up the shell prompt](#25-set-up-the-shell-prompt)
  - [2.6. Customize the `Source Control`](#26-customize-the-source-control)
  - [2.7. Get familiar with `GitLens`](#27-get-familiar-with-gitlens)
  - [2.8. Create a label for tasks](#28-create-a-label-for-tasks)
  - [2.9. View `Markdown` files in `VS Code`](#29-view-markdown-files-in-vs-code)

## 1. Required steps

> [!IMPORTANT]
> Some steps have the `(UPD)` label.
>
> These steps must be completed to get the right setup for this lab,
> even if you have completed similar steps in the previous lab.

> [!IMPORTANT]
> Some steps have the `(NEW)` label.
>
> These steps were not present in previous setups.
> Pay extra attention to these steps to ensure that you have the right setup for this lab.

> [!NOTE]
> We provide all of the hardest steps in the lab setup
> so that TAs can help you get the right setup during the lab.
>
> Tasks are more or less easy when you have the right setup.

### 1.1. (UPD) Find a partner

1. Find a partner for this lab.
2. Sit next to them.

> [!IMPORTANT]
> You work on tasks independently from your partner.
>
> You and your partner work together when reviewing each other's work.

### 1.2. Start creating a VM

> [!NOTE]
> Skip this step if you can [connect to your VM](../../wiki/vm.md#connect-to-the-vm).

[Create a subscription](../../wiki/vm.md#create-a-subscription) to be able to create a VM.

### 1.3. Set up your fork

#### 1.3.1. Sign in on `GitHub`

1. Sign in on [`GitHub`](https://github.com/).
2. [Find `<your-github-username>`](../../wiki/github.md#find-your-github-username).

#### 1.3.2. (UPD) Fork the course instructors' repo

1. [Fork the course instructors' repo](../../wiki/github.md#fork-a-repo).

   The course instructors' repo [URL](../../wiki/web-development.md#url) is <https://github.com/inno-se-toolkit/se-toolkit-lab-4>

#### 1.3.3. (UPD) Go to your fork

1. [Go to your fork](../../wiki/github.md#go-to-your-fork).

   The [URL](../../wiki/web-development.md#url) of your fork should look like `https://github.com/<your-github-username>/se-toolkit-lab-4`.

#### 1.3.4. (UPD) Enable issues

1. [Enable issues](../../wiki/github.md#enable-issues).

#### 1.3.5. (UPD) Add a classmate as a collaborator

1. [Add a collaborator](../../wiki/github.md#add-a-collaborator) — your partner.
2. Your partner should add you as a collaborator in their repo.
3. It's OK if your collaborator can't change `Settings` in your repo.

#### 1.3.6. (UPD) Protect your `main` branch

> [!NOTE]
> Branch protection prevents accidental pushes directly to `main`.
> This enforces the PR workflow and ensures all changes are reviewed.

1. [Protect a branch](../../wiki/github.md#protect-a-branch).

### 1.4. Set up programs

#### 1.4.1. Set up `VS Code`

1. (Optional) [Read about `VS Code`](../../wiki/vs-code.md#what-is-vs-code).
2. [Set up `VS Code`](../../wiki/vs-code.md#set-up-vs-code).

#### 1.4.2. (UPD) Set up `Docker`

1. (Optional) [Read about `Docker`](../../wiki/docker.md#what-is-docker).
2. [Install `Docker`](../../wiki/docker.md#install-docker) if it's not installed.
3. [Start `Docker`](../../wiki/docker.md#start-docker).

#### 1.4.3. (UPD) (`Windows` only) Set the default shell for the `VS Code Terminal`

1. [Check the current shell in the `VS Code Terminal`](../../wiki/vs-code.md#check-the-current-shell-in-the-vs-code-terminal).
2. If it's not `bash` or `zsh`, [set the default shell](../../wiki/vs-code.md#windows-only-set-the-default-shell-for-the-vs-code-terminal) and check again.

#### 1.4.4. Set up `Git`

1. (Optional) [Read about `Git`](../../wiki/git.md#what-is-git).
2. [Install `Git`](https://git-scm.com/install/) if it's not installed.
3. (Optional) [Configure `Git`](../../wiki/git.md#configure-git).

### 1.5. (UPD) Open in `VS Code` the `software-engineering-toolkit` directory

1. Inside the [`Desktop` directory](../../wiki/file-system.md#desktop-directory),
   create the directory `software-engineering-toolkit`.

   Skip this step if this directory exists.

2. [Open in `VS Code` the directory](../../wiki/vs-code.md#open-the-directory):
   `software-engineering-toolkit`.

### 1.6. (UPD) Clone your fork

#### 1.6.1. (UPD) Copy your fork `URL`

1. [Go to your fork](#133-upd-go-to-your-fork).
2. Copy [`<your-fork-url>`](../../wiki/github.md#your-fork-url).

   It should look like `https://github.com/<your-github-username>/se-toolkit-lab-4`.

   See [`<your-github-username>`](../../wiki/github.md#your-github-username).

#### 1.6.2. (UPD) Clone your fork

1. [Clone your fork](../../wiki/git-vscode.md#clone-the-repository):

   - Replace `<repo-url>` with [`<your-fork-url>`](../../wiki/github.md#your-fork-url).
   - Replace `<repo-name>` with `se-toolkit-lab-4`.

### 1.7. (UPD) Open the cloned repo and set up `VS Code`

> [!IMPORTANT]
> Go by the links in the steps below and complete the checks ("You should see ...").
> Otherwise, your setup will be broken.

1. [Open in `VS Code` the directory](../../wiki/vs-code.md#open-the-directory):
   `se-toolkit-lab-4`.
2. [Check the current shell in the `VS Code Terminal`](../../wiki/vs-code.md#check-the-current-shell-in-the-vs-code-terminal).
3. [Install recommended extensions](../../wiki/vs-code.md#install-recommended-extensions).
4. Ask the TA if something doesn't work.

### 1.8. Continue creating a VM

> [!NOTE]
> Don't overwrite the key if it already exists.
> You can use the key that you created before for the new VM.

Complete these steps if you can't [connect to your VM](../../wiki/vm.md#connect-to-the-vm):

1. [Set up `SSH`](../../wiki/ssh.md#set-up-ssh).
2. [Create a VM using the subscription](../../wiki/vm.md#create-a-vm-using-the-subscription).

### 1.9. Set up `Python`

> [!NOTE]
> See [What is `Python`](../../wiki/python.md#what-is-python).

#### 1.9.1. Install `uv`

> [!NOTE]
> See [`uv`](../../wiki/python.md#uv).

1. [Install `uv`](../../wiki/python.md#install-uv).

#### 1.9.2. (UPD) Set up `Python` in `VS Code`

> [!NOTE]
> The dependencies have been updated in this project version.

1. [Set up `Python` in `VS Code`](../../wiki/python.md#set-up-python-in-vs-code).

### 1.10. (NEW) Clean up `Docker`

> [!NOTE]
> Old containers and volumes from a previous lab version may conflict with the updated services.
> Stop running containers, remove stopped containers, and delete unused volumes so you start with a clean state.

1. [Clean up `Docker`](../../wiki/docker.md#clean-up-docker).

### 1.11. Start the services

> [!NOTE]
> See [service](../../wiki/docker.md#service).

#### 1.11.1. (UPD) Set up the `Docker` environment

1. Copy the [`.env.docker.example`](../../.env.docker.example) file to the `.env.docker.secret` file:

   [Run using the `VS Code Terminal`](../../wiki/vs-code.md#run-a-command-using-the-vs-code-terminal):

   ```terminal
   cp .env.docker.example .env.docker.secret
   ```

> [!NOTE]
> The `.env.docker.secret` file contains environment variables for the `Docker` containers.
>
> It was added to [`.gitignore`](../../.gitignore) because you may specify there
> [secrets](../../wiki/environments.md#secrets) such as the API key or the [address of your VM](../../wiki/vm.md#your-vm-ip-address).

> [!TIP]
> No edits are needed for local development.
> The default values in [`.env.docker.example`](../../.env.docker.example) work out of the box.

#### 1.11.2. (UPD) Prepare `Docker`

1. [Start `Docker`](../../wiki/docker.md#start-docker).
2. [Clean up `Docker`](../../wiki/docker.md#clean-up-docker).

#### 1.11.3. (UPD) Start the services using `Docker Compose`

1. Start services using the [`docker compose up` command](../../wiki/docker-compose.md#docker-compose-up):

   [Run using the `VS Code Terminal`](../../wiki/vs-code.md#run-a-command-using-the-vs-code-terminal):

   ```terminal
   docker compose --env-file .env.docker.secret up --build
   ```

   > **NOTE**
   >
   > [`Docker Compose`](../../wiki/docker-compose.md) reads environment variables from `.env.docker.secret`
   > and uses them to configure the containers defined in [`docker-compose.yml`](../../docker-compose.yml).

2. Wait for the services to start. You should see log output from the `app`, `postgres`, `pgadmin`, and `caddy` containers.

   > **NOTE**
   >
   > The database is initialized from [`backend/app/data/init.sql`](../../backend/app/data/init.sql) only on the **first** start of the `PostgreSQL` container.
   >
   > If you need to re-initialize the database (e.g., after pulling upstream changes to `init.sql`), see [Resetting the database](../../wiki/docker-postgres.md#resetting-the-database).

### 1.12. (UPD) Open a new terminal

1. [Open a new `VS Code Terminal`](../../wiki/vs-code.md#open-a-new-vs-code-terminal).

### 1.13. (UPD) Observe containers and services

#### 1.13.1. (UPD) List running containers

1. [Run using the `VS Code Terminal`](../../wiki/vs-code.md#run-a-command-using-the-vs-code-terminal):

   ```terminal
   docker compose --env-file .env.docker.secret ps
   ```

#### 1.13.2. (UPD) See logs of the running services

1. See logs for all services:

   [Run using the `VS Code Terminal`](../../wiki/vs-code.md#run-a-command-using-the-vs-code-terminal):

   ```terminal
   docker compose --env-file .env.docker.secret logs
   ```

2. [See logs for a specific service](../../wiki/docker-compose.md#docker-compose-logs-for-a-specific-service):

   ```terminal
   docker compose --env-file .env.docker.secret logs postgres
   ```

### 1.14. (UPD) Set up the services

#### 1.14.1. (UPD) Open `Swagger UI`

1. Open in a browser: <http://127.0.0.1:42001/docs>.

   You should see the [`Swagger UI`](../../wiki/swagger.md#swagger-ui) page with the [API](../../wiki/web-development.md#api) documentation.

#### 1.14.2. (UPD) Set up `pgAdmin`

> [!NOTE]
> [`pgAdmin`](../../wiki/pgadmin.md#what-is-pgadmin) takes 2-3 minutes to start after you have started the services.

1. [Open `pgAdmin`](../../wiki/pgadmin.md#open-pgadmin).
2. [Add a server in `pgAdmin`](../../wiki/pgadmin.md#add-a-server-in-pgadmin).
3. [Browse the `interacts` table](../../wiki/pgadmin.md#browse-tables)

   You should see rows of data stored in the database.

   <img alt="Interaction logs" src="../images/tasks/setup/database-interaction-logs.png" style="width:400px">

   These are records of what `learners` did with `items` (courses, labs, tasks, steps).
   They `attempt`ed, `complete`d or just `view`ed them.

4. Verify that the following tables exist and contain data:
   - `items`
   - `learners`
   - `interacts`

> [!TIP]
> To view the data in a table, right-click the table and select `View/Edit Data` -> `All Rows`.

### 1.15. (UPD) Stop the services

1. [Check that the current directory is `se-toolkit-lab-4`](../../wiki/shell.md#check-the-current-directory-is-directory-name).
2. [Run using the `VS Code Terminal`](../../wiki/vs-code.md#run-a-command-using-the-vs-code-terminal):

   ```terminal
   docker compose --env-file .env.docker.secret down
   ```

### 1.16. (UPD) Add SSH key for the autochecker

1. [Connect to your VM](../../wiki/vm.md#connect-to-the-vm).
2. [Create the `autochecker` user](../../wiki/vm-autochecker.md#create-the-autochecker-user).
3. [Add the instructor's SSH public key to the `autochecker` user](../../wiki/vm-autochecker.md#add-an-ssh-public-key-to-the-autochecker-user):

### 1.17. (UPD) Set up a coding agent

Follow the [`Coding agents`](../../wiki/coding-agents.md) guide to set up a coding agent on your machine.

### 1.18. (UPD) Log in to the autochecker

1. Open the autochecker in Telegram: <https://t.me/auchebot>
2. Log in.

Use the autochecker to check the task completion.

---

## 2. Optional steps

These enhancements can make your life easier:

- [Set up a coding agent](#24-set-up-a-coding-agent)
- [Set up `Nix`](#21-new-set-up-nix)
- [Set up `direnv`](#22-new-set-up-direnv)
- [Learn to go back after clicking a link](#23-upd-learn-to-go-back-after-clicking-a-link)
- [Set up the shell prompt](#25-set-up-the-shell-prompt)
- [Customize the `Source Control`](#26-customize-the-source-control)
- [Get familiar with `GitLens`](#27-get-familiar-with-gitlens)
- [Create a label for tasks](#28-create-a-label-for-tasks)

### 2.4. Set up a coding agent

A coding agent can help you write code, explain concepts, and debug issues.

See [Coding agents](../../wiki/coding-agents.md).

<div style="display:flex;flex-wrap:wrap;gap:10px">
  <img alt="Qwen request" src="../images/tasks/setup/qwen-request.png" style="width:300px">
  <img alt="Qwen response" src="../images/tasks/setup/qwen-response.png" style="width:300px">
</div>

### 2.1. (NEW) Set up `Nix`

1. (Optional) [Read about `Nix`](../../wiki/nix.md#what-is-nix).
2. [Set up `Nix`](../../wiki/nix.md#set-up-nix).

### 2.2. (NEW) Set up `direnv`

1. [Set up `Nix`](#21-new-set-up-nix).
2. [Set up `direnv`](../../wiki/direnv.md#set-up-direnv).

### 2.3. (UPD) Learn to go back after clicking a link

> [!NOTE]

- `VS Code` - see the [shortcut](../../wiki/vs-code.md#shortcut-go-back)
- Browsers:
  - `Firefox`: `Alt+ArrowLeft`
  - Other browsers: google

### 2.5. Set up the shell prompt

`Starship` shows your current `Git` branch, status, and other useful info directly in your [shell prompt](../../wiki/shell.md#shell-prompt) in almost any terminal, including the [`VS Code Terminal`](../../wiki/vs-code.md#vs-code-terminal).

Complete these steps:

1. [Install `Starship`](https://github.com/starship/starship#-installation).
2. [Open the `VS Code Terminal`](../../wiki/vs-code.md#open-the-vs-code-terminal).

   You should see something similar to this:

   <img alt="Starship in the VS Code Terminal" src="../../wiki/images/starship/terminal-prompt.png" style="width:400px"></img>

### 2.6. Customize the `Source Control`

1. [Open the `Source Control`](../../wiki/vs-code.md#open-the-source-control).
2. Click three dots to the right of `SOURCE CONTROL`.
3. Put checkmarks only near `Changes` and `GitLens` to see only these views.

   <img alt="Changes and GitLens" src="../../wiki/images/vs-code/source-control-allowed-views.png" style="width:400px"></img>

### 2.7. Get familiar with `GitLens`

[`GitLens`](../../wiki/gitlens.md) helps you work with `Git` in `VS Code`.

Complete these steps:

1. [See all branches](../../wiki/gitlens.md#see-all-branches)
2. [Look at the commit graph](../../wiki/gitlens.md#look-at-the-commit-graph)
3. [Inspect the current branch](../../wiki/gitlens.md#inspect-the-current-branch)
4. [Inspect the remotes](../../wiki/gitlens.md#inspect-the-remotes)

### 2.8. Create a label for tasks

[Labels](../../wiki/github.md#label) help you filter and organize issues.

With a `task` label, you can see in one view all issues created for lab tasks.

> [!TIP]
> If you create the `task` label before creating issues, your issues will have this label automatically as configured in the [issue form](../../.github/ISSUE_TEMPLATE/01-task.yml).

Complete these steps:

1. [Create](../../wiki/github.md#create-a-label) the `task` label.
2. [Add the label to issues](../../wiki/github.md#add-a-label-to-issues).
3. [See all issues with the label](../../wiki/github.md#see-all-issues-with-a-label).

### 2.9. View `Markdown` files in `VS Code`

If you want to view [`README.md`](../../README.md) and other `Markdown` files in `VS Code` instead of on `GitHub`:

1. [Install recommended `VS Code` extensions](../../wiki/vs-code.md#install-recommended-extensions).
2. [Open the file](../../wiki/vs-code.md#open-the-file):
   [`README.md`](../../README.md).
3. [Open the `Markdown` preview](../../wiki/vs-code.md#open-the-markdown-preview).
