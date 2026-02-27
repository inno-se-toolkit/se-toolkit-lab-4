# Commit conventions

This project follows [Conventional Commits](https://www.conventionalcommits.org/).

## Format

```text
type(scope): subject

Optional body — use when additional context helps reviewers understand
why the change was made. Write in imperative mood. Wrap at 72 characters.
If the body covers 2+ points, use a bullet list.
```

## Types

| Type | Use when... |
| --- | --- |
| `feat` | Adding new content or a new feature |
| `fix` | Correcting a bug or improving existing behaviour |
| `docs` | Documentation-only changes |
| `refactor` | Code restructuring with no behaviour change |
| `test` | Adding or updating tests |
| `chore` | Maintenance tasks (deps, CI, tooling) |

## Scopes

Every commit must include a scope. Use the scope that best matches the
area of change:

`wiki` | `instructors` | `docs` | `readme` | `caddy` | `lab` |
`frontend` | `backend` | `tests` | `vscode` | `git` | `github` |
`claude` | `nix` | `docker` | `database` | `contributors` | `markdownlint`

### Scope mapping

| Scope | Covers |
| --- | --- |
| `wiki` | `wiki/` pages |
| `instructors` | `instructors/` (internal design notes) |
| `docs` | `docs/` (architecture, contributing, etc.) |
| `readme` | Root `README.md` |
| `caddy` | `caddy/` config and reverse-proxy setup |
| `lab` | `lab/` (task sheets, setup guide) |
| `frontend` | `frontend/` |
| `backend` | `backend/`, `pyproject.toml`, backend config |
| `vscode` | `.vscode/` settings and extensions |
| `git` | `.gitignore`, `.gitmodules`, git config |
| `github` | `.github/` (workflows, issue templates, PR templates) |
| `claude` | `.claude/` (skills, settings) |
| `nix` | `flake.nix`, `flake.lock`, Nix-related config |
| `docker` | `Dockerfile`, `compose.yaml`, Docker-related config |
| `database` | `.sql` files, migrations, schema |
| `contributors` | `CONTRIBUTORS.md` |
| `markdownlint` | `.markdownlint*` config |

## Subject line

- Lowercase, imperative mood, no period at the end
- Under 72 characters
- Example: `feat(wiki): add Docker troubleshooting page`

## Body

- Optional — add one when the subject alone doesn't fully explain the
  change (e.g. non-obvious decisions, side effects, grouped changes)
- Separate from the subject with a blank line
- Write in imperative mood, wrap at 72 characters
- **2+ points &rarr; always use a bullet list** (never multiple
  paragraphs for separate points)

## Examples

```text
feat(docs): add Service section to Docker wiki and link from setup
```

```text
fix(backend): handle missing token in auth middleware

- Return 401 instead of crashing on None
- Add unit test for the empty-header case
```

```text
chore(nix): update flake inputs
```
