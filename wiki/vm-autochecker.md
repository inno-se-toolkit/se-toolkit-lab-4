# VM autochecker

<h2>Table of contents</h2>

- [What is the VM autochecker](#what-is-the-vm-autochecker)
- [Create the `autochecker` user](#create-the-autochecker-user)
- [Add an `SSH` public key to the `autochecker` user](#add-an-ssh-public-key-to-the-autochecker-user)
- [Copy `SSH` authorized keys to a user](#copy-ssh-authorized-keys-to-a-user)

## What is the VM autochecker

The VM autochecker is a bot that verifies VM setup by connecting via [`SSH`](./ssh.md#what-is-ssh) as a restricted user. The `autochecker` user account has no `sudo` access.

## Create the `autochecker` user

1. To create the `autochecker` user without `sudo` privileges,

   [run in the `VS Code Terminal`](./vs-code.md#run-a-command-in-the-vs-code-terminal):

   ```terminal
   sudo adduser --disabled-password --gecos "" autochecker
   ```

2. To create the `.ssh` directory for `autochecker`,

   [run in the `VS Code Terminal`](./vs-code.md#run-a-command-in-the-vs-code-terminal):

   ```terminal
   sudo mkdir -p /home/autochecker/.ssh
   sudo chmod 700 /home/autochecker/.ssh
   sudo chown autochecker:autochecker /home/autochecker/.ssh
   ```

## Add an `SSH` public key to the `autochecker` user

1. To add the autochecker [`SSH`](./ssh.md#what-is-ssh) public key,

   [run in the `VS Code Terminal`](./vs-code.md#run-a-command-in-the-vs-code-terminal):

   ```terminal
   echo "ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIKiL0DDQZw7L0Uf1c9cNlREY7IS6ZkIbGVWNsClqGNCZ se-toolkit-autochecker" | sudo tee /home/autochecker/.ssh/authorized_keys
   ```

2. To set the correct permissions,

   [run in the `VS Code Terminal`](./vs-code.md#run-a-command-in-the-vs-code-terminal):

   ```terminal
   sudo chmod 600 /home/autochecker/.ssh/authorized_keys
   sudo chown autochecker:autochecker /home/autochecker/.ssh/authorized_keys
   ```

## Copy `SSH` authorized keys to a user

Copy the `authorized_keys` file from the current user to another user so they can log in with the same [`SSH`](./ssh.md#what-is-ssh) key.

> [!NOTE]
> Replace `<username>` with the name of the target user.

1. To create the `.ssh` directory,

   [run in the `VS Code Terminal`](./vs-code.md#run-a-command-in-the-vs-code-terminal):

   ```terminal
   sudo mkdir -p /home/<username>/.ssh
   ```

2. To copy the authorized keys,

   [run in the `VS Code Terminal`](./vs-code.md#run-a-command-in-the-vs-code-terminal):

   ```terminal
   sudo cp ~/.ssh/authorized_keys /home/<username>/.ssh/authorized_keys
   ```

3. To set the correct ownership and permissions,

   [run in the `VS Code Terminal`](./vs-code.md#run-a-command-in-the-vs-code-terminal):

   ```terminal
   sudo chown -R <username>:<username> /home/<username>/.ssh
   sudo chmod 700 /home/<username>/.ssh
   sudo chmod 600 /home/<username>/.ssh/authorized_keys
   ```
