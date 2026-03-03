# VM autochecker

<h2>Table of contents</h2>

- [What is the VM autochecker](#what-is-the-vm-autochecker)
- [Set up the VM for autochecker](#set-up-the-vm-for-autochecker)

## What is the VM autochecker

The VM autochecker is a bot that verifies VM setup by connecting via [`SSH`](./ssh.md#what-is-ssh) as a restricted user. The `autochecker` user account has no `sudo` access.

## Set up the VM for autochecker

1. To create the `autochecker` user without `sudo` privileges,

   [run in the `VS Code Terminal`](./vs-code.md#run-a-command-in-the-vs-code-terminal):

   ```terminal
   sudo adduser --disabled-password --gecos "" autochecker
   ```

   The output should be similar to this:

   ```terminal
   ...
   info: Adding user `autochecker' to group `users' ...
   ```

2. To create the `.ssh` directory for `autochecker`,

   [run in the `VS Code Terminal`](./vs-code.md#run-a-command-in-the-vs-code-terminal):

   ```terminal
   sudo mkdir -p /home/autochecker/.ssh
   sudo chmod 700 /home/autochecker/.ssh
   sudo chown autochecker:autochecker /home/autochecker/.ssh
   ```

   You should see no output.

3. To check the information about the directory `/home/autochecker/.ssh/`,

   [run in the `VS Code Terminal`](./vs-code.md#run-a-command-in-the-vs-code-terminal):

   ```terminal
   ls -ld /home/autochecker/.ssh
   ```

   The output should be similar to this:

   ```terminal
   drwx------ 2 autochecker autochecker 4096 Mar  2 19:16 /home/autochecker/.ssh
   ```

4. To add the autochecker [`SSH`](./ssh.md#what-is-ssh) public key,

   [run in the `VS Code Terminal`](./vs-code.md#run-a-command-in-the-vs-code-terminal):

   ```terminal
   echo "ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIKiL0DDQZw7L0Uf1c9cNlREY7IS6ZkIbGVWNsClqGNCZ se-toolkit-autochecker" | sudo tee /home/autochecker/.ssh/authorized_keys
   ```

   You should see the public key:

   ```terminal
   ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIKiL0DDQZw7L0Uf1c9cNlREY7IS6ZkIbGVWNsClqGNCZ se-toolkit-autochecker
   ```

5. To set the correct permissions,

   [run in the `VS Code Terminal`](./vs-code.md#run-a-command-in-the-vs-code-terminal):

   ```terminal
   sudo chmod 600 /home/autochecker/.ssh/authorized_keys
   sudo chown autochecker:autochecker /home/autochecker/.ssh/authorized_keys
   ```

   You should see no output.

6. To check the information about the file `/home/autochecker/.ssh/authorized_keys`,

   [run in the `VS Code Terminal`](./vs-code.md#run-a-command-in-the-vs-code-terminal):

   ```terminal
   ls -l /home/autochecker/.ssh/authorized_keys
   ```

   The output should be similar to this:

   ```
   -rw------- 1 autochecker autochecker 104 Mar  2 19:16 /home/autochecker/.ssh/authorized_keys
   ```
