# VM autochecker setup

<h2>Table of contents</h2>

- [Create the `autochecker` user](#create-the-autochecker-user)
- [Add an SSH public key to the `autochecker` user](#add-an-ssh-public-key-to-the-autochecker-user)
- [Copy SSH authorized keys to a user](#copy-ssh-authorized-keys-to-a-user)

## Create the `autochecker` user

The `autochecker` user is a restricted account for the autochecker bot. It has no `sudo` access.

1. Create the `autochecker` user:

   ```terminal
   adduser --disabled-password --gecos "" autochecker
   ```

2. Create the `.ssh` directory for `autochecker`:

   ```terminal
   mkdir -p /home/autochecker/.ssh
   chmod 700 /home/autochecker/.ssh
   chown autochecker:autochecker /home/autochecker/.ssh
   ```

## Add an SSH public key to the `autochecker` user

1. Create the `authorized_keys` file for `autochecker`:

   ```terminal
   nano /home/autochecker/.ssh/authorized_keys
   ```

2. Paste the SSH public key:

   ```text
   ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIKiL0DDQZw7L0Uf1c9cNlREY7IS6ZkIbGVWNsClqGNCZ se-toolkit-autochecker
   ```

3. Save the file and exit (`Ctrl+O`, `Enter`, `Ctrl+X`).
4. Set the correct permissions:

   ```terminal
   chmod 600 /home/autochecker/.ssh/authorized_keys
   chown autochecker:autochecker /home/autochecker/.ssh/authorized_keys
   ```

## Copy SSH authorized keys to a user

Copy the `authorized_keys` file from the current user to another user so they can log in with the same SSH key.

1. Complete the following steps:
   1. Create the `.ssh` directory:

      ```terminal
      mkdir -p /home/<username>/.ssh
      ```

   2. Copy the authorized keys:

      ```terminal
      cp ~/.ssh/authorized_keys /home/<username>/.ssh/authorized_keys
      ```

   3. Set the correct ownership and permissions:

      ```terminal
      chown -R <username>:<username> /home/<username>/.ssh
      chmod 700 /home/<username>/.ssh
      chmod 600 /home/<username>/.ssh/authorized_keys
      ```

Replace `<username>` with the name of the target user.
