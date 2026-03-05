# `HTTP`

<h2>Table of contents</h2>

- [What is `HTTP`](#what-is-http)
- [Web server and web client](#web-server-and-web-client)
  - [Web server](#web-server)
  - [Web client](#web-client)
- [Communication using `HTTP`](#communication-using-http)
- [`HTTP` request](#http-request)
  - [`HTTP` request method](#http-request-method)
- [`HTTP` request header](#http-request-header)
  - [`HTTP` request payload](#http-request-payload)
  - [Query parameter](#query-parameter)
- [`HTTP` response](#http-response)
- [`HTTP` response status code](#http-response-status-code)
- [Common `HTTP` response status codes](#common-http-response-status-codes)
  - [`200` (OK)](#200-ok)
  - [`201` (Created)](#201-created)
  - [`400` (Bad Request)](#400-bad-request)
  - [`401` (Unauthorized)](#401-unauthorized)
  - [`403` (Forbidden)](#403-forbidden)
  - [`404` (Not Found)](#404-not-found)
  - [`422` (Unprocessable Entity)](#422-unprocessable-entity)
  - [`500` (Internal Server Error)](#500-internal-server-error)
- [Send a `GET` request](#send-a-get-request)
  - [Send a `GET` request using a browser](#send-a-get-request-using-a-browser)
  - [Send a `GET` request using `curl`](#send-a-get-request-using-curl)

## What is `HTTP`

`HTTP` (`HyperText Transfer Protocol`) is the foundation of data communication on the web. This [protocol](./computer-networks.md#protocol) defines how messages are formatted and transmitted between [web servers and web clients](#web-server-and-web-client).

## Web server and web client

<!-- TODO explain what web client and web server are outside of the HTTP context
-->

### Web server

A web server is software that delivers content or services to [web clients](#web-client) over a [network](./computer-networks.md#what-is-a-network) (e.g., [Internet](./computer-networks.md#internet)) using a [protocol](./computer-networks.md#protocol).

> [!NOTE]
> We refer to a web server as software only.
>
> Other sources may refer to it as hardware too.
>
> Example: [What is a web server](https://developer.mozilla.org/en-US/docs/Learn_web_development/Howto/Web_mechanics/What_is_a_web_server).

### Web client

A web client is software that requests content from a [web server](#web-server) and displays the received content.

Web clients include [browsers](./useful-programs.md#browser) ([`Chrome`](./useful-programs.md#chrome), [`Firefox`](./useful-programs.md#firefox)) and command-line tools ([`curl`](./useful-programs.md#curl)).

## Communication using `HTTP`

The following diagram illustrates the communication between a [web client](#web-client) and [web server](#web-server) using the `HTTP` protocol:

```mermaid
sequenceDiagram
    participant Client as Web Client (Browser/Curl)
    participant Server as Web Server

    Client->>Server: HTTP Request (GET, POST, etc.)
    activate Server
    Server-->>Client: HTTP Response (200 OK, 404, etc.)
    deactivate Server

    Note over Client,Server: Communication happens via HTTP protocol
```

## `HTTP` request

An `HTTP` request is a message sent by a client to a server asking for resources or to perform actions. It includes a method, headers, and optional body.

<!-- TODO image -->

<!-- https://www.cloud4y.ru/upload/medialibrary/4c0/hn5x5w7tx2pa0t3m1us71vh51dthf4kg/2.jpg -->

### `HTTP` request method

An `HTTP` method is a verb that tells the server what action to perform on a resource.

Common methods:

- `GET` — retrieve a resource.
- `POST` — create a new resource.
- `PUT` — update an existing resource.
- `DELETE` — remove a resource.

## `HTTP` request header

<!-- TODO -->

### `HTTP` request payload

<!-- TODO -->

### Query parameter

Query parameters are key-value pairs appended to a [URL](./computer-networks.md#url) after a `?` character, used to send data to the server with a request.

## `HTTP` response

An `HTTP` response is the server's answer to an `HTTP` request, containing status information and requested content.

## `HTTP` response status code

Status codes are three-digit numbers returned by servers indicating the result of a request (success, error, redirect, etc.).

## Common `HTTP` response status codes

### `200` (OK)

[`200` (OK)](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status/200) — the request succeeded.

### `201` (Created)

[`201` (Created)](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status/201) — a new resource was created (typically after `POST`).

### `400` (Bad Request)

[`400` (Bad Request)](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status/400) — the request was malformed.

### `401` (Unauthorized)

[`401` (Unauthorized)](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status/401) — authentication is required or the credentials are invalid.

### `403` (Forbidden)

[`403` (Forbidden)](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status/403) — the server understood the request but refuses to authorize it.

### `404` (Not Found)

[`404` (Not Found)](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status/404) — the requested resource does not exist.

### `422` (Unprocessable Entity)

[`422` (Unprocessable Entity)](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status/422) — the request was well-formed but had invalid data.

### `500` (Internal Server Error)

[`500` (Internal Server Error)](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status/500) — an unexpected server error occurred.

## Send a `GET` request

<!-- no toc -->
- Method 1: [Send a `GET` request using a browser](#send-a-get-request-using-a-browser)
- Method 2: [Send a `GET` request using `curl`](#send-a-get-request-using-curl)

### Send a `GET` request using a browser

1. Open the [URL](./computer-networks.md#url) in a browser.

   The browser sends the `GET` request by default.

### Send a `GET` request using `curl`

See [`curl`](./useful-programs.md#send-a-get-request-with-curl).
