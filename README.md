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
      1. [x] Restrict deletions
      2. [x] Require a pull request before merging:
         1. Required approvals: `1`
         2. Require conversation resolution before merging
         3. Allowed merge methods: `Merge`.
      3. [x] Block force pushes
7. In the repo Settings -> Collaborators -> Add people, add a classmate as a collaborator.
8. Make sure your collaborator have accepted the invitation sent to their email.

9. (If needed) On your computer, configure [`git`](https://git-scm.com/):

    ```bash
    git config --global user.name "Your Name"
    git config --global user.email "your@email"
    ```

10. (Recommended) Install [`VS Code`](https://code.visualstudio.com/).
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
- [Create](https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/creating-a-branch-for-an-issue) a new branch for the issue.
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

### 1. Pick a product & describe its architecture (text)

> [!NOTE]
>
> If you use PlantUML, you can render it to PNG/SVG using the [PlantUML VS Code extension](https://marketplace.visualstudio.com/items?itemName=jebbs.plantuml).
>
> If you use Mermaid, just include the code in a Markdown code block with the `mermaid` language tag (see [docs](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/creating-diagrams#creating-mermaid-diagrams)).

1. [ ] Create an issue `[Task] Product & architecture description`.
2. [ ] Create a branch for it.
3. [ ] Switch to that branch.
4. [ ] Create the `docs/` directory if it doesn't exist.
5. [ ] Create `docs/architecture.md`:
     1. [ ] In the `## Product choice` section:
         - [ ] Pick one product from this list or propose your own:
             - Yandex Taxi
             - Telegram
             - ChatGPT.com
             - Wildberries.ru
             - Uchi.ru
             - Any other widely used full-stack app (agree with TA if picking this option).
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
         - [ ] Provide a [component diagram](https://en.wikipedia.org/wiki/Component_diagram) in [`PlantUML`](https://plantuml.com/component-diagram) (see [how to draw a connection](https://stackoverflow.com/questions/55077828/using-required-provided-interfaces-in-component-diagrams-plantuml/57134601#57134601)). Save the PlantUML code in `docs/diagrams/architecture-component.puml` and render it to PNG/SVG format.
     4. [ ] In the `## Data flow` section:
             - Describe what happens when a typical user action occurs (e.g. user orders a taxi / sends a message).
             - Mention which modules talk to each other and what kind of data they exchange.
             - Provide a [sequence diagram](https://en.wikipedia.org/wiki/Sequence_diagram) in [`PlantUML`](https://plantuml.com/sequence-diagram) or [`Mermaid`](https://mermaid.js.org/syntax/sequenceDiagram.html). Store the diagram source code in `docs/diagrams/architecture-sequence.puml` and the rendered image in `docs/images/`.
     5. [ ] In the `## Deployment` section:
         - [ ] Briefly describe where these modules live (high-level view):
             - On user devices (mobile/web app).
             - On servers (backend services, databases).
         - [ ] Provide a [deployment diagram](https://en.wikipedia.org/wiki/Deployment_diagram) in [`PlantUML`](https://plantuml.com/deployment-diagram) or [`Mermaid`](https://mermaid.js.org/syntax/c4.html#c4-deployment-diagram-c4deployment). Store the diagram source code in `docs/diagrams/architecture-deployment.puml` and the rendered image in `docs/images/`.
     6. [ ] In the `## Knowledge Gaps` section:
             - [ ] Write at least two things in your architecture that you are not fully sure about (guesses, questions, etc.).
6. [ ] Commit your changes with a clear message using one of these methods:
   - Method 1: Activity Bar -> Source Control
   - Method 2: `git` CLI (replace `your-branch` with an actual branch name):

        ```bash
        git checkout -b your-branch
        git add docs
        git commit -m "feat(docs): describe high-level architecture of <product>"
        git push -u origin your-branch
        ```

7. [ ] Open a PR to `main`:
    - [ ] [Link the PR](https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/linking-a-pull-request-to-an-issue#linking-a-pull-request-to-an-issue-using-a-keyword) to the issue, e.g. `Closes #<issue number>`.
    - [ ] Request a review from the collaborator.

### 3. Roles, skills, roadmap.sh & job postings

Create an issue:

- `[Task] Roles and skills mapping`
Work in branch `feature/roles-skills`.

1. In `src/roles-and-skills.md`, add the following sections.

   #### 3.1 Roles per module

    - For each major module from `architecture.md`, list **which tech roles** are likely involved.
        - Example: `Backend API` → backend engineer, DevOps, QA engineer, product manager.
    - Use a simple table:

        ```markdown
        | Module            | Roles involved                         |
        |-------------------|----------------------------------------|
        | Mobile app        | Mobile engineer (iOS/Android), QA     |
        | Backend API       | Backend engineer, DevOps, QA          |
        | ...               | ...                                    |
        ```

   #### 3.2 Cross-cutting skills

    - Add a section:

        ```markdown
        ## Common skills across roles
        ```

    - Based on your intuition and some research, list **skills that almost everyone needs**, for example:
        - Git
        - Basic Linux usage
        - Understanding of HTTP / REST APIs
        - Communicating in a team
        - Writing clear issues/PR descriptions

   #### 3.3 Choose a role and visit roadmap.sh

    - Choose **one role** that seems most interesting to you now  
        (e.g. backend, DevOps, frontend, mobile, data engineer, etc.).
    - Go to [roadmap.sh](https://roadmap.sh/), find the relevant roadmap and sign in.
    - Spend a few minutes marking items you **already have at least some knowledge in**.
    - In your markdown file, write:

        ```markdown
        ## My chosen role
        
        - Role: <name>
        - Skills I already have (from roadmap.sh): ...
        - Skills I clearly lack (from roadmap.sh): ...
        ```

   #### 3.4 Job postings (Headhunter)

    - Find **2–3 job postings** for this role on Headhunter (or a similar job site).
    - For each posting, list:
        - Link to the posting.
        - Company name.
        - Role title.
        - 3–5 key skills/requirements they mention.
    - Then write a short comparison:

        ```markdown
        ## Job market snapshot
        
        - Skills that appear in almost every posting:
          - ...
        - Skills that surprised me:
          - ...
        - My key take away:
          - ...
        ```

2. Commit and push your changes, open a PR and link it to the issue.

> 💡 **LLM check:**
>
> - You can ask an LLM “what does a *role* usually do?”, but:
>
>   - You must visit roadmap.sh and real job postings yourself.
>
>   - Your reflections about what you have / don’t have must be honest and personal.
>
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
