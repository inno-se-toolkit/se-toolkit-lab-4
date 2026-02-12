# Contribute

- [Docs design principles](#docs-design-principles)
  - [Instructions](#instructions)
    - [Vendor instructions](#vendor-instructions)
    - [Provide fallback instructions](#provide-fallback-instructions)
    - [Localize the instructions](#localize-the-instructions)
    - [Instructions wording](#instructions-wording)
      - [Split compound instructions](#split-compound-instructions)
      - [Finish complete sentences with a `.`](#finish-complete-sentences-with-a-)
        - [Use instructions wording consistently](#use-instructions-wording-consistently)
  - [Commands in `VS Code`](#commands-in-vs-code)
    - [Commands for the `VS Code Terminal`](#commands-for-the-vs-code-terminal)
    - [Commands for the `Command Palette`](#commands-for-the-command-palette)
  - [Options and steps](#options-and-steps)
  - [Table of contents (ToC)](#table-of-contents-toc)
    - [ToC for a document](#toc-for-a-document)
    - [Skip section in the ToC using `HTML`](#skip-section-in-the-toc-using-html)
    - [Skip sections in the ToC using `Markdown All in One`](#skip-sections-in-the-toc-using-markdown-all-in-one)
  - [Little ToC](#little-toc)
    - [Little ToC for options](#little-toc-for-options)
    - [Little ToC for steps](#little-toc-for-steps)
    - [No little ToC](#no-little-toc)
  - [Use heading levels in section titles](#use-heading-levels-in-section-titles)
  - [Lists](#lists)

## Docs design principles

### Instructions

#### Vendor instructions

Vendor the instructions that aren't good enough anywhere else.

#### Provide fallback instructions

One method to complete a step may not work.

A student will be able to proceed if another method is available.

#### Localize the instructions

Provide instructions where they're easy to keep in mind.

Example (task description):

```markdown
## 0. Follow the `Git Workflow`

## 1. Create an issue
```

#### Instructions wording

##### Split compound instructions

Example of a compound instruction:

```markdown
1. Do A and do B.
```

Example of a fixed instruction:

```markdown
1. Do A.
2. Do B.
```

##### Finish complete sentences with a `.`

Example:

```markdown
1. Do A.
2. Do B.
```

###### Use instructions wording consistently

- Navigate somewhere: `Go to X.`
- Click something: `Click X`.
- Choose an option: `Use any of the following methods:` (note "following").
- Complete all steps: `Complete the following steps:` (note "following").

### Commands in `VS Code`

#### Commands for the `VS Code Terminal`

- Write each command for the `VS Code Terminal` in a multi-line code block with the type `terminal`.
- Write an instruction to run in the `VS Code Terminal` as a link before each code block:

  ~~~markdown
  1. [Run using the `VS Code Terminal`](./lab/appendix/vs-code.md#run-a-command-using-the-vs-code-terminal):
  
     ```terminal
     <command>
     ```
  ~~~

#### Commands for the `Command Palette`

- Write an instruction to run using the `Command Palette` as a link before each command that should be run using the `Command Palette`:

   ```markdown
   1. [Run using the `Command Palette`](./lab/appendix/vs-code.md#run-a-command-using-the-terminal):
      `<command>`"
   ```

### Options and steps

- Clearly differentiate between options and steps.

  Options example: "Use any of the following methods."
  
  Steps example: "Complete the following steps."

### Table of contents (ToC)

#### ToC for a document

Insert a ToC right after the document title so that it's easy to navigate the document.

1. [Run using the `Command Palette`](./lab/appendix/vs-code.md#run-a-command-using-the-command-palette):
   `Markdown All in One: Create Table of Contents`

#### Skip section in the ToC using `HTML`

If you want not to add a section to the ToC, use `HTML` tags for the title of that section.

Example:

```markdown
<h2>Heading 2<h2>
```

#### Skip sections in the ToC using `Markdown All in One`

1. Go to [`.vscode/settings.json`](./.vscode/settings.json).
2. Edit the setting `"markdown.extension.toc.levels"`.
3. Specify the min and max level of heading to include into the ToC.

### Little ToC

Provide a little table of contents (ToC) when the list of items is long.

See:

- [Little ToC for options](#little-toc-for-options)
- [Little ToC for steps](#little-toc-for-steps)
- [No little ToC](#no-little-toc)

#### Little ToC for options

Example:

```markdown
Use any of the following methods:

- [Method 1](#method-1)
- [Method 2](#method-2)

### Method 1

### Method 2
```

#### Little ToC for steps
  
Example:
  
```markdown
Complete the following steps:

1. [Step 1](#step-1)
2. [Step 2](#step-2)

### Step 1

### Step 2
```

#### No little ToC

Don't provide a little ToC when all lists of items are short.

Example:
  
```markdown
Use any of the following methods:

Method 1:

1. Do A.
2. Do B.

Method 2:

1. Do C.
1. Do D.
```

### Use heading levels in section titles

When asking to write particular sections in a file, provide file section headings in section titles:

```markdown

Create the file `docs.md` with the following sections:

1. [## Section 1](#-section-1)
2. [## Section 2](#-section-2)

## ## Section 1

## ## Section 2
```

### Lists

- Each ordered list must be `1. 2. 3.`, not `1. 1. 1.`.

  Good list example:
  
  ```markdown
  1.
  2.
  3.
  ```

  Bad list example:
  
  ```markdown
  1.
  1.
  1.
  ```
