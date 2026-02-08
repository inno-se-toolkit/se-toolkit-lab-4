# Lab setup

## Find a partner

1. Find a classmate to be your partner for this lab.
2. Sit together.

## Set up a fork

1. Create a `GitHub` account.
2. Go to the [original repo](https://github.com/inno-se-toolkit/lab-01-market-product-and-git) (repository).
3. [Fork](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo#forking-a-repository) the original repo.
4. Go to your fork. The `URL` should be like `https://github.com/<your-username>/lab-01-market-product-and-git`.
5. If you see a lock sign near your fork name, [make your fork public](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/managing-repository-settings/setting-repository-visibility#changing-a-repositorys-visibility).

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

Branch protection prevents accidental pushes directly to `main`.
This enforces the PR workflow and ensures all changes are reviewed.

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
1. [Open the Terminal](./appendix/vs-code.md#open-the-terminal).

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

## Clone the repo on your computer

Clone the repo using one of these approaches:

- [Clone the repo using a terminal](#clone-the-repo-using-a-terminal)
- [Clone the repo using `VS Code`](#clone-the-repo-using-vs-code)

### Clone the repo using a terminal

1. On your computer, create a directory `software-engineering-toolkit`.
2. Open a terminal in that directory (google how to do that).
3. In the terminal, you should see `software-engineering-toolkit`.
4. Copy your fork link ([`URL`](https://en.wikipedia.org/wiki/URL)):
   1. Go to your fork on `GitHub`.
   2. Copy its `URL`.
   3. It should look like `https://github.com/<your-username>/lab-01-market-product-and-git`.
5. Return to the terminal.
6. Run the command (replace `<fork-url>` with the copied `URL`):

    ```console
    git clone <fork-url>
    ```

### Clone the repo using `VS Code`

1. Open `VS Code`.
2. [Open the `Command Palette`](../lab/appendix/vs-code.md#open-the-command-palette).
3. Run
4. [Open the `Source Control`](../lab/appendix/vs-code.md#open-the-source-control).
5. Click `CHANGES` to uncollapse that panel.
6. Click `Clone Repository`.
7. Click `Clone from GitHub`.
8. Allow the extension to sign in.
9. Find your fork in the list.
10. Click it.
11. Choose a directory where to clone the repo.
12. Confirm the choice.

## Open the repo in `VS Code`

1. Open `VS Code`.
2. [Open the `Command Palette`](../lab/appendix/vs-code.md#command-palette).
3. Run `File: Open Folder...`
4. Find the directory `lab-01-market-product-and-git` that stores the clone of your fork.
5. Make sure there is `README.md` inside that directory.

## Set up `VS Code` extensions

1. [Install recommended `VS Code` extensions](./appendix/vs-code.md#install-recommended-extensions).
2. Sign in to accounts.
    1. Go to the [`Activity Bar`](./appendix/vs-code.md#activity-bar).
    2. Click the icon `Accounts`.
    3. Click `Sign in with GitHub ...`.
    4. Repeat for the remaining extensions if there are any.

## Explore `VS Code` layout

Look at the [`Basic Layout`](./appendix/vs-code.md#basic-layout).

## Open `Markdown` file preview

Open `README.md` using one of these approaches:

- Approach 1:
  - [Use the `Command Palette`](./appendix/vs-code.md#open-a-file).
- Approach 2:
    1. [Open `Folders`](./appendix/vs-code.md#open-folders).
    2. Click `README.md`.

Open the [`Markdown` preview](https://code.visualstudio.com/docs/languages/markdown#_markdown-preview) using one of these approaches:

- Approach 1:
  1. Go to the [`Editor Toolbar`](./appendix/vs-code.md#editor-toolbar).
  2. Click `Open Preview to the Side`.

- Approach 2:
   1. [Open the `Command Palette`](./appendix/vs-code.md#open-the-command-palette).
   2. Run `Markdown: Open Preview to the Side`.

## Change workspace settings

Look at the [workspace settings](./appendix/vs-code.md#workspace-settings) and change them as necessary.

---

## Optional enhancements

### Set up a coding agent

A coding agent can help you write code, explain concepts, and debug issues.

See [Coding agents](./appendix/coding-agents.md).

### Set up the shell prompt

`Starship` shows your current `Git` branch, status, and other useful info directly in your shell prompt in almost any terminal, including the [`Terminal`](./appendix/vs-code.md#terminal).

Install [`Starship`](https://github.com/starship/starship#-installation).

### Check `GitLens` in `VS Code`

`GitLens` shows commit history, blame annotations, and branch visualization right inside `VS Code`.

Complete these steps:

1. [See all branches](#see-all-branches)
2. [Look at the commit graph](#look-at-the-commit-graph)
3. [Inspect remotes and the current branch](#inspect-remotes-and-the-current-branch)
4. [(Optional) Learn more about `GitLens`](#optional-learn-more-about-gitlens)

#### See all branches

1. Go to the [`Status Bar`](../lab/appendix/vs-code.md#status-bar).
2. Look at the branch name.
3. Click it to see all available branches.
4. If you click a branch, you'll be able to switch to it.

#### Look at the commit graph

1. Go to the [`Status Bar`](../lab/appendix/vs-code.md#status-bar):
1. Click the icon `Visualize commits on the Commit Graph`.
1. Make sure you can see the commit graph.

#### Inspect remotes and the current branch

1. [Open the `Source Control`](../lab/appendix/vs-code.md#open-the-source-control).
2. Go to the [`Sidebar Toolbar`](../lab/appendix/vs-code.md#basic-layout).
3. Click three dots.
4. Click `GITLENS` in the opened [`Primary Side Bar`](../lab/appendix/vs-code.md#basic-layout).
5. Go to the `GITLENS` panel.
6. Click the icon `Remotes`.
7. Make sure `origin` points to your repo URL (hover over it an look at URLs).
8. Click the icon `Commits`.
9. Make sure you can see commits on the current branch.

#### (Optional) Learn more about `GitLens`

See [`GitLens` features](https://help.gitkraken.com/gitlens/gitlens-features/).

### Create a label for tasks

[Labels](https://docs.github.com/en/issues/using-labels-and-milestones-to-track-work/managing-labels) help you filter and organize issues.

With a `task` label, you can see in one view all issues created for lab tasks.

> [!TIP]
> If you create the `task` label before creating issues, your issues will have this label automatically as configured in the [issue form](../.github/ISSUE_TEMPLATE/01-task.yml).

Complete these steps:

1. [Create the `task` label](#create-the-task-label)
1. [Add the label to issues](#add-the-label-to-issues)
1. [See all issues with the label](#see-all-issues-with-the-label)

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
