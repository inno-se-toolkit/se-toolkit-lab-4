# `GitHub`

<h2>Table of contents</h2>

- [`GitHub flow`](#github-flow)
- [The `GitHub` site](#the-github-site)
- [Repository](#repository)
  - [Fork](#fork)
  - [Fork a repo](#fork-a-repo)
- [Issue](#issue)
  - [Issue elements](#issue-elements)
  - [Who can create issues](#who-can-create-issues)
  - [Issue form](#issue-form)
  - [Create an issue](#create-an-issue)
- [Pull request](#pull-request)
  - [Base repo](#base-repo)
  - [Head repo](#head-repo)
  - [Base branch](#base-branch)
  - [Pull request branch](#pull-request-branch)
  - [Create a pull request](#create-a-pull-request)
  - [Open the PR editor using `GitHub`](#open-the-pr-editor-using-github)
    - [Open the PR editor using a button](#open-the-pr-editor-using-a-button)
    - [Open the PR editor using `Pull requests`](#open-the-pr-editor-using-pull-requests)
    - [Open the PR editor using the branch list](#open-the-pr-editor-using-the-branch-list)
  - [Finish creating a PR](#finish-creating-a-pr)
- [`GitHub Projects`](#github-projects)

## `GitHub flow`

`GitHub` flow is a process for organizing the work on a repository.
It can be used both by individual developers and teams.

See [GitHub flow](https://docs.github.com/en/get-started/using-github/github-flow).

## The `GitHub` site

The `GitHub` site has this [URL](./web-development.md#url): <https://github.com>.

## Repository

A repository (or "repo") is a storage location for files that are version-controlled using [`Git`](./git.md#what-is-git).

A `GitHub` repository contains not only your project files but also additional collaborative features such as [issues](#issue) for tracking bugs and tasks, [pull requests](#pull-request) for code review and merging changes, and [Projects](#github-projects) for organizing work.

### Fork

A fork is a copy of an original project repository on `GitHub` that allows you to freely experiment with changes without affecting the original project repository.

When you fork a repository on `GitHub`, you create a personal copy under your `GitHub` account where you can make modifications, test features, and propose changes back to the original repository through [pull requests](#pull-request).

### Fork a repo

1. Go to `GitHub`.
2. Go to the repo that you want to fork.
3. Click `Fork`.
   1. Click `Choose an owner`.
   2. Click `<your-username>` to make you the repo owner.
   3. Click `Create fork`.

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

- `Lab Task` defined in [`.github/ISSUE_TEMPLATE/01-task.yml`](../../.github/ISSUE_TEMPLATE/01-task.yml)
- `Bug Report` defined in [`.github/ISSUE_TEMPLATE/01-task.yml`](../../.github/ISSUE_TEMPLATE/01-task.yml)

### Create an issue

1. Go to [`GitHub`](#the-github-site).
2. Go to the repo where you want to create an issue.
3. Click `Issues`.

   <img alt="GitHub Issues" src="../images/appendix/github/issues.png" style="width:400px"></img>
4. Click `New Issue`.
5. Click one of the suggested [issue forms](#issue-form).
6. In the `Add a title` input field, edit the title.
7. Fill out other input fields.
8. Click `Create`.

## Pull request

### Base repo

### Head repo

### Base branch

### Pull request branch

### Create a pull request

Create a PR to the `<repo-name>/<branch-name>`.

Complete these steps:

- [Open the PR editor using `GitHub`](#open-the-pr-editor-using-github)
- [Finish creating a PR](#finish-creating-a-pr)

> [!TIP]
> You can also [create a PR using  `GitHub Pull Requests` extension](https://code.visualstudio.com/docs/sourcecontrol/github#_creating-pull-requests).

### Open the PR editor using `GitHub`

<!-- no toc -->
- Method 1: [Open the PR editor using a button](#open-the-pr-editor-using-a-button)
- Method 2: [Open the PR editor using `Pull requests`](#open-the-pr-editor-using-pull-requests)
- Method 3: [Open the PR editor using the branch list](#open-the-pr-editor-using-the-branch-list)- [Finish creating a PR](#finish-creating-a-pr)

#### Open the PR editor using a button

Go to your fork on `GitHub`.

If you see the `Compare & pull request` button, click it.

#### Open the PR editor using `Pull requests`

1. Go to your fork on `GitHub`.
2. Click `Pull requests`.
3. Click `New pull request`.
4. Click `base repository: <repo-owner-username>/<repo-name>`.
5. Click `<your-username>/<repo-name>` to select the [base repo](#base-repo).
6. The PR will be created in your repo.
7. Click `base: main`.
8. Click a branch to select the [base branch](#base-branch).
9. Click `compare: <branch-name>` to view all available branches.
10. Click `<branch-name>` to select the [PR branch](#pr-branch).

#### Open the PR editor using the branch list

1. Go to your repo on `GitHub`.
2. Click `main` under the repo name to view all branches.
3. Click `<branch-name>` that you want to use for PR.
4. You'll see the `Contribute` button if the branch has commits that aren't yet in `main`.
5. Click `Contribute`.
6. Click `Open pull request`.

### Finish creating a PR

1. Write the PR title.
2. Write the PR description.
3. [Link the PR](https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/linking-a-pull-request-to-an-issue#linking-a-pull-request-to-an-issue-using-a-keyword) to the issue, e.g. `Closes #<issue number>`.
4. Check the boxes under the PR description.
5. Click `Create pull request`.

<!-- TODO Click Markdown code block to copy -->

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
