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
- [Linting and formatting](#linting-and-formatting)
  - [Python tools](#python-tools)
  - [TypeScript tools](#typescript-tools)
  - [Markdown tools](#markdown-tools)
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

| Element | Style | Example |
| --- | --- | --- |
| File / module | `snake_case` | `interaction_logs.py` |
| Function / variable | `snake_case` | `read_learners` |
| Constant | `UPPER_SNAKE_CASE` | `DEFAULT_PAGE_SIZE` |
| Class | `PascalCase` | `LearnerCreate` |
| SQLModel table name | `snake_case` singular | `__tablename__ = "learner"` |
| Test file | `test_<module>.py` | `test_interactions.py` |
| Test function | `test_<behaviour>` | `test_filters_by_item_id` |

### TypeScript / React (`frontend/`)

| Element | Style | Example |
| --- | --- | --- |
| File — component | `PascalCase.tsx` | `App.tsx` |
| File — utility | `camelCase.ts` | `apiClient.ts` |
| Function / variable | `camelCase` | `setItems` |
| Constant | `UPPER_SNAKE_CASE` | `API_URL` |
| Component | `PascalCase` | `function App()` |
| CSS file | matches component | `App.css` |

### Environment variables

| Scope | Prefix | Example |
| --- | --- | --- |
| Backend | *(none)* | `APP_NAME`, `DATABASE_URL` |
| Frontend (Vite) | `VITE_` | `VITE_API_URL` |

### Markdown / config files

| Element | Style | Example |
| --- | --- | --- |
| Markdown file | `kebab-case.md` | `bug-report.md` |
| Directory | `kebab-case` | `conventions/` |
| Docker / Compose | lowercase | `docker-compose.yml` |
| Nix | lowercase | `flake.nix` |

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
- ty runs in parallel as a second opinion.

### TypeScript types

- All component props and API response shapes must have **explicit
  interfaces**.
- Use the `strict` compiler option — zero errors allowed.
- Prefer `interface` over `type` for object shapes.

## Linting and formatting

> Quality attribute: **Maintainability — Modifiability**
>
> Automated formatting removes style debates from code review and keeps
> diffs focused on logic.

### Python tools

| Tool | Purpose | Command |
| --- | --- | --- |
| Ruff (format) | Auto-formatter | `poe format` |
| Ruff (lint) | Linter | `poe lint` |
| Pyright | Type checker (strict) | `poe pyright-check` |
| ty | Type checker | `poe ty-check` |

### TypeScript tools

| Tool | Purpose | Command |
| --- | --- | --- |
| tsc | Type checker (strict, no emit) | `cd frontend && npx tsc --noEmit` |

### Markdown tools

| Tool | Purpose | Command |
| --- | --- | --- |
| markdownlint-cli2 | Markdown linter | `markdownlint-cli2` |

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

| Layer | What runs | When |
| --- | --- | --- |
| Editor | Ruff format + lint on save | Every save (VS Code) |
| Pre-run | `poe check` (format, lint, typecheck) | Before `poe dev` |
| Unit tests | `poe test` (pytest `tests/unit/`) | Before merging |
| E2E tests | `poe test-e2e` (pytest `tests/e2e/`) | Against deployed API |

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
- Reference `.env.example` / `.env.docker.example` for the expected
  variable names.
- Never hard-code API tokens or database passwords in source code.
