# Writing conventions — applies to both tasks and wiki

- [4.1. Instructions wording](#41-instructions-wording)
- [4.2. Terminal commands](#42-terminal-commands)
- [4.3. Command Palette commands](#43-command-palette-commands)
- [4.4. Options vs steps](#44-options-vs-steps)
- [4.5. Ordered lists](#45-ordered-lists)
- [4.6. Little ToC](#46-little-toc)
- [4.7. Table of contents](#47-table-of-contents)
- [4.8. Links and cross-references](#48-links-and-cross-references)
- [4.9. Notes, tips, warnings](#49-notes-tips-warnings)
- [4.10. Images](#410-images)
- [4.11. Collapsible hints and solutions](#411-collapsible-hints-and-solutions)
- [4.12. Commit message format](#412-commit-message-format)
- [4.13. Diagrams](#413-diagrams)
- [4.14. `<!-- TODO -->` comments](#414----todo----comments)
- [4.15. `<!-- no toc -->` comments](#415----no-toc----comments)
- [4.16. Code snippets in explanations](#416-code-snippets-in-explanations)
- [4.17. Heading levels in section titles](#417-heading-levels-in-section-titles)
- [4.18. Inline formatting of technical terms](#418-inline-formatting-of-technical-terms)
- [4.19. Steps with sub-steps](#419-steps-with-sub-steps)
- [4.20. Placeholders in docs](#420-placeholders-in-docs)

## 4.1. Instructions wording

| Action             | Wording                                        |
| ------------------ | ---------------------------------------------- |
| Navigate somewhere | `Go to X.`                                     |
| Click something    | `Click X.`                                     |
| Choose an option   | `Method N:` prefix (see [4.6](#46-little-toc)) |
| Complete all steps | `Complete the following steps:`                |

- **Split compound instructions.** Never write "Do A and do B." Instead, split into two numbered steps.
- **Finish complete sentences with a `.`**

## 4.2. Terminal commands

Write each command for the `VS Code Terminal` in a multi-line code block with the type `terminal`. Always precede with a link to the wiki.

From a task file:

~~~markdown
1. [Run using the `VS Code Terminal`](../../../wiki/vs-code.md#run-a-command-using-the-vs-code-terminal):

   ```terminal
   <command>
   ```
~~~

From a wiki file:

~~~markdown
1. [Run using the `VS Code Terminal`](./vs-code.md#run-a-command-using-the-vs-code-terminal):

   ```terminal
   <command>
   ```
~~~

Exception: `vs-code.md` itself is exempt because the link would be self-referential.

## 4.3. Command Palette commands

From a task file:

~~~markdown
1. [Run using the `Command Palette`](../../../wiki/vs-code.md#run-a-command-using-the-command-palette):
   `<command>`
~~~

From a wiki file:

~~~markdown
1. [Run using the `Command Palette`](./vs-code.md#run-a-command-using-the-command-palette):
   `<command>`
~~~

Exception: `vs-code.md` itself is exempt because the link would be self-referential.

## 4.4. Options vs steps

Clearly differentiate:

- **Options:** List with `Method N:` prefix (see [4.6](#46-little-toc)).
- **Steps:** "Complete the following steps:" (then list steps in order).

## 4.5. Ordered lists

Each ordered list must use `1. 2. 3.`, **not** `1. 1. 1.`.

## 4.6. Little ToC

Provide a little table of contents when the list of options or steps is long. Use `Method N:` prefixes with full heading text as the link:

```markdown
<!-- no toc -->
- Method 1: [Do X using the `VS Code Terminal`](#do-x-using-the-vs-code-terminal)
- Method 2: [Do X using `GitLens`](#do-x-using-gitlens)

### Do X using the `VS Code Terminal`

### Do X using `GitLens`
```

Don't provide a little ToC when all lists of items are short.

## 4.7. Table of contents

- Insert a ToC right after the document title.
- `Markdown All in One` generates and updates the ToC automatically from your headings. Write sections first, then let the extension generate the ToC. Fix any anchor indices (e.g., step numbers) in the ToC afterwards if needed.
- To skip a section from the ToC, use HTML tags for the title: `<h2>Heading</h2>`.
- To control which heading levels appear in the ToC, edit `"markdown.extension.toc.levels"` in `.vscode/settings.json`.

## 4.8. Links and cross-references

- Link to wiki sections whenever a concept or tool is mentioned for the first time in a section. Don't link when it's mentioned second time. This applies to both task docs and wiki docs. This ensures readers who jump to a specific section can still find relevant references.
- Wiki files can and should cross-reference other wiki files: `[concept name](./other-wiki.md#<section>)`.
- Use relative paths for all links.
- Provide a link to each file that exists in the repo.
- Link format for wiki references from tasks: `[concept name](../../../wiki/<file>.md#<section>)`.
- Tasks can reference steps in other tasks: `[Run the web server](./task-1.md#8-run-the-web-server)`.
- **Don't link to the top-level heading** (the `#` title) of a file. Link to a specific subsection instead. The top-level heading is just the document title — linking to it is the same as linking to the file with no anchor. Good: `[Linux](./linux.md#what-is-linux)`. Bad: `[Linux](./linux.md#linux)`.
- **Compound phrases:** When a tool name and a concept naturally form a single phrase (e.g., `` `GitHub` pull request ``, `` `VS Code` Terminal ``), link the whole phrase to the concept's section rather than creating two adjacent links. Good: `` [`GitHub` pull request](./github.md#pull-request) ``. Bad: `` [`GitHub`](./github.md) [pull request](./github.md#pull-request) ``.

## 4.9. Notes, tips, warnings

Use GitHub-flavored Markdown alerts:

```markdown
> [!NOTE]
> Explanatory information.

> [!TIP]
> Helpful suggestion.

> [!IMPORTANT]
> Critical information.
```

- **Do not indent alerts.** GitHub-flavored Markdown alerts (`> [!NOTE]`, etc.) do not render correctly when indented (e.g., inside a list item). If you need an alert inside a list, restructure the content to place the alert at the top indentation level, or use bold text (e.g., **Note:**) as a fallback.

## 4.10. Images

Use HTML `<img>` tags with a `style` attribute for width control:

```markdown
<img alt="Description" src="../../images/wiki/vs-code/example.png" style="width:400px"></img>
```

## 4.11. Collapsible hints and solutions

Use `<details>` and `<summary>` for hints and solutions:

```markdown
1. <details><summary>Click to open a hint</summary>

   The hint text here.

   </details>

2. <details><summary>Click to open the solution</summary>

   The solution text here.

   </details>
```

## 4.12. Commit message format

Use [conventional commits](https://www.conventionalcommits.org/):

```text
<type>: <short description>

- <detail 1>
- <detail 2>
```

Common types:

- `fix:` — bug fixes
- `feat:` — new features or additions
- `docs:` — documentation changes

When a task specifies a commit message, provide it in a code block:

```markdown
   Use a multi-line message:

   \`\`\`text
   <type>: <short description>

   - <detail 1>
   - <detail 2>
   \`\`\`
```

## 4.13. Diagrams

- Use `.drawio.svg` format for editable diagrams (created with [draw.io](https://app.diagrams.net/)).
- Store diagrams in `lab/images/`.
- Reference them with standard Markdown image syntax: `![Alt text](../images/diagram.drawio.svg)`.

## 4.14. `<!-- TODO -->` comments

Use `<!-- TODO description -->` HTML comments for work-in-progress sections. These are invisible to students but trackable by authors using the `Todo Tree` VS Code extension.

## 4.15. `<!-- no toc -->` comments

Use `<!-- no toc -->` before a list to prevent `Markdown All in One` from including it in the auto-generated ToC:

```markdown
<!-- no toc -->
- [Method 1](#method-1)
- [Method 2](#method-2)
```

## 4.16. Code snippets in explanations

When walking students through code (e.g., debugging a bug), show the relevant code snippet in a fenced code block with the language specified:

~~~markdown
1. Look at the line where the `result` variable gets a value:

   ```<language>
   result = find_by_id(item_id, collection=data)
   ```

   The function `find_by_id` searches for an item in a given collection.
~~~

## 4.17. Heading levels in section titles

When asking to write particular sections in a file, provide file section headings in section titles:

```markdown

Create the file `docs.md` with the following sections:

1. [## Section 1](#-section-1)
2. [## Section 2](#-section-2)

## ## Section 1

## ## Section 2
```

## 4.18. Inline formatting of technical terms

Wrap tool names, technical terms, and acronyms in backticks: `` `VS Code` ``, `` `Git` ``, `` `Docker` ``, `` `Python` ``, `` `SQL` ``, `` `WSL` ``, `` `SSH` ``.

## 4.19. Steps with sub-steps

When multiple actions serve a single logical goal, group them under one step. Write the step as a complete sentence followed by "Complete the following steps:", then list the sub-steps as a nested ordered list:

```markdown
1. Configure the environment. Complete the following steps:
   1. Open `.env.example`.
   2. Copy it to `.env.secret`.
   3. Fill in the values.
```

When actions don't share a logical goal, flatten them into separate top-level steps (see [4.1. Instructions wording](#41-instructions-wording)).

## 4.20. Placeholders in docs

Use placeholders instead of hardcoded environment-specific values (e.g., URLs, ports from `.env`). This keeps docs accurate when students change their configuration.

Bad: `` Open <http://127.0.0.1:5050> in a browser. ``

Good: `` Open <pgadmin-url> in a browser. ``

Define every placeholder in `wiki/placeholders.md`. Each placeholder gets its own section that links to its definition in the relevant wiki doc.
