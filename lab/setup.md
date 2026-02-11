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
  - [12. (Windows only) Set the default shell](#12-windows-only-set-the-default-shell)
  - [13. Open the `Terminal`](#13-open-the-terminal)
  - [14. Configure `Git`](#14-configure-git)
  - [15. Open `VS Code` in the `software-engineering-toolkit` directory](#15-open-vs-code-in-the-software-engineering-toolkit-directory)
  - [16. Copy your fork URL](#16-copy-your-fork-url)
  - [17. Clone the fork on your computer](#17-clone-the-fork-on-your-computer)
    - [Clone the fork using the `Terminal`](#clone-the-fork-using-the-terminal)
    - [Clone the fork using the `Command Palette`](#clone-the-fork-using-the-command-palette)
  - [18. Open `VS Code` in the cloned repo directory](#18-open-vs-code-in-the-cloned-repo-directory)
  - [19. Set up `VS Code` extensions](#19-set-up-vs-code-extensions)
  - [20. Reload `VS Code`](#20-reload-vs-code)
  - [21. Explore `VS Code` layout](#21-explore-vs-code-layout)
  - [22. Open `README.md`](#22-open-readmemd)
  - [23. Open `Markdown` preview](#23-open-markdown-preview)
  - [24. Change the workspace settings](#24-change-the-workspace-settings)
  - [25. Continue creating a VM](#25-continue-creating-a-vm)
- [Optional steps](#optional-steps)
  - [1. Set up a coding agent](#1-set-up-a-coding-agent)
  - [2. Set up the shell prompt](#2-set-up-the-shell-prompt)
  - [3. Customize the `Source Control`](#3-customize-the-source-control)
  - [4. Get familiar with `GitLens`](#4-get-familiar-with-gitlens)
  - [5. Create a label for tasks](#5-create-a-label-for-tasks)
    - [Create the `task` label](#create-the-task-label)
    - [Add the label to issues](#add-the-label-to-issues)
    - [See all issues with the label](#see-all-issues-with-the-label)

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

> [!NOTE]
> We'll refer to your `GitHub` username as `<your-username>`.
>
> Example of a username: `johndoe`.
>
> Note that this username doesn't include `@`.
>
> `<your-username>` also doesn't include `@`.

### 4. Fork the course instructors' repo

1. Go to the course instructors' [repo](https://github.com/inno-se-toolkit/se-toolkit-lab-2).
2. Fork the course instructors' repo:
   1. Click `Fork`.
   2. Click `Choose an owner`.
   3. Click `<your-username>` to make you the repo owner.
   4. Click `Create fork`.

### 5. Go to your fork

1. Go to your fork (a partial copy of the instructors' repo stored on `GitHub`).
2. The URL of your fork should be like `https://github.com/<your-username>/se-toolkit-lab-2`.

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

### 12. (Windows only) Set the default shell

1. Go to [`.vscode/settings.json`](../.vscode/settings.json).
2. If you have `WSL` installed: write there the [setting](https://code.visualstudio.com/docs/terminal/profiles#_wsl) for `WSL`.
3. If you don't have `WSL` installed:
   1. Find the line `// Uncomment to set Git Bash as the default shell.`.
   2. Under that line, [uncomment](./appendix/vs-code.md#basic-layout) the `"terminal.integrated.defaultProfile.windows"` and `"terminal.integrated.profiles.windows"` settings.

### 13. Open the `Terminal`

1. Open `VS Code`.
2. [Open the Terminal](./appendix/vs-code.md#open-the-terminal).

### 14. Configure `Git`

> [!IMPORTANT]
> Replace `<your-name>` with a name and `<your-email>` with an email that you want to see in the commits.

1. (Optional) See [docs](https://git-scm.com/docs/git-config#Documentation/git-config.txt-username) for an explanation of what these commands do.
2. [Run using the `Terminal`](./appendix/vs-code.md#run-a-command-using-the-terminal):

    ```terminal
    git config --global user.name '<your-name>'
    ```

    Example: `git config --global user.name 'John Doe'`

3. [Run using the `Terminal`](./appendix/vs-code.md#run-a-command-using-the-terminal):

     ```terminal
     git config --global user.email '<your-email>'
     ```

     Example: `git config --global user.name 'johndoe@gmail.com'`

### 15. Open `VS Code` in the `software-engineering-toolkit` directory

1. On your computer, create somewhere a directory `software-engineering-toolkit` (e.g., on your `Desktop`).
2. Open `VS Code`.
3. [Run using the `Command Palette`](./appendix/vs-code.md#command-palette):
   `File: Open Folder...`
4. Find the `software-engineering-toolkit` directory that you created.
5. Open this directory.
6. `VS Code` should now open in that directory.
7. [Open `Folders`](./appendix/vs-code.md#open-folders).
8. Look at `FOLDERS`.
9. You should see `SOFTWARE-ENGINEERING-TOOLKIT` there.

### 16. Copy your fork URL

1. Go to your fork on `Gitub`.
2. Copy its [URL](https://en.wikipedia.org/wiki/URL).
3. It should look like `https://github.com/<your-username>/se-toolkit-lab-2`.

### 17. Clone the fork on your computer

Clone the fork using any of the following methods:

- [Clone the fork using the `Terminal`](#clone-the-fork-using-the-terminal)
- [Clone the fork using the `Command Palette`](#clone-the-fork-using-the-command-palette)

#### Clone the fork using the `Terminal`

1. [Open the `Terminal`](./appendix/vs-code.md#open-the-terminal).
2. You should see `software-engineering-toolkit` as your current directory.
3. [Run using the `Terminal`](./appendix/vs-code.md#run-a-command-using-the-terminal):

   ```terminal
    git clone <fork-url>
    ```

    Note: replace `<fork-url>` with the copied fork URL.
4. [Run using the `Terminal`](./appendix/vs-code.md#run-a-command-using-the-terminal):

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
7. You should see `LAB-01-MARKET-PRODUCT-AND-GIT` there.
8. You can close the `VS Code` that you [opened in the `software-engineering-toolkit` directory](#15-open-vs-code-in-the-software-engineering-toolkit-directory).

### 19. Set up `VS Code` extensions

1. [Install recommended `VS Code` extensions](./appendix/vs-code.md#install-recommended-extensions).
2. Sign in to accounts.
    1. Go to the [`Activity Bar`](./appendix/vs-code.md#activity-bar).
    2. Click the icon `Accounts`.
    3. Click `Sign in with GitHub ...`.
    4. Repeat for the remaining extensions if there are any.

### 20. Reload `VS Code`

[Run using the `Command Palette`](./appendix/vs-code.md#run-a-command-using-the-command-palette):
`Developer: Reload Window`.

### 21. Explore `VS Code` layout

Look at the [`Basic Layout`](./appendix/vs-code.md#basic-layout).

### 22. Open `README.md`

> [!NOTE]
> This file (`lab/setup.md`), `README.md`, and other files in this repository that have the extension `.md` are written in [`Markdown`](https://en.wikipedia.org/wiki/Markdown) (more precisely, in [`GitHub-flavored Markdown`](https://github.github.com/gfm/)).

Open [`README.md`](../README.md) using any of the following methods.

Method 1:

1. [Open the file using the `Command Palette`](./appendix/vs-code.md#open-a-file-using-the-command-palette).

Method 2:

1. [Open `Folders`](./appendix/vs-code.md#open-the-folders).
2. Click `README.md`.

### 23. Open `Markdown` preview

> [!NOTE]
> `Markdown` is a [markup language](https://en.wikipedia.org/wiki/Markup_language).
>
> `Markdown` gets translated into [`HTML`](https://en.wikipedia.org/wiki/HTML).
>
> You see the rendered `HTML` when you open a preview in `VS Code` or on `GitHub`.

Open the [`Markdown` preview](https://code.visualstudio.com/docs/languages/markdown#_markdown-preview) using any of the following methods.

Method 1:

1. Go to the [`Editor Toolbar`](./appendix/vs-code.md#editor-toolbar).
2. Click `Open Preview to the Side`.

Method 2:

1. [Run using the `Command Palette`](./appendix/vs-code.md#run-a-command-using-the-command-palette):

   `Markdown: Open Preview to the Side`

### 24. Change the workspace settings

1. Go to the [workspace settings](./appendix/vs-code.md#workspace-settings).
2. Change them as necessary.

### 25. Continue creating a VM

[Create a VM using the subscription](./appendix/vm.md#create-a-vm-using-the-subscription).

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

`Starship` shows your current `Git` branch, status, and other useful info directly in your [shell prompt](https://en.wikibooks.org/wiki/Guide_to_Unix/Explanations/Shell_Prompt) in almost any terminal, including the [`Terminal`](./appendix/vs-code.md#terminal).

Complete these steps:

1. Install [`Starship`](https://github.com/starship/starship#-installation).
2. [Open the `Terminal`](./appendix/vs-code.md#open-the-terminal).
3. You should see something like `se-toolkit-lab-2 on main`.

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
