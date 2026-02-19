# Database

<h2>Table of contents</h2>

- [What is a database](#what-is-a-database)
- [Database server](#database-server)
- [`PostgreSQL`](#postgresql)
- [`pgAdmin`](#pgadmin)
- [SQL basics](#sql-basics)
  - [`SELECT`](#select)
  - [`INSERT`](#insert)
  - [`WHERE`](#where)
- [Database schema](#database-schema)
- [Resetting the database](#resetting-the-database)

## What is a database

A database is an organized collection of data that can be accessed, managed, and updated.

Databases store data in structures such as tables (rows and columns).

## Database server

A database server is software that manages one or more databases and handles queries from clients (applications).

Examples of database servers: `PostgreSQL`, `MySQL`, `SQLite`.

## `PostgreSQL`

`PostgreSQL` is a popular open-source relational database server.

Docs:

- [Official PostgreSQL docs](https://www.postgresql.org/docs/)

## `pgAdmin`

See [`pgAdmin`](./pgadmin.md).

## SQL basics

### `SELECT`

Retrieve data from a table:

```sql
SELECT * FROM items;
```

Retrieve specific columns:

```sql
SELECT title, description FROM items;
```

### `INSERT`

Add a new row to a table:

```sql
INSERT INTO items (title, description) VALUES ('New Item', 'A description.');
```

### `WHERE`

Filter rows by a condition:

```sql
SELECT * FROM learners WHERE enrolled_at >= '2025-10-01';
```

## Database schema

The database schema defines the structure of the database: tables, columns, data types, and constraints.

You can [inspect columns](./pgadmin.md#inspect-columns) of a table in [`pgAdmin`](./pgadmin.md).

> [!NOTE]
> The column names in the database must match the field names in the `Python` code.
> If they don't match, the application will fail to read data from the database.

## Resetting the database

The database is initialized from the file `src/app/data/init.sql` on the first start of the `PostgreSQL` container.

To reset the database to its initial state:

1. [Run using the `VS Code Terminal`](./vs-code.md#run-a-command-using-the-vs-code-terminal):

   ```terminal
   docker compose --env-file .env.docker.secret down -v
   ```

2. This removes the database volume. The next `docker compose up` will re-create the database from `init.sql`.

3. Start the services again:

   ```terminal
   docker compose --env-file .env.docker.secret up --build
   ```
