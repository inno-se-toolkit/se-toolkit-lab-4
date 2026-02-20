# Deploy to a hardened VM

<h4>Time</h4>

~40-50 min

<h4>Purpose</h4>

Learn to deploy a service securely and harden a Linux server.

<h4>Context</h4>

You will deploy the learning management service on your VM, configure the API key for production, and harden the VM with a firewall, `fail2ban`, and SSH restrictions.

<h4>Table of contents</h4>

- [Steps](#steps)
  - [1. Create a `Lab Task` issue](#1-create-a-lab-task-issue)
  - [Part A: Deploy and configure the API key](#part-a-deploy-and-configure-the-api-key)
    - [2. Connect to the VM](#2-connect-to-the-vm)
    - [3. Clone your fork on the VM](#3-clone-your-fork-on-the-vm)
    - [4. Create the `.env.docker.secret` file](#4-create-the-envdockersecret-file)
    - [5. Set a unique `API_TOKEN`](#5-set-a-unique-api_token)
    - [6. Set `CADDY_HOST_ADDRESS`](#6-set-caddy_host_address)
    - [7. Start the services](#7-start-the-services)
    - [8. Verify from the VM](#8-verify-from-the-vm)
    - [9. Verify from your laptop](#9-verify-from-your-laptop)
    - [10. Verify without a token](#10-verify-without-a-token)
  - [Part B: Harden the VM](#part-b-harden-the-vm)
    - [11. Create a non-root SSH user](#11-create-a-non-root-ssh-user)
    - [12. Configure the firewall](#12-configure-the-firewall)
    - [13. Install and configure `fail2ban`](#13-install-and-configure-fail2ban)
    - [14. Disable root SSH login](#14-disable-root-ssh-login)
    - [15. Disable password authentication](#15-disable-password-authentication)
    - [16. Create a `autochecker` SSH user](#16-create-a-autochecker-ssh-user)
    - [17. Add the instructor's SSH public key](#17-add-the-instructors-ssh-public-key)
    - [18. Restart `sshd`](#18-restart-sshd)
  - [19. Write a comment for the issue](#19-write-a-comment-for-the-issue)
- [Acceptance criteria](#acceptance-criteria)

## Steps

### 1. Create a `Lab Task` issue

Title: `[Task] Deploy to a hardened VM`

---

### Part A: Deploy and configure the API key

### 2. Connect to the VM

1. [Run using the `VS Code Terminal`](../../appendix/vs-code.md#run-a-command-using-the-vs-code-terminal):

   ```terminal
   ssh se-toolkit-vm
   ```

2. You should see the remote shell prompt (e.g., `root@<your-vm-name>:~#`).

> [!IMPORTANT]
> Run all subsequent commands (unless specified otherwise) in the shell where you see this prompt.
> This way, you will run commands on the VM.

### 3. Clone your fork on the VM

Use any of the following methods:

**Already cloned the repo on the VM:**

1. Navigate to the project directory:

   ```terminal
   cd se-toolkit-lab-3
   ```

2. Pull the latest changes:

   ```terminal
   git pull
   ```

**Not yet cloned:**

1. [Clone the repo](../../appendix/git-vscode.md#clone-the-repo-using-the-vs-code-terminal).

   Replace `<repo-url>` with [`<your-fork-url>`](../../appendix/github.md#your-fork-url).

2. Navigate to the project directory:

   ```terminal
   cd se-toolkit-lab-3
   ```

### 4. Create the `.env.docker.secret` file

1. Run on the VM:

   ```terminal
   cp .env.docker.example .env.docker.secret
   ```

### 5. Set a unique `API_TOKEN`

1. Open the `.env.docker.secret` file:

   ```terminal
   nano .env.docker.secret
   ```

2. Change the `API_TOKEN` value to something unique and different from the default. For example:

   ```text
   API_TOKEN=my-production-secret-key-2025
   ```

   > **Important:** Do not use the default value `my-secret-api-key` in production. Choose a strong, unique key.

3. Save the file and exit (`Ctrl+O`, `Enter`, `Ctrl+X`).

### 6. Set `CADDY_HOST_ADDRESS`

1. Verify that `CADDY_HOST_ADDRESS` is set to `0.0.0.0` in `.env.docker.secret`.

> [!NOTE]
> `0.0.0.0` means the server listens on **all network interfaces**.
> This makes the service accessible from outside the VM (e.g., from your laptop).

### 7. Start the services

1. Run on the VM:

   ```terminal
   docker compose --env-file .env.docker.secret up --build -d
   ```

   > **Note:** The `-d` flag runs the containers in the background (detached mode).
   > This is useful on a remote server because the containers keep running after you close the terminal.

2. Check that the containers are running:

   ```terminal
   docker compose ps
   ```

3. You should see the containers with the status `Up`.

### 8. Verify from the VM

1. Run on the VM:

   ```terminal
   curl http://127.0.0.1:42002/items -H "Authorization: Bearer <your-token>" | jq .
   ```

   Replace `<your-token>` with the `API_TOKEN` value you set in [Step 5](#5-set-a-unique-api_token).

2. You should see a `JSON` response with the list of items.

### 9. Verify from your laptop

> [!NOTE]
> You can find the IP address of your VM on the [VM page](../../appendix/vm.md#get-the-ip-address-of-the-vm).

1. Open a new terminal **on your laptop** (not on the VM).
2. Run:

   ```terminal
   curl http://<vm-ip>:42002/items -H "Authorization: Bearer <your-token>" | jq .
   ```

   Replace `<vm-ip>` with the IP address of your VM and `<your-token>` with your `API_TOKEN` value.

3. You should see the same `JSON` response as in the previous step.

### 10. Verify without a token

1. Run from your laptop:

   ```terminal
   curl http://<vm-ip>:42002/items | jq .
   ```

2. You should see a `403` Forbidden response.

> [!IMPORTANT]
> Keep the services running on the VM. Do not run `docker compose down`.
> The deployment will be checked automatically.

---

### Part B: Harden the VM

### 11. Create a non-root SSH user

1. Connect to the VM as `root` (if not already connected).
2. Create a new user for operations:

   ```terminal
   adduser operator
   ```

3. Follow the prompts to set a password.
4. Grant the user `sudo` access:

   ```terminal
   usermod -aG sudo operator
   ```

5. [Copy SSH authorized keys to the `operator` user](../../appendix/vm-autochecker.md#copy-ssh-authorized-keys-to-a-user).

   Replace `<username>` with `operator`.

### 12. Configure the firewall

1. Allow the SSH port:

   ```terminal
   ufw allow 22
   ```

2. Allow the application port:

   ```terminal
   ufw allow 42002
   ```

3. Enable the firewall:

   ```terminal
   ufw --force enable
   ```

4. Check the firewall status:

   ```terminal
   ufw status
   ```

5. You should see rules allowing ports `22` and `42002`.

> [!IMPORTANT]
> Make sure to allow port `22` (SSH) **before** enabling the firewall. Otherwise, you will lock yourself out of the VM.

### 13. Install and configure `fail2ban`

1. Install `fail2ban`:

   ```terminal
   apt update && apt install -y fail2ban
   ```

2. Start and enable `fail2ban`:

   ```terminal
   systemctl enable fail2ban
   systemctl start fail2ban
   ```

3. Verify that `fail2ban` is active:

   ```terminal
   systemctl status fail2ban
   ```

4. You should see `Active: active (running)`.

### 14. Disable root SSH login

1. Open the SSH configuration file:

   ```terminal
   nano /etc/ssh/sshd_config
   ```

2. Find the line `PermitRootLogin` and change it to:

   ```text
   PermitRootLogin no
   ```

   > **Tip:** If the line is commented out (starts with `#`), uncomment it by removing the `#`.

3. Save the file and exit (`Ctrl+O`, `Enter`, `Ctrl+X`).

> [!IMPORTANT]
> Before disabling root login, make sure you can log in as the `operator` user you created in [Step 11](#11-create-a-non-root-ssh-user).
> Open a new terminal on your laptop and test: `ssh operator@<vm-ip>`.

### 15. Disable password authentication

1. Open the SSH configuration file:

   ```terminal
   nano /etc/ssh/sshd_config
   ```

2. Find the line `PasswordAuthentication` and change it to:

   ```text
   PasswordAuthentication no
   ```

   > **Tip:** If the line is commented out (starts with `#`), uncomment it by removing the `#`.

3. Save the file and exit (`Ctrl+O`, `Enter`, `Ctrl+X`).

### 16. Create a `autochecker` SSH user

1. [Create the `autochecker` user](../../appendix/vm-autochecker.md#create-the-autochecker-user).

### 17. Add the instructor's SSH public key

1. [Add the instructor's SSH public key to the `autochecker` user](../../appendix/vm-autochecker.md#add-an-ssh-public-key-to-the-autochecker-user).

   Replace step 2 ("Paste the SSH public key") with: paste the instructor's SSH public key (provided by the instructor).

### 18. Restart `sshd`

1. Apply the SSH configuration changes:

   ```terminal
   systemctl restart sshd
   ```

2. Verify the SSH configuration is applied:

   ```terminal
   sshd -T | grep -E "permitrootlogin|passwordauthentication"
   ```

3. You should see:

   ```text
   permitrootlogin no
   passwordauthentication no
   ```

> [!IMPORTANT]
> After restarting `sshd`, verify that you can still connect to the VM as the `operator` user from a **new** terminal on your laptop before closing the current session.

### 19. Write a comment for the issue

1. Go to the issue that you created for this task.
2. Scroll down.
3. Go to `Add a comment`.
4. Write the deployed URL of your service (e.g., `http://<vm-ip>:42002/items`).
5. Click `Close with comment`.

---

## Acceptance criteria

- [ ] Issue has the correct title.
- [ ] The service is accessible at `http://<vm-ip>:42002/items` with the correct API key.
- [ ] The service returns `403` without an API key.
- [ ] `autochecker` user exists and can SSH with a key.
- [ ] `autochecker` has no `sudo` access.
- [ ] `fail2ban` is active.
- [ ] `PermitRootLogin no` is set.
- [ ] `PasswordAuthentication no` is set.
- [ ] The comment with the deployed URL exists.
