# Lab

<h2>Table of contents</h2>

- [What is a lab](#what-is-a-lab)
- [Constants](#constants)
  - [`<lab-repo-name>`](#lab-repo-name)
- [Prompts for coding agents](#prompts-for-coding-agents)
  - [Make the task instructions linear](#make-the-task-instructions-linear)
  - [Give directions on solving the task](#give-directions-on-solving-the-task)

## What is a lab

A lab is the time for learning:

- under the supervision of a TA
- together with your classmates
- with the help of AI assistants (chatbots, [coding agents](./coding-agents.md#what-is-a-coding-agent), etc.)

## Constants

### `<lab-repo-name>`

`se-toolkit-lab-4` (without `<` and `>`).

## Prompts for coding agents

> [!IMPORTANT]
> It's recommended to use a [coding agent](./coding-agents.md#what-is-a-coding-agent)
> because it can read files in your repo and understand the project context
> better than an LLM in a web chat.

<!-- no toc -->
- [Make the task instructions linear](#make-the-task-instructions-linear)
- [Give directions on solving the task](#give-directions-on-solving-the-task)

### Make the task instructions linear

```md
Write complete instructions for @task-1 in tmp/instructions/task-1.md.

Substitute placeholders with concrete values.

Inline relevant instructions from wiki where necessary.
```

### Give directions on solving the task

```md
I want to maximize learning.

Give me directions on how to solve this task.

Why is this task important? 

What exactly do I need to do?
```
