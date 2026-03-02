# Task 1: What You Need to Do Manually

I've prepared everything I can automate. Here are the **manual steps you must complete**:

---

## Files I Created For You

| File | Purpose |
|------|---------|
| `TASK-1-GUIDE.md` | Complete step-by-step guide with all commands |
| `lab/tasks/required/scripts/deploy-task-1.sh` | Auto-deploy script for VM |
| `lab/tasks/required/scripts/task-1-queries.sql` | SQL queries for pgAdmin |
| `lab/tasks/required/templates/task-1-issue-comment.md` | Issue comment template |
| `.env.docker.secret` | Environment file (ready to use) |

---

## Your Manual Checklist

### ✅ Step 1: Create GitHub Issue (2 minutes)

1. Go to: `https://github.com/YOUR_USERNAME/se-toolkit-lab-4/issues/new`
2. Title: `[Task] Observe System Component Interaction`
3. Use the template in `TASK-1-GUIDE.md` Step 1
4. Click **Submit new issue**

---

### ✅ Step 2: Deploy to VM (5 minutes)

**Option A - Use my auto-deploy script:**

```bash
# 1. Connect to VM
ssh se-toolkit-vm

# 2. Run the deployment script
bash ~/se-toolkit-lab-4/lab/tasks/required/scripts/deploy-task-1.sh
```

**Option B - Manual commands:**

```bash
# 1. Connect to VM
ssh se-toolkit-vm

# 2. Navigate and pull
cd se-toolkit-lab-4 && git pull

# 3. Setup environment
cp .env.docker.example .env.docker.secret
sed -i 's/CADDY_HOST_ADDRESS=127.0.0.1/CADDY_HOST_ADDRESS=0.0.0.0/' .env.docker.secret

# 4. Start containers
docker compose --env-file .env.docker.secret up --build -d

# 5. Verify
docker compose --env-file .env.docker.secret ps
```

---

### ✅ Step 3: Test API in Swagger (3 minutes)

1. Open browser: `http://<YOUR_VM_IP>:42002/docs`
2. Click lock icon → Enter API key: `my-secret-api-key`
3. Expand **POST /interactions** → **Try it out**
4. Enter:
   ```json
   {"learner_id": 1, "item_id": 1, "kind": "attempt"}
   ```
5. Click **Execute**

---

### ✅ Step 4: Open DevTools & Take Screenshot (2 minutes)

1. Press `F12` → Go to **Network** tab
2. Find the `/interactions` request
3. Click it → Verify:
   - Headers: POST, Status 201
   - Payload: Your JSON
   - Response: Created interaction
4. **Take screenshot** (Win+Shift+S or Cmd+Shift+4)

---

### ✅ Step 5: Verify in pgAdmin (3 minutes)

1. Open: `http://<YOUR_VM_IP>:42003`
2. Login: `admin@example.com` / `admin`
3. Navigate: Servers → PostgreSQL 17 → lab-4
4. Right-click **lab-4** → **Query Tool**
5. Paste this query:
   ```sql
   SELECT * FROM interacts ORDER BY id DESC LIMIT 5;
   ```
6. Click **Execute** (play button)
7. **Take screenshot** of results

---

### ✅ Step 6: Second Request (1 minute)

1. In Swagger, send another POST:
   ```json
   {"learner_id": 2, "item_id": 3, "kind": "view"}
   ```
2. Re-run SQL query in pgAdmin
3. Verify new row appears

---

### ✅ Step 7: Comment & Close Issue (2 minutes)

1. Go to your GitHub issue
2. Copy template from: `lab/tasks/required/templates/task-1-issue-comment.md`
3. Paste into comment box
4. Drag & drop both screenshots into the comment
5. Click **Comment**
6. Click **Close issue**

---

## Total Time: ~18 minutes

---

## Quick Reference Card

```
┌─────────────────────────────────────────────────────────┐
│  VM IP:           http://<YOUR_VM_IP>                   │
│  Swagger UI:      http://<YOUR_VM_IP>:42002/docs        │
│  pgAdmin:         http://<YOUR_VM_IP>:42003             │
│  API Key:         my-secret-api-key                     │
│  pgAdmin Email:   admin@example.com                     │
│  pgAdmin Pass:    admin                                 │
└─────────────────────────────────────────────────────────┘
```

---

## If Something Goes Wrong

| Problem | Solution |
|---------|----------|
| Can't SSH to VM | Check VM is running at vm.innopolis.university |
| Swagger won't load | Verify `CADDY_HOST_ADDRESS=0.0.0.0` in .env.docker.secret |
| 401 Unauthorized | Click lock icon in Swagger, enter API key |
| Containers not running | Run: `docker compose --env-file .env.docker.secret logs` |
| pgAdmin won't connect | Check container status: `docker compose ps` |

---

## Need Help?

1. Read the full guide: `TASK-1-GUIDE.md`
2. Check SQL queries: `lab/tasks/required/scripts/task-1-queries.sql`
3. Ask a TA or classmate!
