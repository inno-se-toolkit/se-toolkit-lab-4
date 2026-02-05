# Resolve a merge conflict

**Time:** ~15-20 min

**Purpose:** Learn how to resolve merge conflicts — a common situation when working with Git.

**Context:** When multiple changes affect the same lines of code, Git cannot automatically merge them. You need to manually decide which changes to keep. This exercise creates that situation so you can practice resolving it.

## Steps

### 1. Create an issue

Title: `[Task] Resolve a merge conflict`

### 2. Create a practice branch

```console
git switch main
git switch -c conflict-practice
```

### 3. Make a change on the practice branch

Edit `CONTRIBUTORS.md` — change the comment text to something else (e.g., "Add your name here").

Commit:

```console
git add CONTRIBUTORS.md
git commit -m "docs: update contributors instructions"
```

### 4. Make a conflicting change on main

Switch to main and edit the **same line** differently:

```console
git switch main
```

Edit `CONTRIBUTORS.md` — change the same comment to something different (e.g., "Write your name below").

Commit:

```console
git add CONTRIBUTORS.md
git commit -m "docs: update contributors comment"
```

### 5. Merge and resolve the conflict

```console
git merge conflict-practice
```

Git will report a conflict. Open `CONTRIBUTORS.md` — you'll see conflict markers:

```
<<<<<<< HEAD
<!-- Write your name below -->
=======
<!-- Add your name here -->
>>>>>>> conflict-practice
```

Edit the file to keep one version (or combine them). Remove the conflict markers.

Then complete the merge:

```console
git add CONTRIBUTORS.md
git commit -m "docs: resolve merge conflict in contributors"
```

### 6. Document what you learned

Create a PR from `main` to `main` of your fork (or simply add a comment to your issue) explaining:

- What caused the conflict (1 sentence)
- How you resolved it (1 sentence)

### 7. Clean up

Delete the practice branch:

```console
git branch -d conflict-practice
```

Close the issue.

## Acceptance criteria

- [ ] Issue created
- [ ] Successfully created and resolved a merge conflict
- [ ] Documented what caused the conflict and how you resolved it
- [ ] Closed the issue

## Reviewer checklist

- [ ] Issue shows evidence of conflict resolution (screenshot or explanation)
- [ ] Documentation explains what conflicted and how it was resolved
