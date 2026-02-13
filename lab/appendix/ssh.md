# `SSH`

<h2>Table of contents</h2>

- [`SSH` and shells](#ssh-and-shells)
- [SSH daemon](#ssh-daemon)
- [`ssh-agent`](#ssh-agent)
- [Create a new `SSH` key](#create-a-new-ssh-key)
- [Find the `SSH` key files](#find-the-ssh-key-files)
- [Add the host to the `SSH` config](#add-the-host-to-the-ssh-config)
- [Start the `ssh-agent`](#start-the-ssh-agent)
- [Verify the `SSH` setup](#verify-the-ssh-setup)
- [Connect to the VM](#connect-to-the-vm)
- [Common errors](#common-errors)

## `SSH` and shells

`Secure Shell` (`SSH`) is a protocol used to securely connect to remote servers.

You can use it to connect to [your virtual machine](./vm.md#your-vm).

All commands below assume a Unix shell: `Bash` (`Linux`, `WSL`) or `Zsh` (`macOS`).

> [!IMPORTANT]
> **Windows users:** Use `WSL` (Windows Subsystem for Linux). Do not use `PowerShell`, `cmd.exe`, or `Git Bash` — the commands below are not guaranteed to work there.

## SSH daemon

## `ssh-agent`

## Create a new `SSH` key

Generate a key pair: a **private key** (secret) and a **public key** (safe to share).

We'll use the `ed25519` algorithm, which is the modern standard for security and performance.

1. [Run using the `VS Code Terminal`](./vs-code.md#run-a-command-using-the-vs-code-terminal):

   ```terminal
   ssh-keygen -t ed25519 -C "se-toolkit-student" -f ~/.ssh/se_toolkit_key
   ```

   *Note:* You can replace `"se-toolkit-student"` with your email or another label.

   *Note:* `-f ~/.ssh/se_toolkit_key` sets a custom file path and name.

2. **Passphrase:** When asked `Enter passphrase`, you may type a secure password or press `Enter` for no passphrase.
  
   *Note:* If you set a passphrase, use `ssh-agent` to avoid retyping it on every connection.

## Find the `SSH` key files

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

## Add the host to the `SSH` config

1. [Open using the `Command Palette` the file](./vs-code.md#open-a-file-using-the-command-palette):
   `~/.ssh/config`

2. Add this text at the end of the file.

   ```text

   Host se-toolkit-vm
      HostName <your-vm-ip-address>
      User root
      IdentityFile ~/.ssh/se_toolkit_key
      AddKeysToAgent yes
      UseKeychain yes
   ```

3. Replace `<your-vm-ip-address>` with the [IP address of your VM](./vm.md#get-the-ip-address-of-the-vm).

## Start the `ssh-agent`

[Run using the `VS Code Terminal`](./vs-code.md#run-a-command-using-the-vs-code-terminal):

```terminal
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/se_toolkit_key
```

## Verify the `SSH` setup

1. Check that your key is loaded:

   ```terminal
   ssh-add -l
   ```

2. You should see your key fingerprint in the output.

3. If you see `The agent has no identities`, run the [start `ssh-agent` step](#start-the-ssh-agent) again.

## Connect to the VM

You can connect using the alias that you [added to your `SSH` config](#add-the-host-to-the-ssh-config).

1. [Run using the `VS Code Terminal`](./vs-code.md#run-a-command-using-the-vs-code-terminal):

   ```terminal
   ssh se-toolkit-vm
   ```

2. If this is your first time connecting:
   1. You will see a message:
      `The authenticity of host ... can't be established.`

3. Type `yes` and press `Enter`.
4. After successful login, you should see a shell prompt on the remote machine.

## Common errors

`Permission denied (publickey)`:

1. Check `IdentityFile` in `~/.ssh/config`.
2. Ensure the public key was added to the remote host.
3. Ensure your key is loaded: `ssh-add -l`.

`Bad owner or permissions`:

1. [Run using the `VS Code Terminal`](./vs-code.md#run-a-command-using-the-vs-code-terminal):

   ```terminal
   chmod 700 ~/.ssh
   chmod 600 ~/.ssh/se_toolkit_key
   chmod 644 ~/.ssh/se_toolkit_key.pub
   ```

`Connection timed out`:

1. Verify host IP and network connectivity.
2. Verify the VM is running.
3. Use verbose logs to debug:

   ```terminal
   ssh -v se-toolkit-vm
   ```
