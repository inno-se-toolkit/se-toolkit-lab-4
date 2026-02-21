# Lab authoring conventions (condensed)

Source of truth: `lab/design/conventions.md`

## Task document structure (§3)

```
# <Task title>
<h4>Time</h4>  ~N min
<h4>Purpose</h4>  One sentence.
<h4>Context</h4>  1–3 sentences.
<h4>Table of contents</h4>  (auto-generated, HTML tag so it's excluded from ToC)
## Steps
### 0. Follow the `Git workflow`   ← omit if task produces no commits
### 1. Create a `Lab Task` issue   ← always first step
### N. Finish the task             ← last step: PR or comment on issue
----
## Acceptance criteria             ← - [ ] checkbox format, concrete & verifiable
```

## Writing conventions (§4)

- **Instructions:** "Go to X." / "Click X." / "Use any of the following methods:" / "Complete the following steps:"
- **Split compound instructions.** Never "Do A and do B." → two numbered steps.
- **Sentences end with `.`**
- **Ordered lists:** use `1. 2. 3.` — never `1. 1. 1.`
- **Terminal commands:** `terminal` fenced block, preceded by link to appendix.
- **Command Palette:** inline backtick, preceded by link to appendix.
- **Notes/tips/warnings:** `> [!NOTE]`, `> [!TIP]`, `> [!IMPORTANT]` — never indent inside list items.
- **Images:** `<img alt="..." src="..." style="width:400px"></img>`
- **Hints/solutions:** `<details><summary>...</summary>` collapsible blocks.
- **Commit messages:** conventional commits (`fix:`, `feat:`, `docs:`) in a `text` code block.
- **Technical terms in backticks:** `VS Code`, `Git`, `Docker`, `Python`, `SQL`, `WSL`, `SSH`.
- **Placeholders:** `<angle_brackets>` — never hardcode env-specific values (URLs, ports).
- **Links:** relative paths; link to appendix on first mention per section. Compound phrases (e.g., `` `GitHub` pull request ``): one link to the concept's section, not two adjacent links.
- **Alerts:** never indent GFM alerts; use bold **Note:** as fallback inside lists.
- **ToC:** `<h2>Table of contents</h2>` (HTML) so heading is excluded from auto-generated ToC.
- **`<!-- no toc -->`** before lists you don't want in the ToC.

## Appendix section pattern (§12.13)

```markdown
## <Feature Name>
<1-2 sentence explanation.>
Location: see [`Basic Layout`](#basic-layout).
Docs: - [Official docs](https://...)
Actions: - [Action 1](#action-1)
### Action 1
<Steps>
```

## Task design rules (§12, selected)

- Step 0 ("Follow the Git workflow") present only when task produces commits.
- Step 1 always: "Create a `Lab Task` issue" with title `[Task] <title>`.
- Last step: create PR + get review (code tasks) OR comment on issue with evidence (non-code tasks).
- Show expected output after commands.
- `> [!NOTE]` blocks explain "why", not just "what".
- Cross-task references instead of repeating steps: `[Run the web server](./task-1.md#8-...)`.
- Three seed tiers: reference (working), debug (commented + bugs), implement (placeholder templates).
- Placeholder templates include `# Reference:` mapping new resource to reference counterpart.

## Three task endings (§12.11)

1. **Code tasks:** PR → review → merge. Criteria: PR approved, merged, tests pass.
2. **Non-code tasks:** comment with evidence on issue, close issue.
3. **Auto-checked deliverables:** commit a structured file checked by regex/script.
