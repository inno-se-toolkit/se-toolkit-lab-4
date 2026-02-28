# Networks

<h2>Table of contents</h2>

- [What is a network](#what-is-a-network)
- [Machine](#machine)
- [Internet](#internet)
- [IP address](#ip-address)
  - [IPv4](#ipv4)
  - [IPv6](#ipv6)
- [Host](#host)
  - [Hostname](#hostname)
  - [`localhost`](#localhost)
  - [Remote host](#remote-host)

## What is a network

A computer network is a group of interconnected [machines](#machine) that can communicate and share resources over wired or wireless connections.

## Machine

A machine is a physical or virtual computer.

Examples: a personal laptop, a university server, a [virtual machine](./vm.md#what-is-a-vm).

## Internet

The Internet is a global [network](#what-is-a-network) of interconnected [computer networks](#networks).

It uses standardized communication protocols (such as `TCP/IP`) to link billions of devices worldwide, enabling communication and access to information across the globe.

## IP address

An IP address (Internet Protocol address) is a numerical label assigned to each device connected to a [network](#what-is-a-network).

It identifies the device and its location in the network.

Example: `10.93.24.98` ([IPv4](#ipv4)).

### IPv4

`IPv4` (Internet Protocol version 4) uses 32-bit addresses, written as four decimal numbers separated by dots.

Example: `10.93.24.98`, `127.0.0.1`.

It supports approximately 4.3 billion unique addresses.

### IPv6

`IPv6` (Internet Protocol version 6) uses 128-bit addresses, written as eight groups of four hexadecimal digits separated by colons.

Example: `2001:db8::1`.

It was introduced to address the exhaustion of [IPv4](#ipv4) addresses and supports a vastly larger address space.

## Host

A host is any [machine](#machine) that:

- is connected to a [network](#what-is-a-network);
- has an [IP address](#ip-address).

Hosts can send and receive data over the [network](#what-is-a-network).

Examples: computers, servers, [virtual machines](./vm.md).

### Hostname

A hostname is a human-readable label assigned to a [host](#host) on a [network](#what-is-a-network).

It is used to identify the host instead of its [IP address](#ip-address).

Examples: `localhost`, `my-server`, `vm.innopolis.university`.

### `localhost`

`localhost` is a [hostname](#hostname) that refers to the current [host](#host).

It resolves to the loopback [IP address](#ip-address) `127.0.0.1`.

Connections to `localhost` never leave the host — they are handled entirely within the [operating system](./operating-system.md).

### Remote host

A remote [host](#host) is a host that is not the [local host](#localhost) — it is accessed over a [network](#what-is-a-network).

Example: [your VM](./vm.md#your-vm) you connect to via [`SSH`](./ssh.md) is a remote host.
