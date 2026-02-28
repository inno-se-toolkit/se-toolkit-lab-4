# `Linux`

<h2>Table of contents</h2>

- [What is `Linux`](#what-is-linux)
- [Linux distro](#linux-distro)
  - [`Ubuntu`](#ubuntu)
  - [`ArchLinux`](#archlinux)
  - [`NixOS`](#nixos)
  - [`CachyOS`](#cachyos)
- [Program](#program)
  - [Useful programs](#useful-programs)
- [Process](#process)
  - [PID](#pid)
- [Groups](#groups)
- [Users](#users)
  - [The `root` user](#the-root-user)
  - [Get my current user](#get-my-current-user)
  - [Create a non-root user](#create-a-non-root-user)
- [Permissions](#permissions)
  - [The `sudo` command](#the-sudo-command)
- [Inspect ports](#inspect-ports)
  - [See listening TCP ports](#see-listening-tcp-ports)
  - [Inspect a specific port](#inspect-a-specific-port)
- [Service](#service)
- [Troubleshooting](#troubleshooting)
  - [Service is running but a request fails](#service-is-running-but-a-request-fails)

## What is `Linux`

`Linux` is a family of [operating systems](./operating-system.md) commonly used for servers and [virtual machines](./vm.md).

## Linux distro

A `Linux` distro (distribution) is a complete operating system built around the `Linux` kernel, bundled with a package manager, system tools, and default software chosen by its maintainers.

Different distros make different trade-offs between stability and freshness, ease of use and control, and general-purpose vs. specialized use cases.

### `Ubuntu`

`Ubuntu` is a widely used Debian-based `Linux` distro with long-term support (LTS) releases, commonly chosen for servers, cloud VMs, and developer workstations.

Docs:

- [Ubuntu documentation](https://help.ubuntu.com/)

### `ArchLinux`

`ArchLinux` is a minimal, rolling-release `Linux` distro that gives users full control over what gets installed, with packages updated continuously as new versions are released.

Docs:

- [ArchWiki](https://wiki.archlinux.org/)

### `NixOS`

`NixOS` is a `Linux` distro whose entire system configuration — packages, services, and settings — is declared in a single reproducible configuration file using the `Nix` package manager.

`NixOS` has one of the largest package repositories of any `Linux` distro — see [repository statistics](https://repology.org/repositories/statistics/total).

Docs:

- [NixOS documentation](https://nixos.org/learn/)

### `CachyOS`

`CachyOS` is an `ArchLinux`-based distro focused on performance, shipping with optimized kernels and packages compiled with advanced CPU-specific instruction sets.

Docs:

- [CachyOS documentation](https://wiki.cachyos.org/)

## Program

A program is an executable file containing instructions that can be run by the operating system.

It's a static entity stored on disk that becomes a [process](#process) when executed.

Programs can be compiled binaries, scripts, or other executable files that perform specific tasks when run by a user or system.

### Useful programs

See [Useful programs](./useful-programs.md).

## Process

A process is an instance of a running [program](#program).

When you execute a program, the [operating system](./operating-system.md) creates a process that contains the program's code, memory space, variables, and system resources. Each process has a unique process ID (PID) and runs independently of other processes.

Processes can be created, managed, and terminated using various [shell commands](./shell.md#shell-command).

They form the basis of multitasking in the operating system.

### PID

A PID (Process ID) is a unique numerical identifier assigned by the operating system to each running process. PIDs help the operating system to track and manage individual processes.

PIDs are used by various system commands to interact with specific processes, such as terminating them, checking their status, or monitoring their resource usage.

PIDs let the operating system handle multitasking.

## Groups

A group is a collection of [users](#users) that share the same access permissions to [files](./file-system.md#file) and [directories](./file-system.md#directory).

Groups allow an administrator to manage permissions for multiple users at once: adding a user to a group grants them all the group's permissions.

Each user has a primary group and can belong to additional supplementary groups.

## Users

Servers and VMs usually run multiple users.

### The `root` user

`root` is the administrator user.

### Get my current user

1. [Run using the `VS Code Terminal`](./vs-code.md#run-a-command-using-the-vs-code-terminal):

    ```terminal
    whoami
    ```

### Create a non-root user

`root` is useful for initial setup, but daily work should be done with a regular user.

For `Ubuntu`/`Debian` systems:

1. Create a new user:

   ```terminal
   sudo adduser <username>
   ```

2. Allow the user to run administrative commands:

   ```terminal
   sudo usermod -aG sudo <username>
   ```

3. Switch to that user:

    ```terminal
    su - <username>
    ```

4. Verify:

    ```terminal
    whoami
    id
    ```

If you plan to log in via `SSH` as that user, copy `authorized_keys` to the new user's home and fix permissions before logging out from `root`.

## Permissions

### The `sudo` command

`sudo` runs a command with elevated permissions.

```terminal
sudo <command>
```

## Inspect ports

Use the following commands to inspect [ports](./computer-networks.md#port) on a [host](./computer-networks.md#host).

- [See listening TCP ports](#see-listening-tcp-ports)
- [Inspect a specific port](#inspect-a-specific-port)

### See listening TCP ports

```terminal
ss -ltn
```

### Inspect a specific port

```terminal
ss -ltn 'sport = :42000'
```

## Service

A service is a long-running [process](#process) that performs specific system functions or provides functionality to other processes and applications.

Services typically start automatically during system boot and run in the background without direct user interaction. They can be managed using system service managers like `systemd`, `init`, or service scripts.

Common examples include [web servers](./web-development.md), [database servers](./database.md#database-server) (`MySQL`/`PostgreSQL`), [SSH daemons](./ssh.md#ssh-daemon), and network services.

Services often [listen on specific ports](./computer-networks.md#listen-on-a-port) to handle incoming requests.

They form the backbone of system functionality and network communications.

## Troubleshooting

### Service is running but a request fails

Verify both:

1. The process is listening on the expected port.
2. You are using the correct host and port in your request.
