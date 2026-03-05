# `Node.js`

<h2>Table of contents</h2>

- [What is `Node.js`](#what-is-nodejs)
- [`nvm`](#nvm)
  - [Install `nvm`](#install-nvm)
  - [Install `Node.js`](#install-nodejs)
- [`npm`](#npm)
- [Set up `Node.js` in `VS Code`](#set-up-nodejs-in-vs-code)
  - [Install `Node.js` and dependencies](#install-nodejs-and-dependencies)
  - [Check that `Node.js` works](#check-that-nodejs-works)

## What is `Node.js`

`Node.js` is a runtime environment that executes `JavaScript` outside of a browser. In this project, it is used to run the frontend development server and build tools.

Docs:

- [Node.js documentation](https://nodejs.org/en/docs)

## `nvm`

`nvm` (Node Version Manager) is a tool for installing and switching between multiple versions of [`Node.js`](#what-is-nodejs).

Docs:

- [`nvm` repository](https://github.com/nvm-sh/nvm)

### Install `nvm`

1. [Check the current shell in the `VS Code Terminal`](./vs-code.md#check-the-current-shell-in-the-vs-code-terminal).
2. Follow the [installation instructions](https://github.com/nvm-sh/nvm#installing-and-updating) for `macOS` and `Linux`, even if you use `Windows`.
3. To check that `nvm` is installed,

   [run in the `VS Code Terminal`](./vs-code.md#run-a-command-in-the-vs-code-terminal):

   ```terminal
   nvm --version
   ```

4. The output should be similar to this:

   ```terminal
   0.40.3
   ```

### Install `Node.js`

1. To install [`Node.js`](#what-is-nodejs),

   [run in the `VS Code Terminal`](./vs-code.md#run-a-command-in-the-vs-code-terminal):

   ```terminal
   nvm install 25.7.0
   ```

2. The output should be similar to this:

   ```terminal
   Downloading and installing node v25.7.0...
   Now using node v25.7.0 (npm v11.10.1)
   ```

3. To set this version as the default,

   [run in the `VS Code Terminal`](./vs-code.md#run-a-command-in-the-vs-code-terminal):

   ```terminal
   nvm alias default node
   ```

## `npm`

`npm` is the default package manager for [`Node.js`](#what-is-nodejs). It installs and manages project dependencies declared in `package.json`.

Docs:

- [`npm` documentation](https://docs.npmjs.com/)

## Set up `Node.js` in `VS Code`

Complete these steps:

1. [Install `Node.js` and dependencies](#install-nodejs-and-dependencies).
2. [Check that `Node.js` works](#check-that-nodejs-works).

### Install `Node.js` and dependencies

1. [Open in `VS Code` the project directory](./vs-code.md#open-the-directory).

2. To install project dependencies,

   [run in the `VS Code Terminal`](./vs-code.md#run-a-command-in-the-vs-code-terminal):

   ```terminal
   npm install --prefix frontend
   ```

   This command reads `frontend/package.json` and installs all required packages into `frontend/node_modules/`.

3. The output should be similar to this:

   ```terminal
   added 143 packages, and audited 144 packages in 3s
   ```

> [!NOTE]
> The `frontend/node_modules/` directory contains installed packages.
>
> This directory is managed by [`npm`](#npm). You don't need to edit files in this directory manually.

### Check that `Node.js` works

1. To check the `Node.js` version,

   [run in the `VS Code Terminal`](./vs-code.md#run-a-command-in-the-vs-code-terminal):

   ```terminal
   node --version
   ```

2. The output should be similar to this:

   ```terminal
   v25.7.0
   ```
