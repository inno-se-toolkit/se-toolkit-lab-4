# Lab 4 — Testing, Front-end, and AI Agents

> [!CAUTION]
> The lab is UNDER CONSTRUCTION!!
> Instructions may change.

[Sync your cloned repo with the upstream](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/syncing-a-fork#syncing-a-fork-branch-from-the-command-line) from time to time.

<h2>Table of contents</h2>

- [Lab story](#lab-story)
- [Learning advice](#learning-advice)
- [Learning outcomes](#learning-outcomes)
- [Tasks](#tasks)
  - [Prerequisites](#prerequisites)
  - [Required](#required)
  - [Optional](#optional)

## Lab story

You are on the back-end team for the **Learning Management Service**.

The `API` is deployed and secured. Now the team wants to prove it works with real tests, add a front-end so users can interact with the data, and establish the habit of using AI agents as development tools.

A senior engineer explains your next assignment:

> 1. Redeploy the back-end and observe how requests flow from `Swagger` through the `API` to the database.
> 2. Write unit and end-to-end tests, discover existing bugs, and fix them.
> 3. Add a front-end to the system and modify it using an AI coding agent.

> [!IMPORTANT]
> Communicate through issues and PRs and deliver a working deployment.

## Learning advice

Read the tasks and complete them by yourself.

When stuck or not sure, ask an LLM:

> Give me directions on how to solve this task. I want to maximize learning.

> Why is this task important? What exactly do I need to do?

Provide enough context by giving it the whole file, not one or two lines.

Remember: Use the LLM to enhance your understanding, not replace it.

Evaluate LLM answers critically, and verify them against credible sources such as official documentation, course materials, and what you observe in reality.

## Learning outcomes

By the end of this lab, you should be able to:

- Deploy a back-end service to a remote VM.
- Use browser developer tools to inspect `HTTP` requests.
- Examine the request path from `Swagger` through the `API` to the database.
- Construct unit and end-to-end tests for boundary-value cases.
- Diagnose bugs from failing test output and apply fixes.
- Use an AI coding agent to generate and refine tests.
- Differentiate between a dev server and production static files.
- Use an AI coding agent to modify front-end code and observe the result.

In simple words, you should be able to say:
>
> 1. I redeployed the system and observed requests flowing from Swagger to the API to the database!
> 2. I wrote tests, found bugs, and fixed them!
> 3. I added a front-end and modified it using an AI coding agent!

## Tasks

### Prerequisites

1. Complete the [lab setup](./lab/tasks/setup.md)
2. Set up an [AI coding agent](./wiki/coding-agents.md)

### Required

1. [Observe system component interaction](./lab/tasks/required/task-1.md)
2. [Back-end testing](./lab/tasks/required/task-2.md)
3. [Add front-end](./lab/tasks/required/task-3.md)

### Optional

1. [Set up CI/CD with `GitHub Actions`](./lab/tasks/optional/task-1.md)
