# `VS Code`

- [`Basic Layout`](#basic-layout)
- [`Custom Layout`](#custom-layout)
- [`Editor`](#editor)
- [`Activity Bar`](#activity-bar)
- [`Primary Sidebar`](#primary-sidebar)
  - [Open the `Primary Sidebar`](#open-the-primary-sidebar)
  - [Switch between views](#switch-between-views)
- [`Status Bar`](#status-bar)
- [`Editor Toolbar`](#editor-toolbar)
- [`Command Palette`](#command-palette)
  - [Open the `Command Palette`](#open-the-command-palette)
  - [Run a command using the `Command Palette`](#run-a-command-using-the-command-palette)
  - [Open a file using the `Command Palette`](#open-a-file-using-the-command-palette)
- [`Terminal`](#terminal)
  - [Open the `Terminal`](#open-the-terminal)
  - [Close the `Terminal`](#close-the-terminal)
  - [Copy text inside the `Terminal`](#copy-text-inside-the-terminal)
  - [Paste text inside the `Terminal`](#paste-text-inside-the-terminal)
  - [Run a command using the `Terminal`](#run-a-command-using-the-terminal)
- [`Folders`](#folders)
  - [Open the `Folders`](#open-the-folders)
- [`Source Control`](#source-control)
  - [Open the `Source Control`](#open-the-source-control)
  - [Close the `Source Control`](#close-the-source-control)
- [`Extensions`](#extensions)
  - [Open the `Extensions`](#open-the-extensions)
  - [Filter the `Extensions`](#filter-the-extensions)
  - [Install recommended `Extensions`](#install-recommended-extensions)
  - [Use cases](#use-cases)
    - [Move the `Primary Sidebar` to the right](#move-the-primary-sidebar-to-the-right)
- [Keyboard shortcuts](#keyboard-shortcuts)
  - [Frequently used shortcuts](#frequently-used-shortcuts)
- [Workspace settings](#workspace-settings)
  - [Change the workspace settings](#change-the-workspace-settings)

> [!IMPORTANT]
> The first [keyboard shortcut](#keyboard-shortcuts) is always for `Linux`.
> It usually coincides with the shortcut for `Windows`.
>
> You can check shortcuts for your platform in the [reference](https://code.visualstudio.com/docs/configure/keybindings#_keyboard-shortcuts-reference).

## `Basic Layout`

Default user interface (UI).

- [docs 1](https://code.visualstudio.com/docs/getstarted/userinterface#_basic-layout)
- [docs 2](https://code.visualstudio.com/docs/getstarted/tips-and-tricks)

Slightly modified `Basic Layout` schema:

![Basic Layout Schema](../images/vs-code-ui.drawio.svg)

- [Basic layout](https://code.visualstudio.com/docs/getstarted/userinterface#_basic-layout)
- [UX Guidelines](https://code.visualstudio.com/api/ux-guidelines/overview)

## `Custom Layout`

Custom UI appearance.

- [docs 1](https://www.youtube.com/watch?v=nORT3-kONgA)
- [docs 2](https://code.visualstudio.com/docs/configure/custom-layout)

## `Editor`

Space where you can edit files. See [`Basic Layout`](#basic-layout).

- [docs](https://code.visualstudio.com/docs/editing/codebasics)

## `Activity Bar`

Menus of extensions on a side of the [`Editor`](#editor). See [`Basic Layout`](#basic-layout).

- [docs](https://code.visualstudio.com/docs/getstarted/userinterface#_basic-layout)

## `Primary Sidebar`

Views on a side of the [`Editor`](#editor). See [`Basic Layout`](#basic-layout).

- [docs](https://code.visualstudio.com/docs/configure/custom-layout#_primary-side-bar)

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

<img alt="Status Bar (left)" src="../images/appendix/vs-code/status-bar-left.png" style="width:200px"></img>

<img alt="Status Bar (right)" src="../images/appendix/vs-code/status-bar-right.png" style="width:400px"></img>

## `Editor Toolbar`

Quick actions buttons located above the [`Editor`](#editor).

- [docs](https://code.visualstudio.com/api/ux-guidelines/overview#editor-toolbar)

## `Command Palette`

Run editor commands.

- [docs 1](https://code.visualstudio.com/docs/getstarted/userinterface#_command-palette)
- [docs 2](https://code.visualstudio.com/docs/getstarted/getting-started#_access-commands-with-the-command-palette)

Actions:

- [Open the `Command Palette`](#open-the-command-palette)
- [Run a command using the `Command Palette`](#run-a-command-using-the-command-palette)
- [Open a file using the `Command Palette`](#open-a-file-using-the-command-palette)

### Open the `Command Palette`

1. Press `Ctrl+Shift+P` (`Cmd+Shift+P` on `macOS`).

### Run a command using the `Command Palette`

1. [Open the `Command Palette`](#open-the-command-palette).
1. Start typing a command.
1. Select the necessary command (move the cursor via `UpArrow` and `DownArrow` on your keyboard).
1. Press `Enter` or click the necessary command.

### Open a file using the `Command Palette`

1. Press `Ctrl+P` (`Cmd+P` on `macOS`).
2. Start typing the name of the file.
3. Select a file (move the cursor via `UpArrow` and `DownArrow` on your keyboard).
4. Press `Enter`.

## `Terminal`

Run terminal commands inside `VS Code`.

- [docs](https://code.visualstudio.com/docs/terminal/getting-started)

Actions:

- [Open the `Terminal`](#open-the-terminal)
- [Close the `Terminal`](#close-the-terminal)
- [Copy text inside the `Terminal`](#copy-text-inside-the-terminal)
- [Paste text inside the `Terminal`](#paste-text-inside-the-terminal)
- [Run a command using the `Terminal`](#run-a-command-using-the-terminal)

### Open the `Terminal`

Press ```Ctrl+` ``` (```Cmd+` ``` on `macOS`)

### Close the `Terminal`

Press ```Ctrl+` ``` (```Cmd+` ``` on `macOS`)

### Copy text inside the `Terminal`

1. Select text.
1. Press `Ctrl+Shift+C` (`Cmd+C` on `macOS`).

### Paste text inside the `Terminal`

`Ctrl+Shift+V` (`Cmd+V` on `macOS`, `Ctrl+V` on `Windows`)

### Run a command using the `Terminal`

1. [Open the `Terminal`](#open-the-terminal).
1. Write or [paste](#paste-text-inside-the-terminal) a command.
1. Press `Enter`.

## `Folders`

View the file tree.

- [docs](https://code.visualstudio.com/docs/getstarted/userinterface#_explorer-view)

Actions:

- [Open the `Folders`](#open-the-folders)

### Open the `Folders`

1. Go to the [`Activity Bar`](#activity-bar).
2. Click `Folders`.

## `Source Control`

Interact with `Git` via `VS Code` UI.

- [docs](https://code.visualstudio.com/docs/sourcecontrol/overview)

Actions:

- [Open the `Source Control`](#open-the-source-control)
- [Close the `Source Control`](#close-the-source-control)

### Open the `Source Control`

Approach 1:

1. Go to the [`Activity Bar`](#activity-bar).
2. Click `Source Control`.
3. Click `CHANGES` to uncollapse the view.
  
Approach 2:

1. Press `Ctrl+Shift+G G` (`Ctrl+Shift+G` on `macOS`)
2. Click `CHANGES` to uncollapse the view.

### Close the `Source Control`

Approach 1:

1. Go to the [`Activity Bar`](#activity-bar)
2. Click `Source Control`.

Approach 2:

1. Press `Ctrl+B` (`Cmd+B` on `macOS`)

## `Extensions`

Install extensions for `VS Code` from [`VS Code Marketplace`](https://marketplace.visualstudio.com/vscode) to enable new functionality.

- [docs](https://code.visualstudio.com/docs/configure/extensions/extension-marketplace)

Actions:

- [Open the `Extensions`](#open-the-extensions)
- [Filter the `Extensions`](#filter-the-extensions)
- [Install recommended `Extensions`](#install-recommended-extensions)

### Open the `Extensions`

Approach 1:

1. Go to the [`Activity Bar`](#activity-bar).
2. Click the icon `Extensions`.

Approach 2:

1. Press `Ctrl+Shift+X` (`Cmd+Shift+X` on `macOS`).

### Filter the `Extensions`

1. [Open the `Extensions`](#open-the-extensions).
2. Click the icon `Filter Extensions...`.

   <img alt="Filter Extensions" src="../images/appendix/vs-code/extensions-filter.png" style="width:400px"></img>
3. A menu will open.
4. Select a filter in the menu and click it to apply the filter.

### Install recommended `Extensions`

> [!NOTE]
> Recommended extensions are listed in [`.vscode/extensions.json`](../.vscode/extensions.json).

1. [Filter the extensions](#filter-the-extensions).
2. Click `Recommended` in the menu.
3. Click `WORKSPACE RECOMMENDATIONS` to uncollapse this view.
4. Click the icon `Install Workspace Recommended extensions`.

   <img alt="Filter Extensions" src="../images/appendix/vs-code/extensions-install-workspace-recommended.png" style="width:400px"></img>

### Use cases

#### Move the `Primary Sidebar` to the right

[Move](https://code.visualstudio.com/docs/configure/custom-layout#_primary-side-bar) the [`Primary Sidebar`](#primary-sidebar) to the right so that it doesn't move your code whenever the `Primary Sidebar` opens.

[Change the workspace settings](#change-the-workspace-settings) if you don't like that the `Primary Sidebar` on the right side.

## Keyboard shortcuts

Keyboard shortcuts for various commands.

- [docs 1](https://code.visualstudio.com/docs/configure/keybindings#_keyboard-shortcuts-reference)
- [docs 2](https://code.visualstudio.com/docs/configure/keybindings#_keyboard-shortcuts-editor)

### Frequently used shortcuts

- `Alt+-` (`Ctrl+-` on `macOS`) - go back.
- `Ctrl+Tab` - switch to the previous editor.
- `Ctrl+F` (`Cmd+F` on `macOS`) - search in the current editor.
- `Ctrl+Shift+F` (`Cmd+Shift+F` on `macOS`) - search in all files.

## Workspace settings

`VS Code` settings for the workspace.

- [docs](https://code.visualstudio.com/docs/editing/workspaces/workspaces)
- [docs 1](https://code.visualstudio.com/docs/configure/settings#_workspace-settings)
- [docs 2](https://code.visualstudio.com/docs/configure/settings#_settings-json-file)

Settings for this workspace are in [`.vscode/settings.json`](../../.vscode/settings.json).

### Change the workspace settings

Here are some [workspace settings](#workspace-settings) that you can change:

- [`files.autoSave`](https://code.visualstudio.com/docs/editing/codebasics#_save-auto-save) - Enabled to save your work if VS Code closes;
- [`editor.formatOnSave`](https://code.visualstudio.com/docs/editing/codebasics#_formatting) - Enabled to run formatters when you press `Ctrl+S` (or `Cmd+S` on `macOS`) to save code.
- `Markdown` editor and preview [synchronization settings](https://code.visualstudio.com/docs/languages/markdown#_editor-and-preview-synchronization) - Disabled for smoother scrolling of the editor and the preview.
