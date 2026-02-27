# `Python`

<h2>Table of contents</h2>

- [What is `Python`](#what-is-python)
- [Syntax](#syntax)
  - [Code blocks](#code-blocks)
  - [Documentation](#documentation)
  - [Docstring](#docstring)
- [`uv`](#uv)
  - [Install `uv`](#install-uv)
- [Set up `Python` in `VS Code`](#set-up-python-in-vs-code)
  - [Install `Python` and dependencies](#install-python-and-dependencies)
  - [Check that `Python` works](#check-that-python-works)
  - [Select the `Python` interpreter](#select-the-python-interpreter)
  - [Check that the language server works](#check-that-the-language-server-works)
- [Testing](#testing)
  - [`pytest`](#pytest)
  - [The `assert` statement](#the-assert-statement)
- [`Pylance`](#pylance)

## What is `Python`

`Python` is a general-purpose programming language. In this project, it is used to build the backend web server with [`FastAPI`](https://fastapi.tiangolo.com/).

Docs:

- [Python documentation](https://docs.python.org/3/)
- [Learn Python in Y minutes](https://learnxinyminutes.com/python/)

## Syntax

### Code blocks

`Python` uses indentation (spaces) to define code blocks instead of curly braces `{}`.

### Documentation

`Python` supports writing inline documentation as [docstrings](#docstring) embedded directly in source code.

### Docstring

A docstring is a string literal that appears as the first statement in a function, class, or module. It describes what the code does.

Docs:

- [PEP 257 – Docstring Conventions](https://peps.python.org/pep-0257/)

Example:

```python
def greet(name):
    """Return a greeting message for the given name."""
    return f"Hello, {name}!"
```

## `uv`

`uv` is a modern package manager for [`Python`](#what-is-python).

### Install `uv`

1. [Check the current shell in the `VS Code Terminal`](./vs-code.md#check-the-current-shell-in-the-vs-code-terminal).
1. Follow the [installation instructions](https://docs.astral.sh/uv/getting-started/installation/) for `macOS and Linux`, even if you use `Windows`.

## Set up `Python` in `VS Code`

Complete these steps:

1. [Install `Python` and dependencies](#install-python-and-dependencies).
2. [Check that `Python` works](#check-that-python-works).
3. [Select the `Python` interpreter](#select-the-python-interpreter).

### Install `Python` and dependencies

1. [Open in `VS Code` the project directory](./vs-code.md#open-the-directory).
2. [Run using the `VS Code Terminal`](./vs-code.md#run-a-command-using-the-vs-code-terminal):

   ```terminal
   uv sync
   ```

   This command automatically downloads the correct `Python` version, creates the `.venv` virtual environment, and installs all dependencies.

3. The output should be similar to this:

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
> This directory is managed by [`uv`](#uv). You don't need to edit files in this directory manually.

### Check that `Python` works

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
> The [`Python`](#what-is-python) version for this project is specified in the [`pyproject.toml`](../pyproject.toml) file using the `requires-python` setting.

### Select the `Python` interpreter

1. [Run using the `Command Palette`](./vs-code.md#run-a-command-using-the-command-palette):
   `Python: Select Interpreter`.
2. Click `Recommended` to select the interpreter in `./.venv/bin/python`.
3. [Check that the language server works](#check-that-the-language-server-works).

### Check that the language server works

> [!NOTE]
> See [`Pylance`](#pylance).

1. [Open the file](./vs-code.md#open-the-file):
   [`backend/app/main.py`](../backend/app/main.py).
2. Hover over the `add_middleware` method.

   You should see its type:

   <img alt="Type on hover" src="./images/python/type-on-hover.png" style="width:300px">

## Testing

### `pytest`

`pytest` is a testing framework for `Python`. It discovers and runs test functions automatically.

To run all tests, [run using the `VS Code Terminal`](./vs-code.md#run-a-command-using-the-vs-code-terminal):

```terminal
uv run pytest
```

Docs:

- [`pytest` documentation](https://docs.pytest.org/)

### The `assert` statement

The `assert` statement checks that a condition is true. If the condition is false, the test fails with an `AssertionError`.

```python
assert result == expected
```

Docs:

- [`assert` statement](https://docs.python.org/3/reference/simple_stmts.html#the-assert-statement)

## `Pylance`

A [language server](./vs-code.md#language-server) for `Python` that provides static analysis features such as type checking and detection of undefined variables.
