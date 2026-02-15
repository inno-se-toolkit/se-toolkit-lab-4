# `Git`

<h2>Table of contents</h2>

- [What is `Git`](#what-is-git)
- [How `Git` works - text](#how-git-works---text)
- [How `Git` works - videos](#how-git-works---videos)
- [Merge conflict](#merge-conflict)
- [Practice `Git`](#practice-git)
- [`.gitignore`](#gitignore)
- [`GitHub flow`](#github-flow)
- [`Conventional Commits`](#conventional-commits)

## What is `Git`

## How `Git` works - text

- Read this [tutorial](https://hackmd.io/@aabounegm/SWP-git) to learn about `Git`, `Github`, and other `Git` workflows.

Quick mental model:

- `Working tree`: your local files.
- `Staging area`: selected changes for the next commit (`git add`).
- `Commit`: a save point of your progress since the previous save point (`git commit`).
- `Commit history`: a timeline of these save points.

Simple view:

```text
working tree changes -> git add -> git commit
                         (stage)     (save progress)
```

Useful commands:

```terminal
git status
git add <file-path>
git commit -m "docs: update appendix"
git log --oneline --decorate --graph -n 15
```

See [`<file-path>`](./shell.md#file-path).

When confused, start with `git status` and read it carefully before running the next command.

## How `Git` works - videos

- Watch videos to build your mental model of how `Git` works:
  - [Git Explained in 100 Seconds](https://www.youtube.com/watch?v=hwP7WQkmECE)
  - [What is Git? Explained in 2 Minutes!](https://www.youtube.com/watch?v=2ReR1YJrNOM)
  - [A brief introduction to Git for beginners](https://www.youtube.com/watch?v=r8jQ9hVA2qs)
  - [How Git Works: Explained in 4 Minutes](https://www.youtube.com/watch?v=e9lnsKot_SQ)
  - [Git MERGE vs REBASE: Everything You Need to Know](https://www.youtube.com/watch?v=0chZFIZLR_0)

## Merge conflict

<!-- TODO -->

## Practice `Git`

- Practice on [Learn Git Branching](https://learngitbranching.js.org/) (focus on merge/rebase and conflicts).

## `.gitignore`

The `.gitignore` file allows you to specify which files shouldn't be added to the repo.

Example: [`.gitignore`](../../.gitignore)

Common ignored files:

- Secrets (`.env.secret`, keys, tokens).
- Build artifacts (`dist/`, `build/`).
- Local caches and temporary files.

## `GitHub flow`

- Read about the [`GitHub flow`](https://docs.github.com/en/get-started/using-github/github-flow).

Typical sequence:

1. Create an issue.
2. Create a branch from `main`.
3. Commit changes to the branch.
4. Push branch and open a PR.
5. Get review and merge.

## `Conventional Commits`

- Learn about [`Conventional Commits`](https://www.conventionalcommits.org/en/v1.0.0/) for commit message formatting.

Common prefixes:

- `feat:` for new functionality.
- `fix:` for bug fixes.
- `docs:` for documentation changes.
- `refactor:` for code changes without behavior changes.
