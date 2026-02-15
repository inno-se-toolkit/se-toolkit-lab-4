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
    - [4.3. (Optional, `Windows` only) Install `Ubuntu 24.04` using WSL](#43-optional-windows-only-install-ubuntu-2404-using-wsl)
  - [5. Open in `VS Code` the `software-engineering-toolkit` directory](#5-open-in-vs-code-the-software-engineering-toolkit-directory)
  - [6. Set up `Git`](#6-set-up-git)
    - [6.1 Check your `Git` config](#61-check-your-git-config)
    - [6.2 Configure `Git`](#62-configure-git)
  - [6. Open your cloned fork in `VS Code`](#6-open-your-cloned-fork-in-vs-code)
    - [6.1. Copy your fork `URL`](#61-copy-your-fork-url)
    - [6.2. Clone your fork](#62-clone-your-fork)
    - [6.3. Open the cloned repo in `VS Code`](#63-open-the-cloned-repo-in-vs-code)
  - [7. (`Windows` only) Set the default shell](#7-windows-only-set-the-default-shell)
  - [8. Continue creating a VM](#8-continue-creating-a-vm)
  - [9. Set up `Python` in `VS Code`](#9-set-up-python-in-vs-code)
    - [4.3. Install `uv`](#43-install-uv)
    - [9.1. Install `Python` and dependencies](#91-install-python-and-dependencies)
    - [9.2. Select the `Python` interpreter](#92-select-the-python-interpreter)
    - [9.3. Check that `Python` works](#93-check-that-python-works)
- [Optional steps](#optional-steps)
  - [1. Set up a coding agent](#1-set-up-a-coding-agent)
  - [2. Set up the shell prompt](#2-set-up-the-shell-prompt)
  - [3. Customize the `Source Control`](#3-customize-the-source-control)
  - [4. Get familiar with `GitLens`](#4-get-familiar-with-gitlens)
  - [5. Create a label for tasks](#5-create-a-label-for-tasks)
    - [Create the `task` label](#create-the-task-label)
    - [Add the label to issues](#add-the-label-to-issues)
    - [See all issues with the label](#see-all-issues-with-the-label)
  - [7. View `README.md` in `VS Code`](#7-view-readmemd-in-vs-code)

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
2. [Find `<your-username>`](./appendix/github.md#find-your-username).

#### 3.2. Fork the course instructors' repo

1. [Fork](./appendix/github.md#fork-a-repo) the course instructors' repo.

   The course instructors' repo [URL](./appendix/web-development.md#url) is <https://github.com/inno-se-toolkit/se-toolkit-lab-2>

#### 3.3. Go to your fork

1. [Go to your fork](./appendix/github.md#go-to-your-fork).

   The [URL](./appendix/web-development.md#url) of your fork should look like `https://github.com/<your-username>/se-toolkit-lab-2`.

#### 3.4. Enable issues

1. Go to `Settings` -> `General` -> `Features`.
2. Check the box near `Issues`.

#### 3.5. Add a classmate as a collaborator

1. Go to `Settings` -> `Collaborators` -> `Add people`.
2. Add your partner as a collaborator.
3. Your partner should add you as a collaborator in their repo.
4. Make sure your collaborator has accepted the invitation sent to their email.
5. It's OK if your collaborator can't change `Settings` in your repo.

#### 3.6. Protect your `main` branch

> [!NOTE]
> Branch protection prevents accidental pushes directly to `main`.
> This enforces the PR workflow and ensures all changes are reviewed.

Complete these steps:

1. [Go to your fork](#33-go-to-your-fork).
2. Go to `Settings`.
3. Go to `Code and automation`.
4. Go to `Rules`.
5. Go to `Rulesets`.
6. Go to `New ruleset`.
7. Go to `Add branch ruleset`.
8. Set:

   1. `Ruleset Name`: `push`
   2. `Enforcement status`: `Active`
   3. `Target branches` -> `Add target` -> `Include default branch`
   4. Rules:
      - [x] `Restrict deletions`
      - [x] `Require a pull request before merging`:
         - `Required approvals`: `1`
         - `Require conversation resolution before merging`
         - `Allowed merge methods`: `Merge`.
      - [x] Block force pushes

### 4. Install programs

#### 4.1. Install `VS Code`

1. Install [`VS Code`](https://code.visualstudio.com/) if not installed.

2. (Optional) [Learn more](../lab/appendix/vs-code.md) about `VS Code`.

#### 4.2. Install `Git`

1. [Install `Git`](https://git-scm.com/install/) if not installed.

2. (Optional) [Learn more](../lab/appendix/git.md) about `Git`.

#### 4.3. (Optional, `Windows` only) Install `Ubuntu 24.04` using WSL

1. [Set up running `VS Code` using `WSL`](./appendix/vs-code.md#windows-only-set-up-running-vs-code-in-wsl).

### 5. Open in `VS Code` the `software-engineering-toolkit` directory

1. Inside the `Desktop` [directory](./appendix/file-system.md#directory),
   create the directory `software-engineering-toolkit`.

   Skip this step if this directory exists.

2. [Open in `VS Code` the directory](./appendix/git-vscode.md#open-in-vs-code-the-directory):
   `software-engineering-toolkit`.

3. [Check the current shell in the `VS Code Terminal`](./appendix/vs-code.md#check-the-current-shell-in-the-vs-code-terminal).

### 6. Set up `Git`

#### 6.1 Check your `Git` config

1. [Run using the `VS Code Terminal`](./appendix/vs-code.md#run-a-command-using-the-vs-code-terminal):

   ```terminal
   git config --global --list
   ```

   The output should look like this (but with your values):

   ```terminal
   user.name=John Doe
   user.email=johndoe@gmail.com
   ```

#### 6.2 Configure `Git`

Configure `Git` if you want to change the values that you saw while [checking your `Git` config](#61-check-your-git-config).

> [!IMPORTANT]
> Replace `<your-name>` with a name and `<your-email>` with an email that you want to see in the commits.

1. (Optional) See [docs](https://git-scm.com/docs/git-config#Documentation/git-config.txt-username) for an explanation of what these commands do.
2. [Run using the `VS Code Terminal`](./appendix/vs-code.md#run-a-command-using-the-vs-code-terminal):

    ```terminal
    git config --global user.name '<your-name>'
    ```

    Example: `git config --global user.name 'John Doe'`

3. [Run using the `VS Code Terminal`](./appendix/vs-code.md#run-a-command-using-the-vs-code-terminal):

     ```terminal
     git config --global user.email '<your-email>'
     ```

     Example: `git config --global user.name 'johndoe@gmail.com'`

### 6. Open your cloned fork in `VS Code`

#### 6.1. Copy your fork `URL`

1. [Go to your fork](#33-go-to-your-fork).
2. Copy [`<your-fork-url>`](./appendix/github.md#your-fork-url).

   It should look like `https://github.com/<your-username>/se-toolkit-lab-2`.

> [!NOTE]
> Here, the `<repo-name>` is `se-toolkit-lab-2`.

#### 6.2. Clone your fork

1. [Clone your fork](./appendix/git-vscode.md#clone-the-repo):

   - Replace `<repo-url>` with [`<your-fork-url>`](./appendix/github.md#your-fork-url).
   - Replace `<repo-name>` with `se-toolkit-lab-2`.

#### 6.3. Open the cloned repo in `VS Code`

1. [Open in `VS Code` the directory](./appendix/git-vscode.md#open-in-vs-code-the-directory):
   `se-toolkit-lab-2`.
2. [Install recommended extensions](./appendix/vs-code.md#install-recommended-extensions).
3. Close the `VS Code` where you [opened the `software-engineering-toolkit` directory](#5-open-vs-code-in-the-software-engineering-toolkit-directory).

### 7. (`Windows` only) Set the default shell

1. [Set the default shell](./appendix/vs-code.md#windows-only-set-the-default-shell-for-the-vs-code-terminal).

### 8. Continue creating a VM

1. [Set up `SSH`](./appendix/ssh.md#set-up-ssh).
2. [Create a VM using the subscription](./appendix/vm.md#create-a-vm-using-the-subscription).

### 9. Set up `Python` in `VS Code`

#### 4.3. Install `uv`

> [!NOTE]
> [`uv`](./appendix/python.md#uv) is a package manager for [`Python`](./appendix/python.md).

> ![IMPORTANT]

1. Follow the [installation instructions](https://docs.astral.sh/uv/getting-started/installation/).

   If you use `Windows`, follow the instructions for `Linux`.

#### 9.1. Install `Python` and dependencies

1. [Run using the `VS Code Terminal`](./appendix/vs-code.md#run-a-command-using-the-vs-code-terminal):

   ```terminal
   uv sync
   ```

   This command automatically downloads the correct `Python` version, creates the `.venv` virtual environment, and installs all dependencies.

2. The output should be similar to this:

   ```terminal
   Using CPython 3.14.2
   Creating virtual environment at: .venv
   Resolved 36 packages in 0.77ms
   Installed 36 packages in 217ms
   ```

> [!NOTE]
> The `.venv` directory contains the virtual environment.
> That is, files and dependencies that are necessary to run the web server and other tools.
>
> This directory is managed by `uv`. You don't need to edit files in this directory manually.

#### 9.2. Select the `Python` interpreter

1. [Run using the `Command Palette`](./appendix/vs-code.md#run-a-command-using-the-command-palette):
   `Python: Select Interpreter`.
2. Click `Recommended` to select the interpreter in `./.venv/bin/python`.

#### 9.3. Check that `Python` works

1. [Open a new `VS Code Terminal`](./appendix/vs-code.md#open-a-new-terminal).
2. [Run using the `VS Code Terminal`](./appendix/vs-code.md#run-a-command-using-the-vs-code-terminal):

   ```terminal
   uv run python --version
   ```

3. The output should be similar to this:

   ```terminal
   Python 3.14.2
   ```

> [!NOTE]
> The `Python` version for this project is specified in the [`pyproject.toml`](../pyproject.toml) file using the `requires-python` setting.

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
3. You should see something similar to `se-toolkit-lab-2 on main`.

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

[Labels](https://docs.github.com/en/issues/using-labels-and-milestones-to-track-work/managing-labels) help you filter and organize issues.

With a `task` label, you can see in one view all issues created for lab tasks.

> [!TIP]
> If you create the `task` label before creating issues, your issues will have this label automatically as configured in the [issue form](../.github/ISSUE_TEMPLATE/01-task.yml).

Complete these steps:

1. [Create the `task` label](#create-the-task-label)
2. [Add the label to issues](#add-the-label-to-issues)
3. [See all issues with the label](#see-all-issues-with-the-label)

#### Create the `task` label

1. [Go to your fork](#33-go-to-your-fork).
2. Go to `Issues` -> `Labels`.
3. Create a new label:
   1. Click `New label`.
   2. Name: `task`.
   3. Click `Create label`.

#### Add the label to issues

1. [Go to your fork](#33-go-to-your-fork).
2. [Add](https://github.com/orgs/community/discussions/53473#discussioncomment-5697478) the `task` label to some of your issues.

#### See all issues with the label

1. [Go to your fork](#33-go-to-your-fork).
2. Go to `Issues`.
3. If you don't see any `Open` issues, click `Closed`.
4. Filter issues by the label:
   1. Click `Labels`.
   2. In the `Filter labels` input area, write `task`.
   3. Click the suggested label.
5. You should see all issues that have the `task` label.

### 7. View `README.md` in `VS Code`

If you want to view `README.md` in `VS Code` instead of on `GitHub`:

1. [Install recommended `VS Code` extensions](./appendix/vs-code.md#install-recommended-extensions).
2. Sign in to accounts.
    1. Go to the [`Activity Bar`](./appendix/vs-code.md#activity-bar).
    2. Click the icon `Accounts`.
    3. Click `Sign in with GitHub ...`.
    4. Repeat for the remaining extensions if there are any.
3. [Run using the `Command Palette`](./appendix/vs-code.md#run-a-command-using-the-command-palette):
   `Developer: Reload Window`.
4. Look at the [`Basic Layout`](./appendix/vs-code.md#basic-layout).
5. [Open the file](./appendix/vs-code.md#open-the-file):
   `README.md`.
6. [Open the `Markdown` preview](./appendix/vs-code.md#open-the-markdown-preview).
