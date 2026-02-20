# Repo index

<h2>Table of contents</h2>

- [Lab tasks](#lab-tasks)
  - [Setup](#setup)
  - [Git workflow](#git-workflow)
  - [Required tasks](#required-tasks)
  - [Optional tasks](#optional-tasks)
- [Application source](#application-source)
- [Infrastructure](#infrastructure)
- [Appendix](#appendix)
  - [Architectural views](#architectural-views)
  - [`Caddy`](#caddy)
  - [Coding agents](#coding-agents)
  - [Networks](#networks)
  - [Database](#database)
  - [`Docker`](#docker)
  - [`Docker Compose`](#docker-compose)
  - [Environments](#environments)
  - [File formats](#file-formats)
  - [File system](#file-system)
  - [`Git`](#git)
  - [`Git` in `VS Code`](#git-in-vs-code)
  - [`GitHub`](#github)
  - [`GitLens`](#gitlens)
  - [`HTTP`](#http)
  - [`Linux`](#linux)
  - [Operating system (OS)](#operating-system-os)
  - [`pgAdmin`](#pgadmin)
  - [Placeholders](#placeholders)
  - [`Python`](#python)
  - [Security](#security)
  - [Shell](#shell)
  - [`SSH`](#ssh)
  - [Swagger](#swagger)
  - [Testing](#testing)
  - [Useful programs](#useful-programs)
  - [Visualize the architecture](#visualize-the-architecture)
  - [VM](#vm)
  - [Your VM image](#your-vm-image)
  - [`VS Code`](#vs-code)
  - [Web development](#web-development)

## Lab tasks

### [Setup](lab/tasks/setup.md)

Required and optional steps to get the environment ready: fork, clone, install tools, start services.

### [Git workflow](lab/tasks/git-workflow.md)

Branching, committing, opening PRs, and the review process used throughout the lab.

### Required tasks

1. [Explore the API](lab/tasks/required/task-1.md) — `Swagger UI`, authentication, and the API contract.
2. [Enable and debug the interactions endpoint](lab/tasks/required/task-2.md) — trace the bug between code and database schema.
3. [Implement the learners endpoint](lab/tasks/required/task-3.md) — follow the existing pattern to add a new endpoint.
4. [Deploy to a hardened VM](lab/tasks/required/task-4.md) — firewall, `fail2ban`, SSH restrictions, and deployment.

### Optional tasks

1. [Implement the `/outcomes` endpoint](lab/tasks/optional/task-1.md)
2. [Set up CI with `GitHub Actions`](lab/tasks/optional/task-2.md)

## Application source

Entry point and configuration:

- [`src/app/main.py`](src/app/main.py) — FastAPI app creation and router registration.
- [`src/app/settings.py`](src/app/settings.py) — environment-based configuration.
- [`src/app/auth.py`](src/app/auth.py) — API key authentication dependency.
- [`src/app/database.py`](src/app/database.py) — database session setup.
- [`src/app/run.py`](src/app/run.py) — entry point for running the server.

Routers (HTTP endpoints):

- [`src/app/routers/items.py`](src/app/routers/items.py)
- [`src/app/routers/interactions.py`](src/app/routers/interactions.py)
- [`src/app/routers/learners.py`](src/app/routers/learners.py)

Models (Pydantic schemas):

- [`src/app/models/item.py`](src/app/models/item.py)
- [`src/app/models/interaction.py`](src/app/models/interaction.py)
- [`src/app/models/learner.py`](src/app/models/learner.py)

Database queries:

- [`src/app/db/items.py`](src/app/db/items.py)
- [`src/app/db/interactions.py`](src/app/db/interactions.py)
- [`src/app/db/learners.py`](src/app/db/learners.py)

Database seed:

- [`src/app/data/init.sql`](src/app/data/init.sql) — initial schema and data loaded on first `PostgreSQL` start.

## Infrastructure

- [`docker-compose.yml`](docker-compose.yml) — defines the `app`, `postgres`, `pgadmin`, and `caddy` services.
- [`Dockerfile`](Dockerfile) — builds the application container image.
- [`caddy/Caddyfile`](caddy/Caddyfile) — reverse proxy configuration.
- [`.env.docker.example`](.env.docker.example) — template for container environment variables.
- [`pyproject.toml`](pyproject.toml) — Python project metadata and dependencies.

## Appendix

### [Architectural views](lab/appendix/architectural-views.md)

Component, sequence, and deployment diagram types used to document the system architecture.

### [`Caddy`](lab/appendix/caddy.md)

A web server and reverse proxy configured via a `Caddyfile`.

### [Coding agents](lab/appendix/coding-agents.md)

Using LLMs to help complete development tasks inside `VS Code`.

### [Networks](lab/appendix/computer-networks.md)

IP addresses, hosts, `localhost`, and basic networking concepts.

### [Database](lab/appendix/database.md)

`PostgreSQL`, SQL basics (`SELECT`, `INSERT`, `WHERE`), and database schema concepts.

### [`Docker`](lab/appendix/docker.md)

Container images, running containers, volumes, and health checks.

### [`Docker Compose`](lab/appendix/docker-compose.md)

Running multi-container applications from a `docker-compose.yml` file.

### [Environments](lab/appendix/environments.md)

Environment variables, `.env` files, secrets, and deployment environments.

### [File formats](lab/appendix/file-formats.md)

`Markdown` and `JSON` file formats.

### [File system](lab/appendix/file-system.md)

Files, directories, absolute and relative paths, and filesystem concepts.

### [`Git`](lab/appendix/git.md)

Version control basics, `GitHub flow`, merge conflicts, and `Conventional Commits`.

### [`Git` in `VS Code`](lab/appendix/git-vscode.md)

Cloning repos, switching branches, staging, and committing via the `VS Code` UI.

### [`GitHub`](lab/appendix/github.md)

Repositories, forks, issues, and `GitHub`-specific concepts and placeholders.

### [`GitLens`](lab/appendix/gitlens.md)

`VS Code` extension for exploring Git history, branches, and commits visually.

### [`HTTP`](lab/appendix/http.md)

Requests, responses, status codes, and the `HTTP` protocol.

### [`Linux`](lab/appendix/linux.md)

Distributions, users, permissions, processes, and `Linux` fundamentals.

### [Operating system (OS)](lab/appendix/operating-system.md)

Overview of `Linux`, `macOS`, and `Windows`.

### [`pgAdmin`](lab/appendix/pgadmin.md)

Web-based GUI for browsing tables, running SQL queries, and managing `PostgreSQL` databases.

### [Placeholders](lab/appendix/placeholders.md)

Reference for `<your-github-username>`, `<repo-name>`, and other placeholders used in the lab.

### [`Python`](lab/appendix/python.md)

Syntax, package management with `uv`, testing with `pytest`, and static analysis.

### [Security](lab/appendix/security.md)

API key authentication and VM hardening (firewall, `fail2ban`, SSH configuration).

### [Shell](lab/appendix/shell.md)

Shell variants (`bash`, `zsh`), commands, scripting basics, and directory navigation.

### [`SSH`](lab/appendix/ssh.md)

Key setup, connecting to a VM, and common errors.

### [Swagger](lab/appendix/swagger.md)

`Swagger UI` for exploring and testing API endpoints.

### [Testing](lab/appendix/testing.md)

What testing is, assertions, and links to language-specific testing guides.

### [Useful programs](lab/appendix/useful-programs.md)

Reference for common CLI tools: `git`, `jq`, `find`, `ripgrep`, and others.

### [Visualize the architecture](lab/appendix/visualize-architecture.md)

Tools for creating architecture diagrams: `Draw.io`, `PlantUML`, and `Mermaid`.

### [VM](lab/appendix/vm.md)

Creating, connecting to, and managing a virtual machine.

### [Your VM image](lab/appendix/vm-info.md)

Programs pre-installed on the lab VM image (`docker`, `uv`, `python`, `nix`, etc.).

### [`VS Code`](lab/appendix/vs-code.md)

IDE layout, panels, the `Command Palette`, and editor features.

### [Web development](lab/appendix/web-development.md)

Web servers, REST APIs, `JSON`, and using `Swagger UI` to interact with endpoints.
