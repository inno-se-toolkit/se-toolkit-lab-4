# VM

- [Your VM](#your-vm)
- [Create a VM](#create-a-vm)
  - [Create a subscription](#create-a-subscription)
  - [Create a VM using the subscription](#create-a-vm-using-the-subscription)
- [Go to the VM page](#go-to-the-vm-page)
- [Get the `IP address` of the VM](#get-the-ip-address-of-the-vm)
- [Connect to the VM](#connect-to-the-vm)
- [Troubleshooting](#troubleshooting)

## Your VM

The university provides you a virtual machine (VM) for labs and home experiments.

## Create a VM

Complete these steps to create a VM:

<!-- no toc -->
1. [Create a subscription](#create-a-subscription)
2. [Create a new `SSH` key](./ssh.md#create-a-new-ssh-key)
3. [Create a VM using the subscription](#create-a-vm-using-the-subscription)

### Create a subscription

1. Go to [`https://vm.innopolis.university`](https://vm.innopolis.university/).
2. Click `NEW`.
3. Click `ADD SUBSCRIPTION`.
4. Click `Software Engineering Toolkit`.
5. Click checkmark.
6. Go to the [`SUBSCRIPTIONS`](https://vm.innopolis.university/#Workspaces/MyAccountExtension/subscriptions) tab.
7. Look at the `SUBSCRIPTION` column.
8. You should see there `Software Engineering Toolkit`.
9. The `Status` of this subscription may be `Syncing` or `Active`.
10. It can be `Syncing` for a long time.
11. You'll be able to [create a VM using this subscription](#create-a-vm-using-the-subscription) in approximately 15 minutes.

### Create a VM using the subscription

1. [Create a new SSH key](./ssh.md#create-a-new-ssh-key).
2. Go to [`https://vm.innopolis.university`](https://vm.innopolis.university/).
3. Click `+ NEW`.
4. Click `STANDALONE VIRTUAL MACHINE`.
5. Click `FROM GALLERY`.
6. Click `ALL`.
7. Click `Linux Ubuntu 24.04 Software Engineering Toolkit`.
8. Click `->` to go to the page 2.
9. Fill in the fields:
10. `NAME`: Write the name of your VM (we'll refer to it as `<your-vm-name>`).
11. `NEW PASSWORD`: Write the password.
12. `CONFIRM`: Write the same password.
13. `ADMINISTRATOR SSH KEY`:
      1. [Find the `SSH` key files](./ssh.md#find-the-ssh-key-files).
      2. Paste here the public key.
14. Note that the user's name on the VM is `root`.
15. Click `->` to go to the page 3.
16. Go to `NETWORK ADAPTER 1`.
17. Click `Not Connected`.
18. In the drop-down list, click `StudentsCourses01;10.93.24.0/22`.
19. Click checkmark to complete the setup.
20. The VM will become available in approximately 20 minutes.

## Go to the VM page

1. Go to the [`VIRTUALS MACHINES`](https://vm.innopolis.university/#Workspaces/VMExtension/VirtualMachines) tab.
2. Look at the `NAME`.
3. Find `<your-vm-name>`.
4. The `STATUS` should be `Running`.
5. Click `<your-vm-name>`.
6. You should be on the VM page.

## Get the `IP address` of the VM

1. Go to the `quick glance` sidebar.
2. Go to `IP Address(es)`.
3. You should see there `StudentsCourses01 - 10.93.24.98`.
4. The `10.93.24.98` string is the `IP address` of the VM in a university network.
5. We'll refer to this string as `<your-vm-ip-address>`.

## Connect to the VM

1. [Add host to the `SSH` config](./ssh.md#add-host-to-the-ssh-config).
2. Connect your computer to the `Wi-Fi` network `UniversityStudent`.
3. Open `VS Code`.
4. [Connect to the VM](./ssh.md#connect-to-the-new-host)

<!-- TODO what should you see? -->

## Troubleshooting

If you can't connect:

1. [Go to the VM page](#go-to-the-vm-page).
2. Ask the TA to help and show them the VM page and your [`Terminal`](./vs-code.md#terminal).
