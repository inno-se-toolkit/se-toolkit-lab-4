# Lab 01 – Products, Architecture & Roles

To kickstart the course, you will explore two things:
> 1) How real software products are structured;
> 2) What kind of engineers build and operate them.

By the end of this lab you should be able to:

- Explain the basic architecture of a real-world digital product in terms of modules, data flow, and deployment.
    
- Identify which tech roles work on which parts of that product, and which general skills are shared across roles.
    
- Use GitHub issues, branches, and pull requests to structure your work and get a peer review.

To complete this lab, you will:
- Pick an existing digital product.
- Sketch its architecture: modules, data flow, deployment.
- Map modules to tech roles and skills, using real job postings and roadmap.sh.
- Practice using GitHub issues, branches and pull requests to organize your work and get feedback.

This and all other lab assignments will simulate the engineering practices in a real team:
follow processes, communicate via issues/PRs, and keep the work reviewable.

---

## How the lab works (the overall flow)

For starters, **fork** this repo to your GitHub account.

For each task below you need to:
   - Create an **issue**.
   - Implement the task on a **feature branch**.
   - Open a **Pull Request**.
   - Assign the classmate in the PR as the reviewer.
   - After the review, make the necessary changes and get the classmate to approve the PR.
   - Merge the PR to the `main` branch.
   - Close the issue.
At the end:
   - Be ready to demonstrate the completed tasks to the TA.


## Repo structure

- `.github/ISSUE_TEMPLATE` – templates for your issues.
- `.github/pull_request_template.md` – checklist for PRs.
- `src/` – place for any code/scripts/config.


## Tasks

> 🔁 _Reminder: every non-trivial task should have **its own GitHub issue** created from templates in `.github/ISSUE_TEMPLATE`._

You work **independently** on your own repo, but you will ask a classmate to **review your work via a PR**.

---

### 0. Setup

Create an issue called `[Task] Lab 01 setup`

Copy the following steps to the issue:

- [ ] Add a classmate to the repo as a collaborator in Settings.
- [ ] On your machine, configure git if needed:

  ```bash
  git config --global user.name "Your Name"
  git config --global user.email "your@email"
  ```

- [ ] Clone the repo to your laptop.
- [ ] Skim this `README.md` file once so you know what’s coming.
    

_When the steps are done, check them off inside the issue, and eventually close the issue._

_This Setup task does not require a review by a classmate_.

---

### 1. Pick a product & describe its architecture (text)

Create an issue:

- `[Task] Product & architecture description`
    

Work in branch `feature/architecture` (or similar).

1. In `docs/architecture.md`, write:
    
    1. **Product choice (5–7 sentences)**
        
        - Pick one product from this list or propose your own:
            
            - Yandex Taxi
                
            - Telegram
                
            - ChatGPT
                
            - Wildberries

            - Uchi.ru
                
            - Any other widely used fullstack app (agree with TA if picking this option).
                
        - Explain why you personally would be interested to work on this product as a tech specialist.
            
    2. **Modules & data flow**
        
        - Describe the main system **modules** in your own words. For example:
            
            - Mobile app
                
            - Backend API
                
            - Authentication service
                
            - Payment / billing
                
            - Notifications
                
            - Admin panel
                
            - Data analytics
                
        - For each module:
            
            - 1–2 sentences: what it does.
                
        - Then add a short section “**Data flow**”:
            
            - Describe what happens when a typical user action occurs (e.g. user orders a taxi / sends a message).
                
            - Mention which modules talk to each other and what kind of data they exchange.
                
    3. **Deployment (high level)**
        
        - Briefly describe **where** these modules live:
            
            - On user devices (mobile/web).
                
            - On servers (backend services, databases).
                
            - In the cloud (if you know/guess).
                
    4. **Uncertainties (very important)**
        
        - Add a section:
            
            ```markdown
            ## Things I am not sure about
            
            1. ...
            2. ...
            ```
            
            Write at least two things in your architecture that you are not fully sure about (guesses, questions, etc.).
            
2. Commit your changes with a clear message, e.g.:
    
    ```bash
    git checkout -b feature/architecture
    git add docs/architecture.md
    git commit -m "describe modules and data flow for <product>"
    git push -u origin feature/architecture
    ```
    
3. Open a **Pull Request** to `main`:
    
    - Link it to the issue (`Closes #<issue_number>`).
        
    - Request a review from a classmate.
        
4. Continue with next tasks, the reviews will be done in Task 4.
    
---

### 2. Draw the architecture diagram

Create an issue:

- `[Task] Architecture diagram`
    

Work on the same product.

1. Using **draw.io**, draw a diagram that shows:
    
    - Main modules as boxes.
        
    - Arrows showing how data flows between them for a typical user action.
        
    - A separation (if possible) between:
        
        - Client-side (mobile/web).
            
        - Server-side services.
            
        - Data storage (databases, caches, etc.).
            
2. Export the diagram to **PNG or SVG** and save as:
    
    - `diagrams/architecture.png` (or `.svg`)
        
    
    If your tool supports it, also save the **source file**:
    
    - `diagrams/architecture.drawio` (or equivalent).
        
3. Add a short caption inside `docs/architecture.md`:
    
    ```markdown
    ## Diagram
    
    See `diagrams/architecture.png` for a visual representation of the modules and data flow.
    ```
    
4. Commit and push your changes on the same branch to extend the PR.
    

> 💡 **LLM check:**
> 
> - LLMs can help you **decide what boxes/arrows to include**, but the **diagram must be drawn by you**.
>     
> - The TA will ask you to verbally explain the diagram.
>     

---

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
>     - You must visit roadmap.sh and real job postings yourself.
>         
>     - Your reflections about what you have / don’t have must be honest and personal.
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
            
    - Request a review from a classmate for at least one of the PRs.
        
    - Use the [PR template](.github/pull_request_template.md) and make sure the PR descriptions are clear and links the relevant issue(s).
        
2. As a **reviewer**:
    
    - Review at least **one PR** from a classmate.
        
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
>     but you must read your classmate’s work and think of **real feedback**.
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

-  Add a second diagram showing **only backend services** and how they might scale (load balancer, multiple service instances, database).
    
-  Create a file `src/agent-idea.md`:
    
    - Sketch how an “agent/script” could:
        
        - Read `LAB_STORY.md`,
            
        - Generate GitHub issues automatically via API,
            
        - Create initial markdown files for you.
            
-  Try to implement a tiny part of that agent (even just a script that reads this file and prints task titles).
    

---

### Submission checklist

Report each task to the TA when you’re done:

-  The tasks must have an **issue** linked to PRs.
    
-  Close the issue when all related activities (including TA approval) are done.
    
-  Explain your diagram, chosen role in a short conversation with the TA.

