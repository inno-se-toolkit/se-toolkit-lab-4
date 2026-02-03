# Lab setup

## Find a partner

1. Find a classmate to be your partner for this lab.
2. Sit together.

## Set up a fork

1. Create a `GitHub` account.
2. Fork this repo to your `GitHub` account and make your fork public.
3. Continue your work in the forked repo.
4. In the repo -> `Settings` -> `General` -> `Features`, enable `Issues`.
5. <details> <summary> (Optional) Create a label for tasks (click to expand).</summary>

   In the repo -> `Issues` -> `Labels`, create a new label:
   1. Click `New label`.
   2. Name: `task`.
   3. Click `Create label`.

   </details>

6. <details> <summary>(Optional) Protect your <code>main</code> branch (click to expand).</summary>

   In the repo -> `Settings` -> `Code and automation` -> `Add branch ruleset`:
   1. `Ruleset Name`: `push`
   2. `Enforcement status`: `Active`
   3. `Target branches` -> `Add target` -> `Include default branch`
   4. Rules:
      - [x] `Restrict deletions`
      - [x] `Require a pull request before merging`:
         - `Required approvals`: `1`
         - `Require conversation resolution before merging`
         - `Allowed merge methods`: `Merge`.
      - [x] Block force pushes
  
  </details>

## Add a classmate as a collaborator

1. In the repo `Settings` -> `Collaborators` -> `Add people`, add your partner as a collaborator.
2. Make sure your collaborator has accepted the invitation sent to their email.

## Set up `git`

1. (If needed) On your computer, configure [`git`](https://git-scm.com/):

    ```bash
    git config --global user.name "Your Name"
    git config --global user.email "your@email"
    ```

2. <details> <summary> (Optional) Learn more about <code>Git</code> (click to expand).</summary>

   - [How Git Works: Explained in 4 Minutes](https://www.youtube.com/watch?v=e9lnsKot_SQ)
   - [Git MERGE vs REBASE: Everything You Need to Know](https://www.youtube.com/watch?v=0chZFIZLR_0)

   </details>

## Set up `VS Code`

1. Install [`VS Code`](https://code.visualstudio.com/). This is our code editor of choice that we'll use in this course.

    ![VS Code UI](./images/vs-code-ui.png)

2. <details> <summary> Skim <code>VS Code</code> docs (click to open). </summary>

    - [`Basic Layout`](https://code.visualstudio.com/docs/getstarted/userinterface#_basic-layout) - Basic UI elements in `VS Code`.
    - `Activity Bar`, `Status Bar` (see [`Basic Layout`](https://code.visualstudio.com/docs/getstarted/userinterface#_basic-layout)) - Menus of extensions;
    - `Command Palette` ([docs 1](https://code.visualstudio.com/docs/getstarted/userinterface#_command-palette), [docs 2](https://code.visualstudio.com/docs/getstarted/getting-started#_access-commands-with-the-command-palette)) - How to use editor commands;

      To run a command, open `Command Palette`, type the command, select an appropriate command, press `Enter`.
    - [`Terminal`](https://code.visualstudio.com/docs/terminal/getting-started) - How to run terminal commands inside `VS Code`;
    - [`Source Control`](https://code.visualstudio.com/docs/sourcecontrol/overview) - How to use `Git` via `VS Code` UI;
    - [`Extension Marketplace`](https://code.visualstudio.com/docs/configure/extensions/extension-marketplace) - How to install extensions;
    - [`Custom Layout`](https://code.visualstudio.com/docs/configure/custom-layout) - E.g., move the `Primary Side Bar` to the right so that it doesn't move your code whenever the `Primary Side Bar` opens;
    - [Keyboard shortcuts](https://code.visualstudio.com/docs/configure/keybindings#_keyboard-shortcuts-reference).
    - [`settings.json`](https://code.visualstudio.com/docs/configure/settings#_settings-json-file) - Keep workspace settings in a JSON file.
      - [`files.autoSave`](https://code.visualstudio.com/docs/editing/codebasics#_save-auto-save) - Enabled to save your work if VS Code closes;
      - [`editor.formatOnSave`](https://code.visualstudio.com/docs/editing/codebasics#_formatting) - Enabled to run formatters when you press `Ctrl + S` (or `Cmd + S` on `macOS`) to save code.

   </details>

## Set up the shell prompt

(Optional) Install [`Starship`](https://github.com/starship/starship#-installation).

## Open the repository on your computer

1. On your computer, create a directory `software-engineering-toolkit`.
2. In that directory, clone the lab repo.

    ```bash
    git clone https://github.com/<your-username>/lab-01-market-product-and-git
    ```

3. Open the repo in `VS Code`.

    ```bash
    cd software-engineering-toolkit
    code lab-01-market-product-and-git
    ```

## Set up `VS Code` extensions

1. Install the recommended `VS Code` extensions (listed in [`../.vscode/extensions.json`](../.vscode/extensions.json)) when `VS Code` suggests to install them.
2. Sign in to accounts.
    In the `Activity Bar`:
    1. Click `Accounts`
    2. Click `Sign in with GitHub ...`
    3. Repeat for the remaining extensions if there any.

3. <details><summary> (Optional) Check <code>GitLens</code> (click to expand).</summary>

    In the `Status Bar`:

    1. Click `Visualize commits on the Commit Graph`.
    2. Make sure you can see the commit graph.

    In the `Activity Bar`:

    1. Click `Source Control`.
    2. Click `GitLens` in the opened `Primary Side Bar` to open the `GitLens` panel.
    3. In the `GitLens` panel, click `Remotes`.
    4. Make sure `origin` points to your repo URL.
    5. In the `GitLens` panel, click `Commits`.
    6. Make sure you can see commits on the current branch.

    Learn more about [`GitLens` features](https://help.gitkraken.com/gitlens/gitlens-features/).
  
   </details>

## Set up a coding agent

(Optional) Set up a free coding agent to help you with the lab. See [Coding agents](./appendix/coding-agents.md).
