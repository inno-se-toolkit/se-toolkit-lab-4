# `VS Code`

- [`Basic Layout`](#basic-layout)
- [`Activity Bar`](#activity-bar)
- [`Primary Sidebar`](#primary-sidebar)
  - [Open the `Primary Sidebar`](#open-the-primary-sidebar)
- [`Status Bar`](#status-bar)
- [`Editor Toolbar`](#editor-toolbar)
- [`Command Palette`](#command-palette)
  - [Open the `Command Palette`](#open-the-command-palette)
  - [Run a command using the `Command Palette`](#run-a-command-using-the-command-palette)
  - [Open a file using the `Command Palette`](#open-a-file-using-the-command-palette)
- [`Terminal`](#terminal)
  - [Open the `Terminal`](#open-the-terminal)
  - [Close the `Terminal`](#close-the-terminal)
  - [Copy inside the `Terminal`](#copy-inside-the-terminal)
  - [Paste inside the `Terminal`](#paste-inside-the-terminal)
  - [Run a command using the `Terminal`](#run-a-command-using-the-terminal)
- [`Folders`](#folders)
  - [Open `Folders`](#open-folders)
- [`Source Control`](#source-control)
  - [Open the `Source Control`](#open-the-source-control)
  - [Close the `Source Control`](#close-the-source-control)
- [`Extensions`](#extensions)
  - [Install recommended extensions](#install-recommended-extensions)
- [`Custom Layout`](#custom-layout)
  - [Use cases](#use-cases)
- [Keyboard shortcuts](#keyboard-shortcuts)
  - [Frequently used shortcuts](#frequently-used-shortcuts)
- [`settings.json`](#settingsjson)
  - [Workspace settings](#workspace-settings)

> [!IMPORTANT]
> The first [keyboard shortcut](#keyboard-shortcuts) is always for `Linux`.
> It usually coincides with the shortcut for `Windows`.
>
> You can check shortcuts for your platform in the [reference](https://code.visualstudio.com/docs/configure/keybindings#_keyboard-shortcuts-reference).

## `Basic Layout`

Basic layout elements in `VS Code`:

![VS Code UI](../images/vs-code-ui.drawio.svg)

Docs:

- [docs 1](https://code.visualstudio.com/docs/getstarted/userinterface#_basic-layout)
- [docs 2](https://code.visualstudio.com/api/ux-guidelines/overview#items)

## `Activity Bar`

Menus of extensions on a side of the editor.

- [docs](https://code.visualstudio.com/docs/getstarted/userinterface#_basic-layout)

## `Primary Sidebar`

Panels and views on a side of the editor.

### Open the `Primary Sidebar`

For example, [open the `Source Control`](#open-the-source-control).

## `Status Bar`

Statuses and menus of extensions at the bottom of the `VS Code` window.

- [docs](https://code.visualstudio.com/docs/getstarted/userinterface#_basic-layout)

## `Editor Toolbar`

Quick actions buttons located above the editor.

- [docs](https://code.visualstudio.com/api/ux-guidelines/overview#editor-toolbar)

## `Command Palette`

Run editor commands.

- [docs 1](https://code.visualstudio.com/docs/getstarted/userinterface#_command-palette)
- [docs 2](https://code.visualstudio.com/docs/getstarted/getting-started#_access-commands-with-the-command-palette)

### Open the `Command Palette`

1. Press `Ctrl+Shift+P` (`Cmd+Shift+P` on `macOS`).

### Run a command using the `Command Palette`

1. [Open the `Command Palette`](#open-the-command-palette).
1. Start typing a command.
1. Select the necessary command (move the cursor via `UpArrow` and `DownArrow` on your keyboard).
1. Press `Enter`.

### Open a file using the `Command Palette`

1. Press `Ctrl+P` (`Cmd+P` on `macOS`).
2. Start typing the name of the file.
3. Select a file (move the cursor via `UpArrow` and `DownArrow` on your keyboard).
4. Press `Enter`.

## `Terminal`

Run terminal commands inside `VS Code`.

- [docs](https://code.visualstudio.com/docs/terminal/getting-started)

### Open the `Terminal`

Press ```Ctrl+` ``` (```Cmd+` ``` on `macOS`)

### Close the `Terminal`

Press ```Ctrl+` ``` (```Cmd+` ``` on `macOS`)

### Copy inside the `Terminal`

1. Select text.
1. Press `Ctrl+Shift+C` (`Cmd+C` on `macOS`).

### Paste inside the `Terminal`

`Ctrl+Shift+V` (`Cmd+V` on `macOS`, `Ctrl+V` on `Windows`)

### Run a command using the `Terminal`

1. [Open the `Terminal`](#open-the-terminal).
1. Write or [paste](#paste-inside-the-terminal) a command.
1. Press `Enter`.

## `Folders`

View the file tree.

- [docs](https://code.visualstudio.com/docs/editing/workspaces/workspaces)

### Open `Folders`

[`Activity Bar`](#activity-bar) -> Click `Folders`.

## `Source Control`

Interact with `Git` via `VS Code` UI.

- [docs](https://code.visualstudio.com/docs/sourcecontrol/overview)

### Open the `Source Control`

Approaches:

- [`Activity Bar`](#activity-bar) -> Click `Source Control`
- `Ctrl+Shift+G G` (`Ctrl+Shift+G` on `macOS`)

### Close the `Source Control`

Approaches:

- [`Activity Bar`](#activity-bar) -> Click `Source Control`
- `Ctrl+B` (`Cmd+B` on `macOS`)

## `Extensions`

Install extensions for `VS Code` from [`VS Code Marketplace`](https://marketplace.visualstudio.com/vscode) to enable new functionality.

- [docs](https://code.visualstudio.com/docs/configure/extensions/extension-marketplace)

### Install recommended extensions

> [!NOTE]
> Recommended extensions are listed in [`.vscode/extensions.json`](../.vscode/extensions.json).

1. Open `Extensions`:

   - Approach 1:

      1. Go to the [`Activity Bar`](#activity-bar).
      2. Click the icon `Extensions`.

   - Approach 2:
     1. Press `Ctrl+Shift+X` (`Cmd+Shift+X` on `macOS`).

2. In the input field, type `@recommended`.
3. Look at `WORKSPACE RECOMMENDATIONS`.
4. Click the icon `Install Workspace Recommended extensions`.

## `Custom Layout`

Change the [Basic Layout](#basic-layout).

- [docs](https://code.visualstudio.com/docs/configure/custom-layout)

### Use cases

- [Move](https://code.visualstudio.com/docs/configure/custom-layout#_primary-side-bar) the `Primary Side Bar` to the right so that it doesn't move your code whenever the `Primary Side Bar` opens. This setting is already used in [`.vscode/settings.json`](../../.vscode/settings.json).

## Keyboard shortcuts

Keyboard shortcuts for various commands.

- [docs 1](https://code.visualstudio.com/docs/configure/keybindings#_keyboard-shortcuts-reference)
- [docs 2](https://code.visualstudio.com/docs/configure/keybindings#_keyboard-shortcuts-editor)

### Frequently used shortcuts

- `Alt+-` (`Ctrl+-` on `macOS`) - go back.
- `Ctrl+Tab` - switch to the previous editor.
- `Ctrl+F` (`Cmd+F` on `macOS`) - search in the current editor.
- `Ctrl+Shift+F` (`Cmd+Shift+F` on `macOS`) - search in all files.

## `settings.json`

Workspace settings in a `JSON` file that you can store in the repo and share with other collaborators.

Docs:

- [docs](https://code.visualstudio.com/docs/configure/settings#_settings-json-file)

### Workspace settings

The settings for this repo workspace are in [`.vscode/settings.json`](../../.vscode/settings.json).

Here are some settings that you can change:

- [`files.autoSave`](https://code.visualstudio.com/docs/editing/codebasics#_save-auto-save) - Enabled to save your work if VS Code closes;
- [`editor.formatOnSave`](https://code.visualstudio.com/docs/editing/codebasics#_formatting) - Enabled to run formatters when you press `Ctrl+S` (or `Cmd+S` on `macOS`) to save code.
- `Markdown` editor and preview [synchronization settings](https://code.visualstudio.com/docs/languages/markdown#_editor-and-preview-synchronization) - Disabled for smoother scrolling of the editor and the preview.
