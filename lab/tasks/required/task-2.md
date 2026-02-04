# Study tech roles involved in the chosen product

**Time:** ~30-40 min

**Purpose:** Understand the different tech roles involved in developing and maintaining a software product and their responsibilities.

**Context:** Now that you have analyzed the product architecture, you need to understand what roles are typically involved in building and maintaining such systems.

## Steps

### 1. Create an issue

Title: `[Task] Roles and skills mapping`

### 2. Create `docs/roles-and-skills.md`

Create the file and add the following sections:

#### `## Components and roles`

For each selected component from `architecture.md`, list IT roles that are likely involved in the development and maintenance of that component.

Use a nested list. Example:

```markdown
- Mobile app
  - Mobile engineer (iOS/Android)
  - QA
  - ...
- Payment service
  - Back-end engineer
  - DevOps
  - QA
- ...
```

#### `## Roles and responsibilities`

1. Select any five roles from the previous section.
2. Consult an LLM or search engine to find out what are the typical responsibilities of these roles (what do people holding these roles do?).
3. For each selected role, briefly describe the responsibilities.

#### `## Common skills across roles`

Based on your intuition and some research, list **tech skills that are required for these responsibilities**.

## Acceptance Criteria

- [ ] Issue created
- [ ] `docs/roles-and-skills.md` created
- [ ] Components mapped to roles (at least 5 components)
- [ ] Role mapping seems reasonable for this product
- [ ] 5 roles described with responsibilities
- [ ] Common skills section is present
- [ ] Common skills seem reasonable
