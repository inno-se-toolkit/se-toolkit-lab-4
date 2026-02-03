# Pick a product and study its architecture

⏱️ **~30–40 min**

> [!WARNING]
> System architecture diagrams represent the system architecture but they are not the [system architecture](https://github.com/inno-se/the-guide?tab=readme-ov-file#architecture).

1. [ ] Create an issue `[Task] Product & architecture description`.
2. [ ] Learn how to [embed images](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax#images) into your `Markdown` files.
3. [ ] Pick one product from this list:

    - Yandex Go
    - Telegram
    - Wildberries.ru

    Alternatively, choose another full-stack product with at least a million users. In that case, you'll have to [visualize the architecture](./Appendix.md#visualize-the-architecture) on your own.

   > [!NOTE]
   > The provided architecture diagrams are based on educated guesses since the products in the list are mostly closed-source.
   > All diagrams were generated via Gemini 3 Pro (free web version) and edited by the course instructors.

4. [ ] Find the directory with the product's architecture diagrams in two formats:
    - `PlantUML` code in `./docs/diagrams/src/<product-name>`.
    - Rendered architecture diagrams in `./docs/diagrams/out/<product-name>`.

    If you chose another project, provide component, deployment, sequence diagrams in two formats in corresponding directories.

5. [ ] Create `./docs/architecture.md` and add the following contents:
    1. [ ] In the `## Product choice` section:
        - [ ] Provide:
          - [ ] The product's name;
          - [ ] A link to the product's website.
          - [ ] A short description of the product (1–2 sentences).
    2. [ ] In the `## Main components` section:
        > [!NOTE]
        > According to the [`C4 model`](https://c4model.com/abstractions/component), a *component* is a grouping of related functionality encapsulated behind a well-defined interface.
        - [ ] Add the product's `Component Diagram.svg`.
        - [ ] Provide a link to the `PlantUML` code for that [component diagram](./Appendix.md#component-diagram).
        - [ ] Select at least 5 main components of the product from the component diagram.
        - [ ] For each selected component, explain in 1–2 sentences what it does.
    3. [ ] In the `## Data flow` section:
        - [ ] Embed the product's `Sequence Diagram.svg`.
        - [ ] Provide a link to the `PlantUML` code for that [sequence diagram](./Appendix.md#sequence-diagram).
        - [ ] Describe what happens when a typical user action occurs (e.g. a user orders a taxi or sends a message).
        - [ ] Mention which components talk to each other and what kind of data they exchange.
    4. [ ] In the `## Deployment` section:
        - [ ] Embed the product's `Deployment Diagram.svg`.
        - [ ] Provide a link to the `PlantUML` code for that [deployment diagram](./Appendix.md#deployment-diagram).
        - [ ] Briefly describe where the components are deployed.
    5. [ ] In the `## Assumptions and Open Questions` section:
        - [ ] List at least two assumptions you made while describing the architecture.
        - [ ] List at least two questions you couldn't answer from public information.

        Examples:
        - Yandex Go: *"I assumed the rider app talks directly to the driver app, but there's probably a server in between."*
        - Telegram: *"I'm not sure if media files are stored on the same servers as text messages."*
        - Wildberries: *"I don't know if payments are processed by Wildberries or by an external payment service."*
