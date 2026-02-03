# Pick a product and study its architecture

**Time:** ~30-40 min

**Purpose:** Understand how a real software product may be structured by examining its components, data flow, and deployment.

**Context:** Imagine you have joined one of these product teams. On your first days, you need to understand what the product does and how it is structured.

## Steps

### 1. Create an issue

Title: `[Task] Product & architecture description`

### 2. Choose a product

Available products:

- Yandex Go
- Telegram
- Wildberries.ru

Alternatively, choose another full-stack product with at least a million users. In that case, you'll have to [visualize the architecture](../../appendix.md#visualize-the-architecture) on your own.

### 3. Find the diagrams

> [!WARNING]
> System architecture diagrams represent the system architecture but they are not the [system architecture](https://github.com/inno-se/the-guide?tab=readme-ov-file#architecture).

> [!WARNING]
>
> The provided architecture diagrams are based on educated guesses since the products in the list are mostly closed-source.
> All diagrams were generated via Gemini 3 Pro (free web version) and edited by the course instructors.

1. Find the directory with the product's architecture diagrams in two formats:
    - `PlantUML` code is in `./docs/diagrams/src/<product-name>`.
    - Rendered architecture diagrams are in `./docs/diagrams/out/<product-name>`.

2. If you chose another project, provide component, deployment, sequence diagrams in two formats in corresponding directories.

### 4. Create `./docs/architecture.md`

Create the file and add the following sections:

#### `## Product Choice`

Provide:

- Product name;
- Link to the product's website;
- Short description of the product (1-2 sentences).

#### `## Main components`

> [!NOTE]
>
> According to the [`C4 model`](https://c4model.com/abstractions/component), a *component* is a grouping of related functionality encapsulated behind a well-defined interface.

1. Embed the product's `Component Diagram.svg`.

   Example: `![Telegram Component Diagram](./diagrams/out/telegram/component-diagram/Component Diagram.svg)`

2. Provide a link to the `PlantUML` code for that [component diagram](../../appendix.md#visualize-the-architecture#component-diagram).
  
   Example: `![Telegram Component Diagram code](./diagrams/src/telegram/component-diagram.puml)`

3. Select at least 5 components of the product from the component diagram.

4. For each selected component, explain in 1-2 sentences what it does.

#### `## Data flow`

1. Embed the product's `Sequence Diagram.svg`.
2. Provide a link to the `PlantUML` code for that [sequence diagram](../../appendix.md#visualize-the-architecture#sequence-diagram).
3. Describe what happens when a user action described by the diagram occurs.
4. Mention which components talk to each other and what data they exchange.

#### `## Deployment`

1. Embed the product's `Deployment Diagram.svg`.
2. Provide a link to the `PlantUML` code for that [deployment diagram](../../appendix.md#visualize-the-architecture#deployment-diagram).
3. Briefly describe where the components are deployed.

#### `## Assumptions and Open Questions`

1. List at least two assumptions you made while describing the architecture.

    Examples:

    - Yandex Go: *"I assumed the rider app talks directly to the driver app, but there's probably a server in between."*
    - Telegram: *"I'm not sure if media files are stored on the same servers as text messages."*
    - Wildberries: *"I don't know if payments are processed by Wildberries or by an external payment service."*

2. List at least two questions you couldn't answer from public information.
