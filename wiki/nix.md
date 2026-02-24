# `Nix`

<h2>Table of contents</h2>

- [What is `Nix`](#what-is-nix)
- [Install `Nix`](#install-nix)

## What is `Nix`

`Nix` is a cross-platform package manager that provides reproducible, isolated software environments.
It allows you to install tools and dependencies without affecting the rest of your system.

Docs:

- [Nix documentation](https://nix.dev/)
- [Determinate Systems installer](https://github.com/DeterminateSystems/nix-installer#install-determinate-nix)

## Install `Nix`

1. [Run using the `VS Code Terminal`](./vs-code.md#run-a-command-using-the-vs-code-terminal):

   ```terminal
   curl --proto '=https' --tlsv1.2 -sSf -L https://install.determinate.systems/nix | sh -s -- install
   ```

2. Follow the prompts to complete the installation.

3. Open a new terminal after the installation finishes.

   [Open a new `VS Code Terminal`](./vs-code.md#open-a-new-vs-code-terminal).

4. Verify the installation.

   [Run using the `VS Code Terminal`](./vs-code.md#run-a-command-using-the-vs-code-terminal):

   ```terminal
   nix --version
   ```

   The output should be similar to this:

   ```terminal
   nix (Determinate Nix 3.15.2) 2.33.1
   ```
