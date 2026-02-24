# Add Front-end

<h4>Time</h4>

~50 min

<h4>Purpose</h4>

Understand the difference between a dev server and production static files, and use an AI agent to modify front-end code.

<h4>Context</h4>

The back-end API is running on the VM. You will add a front-end that connects to it.
First you will run it locally with a dev server (fast iteration, hot reload).
Then you will build and deploy a production version (static files served by `Caddy`).
Finally, you will use an AI agent to add a new feature to the front-end.

<h4>Table of contents</h4>

- [1. Steps](#1-steps)
  - [1.1. Follow the `Git workflow`](#11-follow-the-git-workflow)
  - [1.2. Create a `Lab Task` issue](#12-create-a-lab-task-issue)
  - [1.3. Part A: Dev version](#13-part-a-dev-version)
    - [1.3.1. Run the dev server](#131-run-the-dev-server)
    - [1.3.2. Edit a source file and observe hot reload](#132-edit-a-source-file-and-observe-hot-reload)
  - [1.4. Part B: Prod version](#14-part-b-prod-version)
    - [1.4.1. Build the production bundle](#141-build-the-production-bundle)
    - [1.4.2. Copy the `dist/` folder to the VM](#142-copy-the-dist-folder-to-the-vm)
    - [1.4.3. Configure `Caddy`](#143-configure-caddy)
    - [1.4.4. Verify in the browser](#144-verify-in-the-browser)
  - [1.5. Part C: Modify the front-end with an AI agent](#15-part-c-modify-the-front-end-with-an-ai-agent)
    - [1.5.1. Add a column using the AI agent](#151-add-a-column-using-the-ai-agent)
    - [1.5.2. Verify in the dev server](#152-verify-in-the-dev-server)
    - [1.5.3. Deploy the change to the VM](#153-deploy-the-change-to-the-vm)
  - [1.6. Finish the task](#16-finish-the-task)
- [2. Acceptance criteria](#2-acceptance-criteria)

## 1. Steps

### 1.1. Follow the `Git workflow`

Follow the [`Git workflow`](../../../wiki/git-workflow.md) to complete this task.

### 1.2. Create a `Lab Task` issue

Title: `[Task] Add Front-end`

### 1.3. Part A: Dev version

> [!NOTE]
> A dev server serves the front-end with hot reload: the browser updates automatically when you save a file.
> This is for local development only — it is not meant to be deployed to production.

#### 1.3.1. Run the dev server

1. [Open a new `VS Code Terminal`](../../../wiki/vs-code.md#open-a-new-vs-code-terminal).
2. Navigate to the front-end project directory.

   ```terminal
   cd frontend
   ```

3. Configure the environment. Complete the following steps:

   1. [Open the file](../../../wiki/vs-code.md#open-the-file) [`frontend/.env.example`](../../../frontend/.env.example).
   2. Copy it to `frontend/.env`.
   3. Fill in `VITE_API_URL` with your API URL, for example `http://<your-vm-ip-address>:<api-port>`.
   4. Fill in `VITE_API_TOKEN` with your [`<api-token>`](../../../wiki/web-development.md#api-token).

4. [Run using the `VS Code Terminal`](../../../wiki/vs-code.md#run-a-command-using-the-vs-code-terminal):

   ```terminal
   npm install
   ```

5. [Run using the `VS Code Terminal`](../../../wiki/vs-code.md#run-a-command-using-the-vs-code-terminal):

   ```terminal
   npm run dev
   ```

6. Open the URL shown in the terminal output in a browser.

   The output should be similar to this:

   ```terminal
   Local: http://localhost:5173/
   ```

7. Verify that the front-end loads and displays data from the API.

#### 1.3.2. Edit a source file and observe hot reload

1. [Open the file](../../../wiki/vs-code.md#open-the-file) [`frontend/src/App.jsx`](../../../frontend/src/App.jsx).
2. Make a small visible change, for example change a heading text.
3. Save the file.
4. Observe that the browser updates automatically without a page refresh.

### 1.4. Part B: Prod version

> [!NOTE]
> A production build compiles the front-end into a `dist/` folder of static [HTML](../../../wiki/web-development.md#html), [CSS](../../../wiki/web-development.md#css), and [JavaScript](../../../wiki/web-development.md#javascript) files.
> These files are copied to the VM and served by `Caddy` — the same model as uploading to a [CDN](../../../wiki/web-development.md#cdn).

#### 1.4.1. Build the production bundle

1. [Run using the `VS Code Terminal`](../../../wiki/vs-code.md#run-a-command-using-the-vs-code-terminal):

   ```terminal
   npm run build
   ```

2. Verify that a `dist/` folder was created.

#### 1.4.2. Copy the `dist/` folder to the VM

1. Copy the `dist/` folder to the VM.

   Method 1: use [`scp`](../../../wiki/ssh.md#scp):

   ```terminal
   scp -r dist/ <vm-user>@<vm-host>:/var/www/frontend/
   ```

   Method 2: use `rsync`:

   ```terminal
   rsync -av dist/ <vm-user>@<vm-host>:/var/www/frontend/
   ```

#### 1.4.3. Configure `Caddy`

1. [Connect to your VM](../../../wiki/vm.md#connect-to-the-vm).
2. Edit the [`Caddyfile`](../../../wiki/caddy.md) on the VM to serve the static files.

   Add the following block to the `Caddyfile`:

   ```caddyfile
   :<frontend-port> {
       root * /var/www/frontend/dist
       file_server
   }
   ```

3. Reload `Caddy`:

   ```terminal
   sudo systemctl reload caddy
   ```

#### 1.4.4. Verify in the browser

1. Open the front-end URL in a browser: `<frontend-url>`
2. Verify that the front-end loads and displays data from the API.

### 1.5. Part C: Modify the front-end with an AI agent

> [!NOTE]
> The AI agent can read all front-end source files and find the right component to modify.
> Your job is to give a clear prompt and verify the result.

#### 1.5.1. Add a column using the AI agent

1. Open the AI agent in the front-end project directory.
2. Give it this prompt:

   > "Add a `description` column to the data table. The API already returns this field. Add it to the table header and display the value in each row."

3. Wait for the agent to make the changes.

#### 1.5.2. Verify in the dev server

1. Check that the dev server is still running (or restart it with `npm run dev`).
2. Open the front-end in the browser.
3. Verify that the new column appears in the table.

> [!NOTE]
> The dev server picks up the changes automatically — no rebuild is needed.

#### 1.5.3. Deploy the change to the VM

1. [Run using the `VS Code Terminal`](../../../wiki/vs-code.md#run-a-command-using-the-vs-code-terminal):

   ```terminal
   npm run build
   ```

2. Copy the updated `dist/` folder to the VM using the [same method as in Part B](#142-copy-the-dist-folder-to-the-vm).
3. Open the front-end URL in the browser and verify the new column appears in the production build.

### 1.6. Finish the task

1. [Commit](../../../wiki/git-workflow.md#commit) your changes.

   Use the following commit message:

   ```text
   feat: add description column to the front-end table
   ```

2. [Create a PR](../../../wiki/git-workflow.md#create-a-pr-to-the-main-branch-in-your-fork) with your changes.
3. [Get a PR review](../../../wiki/git-workflow.md#get-a-pr-review) and complete the subsequent steps in the `Git workflow`.

---

## 2. Acceptance criteria

- [ ] Issue has the correct title.
- [ ] The front-end runs locally with `npm run dev`.
- [ ] The production build is deployed on the VM and served by `Caddy`.
- [ ] The `description` column appears in the data table in both the dev and production builds.
- [ ] PR is approved.
- [ ] PR is merged.
