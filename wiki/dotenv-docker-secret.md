# `.env.docker.secret`

- [What is `.env.docker.secret`](#what-is-envdockersecret)
- [`app`](#app)
  - [`APP_NAME`](#app_name)
  - [`APP_DEBUG`](#app_debug)
  - [`APP_RELOAD`](#app_reload)
  - [`APP_CONTAINER_ADDRESS`](#app_container_address)
  - [`APP_CONTAINER_PORT`](#app_container_port)
  - [`APP_HOST_ADDRESS`](#app_host_address)
  - [`APP_HOST_PORT`](#app_host_port)
  - [`API_TOKEN`](#api_token)
  - [`ENABLE_INTERACTIONS`](#enable_interactions)
  - [`ENABLE_LEARNERS`](#enable_learners)
- [`postgres`](#postgres)
  - [`POSTGRES_DB`](#postgres_db)
  - [`POSTGRES_USER`](#postgres_user)
  - [`POSTGRES_PASSWORD`](#postgres_password)
  - [`POSTGRES_HOST_ADDRESS`](#postgres_host_address)
  - [`POSTGRES_HOST_PORT`](#postgres_host_port)
- [`pgadmin`](#pgadmin)
  - [`PGADMIN_EMAIL`](#pgadmin_email)
  - [`PGADMIN_PASSWORD`](#pgadmin_password)
  - [`PGADMIN_HOST_ADDRESS`](#pgadmin_host_address)
  - [`PGADMIN_HOST_PORT`](#pgadmin_host_port)
- [`caddy`](#caddy)
  - [`CADDY_CONTAINER_PORT`](#caddy_container_port)
  - [`CADDY_HOST_ADDRESS`](#caddy_host_address)
  - [`CADDY_HOST_PORT`](#caddy_host_port)

## What is `.env.docker.secret`

Default values: [`.env.docker.example`](../.env.docker.example)

<!-- TODO values are used for deployment using --env-file. replaces values in docker-compose.yml -->
<!-- TODO explain each variable -->
<!-- TODO add links to computer-networks#0000 for 0.0.0.0 
and links for 127.0.0.1 -->

## `app`

### `APP_NAME`

Default: `"Learning Management Service"`

### `APP_DEBUG`

Default: `false`

### `APP_RELOAD`

Default: `false`

### `APP_CONTAINER_ADDRESS`

Default: `0.0.0.0`

### `APP_CONTAINER_PORT`

Default: `8000`

### `APP_HOST_ADDRESS`

Default: `127.0.0.1`

### `APP_HOST_PORT`

Default: `42001`

### `API_TOKEN`

Default: `my-secret-api-key`

### `ENABLE_INTERACTIONS`

Feature flag

Default: `true`

### `ENABLE_LEARNERS`

Feature flag for enabling the `/learners` endpoint.

Default: `true`

## `postgres`

### `POSTGRES_DB`

Default: `lab-4`

### `POSTGRES_USER`

Default: `postgres`

### `POSTGRES_PASSWORD`

Default: `postgres`

### `POSTGRES_HOST_ADDRESS`

Default: `127.0.0.1`

### `POSTGRES_HOST_PORT`

Default: `42004`

## `pgadmin`

### `PGADMIN_EMAIL`

Default: `admin@example.com`

### `PGADMIN_PASSWORD`

Default: `admin`

### `PGADMIN_HOST_ADDRESS`

Default: `0.0.0.0`

### `PGADMIN_HOST_PORT`

Default: `42003`

## `caddy`

### `CADDY_CONTAINER_PORT`

Default: `80`

### `CADDY_HOST_ADDRESS`

Default: `0.0.0.0`

### `CADDY_HOST_PORT`

Default: `42002`
