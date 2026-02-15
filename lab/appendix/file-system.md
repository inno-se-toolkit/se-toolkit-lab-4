# File system

## What is a file system

## File

## Directory

A directory (a.k.a. "folder" on `Windows`) is a special type of file.

## Path

A path points to a location in the filesystem.

### Absolute path

Starts from the [root directory](#root-directory-) or the [home directory](#home-directory-).

Examples:

1. `/home/johndoe/Desktop`
2. `/nix/store`

### Relative path

Starts from the current directory.

Examples:

- `src/app`
- `./docs`

## Special paths

### Root directory (`/`)

[Absolute path](#absolute-path) for the root of the file system.

### Home directory (`~`)

Shortcut for the [absolute path](#absolute-path) for the [user](./linux.md#users) home directory.

### Parent directory (`..`)

[Relative path](#relative-path) for the parent of the file or a directory.

Examples:

- For the file `parent/child/file.md`, the parent directory is `parent/child`.
- For the directory `parent/child`, the parent directory is `parent`.

## `Desktop` directory

`Windows`: `C:\Users\<username>\Desktop`
`Linux`: `~/Desktop` (see [home directory (`~`)](#home-directory-))

### `<file-path>`

We use `<file-path>` in docs to refer to the [path](#path) of a file.
