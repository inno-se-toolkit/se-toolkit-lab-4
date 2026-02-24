# Back-end Testing

<h4>Time</h4>

~75 min

<h4>Purpose</h4>

Write unit and end-to-end tests, diagnose bugs from failing test output, and use an AI agent to generate additional test cases.

<h4>Context</h4>

The back-end contains intentional bugs at specific boundary values.
You will discover and fix them by writing tests, then use an AI agent to generate additional coverage.

<h4>Table of contents</h4>

- [1. Steps](#1-steps)
  - [1.1. Follow the `Git workflow`](#11-follow-the-git-workflow)
  - [1.2. Create a `Lab Task` issue](#12-create-a-lab-task-issue)
  - [1.3. Part A: Run unit tests locally](#13-part-a-run-unit-tests-locally)
    - [1.3.1. Run existing unit tests](#131-run-existing-unit-tests)
    - [1.3.2. Add a new unit test](#132-add-a-new-unit-test)
    - [1.3.3. Fix the bug](#133-fix-the-bug)
    - [1.3.4. Rerun unit tests](#134-rerun-unit-tests)
    - [1.3.5. Commit the fix](#135-commit-the-fix)
  - [1.4. Part B: Run end-to-end tests remotely](#14-part-b-run-end-to-end-tests-remotely)
    - [1.4.1. Redeploy the fixed version](#141-redeploy-the-fixed-version)
    - [1.4.2. Run existing end-to-end tests](#142-run-existing-end-to-end-tests)
    - [1.4.3. Add two end-to-end tests](#143-add-two-end-to-end-tests)
    - [1.4.4. Fix the bug](#144-fix-the-bug)
    - [1.4.5. Redeploy and rerun](#145-redeploy-and-rerun)
    - [1.4.6. Commit the fix](#146-commit-the-fix)
  - [1.5. Part C: Generate tests with an AI agent](#15-part-c-generate-tests-with-an-ai-agent)
    - [1.5.1. Generate tests](#151-generate-tests)
    - [1.5.2. Review and curate the tests](#152-review-and-curate-the-tests)
    - [1.5.3. Run the full test suite](#153-run-the-full-test-suite)
    - [1.5.4. Commit the curated tests](#154-commit-the-curated-tests)
  - [1.6. Finish the task](#16-finish-the-task)
- [2. Acceptance criteria](#2-acceptance-criteria)

## 1. Steps

### 1.1. Follow the `Git workflow`

Follow the [`Git workflow`](../../../wiki/git-workflow.md) to complete this task.

### 1.2. Create a `Lab Task` issue

Title: `[Task] Back-end Testing`

### 1.3. Part A: Run unit tests locally

> [!NOTE]
> Unit tests do not require a running server. They test individual functions in isolation.

#### 1.3.1. Run existing unit tests

1. [Run using the `VS Code Terminal`](../../../wiki/vs-code.md#run-a-command-using-the-vs-code-terminal):

   ```terminal
   uv run poe test
   ```

2. All existing tests should pass.

   The output should be similar to this:

   ```terminal
   ===================== 3 passed in X.XXs =====================
   ```

#### 1.3.2. Add a new unit test

1. [Open the file](../../../wiki/vs-code.md#open-the-file):
   [`tests/unit/test_interactions.py`](../../../tests/unit/test_interactions.py).
2. Add a new unit test that targets the following boundary-value case:

   An interaction where `item_id` and `learner_id` are different values — for example, `item_id=1` and `learner_id=2`. When filtering by `item_id=1`, this interaction should appear in the results.

   Name the test `test_filter_excludes_interaction_with_different_learner_id`.

3. [Run using the `VS Code Terminal`](../../../wiki/vs-code.md#run-a-command-using-the-vs-code-terminal):

   ```terminal
   uv run poe test
   ```

4. Observe that the new test fails.

   The output should be similar to this:

   ```terminal
   FAILED tests/unit/test_interactions.py::test_filter_excludes_interaction_with_different_learner_id - AssertionError: assert 0 == 1
   ```

   This line means the following:
   - The test failed (`FAILED`).
   - The test is in the file `tests/unit/test_interactions.py`.
   - The name of the failing test is `test_filter_excludes_interaction_with_different_learner_id`.
   - The failed assertion is `assert 0 == 1` — the filter returned 0 interactions, but 1 was expected.

#### 1.3.3. Fix the bug

1. [Open the file](../../../wiki/vs-code.md#open-the-file):
   [`src/app/routers/interactions.py`](../../../src/app/routers/interactions.py).
2. Fix the bug in the `_filter_by_item_id` function.

<details><summary>Click to open a hint</summary>

The filter is applied in-memory after all interactions are fetched from the database.
Look at the condition that decides which interactions to include — it compares the wrong field on the interaction object.

</details>

<details><summary>Click to open the solution</summary>

Find this line in `_filter_by_item_id`:

```python
return [i for i in interactions if i.learner_id == item_id]  # BUG
```

Change it to:

```python
return [i for i in interactions if i.item_id == item_id]
```

</details>

#### 1.3.4. Rerun unit tests

1. [Run using the `VS Code Terminal`](../../../wiki/vs-code.md#run-a-command-using-the-vs-code-terminal):

   ```terminal
   uv run poe test
   ```

2. All tests should pass.

#### 1.3.5. Commit the fix

1. [Commit](../../../wiki/git-workflow.md#commit) your changes.

   Use the following commit message:

   ```text
   fix: filter interactions by item_id instead of learner_id
   ```

### 1.4. Part B: Run end-to-end tests remotely

> [!NOTE]
> End-to-end tests run on your local machine and send real [HTTP](../../../wiki/http.md) requests to the deployed version on the VM.

#### 1.4.1. Redeploy the fixed version

1. Deploy the fixed version to your VM. Follow the same deployment process as in Task 1 (see the [VM](../../../wiki/vm.md) wiki page for a reminder).

#### 1.4.2. Run existing end-to-end tests

1. Set the required environment variables in the terminal. Complete the following steps:

   1. Set the base URL of your deployed API:

      ```terminal
      export API_BASE_URL=https://<your-vm-hostname>
      ```

   2. Set the API token (use the same value as in your `.env.secret`):

      ```terminal
      export API_TOKEN=<your-api-token>
      ```

2. [Run using the `VS Code Terminal`](../../../wiki/vs-code.md#run-a-command-using-the-vs-code-terminal):

   ```terminal
   uv run poe test-e2e
   ```

3. All existing end-to-end tests should pass.

   The output should be similar to this:

   ```terminal
   ===================== 2 passed in X.XXs =====================
   ```

#### 1.4.3. Add two end-to-end tests

1. [Open the file](../../../wiki/vs-code.md#open-the-file):
   [`tests/e2e/test_interactions.py`](../../../tests/e2e/test_interactions.py).
2. Add two end-to-end tests that cover the following boundary-value cases:

   - Test 1: `GET /interactions/` returns [HTTP status code](../../../wiki/http.md#status-code) `200`.
   - Test 2: `GET /interactions/` response body is a [JSON](../../../wiki/file-formats.md#json) array.

   <details><summary>Click to open a hint</summary>

   The response model for `GET /interactions/` defines the fields the API must return.
   Compare the field names in the response model to the column names in the database.
   A mismatch there causes the server to fail when building the response.

   </details>

   <details><summary>Click to open the solution</summary>

   ```python
   import httpx


   def test_get_interactions_returns_200(client: httpx.Client) -> None:
       response = client.get("/interactions/")
       assert response.status_code == 200


   def test_get_interactions_response_is_a_list(client: httpx.Client) -> None:
       response = client.get("/interactions/")
       assert isinstance(response.json(), list)
   ```

   </details>

3. [Run using the `VS Code Terminal`](../../../wiki/vs-code.md#run-a-command-using-the-vs-code-terminal):

   ```terminal
   uv run poe test-e2e
   ```

4. Observe that both new tests fail.

   The output should be similar to this:

   ```terminal
   FAILED tests/e2e/test_interactions.py::test_get_interactions_returns_200 - AssertionError: assert 500 == 200
   FAILED tests/e2e/test_interactions.py::test_get_interactions_response_is_a_list - ...
   ```

   The `500` status code means the server encountered an internal error while building the response.

#### 1.4.4. Fix the bug

1. [Open the file](../../../wiki/vs-code.md#open-the-file):
   [`src/app/models/interaction.py`](../../../src/app/models/interaction.py).
2. Fix the bug in `InteractionModel`.

   <details><summary>Click to open a hint</summary>

   The response model has a field whose name does not match the corresponding column in the database.
   When `FastAPI` tries to serialize the database row into the response model, it cannot find the expected field and returns a `500` error.

   </details>

   <details><summary>Click to open the solution</summary>

   Find this line in `InteractionModel`:

   ```python
   timestamp: datetime  # BUG: should be 'created_at' to match the database column
   ```

   Change it to:

   ```python
   created_at: datetime
   ```

   </details>

#### 1.4.5. Redeploy and rerun

1. Deploy the fixed version to the VM.
2. [Run using the `VS Code Terminal`](../../../wiki/vs-code.md#run-a-command-using-the-vs-code-terminal):

   ```terminal
   uv run poe test-e2e
   ```

3. All end-to-end tests should pass.

#### 1.4.6. Commit the fix

1. [Commit](../../../wiki/git-workflow.md#commit) your changes.

   Use the following commit message:

   ```text
   fix: rename timestamp to created_at in InteractionModel
   ```

> [!IMPORTANT]
> Each fix must be a **separate commit**. Do not combine the Part A and Part B fixes into one commit.

### 1.5. Part C: Generate tests with an AI agent

#### 1.5.1. Generate tests

1. Open the AI agent in the back-end project directory.
2. Give it this prompt:

   > "Read the back-end source code and the existing unit tests. Generate five new unit tests that cover edge cases and boundary values not already tested."

3. Wait for the agent to generate the tests.

#### 1.5.2. Review and curate the tests

1. Review each generated test against the following criteria:

   - **Keep** — the test is correct, targets a real case, and adds coverage not already present.
   - **Fix** — the test has a minor error (wrong assertion, wrong expected value) but the idea is sound — correct it.
   - **Discard** — the test duplicates an existing test, is logically wrong, or tests behaviour outside the scope of the module.

2. Keep at least two tests and discard at least one.

#### 1.5.3. Run the full test suite

1. [Run using the `VS Code Terminal`](../../../wiki/vs-code.md#run-a-command-using-the-vs-code-terminal):

   ```terminal
   uv run poe test
   ```

2. All tests (including the curated AI-generated ones) should pass.

#### 1.5.4. Commit the curated tests

1. [Commit](../../../wiki/git-workflow.md#commit) your changes.

   Use the following commit message:

   ```text
   test: add curated AI-generated unit tests
   ```

### 1.6. Finish the task

1. [Create a PR](../../../wiki/git-workflow.md#create-a-pr-to-the-main-branch-in-your-fork) with your changes.
2. [Get a PR review](../../../wiki/git-workflow.md#get-a-pr-review) and complete the subsequent steps in the `Git workflow`.

---

## 2. Acceptance criteria

- [ ] Issue has the correct title.
- [ ] All unit tests pass.
- [ ] All end-to-end tests pass.
- [ ] AI-generated tests include at least two kept tests and at least one discarded test.
- [ ] The Part A fix and Part B fix are separate commits.
- [ ] PR is approved.
- [ ] PR is merged.
