# Lab setup

## Find a partner

1. Find a classmate to be your partner for this lab.
2. Sit together.

You'll complete tasks individually, but review each other's work via pull requests.

## Set up a fork

1. Create a `GitHub` account.
2. Fork this repo to your `GitHub` account and make your fork public.
3. Continue your work in the forked repo.
4. In the repo -> `Settings` -> `General` -> `Features`, enable `Issues`.

## Add a classmate as a collaborator

1. In the repo `Settings` -> `Collaborators` -> `Add people`, add your partner as a collaborator.
2. Make sure your collaborator has accepted the invitation sent to their email.

## Set up `git`

(If needed) On your computer, configure [`git`](https://git-scm.com/):

```bash
git config --global user.name "Your Name"
git config --global user.email "your@email"
```

## Set up `VS Code`

1. Install [`VS Code`](https://code.visualstudio.com/).

   We chose this editor because it has built-in AI features and many useful [extensions](./appendix/vs-code.md#extensions).

1. This is the [`Basic Layout`](./appendix/vs-code.md#basic-layout) of `VS Code`:

    ![VS Code UI](./images/vs-code-ui.png)

1. Try to [open `Terminal`](./appendix/vs-code.md#terminal).
1. Try to [open `Source Control`](./appendix/vs-code.md#source-conrol).
1. (Optional) [Learn more](../lab/appendix/vs-code.md) about `VS Code`.

## Open the repository on your computer

1. On your computer, create a directory `software-engineering-toolkit`.
2. In that directory, clone the lab repo.

    ```bash
    git clone https://github.com/<your-username>/lab-01-market-product-and-git
    ```

3. Open the repo in `VS Code`.

    ```bash
    cd software-engineering-toolkit
    code lab-01-market-product-and-git
    ```

## Set up `VS Code` extensions

1. Install the recommended `VS Code` extensions (listed in [`.vscode/extensions.json`](../.vscode/extensions.json)) when `VS Code` prompts to install them.
2. If you missed the prompt:
   1. Go to the [`Activity Bar`](./appendix/vs-code.md#activity-bar).
   2. Click the icon `Extensions`. Alternatively, press `Ctrl+Shift+X` (`Cmd+Shift+G` on `macOS`).
   3. In the input field, type `@recommended`.
   4. Look at `WORKSPACE RECOMMENDATIONS`.
   5. Click the icon `Install Workspace Recommended extensions`.
3. Sign in to accounts.
    1. Go to the [`Activity Bar`](./appendix/vs-code.md#activity-bar).
    2. Click the icon `Accounts`.
    3. Click `Sign in with GitHub ...`.
    4. Repeat for the remaining extensions if there are any.

---

## Optional enhancements to make your life easier

### Coding: Set up a coding agent

A coding agent can help you write code, explain concepts, and debug issues.

See [Coding agents](./appendix/coding-agents.md).

### Shell: Set up the prompt

Starship shows your current `git` branch, status, and other useful info directly in your terminal prompt.

Install [`Starship`](https://github.com/starship/starship#-installation).

### `VS Code`: Check `GitLens`

GitLens shows commit history, blame annotations, and branch visualization right inside `VS Code`.

#### Look at the commit graph

1. Go to the [`Status Bar`](../lab/appendix/vs-code.md#status-bar):
1. Click the icon `Visualize commits on the Commit Graph`.
1. Make sure you can see the commit graph.

#### Inspect remotes and the current branch

1. Open [`Source Control`](../lab/appendix/vs-code.md#source-control).
1. Click `GitLens` in the opened `Primary Side Bar`.
1. In the `GitLens` panel, click the icon `Remotes`.
1. Make sure `origin` points to your repo URL (hover over it an look at URLs).
1. In the `GitLens` panel, click the icon `Commits`.
1. Make sure you can see commits on the current branch.

#### (Optional) Learn more about `GitLens`

See [`GitLens` features](https://help.gitkraken.com/gitlens/gitlens-features/).

### Repo: Protect your `main` branch

Branch protection prevents accidental pushes directly to `main`.
This enforces the PR workflow and ensures all changes are reviewed.

1. Open the repo.
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

### Repo: Create a label for tasks

> [!TIP]
> If you create the `task` label before creating issues, your issues will have this label automatically as configured in the [issue form](../.github/ISSUE_TEMPLATE/01-task.yml).

[Labels](https://docs.github.com/en/issues/using-labels-and-milestones-to-track-work/managing-labels) help you filter and organize issues.

With a `task` label, you can see in one view all lab tasks that have this label.

In the repo -> `Issues` -> `Labels`, create a new label:

1. Click `New label`.
2. Name: `task`.
3. Click `Create label`.

Then [add this label](https://github.com/orgs/community/discussions/53473#discussioncomment-5697478) to some of your task issues.

Next, in the repo -> `Issues`, filter by the label:

1. Click `Labels`.
2. In the `Filter labels` input area, write `task`.
3. Click the suggested label.
4. You'll see all issues that have this label.
