# `direnv`

- [What is `direnv`](#what-is-direnv)
- [Set up `direnv`](#set-up-direnv)
  - [Install `direnv`](#install-direnv)
  - [Install `nix-direnv`](#install-nix-direnv)
  - [Reboot your computer](#reboot-your-computer)
  - [Hook `direnv` into your shell](#hook-direnv-into-your-shell)
  - [Install the `VS Code` extension](#install-the-vs-code-extension)
  - [Run `direnv allow`](#run-direnv-allow)
  - [Reset and reload environment](#reset-and-reload-environment)

## What is `direnv`

## Set up `direnv`

Complete these steps:

1. [Install `direnv`](#install-direnv).
2. [Install `nix-direnv`](#install-nix-direnv).
3. [Reboot your computer](#reboot-your-computer).
4. [Hook `direnv` into your shell](#hook-direnv-into-your-shell).
5. [Install the `VS Code` extension](#install-the-vs-code-extension).
6. [Run `direnv allow`](#run-direnv-allow).
7. [Reset and reload environment](#reset-and-reload-environment).

### Install `direnv`

[Run using the `VS Code Terminal`](./vs-code.md#run-a-command-using-the-vs-code-terminal):

```terminal
nix profile add nixpkgs#direnv
```

### Install `nix-direnv`

[Run using the `VS Code Terminal`](./vs-code.md#run-a-command-using-the-vs-code-terminal):

```terminal
nix profile add nixpkgs#nix-direnv
```

### Reboot your computer

Reboot.

### Hook `direnv` into your shell

Complete the [`direnv` setup](https://direnv.net/docs/hook.html) for your shell.

> [!TIP]
> [Open the file using `VS Code`](./vs-code.md#open-the-file).

### Install the `VS Code` extension

[Install the extension](./vs-code.md#install-the-extension) with the identifier `mkhl.direnv`.

### Run `direnv allow`

1. Make sure you are in the directory that contains a `.envrc` file:

   [Run using the `VS Code Terminal`](./vs-code.md#run-a-command-using-the-vs-code-terminal):

   ```terminal
   ls .envrc
   ```

   The output should be:

   ```terminal
   .envrc
   ```

2. Allow `direnv` to use the `.envrc` file:
  
   [Run using the `VS Code Terminal`](./vs-code.md#run-a-command-using-the-vs-code-terminal):

   ```terminal
   direnv allow
   ```

3. Wait for `direnv` to download all dependencies.

### Reset and reload environment

Update the environment in which [`VS Code` extensions](./vs-code.md#extensions) run:

1. [Run using the `Command Palette`](./vs-code.md#run-a-command-using-the-command-palette):
   `direnv: Reset and reload environment`.
2. Wait for `direnv` to finish.
   <img alt="Direnv loading" src="./images/direnv/direnv-loading.png" style="width:300px">
3. Click `Restart`.
   <img alt="Direnv restart extensions" src="./images/direnv/direnv-restart-extensions.png" style="width:300px">
4. Wait 1-2 minutes for extensions to reload.
