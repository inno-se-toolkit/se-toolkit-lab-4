# Lab 2 — Understand, improve, and deploy a web server

<h2>Table of contents</h2>

- [Lab overview](#lab-overview)
- [Lab story](#lab-story)
- [Learning advice](#learning-advice)
- [Learning outcomes](#learning-outcomes)
- [Tasks](#tasks)
  - [Setup (~30 min)](#setup-30-min)
  - [Required tasks (~2 hours)](#required-tasks-2-hours)
  - [Optional tasks](#optional-tasks)
- [Additional Resources on `Git`](#additional-resources-on-git)

## Lab overview

1. Run a web server.
2. Fix a bug.
3. Deploy the web server.

You'll use `Git` and `GitHub` for development, collaboration, and deployment.

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

- Use `Git` and `GitHub` to structure your work and collaborate with peers (commits with clear messages, branches, issues, pull requests, and reviews).
- Check your work against specified acceptance criteria.
- Explain the basic architecture of a real-world digital product in terms of components, data flow, deployment, and tech roles.
- Reflect on your career in tech, examine your current skillset, and plan for the future.

After this lab, you should be able to say:

> I can use `Git` and `GitHub`.
>
> I understand how software products can be structured.
>
> I know how I can grow as an IT specialist.

## Tasks

### Setup (~30 min)

First complete the [lab setup](./lab/setup.md).

### Required tasks (~2 hours)

For all required tasks, you must follow the same [`Git workflow`](./lab/tasks/git-workflow.md).

1. [Practice the `Git workflow`](./lab/tasks/required/task-0.md#practice-the-git-workflow) (~15 min)
2. [Choose a product and study its architecture](./lab/tasks/required/task-1.md#choose-a-product-and-study-its-architecture) (~30 min)
3. [Study tech roles involved in the chosen product](./lab/tasks/required/task-2.md#study-tech-roles-involved-in-the-chosen-product) (~30 min)
4. [Compare your tech skills with the market needs](./lab/tasks/required/task-3.md#compare-your-tech-skills-with-the-market-needs) (~30 min)

### Optional tasks

Complete all optional tasks to leave up to 1 hour early (lab is 3 hours):

1. [Resolve a merge conflict](./lab/tasks/optional/task-1.md#resolve-a-merge-conflict).
2. [Add a CI check](./lab/tasks/optional/task-2.md#add-a-ci-check)
3. [Create a release](./lab/tasks/optional/task-3.md#create-a-release)
4. [Plan skill development](./lab/tasks/optional/task-4.md#plan-skill-development)

## Additional Resources on `Git`

- Read this [tutorial](https://hackmd.io/@aabounegm/SWP-git) to learn about `Git`, `Github`, and other `Git` workflows.
- Short videos to build your mental model of how `Git` works:
  - [Git Explained in 100 Seconds](https://www.youtube.com/watch?v=hwP7WQkmECE)
  - [What is Git? Explained in 2 Minutes!](https://www.youtube.com/watch?v=2ReR1YJrNOM)
  - [A brief introduction to Git for beginners](https://www.youtube.com/watch?v=r8jQ9hVA2qs)
  - [How Git Works: Explained in 4 Minutes](https://www.youtube.com/watch?v=e9lnsKot_SQ)
  - [Git MERGE vs REBASE: Everything You Need to Know](https://www.youtube.com/watch?v=0chZFIZLR_0)
- Practice on [Learn Git Branching](https://learngitbranching.js.org/) (focus on merge/rebase and conflicts).
- Read about [`GitHub flow`](https://docs.github.com/en/get-started/using-github/github-flow).
- Learn about [`Conventional Commits`](https://www.conventionalcommits.org/en/v1.0.0/) for commit message formatting.
