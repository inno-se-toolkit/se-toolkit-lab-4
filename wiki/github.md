# `GitHub`

<h2>Table of contents</h2>

- [What is `GitHub`](#what-is-github)
- [The `GitHub` site](#the-github-site)
- [`GitHub` username](#github-username)
  - [`<your-github-username>`](#your-github-username)
  - [Find `<your-github-username>`](#find-your-github-username)
- [Repository](#repository)
  - [`<repo-name>`](#repo-name)
  - [`<repo-url>`](#repo-url)
  - [`upstream`](#upstream)
  - [`origin`](#origin)
  - [Browse a repository revision](#browse-a-repository-revision)
  - [Make your repository public](#make-your-repository-public)
- [Repository owner](#repository-owner)
  - [`<repo-owner-github-username>`](#repo-owner-github-username)
- [Fork](#fork)
  - [Fork a repo](#fork-a-repo)
  - [`<your-fork-url>`](#your-fork-url)
  - [Go to your fork](#go-to-your-fork)
- [Issue](#issue)
  - [Issue elements](#issue-elements)
  - [Who can create issues](#who-can-create-issues)
  - [Issue form](#issue-form)
  - [Create an issue](#create-an-issue)
- [Pull request](#pull-request)
  - [Base repository](#base-repository)
  - [Head repository](#head-repository)
  - [Default branch](#default-branch)
  - [Base branch](#base-branch)
  - [Compare branch](#compare-branch)
    - [`<compare-branch-name>`](#compare-branch-name)
- [Create a pull request in your fork](#create-a-pull-request-in-your-fork)
  - [Open the PR editor using `GitHub`](#open-the-pr-editor-using-github)
    - [Open the PR editor using a button](#open-the-pr-editor-using-a-button)
    - [Open the PR editor using `Pull requests`](#open-the-pr-editor-using-pull-requests)
    - [Open the PR editor using the branch list](#open-the-pr-editor-using-the-branch-list)
  - [Finish creating a PR](#finish-creating-a-pr)
- [Label](#label)
  - [Create a label](#create-a-label)
  - [Add a label to issues](#add-a-label-to-issues)
  - [See all issues with a label](#see-all-issues-with-a-label)
- [Settings](#settings)
  - [Enable issues](#enable-issues)
  - [Add a collaborator](#add-a-collaborator)
  - [Protect a branch](#protect-a-branch)
- [Personal access token (PAT)](#personal-access-token-pat)
  - [Create a PAT (classic)](#create-a-pat-classic)
- [`GitHub flow`](#github-flow)
- [`GitHub Projects`](#github-projects)
- [`GitHub Actions`](#github-actions)
- [Secrets](#secrets)
  - [Add a secret](#add-a-secret)
- [File preview](#file-preview)
  - [`Markdown` file preview](#markdown-file-preview)
    - [Copy code block](#copy-code-block)

## What is `GitHub`

## The `GitHub` site

The `GitHub` site has this [URL](./web-development.md#url): <https://github.com>.

## `GitHub` username

A `GitHub` username is a unique identifier of a user or an organization on [the `GitHub` site](#the-github-site).

Example of a username: `inno-se-toolkit`.

Note that this username doesn't include `@`.

### `<your-github-username>`

Assume `<your-github-username>` is your [`GitHub` username](#github-username).

`<your-github-username>` doesn't include `@`.

### Find `<your-github-username>`

1. Go to the [`GitHub` site](#the-github-site).
2. Sign in if necessary.
3. You'll see your username in the top left corner.

## Repository

A repository (or "repo") is a storage location for files that are version-controlled using [`Git`](./git.md#what-is-git).

A `GitHub` repository contains not only project files but also additional collaborative features such as [issues](#issue) for tracking bugs and tasks, [pull requests](#pull-request) for code review and merging changes, and [Projects](#github-projects) for organizing work.

### `<repo-name>`

A [repository](#repository) name.

The name must be unique among repositories of the [repository owner](#repository-owner).

### `<repo-url>`

We use `<repo-url>` to refer to a repository [URL](./web-development.md#url).

A repository URL is typically `https://github.com/<repo-owner-github-username>/<repo-name>`.
Placeholder values:

- See [`<repo-owner-github-username>`](#repo-owner-github-username).
- `<repo-name>` is the name of the repository.

### `upstream`

In [`Git`](./git.md#what-is-git), `upstream` is the conventional name for the [remote](./git.md#remote) that points to the original [repository](#repository) that was [forked](#fork).

### `origin`

In [`Git`](./git.md#what-is-git), `origin` is the conventional name for the [remote](./git.md#remote) that points to your own copy of the [repository](#repository) — typically [your fork](#fork).

For example, if your fork [URL](./web-development.md#url) is [`<your-fork-url>`](#your-fork-url), then `origin` points to that URL.

You can verify which URLs `origin` and `upstream` point to by [inspecting remotes](./gitlens.md#inspect-remotes).

### Browse a repository revision

You can browse a repository at a particular [revision](./git.md#revision): `<repo-url>/tree/<revision>`.

- See [`<repo-url>`](#repo-url).
- Replace the `<revision>` at the end of the [URL](./web-development.md#url) with an actual [revision](./git.md#revision).

Example: <https://github.com/nixos/nixpkgs/tree/26eaeac4e409d7b5a6bf6f90a2a2dc223c78d915>

### Make your repository public

1. If you don't see `Public` near your repo name, [make your repo public](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/managing-repository-settings/setting-repository-visibility#changing-a-repositorys-visibility).

## Repository owner

Repository owner is an account where the repo is currently stored.

### `<repo-owner-github-username>`

[`GitHub` username](#github-username) of the [repository owner](#repository-owner).

## Fork

A fork is a copy of an original project repository on `GitHub` that allows you to freely experiment with changes without affecting the original project repository.

When you fork a repository on `GitHub`, you create a personal copy under your `GitHub` account where you can make modifications, test features, and propose changes back to the original repository through [pull requests](#pull-request).

### Fork a repo

1. Go to `GitHub`.
2. Go to the repo that you want to fork.
3. Click `Fork`.
   1. Click `Choose an owner`.
   2. Click `<your-github-username>` to make you the repo owner.
   3. Click `Create fork`.

### `<your-fork-url>`

Assume the [URL](./web-development.md#url) of the [repo that you forked](#fork-a-repo) is `https://github.com/<repo-owner-github-username>/<repo-name>`.

Then, your fork URL should look like `https://github.com/<your-github-username>/<repo-name>`.

We'll refer to this URL as `<your-fork-url>`.

See also:

- [`<your-github-username>`](#your-github-username)
- [`<repo-name>`](#repo-name).

### Go to your fork

1. Open [`<your-fork-url>`](#your-fork-url) in a browser.

## Issue

A `GitHub` issue is a unit of work or discussion related to a `GitHub` [repository](#repository).

Issues are used to track tasks, bugs, enhancements, feature requests, and other activities related to a project.

They serve as a centralized place for collaboration and communication around specific topics or work items.

### Issue elements

- A descriptive title that summarizes the topic
- A detailed description explaining the problem, task, or idea
- Labels to categorize and prioritize the issue
- Assignees who are responsible for addressing the issue
- Comments for ongoing discussion and updates
- Milestones to group related issues together
- Reactions (like 👍, 👎) to gauge community sentiment

### Who can create issues

Issues can be created by repository collaborators or by anyone with access to the repository (if the repository allows public issues).

They are an essential part of the [`GitHub flow`](#github-flow), allowing teams to plan, discuss, and track work effectively.

### Issue form

A repository owner can [provide issue forms](https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/configuring-issue-templates-for-your-repository#creating-issue-forms) so that users are forced to create issues in a given format.

Examples of issue forms:

- `Lab Task` defined in [`.github/ISSUE_TEMPLATE/01-task.yml`](../.github/ISSUE_TEMPLATE/01-task.yml)
- `Bug Report` defined in [`.github/ISSUE_TEMPLATE/01-task.yml`](../.github/ISSUE_TEMPLATE/01-task.yml)

### Create an issue

1. Go to [`GitHub`](#the-github-site).
2. Go to the repo where you want to create an issue.
3. Click `Issues`.

   <img alt="GitHub Issues" src="./images/github/issues.png" style="width:400px"></img>
4. Click `New Issue`.
5. Click one of the suggested [issue forms](#issue-form).
6. In the `Add a title` input field, edit the title.
7. Fill out other input fields.
8. Click `Create`.

## Pull request

### Base repository

The base repository is the [repository](#repository) into which the changes are merged.

When creating a [pull request](#pull-request) from a [fork](#fork), the base repository can be the fork itself or the [upstream](#upstream) repository that was forked.

### Head repository

The head repository is the [repository](#repository) that contains the changes you want to merge.

When creating a [pull request](#pull-request) from a [fork](#fork) for the cours e labs, the head repository is your fork, not the upstream repostory.

### Default branch

The default branch is the primary branch of a [repository](#repository), typically named `main`.

New [pull requests](#pull-request) and code merges target the default branch by default.

### Base branch

The base branch is the branch in the [base repository](#base-repository) that you want to merge your changes into.

### Compare branch

The compare branch (also called the pull request branch or head branch) is the branch that contains the changes you want to merge into the [base branch](#base-branch).

#### `<compare-branch-name>`

A placeholder for the name of the [compare branch](#compare-branch).

## Create a pull request in your fork

1. [Open the PR editor using `GitHub`](#open-the-pr-editor-using-github)
2. [Finish creating a PR](#finish-creating-a-pr)

<!-- TODO explain better
> [!TIP]
> You can also [create a PR using  `GitHub Pull Requests` extension](https://code.visualstudio.com/docs/sourcecontrol/github#_creating-pull-requests).
-->

### Open the PR editor using `GitHub`

- Method 1: [Open the PR editor using a button](#open-the-pr-editor-using-a-button)
- Method 2: [Open the PR editor using `Pull requests`](#open-the-pr-editor-using-pull-requests)
- Method 3: [Open the PR editor using the branch list](#open-the-pr-editor-using-the-branch-list)- [Finish creating a PR](#finish-creating-a-pr)

#### Open the PR editor using a button

1. [Go to your fork](#go-to-your-fork).
2. If you see the `Compare & pull request` button, click it.

   Otherwise, [open the PR editor using another method](#open-the-pr-editor-using-github).

#### Open the PR editor using `Pull requests`

1. [Go to your fork](#go-to-your-fork).
2. Click `Pull requests`.
3. Click `New pull request`.
4. Select your fork as the [base repository](#base-repository):
   1. Click `base repository: <repo-owner-github-username>/<repo-name>`.
   2. In `Filter repos`, write `<your-github-username>`.
   3. Click `<your-github-username>/<repo-name>` to select your fork.
5. Select `main` as the [base branch](#base-branch):
   1. Click `base: <branch-name>`.
   2. In `Find a branch`, write `main`.
   3. Click `main` in the list.
6. Select `<compare-branch-name>` as the [compare branch](#compare-branch):
   1. Click `compare: main`.
   2. In `Find a branch`, write [`<compare-branch-name>`](#compare-branch-name).
   3. Click the `<compare-branch-name>` in the list.
7. Click `Create pull request`.

#### Open the PR editor using the branch list

1. [Go to your fork](#go-to-your-fork).
2. Click `main` under the repo name to view all branches.
3. Click `<branch-name>` that you want to use for PR.
4. You'll see the `Contribute` button if the branch has commits that aren't yet in the `main` branch.
5. Click `Contribute`.
6. Click `Open pull request`.

### Finish creating a PR

1. Write the PR title.
2. Write the PR description.
3. [Link the PR](https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/linking-a-pull-request-to-an-issue#linking-a-pull-request-to-an-issue-using-a-keyword) to the issue, e.g. `Closes #<issue-number>`.

   **Note:** linking an issue works only for PRs that have the repo [default branch](#default-branch) as the [base branch](#base-branch).
4. Check the boxes under the PR description.
5. Click `Create pull request`.

## Label

A [label](https://docs.github.com/en/issues/using-labels-and-milestones-to-track-work/managing-labels) helps you filter and organize [issues](#issue).

### Create a label

1. [Go to your fork](#go-to-your-fork).
2. Go to `Issues` -> `Labels`.
3. Create a new label:
   1. Click `New label`.
   2. Name: `<label-name>`.
   3. Click `Create label`.

### Add a label to issues

1. [Go to your fork](#go-to-your-fork).
2. [Add](https://github.com/orgs/community/discussions/53473#discussioncomment-5697478) the `<label-name>` label to some of your issues.

### See all issues with a label

1. [Go to your fork](#go-to-your-fork).
2. Go to `Issues`.
3. If you don't see any `Open` issues, click `Closed`.
4. Filter issues by the label:
   1. Click `Labels`.
   2. In the `Filter labels` input area, write `<label-name>`.
   3. Click the suggested label.
5. You should see all issues that have the `<label-name>` label.

## Settings

### Enable issues

1. [Go to your fork](#go-to-your-fork).
2. Go to `Settings` -> `General` -> `Features`.
3. Check the box near `Issues`.
4. [Go to your fork](#go-to-your-fork).

   You should see the `Issues` tab.
   Example:

   <img alt="GitHub Issues" src="./images/github/issues-tab.png" style="width:400px"></img>

### Add a collaborator

1. [Go to your fork](#go-to-your-fork).
2. Go to `Settings` -> `Collaborators` -> `Add people`.
3. Add the person as a collaborator.
4. Make sure the collaborator has accepted the invitation sent to their email.

### Protect a branch

1. [Go to your fork](#go-to-your-fork).
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

## Personal access token (PAT)

<!-- TODO explain -->

### Create a PAT (classic)

1. Open in a browser <https://github.com/>.
2. Click your profile icon in the top right corner.
3. Click `Settings`.
4. Scroll down until `Developer settings` in the left sidebar.
5. Click `Developer settings`.
6. Click `Personal access tokens`.
7. Click `Tokens (classic)`.
8. Click `Generate new token`.
9. Click `Generate new token (classic)`.
10. Write a note.
11. Go to `Select scopes`.
12. Check the marks near:
    - `repo`
    - `workflow`

    <img alt="GitHub Issues" src="./images/github/pat-classic-permissions.png" style="width:400px"></img>

13. Scroll to the bottom of the page.
14. Click `Generate token`.

## `GitHub flow`

`GitHub` flow is a process for organizing the work on a repository.
It can be used both by individual developers and teams.

See [GitHub flow](https://docs.github.com/en/get-started/using-github/github-flow).

## `GitHub Projects`

<!-- TODO structure better and simplify -->

`GitHub Projects` is a project management tool integrated directly into `GitHub` that helps you plan, track, and manage your work. With `GitHub Projects`, you can create boards to organize [issues](#issue), [pull requests](#pull-request), and notes in a customizable workflow.

Key features of `GitHub Projects` include:

- **Boards**: Visual Kanban-style boards to track work items across different stages (e.g., To Do, In Progress, Done)
- **Automation**: Built-in automation rules to move items between columns based on status changes
- **Views**: Multiple view options including board, table, and roadmap views
- **Integration**: Direct integration with issues and pull requests in your repositories
- **Custom fields**: Ability to add custom fields to track additional information like priority, team, or estimates
- **Templates**: Pre-built templates for common workflows like Agile, Scrum, or basic task tracking

`GitHub Projects` can be scoped to a single repository or span multiple repositories, making it ideal for managing work across entire organizations or teams.

You can use Projects to plan sprints, track bug fixes, manage feature development, or coordinate any other collaborative work.

## `GitHub Actions`

`GitHub Actions` is a `CI/CD` platform built into `GitHub` that runs automated workflows when events happen in a [repository](#repository) — for example, on every push to `main`.

Workflows are defined as `YAML` files in `.github/workflows/`.

Docs:

- [`GitHub Actions`](https://docs.github.com/en/actions)

## Secrets

A `GitHub` secret is an encrypted environment variable stored in a [repository](#repository). Secrets are used to store sensitive values like API keys, passwords, and tokens so they are not exposed in workflow files.

Secrets are accessed in workflow files as `${{ secrets.SECRET_NAME }}`.

### Add a secret

1. [Go to your fork](#go-to-your-fork).
2. Go to `Settings` → `Secrets and variables` → `Actions`.
3. Click `New repository secret`.
4. Enter the secret name and value.
5. Click `Add secret`.

## File preview

### `Markdown` file preview

#### Copy code block

In a code block, click the copy icon to copy the block of code.

<img alt="Copy code block" src="./images/github/code-block-copy.png" style="width:100px"></img>

Code block example:

```terminal
ls .
```
