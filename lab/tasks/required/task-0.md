# Practice the `Git workflow`

**Time:** ~15 min

**Purpose:** Practice the [`Git workflow`](../git-workflow.md) before working on the main tasks.

**Context:** This task is an opportunity to practice the full cycle (Issue → Branch → Commits → PR → Review → Merge).

## Steps

### 1. Create an issue

Title: `[Task] Add my name to contributors`

### 2. Create a branch

On the issue page, click `Create a branch` in the right sidebar.

Alternatively, use the terminal:

```bash
git checkout -b add-contributor
```

### 3. Add your name

> [!NOTE]
> Replace `<your-username>` with your `GitHub` username without `@`.

1. Open [`CONTRIBUTORS.md`](../../../CONTRIBUTORS.md).
2. Add your GitHub username below the comment:

    ```markdown
    <!--
    ...
    -->
    - @<your-username>
    ```

3. Save the file.

### 4. Commit and push

```bash
git add CONTRIBUTORS.md
git commit -m 'docs: add <your-username> to contributors'
git push -u origin add-contributor
```

### 5. Create a Pull Request (PR)

Go to your fork on `GitHub`.

Open PR editor using one of the following methods.

#### Open PR editor using a prompt

If you see the `Compare & pull request` button, click it.

#### Open PR editor using `Pull requests`

1. Click `Pull requests`.
2. Click `New pull request`.
3. Click `base repository: <your-username>/lab-01-market-product-and-git`.
4. Click `<your-username>/lab-01-market-product-and-git`.
5. Click `compare: main`.
6. Click `add-contributor`.
7. Click `Create pull request`.

#### Open PR editor using the branch list

1. Click `main`.
2. Click `add-contributor` in the list.
3. Click `Contribute`.
4. Click `Open pull request`.

#### Finish creating a PR

1. Write the PR title (`Add @<your-username> to contributors`).
2. Write the PR description.
3. Click `Create pull request`.

### 6. Get review and merge

1. Request a review from your partner.
2. Once your partner has approved the PR, click `Merge pull request`.
3. Delete the branch when prompted.

## Acceptance criteria

- [ ] Issue created
- [ ] Username added to `CONTRIBUTORS.md`
- [ ] Commit message follows `type: description` format
- [ ] PR created and linked to issue
- [ ] Partner reviewed and approved
- [ ] PR merged
