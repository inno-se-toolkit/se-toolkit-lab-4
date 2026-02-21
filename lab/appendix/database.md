# Database

<h2>Table of contents</h2>

- [What is a database](#what-is-a-database)
- [Database server](#database-server)
- [`PostgreSQL`](#postgresql)
- [`pgAdmin`](#pgadmin)
- [`SQL`](#sql)
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

## `SQL`

See [`SQL`](./sql.md).

## Database schema

The database schema defines the structure of the database: tables, columns, data types, and constraints.

You can [inspect columns](./pgadmin.md#inspect-columns) of a table in [`pgAdmin`](./pgadmin.md).

> [!NOTE]
> The column names in the database must match the field names in the `Python` code.
> If they don't match, the application will fail to read data from the database.

## Resetting the database

See [`Resetting the database`](./docker-postgres.md#resetting-the-database).
