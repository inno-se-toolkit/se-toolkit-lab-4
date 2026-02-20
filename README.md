# Lab 3 — REST API, Database, and Security

> [!CAUTION]
> The lab is UNDER CONSTRUCTION!!
> Instructions may change.

<h2>Table of contents</h2>

- [Lab story](#lab-story)
- [Learning advice](#learning-advice)
- [Learning outcomes](#learning-outcomes)
- [Tasks](#tasks)
  - [Prerequisites](#prerequisites)
  - [Required](#required)
  - [Optional](#optional)

## Lab story

You were hired by a company that develops a novel e-learning system.

The system recommends educational resources to students.

You joined a [back end](https://roadmap.sh/backend) team working on a web server for the **Learning Management Service**.

The web server is implemented using the [`FastAPI`](https://fastapi.tiangolo.com/) framework in [`Python`](https://www.python.org/) and uses a [`PostgreSQL`](https://www.postgresql.org/) database.

The prototype works and is deployed. Now the team needs to make it production-ready: understand the API contract, expose interaction logs, add a new endpoint for learners, secure the service, and deploy it on a hardened VM.

A senior engineer explains your next assignment:

> 1. Explore the API documentation and learn how to authenticate.
> 2. Enable and debug the broken `/interactions` endpoint.
> 3. Implement the `/learners` endpoint using the existing pattern.
> 4. Deploy the secured service to a hardened VM.

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

- Explore a REST API using `Swagger UI`.
- Authenticate API requests using an API key.
- Examine a database using `pgAdmin`.
- Debug a broken endpoint by tracing code and comparing to the database schema.
- Implement a new endpoint by following an existing reference implementation.
- Deploy a service with API key authentication.
- Harden a Linux server (firewall, `fail2ban`, SSH restrictions).

In simple words, you should be able to say:
>
> 1. I explored an API using Swagger and authenticated with an API key!
> 2. I debugged a broken endpoint by comparing the code to the database!
> 3. I implemented a new endpoint by following an existing pattern!
> 4. I deployed a secured service on a hardened VM!

## Tasks

### Prerequisites

1. [Lab setup](./lab/tasks/setup.md).
2. (Optional) Check the [repo index](./index.md).

### Required

1. [Explore the API](./lab/tasks/required/task-1.md)
2. [Enable and debug the interactions endpoint](./lab/tasks/required/task-2.md)
3. [Implement the learners endpoint](./lab/tasks/required/task-3.md)
4. [Deploy to a hardened VM](./lab/tasks/required/task-4.md)

### Optional

1. [Implement the `/outcomes` endpoint](./lab/tasks/optional/task-1.md)
2. [Set up CI with `GitHub Actions`](./lab/tasks/optional/task-2.md)
