# `Nix`

<h2>Table of contents</h2>

- [What is `Nix`](#what-is-nix)
- [`nixpkgs`](#nixpkgs)
  - [`nixpkgs` repository](#nixpkgs-repository)
    - [Browse a `nixpkgs` repository revision](#browse-a-nixpkgs-repository-revision)
  - [Search `nixpkgs`](#search-nixpkgs)
- [Set up `Nix`](#set-up-nix)
  - [Install `Nix`](#install-nix)
  - [Verify `Nix` installation](#verify-nix-installation)
  - [Install `jq`](#install-jq)
  - [Pin `nixpkgs`](#pin-nixpkgs)
  - [Install `nil`](#install-nil)
  - [Install `nixfmt`](#install-nixfmt)
- [Flake](#flake)
  - [`flake.lock`](#flakelock)
  - [Devshell](#devshell)
  - [Common flake commands](#common-flake-commands)
    - [`nix flake update`](#nix-flake-update)
- [Flake registry](#flake-registry)
  - [`nix registry pin`](#nix-registry-pin)
- [Troubleshooting](#troubleshooting)
  - [Enable `nix-daemon`](#enable-nix-daemon)
  - [Restart `nix-daemon`](#restart-nix-daemon)

## What is `Nix`

`Nix` is a cross-platform [package manager](./package-manager.md#package) that provides reproducible, isolated software [environments](./environments.md#what-is-environment).
It allows you to install [tools](./package-manager.md#tool) and [dependencies](./package-manager.md#dependency) without affecting the rest of your system.

Many of the packages are available in [`nixpkgs`](#nixpkgs).

Docs:

- [Nix documentation](https://nix.dev/)
- [Nix 2.33.3 Reference Manual](https://nix.dev/manual/nix/2.33/)
- [NixOS & Flakes Book](https://nixos-and-flakes.thiscute.world/introduction/)

## `nixpkgs`

`nixpkgs` is the official [package](./package-manager.md#package) collection for `Nix`, containing over 120,000 packages.
It is a source from which `Nix` installs [tools](./package-manager.md#tool) and [dependencies](./package-manager.md#dependency).

According to [`Repology`](https://repology.org/docs/about), `nixpkgs` contains the largest number of the newest versions of packages among `Linux` repositories (see the [comparison](https://repology.org/repositories/statistics/newest)).

Docs:

- [Nixpkgs Reference Manual](https://nixos.org/manual/nixpkgs/stable/)

### `nixpkgs` repository

`nixpkgs` on [`GitHub`](./github.md#what-is-github): <https://github.com/nixos/nixpkgs>

#### Browse a `nixpkgs` repository revision

See [Browse a repository revision](./github.md#browse-a-repository-revision):

- `<repo-url>` is <https://github.com/nixos/nixpkgs>.
- `<revision>` is a revision that you want to browse.

Example: `https://github.com/nixos/nixpkgs/tree/26eaeac4e409d7b5a6bf6f90a2a2dc223c78d915`

### Search `nixpkgs`

[Search nixpkgs](https://search.nixos.org/packages).

## Set up `Nix`

Complete these steps:

1. [Install `Nix`](#install-nix).
2. [Verify `Nix` installation](#verify-nix-installation).
3. [Install `jq`](#install-jq).
4. [Pin `nixpkgs`](#pin-nixpkgs).
5. [Install `nil`](#install-nil).
6. [Install `nixfmt`](#install-nixfmt).

### Install `Nix`

1. Install `Nix` using the [`Determinate Systems` installer](https://github.com/DeterminateSystems/nix-installer#install-determinate-nix):

   [Run using the `VS Code Terminal`](./vs-code.md#run-a-command-using-the-vs-code-terminal):

   ```terminal
   curl -fsSL https://install.determinate.systems/nix | sh -s -- install
   ```

2. Follow the prompts to complete the installation.
3. [Delete the current `VS Code Terminal`](./vs-code.md#delete-a-vs-code-terminal).
4. [Open a new `VS Code Terminal`](./vs-code.md#open-a-new-vs-code-terminal).

### Verify `Nix` installation

1. Check the version of the `nix` [program](./operating-system.md#program):

   [Run using the `VS Code Terminal`](./vs-code.md#run-a-command-using-the-vs-code-terminal):

   ```terminal
   nix --version
   ```

   The output should be similar to this:

   ```terminal
   nix (Determinate Nix 3.16.3) 2.33.3
   ```

### Install `jq`

1. Install [`jq`](./useful-programs.md#jq) from [`nixpkgs`](#nixpkgs):

   [Run using the `VS Code Terminal`](./vs-code.md#run-a-command-using-the-vs-code-terminal):

   ```terminal
   nix profile add nixpkgs#jq
   ```

### Pin `nixpkgs`

1. Get the [commit hash](./git.md#commit-hash) of the [`nixpkgs` repository](#nixpkgs-repository) specified in the [`flake.lock`](#flakelock):

   [Run using the `VS Code Terminal`](./vs-code.md#run-a-command-using-the-vs-code-terminal):

   ```terminal
   nix flake metadata --json | jq -r '.locks.nodes.nixpkgs.locked.rev'
   ```

   The output should be as follows:

   ```terminal
   26eaeac4e409d7b5a6bf6f90a2a2dc223c78d915
   ```

2. Pin `nixpkgs` in your [flake registry](#flake-registry) to the same commit hash:

   [Run using the `VS Code Terminal`](./vs-code.md#run-a-command-using-the-vs-code-terminal):

   ```terminal
   nix registry pin nixpkgs github:nixos/nixpkgs/26eaeac4e409d7b5a6bf6f90a2a2dc223c78d915
   ```

### Install `nil`

> `nil` is a [language server](./vs-code.md#language-server) for [`Nix`](#what-is-nix).

1. [Run using the `VS Code Terminal`](./vs-code.md#run-a-command-using-the-vs-code-terminal):

   ```terminal
   nix profile add nixpkgs#nil
   ```

2. Check the `nil` version:

   [Run using the `VS Code Terminal`](./vs-code.md#run-a-command-using-the-vs-code-terminal):

   ```terminal
   nil --version
   ```

   The output should be:

   ```terminal
   nil 2025-06-13
   ```

### Install `nixfmt`

> `nixfmt` is a formatter for [`Nix`](#what-is-nix).

1. [Run using the `VS Code Terminal`](./vs-code.md#run-a-command-using-the-vs-code-terminal):

   ```terminal
   nix profile add nixpkgs#nixfmt
   ```

2. Check the `nixfmt` version:

   [Run using the `VS Code Terminal`](./vs-code.md#run-a-command-using-the-vs-code-terminal):

   ```terminal
   nixfmt --version
   ```

   The output should be:

   ```terminal
   nixfmt 1.2.0
   ```

## Flake

Docs:

- [Flakes on NixOS wiki](https://wiki.nixos.org/wiki/Flakes)
- [Flakes on nix.dev](https://nix.dev/concepts/flakes.html)

### `flake.lock`

Docs:

- [Lock files](https://nix.dev/manual/nix/2.33/command-ref/new-cli/nix3-flake.html#lock-files)

Example: [`flake.lock`](../flake.lock).

### Devshell

<!-- TODO -->

### Common flake commands

#### `nix flake update`

Update the revision of inputs used in this project using the [`nix flake update`](https://nix.dev/manual/nix/2.33/command-ref/new-cli/nix3-flake-update.html) command.

## Flake registry

Docs:

- [`nix registry`](https://nix.dev/manual/nix/2.33/command-ref/new-cli/nix3-registry.html)

### `nix registry pin`

<https://nix.dev/manual/nix/2.33/command-ref/new-cli/nix3-registry-pin.html>

## Troubleshooting

### Enable `nix-daemon`

[Run using the `VS Code Terminal`](./vs-code.md#run-a-command-using-the-vs-code-terminal):

```terminal
sudo systemctl enable nix-daemon
```

### Restart `nix-daemon`

[Run using the `VS Code Terminal`](./vs-code.md#run-a-command-using-the-vs-code-terminal):

```terminal
sudo systemctl restart nix-daemon
```
