# `Docker Compose`

<h2>Table of contents</h2>

- [What is `Docker Compose`](#what-is-docker-compose)
- [Commands](#commands)
  - [`docker compose up`](#docker-compose-up)
  - [`docker compose up` a specific service](#docker-compose-up-a-specific-service)
  - [`docker compose down`](#docker-compose-down)
  - [`docker compose down` a specific service](#docker-compose-down-a-specific-service)
  - [`docker compose ps`](#docker-compose-ps)
  - [`docker compose logs`](#docker-compose-logs)
  - [`docker compose logs` for a specific service](#docker-compose-logs-for-a-specific-service)
  - [`docker compose -f`](#docker-compose--f)
  - [`docker compose --env-file`](#docker-compose---env-file)
  - [`docker compose down -v`](#docker-compose-down--v)

## What is `Docker Compose`

`Docker Compose` runs multi-container apps from a `docker-compose.yml` file.

Example of the file: [`docker-compose.yml`](../docker-compose.yml).

See also:

- [`Docker`](./docker.md) for general `Docker` concepts ([images](./docker.md#image), [containers](./docker.md#container), [volumes](./docker.md#volumes), [health checks](./docker.md#health-checks), etc.).

## Commands

## `docker compose up`

Start services:

```terminal
docker compose up
```

Build images and start services:

```terminal
docker compose up --build
```

## `docker compose up` a specific service

Start a single service (and its dependencies):

```terminal
docker compose up <service>
```

Build and start a single service:

```terminal
docker compose up <service> --build
```

## `docker compose down`

Stop and remove resources created by `up`:

```terminal
docker compose down
```

## `docker compose down` a specific service

Stop and remove a single service:

```terminal
docker compose down <service>
```

## `docker compose ps`

List running containers:

```terminal
docker compose ps
```

## `docker compose logs`

Show logs from all services:

```terminal
docker compose logs
```

## `docker compose logs` for a specific service

Show logs for one service:

```terminal
docker compose logs <service>
```

## `docker compose -f`

Use a specific compose file:

```terminal
docker compose -f <compose-file> up
```

## `docker compose --env-file`

Load environment variables from a specific file:

```terminal
docker compose --env-file <env-file> up --build
```

This is useful when you need different settings for local/dev/test/prod environments.

## `docker compose down -v`

Stop services and remove volumes (including database data):

```terminal
docker compose down -v
```

> [!IMPORTANT]
> The `-v` flag removes named volumes. This deletes all data stored in the database.
> Use this when you want to reset the database to its initial state.
