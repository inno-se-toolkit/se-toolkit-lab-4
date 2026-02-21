# VM

<h2>Table of contents</h2>

- [What is a VM](#what-is-a-vm)
- [Your VM](#your-vm)
- [`<your-vm-name>`](#your-vm-name)
- [`<your-vm-ip-address>`](#your-vm-ip-address)
- [Prepare the connection](#prepare-the-connection)
- [Go to the VMs site](#go-to-the-vms-site)
- [Create a VM](#create-a-vm)
  - [Create a subscription](#create-a-subscription)
  - [Create a VM using the subscription](#create-a-vm-using-the-subscription)
- [Go to the VM page](#go-to-the-vm-page)
- [Get the `IP address` of the VM](#get-the-ip-address-of-the-vm)
- [Connect to the VM](#connect-to-the-vm)
- [Delete VM](#delete-vm)
- [Troubleshooting](#troubleshooting)
  - [`ping` times out](#ping-times-out)

## What is a VM

A virtual machine (`VM`) is a software-emulated computer that runs on a physical host machine, with its own [operating system](./operating-system.md) and isolated environment.
In this lab, you use a `VM` provided by the university to deploy and run the application remotely over [SSH](./ssh.md).

Docs:

- [What is a virtual machine?](https://azure.microsoft.com/en-us/resources/cloud-computing-dictionary/what-is-a-virtual-machine)

## Your VM

The university provides you a virtual machine (VM) for labs and home experiments for the duration of the `Software Engineering Toolkit` course.

You probably won't have access to the VMs after the course finishes.

See [VM image](./vm-info.md) for the information about your VM.

## `<your-vm-name>`

## `<your-vm-ip-address>`

The [IP address](./computer-networks.md)

## Prepare the connection

1. Disable `VPN`.
2. Connect your computer to the `Wi-Fi` network `UniversityStudent`.
3. [Run using the `VS Code Terminal`](./vs-code.md#run-a-command-using-the-vs-code-terminal):

   ```terminal
   ping <your-vm-ip-address>
   ```

   See [`<your-vm-ip-address>`](#your-vm-ip-address).

## Go to the VMs site

1. Open the [https://vm.innopolis.university](https://vm.innopolis.university) site in a browser.

## Create a VM

Complete these steps to create a VM:

<!-- no toc -->
1. [Create a subscription](#create-a-subscription)
2. [Create a new `SSH` key](./ssh.md#create-a-new-ssh-key)
3. [Create a VM using the subscription](#create-a-vm-using-the-subscription)

### Create a subscription

1. [Go to the VMs site](#go-to-the-vms-site).
2. Click `NEW`.
3. Click `ADD SUBSCRIPTION`.
4. Click `Software Engineering Toolkit`.
5. Click checkmark.
6. Go to the [`SUBSCRIPTIONS`](https://vm.innopolis.university/#Workspaces/MyAccountExtension/subscriptions) tab.
7. Look at the `SUBSCRIPTION` column.

   You should see there `Software Engineering Toolkit`.

   The `Status` of this subscription can be `Syncing` or `Active`.

   It can be `Syncing` for a long time.

   Nevertheless, you'll be able to [create a VM using this subscription](#create-a-vm-using-the-subscription) in approximately 15 minutes.

   Don't just sit and wait. Complete other steps.

### Create a VM using the subscription

1. [Create a new `SSH` key](./ssh.md#create-a-new-ssh-key) if not created.
2. [Go to the `vm.innopolis.university` site](#go-to-the-vms-site).
3. Click `+ NEW`.
4. Click `STANDALONE VIRTUAL MACHINE`.
5. Click `FROM GALLERY`.
6. Click `ALL`.
7. Click `Linux Ubuntu 24.04 Software Engineering Toolkit`.
8. Click `->` to go to the page 2.
9. Fill in the fields:
    `NAME`: Write the name of your VM (we'll refer to it as `<your-vm-name>` in the instructions).
    `NEW PASSWORD`: Write the password.
    `CONFIRM`: Write the same password.
    `ADMINISTRATOR SSH KEY`:
       1. [Find the `SSH` key files](./ssh.md#find-the-ssh-key-files).
       2. Copy the **full content** of the public key file.
       3. Paste the content into the input field.
10. Note that the user's name on the VM is [`root`](./linux.md#the-root-user).
11. Click `->` to go to the page 3.
12. Go to `NETWORK ADAPTER 1`.
13. Click `Not Connected`.
14. In the drop-down list, click `StudentsCourses01;10.93.24.0/22`.
15. Click checkmark to complete the setup.
16. The VM will become available in approximately 20 minutes.

## Go to the VM page

<!-- TODO open vm -->
1. [Go to the VMs site](#go-to-the-vms-site).
2. Open the `VIRTUALS MACHINES` tab ([https://vm.innopolis.university/#Workspaces/VMExtension/VirtualMachines](https://vm.innopolis.university/#Workspaces/VMExtension/VirtualMachines)).
3. Look at the `NAME`.
4. Find `<your-vm-name>`.
5. The `STATUS` should be `Running`.
6. Click `<your-vm-name>`.
7. Click `DASHBOARD`.
8. You should be on the VM page.

## Get the `IP address` of the VM

1. [Go to the VM page](#go-to-the-vm-page).
2. Go to the `quick glance` sidebar (on the right).
3. Go to `IP Address(es)`.
4. You should see there `StudentsCourses01 - 10.93.24.98`.
5. The `10.93.24.98` string is the [`IP address`](./computer-networks.md#ip-address) of the VM in a university network.
6. We'll refer to this string as `<your-vm-ip-address>`.

## Connect to the VM

1. [Add host to the `SSH` config](./ssh.md#add-the-host-to-ssh).
2. Disable `VPN`.
3. Connect your computer to the `Wi-Fi` network `UniversityStudent`.
4. Open [`VS Code`](./vs-code.md).
5. [Connect to the VM](./ssh.md#connect-to-the-vm).
6. If the connection is successful, you should see:
   1. The host fingerprint prompt (first connection only).
   2. A remote [shell prompt](./shell.md#shell-prompt) on the VM (for example, `root@<your-vm-name>:~#`).
   3. If you use the `ms-vscode-remote.remote-ssh` exntension in `VS Code`, the status bar should show that you are connected to a remote host.
7. Otherwise, see [troubleshooting](#troubleshooting).

## Delete VM

## Troubleshooting

### `ping` times out

1. Connect to the Wi `UniversityStudent`
2. recreate the VM.

   Use the same public key as before.

If you can't connect:

1. [Go to the VM page](#go-to-the-vm-page).
2. Verify the VM is in `Running` status.
3. Verify the VM `IP address` has not changed.
4. In your local terminal, test the [`SSH`](./ssh.md) connection in verbose mode:

   ```terminal
   ssh -v se-toolkit-vm
   ```

5. If you get `Permission denied (publickey)`, check:
   1. Your public key was added to the VM configuration.
   2. `IdentityFile` in your SSH config points to the correct private key.
   3. Your private key file permissions are correct (`chmod 600 ~/.ssh/se_toolkit_key` on Linux/macOS/WSL).
6. Ask the TA to help and show them:
   1. The VM page.
   2. The output of `ssh -v se-toolkit-vm`.
   3. Your [`VS Code Terminal`](./vs-code.md#vs-code-terminal).
