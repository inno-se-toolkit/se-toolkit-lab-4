# Lab 3 — Plan

## Context

Lab 3 builds on Lab 2, where students:

- Ran a FastAPI web server locally
- Fixed a bug and submitted a PR
- Ran the server using Docker Compose (with Caddy reverse proxy)
- Deployed to a Linux VM

Lab 3 combines the scope of the old Lab 3 (REST API design + testing) and old Lab 4 (database + containerized deployment), taking into account that Docker Compose was already introduced in Lab 2.

The starting codebase is a fork of Lab 2: a FastAPI app serving course items from JSON files, with Docker Compose + Caddy already configured.

---

## Story

> Your senior engineer says:
>
> "The prototype works and is deployed. Now we need to make it production-grade.
> That means proper API documentation, a real database, automated tests,
> and a server that won't get hacked on the first day."

---

## Proposed structure

### Required tasks

#### Task 1: Explore the API documentation (Swagger)

FastAPI auto-generates interactive docs at `/docs` (Swagger UI) and `/redoc`.

Students will:

- Open Swagger UI in the browser
- Try existing endpoints interactively (send requests, inspect responses)
- Read the generated OpenAPI spec
- Understand how Pydantic models become documented request/response schemas

**Key concepts:** OpenAPI, Swagger UI, interactive API docs, API contract.

**Why first:** Immediate visual payoff. Students see something tangible before writing code.

---

#### Task 2: Design and implement new endpoints (RESTful API)

Extend the existing API with full CRUD operations.

Students will:

- Add endpoints: `POST /items`, `PUT /items/{id}`, `DELETE /items/{id}`
- Use proper HTTP status codes (`201 Created`, `204 No Content`, `404 Not Found`, `422 Unprocessable Entity`)
- Define Pydantic request/response schemas (`ItemCreate`, `ItemUpdate`, `ItemRead`)
- Add input validation (e.g., name required, price > 0)
- Verify new endpoints appear correctly in Swagger UI

**Key concepts:** REST conventions, HTTP verbs, status codes, request/response schemas, input validation.

---

#### Task 3: Add a database

Replace JSON file storage with a real database.

Students will:

- Add a Postgres service to `docker-compose.yml` (they already know Compose from Lab 2)
- Set up SQLAlchemy: engine, session, declarative base
- Create SQLAlchemy models mirroring the Pydantic schemas
- Replace the JSON-reading service layer with DB queries
- Verify data persists across server restarts

**Key concepts:** Relational database, ORM, SQLAlchemy, Docker Compose multi-service, data persistence.

**Why Postgres over SQLite:** More realistic (separate service, runs in Docker like production). Students already know Compose, so adding a service is natural.

---

#### Task 4: Write tests

Students will:

- Write tests using `pytest` + FastAPI `TestClient`
- Test each CRUD endpoint (create, read, update, delete)
- Test error cases (404 for missing items, 422 for invalid input)
- Use test fixtures to isolate DB state between tests

**Key concepts:** Automated testing, test isolation, fixtures, TestClient.

---

#### Task 5: Harden the server

Students will:

- Create a non-root SSH user with `sudo` access
- Set up SSH key authentication for that user
- Disable root password login in `sshd_config`
- Install and configure `ufw` (firewall) — allow only SSH + app port
- Install and configure `fail2ban` — protect against brute-force

**Key concepts:** Principle of least privilege, SSH key auth, firewall, brute-force protection.

---

#### Task 6: Create a checkbot SSH user

Students will:

- Create a dedicated limited user (e.g., `checkbot`) on the VM
- Add the instructor-provided public key to `checkbot`'s `authorized_keys`
- This enables the autochecker to SSH into the VM and verify the deployment

**Key concepts:** Dedicated service accounts, least-privilege access, SSH public key distribution.

---

### Optional tasks

- **Pagination and filtering:** `GET /items?page=1&size=10`, `GET /items?min_price=10`
- **Alembic migrations:** Version-controlled database schema changes
- **Health check endpoint:** `/health` that verifies DB connectivity
- **HTTPS:** Configure Caddy with a real domain and automatic TLS

---

## Open questions and concerns

### 1. Student skill level

Students might be overwhelmed. Many of them worked on backend for the first time in Lab 2. They have completed one semester of programming and are now in their second semester of CS. The jump from "run and fix someone else's code" (Lab 2) to "add a database, write tests, configure a firewall" (Lab 3) is significant.

### 2. Two versions of each task

It would be good to have two variants of each task:

- **High-level version:** Clearly states the desired result and acceptance criteria, but doesn't prescribe how to get there. For stronger students who want to figure it out.
- **Step-by-step version:** Detailed instructions like Lab 2 (click here, run this command, check that). For students who need more guidance.

Open question: how to present these two variants? Collapsible sections? Separate pages? A "hints" appendix? Something to think about.

### 3. Success threshold — what do we actually require?

We should be very clear about what the threshold of success is — both for us (instructors) and for students. What are the key things we want them to take away from this lab?

The **required tasks should target this minimum**. Everything above that (optional tasks, stretch goals) is extra.

Suggested key takeaways (to discuss):

- Students can explain what a REST API is and what Swagger docs show
- Students can add an endpoint with proper status codes
- Students can connect a database to a web app
- Students can write and run a test
- Students have a minimally secure server (non-root user, firewall)

Once we agree on the minimum, we should evaluate whether the required tasks above are right-sized or if some should move to optional.

### 4. Task sizing

Is 6 required tasks too many? Possible simplifications:

- **Merge Tasks 5 and 6** (server hardening + checkbot user) into one task
- **Make Task 4 (tests) optional** if we decide the core takeaway is API + DB + deployment
- **Reduce Task 2 scope** — maybe only POST + one other verb, not full CRUD

### 5. Autochecker integration

Tasks 5-6 (server hardening + checkbot SSH user) enable the autochecker to SSH into the VM and verify deployments. This is a dependency for automated grading of the deployment tasks. We need to decide: should this be early in the lab (so autochecker works from the start) or late (as a capstone)?
