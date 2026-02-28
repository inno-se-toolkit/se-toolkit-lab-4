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

VM hardening is the process of securing a virtual machine by reducing its attack surface.

Docs:

- [CIS Benchmarks](https://www.cisecurity.org/cis-benchmarks)

## Hardening steps

### Create a non-root user

1. Connect to the VM as root:

   [Run using the `VS Code Terminal`](./vs-code.md#run-a-command-using-the-vs-code-terminal):

   ```terminal
   ssh root@<vm-ip>
   ```

2. Create a new user:

   [Run using the `VS Code Terminal`](./vs-code.md#run-a-command-using-the-vs-code-terminal):

   ```terminal
   adduser <username>
   ```

3. Add the user to the `sudo` group:

   [Run using the `VS Code Terminal`](./vs-code.md#run-a-command-using-the-vs-code-terminal):

   ```terminal
   usermod -aG sudo <username>
   ```

4. Copy your [`SSH`](./ssh.md#what-is-ssh) key to the new user:

   [Run using the `VS Code Terminal`](./vs-code.md#run-a-command-using-the-vs-code-terminal):

   ```terminal
   mkdir -p /home/<username>/.ssh
   cp /root/.ssh/authorized_keys /home/<username>/.ssh/
   chown -R <username>:<username> /home/<username>/.ssh
   chmod 700 /home/<username>/.ssh
   chmod 600 /home/<username>/.ssh/authorized_keys
   ```

5. Verify you can `SSH` as the new user. Open a new terminal on your laptop:

   [Run using the `VS Code Terminal`](./vs-code.md#run-a-command-using-the-vs-code-terminal):

   ```terminal
   ssh <username>@<vm-ip>
   ```

6. Disconnect from the root session and use the non-root user for all remaining steps.

### Configure `ufw` firewall

`ufw` (`Uncomplicated Firewall`) is a simple firewall for [`Linux`](./linux.md#what-is-linux).

1. Allow [`SSH`](./ssh.md#what-is-ssh):

   [Run using the `VS Code Terminal`](./vs-code.md#run-a-command-using-the-vs-code-terminal):

   ```terminal
   sudo ufw allow 22
   ```

2. Allow the application port:

   [Run using the `VS Code Terminal`](./vs-code.md#run-a-command-using-the-vs-code-terminal):

   ```terminal
   sudo ufw allow 42002
   ```

3. Enable the firewall:

   [Run using the `VS Code Terminal`](./vs-code.md#run-a-command-using-the-vs-code-terminal):

   ```terminal
   sudo ufw enable
   ```

4. Check the status:

   [Run using the `VS Code Terminal`](./vs-code.md#run-a-command-using-the-vs-code-terminal):

   ```terminal
   sudo ufw status
   ```

> [!IMPORTANT]
> Always allow `SSH` (port 22) before enabling `ufw`. Otherwise, you will lock yourself out of the VM.

### Configure `fail2ban`

`fail2ban` blocks IP addresses that make too many failed login attempts.

1. Update the package list:

   [Run using the `VS Code Terminal`](./vs-code.md#run-a-command-using-the-vs-code-terminal):

   ```terminal
   sudo apt update
   ```

2. Install `fail2ban`:

   [Run using the `VS Code Terminal`](./vs-code.md#run-a-command-using-the-vs-code-terminal):

   ```terminal
   sudo apt install -y fail2ban
   ```

3. Enable the service:

   [Run using the `VS Code Terminal`](./vs-code.md#run-a-command-using-the-vs-code-terminal):

   ```terminal
   sudo systemctl enable fail2ban
   ```

4. Start the service:

   [Run using the `VS Code Terminal`](./vs-code.md#run-a-command-using-the-vs-code-terminal):

   ```terminal
   sudo systemctl start fail2ban
   ```

5. Check the status:

   [Run using the `VS Code Terminal`](./vs-code.md#run-a-command-using-the-vs-code-terminal):

   ```terminal
   sudo systemctl status fail2ban
   ```

### Disable root `SSH` login

1. Open the [`SSH`](./ssh.md#what-is-ssh) config:

   [Run using the `VS Code Terminal`](./vs-code.md#run-a-command-using-the-vs-code-terminal):

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

1. Open the [`SSH`](./ssh.md#what-is-ssh) config:

   [Run using the `VS Code Terminal`](./vs-code.md#run-a-command-using-the-vs-code-terminal):

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

The `autochecker` user is a restricted user for the instructor to verify VM hardening.

1. Create the user without `sudo` privileges:

   [Run using the `VS Code Terminal`](./vs-code.md#run-a-command-using-the-vs-code-terminal):

   ```terminal
   sudo adduser --disabled-password --gecos "" autochecker
   ```

2. Create the `.ssh` directory:

   [Run using the `VS Code Terminal`](./vs-code.md#run-a-command-using-the-vs-code-terminal):

   ```terminal
   sudo mkdir -p /home/autochecker/.ssh
   sudo chmod 700 /home/autochecker/.ssh
   ```

3. Add the instructor's [`SSH`](./ssh.md#what-is-ssh) public key:

   [Run using the `VS Code Terminal`](./vs-code.md#run-a-command-using-the-vs-code-terminal):

   ```terminal
   echo "<instructor-public-key>" | sudo tee /home/autochecker/.ssh/authorized_keys
   ```

4. Set permissions:

   [Run using the `VS Code Terminal`](./vs-code.md#run-a-command-using-the-vs-code-terminal):

   ```terminal
   sudo chown -R autochecker:autochecker /home/autochecker/.ssh
   sudo chmod 600 /home/autochecker/.ssh/authorized_keys
   ```

> [!NOTE]
> The instructor will provide the public key to add.

### Restart `sshd`

After changing the [`SSH`](./ssh.md#what-is-ssh) config, restart the `SSH` service.

1. Validate the config:

   [Run using the `VS Code Terminal`](./vs-code.md#run-a-command-using-the-vs-code-terminal):

   ```terminal
   sudo sshd -t
   ```

   If the command prints no output, the config is valid. If it prints errors, fix them in `/etc/ssh/sshd_config` before continuing.

2. Restart the service:

   [Run using the `VS Code Terminal`](./vs-code.md#run-a-command-using-the-vs-code-terminal):

   ```terminal
   sudo systemctl restart sshd
   ```

3. Verify you can still connect. Open a **new** terminal on your laptop and log in:

   [Run using the `VS Code Terminal`](./vs-code.md#run-a-command-using-the-vs-code-terminal):

   ```terminal
   ssh <username>@<vm-ip>
   ```

> [!IMPORTANT]
> Keep your current `SSH` session open until you confirm the new connection works. If the new connection fails, use the existing session to fix the config.
