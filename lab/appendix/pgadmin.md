# `pgAdmin`

<h2>Table of contents</h2>

- [What is `pgAdmin`](#what-is-pgadmin)
- [Open `pgAdmin`](#open-pgadmin)
- [Add a server in `pgAdmin`](#add-a-server-in-pgadmin)
- [Browse tables](#browse-tables)
- [Inspect columns](#inspect-columns)
- [Run a query](#run-a-query)

## What is `pgAdmin`

`pgAdmin` is a web-based graphical tool for managing `PostgreSQL` databases.

It lets you browse tables, run SQL queries, and inspect the database schema.

Docs:

- [Official PgAdmin docs](https://www.pgadmin.org/docs/)

## Open `pgAdmin`

1. Open <http://127.0.0.1:5050> in a browser.
2. Log in with the credentials from `.env.docker.secret`:
   - Email: the value of `PGADMIN_EMAIL` (default: `admin@example.com`).
   - Password: the value of `PGADMIN_PASSWORD` (default: `admin`).

## Add a server in `pgAdmin`

1. [Open `pgAdmin`](#open-pgadmin).
2. Right-click `Servers` in the left panel.
3. Click `Register` -> `Server...`.
4. In the `General` tab:
   - Name: `lab3`.
5. In the `Connection` tab:
   - Host name/address: `postgres`.
   - Port: `5432`.
   - Maintenance database: the value of `POSTGRES_DB` (default: `lab3`).
   - Username: the value of `POSTGRES_USER` (default: `postgres`).
   - Password: the value of `POSTGRES_PASSWORD` (default: `postgres`).
6. Click `Save`.

> [!IMPORTANT]
> The host name is `postgres`, not `localhost`.
> This is because `pgAdmin` and `PostgreSQL` run in separate `Docker` containers.
> `Docker Compose` creates a network where services can reach each other by their service name.

## Browse tables

1. [Add a server](#add-a-server-in-pgadmin) if you haven't already.
2. Expand: `Servers` -> `lab3` -> `Databases` -> `lab3` -> `Schemas` -> `public` -> `Tables`.
3. Right-click a table -> `View/Edit Data` -> `All Rows`.

## Inspect columns

1. [Add a server](#add-a-server-in-pgadmin) if you haven't already.
2. Expand: `Servers` -> `lab3` -> `Databases` -> `lab3` -> `Schemas` -> `public` -> `Tables`.
3. Right-click a table -> `Properties` -> `Columns`.

## Run a query

1. [Add a server](#add-a-server-in-pgadmin) if you haven't already.
2. Right-click the `lab3` database.
3. Click `Query Tool`.
4. Write your SQL query, e.g.:

   ```sql
   SELECT * FROM interaction_logs WHERE item_id = 2;
   ```

5. Click `Execute Script` (or press `F5`).
