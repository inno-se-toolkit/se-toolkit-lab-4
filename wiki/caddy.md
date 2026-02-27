# `Caddy`

<h2>Table of contents</h2>

- [What is `Caddy`](#what-is-caddy)
- [`Caddyfile`](#caddyfile)
  - [`Caddyfile` in this project](#caddyfile-in-this-project)

## What is `Caddy`

`Caddy` is an open-source [web server](./web-development.md#web-server) used in this project as a reverse proxy. A reverse proxy is a server that sits in front of a backend [service](./web-development.md#service) and forwards incoming client requests to it.

In this project, `Caddy` serves the front-end static files and forwards API requests to the `app` [service](./docker.md#service) running inside the `Docker` network.

Docs:

- [Caddy](https://caddyserver.com/docs/)

## `Caddyfile`

A `Caddyfile` is `Caddy`'s configuration file. It defines which port `Caddy` listens on and where to forward requests.

Docs:

- [Caddyfile concepts](https://caddyserver.com/docs/caddyfile/concepts)
- [Environment variables in `Caddyfile`](https://caddyserver.com/docs/caddyfile/concepts#environment-variables)

### `Caddyfile` in this project

In this project, the `Caddyfile` is at [`caddy/Caddyfile`](../caddy/Caddyfile):

```caddyfile
:{$CADDY_CONTAINER_PORT} {
    handle /items* {
        reverse_proxy http://app:{$APP_CONTAINER_PORT}
    }
    handle /learners* {
        reverse_proxy http://app:{$APP_CONTAINER_PORT}
    }
    handle /interactions* {
        reverse_proxy http://app:{$APP_CONTAINER_PORT}
    }
    handle /docs* {
        reverse_proxy http://app:{$APP_CONTAINER_PORT}
    }
    handle /openapi.json {
        reverse_proxy http://app:{$APP_CONTAINER_PORT}
    }
    handle {
        root * /srv
        try_files {path} /index.html
        file_server
    }
}
```

This configuration:

- Listens on the port specified by the `CADDY_CONTAINER_PORT` [environment variable](./environments.md#environment-variables).
- Routes API paths (`/items*`, `/learners*`, `/interactions*`, `/docs*`, `/openapi.json`) to the `app` service.
- Serves the front-end static files from `/srv` for all other paths. The `try_files` directive falls back to `index.html` for client-side routing.

The `{$VARIABLE}` syntax reads the value of an [environment variable](./environments.md#environment-variables) at runtime.
