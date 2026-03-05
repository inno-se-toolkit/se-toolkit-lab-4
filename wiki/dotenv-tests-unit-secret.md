# `.env.tests.unit.secret`

- [What is `.env.tests.unit.secret`](#what-is-envtestsunitsecret)
- [`NAME`](#name)
- [`DEBUG`](#debug)
- [`ADDRESS`](#address)
- [`PORT`](#port)
- [`RELOAD`](#reload)
- [`API_KEY`](#api_key)
- [`APP_ENABLE_INTERACTIONS`](#app_enable_interactions)
- [`APP_ENABLE_LEARNERS`](#app_enable_learners)
- [`DB_HOST`](#db_host)
- [`DB_PORT`](#db_port)
- [`DB_NAME`](#db_name)
- [`DB_USER`](#db_user)
- [`DB_PASSWORD`](#db_password)

## What is `.env.tests.unit.secret`

`.env.tests.unit.secret` is an [`.env` file](./environments.md#env-file) that stores [environment variables](./environments.md#environment-variable) for running [unit tests](./quality-assurance.md#unit-test).

Default values: [`.env.tests.unit.example`](../.env.tests.unit.example)

> It was added to [`.gitignore`](./git.md#gitignore) because it may contain [secrets](./environments.md#secrets).

## `NAME`

See [`APP_NAME`](./dotenv-docker-secret.md#app_name) in [`.env.docker.secret`](./dotenv-docker-secret.md#what-is-envdockersecret).

Default: `"Learning Management Service"`

## `DEBUG`

See [`APP_DEBUG`](./dotenv-docker-secret.md#app_debug) in `.env.docker.secret`.

Default: `false`

## `ADDRESS`

The [IP address](./computer-networks.md#ip-address) the app [listens on](./computer-networks.md#listen-on-a-port) during tests. [`127.0.0.1`](./computer-networks.md#127001) restricts access to the local machine only.

Default: `127.0.0.1`

## `PORT`

The [port number](./computer-networks.md#port-number) the app [listens on](./computer-networks.md#listen-on-a-port) during tests.

Default: `8000`

## `RELOAD`

See [`APP_RELOAD`](./dotenv-docker-secret.md#app_reload) in `.env.docker.secret`.

Default: `false`

## `API_KEY`

See [`API_KEY`](./dotenv-docker-secret.md#api_key) in `.env.docker.secret`.

Default: `test`

## `APP_ENABLE_INTERACTIONS`

See [`APP_ENABLE_INTERACTIONS`](./dotenv-docker-secret.md#app_enable_interactions) in `.env.docker.secret`.

Default: `true`

## `APP_ENABLE_LEARNERS`

See [`APP_ENABLE_LEARNERS`](./dotenv-docker-secret.md#app_enable_learners) in `.env.docker.secret`.

Default: `true`

## `DB_HOST`

The hostname of the [database](./database.md#what-is-a-database) used during tests.

Default: `localhost`

## `DB_PORT`

See [`POSTGRES_HOST_PORT`](./dotenv-docker-secret.md#postgres_host_port) in `.env.docker.secret`.

Default: `5432`

## `DB_NAME`

See [`POSTGRES_DB`](./dotenv-docker-secret.md#postgres_db) in `.env.docker.secret`.

Default: `test`

## `DB_USER`

See [`POSTGRES_USER`](./dotenv-docker-secret.md#postgres_user) in `.env.docker.secret`.

Default: `test`

## `DB_PASSWORD`

See [`POSTGRES_PASSWORD`](./dotenv-docker-secret.md#postgres_password) in `.env.docker.secret`.

Default: `test`
