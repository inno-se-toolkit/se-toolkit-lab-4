# Task 1: Complete Guide

## Step 1: Create GitHub Issue

1. Go to your fork: https://github.com/vanya630/se-toolkit-lab-4
2. Click **Issues** → **New issue**
3. Title: `[Task] Observe System Component Interaction`
4. Click **Submit new issue**
5. Keep the issue open - you'll add comments to it

---

## Step 2: Connect to VM and Deploy

Connect to your VM (IP: 10.93.25.246) using SSH. You may need to use Azure Portal or your SSH key.

### On the VM, run these commands:

```bash
# Clone your fork (if not already cloned)
cd ~
git clone https://github.com/vanya630/se-toolkit-lab-4.git
cd se-toolkit-lab-4

# Clean up Docker
docker rm -f $(docker ps -aq) 2>/dev/null || true
docker volume rm $(docker volume ls -q) 2>/dev/null || true

# Create environment file
cp .env.docker.example .env.docker.secret

# Start services
docker compose --env-file .env.docker.secret up --build -d

# Check services are running
docker compose --env-file .env.docker.secret ps
```

Wait for all services to show `Up` status (especially `postgres` should show `healthy`).

---

## Step 3: Open Swagger UI

1. Open browser: `http://10.93.25.246:42002/docs`
2. Click the **lock icon** (Authorize)
3. Enter API Key: `my-secret-api-key` (from .env.docker.secret)
4. Click **Authorize** → **Close**

---

## Step 4: Open Browser DevTools

1. Press `F12` (or right-click → Inspect)
2. Go to **Network** tab
3. Keep this tab open

---

## Step 5: Send POST Request via Swagger UI

1. In Swagger UI, find and expand `POST /learners/`
2. Click **Try it out**
3. Enter this JSON:
   ```json
   {
     "name": "John Doe",
     "email": "john-doe@email.com"
   }
   ```
4. Click **Execute**
5. You should see:
   - Code: `201`
   - Response body with `id`, `name`, `email`, `enrolled_at`

---

## Step 6: Copy Request as fetch (Comment 1)

1. In Network tab, click on the `learners` request
2. Right-click on the request → **Copy** → **Copy as fetch**
3. Go to your GitHub issue
4. Add a comment with this format:

```markdown
## Comment 1: Request as fetch code

```js
<paste the fetch code here>
```
```

---

## Step 7: Copy Response (Comment 2)

1. In Network tab, click on the `learners` request
2. Click **Response** tab
3. Copy the JSON response
4. Add another comment:

```markdown
## Comment 2: Response as JSON

```json
<paste the JSON response here>
```
```

---

## Step 8: Verify in pgAdmin (Comment 3)

1. Open pgAdmin: `http://10.93.25.246:42003`
2. Login with:
   - Email: `admin@example.com`
   - Password: `admin`
3. Connect to `postgres-lab-4` server
4. Navigate: Databases → db-lab-4 → public → Tables → learner
5. Right-click `learner` table → Query Tool
6. Run query:
   ```sql
   SELECT * FROM learner ORDER BY id DESC LIMIT 5;
   ```
7. Click the download icon (⬇️) to save as CSV
8. Save the file (e.g., `learner-data.csv`)
9. Add comment to issue and attach this CSV file

---

## Step 9: Get ERD Screenshot (Comment 4)

1. In pgAdmin, right-click on `db-lab-4` database
2. Click **ERD for Database** (or use Tools → ERD Tool)
3. Wait for the diagram to load with all 3 tables:
   - `learner`
   - `item`
   - `interacts` (or `interaction`)
4. Make a screenshot showing all tables
5. Add comment to issue and paste the screenshot

---

## Step 10: Close Issue

1. Add final comment: "Task completed. All acceptance criteria met."
2. Click **Close issue**

---

## Step 11: Check with Autochecker

Use the autochecker Telegram bot to verify your task completion.

---

## Acceptance Criteria Checklist

- [ ] Issue has correct title: `[Task] Observe System Component Interaction`
- [ ] Comment 1 includes request as fetch code
- [ ] Comment 2 includes response as JSON code
- [ ] Comment 3 includes CSV table with data from pgAdmin
- [ ] Comment 4 includes screenshot of ERD
- [ ] Issue is closed
