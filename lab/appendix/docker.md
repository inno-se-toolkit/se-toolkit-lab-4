# `Docker`

<h2>Table of contents</h2>

- [Image](#image)
- [Container](#container)
- [`Docker`](#docker)
  - [`docker run`](#docker-run)
  - [`docker ps`](#docker-ps)
- [`Docker Compose`](#docker-compose)
  - [`docker compose up`](#docker-compose-up)
  - [`docker compose down`](#docker-compose-down)
  - [`docker compose -f`](#docker-compose--f)
  - [`docker compose --env-file`](#docker-compose---env-file)

## Image

<!-- TODO -->

## Container

<!-- TODO reference image -->

A container is an isolated runtime for an application and its dependencies.

Why containers are useful:

- The app runs consistently across machines.
- Dependencies are packaged with the app.
- Multiple services can run side-by-side with explicit ports and networks.

## `Docker`

`Docker` is a platform for building and running containers.

### `docker run`

`docker run` starts a container from an image.

Common pattern:

```terminal
docker run --name <container-name> -p <host-port>:<container-port> <image-name>
```

Useful flags:

- `-d` - run in background (detached mode).
- `--rm` - remove container after it exits.
- `-e KEY=VALUE` - pass environment variable.

### `docker ps`

`docker ps` shows running containers.

Useful variants:

```terminal
docker ps
docker ps -a
```

- `docker ps` - only running containers.
- `docker ps -a` - all containers (including stopped).

## `Docker Compose`

`Docker Compose` runs multi-container apps from a `docker-compose.yml` file.

Example of how containers fit together:

```text
-------------------- Docker host --------------------
|                                                     |
|  ------------ container ------------               |
|  | Linux userspace runtime         |               |
|  | app/service process             |               |
|  ----------------------------------               |
|                                                     |
|  ------------ container ------------               |
|  | Linux userspace runtime         |               |
|  | another app/service process     |               |
|  ----------------------------------               |
|                                                     |
-------------------------------------------------------
```

### `docker compose up`

Start services:

```terminal
docker compose up
```

Build images and start services:

```terminal
docker compose up --build
```

### `docker compose down`

Stop and remove resources created by `up`:

```terminal
docker compose down
```

### `docker compose -f`

Use a specific compose file:

```terminal
docker compose -f docker-compose.prod.yml up -d
```

### `docker compose --env-file`

Load environment variables from a specific file:

```terminal
docker compose --env-file .env.docker.secret up --build
```

This is useful when you need different settings for local/dev/test/prod environments.
