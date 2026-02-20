# `Caddy`

<h2>Table of contents</h2>

- [What is `Caddy`](#what-is-caddy)
- [`Caddyfile`](#caddyfile)
  - [`Caddyfile` in this project](#caddyfile-in-this-project)

## What is `Caddy`

`Caddy` is an open-source [web server](./web-development.md#web-server) used in this project as a reverse proxy. A reverse proxy is a server that sits in front of a backend [service](./web-development.md#service) and forwards incoming client requests to it.

In this project, `Caddy` receives requests from clients and forwards them to the `app` [service](./docker.md#service) running inside the `Docker` network.

Docs:

- [Caddy](https://caddyserver.com/docs/)

## `Caddyfile`

A `Caddyfile` is `Caddy`'s configuration file. It defines which port `Caddy` listens on and where to forward requests.

Docs:

- [Caddyfile concepts](https://caddyserver.com/docs/caddyfile/concepts)
- [Environment variables in `Caddyfile`](https://caddyserver.com/docs/caddyfile/concepts#environment-variables)

### `Caddyfile` in this project

In this project, the `Caddyfile` is at [`caddy/Caddyfile`](../../caddy/Caddyfile):

```caddyfile
:{$CADDY_CONTAINER_PORT} {
    reverse_proxy http://app:{$APP_CONTAINER_PORT}
}
```

This configuration:

- Listens on the port specified by the `CADDY_CONTAINER_PORT` [environment variable](./environments.md#environment-variables).
- Forwards all requests to the `app` service on the port specified by `APP_CONTAINER_PORT`.

The `{$VARIABLE}` syntax reads the value of an [environment variable](./environments.md#environment-variables) at runtime.
