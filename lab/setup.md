# Lab setup

- [Steps](#steps)
  - [1. Find a partner](#1-find-a-partner)
  - [2. Start creating a VM](#2-start-creating-a-vm)
  - [3. Sign in on `GitHub`](#3-sign-in-on-github)
  - [4. Fork the course instructors' repo](#4-fork-the-course-instructors-repo)
  - [5. Go to your fork](#5-go-to-your-fork)
  - [6. Make your fork public](#6-make-your-fork-public)
  - [7. Enable issues](#7-enable-issues)
  - [8. Add a classmate as a collaborator](#8-add-a-classmate-as-a-collaborator)
  - [9. Protect your `main` branch](#9-protect-your-main-branch)
  - [10. Install `Git`](#10-install-git)
  - [11. Install `VS Code`](#11-install-vs-code)
  - [12. (Optional, `Windows` only) Install WSL](#12-optional-windows-only-install-wsl)
  - [13. Open `VS Code` in the `software-engineering-toolkit` directory](#13-open-vs-code-in-the-software-engineering-toolkit-directory)
  - [14. (Windows only) Set the default shell](#14-windows-only-set-the-default-shell)
  - [15. Install `uv`](#15-install-uv)
  - [15. Configure `Git`](#15-configure-git)
  - [16. Copy your fork URL](#16-copy-your-fork-url)
  - [17. Clone the fork on your computer](#17-clone-the-fork-on-your-computer)
    - [Clone the fork using the `VS Code Terminal`](#clone-the-fork-using-the-vs-code-terminal)
    - [Clone the fork using the `Command Palette`](#clone-the-fork-using-the-command-palette)
  - [18. Open `VS Code` in the cloned repo directory](#18-open-vs-code-in-the-cloned-repo-directory)
  - [19. Continue creating a VM](#19-continue-creating-a-vm)
  - [20. Install `Python` and dependencies](#20-install-python-and-dependencies)
  - [21. Select the `Python` interpreter](#21-select-the-python-interpreter)
  - [22. Check that `Python` works](#22-check-that-python-works)
- [Optional steps](#optional-steps)
  - [1. Change the workspace settings](#1-change-the-workspace-settings)
  - [2. Set up a coding agent](#2-set-up-a-coding-agent)
  - [3. Set up the shell prompt](#3-set-up-the-shell-prompt)
  - [4. Customize the `Source Control`](#4-customize-the-source-control)
  - [5. Get familiar with `GitLens`](#5-get-familiar-with-gitlens)
  - [6. Create a label for tasks](#6-create-a-label-for-tasks)
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

### 3. Sign in on `GitHub`

1. Sign in on [`GitHub`](https://github.com/).
2. [Find `<your-username>`](./appendix/github.md#find-your-username).

### 4. Fork the course instructors' repo

1. [Fork](./appendix/github.md#fork-a-repo) the course instructors' repo.

   The course instructors' repo [URL](./appendix/web-development.md#url) is <https://github.com/inno-se-toolkit/se-toolkit-lab-2>

### 5. Go to your fork

1. [Go to your fork](./appendix/github.md#go-to-your-fork).

   The [URL](./appendix/web-development.md#url) of your fork should look like `https://github.com/<your-username>/se-toolkit-lab-2`.

### 6. Make your fork public

1. If you don't see `Public` near your fork name, [make your fork public](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/managing-repository-settings/setting-repository-visibility#changing-a-repositorys-visibility).

### 7. Enable issues

1. Go to `Settings` -> `General` -> `Features`.
2. Check the box near `Issues`.

### 8. Add a classmate as a collaborator

1. Go to `Settings` -> `Collaborators` -> `Add people`.
2. Add your partner as a collaborator.
3. Your partner should add you as a collaborator in their repo.
4. Make sure your collaborator has accepted the invitation sent to their email.
5. It's OK if your collaborator can't change `Settings` in your repo.

### 9. Protect your `main` branch

> [!NOTE]
> Branch protection prevents accidental pushes directly to `main`.
> This enforces the PR workflow and ensures all changes are reviewed.

Complete these steps:

1. [Go to your fork](#5-go-to-your-fork).
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

### 10. Install `Git`

[Install `Git`](https://git-scm.com/install/).

### 11. Install `VS Code`

1. Install [`VS Code`](https://code.visualstudio.com/).

   We chose this editor because it has built-in AI features and many useful [extensions](./appendix/vs-code.md#extensions).

2. (Optional) [Learn more](../lab/appendix/vs-code.md) about `VS Code`.

### 12. (Optional, `Windows` only) Install WSL

[Install WSL](https://learn.microsoft.com/en-us/windows/wsl/install).

### 13. Open `VS Code` in the `software-engineering-toolkit` directory

1. On your computer, create somewhere a directory `software-engineering-toolkit` (e.g., on your `Desktop`).
2. [Run using the `Command Palette`](./appendix/vs-code.md#command-palette):
   `File: Open Folder...`
3. Find the `software-engineering-toolkit` directory that you created.
4. Open this directory.
5. `VS Code` should now open in that directory.
6. [Open `Folders`](./appendix/vs-code.md#open-folders).
7. Look at `FOLDERS`.
8. You should see `SOFTWARE-ENGINEERING-TOOLKIT` there.

### 14. (Windows only) Set the default shell

1. [Run using the `Command Palette`](./appendix/vs-code.md#command-palette):
   `Terminal: Select Default Profile`
2. Select `WSL Bash` if available.
3. Otherwise, select `Git Bash` if available.
4. If none of them are available, ask the TA to help you.
5. Otherwise, [open the `VS Code Terminal`](./appendix/vs-code.md#open-the-vs-code-terminal).
6. You should see `bash` there:

   <img alt="Terminal Bash" src="./images/appendix/vs-code/terminal-bash.png" style="width:400px"></img>

<!-- TODO check how it looks like on windows -->

### 15. Install `uv`

Follow the [installation instructions](https://docs.astral.sh/uv/getting-started/installation/) for your platform (`Windows`, `Linux`, `macOS`).

[Run the command using the `VS Code Terminal`](./appendix/vs-code.md#run-a-command-using-the-vs-code-terminal).

### 15. Configure `Git`

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

### 16. Copy your fork URL

1. [Go to your fork](#5-go-to-your-fork).
2. Copy [`<your-fork-url>`](./appendix/github.md#your-fork-url).
3. It should look like `https://github.com/<your-username>/se-toolkit-lab-2`.

### 17. Clone the fork on your computer

Clone the fork using any of the following methods:

- [Clone the fork using the `VS Code Terminal`](#clone-the-fork-using-the-vs-code-terminal)
- [Clone the fork using the `Command Palette`](#clone-the-fork-using-the-command-palette)

#### Clone the fork using the `VS Code Terminal`

1. [Open the `VS Code Terminal`](./appendix/vs-code.md#open-the-vs-code-terminal).
2. You should see `software-engineering-toolkit` as your [current working directory](./appendix/shell.md#current-working-directory).
3. [Run using the `VS Code Terminal`](./appendix/vs-code.md#run-a-command-using-the-vs-code-terminal):

   ```terminal
    git clone <fork-url>
    ```

    Note: replace `<fork-url>` with the copied fork URL.
4. [Run using the `VS Code Terminal`](./appendix/vs-code.md#run-a-command-using-the-vs-code-terminal):

   ```terminal
   ls
   ```

5. You should see `se-toolkit-lab-2` - the output of the command. This is the directory that contains the cloned repo.

#### Clone the fork using the `Command Palette`

1. [Run using the `Command Palette`](../lab/appendix/vs-code.md#run-a-command-using-the-command-palette):
   `Git: Clone`.
2. Click `Clone from GitHub`.
3. Allow the extension to sign in.
4. Find your fork in the list.
5. It should look like `<your-username>/se-toolkit-lab-2`.
6. Click it.
7. Choose a directory where to clone the repo.
8. You should choose `software-engineering-toolkit` that you created before.
9. Confirm the choice.

### 18. Open `VS Code` in the cloned repo directory

1. [Run using the `Command Palette`](../lab/appendix/vs-code.md#run-a-command-using-the-command-palette):
   `File: Open Folder...`.
2. Choose the directory `se-toolkit-lab-2` that is a clone of your fork.
3. Make sure there is `README.md` inside that directory.
4. `VS Code` should open in that directory.
5. [Open `Folders`](./appendix/vs-code.md#open-folders).
6. Look at `FOLDERS`.
7. You should see `SE-TOOLKIT-LAB-2` there.
8. You can close the `VS Code` that you [opened in the `software-engineering-toolkit` directory](#13-open-vs-code-in-the-software-engineering-toolkit-directory).

### 19. Continue creating a VM

[Create a VM using the subscription](./appendix/vm.md#create-a-vm-using-the-subscription).

### 20. Install `Python` and dependencies

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

### 21. Select the `Python` interpreter

1. [Run using the `Command Palette`](./appendix/vs-code.md#run-a-command-using-the-command-palette):
   `Python: Select Interpreter`.
2. Click `Recommended` to select the interpreter in `./.venv/bin/python`.

### 22. Check that `Python` works

1. [Open a new `VS Code Terminal`](./appendix/vs-code.md#open-a-new-terminal).
2. [Run using the `VS Code Terminal`](./appendix/vs-code.md#run-a-command-using-the-vs-code-terminal):

   ```terminal
   uv run python --version
   ```

3. The output should be similar to this:

   ```terminal
   Python 3.12.12
   ```

> [!NOTE]
> The `Python` version for this project is specified in the [`pyproject.toml`](../pyproject.toml) file using the `requires-python` setting.

---

## Optional steps

These enhancements can make your life easier:

- [1. Change the workspace settings](#1-change-the-workspace-settings)
- [2. Set up a coding agent](#2-set-up-a-coding-agent)
- [3. Set up the shell prompt](#3-set-up-the-shell-prompt)
- [4. Customize the `Source Control`](#4-customize-the-source-control)
- [5. Get familiar with `GitLens`](#5-get-familiar-with-gitlens)
- [6. Create a label for tasks](#6-create-a-label-for-tasks)

### 1. Change the workspace settings

1. Go to the [workspace settings](./appendix/vs-code.md#workspace-settings).
2. Change them as necessary.

### 2. Set up a coding agent

A coding agent can help you write code, explain concepts, and debug issues.

See [Coding agents](./appendix/coding-agents.md).

### 3. Set up the shell prompt

`Starship` shows your current `Git` branch, status, and other useful info directly in your [shell prompt](https://en.wikibooks.org/wiki/Guide_to_Unix/Explanations/Shell_Prompt) in almost any terminal, including the [`VS Code Terminal`](./appendix/vs-code.md#terminal).

Complete these steps:

1. Install [`Starship`](https://github.com/starship/starship#-installation).
2. [Open the `VS Code Terminal`](./appendix/vs-code.md#open-the-vs-code-terminal).
3. You should see something similar to `se-toolkit-lab-2 on main`.

### 4. Customize the `Source Control`

1. [Open the `Source Control`](./appendix/vs-code.md#open-the-source-control).
2. Click three dots to the right of `SOURCE CONTROL`.
3. Put checkmarks only near `Changes` and `GitLens` to see only these views.

   <img alt="Changes and GitLens" src="./images/appendix/vs-code/source-control-allowed-views.png" style="width:400px"></img>

### 5. Get familiar with `GitLens`

[`GitLens`](./appendix/gitlens.md) helps you work with `Git` in `VS Code`.

Complete these steps:

1. [See all branches](./appendix/gitlens.md#see-all-branches)
2. [Look at the commit graph](./appendix/gitlens.md#look-at-the-commit-graph)
3. [Inspect the current branch](./appendix/gitlens.md#inspect-the-current-branch)
4. [Inspect the remotes](./appendix/gitlens.md#inspect-the-remotes)

### 6. Create a label for tasks

[Labels](https://docs.github.com/en/issues/using-labels-and-milestones-to-track-work/managing-labels) help you filter and organize issues.

With a `task` label, you can see in one view all issues created for lab tasks.

> [!TIP]
> If you create the `task` label before creating issues, your issues will have this label automatically as configured in the [issue form](../.github/ISSUE_TEMPLATE/01-task.yml).

Complete these steps:

1. [Create the `task` label](#create-the-task-label)
2. [Add the label to issues](#add-the-label-to-issues)
3. [See all issues with the label](#see-all-issues-with-the-label)

#### Create the `task` label

1. Go to your fork.
2. Go to `Issues` -> `Labels`.
3. Create a new label:
   1. Click `New label`.
   2. Name: `task`.
   3. Click `Create label`.

#### Add the label to issues

1. Go to your fork.
2. [Add](https://github.com/orgs/community/discussions/53473#discussioncomment-5697478) the `task` label to some of your issues.

#### See all issues with the label

1. Go to your fork.
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
5. Open [`README.md`](../README.md) using any of the following methods.

   Method 1:

   1. [Open the file using the `Command Palette`](./appendix/vs-code.md#open-a-file-using-the-command-palette).

   Method 2:

   1. [Open `Folders`](./appendix/vs-code.md#open-the-folders).
   2. Click `README.md`.

6. Open the [`Markdown` preview](https://code.visualstudio.com/docs/languages/markdown#_markdown-preview) using any of the following methods.

   > [!NOTE]
   > `Markdown` is a [markup language](https://en.wikipedia.org/wiki/Markup_language).
   >
   > `Markdown` gets translated into [`HTML`](https://en.wikipedia.org/wiki/HTML).
   >
   > You see the rendered `HTML` when you open a preview in `VS Code` or on `GitHub`.

   Method 1:

   1. Go to the [`Editor Toolbar`](./appendix/vs-code.md#editor-toolbar).
   2. Click `Open Preview to the Side`.

   Method 2:

   1. [Run using the `Command Palette`](./appendix/vs-code.md#run-a-command-using-the-command-palette):

      `Markdown: Open Preview to the Side`
