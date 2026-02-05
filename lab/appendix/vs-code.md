# `VS Code`

## `Basic Layout`

Basic UI elements in `VS Code`.

![VS Code UI](../images/vs-code-ui.png)

Docs:

- [docs 1](https://code.visualstudio.com/docs/getstarted/userinterface#_basic-layout)

## `Activity Bar`

Menus of extensions on the side.

Docs:

- [docs 1](https://code.visualstudio.com/docs/getstarted/userinterface#_basic-layout)

## `Status Bar`

Statuses and menus of extensions at the bottom.

Docs:

- [docs 1](https://code.visualstudio.com/docs/getstarted/userinterface#_basic-layout)

## `Command Palette`

Run editor commands.

Docs:

- [docs 1](https://code.visualstudio.com/docs/getstarted/userinterface#_command-palette)
- [docs 2](https://code.visualstudio.com/docs/getstarted/getting-started#_access-commands-with-the-command-palette)

To run a command:

1. Open `Command Palette`: `Ctrl+Shift+P` (`Cmd+Shift+P` on `macOS`).
1. Start typing a command.
1. Select the necessary command (move the cursor via arrow up and arrow down on your keyboard).
1. Press `Enter`.

## `Terminal`

Run terminal commands inside `VS Code`.

Docs:

- [docs 1](https://code.visualstudio.com/docs/terminal/getting-started)

To open a terminal:

- Press ```Ctrl+` ``` (```Cmd+` ``` on `macOS`)

To close a terminal:

- Press ```Ctrl+` ``` (```Cmd+` ``` on `macOS`)

## `Source Control`

Interact with `git` via `VS Code` UI.

Ways to open:

- [`Activity Bar`](#activity-bar) -> Click `Source Control`
- `Ctrl+Shift+G G` or `Ctrl+Shift+G` on `macOS`

Ways to close:

- [`Activity Bar`](#activity-bar) -> Click `Source Control`
- `Ctrl+B` (`Cmd+B` on `macOS`)

Docs:

- [docs 1](https://code.visualstudio.com/docs/sourcecontrol/overview)

## `Extensions`

Install extensions for `VS Code` from [`VS Code Marketplace`](https://marketplace.visualstudio.com/vscode) to enable new functionality.

Docs:

- [docs 1](https://code.visualstudio.com/docs/configure/extensions/extension-marketplace)

## `Custom Layout`

Change the [Basic Layout](#basic-layout).

Docs:

- [docs 1](https://code.visualstudio.com/docs/configure/custom-layout)

Use cases:

- [Move](https://code.visualstudio.com/docs/configure/custom-layout#_primary-side-bar) the `Primary Side Bar` to the right so that it doesn't move your code whenever the `Primary Side Bar` opens.

## Keyboard shortcuts

Keyboard shortcuts for various commands.

Docs:

- [docs 1](https://code.visualstudio.com/docs/configure/keybindings#_keyboard-shortcuts-reference).

## `settings.json`

Workspace settings in a `JSON` file that you can store in the repo and share with other collaborators.

This repo has [`.vscode/settings.json`](../../.vscode/settings.json).

Docs:

- [docs 1](https://code.visualstudio.com/docs/configure/settings#_settings-json-file).

### Settings

- [`files.autoSave`](https://code.visualstudio.com/docs/editing/codebasics#_save-auto-save) - Enabled to save your work if VS Code closes;
- [`editor.formatOnSave`](https://code.visualstudio.com/docs/editing/codebasics#_formatting) - Enabled to run formatters when you press `Ctrl+S` (or `Cmd+S` on `macOS`) to save code.
