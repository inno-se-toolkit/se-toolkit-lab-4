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

A `path` points to a location in the filesystem.

- Absolute path: starts from root, for example `/home/user/project`.
- Relative path: starts from current directory, for example `src/app`.
- Home shortcut: `~` means your home directory.

### Current working directory

The current working directory is the directory where commands run by default.

Show the current working directory:

```terminal
pwd
```

Navigate directories:

```terminal
cd /absolute/path
cd relative/path
cd ~
cd ..
```

List files in the current working directory:

```terminal
ls
```

When a command fails with "No such file or directory", verify your current directory first using `pwd`.
