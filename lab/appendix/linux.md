# `Linux`

`Linux` is a family of operating systems commonly used for servers and virtual machines.

## `bash`

Many setup and deployment commands are run in a shell, often `bash`.

Check what shell is running:

```terminal
echo "$SHELL"
ps -p $$ -o comm=
```

Useful `bash` basics:

- `pwd` - show current directory.
- `ls` - list files.
- `cd <dir>` - go to a directory.
- `cat <file>` - print file content.

## Users and permissions

Servers and VMs usually run multiple users.

- `root` is the administrator user.
- `sudo` runs a command with elevated permissions.

Useful commands:

```terminal
whoami
id
```

If a command fails with permission errors, run it with `sudo` when appropriate:

```terminal
sudo <command>
```

## Create a non-root user

`root` is useful for initial setup, but daily work should be done with a regular user.

For Ubuntu/Debian systems:

1. Create a new user:

```terminal
sudo adduser <username>
```

2. Allow the user to run administrative commands:

```terminal
sudo usermod -aG sudo <username>
```

3. Switch to that user:

```terminal
su - <username>
```

4. Verify:

```terminal
whoami
id
```

If you plan to log in via `SSH` as that user, copy `authorized_keys` to the new user's home and fix permissions before logging out from `root`.

## Port

A `port` is a numbered communication endpoint on a host.
Web servers usually listen on specific TCP ports such as `80`, `443`, or custom ports like `42000`.

See listening TCP ports:

```terminal
ss -ltn
```

Inspect a specific port (example: `42000`):

```terminal
ss -ltn 'sport = :42000'
```

If your service should be running but a request fails, verify both:

1. The process is listening on the expected port.
2. You are using the correct host and port in your request.

> [!NOTE]
> `Windows` and `macOS` also have ports.
