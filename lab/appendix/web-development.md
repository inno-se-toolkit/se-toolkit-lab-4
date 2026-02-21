# Web development

<h2>Table of contents</h2>

- [Web server and web client](#web-server-and-web-client)
  - [Web server](#web-server)
  - [Web client](#web-client)
- [Protocol](#protocol)
- [Data format](#data-format)
  - [`JSON`](#json)
    - [`JSON` data types](#json-data-types)
    - [Example of `JSON` data](#example-of-json-data)
  - [`Protobuf`](#protobuf)
- [REST API](#rest-api)
- [API](#api)
  - [`<api-token>`](#api-token)
- [`Swagger UI`](#swagger-ui)
  - [Open `Swagger UI`](#open-swagger-ui)
  - [Authorize in `Swagger UI`](#authorize-in-swagger-ui)
  - [Try an endpoint in `Swagger UI`](#try-an-endpoint-in-swagger-ui)
- [Endpoint](#endpoint)
- [Send a `GET` request](#send-a-get-request)
  - [Send a `GET` request using a browser](#send-a-get-request-using-a-browser)
  - [Send a `GET` request using `curl`](#send-a-get-request-using-curl)
- [Pretty-print the `JSON` response](#pretty-print-the-json-response)
  - [Pretty-print the `JSON` response using `jq`](#pretty-print-the-json-response-using-jq)
  - [Pretty-print the `JSON` response using a browser](#pretty-print-the-json-response-using-a-browser)
- [URL](#url)
  - [Purpose](#purpose)
  - [Components of a URL](#components-of-a-url)
  - [URL example](#url-example)
- [Service](#service)
- [Feature flag](#feature-flag)

## Web server and web client

### Web server

A web server is software that delivers content or services to [web clients](#web-client) over the [Internet](./computer-networks.md#internet) using a [protocol](#protocol).

> [!NOTE]
> We refer to a web server as software only.
>
> Other sources may refer to it as hardware too.
>
> Example: [What is a web server](https://developer.mozilla.org/en-US/docs/Learn_web_development/Howto/Web_mechanics/What_is_a_web_server).

### Web client

A web client is software that requests content from a [web server](#web-server) and displays the received content.

Web clients include browsers (`Chrome`, `Firefox`) and command-line tools ([`curl`](#send-a-get-request-using-curl)).

## Protocol

A protocol is a set of rules that define how data is transmitted and received over a network. In web development, protocols govern communication between [web servers and web clients](#web-server-and-web-client).

## Data format

### `JSON`

`JSON` (`JavaScript Object Notation`) is a lightweight, text-based data interchange format that is easy for humans to read and write, and easy for machines to parse and generate.

It is language-independent but derived from `JavaScript` and commonly used in web applications to transmit data between a [server and a client](#web-server-and-web-client).

See [Learn `JSON` in Y minutes](https://learnxinyminutes.com/json/).

#### `JSON` data types

`JSON` supports basic data types like strings, numbers, booleans, arrays, and objects, making it ideal for representing structured data. Its simplicity and compatibility with most programming languages have made it the de facto standard for API responses and configuration files.

#### Example of `JSON` data

```json
{
  "name": "John Doe",
  "age": 35,
  "active": true,
  "skills": ["Python", "JavaScript", "Go"]
}
```

### `Protobuf`

`Protobuf` (`Protocol Buffers`) is a binary serialization format developed by `Google` for structured data exchange between applications. It's a language-neutral, platform-neutral mechanism for serializing structured data, similar to `XML` or `JSON` but more compact and faster.

`Protobuf` uses `.proto` files to define data structures, which are then compiled into language-specific classes for various programming languages. It's commonly used in microservices architectures and API communications where efficiency and schema evolution are important.

## REST API

A REST API (`Representational State Transfer`) is a style of API design that uses `HTTP` methods and noun-based resource paths.

Key principles:

- **Resources** are identified by paths: `/items`, `/learners`, `/interactions`.
- **`HTTP` methods** define the action:
  - `GET` — read a resource.
  - `POST` — create a new resource.
  - `PUT` — update an existing resource.
  - `DELETE` — remove a resource.
- **Status codes** indicate the result: `200`, `201`, `404`, etc.

Example:

| Action               | Method | Path           | Status code |
| -------------------- | ------ | -------------- | ----------- |
| List all items       | `GET`  | `/items`       | `200`       |
| Get one item         | `GET`  | `/items/{id}`  | `200`/`404` |
| Create an item       | `POST` | `/items`       | `201`       |
| Update an item       | `PUT`  | `/items/{id}`  | `200`/`404` |

## API

An API (`Application Programming Interface`) is a set of rules that lets programs communicate with each other.

A web API exposes [endpoints](#endpoint) that clients can call over `HTTP`.

Docs:

- [An introduction to APIs: A comprehensive guide](https://zapier.com/blog/api/)

### `<api-token>`

The value that you use to authenticate in the API.

## `Swagger UI`

`Swagger UI` is an interactive web page that lets you explore and test a REST API.

`FastAPI` auto-generates `Swagger UI` at the `/docs` path.

Actions:

- [Open `Swagger UI`](#open-swagger-ui)
- [Authorize in `Swagger UI`](#authorize-in-swagger-ui)
- [Try an endpoint in `Swagger UI`](#try-an-endpoint-in-swagger-ui)

### Open `Swagger UI`

1. Open <http://127.0.0.1:42001/docs> in a browser.

### Authorize in `Swagger UI`

If the API requires authentication:

1. [Open `Swagger UI`](#open-swagger-ui).
2. Click the `Authorize` button (lock icon at the top right).
3. In the `Value` field, enter the [`<api-token>`](#api-token).
4. Click `Authorize`.
5. Click `Close`.

All subsequent requests will include the API key in the `Authorization` header.

### Try an endpoint in `Swagger UI`

1. [Open `Swagger UI`](#open-swagger-ui).
2. Click on an endpoint (e.g., `GET /items`).
3. Click `Try it out`.
4. Fill in parameters if needed.
5. Click `Execute`.
6. See the response below: status code, response body, headers.

## Endpoint

An endpoint is a specific [API](#api) entry point identified by:

- HTTP method (`GET`, `POST`, `PUT`, `DELETE`, ...).
- Path (`/status`, `/items`, ...).

Example:

- `GET /status` is one endpoint.
- `POST /status` is a different endpoint.

## Send a `GET` request

### Send a `GET` request using a browser

1. Open the URL in a browser.

   The browser will send the `GET` query by default.

### Send a `GET` request using `curl`

See [`curl`](./useful-programs.md#send-a-get-request-with-curl).

## Pretty-print the `JSON` response

### Pretty-print the `JSON` response using `jq`

1. [Install `jq`](./useful-programs.md#jq) if not installed.
2. [Run using the `VS Code Terminal`](./vs-code.md#run-a-command-using-the-vs-code-terminal):

   ```terminal
   <command-that-produces-json-response> | jq .
   ```

   [Pipe the output](./bash.md#pipe-the-stdout) to `jq`.

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

A URL (`Uniform Resource Locator`) is a reference or address used to identify and locate resources on the Internet. It's commonly known as a "web address" and specifies the location of a resource on a web server as well as the protocol used to access it.

### Purpose

URLs are used by web browsers and other applications to retrieve resources like web pages, images, videos, and API endpoints. They provide a standardized way to locate and access resources across the Internet.

### Components of a URL

A typical URL consists of several components:

- **Scheme/Protocol**: Specifies how to access the resource (e.g., `http`, `https`, `ftp`).
- **Host/Domain**: The server where the resource is located (e.g., `www.example.com`).
- **Port** (optional): The specific port number on the server (e.g., `:8080`).
- **Path**: The location of the specific resource on the server (e.g., `/folder/page.html`).
- **Query parameters** (optional): Additional data passed to the server (e.g., `?param1=value1&param2=value2`).
- **Fragment** (optional): Points to a specific section within the resource (e.g., `#section1`).

### URL example

```text
https://www.example.com:8080/search?q=cats&page=1#results
```

Where:

- Scheme: `https`
- Host: `www.example.com`
- Port: `8080`
- Path: `/search`
- Query: `?q=cats&page=1`
- Fragment: `#results`

## Service

A service is an application (or part of a system) that exposes endpoints and performs a focused responsibility.

Examples:

- Course materials service.
- Authentication service.
- Recommendation service.

A service can call other services over the network, but to the client it still appears as endpoints that return responses.

## Feature flag
