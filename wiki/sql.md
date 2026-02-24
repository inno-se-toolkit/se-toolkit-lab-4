# `SQL`

<h2>Table of contents</h2>

- [What is `SQL`](#what-is-sql)
- [`SELECT`](#select)
- [`INSERT`](#insert)
- [`WHERE`](#where)

## What is `SQL`

`SQL` (Structured Query Language) is the standard language for interacting with relational databases such as [`PostgreSQL`](./database.md#postgresql).

Docs:

- [PostgreSQL SQL syntax](https://www.postgresql.org/docs/current/sql.html)

## `SELECT`

Retrieve data from a table:

```sql
SELECT * FROM items;
```

Retrieve specific columns:

```sql
SELECT title, description FROM items;
```

## `INSERT`

Add a new row to a table:

```sql
INSERT INTO items (title, description) VALUES ('New Item', 'A description.');
```

## `WHERE`

Filter rows by a condition:

```sql
SELECT * FROM learners WHERE enrolled_at >= '2025-10-01';
```
