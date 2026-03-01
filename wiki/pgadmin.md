# `pgAdmin`

<h2>Table of contents</h2>

- [What is `pgAdmin`](#what-is-pgadmin)
- [`<pgadmin-port>`](#pgadmin-port)
- [Open `pgAdmin`](#open-pgadmin)
- [Connect to a `PostgreSQL` server](#connect-to-a-postgresql-server)
- [Open the database](#open-the-database)
- [Open tables in the database](#open-tables-in-the-database)
- [Browse the table](#browse-the-table)
- [Inspect columns in the table](#inspect-columns-in-the-table)
- [Run a query](#run-a-query)
- [Copy the data output](#copy-the-data-output)
- [Get the ER diagram](#get-the-er-diagram)

## What is `pgAdmin`

`pgAdmin` is a web-based graphical tool for managing `PostgreSQL` databases.

It lets you:

<!-- no toc -->
- [connect to a `PostgreSQL` server](#connect-to-a-postgresql-server);
- [open a database](#open-the-database) on that server;
- inspect the [database schema](./database.md#database-schema);
- [browse tables](#browse-the-table) in that database;
- run [`SQL` queries](./sql.md#sql-query) against that database.

Docs:

- [Official PgAdmin docs](https://www.pgadmin.org/docs/)

## `<pgadmin-port>`

The value of [`PGADMIN_HOST_PORT` in `.env.docker.secret`](./dotenv-docker-secret.md#pgadmin_host_port) that you used to run the `pgadmin` [service](./docker.md#service).

## Open `pgAdmin`

> [!NOTE]
> The default values are defined in [`.env.docker.example`](../.env.docker.example).
>
> The actual values are in `.env.docker.secret`.

1. Open `http://<address>:<pgadmin-port>` in a browser. Replace:
   - `<address>` with:
     - [`localhost`](./computer-networks.md#localhost) if you deployed on your local machine.
     - [`<your-vm-ip-address>`](vm.md#your-vm-ip-address) if you deployed on [your VM](./vm.md#your-vm);
   - [`<pgadmin-port>`](#pgadmin-port).
2. Log in with the credentials from `.env.docker.secret`:
   - `Email`: the value of `PGADMIN_EMAIL` (default: `admin@example.com`).
   - `Password`: the value of `PGADMIN_PASSWORD` (default: `admin`).

<!-- TODO servers.json -->

## Connect to a `PostgreSQL` server

> [!NOTE]
> The environment variables are defined in the [`.env.docker.secret`](./dotenv-docker-secret.md#what-is-envdockersecret) file that you used to deploy the [`pgadmin` service](./docker-compose-yml.md#pgadmin-service).

1. [Open `pgAdmin`](#open-pgadmin).
2. Right-click `Servers` in the left panel.
3. Click `Register` -> `Server...`.
4. In the `General` tab:
   - `Name`: the value of [`POSTGRES_SERVER_NAME`](./dotenv-docker-secret.md#postgres_server_name).
5. In the `Connection` tab:
   - `Host name/address`: the value of the [`PostgreSQL` service name](./constants.md#postgresql-service-name) (see [`Docker Compose` networking](./docker-compose.md#networking)).
   - `Port`: The value of the [default `PostgreSQL` port](./constants.md#default-postgresql-port).
   - `Maintenance database`: the value of [`POSTGRES_SERVER_NAME`](./dotenv-docker-secret.md#postgres_server_name).
   - `Username`: the value of [`POSTGRES_USER`](./dotenv-docker-secret.md#postgres_user).
   - `Password`: the value of [`POSTGRES_PASSWORD`](./dotenv-docker-secret.md#postgres_password).
6. Click `Save`.

> [!IMPORTANT]
> The host name is `postgres`, not `localhost`.
> This is because `pgAdmin` and `PostgreSQL` run in separate `Docker` containers.
> `Docker Compose` creates a network where services can reach each other by their service name.

## Open the database

> [!NOTE]
> The `<db-name>` is the name of the database which you want to open.

1. Expand `Servers`.
2. Expand `<server-name>`.
3. Expand `Databases`.
4. Expand `<db-name>`.

## Open tables in the database

> [!NOTE]
> The `<db-name>` is the name of the database where you want to open tables.

1. [Open the database `<db-name>`](#open-the-database).
2. Expand `Schemas`.
3. Expand `public`.
4. Expand `Tables`.

## Browse the table

> [!NOTE]
> The `<db-name>` is the name of the database where you want to browse tables.
>
> The `<table-name>` is the name of the table that you want to inspect.

1. [Open tables in the database `<db-name>`](#open-tables-in-the-database).
2. Right-click `<table-name>`.
3. Click `View/Edit Data`.
4. Click `All Rows`.

## Inspect columns in the table

> [!NOTE]
> The `<db-name>` is the name of the database where you want to inspect columns in the table `<table-name>`.
>
> The `<table-name>` is the name of the table where you want to inspect columns.

1. [Open tables in the database `<db-name>`](#open-tables-in-the-database).
2. Right-click `<table-name>`.
3. Click `Properties`.
4. Click `Columns`.

## Run a query

> [!NOTE]
> The `<db-name>` is the name of the database where you want to run a query.

1. [Open the database `<db-name>`](#open-the-database).
2. Right-click `<db-name>`.
3. Click `Query Tool`.
4. Write your [`SQL`](./sql.md) query, e.g.:

   ```sql
   SELECT tablename FROM pg_tables WHERE schemaname = 'public';
   ```

5. Click `Execute Script`.

   <img alt="Execute script" src="./images/pgadmin/execute-script.png" style="width:300px">

   In the `Data Output` tab, you should see a table with the data returned by the query:

   <img alt="Query data output tab" src="./images/pgadmin/query-data-output-tab.png" style="width:300px">

   In the `Messages` tab, you should see the text report about your query.

   <img alt="Query messages tab" src="./images/pgadmin/query-messages-tab.png" style="width:300px">

## Copy the data output

1. [Run a query](#run-a-query).
2. Open the `Data Output` tab.
3. Click the upper-left corner in the `Data Output` tab to select the full table.

   <img alt="Data Output - select all" src="./images/pgadmin/data-output-select-all.png" style="width:400px">
4. Click `Copy` to copy the full table to the clipboard.

   <img alt="Data Output - select all" src="./images/pgadmin/data-output-copy.png" style="width:400px">

