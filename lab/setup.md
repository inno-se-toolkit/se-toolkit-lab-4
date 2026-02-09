# Lab setup

- [Find a partner](#find-a-partner)
- [Fork the course instructors' repo](#fork-the-course-instructors-repo)
- [Enable issues](#enable-issues)
- [Add a classmate as a collaborator](#add-a-classmate-as-a-collaborator)
- [Protect your `main` branch](#protect-your-main-branch)
- [Install `Git`](#install-git)
- [Install `VS Code`](#install-vs-code)
- [Open the `Terminal`](#open-the-terminal)
- [Configure `Git`](#configure-git)
- [Open `VS Code` in the `software-engineering-toolkit` directory](#open-vs-code-in-the-software-engineering-toolkit-directory)
- [Copy your fork URL](#copy-your-fork-url)
- [Clone the fork on your computer](#clone-the-fork-on-your-computer)
  - [Clone the fork using the `Terminal`](#clone-the-fork-using-the-terminal)
  - [Clone the fork using the `Command Palette`](#clone-the-fork-using-the-command-palette)
- [Open the repo in `VS Code`](#open-the-repo-in-vs-code)
- [Set up `VS Code` extensions](#set-up-vs-code-extensions)
- [Reload `VS Code`](#reload-vs-code)
- [Explore `VS Code` layout](#explore-vs-code-layout)
- [Open `README.md`](#open-readmemd)
- [Open `Markdown` preview](#open-markdown-preview)
- [Change workspace settings](#change-workspace-settings)
- [Optional enhancements](#optional-enhancements)
  - [Set up a coding agent](#set-up-a-coding-agent)
  - [Set up the shell prompt](#set-up-the-shell-prompt)
- [Customize the `Source Control`](#customize-the-source-control)
  - [Get familiar with `GitLens`](#get-familiar-with-gitlens)
  - [Create a label for tasks](#create-a-label-for-tasks)
    - [Create the `task` label](#create-the-task-label)
    - [Add the label to issues](#add-the-label-to-issues)
    - [See all issues with the label](#see-all-issues-with-the-label)

## Find a partner

1. Find a classmate to be your partner for this lab.
2. Sit together.

## Fork the course instructors' repo

1. Create a `GitHub` account.
2. Go to the course instructors' [repo](https://github.com/inno-se-toolkit/lab-01-market-product-and-git) (repository).
3. Fork this repo: follow the [instructions on forking](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo#forking-a-repository).
4. Go to your fork (a partial copy of the instructors' repo stored on `GitHub`).
5. The URL of your fork should be like `https://github.com/<your-username>/lab-01-market-product-and-git`.
6. If you don't see `Public` near your fork name, [make your fork public](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/managing-repository-settings/setting-repository-visibility#changing-a-repositorys-visibility).

> [!NOTE]
> Continue working in your fork.

## Enable issues

1. Go to `Settings` -> `General` -> `Features`.
2. Check the box near `Issues`.

## Add a classmate as a collaborator

1. Go to `Settings` -> `Collaborators` -> `Add people`.
2. Add your partner as a collaborator.
3. Your partner should add you as a collaborator in their repo.
4. Make sure your collaborator has accepted the invitation sent to their email.
5. It's OK if your collaborator can't change `Settings` in your repo.

## Protect your `main` branch

> [!NOTE]
> Branch protection prevents accidental pushes directly to `main`.
> This enforces the PR workflow and ensures all changes are reviewed.

Complete these steps:

1. Go to your fork on `GitHub`.
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

## Install `Git`

[Install `Git`](https://git-scm.com/install/).

## Install `VS Code`

1. Install [`VS Code`](https://code.visualstudio.com/).

   We chose this editor because it has built-in AI features and many useful [extensions](./appendix/vs-code.md#extensions).

2. (Optional) [Learn more](../lab/appendix/vs-code.md) about `VS Code`.

## Open the `Terminal`

1. Open `VS Code`.
2. [Open the Terminal](./appendix/vs-code.md#open-the-terminal).

## Configure `Git`

> [!IMPORTANT]
> Replace `<your-name>` with a name and `<your-email>` with an email that you want to see in the commits.

1. (Optional) See [docs](https://git-scm.com/docs/git-config#Documentation/git-config.txt-username) for an explanation of what these commands do.
2. [Run using the `Terminal`](./appendix/vs-code.md#run-a-command-using-the-terminal):

    ```console
    git config --global user.name '<your-name>'
    ```

    Example: `git config --global user.name 'John Doe'`

3. [Run using the `Terminal`](./appendix/vs-code.md#run-a-command-using-the-terminal):

     ```console
     git config --global user.email '<your-email>'
     ```

     Example: `git config --global user.name 'johndoe@gmail.com'`

## Open `VS Code` in the `software-engineering-toolkit` directory

1. On your computer, create somewhere a directory `software-engineering-toolkit` (e.g., on your `Desktop`).
2. Open `VS Code`.
3. [Run using the `Command Palette`](./appendix/vs-code.md#command-palette): `File: Open Folder...`.
4. Find the `software-engineering-toolkit` directory that you created.
5. Open this directory.
6. `VS Code` should now open in that directory.
7. [Open `Folders`](./appendix/vs-code.md#open-folders).
8. Look at `FOLDERS`.
9. You should see `SOFTWARE-ENGINEERING-TOOLKIT` there.

## Copy your fork URL

1. Go to your fork on `Gitub`.
2. Copy its [URL](https://en.wikipedia.org/wiki/URL).
3. It should look like `https://github.com/<your-username>/lab-01-market-product-and-git`.

## Clone the fork on your computer

Clone the fork using any of these approaches:

- [Clone the fork using the `Terminal`](#clone-the-fork-using-the-terminal)
- [Clone the fork using the `Command Palette`](#clone-the-fork-using-the-command-palette)

### Clone the fork using the `Terminal`

1. [Open the `Terminal`](./appendix/vs-code.md#open-the-terminal).
2. Make sure you see `software-engineering-toolkit` as your current directory.
3. [Run using the `Terminal`](./appendix/vs-code.md#run-a-command-using-the-terminal):

   ```console
    git clone <fork-url>
    ```

    Note: replace `<fork-url>` with the copied fork URL.
4. [Run using the `Terminal`](./appendix/vs-code.md#run-a-command-using-the-terminal):

   ```console
   ls
   ```

5. You should see `lab-01-market-product-and-git` - the output of the command. This is the directory that contains the cloned repo.

### Clone the fork using the `Command Palette`

1. [Run using the `Command Palette`](../lab/appendix/vs-code.md#run-a-command-using-the-command-palette): `Git: Clone`.
2. Click `Clone from GitHub`.
3. Allow the extension to sign in.
4. Find your fork in the list.
5. It should look like `<your-username>/lab-01-market-product-and-git`.
6. Click it.
7. Choose a directory where to clone the repo.
8. You should choose `software-engineering-toolkit` that you created before.
9. Confirm the choice.

## Open the repo in `VS Code`

1. [Run using the `Command Palette`](../lab/appendix/vs-code.md#run-a-command-using-the-command-palette): `File: Open Folder...`.
2. Choose the directory `lab-01-market-product-and-git` that is a clone of your fork.
3. Make sure there is `README.md` inside that directory.
4. `VS Code` should open in that directory.
5. [Open `Folders`](./appendix/vs-code.md#open-folders).
6. Look at `FOLDERS`.
7. You should see `LAB-01-MARKET-PRODUCT-AND-GIT` there.
8. You can close the `VS Code` that you [opened in the `software-engineering-toolkit` directory](#open-vs-code-in-the-software-engineering-toolkit-directory).

## Set up `VS Code` extensions

1. [Install recommended `VS Code` extensions](./appendix/vs-code.md#install-recommended-extensions).
2. Sign in to accounts.
    1. Go to the [`Activity Bar`](./appendix/vs-code.md#activity-bar).
    2. Click the icon `Accounts`.
    3. Click `Sign in with GitHub ...`.
    4. Repeat for the remaining extensions if there are any.

## Reload `VS Code`

[Run using the `Command Palette`](./appendix/vs-code.md#run-a-command-using-the-command-palette): `Developer: Reload Window`.

## Explore `VS Code` layout

Look at the [`Basic Layout`](./appendix/vs-code.md#basic-layout).

## Open `README.md`

> [!NOTE]
> This file (`lab/setup.md`), `README.md`, and other files in this repository that have the extension `.md` are written in [`Markdown`](https://en.wikipedia.org/wiki/Markdown) (more precisely, in [`GitHub-flavored Markdown`](https://github.github.com/gfm/)).

Open [`README.md`](../README.md) using one of these approaches:

- Approach 1: [Open the file using the `Command Palette`](./appendix/vs-code.md#open-a-file).
- Approach 2:
    1. [Open `Folders`](./appendix/vs-code.md#open-folders).
    2. Click `README.md`.

## Open `Markdown` preview

> [!NOTE]
> `Markdown` gets translated into [`HTML`](https://en.wikipedia.org/wiki/HTML).
> You see the rendered `HTML` when you open a preview in `VS Code` or on `GitHub`.

Open the [`Markdown` preview](https://code.visualstudio.com/docs/languages/markdown#_markdown-preview) using one of these approaches:

- Approach 1:
  1. Go to the [`Editor Toolbar`](./appendix/vs-code.md#editor-toolbar).
  2. Click `Open Preview to the Side`.

- Approach 2:
   1. [Run using the `Command Palette`](./appendix/vs-code.md#run-a-command-using-the-command-palette): `Markdown: Open Preview to the Side`.

## Change workspace settings

Look at the [workspace settings](./appendix/vs-code.md#workspace-settings) and change them as necessary.

---

## Optional enhancements

These enhancements can make your life easier:

- [Set up a coding agent](#set-up-a-coding-agent)
- [Set up the shell prompt](#set-up-the-shell-prompt)
- [Customize the `Source Control`](#customize-the-source-control)
- [Get familiar with `GitLens`](#get-familiar-with-gitlens)
- [Create a label for tasks](#create-a-label-for-tasks)

### Set up a coding agent

A coding agent can help you write code, explain concepts, and debug issues.

See [Coding agents](./appendix/coding-agents.md).

### Set up the shell prompt

`Starship` shows your current `Git` branch, status, and other useful info directly in your [shell prompt](https://en.wikibooks.org/wiki/Guide_to_Unix/Explanations/Shell_Prompt) in almost any terminal, including the [`Terminal`](./appendix/vs-code.md#terminal).

Complete these steps:

1. Install [`Starship`](https://github.com/starship/starship#-installation).
2. [Open the `Terminal`](./appendix/vs-code.md#open-the-terminal).
3. You should see something like `lab-01-market-product-and-git on main`.

## Customize the `Source Control`

1. [Open the `Source Control`](./appendix/vs-code.md#open-the-source-control).
2. Click three dots to the right of `SOURCE CONTROL`.
3. Put checkmarks only near `Changes` and `GitLens` to see only these views.

   <img alt="Changes and GitLens" src="./images/appendix/vs-code/source-control-allowed-views.png" style="width:400px"></img>

### Get familiar with `GitLens`

[`GitLens`](./appendix/gitlens.md) helps you work with `Git` in `VS Code`.

Complete these steps:

1. [See all branches](./appendix/gitlens.md#see-all-branches)
2. [Look at the commit graph](./appendix/gitlens.md#look-at-the-commit-graph)
3. [Inspect the current branch](./appendix/gitlens.md#inspect-the-current-branch)
4. [Inspect the remotes](./appendix/gitlens.md#inspect-the-remotes)

### Create a label for tasks

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
