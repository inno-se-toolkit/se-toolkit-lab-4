# File system

<h2>Table of contents</h2>

- [What is a file system](#what-is-a-file-system)
- [File](#file)
  - [File name](#file-name)
  - [Extension](#extension)
  - [Location](#location)
- [Directory](#directory)
- [Path](#path)
  - [Absolute path](#absolute-path)
  - [Relative path](#relative-path)
- [Special paths](#special-paths)
  - [Root directory (`/`)](#root-directory-)
  - [Home directory (`~`)](#home-directory-)
  - [Parent directory (`..`)](#parent-directory-)
  - [`Desktop` directory](#desktop-directory)
  - [`<file-path>`](#file-path)

## What is a file system

A file system is the method an [operating system](./operating-system.md) uses to organize and store data on a storage device.

It defines how [files](#file) are named, stored, and retrieved.

Docs:

- [File system (Wikipedia)](https://en.wikipedia.org/wiki/File_system)

## File

A file is a named collection of data stored on the [file system](#what-is-a-file-system).
Files contain data such as text, code, images, or other content.

### File name

The file name identifies the file within its [directory](#directory).

Example: `README.md` has the file name `README.md`.

### Extension

The extension is the suffix after the last `.` in the file name.
It indicates the file type or [format](./file-formats.md).

Example: `README.md` has the extension `.md`.

### Location

The location of a file is the [path](#path) to its containing [directory](#directory).

Example: for the file `/home/user/project/README.md`, the location is `/home/user/project`.

## Directory

A directory (a.k.a. "folder" on `Windows`) is a special type of file that contains other files and directories.
Directories are nested inside one another, forming a tree structure rooted at the [root directory](#root-directory-).

## Path

A path points to a location in the filesystem.

### Absolute path

Starts from the [root directory](#root-directory-) or the [home directory](#home-directory-).

Examples:

1. `/home/inno-se-toolkit/Desktop` (`Linux` / `macOS`)
2. `C:\Users\inno-se-toolkit\Desktop` (`Windows`)

### Relative path

Starts from the current directory.

Examples:

- `src/app`
- `./docs`

## Special paths

### Root directory (`/`)

The root directory is the top-level [directory](#directory) of the file system.
All other files and directories are contained within it.
Its [absolute path](#absolute-path) is `/`.

### Home directory (`~`)

Shortcut for the [absolute path](#absolute-path) for the [user](./linux.md#users) home directory.

### Parent directory (`..`)

[Relative path](#relative-path) for the parent of the file or a directory.

Examples:

- For the file `parent/child/file.md`, the parent directory is `parent/child`.
- For the directory `parent/child`, the parent directory is `parent`.

### `Desktop` directory

The `Desktop` directory is the folder that corresponds to the desktop on your screen.

`Windows`: `C:\Users\<username>\Desktop`
`Linux`: `~/Desktop` (see [home directory (`~`)](#home-directory-))

### `<file-path>`

We use `<file-path>` in docs to refer to the [path](#path) of a file.
