# Environments

<h2>Table of contents</h2>

- [What is environment](#what-is-environment)
- [Environment variables](#environment-variables)
- [Common environment variables](#common-environment-variables)
  - [`PATH` environment variable](#path-environment-variable)
- [`.env` file](#env-file)
- [Secrets](#secrets)
  - [Unencrypted secrets](#unencrypted-secrets)
  - [Unencrypted secrets in the repo](#unencrypted-secrets-in-the-repo)
  - [Store encrypted secrets in the repo](#store-encrypted-secrets-in-the-repo)
  - [Add files containing secrets to `.gitignore`](#add-files-containing-secrets-to-gitignore)
- [Deployment environments](#deployment-environments)
  - [Development environment](#development-environment)
  - [Integration environment](#integration-environment)
  - [Staging environment](#staging-environment)
  - [Production environment](#production-environment)

## What is environment

## Environment variables

Environment variables are named values that are available to a program running in a particular [deployment environment](#deployment-environments).

Look at the environment variables available to the `VS Code Terminal`:

1. [Run using the `VS Code Terminal`](./vs-code.md#run-a-command-using-the-vs-code-terminal):

   ```terminal
   env
   ```

2. You should see a list of environment variables in the `<env-variable-name>=<env-variable-value>` format.

## Common environment variables

These [environment variables](#environment-variables) are available in most [operating systems](./operating-system.md#what-is-an-operating-system):

- [`PATH`](#path-environment-variable)

### `PATH` environment variable

`PATH` contains a list of [directories](./file-system.md#directory) separated by `:`. When you run a command in the [terminal](./vs-code.md#vs-code-terminal), the system looks for the [program](./operating-system.md#program) in each directory listed in `PATH`, from left to right.

1. [Check the current shell in the `VS Code Terminal`](./vs-code.md#check-the-current-shell-in-the-vs-code-terminal).
2. [Run using the `VS Code Terminal`](./vs-code.md#run-a-command-using-the-vs-code-terminal):

   ```terminal
   echo $PATH
   ```

3. You should see a list of directories separated by `:`.

## `.env` file

We call `.env` file a file that contains a list of [environment variables](#environment-variables) in the `<env-variable-name>=<env-variable-value>` format.

Examples:

- [.env.example](../.env.example)
- [.env.docker.example](../.env.docker.example)

Docs:

- [Security - `.env`](https://www.dotenv.org/docs/security/env.html)

## Secrets

Secrets are values that only specific people may know such as passwords, personal tokens, private keys, etc.

Secrets are sometimes stored in [`.env` files](#env-file).

### Unencrypted secrets

Unencrypted secrets are secrets that can be used as-is.

For example, a password can be copied to enter a site.

### Unencrypted secrets in the repo

Don't store unencrypted secrets in the repo.

Don't store in the repo files (e.g., [`.env` files](#env-file)) that contain unencrypted secrets.

If you add files containing secrets to the repo, bad people may steal the secrets from your repo and hack your app.

Therefore, you should use any of these methods:

<!-- no toc -->
- [Store encrypted secrets in the repo](#store-encrypted-secrets-in-the-repo)
- [Add files containing secrets to `.gitignore`](#add-files-containing-secrets-to-gitignore)

### Store encrypted secrets in the repo

If you want to store secrets in the repo, encrypt them first using a [tool](https://github.com/inno-se/the-guide?tab=readme-ov-file#secrets).

Then, you can commit the file containing the secrets.

### Add files containing secrets to `.gitignore`

Match in [`.gitignore`](./git.md#gitignore) all files that can contain [unencrypted secrets](#unencrypted-secrets-in-the-repo) so that these secrets don't get added to the repo.

## Deployment environments

A program can run in multiple [deployment environments](https://github.com/inno-se/the-guide?tab=readme-ov-file#environments).

Each development environment may need a specific set of [environment variables](#environment-variables). This set can be different for each environment.

### Development environment

### Integration environment

### Staging environment

### Production environment
