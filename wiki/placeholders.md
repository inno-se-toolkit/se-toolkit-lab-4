# Placeholders

<h2>Table of contents</h2>

- [`<your-github-username>`](#your-github-username)
- [`<repo-name>`](#repo-name)
- [`<repo-url>`](#repo-url)
- [`<repo-owner-github-username>`](#repo-owner-github-username)
- [`<your-fork-url>`](#your-fork-url)
- [`<db-name>`](#db-name)
- [`<api-port>`](#api-port)
- [`<frontend-port>`](#frontend-port)
- [`<frontend-url>`](#frontend-url)

## `<your-github-username>`

See [`<your-github-username>`](./github.md#your-github-username) in the [`GitHub` wiki](./github.md).

## `<repo-name>`

See [`<repo-name>`](./github.md#repo-name) in the [`GitHub` wiki](./github.md).

## `<repo-url>`

See [`<repo-url>`](./github.md#repo-url) in the [`GitHub` wiki](./github.md).

## `<repo-owner-github-username>`

See [`Repository owner`](./github.md#repository-owner) in the [`GitHub` wiki](./github.md).

## `<your-fork-url>`

See [`<your-fork-url>`](./github.md#your-fork-url) in the [`GitHub` wiki](./github.md).

## `<db-name>`

See [`<db-name>`](./database.md#db-name) in the [`Database` wiki](./database.md).

## `<api-port>`

The port the API is accessible on. From your `.env.docker.secret` file, this is `CADDY_HOST_PORT`.

## `<frontend-port>`

The port `Caddy` serves the front-end on. This is the same as `CADDY_HOST_PORT` (default: `42002`), because `Caddy` serves both the front-end and the API on the same port.

## `<frontend-url>`

The full URL of the front-end: `http://<your-vm-ip-address>:<frontend-port>/`.
