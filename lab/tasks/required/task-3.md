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
    - [1.4.1. Deploy the front-end to the VM](#141-deploy-the-front-end-to-the-vm)
    - [1.4.2. Verify in the browser](#142-verify-in-the-browser)
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
   3. Set `VITE_API_TARGET` to the URL of your back-end API, for example `http://<your-vm-ip-address>:<api-port>`.

> [!NOTE]
> The dev server proxies API requests (e.g., `/items`) to the `VITE_API_TARGET` URL.
> The API token is entered at runtime through the front-end UI — it is not stored in the `.env` file.

1. [Run in the `VS Code Terminal`](../../../wiki/vs-code.md#run-a-command-in-the-vs-code-terminal):

   ```terminal
   npm install
   ```

2. [Run in the `VS Code Terminal`](../../../wiki/vs-code.md#run-a-command-in-the-vs-code-terminal):

   ```terminal
   npm run dev
   ```

3. Open the URL shown in the terminal output in a browser.

   The output should be similar to this:

   ```terminal
   Local: http://localhost:5173/
   ```

4. Verify that the front-end loads and displays data from the API.

#### 1.3.2. Edit a source file and observe hot reload

1. [Open the file](../../../wiki/vs-code.md#open-the-file) [`frontend/src/App.tsx`](../../../frontend/src/App.tsx).
2. Make a small visible change, for example change a heading text.
3. Save the file.
4. Observe that the browser updates automatically without a page refresh.

### 1.4. Part B: Prod version

> [!NOTE]
> A production build compiles the front-end into static [HTML](../../../wiki/web-development.md#html), [CSS](../../../wiki/web-development.md#css), and [JavaScript](../../../wiki/web-development.md#javascript) files.
> In this project, the [`Caddy`](../../../wiki/caddy.md) [Docker](../../../wiki/docker.md#docker) container builds the front-end and serves the static files.
> The [`Caddyfile`](../../../wiki/caddy.md#caddyfile) routes API requests to the back-end and serves the front-end for all other paths.

#### 1.4.1. Deploy the front-end to the VM

1. [Connect to your VM](../../../wiki/vm.md#connect-to-the-vm).
2. Navigate to the project directory and pull the latest changes:

   ```terminal
   cd se-toolkit-lab-4 && git pull
   ```

3. Rebuild and restart the `caddy` service:

   ```terminal
   docker compose --env-file .env.docker.secret up --build caddy -d
   ```

> [!NOTE]
> The `caddy` service uses a multi-stage [`Dockerfile`](../../../wiki/docker.md#dockerfile) (`frontend/Dockerfile`).
> Stage 1 builds the front-end (`npm run build`), and stage 2 copies the output into the `Caddy` image.
> Rebuilding the container is how you deploy front-end changes — there is no need to copy files manually.

#### 1.4.2. Verify in the browser

1. Open in a browser: `http://<your-vm-ip-address>:<app-port>/`.

   Replace:

   - [`<your-vm-ip-address>`](../../../wiki/vm.md#your-vm-ip-address)
   - [`<app-port>`](../../../wiki/placeholders.md#app-port).

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

1. [Commit](../../../wiki/git-workflow.md#commit) your changes.

   Use the following commit message:

   ```text
   feat: add description column to the front-end table
   ```

2. Push your changes.
3. [Connect to your VM](../../../wiki/vm.md#connect-to-the-vm).
4. Navigate to the project directory and checkout your task branch:

   ```terminal
   cd se-toolkit-lab-4 && git fetch origin && git checkout <task-branch-name>
   ```

   Replace [`<task-branch-name>`](../../../wiki/git-workflow.md#task-branch-name) with the name of your branch.

5. Rebuild and restart the `caddy` service:

   ```terminal
   docker compose --env-file .env.docker.secret up --build caddy -d
   ```

6. Open the [`<app-url>`](../../../wiki/placeholders.md#app-url) in the browser and verify the new column appears in the production build.

### 1.6. Finish the task

1. [Create a PR](../../../wiki/git-workflow.md#create-a-pr-to-the-main-branch-in-your-fork) with your changes.
2. [Get a PR review](../../../wiki/git-workflow.md#get-a-pr-review) and complete the subsequent steps in the `Git workflow`.

---

## 2. Acceptance criteria

- [ ] Issue has the correct title.
- [ ] The front-end runs locally with `npm run dev`.
- [ ] The production build is deployed on the VM and served by `Caddy`.
- [ ] The `description` column appears in the data table in both the dev and production builds.
- [ ] PR is approved.
- [ ] PR is merged.
