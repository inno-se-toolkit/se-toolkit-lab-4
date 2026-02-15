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
- [Host](#host)
- [Port](#port)
  - [Port number](#port-number)
  - [System port](#system-port)
  - [User port](#user-port)
  - [Listen on a port](#listen-on-a-port)
  - [Inspect ports](#inspect-ports)
    - [See listening TCP ports](#see-listening-tcp-ports)
    - [Inspect a specific port](#inspect-a-specific-port)
  - [Service](#service)
- [Troubleshooting](#troubleshooting)
  - [Service is running but a request fails](#service-is-running-but-a-request-fails)

## What is `Linux`

`Linux` is a family of [operating systems](./operating-system.md) commonly used for servers and [virtual machines](./vm.md).

## Linux distro

### `Ubuntu`

### `ArchLinux`

### `NixOS`

### `CachyOS`

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

## Host

<!-- TODO -->

## Port

A [*network port*](https://en.wikipedia.org/wiki/Port_(computer_networking)) (or simply *port*) is a [numbered](#port-number) communication endpoint on a [host](#host).

> [!NOTE]
> `Windows` and `macOS` also have ports.

### Port number

A port number is a numerical identifier used in networking to distinguish between different [processes](#process) running on a single [host](#host).

Only one process can bind to a specific port number on a given network interface.

### System port

The port numbers in the range from 0 to 1023 are the **well-known ports** or **system ports**.
They are used by system processes that provide widely used types of network services.
[[source](https://en.wikipedia.org/wiki/List_of_TCP_and_UDP_port_numbers#Well-known_ports)]

### User port

A **user port** (or **registered port**) is a [network port](#port) designated for use with a certain protocol or application.
[[source](https://en.wikipedia.org/wiki/Registered_port)]

### Listen on a port

When a [process](#process) "listens on a port", it means the process has bound itself to a specific network port number and is waiting for incoming network connections on that port.

The [operating system](./operating-system.md) allocates the port to that process, and any incoming network traffic directed to that port will be handled by the listening process.

This is how [services](#service) like [web servers](./web-development.md), [SSH daemons](./ssh.md#ssh-daemon), or [databases](./database.md) accept connections from clients. A port can only be listened to by one process at a time.

### Inspect ports

- [See listening TCP ports](#see-listening-tcp-ports)
- [Inspect a specific port](#inspect-a-specific-port)

#### See listening TCP ports

```terminal
ss -ltn
```

#### Inspect a specific port

```terminal
ss -ltn 'sport = :42000'
```

### Service

A service is a long-running [process](#process) that performs specific system functions or provides functionality to other processes and applications.

Services typically start automatically during system boot and run in the background without direct user interaction. They can be managed using system service managers like `systemd`, `init`, or service scripts.

Common examples include [web servers](./web-development.md), [database servers](./database.md#database-server) (`MySQL`/`PostgreSQL`), [SSH daemons](./ssh.md#ssh-daemon), and network services.

Services often listen on specific ports to handle incoming requests.

They form the backbone of system functionality and network communications.

## Troubleshooting

### Service is running but a request fails

Verify both:

1. The process is listening on the expected port.
2. You are using the correct host and port in your request.
