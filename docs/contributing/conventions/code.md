# Code conventions

This document defines the coding conventions for the project. Each
convention is mapped to an
[ISO 25010](https://iso25000.com/index.php/en/iso-25000-standards/iso-25010)
quality attribute so the reasoning behind every rule is explicit.

- [Naming](#naming)
  - [Python (`backend/`)](#python-backend)
  - [TypeScript / React (`frontend/`)](#typescript--react-frontend)
  - [Environment variables](#environment-variables)
  - [Markdown / config files](#markdown--config-files)
- [Comments and docstrings](#comments-and-docstrings)
  - [Python comments](#python-comments)
  - [TypeScript comments](#typescript-comments)
  - [TODO comments](#todo-comments)
- [Type safety](#type-safety)
  - [Python types](#python-types)
  - [TypeScript types](#typescript-types)
- [API calls](#api-calls)
  - [Frontend fetch URLs](#frontend-fetch-urls)
- [Linting and formatting](#linting-and-formatting)
  - [Python tools](#python-tools)
    - [`Ruff` (format)](#ruff-format)
    - [`Ruff` (lint)](#ruff-lint)
    - [`Pyright`](#pyright)
    - [`ty`](#ty)
  - [TypeScript tools](#typescript-tools)
    - [`ESLint`](#eslint)
    - [`tsc`](#tsc)
  - [Markdown tools](#markdown-tools)
    - [`markdownlint-cli2`](#markdownlint-cli2)
  - [Run everything at once](#run-everything-at-once)
- [Shift-left testing](#shift-left-testing)
  - [Writing tests](#writing-tests)
- [Security](#security)

## Naming

> Quality attribute: **Maintainability — Modifiability**
>
> Consistent naming lets any contributor find and change code without
> guessing at conventions.

### Python (`backend/`)

- **File / module** — `snake_case` — e.g., `interaction_logs.py`
- **Function / variable** — `snake_case` — e.g., `read_learners`
- **Constant** — `UPPER_SNAKE_CASE` — e.g., `DEFAULT_PAGE_SIZE`
- **Class** — `PascalCase` — e.g., `LearnerCreate`
- **SQLModel table name** — `snake_case` singular — e.g., `__tablename__ = "learner"`
- **Test file** — `test_<module>.py` — e.g., `test_interactions.py`
- **Test function** — `test_<behaviour>` — e.g., `test_filters_by_item_id`

### TypeScript / React (`frontend/`)

- **File — component** — `PascalCase.tsx` — e.g., `App.tsx`
- **File — utility** — `camelCase.ts` — e.g., `apiClient.ts`
- **Function / variable** — `camelCase` — e.g., `setItems`
- **Constant** — `UPPER_SNAKE_CASE` — e.g., `API_URL`
- **Component** — `PascalCase` — e.g., `function App()`
- **CSS file** — matches component — e.g., `App.css`

### Environment variables

- **Backend** — no prefix — e.g., `APP_NAME`, `DATABASE_URL`
- **Frontend (`Vite`)** — `VITE_` prefix — e.g., `VITE_API_URL`

### Markdown / config files

- **Markdown file** — `kebab-case.md` — e.g., `bug-report.md`
- **Directory** — `kebab-case` — e.g., `conventions/`
- **Docker / Compose** — lowercase — e.g., `docker-compose.yml`
- **Nix** — lowercase — e.g., `flake.nix`

## Comments and docstrings

> Quality attribute: **Maintainability — Analysability**
>
> Comments explain *why*, not *what*. Enough context for a newcomer to
> understand intent without asking the author.

### Python comments

- Every module starts with a one-line docstring:
  `"""Router for learner endpoints."""`
- Every public class and function has a docstring.
- Use inline comments only when the logic is non-obvious.

### TypeScript comments

- Use `//` comments for non-obvious logic.
- No JSDoc is required for small components; add it when a function
  signature is not self-explanatory.

### TODO comments

Mark unfinished work with `TODO` so it can be found by search:

```python
# TODO: add pagination support
```

## Type safety

> Quality attribute: **Functional Suitability — Functional Correctness**
>
> Catching type errors at write-time is cheaper than catching them at
> run-time.

### Python types

- All function signatures must have **full type annotations** (params
  and return type).
- Use `X | None` union syntax, not `Optional[X]`.
- Pyright runs in **strict** mode — zero errors allowed.
- ty runs as a second opinion.

### TypeScript types

- All component props and API response shapes must have **explicit
  interfaces**.
- Use the `strict` compiler option — zero errors allowed.
- Prefer `interface` over `type` for object shapes.

## API calls

> Quality attribute: **Functional Suitability — Functional Correctness**
>
> Consistent URL formatting prevents routing mismatches between the
> frontend and the FastAPI backend.

### Frontend fetch URLs

- Always end API path strings with a trailing slash — e.g., `/items/`,
  not `/items`.
- FastAPI redirects requests without a trailing slash, which can cause
  `fetch` to silently lose the request body or method.

## Linting and formatting

> Quality attribute: **Maintainability — Modifiability**
>
> Automated formatting removes style debates from code review and keeps
> diffs focused on logic.

### Python tools

#### `Ruff` (format)

Auto-formatter: `poe format`

#### `Ruff` (lint)

Linter: `poe lint`

#### `Pyright`

Type checker (strict): `poe pyright-check`

#### `ty`

Type checker: `poe ty-check`

### TypeScript tools

#### `ESLint`

Linter: `cd frontend && npm run lint`

#### `tsc`

Type checker (strict, no emit): `cd frontend && npx tsc --noEmit`

### Markdown tools

#### `markdownlint-cli2`

Markdown linter: `markdownlint-cli2`

### Run everything at once

```sh
poe check          # format → lint → typecheck
poe dev            # check + run server
```

## Shift-left testing

> Quality attribute: **Functional Suitability — Functional Correctness**,
> **Reliability — Maturity**
>
> Catch defects as early in the pipeline as possible: editor → commit →
> CI.

- **Editor** — Ruff format + lint on save — every save (`VS Code`)
- **Pre-run** — `poe check` (format, lint, typecheck) — before `poe dev`
- **Unit tests** — `poe test` (pytest `tests/unit/`) — before merging
- **E2E tests** — `poe test-e2e` (pytest `tests/e2e/`) — against deployed API

### Writing tests

- Place unit tests in `tests/unit/`, E2E tests in `tests/e2e/`.
- Name test files `test_<module>.py`.
- One assertion per test when possible; name the test after the
  expected behaviour.

## Security

> Quality attribute: **Security — Confidentiality**
>
> Secrets never enter version control.

- Store secrets in `.env` files. These files are git-ignored.
- Reference `.env.docker.example` for the expected variable names.
- Never hard-code API keys, API tokens, or database passwords in source code.
