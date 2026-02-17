-- Learning Management Service — Database Initialization
-- This script runs automatically on the first start of the PostgreSQL container.

-- Items: learning materials organized as a tree (course → labs → tasks → steps).
-- The tree structure uses the adjacency list pattern (parent_id).
-- Type-specific attributes are stored in a JSONB column.
CREATE TABLE IF NOT EXISTS items (
    id SERIAL PRIMARY KEY,
    type VARCHAR(50) NOT NULL DEFAULT 'step',
    parent_id INTEGER REFERENCES items(id),
    title VARCHAR(255) NOT NULL,
    description TEXT NOT NULL DEFAULT '',
    attributes JSONB NOT NULL DEFAULT '{}',
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

-- Learners: students using the system
CREATE TABLE IF NOT EXISTS learners (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE,
    enrolled_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

-- Interaction logs: records of learners interacting with items
CREATE TABLE IF NOT EXISTS interaction_logs (
    id SERIAL PRIMARY KEY,
    learner_id INTEGER NOT NULL REFERENCES learners(id),
    item_id INTEGER NOT NULL REFERENCES items(id),
    kind VARCHAR(50) NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

-- Seed data: items (a course with labs, tasks, and steps)
INSERT INTO items (type, title, description, attributes) VALUES
    ('course', 'Software Engineering', 'A course on SE principles and practices.', '{"instructors": ["Alice Johnson"]}');

INSERT INTO items (type, parent_id, title, description, attributes) VALUES
    ('lab', 1, 'Version Control with Git', 'Learn Git basics: commits, branches, merging.', '{"start": "2025-09-08T09:00:00", "finish": "2025-09-14T23:59:00"}'),
    ('lab', 1, 'REST API Design', 'Design RESTful APIs using HTTP methods and status codes.', '{"start": "2025-09-15T09:00:00", "finish": "2025-09-21T23:59:00"}'),
    ('lab', 1, 'Docker Fundamentals', 'Containerize applications using Docker and Docker Compose.', '{"start": "2025-09-22T09:00:00", "finish": "2025-09-28T23:59:00"}'),
    ('lab', 1, 'Database Integration', 'Connect a web application to a PostgreSQL database.', '{"start": "2025-09-29T09:00:00", "finish": "2025-10-05T23:59:00"}');

INSERT INTO items (type, parent_id, title, description) VALUES
    ('task', 5, 'Testing with pytest', 'Write and run automated tests for Python applications.'),
    ('task', 4, 'Linux Server Administration', 'Basic server management and security hardening.'),
    ('step', 6, 'CI/CD Pipelines', 'Automate testing and deployment with GitHub Actions.');

-- Seed data: learners
INSERT INTO learners (name, email, enrolled_at) VALUES
    ('Alice Johnson', 'alice@example.com', '2025-09-01 09:00:00'),
    ('Bob Smith', 'bob@example.com', '2025-09-01 09:15:00'),
    ('Charlie Brown', 'charlie@example.com', '2025-09-15 10:00:00'),
    ('Diana Prince', 'diana@example.com', '2025-10-01 08:30:00'),
    ('Eve Adams', 'eve@example.com', '2025-10-15 11:00:00');

-- Seed data: interaction logs
INSERT INTO interaction_logs (learner_id, item_id, kind, created_at) VALUES
    (1, 1, 'view', '2025-09-02 10:00:00'),
    (1, 2, 'view', '2025-09-02 10:30:00'),
    (1, 2, 'complete', '2025-09-03 14:00:00'),
    (2, 1, 'view', '2025-09-02 11:00:00'),
    (2, 3, 'view', '2025-09-05 09:00:00'),
    (2, 3, 'attempt', '2025-09-05 09:30:00'),
    (3, 1, 'view', '2025-09-16 10:00:00'),
    (3, 4, 'view', '2025-09-18 15:00:00'),
    (4, 1, 'view', '2025-10-02 08:00:00'),
    (4, 5, 'complete', '2025-10-05 16:00:00'),
    (5, 1, 'view', '2025-10-16 09:00:00'),
    (5, 6, 'view', '2025-10-16 09:30:00');
