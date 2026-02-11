# Web development

- [Client-server architecture](#client-server-architecture)
- [Endpoint](#endpoint)
- [Service](#service)

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

## Service

A service is an application (or part of a system) that exposes endpoints and performs a focused responsibility.

Examples:

- Course materials service.
- Authentication service.
- Recommendation service.

A service can call other services over the network, but to the client it still appears as endpoints that return responses.
