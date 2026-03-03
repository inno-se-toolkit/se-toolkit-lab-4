# CI/CD

<h4>Time</h4>

~60 min

<h4>Purpose</h4>

Build a CI pipeline that runs tests and publishes container images, and update the deployment to use published images.

<h4>Context</h4>

Running tests manually works for a single developer.
With CI, tests run automatically on every push to `GitHub`, and a passing pipeline publishes a ready-to-deploy image.
Your VM then pulls the published image instead of building from source.

<h4>Table of contents</h4>

- [1. Steps](#1-steps)
  - [1.1. Follow the `Git workflow`](#11-follow-the-git-workflow)
  - [1.2. Create a `Lab Task` issue](#12-create-a-lab-task-issue)
  - [1.3. Create a `GitHub Actions` workflow](#13-create-a-github-actions-workflow)
  - [1.4. Publish images to `DockerHub`](#14-publish-images-to-dockerhub)
  - [1.5. Deploy using published images](#15-deploy-using-published-images)
  - [1.6. Finish the task](#16-finish-the-task)
- [2. Acceptance criteria](#2-acceptance-criteria)

## 1. Steps

### 1.1. Follow the `Git workflow`

Follow the [`Git workflow`](../../../wiki/git-workflow.md) to complete this task.

### 1.2. Create a `Lab Task` issue

Title: `[Task] CI/CD`

### 1.3. Create a `GitHub Actions` workflow

> [!NOTE]
> [`GitHub Actions`](../../../wiki/github.md#github-actions) runs your workflow automatically on every push to `GitHub`.

<!-- TODO integration job, staging job -->

1. Create the file `.github/workflows/ci.yml`.
2. Make the workflow run on every push to `main`.
3. Create the `test` job that does the following:
   1. Check out the repository.
   2. Run all back-end unit tests using `uv run poe test`.
   3. Start containers using `Docker Compose`.
   4. Run all end-to-end tests.
4. [Commit](../../../wiki/git-workflow.md#commit) the workflow file.
5. Push the branch to `GitHub`.

   Verify the workflow runs and passes in the `Actions` tab of your fork.

### 1.4. Publish images to `DockerHub`

> [!NOTE]
> Publishing images to [`DockerHub`](../../../wiki/docker.md#dockerhub) lets your VM pull a pre-built image instead of building from source on each deploy.

1. Create a `DockerHub` account if you don't have one.
2. Add your `DockerHub` credentials as [`GitHub` secrets](../../../wiki/github.md#secrets):
   - `DOCKERHUB_USERNAME`
   - `DOCKERHUB_TOKEN`
3. In `.github/workflows/ci.yml`, add the `publish` job that runs after the `test` job passes.
4. The `publish` job must do the following:
   1. Log in to `DockerHub` using the secrets.
   2. Build the [`Docker` image](../../../wiki/docker.md#image) of your backend.
   3. Push the image to `DockerHub` as `<your-dockerhub-username>/se-toolkit-lab-4-backend:<git-commit-hash>`. Replace:

   - [`<your-dockerhub-username>`](../../../wiki/docker.md#your-dockerhub-username)
   - `<git-commit-hash>` with the [hash of the commit](../../../wiki/git.md#commit-hash) that triggered the workflow.
5. [Commit](../../../wiki/git-workflow.md#commit) the workflow update.
6. Push the branch to `GitHub`.

   Verify the image appears on `DockerHub` after the workflow passes.

### 1.5. Deploy using published images

1. [Connect to your VM](../../../wiki/vm.md#connect-to-the-vm).
2. [Open the file](../../../wiki/vs-code.md#open-the-file):
   [`docker-compose.yml`](../../../docker-compose.yml).
3. Replace each `build: .` entry with the published image reference:

   **Before:**

   ```yaml
   app:
     build: .
   ```

   **After:**

   ```yaml
   app:
     image: <your-dockerhub-username>/se-toolkit-lab-4-backend:<git-sha>
   ```

   Replace :
   - [`<your-dockerhub-username>`](../../../wiki/docker.md#your-dockerhub-username)
   - `<git-commit-hash>`

4. To pull the containers,

   [run in the `VS Code Terminal`](../../../wiki/vs-code.md#run-a-command-in-the-vs-code-terminal):

   ```terminal
   docker compose --env-file .env.docker.secret pull
   ```

   The output should be similar to this:

   ```terminal
   [+] Pulling 1/1
    ✔ app Pulled
   ```

5. To start the services,

   [run in the `VS Code Terminal`](../../../wiki/vs-code.md#run-a-command-in-the-vs-code-terminal):

   ```terminal
   docker compose --env-file .env.docker.secret up --build -d
   ```

   The output should be similar to this:

   ```terminal
   [+] Running 1/1
    ✔ Container se-toolkit-lab-app-1  Started
   ```

   [Verify the back-end is running](../required/task-1.md#12-deploy-the-back-end-to-the-vm) using the same checks as in Task 1.

   <!-- TODO move generic troubleshooting to wiki -->

   <details><summary>Troubleshooting</summary>

   <h4>Port conflict (<code>port is already allocated</code>)</h4>

   Stop the process that uses the port, then retry.

   <h4>Containers exit immediately</h4>

   To rebuild all containers from scratch,

   [run in the `VS Code Terminal`](../../../wiki/vs-code.md#run-a-command-in-the-vs-code-terminal):

   ```terminal
   docker compose --env-file .env.docker.secret down -v
   docker compose --env-file .env.docker.secret up --build -d
   ```

   <h4>Missing <code>.env.docker.secret</code></h4>

   Ensure the `.env.docker.secret` file exists in the project root. Copy it from `.env.docker.example` if needed.

   </details>

### 1.6. Finish the task

1. [Create a PR](../../../wiki/git-workflow.md#create-a-pr-to-the-main-branch-in-your-fork) with your changes.
2. [Get a PR review](../../../wiki/git-workflow.md#get-a-pr-review) and complete the subsequent steps in the `Git workflow`.

---

## 2. Acceptance criteria

- [ ] Issue has the correct title.
- [ ] The `GitHub Actions` workflow runs all tests on every push.
- [ ] Images are published to `DockerHub` after a successful run.
- [ ] The VM deploys using published images instead of local builds.
- [ ] PR is approved.
- [ ] PR is merged.
