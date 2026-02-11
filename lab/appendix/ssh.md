# `SSH`

## `SSH` and shells

`Secure Shell` (`SSH`) is a protocol used to securely connect to remote servers.

You can use it to connect to [your virtual machine](./vm.md#your-vm).

Since you are using `Git Bash` (`Windows`), `WSL` (`Windows`), `Zsh` (`macOS`), or `Bash` (`Linux`), the commands below will work in your terminal without requiring `PowerShell` or GUI tools like `PuTTY`.

## Create a new `SSH` key (custom location)

We need to generate a pair of keys: a **public key** and a **private key**.

We'll use the `ed25519` algorithm, which is the modern standard for security and performance.

1. [Run using the `Terminal`](./vs-code.md#run-a-command-using-the-terminal):

   ```terminal
   ssh-keygen -t ed25519 -C "se-toolkit-student" -f ~/.ssh/se_toolkit_key
   ```

   *Note:* you can replace the comment inside quotes (`"se-toolkit-student"`) with your own email, or leave it as is.

   *Note:* The `-f ~/.ssh/se_toolkit_key` part tells the computer exactly where to save the file and names it `se_toolkit_key`. The `~` symbol is a universal shortcut for your user's home folder on `Windows` (`Git Bash`/`WSL`), `macOS`, and `Linux`.

2. **Passphrase:** When asked `Enter passphrase`, you may type a secure password or press `Enter` for no passphrase.
  
  *Note:* If you set a passphrase, you will need to type it whenever you use the key unless you use the `ssh-agent`.

## Find the `SSH` key files

`SSH` keys are generated in pairs. You must know which file is which.

Because you used a custom name, your keys are named `se_toolkit_key` (private) and `se_toolkit_key.pub` (public).

1. Verify they were created:

   [Run using the `Terminal`](./vs-code.md#run-a-command-using-the-terminal):

   ```bash
   ls ~/.ssh/se_toolkit_key*
   ```

2. You should see two files listed.

   The file ending in `.pub` contains the public key.

   Another file contains the private key.

> [!IMPORTANT]
> Never share the private key.
> This is your secret identity.

## Add host to the `SSH` config

1. Open the `SSH` config file:

   [Open using the `Command Palette` the file](./vs-code.md#open-a-file-using-the-command-palette):
   `~/.ssh/config`

2. Add the entry:

    ```text
    Host se-toolkit-vm
        HostName <your-vm-ip-address>
        User root
        IdentityFile ~/.ssh/se_toolkit_key
        AddKeysToAgent yes
        UseKeychain yes
    ```

    *Note:* Replace `<your-vm-ip-address>` with the [IP address of your VM](./vm.md#get-the-ip-address-of-the-vm).

    *Note:* `IdentityFile` line says to use the key that you created.

## Start the `ssh-agent`

1. [Open using the `Command Palette` the file](./vs-code.md#open-a-file-using-the-command-palette):
   - `~/.bashrc` if you use `bash`
   - `~/.zshrc` if you use `zsh`

2. Paste this code at the bottom of the file:

    ```text
    # Define environment file location
    SSH_ENV="$HOME/.ssh/agent.env"

    function start_agent {
        echo "Initialising new SSH agent..."
        # Start ssh-agent and pipe output (SSH_AUTH_SOCK/PID) to the environment file
        /usr/bin/ssh-agent | sed 's/^echo/#echo/' > "${SSH_ENV}"
        chmod 600 "${SSH_ENV}"
        . "${SSH_ENV}" > /dev/null
        # Load your default keys (optional, remove if you prefer manual adding)
        ssh-add
    }

    # Check if the environment file exists
    if [ -f "${SSH_ENV}" ]; then
        . "${SSH_ENV}" > /dev/null
        # Check if the agent process is actually running using the PID
        # ps -p works on Linux/macOS. MinGW (Git Bash) might need specific handling but usually works.
        ps -p "${SSH_AGENT_PID}" > /dev/null 2>&1 || {
            start_agent;
        }
    else
        start_agent;
    fi
    ```

<!-- TODO check this code works -->
<!-- TODO how to check whether everything is OK? -->

## Connect to the new host

Now that the configuration is saved, you can connect using the alias you [defined](#add-host-to-the-ssh-config).

1. [Run using the `Terminal`](../lab/lab-1/lab/appendix/vs-code.md#run-a-command-using-the-terminal):

    ```bash
    ssh se-toolkit-vm
    ```

2. If this is your first time connecting, you will see a message:
   `The authenticity of host ... can't be established.`
   Type `yes` and press **Enter**.
