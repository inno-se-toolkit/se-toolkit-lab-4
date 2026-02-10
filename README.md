# Lab 2 — Understand, improve, and deploy a web server

<h2>Table of contents</h2>

- [Lab story](#lab-story)
- [Learning advice](#learning-advice)
- [Learning outcomes](#learning-outcomes)
- [Tasks](#tasks)
  - [Required](#required)
  - [Optional](#optional)

## Lab story

You were hired by a company that develops a novel e-learning system.

The system recommends educational resources to students.

You have joined a [back end](https://roadmap.sh/backend) team in that company.

Your team is working on a read-only service called **Course Materials Service**.

The service is implemented using the [`FastAPI`](https://fastapi.tiangolo.com/) framework in [`Python`](https://www.python.org/).

Currently, it serves courses-related items (courses, labs, tasks, steps).

For simplicity, the service uses data stored is [`JSON`](https://en.wikipedia.org/wiki/JSON) files (`JSON resources`) in [`src/app/data/course_items.json`](./src/app/data/course_items.json).

A senior engineer explains your first assignment:

> Before we give you bigger features, you need to show you can:
>
> 1. Run our back end service on your machine.
> 2. Verify that it’s working: query the `/status` endpoint.
> 3. Investigate and fix a bug in the `/items` endpoint.
> 4. Deploy your updated service to a remote `Linux` server.
>
> We expect that you'll communicate through issues and PRs and deliver a working deployment.

## Learning advice

You need to read the lab tasks and docs to understand them. Do what you can by yourself.

When stuck or unsure, feel free to ask an LLM:

> Give me directions on how to solve this task. I want to maximize learning.

You can also ask LLMs to explain the logic behind tasks if you don't understand it. Example:

> Why is this task important? What exactly do they want to teach me?

Remember: Use LLMs as a tool to enhance your understanding, not replace it.

Always critically evaluate the information provided by LLMs.

Verify this information against credible sources such as official documentation, course materials, and what you observe in reality.

## Learning outcomes

By the end of this lab, you should be able to:

- Follow the [`Git workflow`](./lab/tasks/git-workflow.md).
- Check your work against specified acceptance criteria.
- Explore the code of an existing web server written in `Python`.
- Run the web server on your computer.
- Query the web server.
- Inspect the responses of the web server.
- Test the web server.
- Identify a bug (problem) in the web server.
- Document the bug using a `GitHub` issue.
- Submit a fix of the bug as a PR.
- Deploy the fixed web server to a remote `Linux` virtual machine (VM).
- Test the deployed web server.

## Tasks

### Required

1. [Lab setup](./lab/setup.md).
2. [Run the service](./lab/tasks/required/task-1.md)
3. [Identify, report, and fix a bug](./lab/tasks/required/task-2.md)
4. [Run the service using `Docker Compose`](./lab/tasks/required/task-3.md)

5. [Deploy the service to the VM](./lab/tasks/required/task-4.md)

### Optional

1. [Implement the `/outcomes` endpoint](./lab/tasks/optional/task-1.md)
2. [Make your VM a proxy to your partner's VM](./lab/tasks/optional/task-2.md)

