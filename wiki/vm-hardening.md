# VM hardening

<h2>Table of contents</h2>

- [What is VM hardening](#what-is-vm-hardening)
- [Hardening steps](#hardening-steps)
  - [Create a non-root user](#create-a-non-root-user)
  - [Configure `ufw` firewall](#configure-ufw-firewall)
  - [Configure `fail2ban`](#configure-fail2ban)
  - [Disable root `SSH` login](#disable-root-ssh-login)
  - [Disable password authentication](#disable-password-authentication)
  - [Create the `autochecker` user](#create-the-autochecker-user)
  - [Restart `sshd`](#restart-sshd)

## What is VM hardening

VM hardening is the process of securing a [virtual machine](./vm.md#what-is-a-vm) by reducing its attack surface.

Docs:

- [CIS Benchmarks](https://www.cisecurity.org/cis-benchmarks)

## Hardening steps

### Create a non-root user

1. To connect to the VM as root,

   [run in the `VS Code Terminal`](./vs-code.md#run-a-command-in-the-vs-code-terminal):

   ```terminal
   ssh root@<vm-ip>
   ```

2. To create a new user,

   [run in the `VS Code Terminal`](./vs-code.md#run-a-command-in-the-vs-code-terminal):

   ```terminal
   adduser <username>
   ```

3. To add the user to the `sudo` group,

   [run in the `VS Code Terminal`](./vs-code.md#run-a-command-in-the-vs-code-terminal):

   ```terminal
   usermod -aG sudo <username>
   ```

4. To copy your [`SSH`](./ssh.md#what-is-ssh) key to the new user,

   [run in the `VS Code Terminal`](./vs-code.md#run-a-command-in-the-vs-code-terminal):

   ```terminal
   mkdir -p /home/<username>/.ssh
   cp /root/.ssh/authorized_keys /home/<username>/.ssh/
   chown -R <username>:<username> /home/<username>/.ssh
   chmod 700 /home/<username>/.ssh
   chmod 600 /home/<username>/.ssh/authorized_keys
   ```

5. To verify you can `SSH` as the new user,

   [run in the `VS Code Terminal`](./vs-code.md#run-a-command-in-the-vs-code-terminal):

   ```terminal
   ssh <username>@<vm-ip>
   ```

6. Disconnect from the root session and use the non-root user for all remaining steps.

### Configure `ufw` firewall

`ufw` (`Uncomplicated Firewall`) is a simple firewall for [`Linux`](./linux.md#what-is-linux).

1. Look up the value of `CADDY_HOST_PORT` in the `.env.docker.secret` file.
   This is your [`<app-port>`](./placeholders.md#app-port).

2. To allow [`SSH`](./ssh.md#what-is-ssh),

   [run in the `VS Code Terminal`](./vs-code.md#run-a-command-in-the-vs-code-terminal):

   ```terminal
   sudo ufw allow 22
   ```

3. To allow the application port,

   [run in the `VS Code Terminal`](./vs-code.md#run-a-command-in-the-vs-code-terminal):

   ```terminal
   sudo ufw allow <api-port>
   ```

4. To enable the firewall,

   [run in the `VS Code Terminal`](./vs-code.md#run-a-command-in-the-vs-code-terminal):

   ```terminal
   sudo ufw enable
   ```

5. To check the status,

   [run in the `VS Code Terminal`](./vs-code.md#run-a-command-in-the-vs-code-terminal):

   ```terminal
   sudo ufw status
   ```

> [!IMPORTANT]
> Always allow `SSH` (port 22) before enabling `ufw`. Otherwise, you will lock yourself out of the VM.

### Configure `fail2ban`

`fail2ban` blocks IP addresses that make too many failed login attempts.

1. To update the package list,

   [run in the `VS Code Terminal`](./vs-code.md#run-a-command-in-the-vs-code-terminal):

   ```terminal
   sudo apt update
   ```

2. To install `fail2ban`,

   [run in the `VS Code Terminal`](./vs-code.md#run-a-command-in-the-vs-code-terminal):

   ```terminal
   sudo apt install -y fail2ban
   ```

3. To enable the service,

   [run in the `VS Code Terminal`](./vs-code.md#run-a-command-in-the-vs-code-terminal):

   ```terminal
   sudo systemctl enable fail2ban
   ```

4. To start the service,

   [run in the `VS Code Terminal`](./vs-code.md#run-a-command-in-the-vs-code-terminal):

   ```terminal
   sudo systemctl start fail2ban
   ```

5. To check the status,

   [run in the `VS Code Terminal`](./vs-code.md#run-a-command-in-the-vs-code-terminal):

   ```terminal
   sudo systemctl status fail2ban
   ```

### Disable root `SSH` login

1. To open the [`SSH`](./ssh.md#what-is-ssh) config,

   [run in the `VS Code Terminal`](./vs-code.md#run-a-command-in-the-vs-code-terminal):

   ```terminal
   sudo nano /etc/ssh/sshd_config
   ```

2. Find the line `PermitRootLogin` and set it to:

   ```text
   PermitRootLogin no
   ```

3. Save and exit (`Ctrl+O`, `Enter`, `Ctrl+X`).

> [!IMPORTANT]
> Make sure you can `SSH` as a non-root user before disabling root login.

### Disable password authentication

1. To open the [`SSH`](./ssh.md#what-is-ssh) config,

   [run in the `VS Code Terminal`](./vs-code.md#run-a-command-in-the-vs-code-terminal):

   ```terminal
   sudo nano /etc/ssh/sshd_config
   ```

2. Find the line `PasswordAuthentication` and set it to:

   ```text
   PasswordAuthentication no
   ```

3. Save and exit (`Ctrl+O`, `Enter`, `Ctrl+X`).

> [!IMPORTANT]
> Make sure your `SSH` key is set up before disabling password authentication.

### Create the `autochecker` user

1. [Create the `autochecker` user](./vm-autochecker.md#create-the-autochecker-user).
2. [Add the `SSH` public key to the `autochecker` user](./vm-autochecker.md#add-an-ssh-public-key-to-the-autochecker-user).

### Restart `sshd`

After changing the [`SSH`](./ssh.md#what-is-ssh) config, restart the `SSH` service.

1. To validate the config,

   [run in the `VS Code Terminal`](./vs-code.md#run-a-command-in-the-vs-code-terminal):

   ```terminal
   sudo sshd -t
   ```

   If the command prints no output, the config is valid. If it prints errors, fix them in `/etc/ssh/sshd_config` before continuing.

2. To restart the service,

   [run in the `VS Code Terminal`](./vs-code.md#run-a-command-in-the-vs-code-terminal):

   ```terminal
   sudo systemctl restart sshd
   ```

3. To verify you can still connect,

   [run in the `VS Code Terminal`](./vs-code.md#run-a-command-in-the-vs-code-terminal):

   ```terminal
   ssh <username>@<vm-ip>
   ```

> [!IMPORTANT]
> Keep your current `SSH` session open until you confirm the new connection works. If the new connection fails, use the existing session to fix the config.
