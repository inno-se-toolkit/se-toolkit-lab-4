# Shell

<h2>Table of contents</h2>

The `shell` is a program that reads your commands and runs them.

## Shell variants

### `bash`

`bash` is the most common shell in learning materials and server docs.

> [!NOTE]
> On `Windows`, you can run `bash` commands using one of the following options:
>
> - Using the `Git Bash`.
> - Using the `WSL`.

### `Git Bash` (`Windows`)

`Git Bash` is a terminal shipped with `Git for Windows`.
It provides a Unix-like shell environment on Windows.

### `zsh`

`zsh` is the default shell on modern `macOS` and is also common on Linux.
Most `bash` commands in this course work in `zsh` as well.

## Path

A path points to a location in the filesystem.

### Absolute path

Starts from [root](#root-) or [home](#home-).

Examples:

1. `/home`
2. `/nix/store`

### Relative path

Starts from the current directory.

Examples:

- `src/app`
- `./docs`

### Root (`/`)

[Absolute path](#absolute-path) for the root of the file system.

### Home (`~`)

Shortcut for the [absolute path](#absolute-path) for the [user](./linux.md#users) home directory.

### Parent directory (`..`)

[Relative path](#relative-path) for the parent of the file or a directory.

Examples:

- For the file `parent/child/file.md`, the parent directory is `parent/child`.
- For the directory `parent/child`, the parent directory is `parent`.

## `<file-path>`

A [path](#path) to a file.

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
