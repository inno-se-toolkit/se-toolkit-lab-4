# `Git` in `VS Code`

<h2>Table of contents</h2>

- [Open `VS Code` in the directory](#open-vs-code-in-the-directory)
- [Clone the repo](#clone-the-repo)
  - [Clone the repo using the `VS Code Terminal`](#clone-the-repo-using-the-vs-code-terminal)
  - [Clone the repo using the `Command Palette`](#clone-the-repo-using-the-command-palette)
- [Switch to the `<branch-name>` branch](#switch-to-the-branch-name-branch)
  - [Switch to the `<branch-name>` branch using the `VS Code Terminal`](#switch-to-the-branch-name-branch-using-the-vs-code-terminal)
  - [Switch to the `<branch-name>` branch using `GitLens`](#switch-to-the-branch-name-branch-using-gitlens)
- [Detect conflicts](#detect-conflicts)
- [Pull changes from `origin/<branch-name>`](#pull-changes-from-originbranch-name)
  - [Pull changes from `origin/<branch-name>` using the `VS Code Terminal`](#pull-changes-from-originbranch-name-using-the-vs-code-terminal)
  - [Pull changes from `origin/<branch-name>` using `GitLens`](#pull-changes-from-originbranch-name-using-gitlens)
- [Stage using the `Source Control`](#stage-using-the-source-control)
  - [Stage all changes in a specific file](#stage-all-changes-in-a-specific-file)
  - [Stage all changes in specific files](#stage-all-changes-in-specific-files)
  - [Stage specific changes in a specific file](#stage-specific-changes-in-a-specific-file)
- [Unstage specific changes](#unstage-specific-changes)
- [Commit changes](#commit-changes)
  - [Commit using the `VS Code Terminal`](#commit-using-the-vs-code-terminal)
  - [Commit using `Source Control`](#commit-using-source-control)
    - [Commit staged changes](#commit-staged-changes)
- [Undo commits](#undo-commits)
  - [Undo commits using the `VS Code Terminal`](#undo-commits-using-the-vs-code-terminal)
  - [Undo commits using `GitLens`](#undo-commits-using-gitlens)
- [Publish the branch](#publish-the-branch)
  - [Publish using the `VS Code Terminal`](#publish-using-the-vs-code-terminal)
  - [Publish using `GitLens`](#publish-using-gitlens)
- [Push more commits](#push-more-commits)
  - [Push using the `VS Code Terminal`](#push-using-the-vs-code-terminal)
  - [Push using `GitLens`](#push-using-gitlens)
- [Switch to a new branch](#switch-to-a-new-branch)
  - [Switch to a new branch using `GitHub`](#switch-to-a-new-branch-using-github)
  - [Switch to a new branch using the `VS Code Terminal`](#switch-to-a-new-branch-using-the-vs-code-terminal)
  - [Switch to a new branch using `GitLens`](#switch-to-a-new-branch-using-gitlens)

## Open `VS Code` in the directory

> [!NOTE]
> The `<directory-name>` is the name of a directory.
>
> Example: `software-engineering-toolkit`

1. [Run using the `Command Palette`](./appendix/vs-code.md#command-palette):
   `File: Open Folder...`
2. Find the directory `<directory-name>` that you created.
3. Open this directory.

   `VS Code` should now open in that directory.
4. [Open `Folders`](./appendix/vs-code.md#open-folders).
5. Look at `FOLDERS`.
6. You should see `<DIRECTORY-NAME>` there.

   Example: `SOFTWARE-ENGINEERING-TOOLKIT`

## Clone the repo

> [!NOTE]
> The [`<repo-url>`](./github.md#repo-url) is the repo [URL](./web-development.md#url).
>
> The [`<repo-name>`](./github.md#repo-name) is the repo name.

- Method 1: [Clone the repo using the `VS Code Terminal`](#clone-the-repo-using-the-vs-code-terminal)
- Method 2: [Clone the repo using the `Command Palette`](#clone-the-repo-using-the-command-palette)

### Clone the repo using the `VS Code Terminal`

1. Open `VS Code` in the `software-engineering-toolkit`.
1. [Open the `VS Code Terminal`](./appendix/vs-code.md#open-the-vs-code-terminal).
   You should see `software-engineering-toolkit` as your [current working directory](./shell.md#current-working-directory).
1. [Run using the `VS Code Terminal`](./appendix/vs-code.md#run-a-command-using-the-vs-code-terminal):

    ```terminal
    git clone <repo-url>
    ```

    Example:

    ```terminal
    git clone <repo-url>
    ```

1. [Run using the `VS Code Terminal`](./appendix/vs-code.md#run-a-command-using-the-vs-code-terminal):

   ```terminal
   ls
   ```

   You should see `<repo-name>` - the output of the command.
   This is the directory that contains the cloned repo.

### Clone the repo using the `Command Palette`

1. [Run using the `Command Palette`](../lab/appendix/vs-code.md#run-a-command-using-the-command-palette):
   `Git: Clone`.
2. Click `Clone from GitHub`.
3. Allow the extension to sign in.
4. Paste the [`<repo-url>`](./github.md#repo-url).
5. [Select](./vs-code.md#select-an-option-from-a-list) the repo.
6. Choose a directory where to clone the repo.

   You should choose `software-engineering-toolkit` that you created before.
7. Confirm the choice.

## Switch to the `<branch-name>` branch

- Method 1: [Switch to the `<branch-name>` branch using the `VS Code Terminal`](#switch-to-the-branch-name-branch-using-the-vs-code-terminal)
- Method 2: [Switch to the `<branch-name>` branch using `GitLens`](#switch-to-the-branch-name-branch-using-gitlens)

### Switch to the `<branch-name>` branch using the `VS Code Terminal`

1. [Run using the `VS Code Terminal`](./vs-code.md#run-a-command-using-the-vs-code-terminal):

   ```terminal
   git switch <branch name>
   ```

   Example:

   ```terminal
   git switch main
   ```

### Switch to the `<branch-name>` branch using `GitLens`

1. [Run using the `Command Palette`](./vs-code.md#run-a-command-using-the-command-palette):
   `GitLens: Git Switch to..`.
2. [Select](./vs-code.md#select-an-option-from-a-list) the `<branch-name>` branch.

## Detect conflicts

It can happen that commits on your `origin/<branch-name>` are different from commits
on the `<branch-name>` branch in your cloned repo on your computer.

Check whether you have such conflicts:

1. Look at the [`Status Bar`](../appendix/vs-code.md#status-bar).

   <img alt="Commit Conflict" src="../images/appendix/vs-code/status-bar-commit-conflict.png" style="width:400px"></img>

   You should see that there is a non-zero number of commits to pull from `origin/<branch-name>`.

## Pull changes from `origin/<branch-name>`

> [!NOTE]
> `origin` is an alias for your fork on `GitHub` (see [Inspect remotes](./gitlens.md#inspect-remotes)).

Pull changes from the `<branch-name>` branch in your fork on `GitHub`.

We call that branch `origin/<branch-name>`.

- Method 1: [Pull changes from `origin/<branch-name>` using the `VS Code Terminal`](#pull-changes-from-originbranch-name-using-the-vs-code-terminal)
- Method 2: [Pull changes from `origin/<branch-name>` using `GitLens`](#pull-changes-from-originbranch-name-using-gitlens)

### Pull changes from `origin/<branch-name>` using the `VS Code Terminal`

1. [Run using the `VS Code Terminal`](../appendix/vs-code.md#run-a-command-using-the-vs-code-terminal):

   ```terminal
   git pull origin <branch-name>
   ```

   Example:

   ```terminal
   git pull origin main
   ```

### Pull changes from `origin/<branch-name>` using `GitLens`

1. [Run using the `Command Palette`](../appendix/vs-code.md#run-a-command-using-the-command-palette):
   `GitLens: Pull`

## Stage using the `Source Control`

### Stage all changes in a specific file

<!-- TODO click + near the name -->

### Stage all changes in specific files

<!-- TODO select and click + -->

### Stage specific changes in a specific file

1. [Open the `Source Control`](./vs-code.md#open-the-source-control).
2. Go to `Changes`.
3. Click a file to open it.
4. Select changed lines in the editor (red-green).
5. Right mouse click the selected lines.
6. Click `Stage Selected Ranges`.

## Unstage specific changes

1. [Open the `Source Control`](./vs-code.md#open-the-source-control).
2. Go to `Staged Changes`.
3. Click a file.
4. Select changed lines in the editor (red-green).
5. Right mouse click the selected lines.
6. Click `Unstage Selected Ranges`.

## Commit changes

> ![NOTE]
> Commit message format is: `type: short description`
>
> Common types:
>
> - `fix:` — bug fixes
> - `feat:` — additions (e.g., new feature)
> - `docs:` — documentation changes

Use any of the following methods:

<!-- no toc -->
- [Commit changes](#commit-changes)
  - [Commit using the `VS Code Terminal`](#commit-using-the-vs-code-terminal)
  - [Commit using `Source Control`](#commit-using-source-control)
    - [Commit staged changes](#commit-staged-changes)

### Commit using the `VS Code Terminal`

1. Open the [`VS Code Terminal`](./vs-code.md#open-the-vs-code-terminal).
2. Run:

   ```terminal
   git add <file>
   # example: git add README.md
   # example (path with spaces): git add 'path/some image.svg'
   
   git commit -m '<type>: <short description>'
   # example: git commit -m 'docs: add architecture diagram'
   ```

### Commit using `Source Control`

1. [Open the `Source Control`](./vs-code.md#open-the-source-control).
2. Go to `Changes`.
3. Hover over a file name.
4. Click `+` to stage the file.
5. Write a commit message, e.g., `docs: add architecture diagram`.
6. Click `Commit`.

#### Commit staged changes

1. [Open the `Source Control`](./vs-code.md#open-the-source-control).
2. Write a commit message.
3. Click `Commit`.

## Undo commits

> [!NOTE]
> There can appear a merge [conflict](./git.md#merge-conflict) when you try to undo.

Undo commits using any of the following methods:

<!-- no toc -->
- [Undo commits](#undo-commits)
  - [Undo commits using the `VS Code Terminal`](#undo-commits-using-the-vs-code-terminal)
  - [Undo commits using `GitLens`](#undo-commits-using-gitlens)

### Undo commits using the `VS Code Terminal`

[Run using the `VS Code Terminal`](./vs-code.md#run-a-command-using-the-vs-code-terminal):

```terminal
git reset --soft HEAD~1
```

Your changes are staged now.

You can stage more changes.

```terminal
git add some-file
```

Then, you can commit using the previous message.

```terminal
git commit -C ORIG_HEAD
```

### Undo commits using `GitLens`

See [Undo commit on the current branch](./gitlens.md#undo-a-commit-on-the-current-branch).

## Publish the branch

### Publish using the `VS Code Terminal`

1. [Run using the `VS Code Terminal`](./vs-code.md#run-a-command-using-the-vs-code-terminal):

   ```terminal
   git push -u origin <branch-name>
   ```

### Publish using `GitLens`

1. [Open the `Source Control`](./vs-code.md#open-the-source-control).
2. Click `GITLENS` to open the `GitLens` panel.
3. Click the `Commits` icon.
4. Click the `Publish Branch` icon to the right of `Publish <branch-name> to GitHub`.
5. Press `Enter` to confirm.

## Push more commits

### Push using the `VS Code Terminal`

1. [Run using the `VS Code Terminal`](./vs-code.md#run-a-command-using-the-vs-code-terminal):

   ```terminal
   git push
   ```

### Push using `GitLens`

1. [Open the `Source Control`](./vs-code.md#open-the-source-control).
2. Click `GITLENS`.
3. Click the `Commits` icon.
4. Click the `Push` icon to the right of `COMMITS`.

## Switch to a new branch

Create a new branch and switch to it:

<!-- no toc -->
- Method 1: [Switch to a new branch using `GitHub`](#switch-to-a-new-branch-using-github)
- Method 2: [Switch to a new branch using the `VS Code Terminal`](#switch-to-a-new-branch-using-the-vs-code-terminal)
- Method 3: [Switch to a new branch using `GitLens`](#switch-to-a-new-branch-using-gitlens)

> [!IMPORTANT]
> Replace the `<branch-name>` with the actual branch name.

### Switch to a new branch using `GitHub`

1. [Go to the repo](./github.md#go-to-your-fork).
2. [Create a branch](https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/creating-a-branch-for-an-issue).
3. Copy the command provided by `GitHub`.

   It's looks like this:

   ```terminal
   git fetch origin
   git checkout <branch-name>
   ```

4. [Run the copied command using the `VS Code Terminal`](./vs-code.md#run-a-command-using-the-vs-code-terminal).

### Switch to a new branch using the `VS Code Terminal`

1. [Run using the `VS Code Terminal`](./vs-code.md#run-a-command-using-the-vs-code-terminal):

    ```terminal
    git checkout -b <branch-name>
    ```

### Switch to a new branch using `GitLens`

1. [Run using the `Command Palette`](./vs-code.md#run-a-command-using-the-command-palette):
   `GitLens: Git Create Branch...`.
2. [Select](./vs-code.md#select-an-option-from-a-list)
   `main` as the base branch.
3. Write `<branch-name>` to provide the new branch name.
4. Press `Enter` to confirm.
5. [Select](./vs-code.md#select-an-option-from-a-list)
   `Create & Switch to Branch`.
