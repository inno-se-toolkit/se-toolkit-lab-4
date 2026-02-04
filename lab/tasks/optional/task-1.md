# Resolve a merge conflict

1. Create the issue `[Task] Resolve a merge conflict`.
2. (Optional) Complete the first three tasks in `Introduction Sequence` on [Learn Git Branching](https://learngitbranching.js.org/).
3. Open your cloned fork in `VS Code`.
4. Switch to the `main` branch.

   ```console
   git switch main
   ```

   Alternatively, use [`Command Palette`](https://code.visualstudio.com/docs/getstarted/getting-started#_access-commands-with-the-command-palette) -> `GitLens: Git Switch to...`.

5. Create two branches from `main`:

   ```console
   git branch feature-1
   git branch feature-2
   ```

   Alternatively, use `Command Palette` -> `GitLens: Git Create Branch...`.

6. On `feature-1` branch:
    - Edit a file (e.g., change the first line in `README.md`).
    - Commit your changes.
7. On `feature-2` branch:
    - Edit the **same lines** in the same file that you edited on the `feature-1` branch.
    - The changes on `feature-2` must differ from changes on `feature-1`.
    - Commit your changes.
8. Merge `feature-2` into `feature-1`.

    ```console
    git switch feature-1
    git merge feature-2
    ```

9. This will create a merge conflict since both branches modified the same lines.

10. In the `Primary Sidebar` -> `Merge Changes` -> Click the file that you changed.
11. The file will open.
12. Click inside that file.
13. Click `Resolve in Merge Editor` to resolve the merge conflict in the [3-way merge editor](https://code.visualstudio.com/docs/sourcecontrol/merge-conflicts#_use-the-3way-merge-editor).
14. Accept a change that you like more.
15. Click `Complete Merge`.
16. In the `Primary Sidebar` -> `Source Control` -> `Staged Changes` -> Click the file to see changes that you applied.
17. Click `Continue`.
18. Click `Publish Branch` to push `feature-1` to `GitHub`.
19. Create a PR from `feature-1` to `main`.
20. In the PR summary explain:
    - What conflicted (1–2 sentences).
    - How you resolved the conflict (1–2 sentences).
21. Provide a link to the PR in the issue description.
22. Close the PR. Don't merge it.
23. Close the issue.
