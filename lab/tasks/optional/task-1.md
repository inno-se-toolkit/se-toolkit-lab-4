# CI/CD

<h4>Time</h4>

~60 min

<h4>Purpose</h4>

Build a `CI` pipeline that runs tests and publishes container images, and update the deployment to use published images.

<h4>Context</h4>

Running tests manually works for a single developer.
With `CI`, tests run automatically on every push to `GitHub`, and a passing pipeline publishes a ready-to-deploy image.
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

1. Create the file `.github/workflows/ci.yml`.
2. Add a workflow that does the following on every push to `main`:
   1. Checks out the repository.
   2. Runs all back-end unit tests using `uv run poe test`.
   3. Runs all end-to-end tests against the deployed API.
3. [Commit](../../../wiki/git-workflow.md#commit) the workflow file.
4. Push the branch to `GitHub` and verify the workflow runs and passes in the `Actions` tab of your fork.

### 1.4. Publish images to `DockerHub`

> [!NOTE]
> Publishing images to [`DockerHub`](../../../wiki/docker.md#dockerhub) lets your VM pull a pre-built image instead of building from source on each deploy.

1. Create a `DockerHub` account if you don't have one.
2. Add your `DockerHub` credentials as [`GitHub` secrets](../../../wiki/github.md#secrets):
   - `DOCKERHUB_USERNAME`
   - `DOCKERHUB_TOKEN`
3. Update `.github/workflows/ci.yml` to add a publish step after tests pass:
   1. Log in to `DockerHub` using the secrets.
   2. Build the Docker image.
   3. Push the image to `DockerHub` as `<your-dockerhub-username>/se-toolkit-lab:<git-sha>`.
4. [Commit](../../../wiki/git-workflow.md#commit) the workflow update.
5. Push and verify the image appears on `DockerHub` after the workflow passes.

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
     image: <your-dockerhub-username>/se-toolkit-lab:<git-sha>
   ```

4. On the VM, pull and restart the services:

   ```terminal
   docker compose --env-file .env.docker.secret pull
   docker compose --env-file .env.docker.secret up -d
   ```

5. Verify the back-end is running using the same checks as in Task 1.

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
