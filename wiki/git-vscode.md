# `Git` in `VS Code`

<h2>Table of contents</h2>

- [Clone the repository](#clone-the-repository)
  - [Clone the repo using the `VS Code Terminal`](#clone-the-repo-using-the-vs-code-terminal)
  - [Clone the repo using the `Command Palette`](#clone-the-repo-using-the-command-palette)
- [Switch to the `<branch-name>` branch](#switch-to-the-branch-name-branch)
  - [Switch to the `<branch-name>` branch using the `VS Code Terminal`](#switch-to-the-branch-name-branch-using-the-vs-code-terminal)
  - [Switch to the `<branch-name>` branch using `GitLens`](#switch-to-the-branch-name-branch-using-gitlens)
- [Detect conflicts](#detect-conflicts)
- [Resolve a merge conflict](#resolve-a-merge-conflict)
  - [Resolve a merge conflict using `VS Code`](#resolve-a-merge-conflict-using-vs-code)
  - [Resolve a merge conflict using `GitLens`](#resolve-a-merge-conflict-using-gitlens)
  - [Resolve a merge conflict using the `VS Code Terminal`](#resolve-a-merge-conflict-using-the-vs-code-terminal)
- [Pull changes from `origin/<branch-name>`](#pull-changes-from-originbranch-name)
  - [Pull changes from `origin/<branch-name>` using the `VS Code Terminal`](#pull-changes-from-originbranch-name-using-the-vs-code-terminal)
  - [Pull changes from `origin/<branch-name>` using `GitLens`](#pull-changes-from-originbranch-name-using-gitlens)
- [Pull changes from `origin/<branch-name>` and rebase](#pull-changes-from-originbranch-name-and-rebase)
  - [Pull and rebase using the `VS Code Terminal`](#pull-and-rebase-using-the-vs-code-terminal)
  - [Pull and rebase using `GitLens`](#pull-and-rebase-using-gitlens)
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

## Clone the repository

> [!NOTE]
> See [`<repo-url>`](./github.md#repo-url), [`<repo-name>`](./github.md#repo-name).

<!-- no toc -->
- Method 1: [Clone the repo using the `VS Code Terminal`](#clone-the-repo-using-the-vs-code-terminal)
- Method 2: [Clone the repo using the `Command Palette`](#clone-the-repo-using-the-command-palette)

### Clone the repo using the `VS Code Terminal`

1. Open `VS Code`.
2. [Open the `VS Code Terminal`](./vs-code.md#open-the-vs-code-terminal).
3. Navigate to the directory where you want to clone the repo:

   [Run using the `VS Code Terminal`](./vs-code.md#run-a-command-using-the-vs-code-terminal):

   ```terminal
   cd <directory-path>
   ```

   Example:

   ```terminal
   cd ~/Desktop/software-engineering-toolkit
   ```

4. [Run using the `VS Code Terminal`](./vs-code.md#run-a-command-using-the-vs-code-terminal):

    ```terminal
    git clone <repo-url>
    ```

    Example:

    ```terminal
    git clone https://github.com/microsoft/vscode
    ```

5. If `git` asks for a password, provide [your PAT](./github.md#create-a-pat-classic).

6. [Run using the `VS Code Terminal`](./vs-code.md#run-a-command-using-the-vs-code-terminal):

   ```terminal
   ls
   ```

   You should see `<repo-name>` - the output of the command.
   This is the directory that contains the cloned repo.

### Clone the repo using the `Command Palette`

1. [Run using the `Command Palette`](./vs-code.md#run-a-command-using-the-command-palette):
   `Git: Clone`.
2. Click `Clone from GitHub`.
3. Allow the extension to sign in.
4. Paste the [`<repo-url>`](./github.md#repo-url).
5. [Select](./vs-code.md#select-an-option-from-a-list) the repo.
6. Choose a directory where to clone the repo.
7. Confirm the choice.

## Switch to the `<branch-name>` branch

<!-- no toc -->
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

1. Look at the [`Status Bar`](./vs-code.md#status-bar).

   <img alt="Commit Conflict" src="./images/vs-code/status-bar-commit-conflict.png" style="width:400px"></img>

   You should see that there is a non-zero number of commits to pull from `origin/<branch-name>`.

## Resolve a merge conflict

Resolve a [merge conflict](./git.md#merge-conflict).

<!-- no toc -->
- Method 1: [Resolve a merge conflict using `VS Code`](#resolve-a-merge-conflict-using-vs-code)
- Method 2: [Resolve a merge conflict using `GitLens`](#resolve-a-merge-conflict-using-gitlens)
- Method 3: [Resolve a merge conflict using the `VS Code Terminal`](#resolve-a-merge-conflict-using-the-vs-code-terminal)

### Resolve a merge conflict using `VS Code`

`VS Code` has a built-in merge conflict editor.

1. Open a file with conflicts.
2. Use the inline options that appear above the conflict markers:
   - `Accept Current Change` — keep your branch's version.
   - `Accept Incoming Change` — keep the other branch's version.
   - `Accept Both Changes` — keep both versions.
3. Save the file.
4. [Run using the `VS Code Terminal`](./vs-code.md#run-a-command-using-the-vs-code-terminal):

   ```terminal
   git add <file-path>
   ```

5. [Run using the `VS Code Terminal`](./vs-code.md#run-a-command-using-the-vs-code-terminal):

   ```terminal
   git merge --continue
   ```

Docs:

- [Merge conflicts in `VS Code`](https://code.visualstudio.com/docs/sourcecontrol/overview#_merge-conflicts)

### Resolve a merge conflict using `GitLens`

If you see a pull error like the one below, resolve the conflicts:

<img alt="Pull Error" src="./images/gitlens/pull-error.png" style="width:400px"></img>

For each conflicting file, complete the following steps:

1. [Open the `Source Control`](./vs-code.md#open-the-source-control).
2. Go to `Merge Changes`.
3. Click a conflicting file.
4. Click `Resolve in Merge Editor`.
5. Accept the changes that you want to keep.
6. Click `Complete Merge`.
7. [Open the `Source Control`](./vs-code.md#open-the-source-control).
8. Click `Continue`.

> [!NOTE]
> If there are more conflicts, `VS Code` shows `Merging (1/3)` or `Rebasing (1/3)` (or similar).
> Repeat the steps above for each remaining conflict.

### Resolve a merge conflict using the `VS Code Terminal`

1. [Run using the `VS Code Terminal`](./vs-code.md#run-a-command-using-the-vs-code-terminal):

   ```terminal
   git status
   ```

   Files with conflicts are listed under `Unmerged paths`.

2. Open each conflicted file.
3. Find the conflict markers (`<<<<<<<`, `=======`, `>>>>>>>`).
4. Edit the file to keep the correct content.
5. Remove all conflict markers from the file.
6. [Run using the `VS Code Terminal`](./vs-code.md#run-a-command-using-the-vs-code-terminal):

   ```terminal
   git add <file-path>
   ```

7. [Run using the `VS Code Terminal`](./vs-code.md#run-a-command-using-the-vs-code-terminal):

   ```terminal
   git merge --continue
   ```

## Pull changes from `origin/<branch-name>`

> [!NOTE]
> `origin` is an alias for your fork on `GitHub` (see [Inspect remotes](./gitlens.md#inspect-remotes)).

Pull changes from the `<branch-name>` branch in your fork on `GitHub`.

We call that branch `origin/<branch-name>`.

<!-- no toc -->
- Method 1: [Pull changes from `origin/<branch-name>` using the `VS Code Terminal`](#pull-changes-from-originbranch-name-using-the-vs-code-terminal)
- Method 2: [Pull changes from `origin/<branch-name>` using `GitLens`](#pull-changes-from-originbranch-name-using-gitlens)

### Pull changes from `origin/<branch-name>` using the `VS Code Terminal`

1. [Run using the `VS Code Terminal`](./vs-code.md#run-a-command-using-the-vs-code-terminal):

   ```terminal
   git pull origin <branch-name>
   ```

   Example:

   ```terminal
   git pull origin main
   ```

### Pull changes from `origin/<branch-name>` using `GitLens`

1. [Run using the `Command Palette`](./vs-code.md#run-a-command-using-the-command-palette):
   `GitLens: Pull`

## Pull changes from `origin/<branch-name>` and rebase

<!-- no toc -->
- Method 1: [Pull and rebase using the `VS Code Terminal`](#pull-and-rebase-using-the-vs-code-terminal)
- Method 2: [Pull and rebase using `GitLens`](#pull-and-rebase-using-gitlens)

### Pull and rebase using the `VS Code Terminal`

1. [Run using the `VS Code Terminal`](./vs-code.md#run-a-command-using-the-vs-code-terminal):

   ```terminal
   git pull --rebase origin <branch-name>
   ```

   Example:

   ```terminal
   git pull --rebase origin main
   ```

### Pull and rebase using `GitLens`

1. [Run using the `Command Palette`](./vs-code.md#run-a-command-using-the-command-palette):
   `GitLens: Pull`
2. [Select](./vs-code.md#select-an-option-from-a-list)
   `Pull with Rebase`.
3. If `GitLens` does not show any error, the rebase is complete.

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

> [!NOTE]
> Commit message format is: `type: short description`
>
> Common types:
>
> - `fix:` — bug fixes
> - `feat:` — additions (e.g., new feature)
> - `docs:` — documentation changes

<!-- no toc -->
- Method 1: [Commit using the `VS Code Terminal`](#commit-using-the-vs-code-terminal)
- Method 2: [Commit using `Source Control`](#commit-using-source-control)
  - [Commit staged changes](#commit-staged-changes)

### Commit using the `VS Code Terminal`

1. Open the [`VS Code Terminal`](./vs-code.md#open-the-vs-code-terminal).
2. Run:

   ```terminal
   git add <file-path>
   # example: git add README.md
   # example (path with spaces): git add 'path/some image.svg'
   
   git commit -m '<type>: <short description>'
   # example: git commit -m 'docs: add architecture diagram'
   ```

   See [`<file-path>`](./file-system.md#file-path).

### Commit using `Source Control`

1. [Open the `Source Control`](./vs-code.md#open-the-source-control).
2. Go to `Changes`.
3. Hover over a file name.
4. Click `+` to stage the file.
5. [Commit staged changes](#commit-staged-changes)

#### Commit staged changes

1. [Open the `Source Control`](./vs-code.md#open-the-source-control).
2. Write a [commit message](./git.md#commit-message).
3. Click `Commit`.

## Undo commits

> [!NOTE]
> There can appear a merge [conflict](./git.md#merge-conflict) when you try to undo.

<!-- no toc -->
- Method 1: [Undo commits using the `VS Code Terminal`](#undo-commits-using-the-vs-code-terminal)
- Method 2: [Undo commits using `GitLens`](#undo-commits-using-gitlens)

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
