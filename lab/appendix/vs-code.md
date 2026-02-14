# `VS Code`

<h2>Table of contents</h2>

- [`Basic Layout`](#basic-layout)
- [`Custom Layout`](#custom-layout)
  - [Move the `Primary Sidebar` to the right](#move-the-primary-sidebar-to-the-right)
- [`Editor`](#editor)
- [`Activity Bar`](#activity-bar)
- [`Primary Sidebar`](#primary-sidebar)
  - [Open the `Primary Sidebar`](#open-the-primary-sidebar)
  - [Switch between `Primary Sidebar` views](#switch-between-primary-sidebar-views)
- [`Status Bar`](#status-bar)
- [`Editor Toolbar`](#editor-toolbar)
- [`Command Palette`](#command-palette)
  - [Open the `Command Palette`](#open-the-command-palette)
  - [Run a command using the `Command Palette`](#run-a-command-using-the-command-palette)
  - [Open the file using `Quick Open`](#open-the-file-using-quick-open)
  - [Select an option from a list](#select-an-option-from-a-list)
- [`Panel Toolbar`](#panel-toolbar)
- [`VS Code Terminal`](#vs-code-terminal)
  - [Open the `VS Code Terminal`](#open-the-vs-code-terminal)
  - [Close the `VS Code Terminal`](#close-the-vs-code-terminal)
  - [Open a new `VS Code Terminal`](#open-a-new-vs-code-terminal)
  - [Switch to another `VS Code Terminal`](#switch-to-another-vs-code-terminal)
  - [Copy text inside the `VS Code Terminal`](#copy-text-inside-the-vs-code-terminal)
  - [Paste text inside the `VS Code Terminal`](#paste-text-inside-the-vs-code-terminal)
  - [Check the current shell in the `VS Code Terminal`](#check-the-current-shell-in-the-vs-code-terminal)
  - [(`Windows` only) Set up running `VS Code` in `WSL`](#windows-only-set-up-running-vs-code-in-wsl)
  - [(`Windows` only) Set the default shell for the `VS Code Terminal`](#windows-only-set-the-default-shell-for-the-vs-code-terminal)
  - [Run a command using the `VS Code Terminal`](#run-a-command-using-the-vs-code-terminal)
- [`Explorer`](#explorer)
  - [Open the `Explorer`](#open-the-explorer)
  - [Open the file using the `Explorer`](#open-the-file-using-the-explorer)
- [`Source Control`](#source-control)
  - [Open the `Source Control`](#open-the-source-control)
  - [Close the `Source Control`](#close-the-source-control)
- [`Extensions`](#extensions)
  - [Open the `Extensions`](#open-the-extensions)
  - [Filter the `Extensions`](#filter-the-extensions)
  - [Install recommended `Extensions`](#install-recommended-extensions)
- [Keyboard shortcuts](#keyboard-shortcuts)
  - [Frequently used shortcuts](#frequently-used-shortcuts)
    - [Shortcut: Go back](#shortcut-go-back)
    - [Shortcut: Switch to the previous editor](#shortcut-switch-to-the-previous-editor)
    - [Shortcut: Search in the current editor](#shortcut-search-in-the-current-editor)
    - [Shortcut: Search in all files](#shortcut-search-in-all-files)
    - [Shortcut: Toggle line comment](#shortcut-toggle-line-comment)
- [Workspace settings](#workspace-settings)
  - [Change the workspace settings](#change-the-workspace-settings)
- [Common actions](#common-actions)
  - [(Windows only) Open the directory in `WSL`](#windows-only-open-the-directory-in-wsl)
  - [Open the file](#open-the-file)
  - [Open the `Markdown` preview](#open-the-markdown-preview)
- [Language server](#language-server)
  - [Type on hover](#type-on-hover)
  - [Docs on hover](#docs-on-hover)
  - [Go to the definition](#go-to-the-definition)
  - [Rename a symbol](#rename-a-symbol)

> [!IMPORTANT]
> The first [keyboard shortcut](#keyboard-shortcuts) is always for `Linux`.
> It usually coincides with the shortcut for `Windows`.
>
> You can check shortcuts for your platform in the [reference](https://code.visualstudio.com/docs/configure/keybindings#_keyboard-shortcuts-reference).

## `Basic Layout`

Default user interface (UI).

Docs:

- [Basic layout](https://code.visualstudio.com/docs/getstarted/userinterface#_basic-layout)
- [Visual Studio Code tips and tricks](https://code.visualstudio.com/docs/getstarted/tips-and-tricks)
- [UX Guidelines](https://code.visualstudio.com/api/ux-guidelines/overview)

Schema that we use in docs:

![Basic Layout Schema](../images/vs-code-ui.drawio.svg)

## `Custom Layout`

Custom UI appearance.

Docs:

- [Customizing VS Code's UI for Productivity](https://www.youtube.com/watch?v=nORT3-kONgA)
- [Custom Layout](https://code.visualstudio.com/docs/configure/custom-layout)

Actions:

- [Move the `Primary Sidebar` to the right](#move-the-primary-sidebar-to-the-right)

### Move the `Primary Sidebar` to the right

[Move](https://code.visualstudio.com/docs/configure/custom-layout#_primary-side-bar) the [`Primary Sidebar`](#primary-sidebar) to the right so that it doesn't move your code whenever the `Primary Sidebar` opens.

[Change the workspace settings](#change-the-workspace-settings) if you don't like that the `Primary Sidebar` on the right side.

## `Editor`

Space where you can edit files.

Location: see [`Basic Layout`](#basic-layout).

Docs:

- [Basic editing](https://code.visualstudio.com/docs/editing/codebasics)

## `Activity Bar`

Menus of extensions on a side of the [`Editor`](#editor).

Location: see [`Basic Layout`](#basic-layout).

## `Primary Sidebar`

Views on a side of the [`Editor`](#editor). See [`Basic Layout`](#basic-layout).

Docs:

- [Primary Side Bar](https://code.visualstudio.com/docs/configure/custom-layout#_primary-side-bar)

Actions:

- [Open the `Primary Sidebar`](#open-the-primary-sidebar)
- [Switch between `Primary Sidebar` views](#switch-between-primary-sidebar-views)

### Open the `Primary Sidebar`

For example, [open the `Source Control`](#open-the-source-control).

### Switch between `Primary Sidebar` views

Click icons in the [`Activity Bar`](#activity-bar).

## `Status Bar`

Statuses and menus of extensions at the bottom of the `VS Code` window.

- [docs](https://code.visualstudio.com/docs/getstarted/userinterface#_basic-layout)

<img alt="Status Bar (left)" src="../images/appendix/vs-code/status-bar-left.png" style="width:400px"></img>

<img alt="Status Bar (right)" src="../images/appendix/vs-code/status-bar-right.png" style="width:400px"></img>

## `Editor Toolbar`

Quick actions buttons located above the [`Editor`](#editor).

- [docs](https://code.visualstudio.com/api/ux-guidelines/overview#editor-toolbar)

<img alt="Editor Toolbar" src="../images/appendix/vs-code/editor-toolbar.png" style="width:400px"></img>

## `Command Palette`

Run editor commands in `VS Code`.

Docs:

- [Command Palette](https://code.visualstudio.com/docs/getstarted/userinterface#_command-palette)
- [Access commands with the Command Palette](https://code.visualstudio.com/docs/getstarted/getting-started#_access-commands-with-the-command-palette)

Actions:

- [Open the `Command Palette`](#open-the-command-palette)
- [Run a command using the `Command Palette`](#run-a-command-using-the-command-palette)
- [Open the file using `Quick Open`](#open-the-file-using-quick-open)

### Open the `Command Palette`

1. Press `Ctrl+Shift+P` (`Cmd+Shift+P` on `macOS`).

### Run a command using the `Command Palette`

1. [Open the `Command Palette`](#open-the-command-palette).
2. Start typing a command.
3. [Select](#select-an-option-from-a-list) the necessary command.

### Open the file using `Quick Open`

1. Press `Ctrl+P` (`Cmd+P` on `macOS`).
2. Start typing the name of the file.
3. [Select](#select-an-option-from-a-list) the file.

### Select an option from a list

Method 1:

1. Click the option.

Method 2:

1. Change the highlighted option using `UpArrow` and `DownArrow` on your keyboard.
2. Press `Enter` to confirm the option.

## `Panel Toolbar`

Switch between panels.

Location: see [`Basic Layout`](#basic-layout).

Left side with tabs:

<img alt="Panel Toolbar Left" src="../images/appendix/vs-code/panel-toolbar-left.png" style="width:400px"></img>

Right side (depends on the current tab; this one is for the `VS Code Terminal`):

<img alt="Panel Toolbar Right" src="../images/appendix/vs-code/panel-toolbar-left.png" style="width:400px"></img>

## `VS Code Terminal`

Run terminal commands inside `VS Code`.

Docs:

- [Getting started with the terminal](https://code.visualstudio.com/docs/terminal/getting-started)

Actions:

- [Open the `VS Code Terminal`](#open-the-vs-code-terminal)
- [Close the `VS Code Terminal`](#close-the-vs-code-terminal)
- [Open a new `VS Code Terminal`](#open-a-new-vs-code-terminal)
- [Switch to another `VS Code Terminal`](#switch-to-another-vs-code-terminal)
- [Copy text inside the `VS Code Terminal`](#copy-text-inside-the-vs-code-terminal)
- [Paste text inside the `VS Code Terminal`](#paste-text-inside-the-vs-code-terminal)
- [Run a command using the `VS Code Terminal`](#run-a-command-using-the-vs-code-terminal)

### Open the `VS Code Terminal`

Press ```Ctrl+` ``` (```Cmd+` ``` on `macOS`)

### Close the `VS Code Terminal`

Press ```Ctrl+` ``` (```Cmd+` ``` on `macOS`)

### Open a new `VS Code Terminal`

Use any of the following methods.

Method 1:

1. Press ```Ctrl+Shift+` ``` (```Cmd+Shift+` ``` on `macOS`).

Method 2:

1. [Open the `VS Code Terminal`](#open-the-vs-code-terminal).
2. Click the `+` icon.

   <img alt="New Terminal" src="../images/appendix/vs-code/terminal-new-plus.png" style="width:400px"></img>

### Switch to another `VS Code Terminal`

Use any of the following methods:

Method 1:

1. [Open the `VS Code Terminal`](#open-the-vs-code-terminal).
2. Click a terminal tab in the terminal panel.

    <img alt="Switch Terminal" src="../images/appendix/vs-code/terminal-panel-switch.png" style="width:400px"></img>

Method 2:

1. [Open the `VS Code Terminal`](#open-the-vs-code-terminal).
1. Press `Ctrl+PageDown` / `Ctrl+PageUp` (`Cmd+Shift+]` / `Cmd+Shift+[` on `macOS`).

### Copy text inside the `VS Code Terminal`

1. Select text.
2. Press `Ctrl+Shift+C` (`Cmd+C` on `macOS`).

### Paste text inside the `VS Code Terminal`

`Ctrl+Shift+V` (`Cmd+V` on `macOS`, `Ctrl+V` on `Windows`)

### Check the current shell in the `VS Code Terminal`

1. [Open the `VS Code Terminal`](#open-the-vs-code-terminal)
2. Look at the [`Panel Toolbar`](#panel-toolbar).

   <img alt="Current Terminal Shell" src="../images/appendix/vs-code/terminal-single-current-shell-bash.png" style="width:400px"></img>

   You should see on:
   - `Windows`: `bash` or `WSL`;

     If you see something else, [set the default shell](#windows-only-set-the-default-shell-for-the-vs-code-terminal).
   - `macOS`: `zsh` or `bash`;
   - `Linux`: `bash`, `fish`, `zsh`, or another shell name.

### (`Windows` only) Set up running `VS Code` in `WSL`

1. [Install recommended extensions](#install-recommended-extensions).

   They include the [`ms-vscode-remote.remote-wsl`](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-wsl) extension that lets you use `WSL` in `VS Code`.
1. Complete these steps of the [tutorial](https://code.visualstudio.com/docs/remote/wsl-tutorial):
   1. [Enable `WSL`](https://code.visualstudio.com/docs/remote/wsl-tutorial#_enable-wsl).
   2. [Install a `Linux` distro](https://code.visualstudio.com/docs/remote/wsl-tutorial#_install-a-linux-distro).
   3. Run using the current `WSL` terminal:

      ```terminal
      mkdir helloWorld
      cd helloWorld
      ```

   4. [Run `VS Code` in `WSL`](https://code.visualstudio.com/docs/remote/wsl-tutorial#_run-in-wsl).
   5. [End your `WSL` connection](https://code.visualstudio.com/docs/remote/wsl-tutorial#_ending-your-wsl-connection).

### (`Windows` only) Set the default shell for the `VS Code Terminal`

1. Make sure you can [run `VS Code` in WSL](#windows-only-set-up-running-vs-code-in-wsl).
2. [Run using the `Command Palette`](#run-a-command-using-the-command-palette):
   `Terminal: Select Default Profile`.
3. There can be the following cases.

   - Case 1 (bad): You don't have the recommended extensions installed.

     <img alt="Terminal Default Profile Bad Options" src="../images/appendix/vs-code/command-palette-default-terminal-profile-bad-options.png" style="width:400px"></img>

     Return to the first step and make sure you can [run `VS Code` in WSL](#windows-only-set-up-running-vs-code-in-wsl).
   - Case 2 (good): You're running `VS Code` outside `WSL`.

     <img alt="Terminal Default Profile Outside WSL" src="../images/appendix/vs-code/command-palette-default-terminal-profile-outside-wsl-wsl.png" style="width:400px"></img>

     [Select](#select-an-option-from-a-list) `Ubuntu (WSL)` or another option with `WSL` in the name.

     **Note:** [`Ubuntu`](./linux.md#ubuntu) is a [`Linux` distro](./linux.md#ubuntu).

   - Case 3 (the best): You're running `VS Code` inside `WSL`. You've probably [opened the directory inside `WSL`](#open-the-directory-in-wsl). This is the best case.

     <img alt="Terminal Default Profile Outside WSL" src="../images/appendix/vs-code/command-palette-default-terminal-profile-inside-wsl-bash.png" style="width:400px"></img>

     [Select](#select-an-option-from-a-list) `bash`.
4. [Open the `VS Code Terminal`](#open-the-vs-code-terminal).
5. Close all tabs in the `VS Code Terminal`.
6. [Open a new `VS Code Terminal`](#open-a-new-vs-code-terminal).

### Run a command using the `VS Code Terminal`

1. [Open the `VS Code Terminal`](#open-the-vs-code-terminal).
2. Write or [paste](#paste-text-inside-the-vs-code-terminal) a command.
3. Press `Enter`.

## `Explorer`

View the file tree.

Location: [`Activity Bar`](#activity-bar).

Docs:

- [Explorer view](https://code.visualstudio.com/docs/getstarted/userinterface#_explorer-view)

Actions:

- [Open the `Explorer`](#open-the-explorer)
- [Open the file using the `Explorer`](#open-the-file-using-the-explorer)

### Open the `Explorer`

1. Go to the [`Activity Bar`](#activity-bar).
2. Click the `Explorer` icon.

   <img alt="Explorer" src="../images/appendix/vs-code/activity-bar-explorer.png" style="width:100px"></img>

### Open the file using the `Explorer`

1. [Open the `Explorer`](#open-the-explorer).
2. Search for the file in the file tree.
3. Click it.

## `Source Control`

Interact with `Git` via `VS Code` UI.

Docs:

- [Source Control in VS Code](https://code.visualstudio.com/docs/sourcecontrol/overview)

Actions:

- [Open the `Source Control`](#open-the-source-control)
- [Close the `Source Control`](#close-the-source-control)

### Open the `Source Control`

Method 1:

1. Go to the [`Activity Bar`](#activity-bar).
2. Click `Source Control`.

   <img alt="Activity Bar - Source Control" src="../images/appendix/vs-code/activity-bar-source-control.png" style="width:100px"></img>
3. Click `CHANGES` to uncollapse the view.

   <img alt="Source Control - Changes" src="../images/appendix/vs-code/source-control-changes.png" style="width:100px"></img>
  
Method 2:

1. Press `Ctrl+Shift+G G` (`Ctrl+Shift+G` on `macOS`)
2. Click `CHANGES` to uncollapse the view.

### Close the `Source Control`

Method 1:

1. Go to the [`Activity Bar`](#activity-bar)
2. Click `Source Control`.

   <img alt="Explorer" src="../images/appendix/vs-code/activity-bar-source-control.png" style="width:100px"></img>

Method 2:

1. Click outside of the [`Editor`](#editor).
2. Press `Ctrl+B` (`Cmd+B` on `macOS`).

## `Extensions`

Install extensions for `VS Code` from [`VS Code Marketplace`](https://marketplace.visualstudio.com/vscode) to enable new functionality.

Docs:

- [Extension Marketplace](https://code.visualstudio.com/docs/configure/extensions/extension-marketplace)

Actions:

- [Open the `Extensions`](#open-the-extensions)
- [Filter the `Extensions`](#filter-the-extensions)
- [Install recommended `Extensions`](#install-recommended-extensions)

### Open the `Extensions`

Method 1:

1. Go to the [`Activity Bar`](#activity-bar).
2. Click the icon `Extensions`.

Method 2:

1. Press `Ctrl+Shift+X` (`Cmd+Shift+X` on `macOS`).

### Filter the `Extensions`

1. [Open the `Extensions`](#open-the-extensions).
2. Click the icon `Filter Extensions...`.

   <img alt="Filter Extensions" src="../images/appendix/vs-code/extensions-filter.png" style="width:400px"></img>
3. A menu will open.
4. Select a filter in the menu and click it to apply the filter.

### Install recommended `Extensions`

> [!NOTE]
> Recommended extensions are listed in [`.vscode/extensions.json`](../../.vscode/extensions.json).

1. [Filter the extensions](#filter-the-extensions).
2. Click `Recommended` in the menu.
3. Click `WORKSPACE RECOMMENDATIONS` to uncollapse this view.
4. Click the icon `Install Workspace Recommended extensions`.

   <img alt="Install Workspace Recommended Extensions" src="../images/appendix/vs-code/extensions-install-workspace-recommended.png" style="width:400px"></img>

## Keyboard shortcuts

Keyboard shortcuts for various commands.

Docs:

- [Keyboard Shortcuts reference](https://code.visualstudio.com/docs/configure/keybindings#_keyboard-shortcuts-reference)
- [Keyboard Shortcuts editor](https://code.visualstudio.com/docs/configure/keybindings#_keyboard-shortcuts-editor)

### Frequently used shortcuts

- [Go back](#shortcut-go-back)
- [Switch to the previous editor](#shortcut-switch-to-the-previous-editor)
- [Search in the current editor](#shortcut-search-in-the-current-editor)
- [Search in all files](#shortcut-search-in-all-files)
- [Toggle line comment](#shortcut-toggle-line-comment)

#### Shortcut: Go back

`Alt+-` (`Ctrl+-` on `macOS`)

#### Shortcut: Switch to the previous editor

`Ctrl+Tab`

#### Shortcut: Search in the current editor

`Ctrl+F` (`Cmd+F` on `macOS`)

#### Shortcut: Search in all files

`Ctrl+Shift+F` (`Cmd+Shift+F` on `macOS`)

#### Shortcut: Toggle line comment

`Ctrl+/` (`Cmd+/` on `macOS`)

> [!TIP]
> This shortcut also works for a sequence of lines:
>
> 1. Select lines.
> 2. Press the shortcut.

## Workspace settings

`VS Code` settings for the workspace.

Docs:

- [What is a VS Code workspace?](https://code.visualstudio.com/docs/editing/workspaces/workspaces)
- [Workspace settings](https://code.visualstudio.com/docs/configure/settings#_workspace-settings)
- [Settings JSON file](https://code.visualstudio.com/docs/configure/settings#_settings-json-file)

Settings for this workspace are in [`.vscode/settings.json`](../../.vscode/settings.json).

### Change the workspace settings

Here are some [workspace settings](#workspace-settings) that you can change:

- [`files.autoSave`](https://code.visualstudio.com/docs/editing/codebasics#_save-auto-save) - Enabled to save your work if VS Code closes;
- [`editor.formatOnSave`](https://code.visualstudio.com/docs/editing/codebasics#_formatting) - Enabled to run formatters when you press `Ctrl+S` (or `Cmd+S` on `macOS`) to save code.
- `Markdown` editor and preview [synchronization settings](https://code.visualstudio.com/docs/languages/markdown#_editor-and-preview-synchronization) - Disabled for smoother scrolling of the editor and the preview.

## Common actions

### (Windows only) Open the directory in `WSL`

1. [Run using the `Command Palette`](./appendix/vs-code.md#command-palette):
   `WSL: Open Folder in WSL...`
2. Click `Show Local`.
3. Select the directory.
4. [Check the current shell in the `VS Code Terminal`](#check-the-current-shell-in-the-vs-code-terminal).

### Open the file

Method 1: [Open the file using `Quick Open`](#open-the-file-using-quick-open)

Method 2: [Open the file using the `Explorer`](#open-the-file-using-the-explorer)

### Open the `Markdown` preview

> [!NOTE]
> See [`Markdown`](./file-formats.md#markdown).

Method 1:

1. Go to the [`Editor Toolbar`](./appendix/vs-code.md#editor-toolbar).
2. Click `Open Preview to the Side`.

Method 2:

1. [Run using the `Command Palette`](./appendix/vs-code.md#run-a-command-using-the-command-palette):

  `Markdown: Open Preview to the Side`

## Language server

### Type on hover

### Docs on hover

### Go to the definition

### Rename a symbol
