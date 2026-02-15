# Shell

<h2>Table of contents</h2>

## What is shell

An [operating system](./operating-system.md) shell is a computer program that provides relatively broad and direct access to the system on which it runs.
[[source](https://en.wikipedia.org/wiki/Shell_(computing))]

### Login shell

<!-- TODO -->

## Shell variants

### `bash`

`Bash` (short for "Bourne Again SHell") is an interactive command interpreter and scripting language developed for `Unix`-like operating systems (e.g., [`Linux`](./linux.md#what-is-linux)).
[[source]]

> [!NOTE]
> `Bash` is the default login shell for `Ubuntu`.

`bash` is the most common shell in learning materials and server docs.

> [!NOTE]
> On `Windows`, you must to [open a directory in `WSL`](./vs-code.md#windows-only-open-the-directory-in-wsl) to run `bash`.

### `Git Bash` (`Windows`)

`Git Bash` is a terminal shipped with `Git for Windows`.
It provides a Unix-like shell environment on Windows.

### `zsh`

`zsh` is the default shell on modern `macOS` and is also common on Linux.
Most `bash` commands in this course work in `zsh` as well.

## Shell prompt

## Shell command

## Current working directory

The current working directory is the directory where commands run by default.

### Show the current working directory

1. [Run using the `VS Code Terminal`](./vs-code.md#run-a-command-using-the-vs-code-terminal):

   ```terminal
   pwd
   ```

### Navigate directories

1. [Run using the `VS Code Terminal`](./vs-code.md#run-a-command-using-the-vs-code-terminal):

    ```terminal
    cd /
    cd ~
    cd ..
    ```

List files in the current working directory:

```terminal
ls
```

When a command fails with "No such file or directory", verify your current directory first using `pwd`.

## Useful commands

These commands run programs:

- `pwd` - show current directory.
- `ls` - list files.
- `cd <dir>` - go to a directory.
- `cat <file-path>` - print the content of a file at the [`<file-path>`](./shell.md#file-path).

### Check what shell is running

1. [Run using the `VS Code Terminal`](./vs-code.md#run-a-command-using-the-vs-code-terminal):

    ```terminal
    echo "$SHELL"
    ```

## `Bash`

### `Bash` syntax basics

#### Run a command

```terminal
<command> <arguments>
```

Example:

```terminal
ls .
```

#### Pipe the `stdout`

```terminal
<command 1> | <command 2>
```
