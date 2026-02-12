# `GitHub`

<h2>Table of contents</h2>

- [The `GitHub` site](#the-github-site)
- [Create an issue](#create-an-issue)
- [Issue form](#issue-form)
- [Pull request](#pull-request)
  - [Base repo](#base-repo)
  - [Head repo](#head-repo)
  - [Base branch](#base-branch)
  - [PR branch](#pr-branch)
- [Create a PR](#create-a-pr)
  - [Open the PR editor using `GitHub`](#open-the-pr-editor-using-github)
    - [Open the PR editor using a button](#open-the-pr-editor-using-a-button)
    - [Open the PR editor using `Pull requests`](#open-the-pr-editor-using-pull-requests)
    - [Open the PR editor using the branch list](#open-the-pr-editor-using-the-branch-list)
  - [Finish creating a PR](#finish-creating-a-pr)

## The `GitHub` site

[URL](./web-development.md#url): <https://github.com>

## Create an issue

1. Go to the repo on [`GitHub`](#the-github-site).
2. Click `Issues`.

   <img alt="GitHub Issues" src="../images/appendix/github/issues.png" style="width:400px"></img>
3. Click `New Issue`.
4. Click one of the suggested [issue forms](#issue-form).
5. In the `Add a title` input field, edit the title.
6. Fill out other input fields.
7. Click `Create`.

## Issue form

A repository owner can provide [issue forms](https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/configuring-issue-templates-for-your-repository#creating-issue-forms) so that users can create issues in a given format.

Examples:

- `Lab Task` - [`.github/ISSUE_TEMPLATE/01-task.yml`](../../.github/ISSUE_TEMPLATE/01-task.yml)
- `Bug Report` - [`.github/ISSUE_TEMPLATE/01-task.yml`](../../.github/ISSUE_TEMPLATE/01-task.yml)

## Pull request

### Base repo

### Head repo

### Base branch

### PR branch

## Create a PR

Create a PR to the `<repo-name>/<branch-name>`.

Complete these steps:

- [Open the PR editor using `GitHub`](#open-the-pr-editor-using-github)
- [Finish creating a PR](#finish-creating-a-pr)

> [!TIP]
> You can also [create a PR using  `GitHub Pull Requests` extension](https://code.visualstudio.com/docs/sourcecontrol/github#_creating-pull-requests).

### Open the PR editor using `GitHub`

Methods:

<!-- no toc -->
1. [Open the PR editor using a button](#open-the-pr-editor-using-a-button)
2. [Open the PR editor using `Pull requests`](#open-the-pr-editor-using-pull-requests)
3. [Open the PR editor using the branch list](#open-the-pr-editor-using-the-branch-list)- [Finish creating a PR](#finish-creating-a-pr)

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
