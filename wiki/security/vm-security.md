# VM security

<h2>Table of contents</h2>

- [VM hardening](#vm-hardening)
  - [Create a non-root user](#create-a-non-root-user)
  - [Configure `ufw` firewall](#configure-ufw-firewall)
  - [Configure `fail2ban`](#configure-fail2ban)
  - [Disable root SSH login](#disable-root-ssh-login)
  - [Disable password authentication](#disable-password-authentication)
  - [Create the `autochecker` user](#create-the-autochecker-user)
  - [Restart `sshd`](#restart-sshd)

## VM hardening

VM hardening is the process of securing a server by reducing its attack surface.

### Create a non-root user

1. Connect to the VM as root:

   ```terminal
   ssh root@<vm-ip>
   ```

2. Create a new user:

   ```terminal
   adduser <username>
   ```

3. Add the user to the `sudo` group:

   ```terminal
   usermod -aG sudo <username>
   ```

4. Copy your SSH key to the new user:

   ```terminal
   mkdir -p /home/<username>/.ssh
   cp /root/.ssh/authorized_keys /home/<username>/.ssh/
   chown -R <username>:<username> /home/<username>/.ssh
   chmod 700 /home/<username>/.ssh
   chmod 600 /home/<username>/.ssh/authorized_keys
   ```

5. Verify you can SSH as the new user (from your laptop):

   ```terminal
   ssh <username>@<vm-ip>
   ```

### Configure `ufw` firewall

`ufw` (`Uncomplicated Firewall`) is a simple firewall for `Linux`.

1. Allow SSH:

   ```terminal
   sudo ufw allow 22
   ```

2. Allow the application port:

   ```terminal
   sudo ufw allow 42002
   ```

3. Enable the firewall:

   ```terminal
   sudo ufw enable
   ```

4. Check the status:

   ```terminal
   sudo ufw status
   ```

> [!IMPORTANT]
> Always allow SSH (port 22) before enabling `ufw`. Otherwise, you will lock yourself out of the VM.

### Configure `fail2ban`

`fail2ban` blocks IP addresses that make too many failed login attempts.

1. Install `fail2ban`:

   ```terminal
   sudo apt update && sudo apt install -y fail2ban
   ```

2. Start and enable the service:

   ```terminal
   sudo systemctl enable fail2ban
   sudo systemctl start fail2ban
   ```

3. Check the status:

   ```terminal
   sudo systemctl status fail2ban
   ```

### Disable root SSH login

1. Open the SSH config:

   ```terminal
   sudo nano /etc/ssh/sshd_config
   ```

2. Find the line `PermitRootLogin` and set it to:

   ```text
   PermitRootLogin no
   ```

3. Save and exit (`Ctrl+O`, `Enter`, `Ctrl+X`).

> [!IMPORTANT]
> Make sure you can SSH as a non-root user before disabling root login.

### Disable password authentication

1. Open the SSH config:

   ```terminal
   sudo nano /etc/ssh/sshd_config
   ```

2. Find the line `PasswordAuthentication` and set it to:

   ```text
   PasswordAuthentication no
   ```

3. Save and exit.

> [!IMPORTANT]
> Make sure your SSH key is set up before disabling password authentication.

### Create the `autochecker` user

The `autochecker` user is a restricted user for the instructor to verify VM hardening.

1. Create the user (no sudo):

   ```terminal
   sudo adduser --disabled-password --gecos "" autochecker
   ```

2. Create the `.ssh` directory:

   ```terminal
   sudo mkdir -p /home/autochecker/.ssh
   sudo chmod 700 /home/autochecker/.ssh
   ```

3. Add the instructor's SSH public key:

   ```terminal
   echo "<instructor-public-key>" | sudo tee /home/autochecker/.ssh/authorized_keys
   ```

4. Set permissions:

   ```terminal
   sudo chown -R autochecker:autochecker /home/autochecker/.ssh
   sudo chmod 600 /home/autochecker/.ssh/authorized_keys
   ```

> [!NOTE]
> The instructor will provide the public key to add.

### Restart `sshd`

After changing the SSH config, restart the SSH service:

```terminal
sudo systemctl restart sshd
```
