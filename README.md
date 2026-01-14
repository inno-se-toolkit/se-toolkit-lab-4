# Lab 01 – Products, Architecture & Roles

To kickstart the course, you will explore two things:
>
> 1) How real software products are structured;
> 2) What kind of engineers build and operate them.
>
## Learning Outcomes

By the end of this lab you should be able to:

- Use GitHub to structure your work and collaborate with peers (issues, branches, pull requests, and reviews).
- Explain the basic architecture of a real-world digital product in terms of components, data flow, and deployment.
- Reflect on your career in tech, examine your current skillset, and plan for the future.

## Tasks overview

To complete this lab, you will need to:

- Setup your github account and this lab's repo.
- Pick an existing digital product.
- Sketch its architecture: components, data flow, deployment.
- Map components to tech roles and skills using real job postings and `roadmap.sh`.
- Practice using GitHub issues, branches and pull requests (PRs) to organize your work in a repository (repo) and get feedback from peers.

This and all other lab assignments will simulate real-life engineering practices:

- Follow processes;
- Communicate via issues/PRs;
- Keep the work reviewable;
- Write acceptance criteria;
- Write clear commit messages.

## Repo structure

- `.github/ISSUE_TEMPLATE` – templates for your issues.
- `.github/pull_request_template.md` – a template for PRs.

---

## Lab setup

<!-- TODO list what you'll get as a result of the setup -->

### Set up a fork

1. Create a GitHub account.
2. Fork this repo to your GitHub account.
3. Continue your work in the forked repo.
4. In the repo -> `Settings` -> `General` -> `Features`, enable `Issues`.
5. <details> <summary> (Optional) Create a label for tasks.</summary>

   In the repo -> `Issues` -> `Labels`, create a new label:
   1. Click `New label`.
   2. Name: `task`.
   3. Click `Create label`.

   </details>
    <!-- TODO ask students to provide a proof of the setup -->
6. <details> <summary>(Optional) Protect your <code>main</code> branch. </summary>

   In the repo -> `Settings` -> `Code and automation` -> `Add branch ruleset`:
   1. `Ruleset Name`: `push`
   2. `Enforcement status`: `Active`
   3. `Target branches` -> `Add target` -> `Include default branch`
   4. Rules:
      - [x] `Restrict deletions`
      - [x] `Require a pull request before merging`:
         - `Required approvals`: `1`
         - `Require conversation resolution before merging`
         - `Allowed merge methods`: `Merge`.
      - [x] Block force pushes
  
  </details>

### Add a classmate as a collaborator

1. In the repo `Settings` -> `Collaborators` -> `Add people`, add a classmate as a collaborator.
2. Make sure your collaborator have accepted the invitation sent to their email.

### Set up your local tools

1. (If needed) On your computer, configure [`git`](https://git-scm.com/):

    ```bash
    git config --global user.name "Your Name"
    git config --global user.email "your@email"
    ```

2. Install [`VS Code`](https://code.visualstudio.com/). This is our code editor of choice that we'll use in this course.

    - Read about [`Basic Layout`](https://code.visualstudio.com/docs/getstarted/userinterface#_basic-layout) - Basic UI elements in `VS Code`.

    <!-- TODO: Add a screenshot with all key elements marked. -->
    - <details> <summary> (Optional) Learn more about <code>VS Code</code>. </summary>

      - [`Activity Bar`](https://code.visualstudio.com/api/ux-guidelines/activity-bar) - Menus of extensions;
      - [`Status Bar`] - Status information and additional menus of extensions.
      - [`Command Palette`](https://code.visualstudio.com/docs/getstarted/userinterface#_command-palette) - How to use commands provided by extensions;
      - [`Terminal`](https://code.visualstudio.com/docs/terminal/getting-started) - How to run terminal commands inside `VS Code`;
      - [`Source Control`](https://code.visualstudio.com/docs/sourcecontrol/overview) - How to use `Git` via `VS Code` UI;
      - [`Extension Marketplace`](https://code.visualstudio.com/docs/configure/extensions/extension-marketplace) - How to install extensions;
      - Enable [`files.autoSave`](https://code.visualstudio.com/docs/editing/codebasics#_save-auto-save) - How to enable auto-save to not lose your work;
      - Enable [`editor.formatOnSave`](https://code.visualstudio.com/docs/editing/codebasics#_formatting) - How to enable auto-formatting to keep your code clean;
      - [`Custom Layout`](https://code.visualstudio.com/docs/configure/custom-layout) - E.g., move the `Primary Side Bar` to the right.

      </details>

### Open the repository on your machine

1. On your computer, create a directory `pre-swp`.
2. In that directory, clone the lab repo.

    ```bash
    git clone https://github.com/<your-username>/lab-01-market-product-and-git
    ```

3. Open the repo in `VS Code`.

    ```bash
    cd pre-swp
    code lab-01-market-product-and-git
    ```

### Set up `VS Code` extensions

1. Install the recommended `VS Code` extensions (listed in [`./.vscode/extensions.json`](./.vscode/extensions.json)) when `VS Code` suggests to install them.
2. Sign in to accounts.
    In the `Activity Bar`:
    1. Click `Accounts`
    2. Click `Sign in with GitHub`
    3. Repeat for any of the extensions if needed.

3. <details><summary> (Optional) Check <code>GitLens</code>.</summary>

    In the `Status Bar`:

    1. Click `Visualize commits on the Commit Graph`.
    2. Make sure you can see the commit graph.

    In the `Activity Bar`:

    1. Click `Source Control`.
    2. Click `GitLens` in the opened `Primary Side Bar` to open the `GitLens` panel.
    3. In the `GitLens` panel, click `Remotes`.
    4. Make sure `origin` points to your repo URL.
    5. In the `GitLens` panel, click `Commits`.
    6. Make sure you can see commits on the current branch.

    Learn more about [`GitLens` features](https://help.gitkraken.com/gitlens/gitlens-features/).
  
  </details>
  
### (Optional) Set up an agent

1. Watch [tutorial](https://www.youtube.com/watch?v=G0uIVEt3aj4).
2. Set up [`Kilo Code`](https://kilo.ai/install) or another coding agent with [`Qwen3 Coder`](https://github.com/QwenLM/Qwen3-Coder) or another free model, e.g., from [`OpenRouter`](https://openrouter.ai/collections/free-models).

### Skim the lab description

1. Skim this `README.md` file once so you know what’s coming.

---

## Submission checklist

By the end of the lab:

- Make sure that each task that you have completed has a corresponding issue linked to a PR.
- Close the issues for which all related activities are done.
<!-- - TODO how does a TA check the work? -->
- Explain your diagram, chosen role in a short conversation with the TA.

<!-- TODO check out all completed steps -->

---

## Procedure for each task

> [!NOTE]
> This procedure is based on the [`GitHub flow`](https://docs.github.com/en/get-started/using-github/github-flow).

1. [Create](https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/creating-an-issue) a `GitHub` issue in your forked repo using the `Lab Task` [issue form](https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/configuring-issue-templates-for-your-repository#creating-issue-forms).
2. Create a new branch for the issue via [`GitHub`](https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/creating-a-branch-for-an-issue) or via `git checkout -b <branch-name>`.
3. Make [commits](https://smartprogramming.in/tutorials/git-and-github/git-commit) to that branch to complete the task.
     - Commit messages must follow the [`Conventional Commits`](https://www.conventionalcommits.org/en/v1.0.0/) format.
     - Commit to the branch using one of these approaches:
       1. Using `VS Code` (see [docs](https://code.visualstudio.com/docs/sourcecontrol/staging-commits)): `Activity Bar` -> `Source Control` -> Click a file -> Select lines in the editor -> Right mouse click the selected lines -> Click `Stage Selected Ranges` -> Write a commit message -> Click `Commit`.
       2. Using a terminal (adds all changes in these files to the staging area):

          ```console
          git add <file 1> <file 2> ... <file n>
          git commit -m "<message>"
          ```

4. Push the branch to your forked repo:

    ```console
    git push -u origin <branch-name>
    ```

5. Create a PR to the `main` branch via [`GitHub`](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request) ([tutorial](https://www.geeksforgeeks.org/git/creating-a-pull-request-on-any-public-repository-from-github-using-vs-code/)) or via [`GitHub Pull Requests`](https://code.visualstudio.com/docs/sourcecontrol/github#_pull-requests).
6. Write an appropriate PR description following the PR template.
7. [Link the PR](https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/linking-a-pull-request-to-an-issue#linking-a-pull-request-to-an-issue-using-a-keyword) to the issue, e.g. `Closes #<issue number>`.
8. Request a review of the PR from the collaborator.
9. Address the comments, e.g., make fixes or ask to clarify the comment.
10. Get the collaborator to approve the PR.
11. Merge the PR to the `main` branch.
12. Close the issue.
13. Delete the branch.

## PR reviews

As a PR reviewer, you must:

- Review the assigned PR and leave at least 2 meaningful comments created for [particular lines](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/reviewing-changes-in-pull-requests/commenting-on-a-pull-request#adding-comments-to-a-pull-request).
- Approve the PR if you're satisfied with the PR.

As a PR author, you must:

- Reply to comments in a meaningful way, e.g., write “Fixed in d0d5aeb” (`d0d5aeb` being the id of commit where you addressed the comment), ask to clarify the comment, or explain why you disagree.
- Make necessary changes based on the review.

---

## Tasks

You work **independently** on the tasks below in your forked repo.

For each task, follow the [procedure](#procedure-for-each-task).

Tasks are non-optional unless marked as "optional".

### 1. Pick a product and describe its architecture

1. [ ] Create an issue `[Task] Product & architecture description`.
2. [ ] Decide on how to make the architecture diagrams. We suggest the following approaches:
   1. You can *prototype* diagrams in `./docs/diagrams/prototype` via the [`hediet.vscode-drawio`](https://marketplace.visualstudio.com/items?itemName=hediet.vscode-drawio) extension ([example](./docs/diagrams/prototype/example.drawio.svg)).

      However, it's not a good idea to version control images because you can't conveniently visualize their diffs and therefore can't track changes well.

      Therefore, you must use the ["diagrams as code"](https://simmering.dev/blog/diagrams/) approach and eventually switch to one of the following approaches.
   2. <details><summary> You can write <code><a href="https://plantuml.com/">PlantUML</a></code> code.</summary>

      - [ ] Install the [`jebbs.plantuml`](https://marketplace.visualstudio.com/items?itemName=jebbs.plantuml) `VS Code` extension.
      - [ ] Install [`Docker`](https://docs.docker.com/get-started/get-docker/).
      - [ ] Run in the terminal `docker run --name plantuml-server -d -p 48080:8080 plantuml/plantuml-server:jetty` to start a `PlantUML` server.
      - [ ] Open the `PlantUML` server in the browser at `http://localhost:48080` to make sure it works.
      - [ ] Open [`./docs/diagrams/src/architecture-component.puml`](./docs/diagrams/src/architecture-component.puml) in `VS Code`.
      - [ ] Click the `Preview Current Diagram` icon.

          The `48080` port is already set in [`./.vscode/settings.json`](./.vscode/settings.json). Therefore, previewing should work out of the box.

      - [ ] Write the `PlantUML` code in `./docs/diagrams/src/` and render the diagrams to SVG in `./docs/diagrams/out/` using the `jebbs.plantuml` extension. These directories are already set in [`./.vscode/settings.json`](./.vscode/settings.json).
      - [ ] To render diagrams to SVG, open the [`Command Palette`](https://code.visualstudio.com/docs/getstarted/userinterface#_command-palette), write `PlantUML: Export Workspace Diagrams`, and choose `svg`.
      - [ ] [Include](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax) the rendered images into your `Markdown` file.

      </details>
   3. You can write [`Mermaid`](https://mermaid.js.org/) code in `Markdown` files in code blocks with the `mermaid` language tag (see [docs](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/creating-diagrams#creating-mermaid-diagrams)).
   4. You can use any other tool if it supports the "diagrams as code" approach, e.g., [`Structurizr`](https://structurizr.com/), [`D2`](https://d2lang.com/), [`LikeC4`](https://github.com/likec4/likec4) etc.

    > [!IMPORTANT]
    >
    > The goal of the diagram drawing tasks is to get familiar with certain architectural views (static, dynamic), not to design a system.
    >
    > To design a system rationally, you need to consider the architectural drivers. This approach is outlined in the optional [Task 4](#4-optional-update-architecture).

3. [ ] Create `./docs/architecture.md`. In `./docs/architecture.md`:
    1. [ ] In the `## Product choice` section:
         - [ ] Pick one product from this list or propose your own:
             - Yandex Taxi
             - Telegram
             - ChatGPT.com
             - Wildberries.ru
             - Uchi.ru
             - Any other widely used full-stack app (except for Uber because it's used in examples). Agree with your TA if you choose this option.
         - [ ] Provide:
           - [ ] The product's name;
           - [ ] A link to the product's website.
           - [ ] A short description of the product (1–2 sentences).
    2. [ ] In the `## Motivation` section:
         - [ ] Explain in 3-4 sentences why you personally would be interested to work on this product as a tech specialist.
    3. [ ] In the `## Main components` section:
        - [ ] Select at least 5 main [components](https://c4model.com/abstractions/component) of the product. For example:
          - Mobile app
          - Backend API
          - Authentication service
          - Payment / billing
          - Notifications
          - Admin panel
          - Data analytics
        - [ ] For each component, explain in 1–2 sentences what it does.
        - [ ] Provide a [component diagram](https://en.wikipedia.org/wiki/Component_diagram).
          - [ ] If you use [`PlantUML`](https://plantuml.com/component-diagram):
            - [ ] Store the diagram source code in `./docs/diagrams/src/architecture-component.puml`.
            - [ ] See [how to draw a connection](https://stackoverflow.com/questions/55077828/using-required-provided-interfaces-in-component-diagrams-plantuml/57134601#57134601).
    4. [ ] In the `## Data flow` section:
          - [ ] Describe what happens when a typical user action occurs (e.g. user orders a taxi / sends a message).
          - [ ] Mention which components talk to each other and what kind of data they exchange.
          - [ ] Provide a [sequence diagram](https://en.wikipedia.org/wiki/Sequence_diagram).
            - [ ] If you use [`PlantUML`](https://plantuml.com/sequence-diagram):
              - [ ] Store the diagram source code in `./docs/diagrams/src/architecture-sequence.puml`.
            - [ ] Alternatively, use [`Mermaid`](https://mermaid.js.org/syntax/sequenceDiagram.html).
    5. [ ] In the `## Deployment` section:
         - [ ] Briefly describe where these components live (high-level view). Example:
             - On user devices (mobile/web app).
             - On servers (backend services, databases).
         - [ ] Provide a [deployment diagram](https://en.wikipedia.org/wiki/Deployment_diagram).
           - [ ] If you use [`PlantUML`](https://plantuml.com/deployment-diagram):
             - [ ] Store the diagram source code in `./docs/diagrams/src/architecture-deployment.puml`.
           - [ ] Alternatively, use [`Mermaid`](https://mermaid.js.org/syntax/c4.html#c4-deployment-diagram-c4deployment).
    6. [ ] In the `## Knowledge Gaps` section:
         - [ ] Write at least two things in your architecture that you are not fully sure about (guesses, questions, etc.).

---

### 2. Roles, skills, roadmap.sh, and job postings

1. [ ] Create an issue `[Task] Roles and skills mapping`.

    > [!IMPORTANT]
    > You can ask an LLM “what does a `<role-name>` usually do?”, but:
    >
    > - You must visit `roadmap.sh` and real job postings yourself.
    > - Your reflections about what you have / don’t have must be honest and personal.

2. [ ] In `./docs/roles-and-skills.md`:

     - [ ] In the `## Roles for components` section:
        - [ ] For each component from `architecture.md`, list IT roles that are likely involved in the development and maintenance of that component.
        - [ ] Use a nested list. Example:
          - Mobile app
            - Mobile engineer (iOS/Android)
            - QA
            - ...
          - Payment service
            - Back end engineer
            - DevOps
            - QA
          - ...

     - [ ] In the `## Common skills across roles` section:
       - [ ] Based on your intuition and some research, list **skills that almost everyone needs**. Example:
          - Git
          - Basic Linux usage
          - Understanding of HTTP and REST APIs
          - Agentic coding
          - Communicating in a team
          - Writing clear issues and PR descriptions
          - Planning
          - ...

3. [ ] Choose *one* role that seems most interesting to you now.
4. [ ] Go to [`roadmap.sh`](https://roadmap.sh/) and sign up.
5. [ ] Find the roadmap relevant for the role you chose.
6. [ ] In that roadmap, mark the items you already have at least some knowledge in.
7. [ ] In `./docs/roles-and-skills.md`, in the `## My chosen role` section, write:

    ```markdown
    ### Role
    
    <name>
    
    ### Skills I already have
    <!-- from roadmap.sh -->
    - ...
    
    ### Skills I clearly lack
    <!-- from roadmap.sh, 8-10 skills -->
    - ...
    ```

8. [ ] Find **5-7 job postings** for this role on [`HH.ru`](https://hh.ru) or a similar job site.
9. [ ] For each posting, list:
    - Link to the posting.
    - Company name.
    - Role title.
    - 3–5 key skills/requirements they mention.
10. [ ] In `./docs/roles-and-skills.md`, in the `## Job market snapshot` section, write:

    ```markdown
    ### Skills that appear in almost every posting
    <!-- 3-10 skills -->
    - ...
    
    ### Skills from postings that I haven't yet seen on roadmap.sh
    <!-- 1-5 skills -->
    - ...
    
    ### My key takeaway
    ...
    ```

---

### 3. Short personal reflection

1. [ ] Create the issue `[Task] Personal reflection`.

    > [!IMPORTANT]
    > Write this section **without** an LLM. It’s about your own thoughts.

2. [ ] In `./docs/reflection.md` write 5–10 sentences answering:
    - [ ] Which role did you choose and why?
    - [ ] What is one thing about the product’s architecture that was new to you?
    - [ ] Which course topics (`Git`, `Linux`, `Docker`, `REST`, `CI/CD`, full-stack development, data processing) seem most relevant to your chosen role?
    - [ ] What is one concrete skill you would like to improve this semester?

---

### 4. (Optional) Update architecture

1. Create the issue `[Task] Update architecture`.
2. [ ] In `./docs/architecture.md`:
    - [ ] In the `## Architectural drivers` section:
      - [ ] List 10-15 [architectural drivers](https://github.com/inno-se/the-guide?tab=readme-ov-file#architectural-drivers) for the system:
        - [ ] business goals;
        - [ ] technical constraints;
        - [ ] primary functional requirements;
        - [ ] quality requirements.
        - [ ] architectural concerns.
    - [ ] In the `## Design decisions` section:
      - [ ] List 5-7 key design decisions for the system ([example](https://github.com/otrebmuh/HotelPricingSystem/blob/433e061f712a8748fdf04a6f767752e12be2f4b9/Design/Architecture.md#10-design-decisions)).
      - [ ] Link each decision to an architectural driver.
      - [ ] Justify each decision (provide rationale) in 1-2 sentences.
      - [ ] List 1-2 discarded alternatives for each decision.

3. [ ] Update the diagrams to match your design decisions.

### 5. (Optional) Work on an agent

1. Create the issue `[Task] Work on an agent`.
2. [ ] In `docs/agent-idea.md`, sketch how an AI agent could:
    - [ ] Read `README.md`;
    - [ ] Generate `GitHub` issues automatically;
    - [ ] Create initial `Markdown` files for you.
    - [ ] Complete all tasks for you.

3. [ ] Try to implement a part of that agent.
4. [ ] Test that agent in a different fork of this repo.

### 6. (Optional) Take-home exercise

- [ ] Read this [tutorial](https://hackmd.io/@aabounegm/SWP-git) to learn about `Git`, `Github`, and `Git` workflows.
