# Task 1: Observe System Component Interaction - Complete Guide

This guide contains everything you need to complete Task 1.

---

## Quick Reference

| Item | Value |
|------|-------|
| **VM IP Address** | Get from: https://vm.innopolis.university → Your VM → Dashboard → IP Address |
| **Swagger UI** | `http://<VM_IP>:42002/docs` |
| **pgAdmin** | `http://<VM_IP>:42003` |
| **API Key** | `my-secret-api-key` |
| **pgAdmin Email** | `admin@example.com` |
| **pgAdmin Password** | `admin` |

---

## Step 1: Create GitHub Issue

1. Go to your GitHub repository: `https://github.com/YOUR_USERNAME/se-toolkit-lab-4/issues`
2. Click **New issue**
3. Select **Lab Task** template
4. Fill in:
   - **Title**: `[Task] Observe System Component Interaction`
   - **Description**: 
     ```
     Trace a request from Swagger through the API to the database using browser developer tools and pgAdmin.
     ```
   - **Plan**:
     ```
     - [ ] Deploy the back-end to the VM
     - [ ] Open Swagger UI and authorize
     - [ ] Send POST /interactions request
     - [ ] Observe request in browser Network tab
     - [ ] Verify data in pgAdmin
     - [ ] Take screenshots and add comment
     ```
5. Click **Submit new issue**

---

## Step 2: Deploy to VM

### 2.1 Connect to VM

Open VS Code Terminal and run:

```bash
ssh se-toolkit-vm
```

If you haven't configured SSH yet, use:
```bash
ssh root@<YOUR_VM_IP>
```

### 2.2 Pull Latest Code

```bash
cd se-toolkit-lab-4 && git pull
```

### 2.3 Create Environment File

```bash
cp .env.docker.example .env.docker.secret
```

### 2.4 Edit Environment File

```bash
nano .env.docker.secret
```

Find this line:
```
CADDY_HOST_ADDRESS=127.0.0.1
```

Change it to:
```
CADDY_HOST_ADDRESS=0.0.0.0
```

Save: Press `Ctrl+X`, then `Y`, then `Enter`

### 2.5 Start Containers

```bash
docker compose --env-file .env.docker.secret up --build -d
```

### 2.6 Verify Containers Running

```bash
docker compose --env-file .env.docker.secret ps
```

You should see 4 containers: `app`, `postgres`, `pgadmin`, `caddy` - all with status "running"

---

## Step 3: Open Swagger UI

1. Open browser and go to: `http://<YOUR_VM_IP>:42002/docs`
2. Click the **lock icon** (Authorize) in the top right
3. Enter API key: `my-secret-api-key`
4. Click **Authorize**, then **Close**

---

## Step 4: Open Browser Developer Tools

1. Press `F12` (or `Ctrl+Shift+I`)
2. Click the **Network** tab
3. Keep this open - you'll see the API request appear here

---

## Step 5: Send POST Request

### 5.1 In Swagger UI

1. Find and expand **POST /interactions**
2. Click **Try it out**
3. Enter this JSON:
   ```json
   {
     "learner_id": 1,
     "item_id": 1,
     "kind": "attempt"
   }
   ```
4. Click **Execute**

### 5.2 In Browser DevTools (Network Tab)

You should see a request to `/interactions` appear. Click on it and observe:

- **Headers tab**: 
  - Request URL: `http://<VM_IP>:42002/interactions/`
  - Request Method: `POST`
  - Status Code: `201`
- **Payload tab**: Your JSON body
- **Response tab**: The created interaction with an `id`

> ⚠️ **TAKE SCREENSHOT NOW** - Capture the Network tab showing the request and response

---

## Step 6: Verify in pgAdmin

### 6.1 Open pgAdmin

1. Go to: `http://<YOUR_VM_IP>:42003`
2. Login:
   - Email: `admin@example.com`
   - Password: `admin`

### 6.2 Run Query

1. Expand **Servers** → **PostgreSQL 17** → **Databases** → **lab-4**
2. Right-click **lab-4** → **Query Tool**
3. Enter this SQL:
   ```sql
   SELECT * FROM interacts ORDER BY id DESC LIMIT 5;
   ```
4. Click the **play button** (Execute)

You should see your new interaction at the top of the results.

> ⚠️ **TAKE SCREENSHOT NOW** - Capture pgAdmin showing the query results with your new row

---

## Step 7: Send Another Request

### 7.1 In Swagger UI

Send another POST with different values:
```json
{
  "learner_id": 2,
  "item_id": 3,
  "kind": "view"
}
```

### 7.2 In pgAdmin

Re-run the same SQL query:
```sql
SELECT * FROM interacts ORDER BY id DESC LIMIT 5;
```

Verify the new row appears.

---

## Step 8: Create Issue Comment

### 8.1 Prepare Screenshots

You need 2 screenshots:
1. **Browser DevTools** - Network tab showing POST /interactions request and response
2. **pgAdmin** - Query results showing the database row(s)

### 8.2 Add Comment to Issue

1. Go to your GitHub issue
2. In the comment box, paste this template and add your screenshots:

---

```markdown
## Task Completion Evidence

### Screenshot 1: Browser Developer Tools (Network Tab)

![Network Tab Screenshot](./screenshots/network-tab.png)

The HTTP request shows:
- **Method**: POST
- **URL**: http://<VM_IP>:42002/interactions/
- **Status**: 201 Created
- **Request Body**: `{"learner_id": 1, "item_id": 1, "kind": "attempt"}`

### Screenshot 2: pgAdmin Database Verification

![pgAdmin Screenshot](./screenshots/pgadmin.png)

The database query shows the interaction was stored:
- **Table**: interacts
- **Query**: `SELECT * FROM interacts ORDER BY id DESC LIMIT 5;`
- **Result**: New row with learner_id=1, item_id=1, kind=attempt

### Summary

Data flow confirmed: Browser → API (FastAPI) → Database (PostgreSQL)
```

---

### 8.3 Upload Screenshots

1. Drag and drop your screenshots into the comment box
2. GitHub will upload them and create markdown links
3. Update the template above with the actual image links

### 8.4 Close the Issue

1. Click **Close issue** button
2. Task complete! ✅

---

## Troubleshooting

### Containers not starting
```bash
# Check logs
docker compose --env-file .env.docker.secret logs

# Restart
docker compose --env-file .env.docker.secret down
docker compose --env-file .env.docker.secret up --build -d
```

### Cannot access Swagger UI
- Verify VM IP is correct
- Check firewall allows port 42002
- Ensure `CADDY_HOST_ADDRESS=0.0.0.0` in `.env.docker.secret`

### API returns 401 Unauthorized
- Click the lock icon in Swagger UI
- Enter API key: `my-secret-api-key`

### pgAdmin won't connect
- Verify containers are running: `docker compose ps`
- Check port 42003 is accessible
