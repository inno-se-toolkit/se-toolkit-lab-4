# `Docker Compose`

<h2>Table of contents</h2>

- [What is `Docker Compose`](#what-is-docker-compose)
- [Service](#service)
  - [Service name](#service-name)
- [`Docker Compose` networking](#docker-compose-networking)

## What is `Docker Compose`

`Docker Compose` runs multi-container apps from a `docker-compose.yml` file.

Example of the file: [`docker-compose.yml`](../docker-compose.yml).

See also:

- [`Docker`](./docker.md) for general `Docker` concepts ([images](./docker.md#image), [containers](./docker.md#container), [volumes](./docker.md#volumes), [health checks](./docker.md#health-checks), etc.).

## Service

<!-- TODO -->

### Service name

<!-- TODO -->

## `Docker Compose` networking

`Docker Compose` creates a [network](./computer-networks.md#what-is-a-network) where [services](#service) can reach each other by their [service name](#service-name).

Docs:

- [Networking in Compose](https://docs.docker.com/compose/how-tos/networking/)
