# `SSH`

<h2>Table of contents</h2>

- [What is `SSH`](#what-is-ssh)
- [SSH daemon](#ssh-daemon)
- [`ssh-agent`](#ssh-agent)
- [Set up SSH](#set-up-ssh)
  - [Create a new `SSH` key](#create-a-new-ssh-key)
  - [Find the `SSH` key files](#find-the-ssh-key-files)
  - [Start the `ssh-agent`](#start-the-ssh-agent)
  - [Verify the `SSH` setup](#verify-the-ssh-setup)
- [Add the host to `SSH`](#add-the-host-to-ssh)
- [Connect to the VM](#connect-to-the-vm)
- [Login](#login)
  - [Login without password](#login-without-password)
  - [Login with password](#login-with-password)
- [Common errors](#common-errors)
  - [`Permission denied (publickey)`](#permission-denied-publickey)
  - [`Bad owner or permissions`](#bad-owner-or-permissions)
  - [`Connection timed out`](#connection-timed-out)
- [`scp`](#scp)

## What is `SSH`

`SSH` (`Secure Shell`) is a protocol used to securely connect to remote machines.

You can use it to connect to [your virtual machine](./vm.md#your-vm).

All commands below assume a Unix shell: `Bash` (`Linux`, `WSL`) or `Zsh` (`macOS`).

> [!IMPORTANT]
> **Windows users:** Use `WSL` (Windows Subsystem for Linux). Do not use `PowerShell`, `cmd.exe`, or `Git Bash` — the commands below are not guaranteed to work there.

## SSH daemon

The `SSH` daemon (`sshd`) is a program that runs on the [remote host](./computer-networks.md#remote-host) and [listens](./computer-networks.md#listen-on-a-port) for incoming `SSH` connections.

You do not need to configure it — your [VM](./vm.md#your-vm) already has it running.

## `ssh-agent`

`ssh-agent` is a background program that stores your private `SSH` key in memory for the duration of your session.

When `ssh-agent` holds your key, you do not need to type a passphrase every time you connect.

See [Start the `ssh-agent`](#start-the-ssh-agent) for setup instructions.

## Set up SSH

Set up [`SSH`](#what-is-ssh) to connect to a [remote host](./computer-networks.md#remote-host).

Steps:

<!-- no toc -->
1. [Check your current shell](./vs-code.md#check-the-current-shell-in-the-vs-code-terminal).
2. [Create a new `SSH` key](#create-a-new-ssh-key)
3. [Find the `SSH` key files](#find-the-ssh-key-files)
4. [Start the `ssh-agent`](#start-the-ssh-agent)
5. [Verify the `SSH` setup](#verify-the-ssh-setup)

### Create a new `SSH` key

Generate a key pair: a **private key** (secret) and a **public key** (safe to share).

We'll use the `ed25519` algorithm, which is the modern standard for security and performance.

Steps:

1. [Run using the `VS Code Terminal`](./vs-code.md#run-a-command-using-the-vs-code-terminal):

   ```terminal
   ssh-keygen -t ed25519 -C "se-toolkit-student" -f ~/.ssh/se_toolkit_key
   ```

   *Note:* You can replace `"se-toolkit-student"` with your email or another label.

   *Note:* `-f ~/.ssh/se_toolkit_key` sets a custom file path and name.

2. **Passphrase:** When asked `Enter passphrase`, you may type a secure password or press `Enter` for no passphrase.
  
   *Note:* If you set a passphrase, use `ssh-agent` to avoid retyping it on every connection.

### Find the `SSH` key files

`SSH` keys are generated in pairs. You must know which file is which.

Because you used a custom name, your keys are named `se_toolkit_key` (private) and `se_toolkit_key.pub` (public).

1. Verify they were created:

   [Run using the `VS Code Terminal`](./vs-code.md#run-a-command-using-the-vs-code-terminal):

   ```terminal
   ls ~/.ssh/se_toolkit_key*
   ```

2. You should see two files listed.

   The file ending in `.pub` contains the public key.

   Another file contains the private key.

3. View the content of the public key file:

   [Run using the `VS Code Terminal`](./vs-code.md#run-a-command-using-the-vs-code-terminal):

   ```terminal
   cat ~/.ssh/se_toolkit_key.pub
   ```

   You should see something similar to this:

   ```terminal
   ssh-ed25519 AKdk38D3faWJnlFfalFJSKEFGG/vmLQ62Z+vpWCe5e/c2n37cnNc39N3c8qb7cBS+e3d se-toolkit-student
   ```

> [!IMPORTANT]
> Never share the private key.
> This is your secret identity.

### Start the `ssh-agent`

1. [Run using the `VS Code Terminal`](./vs-code.md#run-a-command-using-the-vs-code-terminal):

   ```terminal
   eval "$(ssh-agent -s)"
   ssh-add ~/.ssh/se_toolkit_key
   ```

### Verify the `SSH` setup

1. [Open a new `VS Code Terminal`](./vs-code.md#open-a-new-vs-code-terminal).
2. [Check the current shell in the `VS Code Terminal`](./vs-code.md#check-the-current-shell-in-the-vs-code-terminal).
3. [Run using the `VS Code Terminal`](./vs-code.md#run-a-command-using-the-vs-code-terminal):

   ```terminal
   ssh-add -l
   ```

4. You should see your key fingerprint in the output.

5. If you see `The agent has no identities`, run the [start `ssh-agent` step](#start-the-ssh-agent) again.

## Add the host to `SSH`

> [!NOTE]
> See [host](./computer-networks.md#host).

1. Make sure you have [set up `SSH`](#set-up-ssh).
2. Get [`<your-vm-ip-address>`](./vm.md#your-vm-ip-address).
3. [Open the file](./vs-code.md#open-the-file):
   `~/.ssh/config`
4. Add this text at the end of the file.

   - `Linux`, `Windows`:

     ```text
  
     Host se-toolkit-vm
        HostName <your-vm-ip-address>
        User root
        IdentityFile ~/.ssh/se_toolkit_key
        AddKeysToAgent yes
     ```

   - `macOS`:

     ```text
  
     Host se-toolkit-vm
        HostName <your-vm-ip-address>
        User root
        IdentityFile ~/.ssh/se_toolkit_key
        AddKeysToAgent yes
        UseKeychain yes
     ```

5. Replace [`<your-vm-ip-address>`](./vm.md#your-vm-ip-address) in the `~/.ssh/config` file.

## Connect to the VM

You can connect using the alias that you [added to your `SSH` config](#add-the-host-to-ssh).

1. [Run using the `VS Code Terminal`](./vs-code.md#run-a-command-using-the-vs-code-terminal):

   ```terminal
   ssh se-toolkit-vm
   ```

2. If this is your first time connecting:
   1. You will see a message:
      `The authenticity of host ... can't be established.`

   2. Type `yes` and press `Enter`.
3. After a successful login, you should see the [shell prompt](./shell.md#shell-prompt):

   ```terminal
   root@<your-vm-name>:~#
   ```

   See [`<your-vm-name>`](./vm.md#your-vm-name).

## Login

`SSH` supports two authentication methods: [key-based](#login-without-password) (no password prompt) and [password-based](#login-with-password).

### Login without password

Key-based authentication uses your private key to prove your identity. The remote host checks whether the matching public key is listed as authorized.

This is the recommended method and is what [Set up SSH](#set-up-ssh) configures.

1. [Set up SSH](#set-up-ssh).
2. Ensure your public key is added to the remote host.
3. [Connect to the VM](#connect-to-the-vm).

You will not be asked for a password.

### Login with password

Password-based authentication asks you to type the remote user's password.

> [!NOTE]
> Password authentication may be disabled on the VM. Use [key-based authentication](#login-without-password) instead.

1. [Run using the `VS Code Terminal`](./vs-code.md#run-a-command-using-the-vs-code-terminal):

   ```terminal
   ssh -o PasswordAuthentication=yes root@<your-vm-ip-address>
   ```

2. Type the VM's root password when prompted.

## Common errors

### `Permission denied (publickey)`

1. Check `IdentityFile` in `~/.ssh/config`.
2. Ensure the public key was added to the remote host.
3. Ensure your key is loaded: `ssh-add -l`.

### `Bad owner or permissions`

1. [Run using the `VS Code Terminal`](./vs-code.md#run-a-command-using-the-vs-code-terminal):

   ```terminal
   chmod 700 ~/.ssh
   chmod 600 ~/.ssh/se_toolkit_key
   chmod 644 ~/.ssh/se_toolkit_key.pub
   ```

### `Connection timed out`

1. Verify host IP and network connectivity.
2. Verify the VM is running.
3. Try to ping the VM:

   Run using the `VS Code Terminal`:

   ```terminal
   ping <your-vm-ip-address>
   ```

   You should see logs like these:

   ```terminal
   PING 10.93.24.112 (10.93.24.112) 56(84) bytes of data.

   64 bytes from 10.93.24.112: icmp_seq=1 ttl=61 time=2.15 ms
   64 bytes from 10.93.24.112: icmp_seq=2 ttl=61 time=0.996 ms
   64 bytes from 10.93.24.112: icmp_seq=3 ttl=61 time=1.08 ms
   
   ...
   ```

4. Use verbose logs to debug:

   ```terminal
   ssh -v se-toolkit-vm
   ```

5. Try to stop, delete, and create a new VM if there are still problems.

## `scp`

`scp` (`Secure Copy`) copies files between machines over [`SSH`](#what-is-ssh).

Common pattern:

```terminal
scp -r <local-path> <user>@<host>:<remote-path>
```

The `-r` flag copies directories recursively.
