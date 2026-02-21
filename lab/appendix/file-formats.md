# File formats

<h2>Table of contents</h2>

- [What is a file format?](#what-is-a-file-format)
- [Common file formats](#common-file-formats)
  - [`Markdown`](#markdown)
    - [`Markdown` docs](#markdown-docs)
    - [`Markdown` in this project](#markdown-in-this-project)
  - [`JSON`](#json)
    - [`JSON` docs](#json-docs)
    - [`JSON` example](#json-example)
    - [`JSON` in this project](#json-in-this-project)
  - [`TOML`](#toml)
    - [`TOML` docs](#toml-docs)
    - [`TOML` example](#toml-example)
    - [`TOML` in this project](#toml-in-this-project)
  - [`YAML`](#yaml)
    - [`YAML` docs](#yaml-docs)
    - [`YAML` example](#yaml-example)
    - [`YAML` in this project](#yaml-in-this-project)
  - [`.env`](#env)
    - [`.env` docs](#env-docs)
    - [`.env` example](#env-example)
    - [`.env` in this project](#env-in-this-project)
  - [`Python`](#python)
    - [`Python` docs](#python-docs)
    - [`Python` example](#python-example)
    - [`Python` in this project](#python-in-this-project)

## What is a file format?

A file format defines how data is structured and stored in a [file](./file-system.md#file).

The [file extension](./file-system.md#extension) (e.g., [`.json`](#json), [`.toml`](#toml), [`.py`](#python)) indicates the format and tells editors and tools how to read the file.

## Common file formats

### `Markdown`

`Markdown` is a [markup language](https://en.wikipedia.org/wiki/Markup_language).

`Markdown` gets translated into [`HTML`](https://en.wikipedia.org/wiki/HTML).

You see the rendered `HTML` when you [open the `Markdown` preview](./vs-code.md#open-the-markdown-preview) in `VS Code` or view a `Markdown` file on [`GitHub`](./github.md).

#### `Markdown` docs

- [Learn Markdown in Y minutes](https://learnxinyminutes.com/docs/markdown/)

#### `Markdown` in this project

- [`lab/appendix/file-formats.md`](./file-formats.md) — this file.
- [`README.md`](../../README.md) — project overview.
- [`.github/pull_request_template.md`](../../.github/pull_request_template.md) — [`GitHub` pull request](./github.md#pull-request) template.

### `JSON`

`JSON` (JavaScript Object Notation) is a human-readable text format for structured data.

#### `JSON` docs

- [JSON.org](https://www.json.org/)
- [Learn JSON in Y minutes](https://learnxinyminutes.com/docs/json/)

#### `JSON` example

```json
{
  "id": 1,
  "title": "Introduction to Python",
  "published": true
}
```

#### `JSON` in this project

- [`.vscode/settings.json`](../../.vscode/settings.json) — `VS Code` editor settings.
- [`HTTP`](./http.md) request and response bodies when calling the `API`.

### `TOML`

`TOML` (Tom's Obvious, Minimal Language) is a configuration file format designed to be minimal and easy to read.

#### `TOML` docs

- [TOML documentation](https://toml.io/)
- [Learn TOML in Y minutes](https://learnxinyminutes.com/docs/toml/)

#### `TOML` example

```toml
[project]
name = "my-app"
version = "1.0.0"

[server]
host = "localhost"
port = 8080
```

#### `TOML` in this project

[`pyproject.toml`](../../pyproject.toml) — the [`Python`](./python.md) project configuration file.

### `YAML`

`YAML` (YAML Ain't Markup Language) is a human-readable data serialization format commonly used for configuration files.

#### `YAML` docs

- [YAML specification](https://yaml.org/)
- [Learn YAML in Y minutes](https://learnxinyminutes.com/docs/yaml/)

#### `YAML` example

```yaml
name: my-app
version: "1.0.0"

server:
  host: localhost
  port: 8080
```

#### `YAML` in this project

- [`.github/workflows/`](../../.github/workflows/) — [`GitHub Actions`](./github.md) workflow files.
- [`docker-compose.yml`](../../docker-compose.yml) — [`Docker Compose`](./docker-compose.md) service definitions.

### `.env`

`.env` files store [environment variables](./environments.md) as key-value pairs, one per line.

#### `.env` docs

- [Dotenv File Format](https://hexdocs.pm/dotenvy/dotenv-file-format.html)

#### `.env` example

```shell
DEBUG=false
PORT=8080
SECRET_KEY=changeme
```

#### `.env` in this project

Used for local and [`Docker`](./docker.md) environment configuration.

### `Python`

`.py` files contain [`Python`](./python.md) source code.

#### `Python` docs

- [Learn Python in Y minutes](https://learnxinyminutes.com/docs/python/)

#### `Python` example

```python
def greet(name: str) -> str:
    return f"Hello, {name}!"
```

#### `Python` in this project

Used for the application code and tests.
