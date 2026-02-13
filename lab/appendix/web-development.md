# Web development

- [Protocol](#protocol)
- [`HTTP`](#http)
  - [`HTTP` request](#http-request)
    - [Query parameter](#query-parameter)
  - [`HTTP` response](#http-response)
  - [`HTTP` response status code](#http-response-status-code)
  - [Common `HTTP` response status codes](#common-http-response-status-codes)
    - [`404` response status code](#404-response-status-code)
- [Client-server architecture](#client-server-architecture)
- [API](#api)
- [Endpoint](#endpoint)
- [Send a `GET` query](#send-a-get-query)
  - [Send a `GET` query using a browser](#send-a-get-query-using-a-browser)
  - [Send a `GET` query using curl](#send-a-get-query-using-curl)
- [Pretty-print the `JSON` response](#pretty-print-the-json-response)
- [Pretty-print the `JSON` response using `jq`](#pretty-print-the-json-response-using-jq)
  - [Pretty-print the `JSON` response using a browser](#pretty-print-the-json-response-using-a-browser)
- [URL](#url)
- [Service](#service)

## Protocol

## `HTTP`

### `HTTP` request

#### Query parameter

### `HTTP` response

### `HTTP` response status code

### Common `HTTP` response status codes

#### `404` response status code

## Client-server architecture

In client-server architecture:

- A **client** sends requests (browser, mobile app, `curl`).
- A **server** receives requests, runs logic, and returns responses.

```text
Client (browser/curl)
        |
        | HTTP request (e.g., GET /status)
        v
Service (server app)
        |
        | HTTP response (e.g., 200 + JSON)
        v
Client (renders or prints result)
```

Common response parts:

- Status code (`200`, `404`, `500`, etc.).
- Headers (metadata).
- Body (often `JSON` in APIs).

## API

## Endpoint

An endpoint is a specific API entry point identified by:

- HTTP method (`GET`, `POST`, `PUT`, `DELETE`, ...).
- Path (`/status`, `/items`, ...).

Example:

- `GET /status` is one endpoint.
- `POST /status` is a different endpoint.

Quick check with `curl`:

```terminal
curl http://127.0.0.1:42000/status
```

## Send a `GET` query

### Send a `GET` query using a browser

### Send a `GET` query using curl

## Pretty-print the `JSON` response

## Pretty-print the `JSON` response using `jq`

1. [Install `jq`](./linux.md#install-jq) if not installed.
2. [Run using the `VS Code Terminal`](./vs-code.md#run-a-command-using-the-vs-code-terminal):

   ```terminal
   <command-that-produces-json-response> | jq .
   ```

   [Pipe the output](./linux.md#pipe) to `jq`.

Example:

```terminal
curl -s https://jsonplaceholder.typicode.com/todos/1 | jq .
```

### Pretty-print the `JSON` response using a browser

`Chrome`:

1. click `Pretty-print`.

`Firefox`:

1. Click `Raw Data`
2. Clik `Pretty Print`

<!-- TODO other browsers -->

## URL

## Service

A service is an application (or part of a system) that exposes endpoints and performs a focused responsibility.

Examples:

- Course materials service.
- Authentication service.
- Recommendation service.

A service can call other services over the network, but to the client it still appears as endpoints that return responses.
