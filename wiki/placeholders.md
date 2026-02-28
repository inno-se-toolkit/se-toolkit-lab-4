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
- [`<app-port>`](#app-port)
- [`<app-url>`](#app-url)

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

The port the API (backend) is accessible on.

This is the value of `CADDY_HOST_PORT` in your `.env.docker.secret` file.

## `<frontend-port>`

The port `Caddy` serves the frontend on.

This is the value of `CADDY_HOST_PORT` in your `.env.docker.secret` file.

## `<app-port>`

`Caddy` serves both the frontend and the API on the same port (see [`<api-port>`](#api-port), [`<frontend-port>`](#frontend-port)).

## `<app-url>`

The full URL of the app deployed to [your VM](./vm.md#your-vm): `http://<your-vm-ip-address>:<app-port>/`.

See [`<your-vm-ip-address>`](./vm.md#your-vm-ip-address) and [`<app-port>`](#app-port).
