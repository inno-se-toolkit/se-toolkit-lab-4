# Lab 01 – Products, Architecture & Roles

To kickstart the course, you will explore two things:
>
> 1) How real software products are structured;
> 2) What kind of engineers build and operate them.
>
## Learning Outcomes

By the end of this lab you should be able to:

- Explain the basic architecture of a real-world digital product in terms of modules, data flow, and deployment.
- Identify which tech roles work on which parts of that product, and which general skills are shared across roles.
- Use GitHub issues, branches, and pull requests (PRs) to structure your work and get a peer review.

## Tasks overview

To complete this lab, you will need to:

- Pick an existing digital product.
- Sketch its architecture: modules, data flow, deployment.
- Map modules to tech roles and skills using real job postings and `roadmap.sh`.
- Practice using GitHub issues, branches and pull requests (PRs) to organize your work in a repository (repo) and get feedback from peers.

This and all other lab assignments will simulate the engineering practices in a real team:

- Follow processes;
- Communicate via issues/PRs;
- Keep the work reviewable;
- Practice writing acceptance criteria;
- Write clear commit messages.

## Repo structure

- `.github/ISSUE_TEMPLATE` – templates for your issues.
- `.github/pull_request_template.md` – a template for PRs.

---

## Lab setup

1. Create a GitHub account.
2. Fork this repo to your GitHub account.
3. Continue your work in the forked repo.
4. In the repo Settings -> General -> Features, enable Issues.
5. In Issues -> Labels, create a new label:
   1. Click `New label`.
   2. Name: `task`.
   3. Click `Create label`.
6. In the repo Settings -> Code and automation -> Add branch ruleset:
   1. Ruleset Name: `push`
   2. Enforcement status: `Active`
   3. Target branches -> Add target -> Include default branch
   4. Rules:
      - [x] Restrict deletions
      - [x] Require a pull request before merging:
         - Required approvals: `1`
         - Require conversation resolution before merging
         - Allowed merge methods: `Merge`.
      - [x] Block force pushes
7. In the repo Settings -> Collaborators -> Add people, add a classmate as a collaborator.
8. Make sure your collaborator have accepted the invitation sent to their email.

9. (If needed) On your computer, configure [`git`](https://git-scm.com/):

    ```bash
    git config --global user.name "Your Name"
    git config --global user.email "your@email"
    ```

10. (Recommended) Install [`VS Code`](https://code.visualstudio.com/) and read about:
    - [Command Palette](https://code.visualstudio.com/docs/getstarted/userinterface#_command-palette).
    - [Terminal](https://code.visualstudio.com/docs/terminal/getting-started).
    - [Source Control](https://code.visualstudio.com/docs/sourcecontrol/overview).
    - [Extension Marketplace](https://code.visualstudio.com/docs/configure/extensions/extension-marketplace).
11. On your computer, create a directory `pre-swp`.
12. In that directory, clone the lab repo.

    ```bash
    git clone https://github.com/your-username/lab-01-market-product-and-git
    ```

13. Open the repo in `VS Code`.

    ```bash
    cd pre-swp
    code lab-01-market-product-and-git
    ```

14. Install recommended VS Code extensions.
15. Sign in to accounts.

    In the Activity Bar:

    1. Click `Accounts`
    2. Click `Sign in with GitHub to use GitLens ...`
    3. Click `Accounts`
    4. Click `Sign in with GitHub to use GitHub Pull Requests ...`.

16. Check GitLens.

    In the Activity Bar:

    1. Click `Source Control`
    2. In the `GitLens` panel, click `Remotes`.
    3. Make sure `origin` points to your repo URL.
    4. In the `GitLens` panel, click `Commits`.
    5. Make sure you can see commits to this repo.

17. Skim this `README.md` file once so you know what’s coming.

---

## Main tasks

You work **independently** on the tasks below in your forked repo.

When you're done with a task, you ask your collaborator to review your PR created for that task.

The exact flow for each task is `Issue -> PR -> Review`:

- [Create](https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/creating-an-issue) a GitHub issue in your forked repo using one of the suggested issue types.
- Create a new branch for the issue using [GitHub](https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/creating-a-branch-for-an-issue) or via `git checkout -b branch-name`.
- Make commits to that branch to complete the task.
- Write a commit message following the [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) format for each commit.
- [Create](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request#creating-the-pull-request) a PR to the `main` branch.
- Request a review of the PR from the collaborator.
- Make necessary changes based on the review.
- Get the collaborator to approve the PR.
- Merge the PR to the `main` branch.
- Close the issue.

Be ready to demonstrate the completed tasks to the TA at the end of the lab.

---

### 1. Pick a product and describe its architecture

1. [ ] Create an issue `[Task] Product & architecture description`.
2. [ ] Create a branch for it and switch to that branch, e.g., `git checkout -b task-1`.
3. [ ] Decide on how to make the architecture diagrams. We suggest the following approaches:
   1. You can *prototype* diagrams via the [`hediet.vscode-drawio`](https://marketplace.visualstudio.com/items?itemName=hediet.vscode-drawio) extension. However, it's not a good idea to version control images because you can't conveniently visualize their diffs and therefore can't track changes. Therefore, you must use the ["diagrams as code"](https://simmering.dev/blog/diagrams/) approach and eventually switch to one of the other approaches.
   2. You can write [PlantUML](https://plantuml.com/) code.
      - [ ] Install the [`jebbs.plantuml`](https://marketplace.visualstudio.com/items?itemName=jebbs.plantuml) VS Code extension.
      - [ ] Run `docker run --name plantuml-server -d -p 48080:8080 plantuml/plantuml-server:jetty` to access the PlantUML server. The `48080` port is already set in `./.vscode/settings.json`.
      - [ ] Write the PlantUML code in `./docs/diagrams/src/` and render the diagrams to SVG in `./docs/diagrams/out/` using the `jebbs.plantuml` extension. These directories are already set in `./.vscode/settings.json`.
      - [ ] [Include](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax) the rendered images into your Markdown file.
   3. You can write [Mermaid](https://mermaid.js.org/) code in Markdown code blocks with the `mermaid` language tag (see [docs](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/creating-diagrams#creating-mermaid-diagrams)).
   4. You can use any other tool if it supports the "diagrams as code" approach, e.g., [Structurizr](https://structurizr.com/), [D2](https://d2lang.com/), [LikeC4](https://github.com/likec4/likec4) etc.
4. [ ] Create `./docs/architecture.md`. In `./docs/architecture.md`:
    1. [ ] In the `## Product choice` section:
         - [ ] Pick one product from this list or propose your own:
             - Yandex Taxi
             - Telegram
             - ChatGPT.com
             - Wildberries.ru
             - Uchi.ru
             - Any other widely used full-stack app except for Uber because it's used in examples (agree with TA if you choose this option).
    2. [ ] In the `## Motivation` section:
         - [ ] Explain in 3-4 sentences why you personally would be interested to work on this product as a tech specialist.
    3. [ ] In the `## Main modules` section:
        - [ ] Select at least 5 main system modules. For example:
          - Mobile app
          - Backend API
          - Authentication service
          - Payment / billing
          - Notifications
          - Admin panel
          - Data analytics
        - [ ] For each module, explain in 1–2 sentences what it does.
        - [ ] Provide a [component diagram](https://en.wikipedia.org/wiki/Component_diagram).
          - [ ] If you use [`PlantUML`](https://plantuml.com/component-diagram):
            - [ ] Store the diagram source code in `./docs/diagrams/src/architecture-component.puml`.
            - [ ] See [how to draw a connection](https://stackoverflow.com/questions/55077828/using-required-provided-interfaces-in-component-diagrams-plantuml/57134601#57134601).
    4. [ ] In the `## Data flow` section:
          - [ ] Describe what happens when a typical user action occurs (e.g. user orders a taxi / sends a message).
          - [ ] Mention which modules talk to each other and what kind of data they exchange.
          - [ ] Provide a [sequence diagram](https://en.wikipedia.org/wiki/Sequence_diagram).
            - [ ] If you use [`PlantUML`](https://plantuml.com/sequence-diagram):
              - [ ] Store the diagram source code in `./docs/diagrams/src/architecture-sequence.puml`.
            - [ ] Alternatively, use [`Mermaid`](https://mermaid.js.org/syntax/sequenceDiagram.html).
    5. [ ] In the `## Deployment` section:
         - [ ] Briefly describe where these modules live (high-level view):
             - On user devices (mobile/web app).
             - On servers (backend services, databases).
         - [ ] Provide a [deployment diagram](https://en.wikipedia.org/wiki/Deployment_diagram).
           - [ ] If you use [`PlantUML`](https://plantuml.com/deployment-diagram):
             - [ ] Store the diagram source code in `./docs/diagrams/src/architecture-deployment.puml`.
           - [ ] Alternatively, use [`Mermaid`](https://mermaid.js.org/syntax/c4.html#c4-deployment-diagram-c4deployment).
    6. [ ] In the `## Knowledge Gaps` section:
         - [ ] Write at least two things in your architecture that you are not fully sure about (guesses, questions, etc.).
5. [ ] Commit and push your changes with a clear message following [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) using one of these methods:
    1. In VS Code:
       1. Activity Bar -> Source Control -> Commit.
       2. GitLens panel -> `task-1` -> Publish task-1 to GitHub.
    2. Via `git` CLI:

        ```bash
        git add docs
        git commit -m "feat(docs): describe the high-level architecture of the product"
        git push -u origin task-1
        ```

6. [ ] Open a PR to `main`:
    - [ ] [Link the PR](https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/linking-a-pull-request-to-an-issue#linking-a-pull-request-to-an-issue-using-a-keyword) to the issue, e.g. `Closes #<issue number>`.
    - [ ] Request a review from the collaborator.

---

### 2. Roles, skills, roadmap.sh, and job postings

1. [ ] Create an issue `[Task] Roles and skills mapping`.

2. [ ] Create a branch for it and switch to that branch, e.g., `git checkout -b task-2`.

    > [!IMPORTANT]
    > You can ask an LLM “what does a *role* usually do?”, but:
    >
    > - You must visit `roadmap.sh` and real job postings yourself.
    > - Your reflections about what you have / don’t have must be honest and personal.

3. [ ] In `./docs/roles-and-skills.md`:

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
          - Understanding of HTTP / REST APIs
          - Agentic coding
          - Communicating in a team
          - Writing clear issues/PR descriptions
          - Planning
          - ...

4. [ ] Choose *one* role that seems most interesting to you now.
5. [ ] Go to [`roadmap.sh`](https://roadmap.sh/) and sign up.
6. [ ] Find the roadmap relevant for the role you chose.
7. [ ] In that roadmap, mark the items you already have at least some knowledge in.
8. [ ] In `./docs/roles-and-skills.md`, in the `## My chosen role` section, write:

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

9. [ ] Find **5-7 job postings** for this role on [`HH.ru`](https://hh.ru) or a similar job site.
10. [ ] For each posting, list:
    - Link to the posting.
    - Company name.
    - Role title.
    - 3–5 key skills/requirements they mention.
11. [ ] In `./docs/roles-and-skills.md`, in the `## Job market snapshot` section, write:

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

12. Follow the process for [Main tasks](#main-tasks) to complete the issue with a PR.

---

### 4. Peer review via PR

Create an issue:

- `[Task] Code review for Lab 01`
You will act as both **author** and **reviewer**.

1. As an **author**:
    - Create two **PRs** that:
        - Adds `docs/architecture.md` with the diagram.
        - Adds `src/roles-and-skills.md`.
    - Request a review from a collaborator for at least one of the PRs.
    - Use the [PR template](.github/pull_request_template.md) and make sure the PR descriptions are clear and links the relevant issue(s).
2. As a **reviewer**:
    - Review at least **one PR** from a collaborator.
    - Leave at least **2 meaningful comments** to improve your colleagues work, which they need to address. For example:
        - A question about architecture (“Why does the mobile app talk directly to the database?”).
        - Some important commonly-appearing skills weren't mentioned.
3. As an **author**, address the comments:
    - Make changes where reasonable.
    - Reply to comments with something like “Fixed in 123abc” (123abc being the commit id) or explain why you disagree.
4. When both sides are happy, **merge the PR**.

> 💡 **LLM check:**
>
> - You can ask an LLM “how to phrase a polite review comment”,  
>     but you must read your collaborator’s work and think of **real feedback**.
>
---

### 5. Short personal reflection

Create an issue:

- `[Task] Personal reflection – Lab 01`

1. In `src/reflection.md` write 5–10 sentences answering:
    - Which role did you choose and why?
    - What is one thing about the product’s architecture that was new to you?
    - Which course topics (Git, Linux, Docker, REST, CI/CD, fullstack, data) seem most relevant to your chosen role?
    - What is one concrete skill you would like to improve this semester?
2. Commit, push, and (optionally) open a small PR, or add it to an existing one.

> 💡 **LLM check:**
>
> - Write this section **without** an LLM. It’s about your own thoughts.
>
---

### 6. Stretch tasks (optional)

If you finish early:

- Add a second diagram showing **only backend services** and how they might scale (load balancer, multiple service instances, database).
- Create a file `src/agent-idea.md`:
  - Sketch how an “agent/script” could:
    - Read `LAB_STORY.md`,
    - Generate GitHub issues automatically via API,
    - Create initial markdown files for you.
- Try to implement a tiny part of that agent (even just a script that reads this file and prints task titles).

---

### Submission checklist

Report each task to the TA when you’re done:

- The tasks must have an **issue** linked to PRs.
- Close the issue when all related activities (including TA approval) are done.
- Explain your diagram, chosen role in a short conversation with the TA.
