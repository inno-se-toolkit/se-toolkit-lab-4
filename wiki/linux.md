# `Linux`

<h2>Table of contents</h2>

- [What is `Linux`](#what-is-linux)
- [Linux distro](#linux-distro)
  - [`Ubuntu`](#ubuntu)
  - [`ArchLinux`](#archlinux)
  - [`NixOS`](#nixos)
  - [`CachyOS`](#cachyos)
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

## Troubleshooting

### Service is running but a request fails

Verify both:

1. The process is listening on the expected port.
2. You are using the correct host and port in your request.
