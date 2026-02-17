# `Python`

<h2>Table of contents</h2>

- [Package managers](#package-managers)
  - [`uv`](#uv)
    - [Install `uv`](#install-uv)
    - [Install `Python` and dependencies](#install-python-and-dependencies)
- [Select the `Python` interpreter](#select-the-python-interpreter)
- [Check that `Python` works](#check-that-python-works)
- [Testing](#testing)

## Syntax

## Documentation

### Docstring

## Package managers

### `uv`

`uv` is a modern package manager for `Python`.

#### Install `uv`

1. Follow the [installation instructions](https://docs.astral.sh/uv/getting-started/installation/).

   If you use `Windows`, follow the instructions for `Linux`.

#### Install `Python` and dependencies

1. [Run using the `VS Code Terminal`](./vs-code.md#run-a-command-using-the-vs-code-terminal):

   ```terminal
   uv sync
   ```

   This command automatically downloads the correct `Python` version, creates the `.venv` virtual environment, and installs all dependencies.

2. The output should be similar to this:

   ```terminal
   Using CPython 3.14.2
   Creating virtual environment at: .venv
   Resolved 36 packages in 0.77ms
   Installed 36 packages in 217ms
   ```

> [!NOTE]
> The `.venv` directory contains the virtual environment.
> That is, files and dependencies that are necessary to run the web server and other tools.
>
> This directory is managed by `uv`. You don't need to edit files in this directory manually.

## Select the `Python` interpreter

1. [Run using the `Command Palette`](./vs-code.md#run-a-command-using-the-command-palette):
   `Python: Select Interpreter`.
2. Click `Recommended` to select the interpreter in `./.venv/bin/python`.

## Check that `Python` works

1. [Open a new `VS Code Terminal`](./vs-code.md#open-a-new-vs-code-terminal).
2. [Run using the `VS Code Terminal`](./vs-code.md#run-a-command-using-the-vs-code-terminal):

   ```terminal
   uv run python --version
   ```

3. The output should be similar to this:

   ```terminal
   Python 3.14.2
   ```

> [!NOTE]
> The `Python` version for this project is specified in the [`pyproject.toml`](../../pyproject.toml) file using the `requires-python` setting.

## Testing

### `pytest`

### The `assert` statement

## Dynamic analysis

Examples:

- [Testing](#testing)

## Static analysis

## `Pylance`

A [language server](./vs-code.md#language-server) for `Python`.
