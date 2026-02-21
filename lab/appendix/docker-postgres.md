# `PostgreSQL` with `Docker`

<h2>Table of contents</h2>

- [What is `PostgreSQL` with `Docker`](#what-is-postgresql-with-docker)
- [Resetting the database](#resetting-the-database)

## What is `PostgreSQL` with `Docker`

This appendix covers managing the `PostgreSQL` [container](./docker.md#container) in this project.

See also:

- [`Database`](./database.md) for database concepts.
- [`Docker Compose`](./docker-compose.md) for general `Docker Compose` commands.

## Resetting the database

The database is initialized from the file [`src/app/data/init.sql`](../../src/app/data/init.sql) on the first start of the container with `PostgreSQL` (see the [service](./docker.md#service) `postgres` in [`docker-compose.yml`](../../docker-compose.yml)).

To reset the database to its initial state:

1. [Run using the `VS Code Terminal`](./vs-code.md#run-a-command-using-the-vs-code-terminal):

   ```terminal
   docker compose --env-file .env.docker.secret down postgres -v
   ```

2. This removes the database [volume](./docker.md#volumes). The next `docker compose up` will re-create the database from [`init.sql`](../../src/app/data/init.sql).

3. Start the services again:

   ```terminal
   docker compose --env-file .env.docker.secret up postgres --build
   ```
