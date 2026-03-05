# Task 1: Observe System Component Interaction - Complete Guide

## Issue to Create on GitHub

**Go to:** https://github.com/vanya630/se-toolkit-lab-4/issues/new

**Title:** `[Task] Observe System Component Interaction`

**Body:**
```
## Purpose
Trace a request from Swagger UI through the API to the database using browser developer tools and pgAdmin.

## Acceptance Criteria
- [ ] Deployed back-end to VM
- [ ] Swagger UI accessible and returns 200
- [ ] POST /learners/ request sent successfully
- [ ] Data verified in pgAdmin
- [ ] 4 comments added with required artifacts
- [ ] Issue closed
```

---

## Comments to Add to the Issue

### Comment 1: Request as fetch code

```js
fetch("http://10.93.25.246:42002/learners/", {
  "headers": {
    "accept": "application/json",
    "authorization": "Bearer my-secret-api-key",
    "content-type": "application/json"
  },
  "body": "{\"name\":\"John Doe\",\"email\":\"john-doe@email.com\"}",
  "method": "POST",
  "mode": "cors"
});
```

### Comment 2: Response as JSON

```json
{
  "email": "john-doe@email.com",
  "name": "John Doe",
  "id": 6,
  "enrolled_at": "2026-03-05T17:28:37.214333"
}
```

### Comment 3: Data output from pgAdmin (CSV)

Attach the file: `learner-data.csv`

Content:
```csv
id,name,email,enrolled_at
6,John Doe,john-doe@email.com,2026-03-05 17:28:37.214333
5,Eve Adams,eve@example.com,2025-10-15 11:00:00
4,Diana Prince,diana@example.com,2025-10-01 08:30:00
3,Charlie Brown,charlie@example.com,2025-09-15 10:00:00
2,Bob Smith,bob@example.com,2025-09-01 09:15:00
```

### Comment 4: ERD Screenshot

**You need to take this screenshot:**

1. Open pgAdmin: http://10.93.25.246:42003
2. Login: `admin@example.com` / `admin`
3. Connect to `postgres-lab-4` server
4. Right-click on `lab-4` database
5. Click **ERD for Database** (or Tools → ERD Tool)
6. Take a screenshot showing all 3 tables:
   - `learner` (id, name, email, enrolled_at)
   - `item` (id, type, name, description)
   - `interacts` (id, learner_id, item_id, kind, created_at)
7. Paste the screenshot in Comment 4

---

## Final Steps

1. Add all 4 comments to the issue
2. Attach the `learner-data.csv` file to Comment 3
3. Paste ERD screenshot in Comment 4
4. Add final comment: "Task completed. All acceptance criteria met."
5. Click **Close issue**

---

## Verification

Test Swagger UI:
```bash
curl -s -o /dev/null -w "%{http_code}" http://10.93.25.246:42002/docs
# Should return: 200
```

Test API endpoint:
```bash
curl -s -X POST "http://10.93.25.246:42002/learners/" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer my-secret-api-key" \
  -d '{"name": "Test User", "email": "test@email.com"}'
```

---

## Files Created

- `task1-comments.md` - All comment templates
- `learner-data.csv` - CSV export for Comment 3
- `TASK1-COMPLETE-GUIDE.md` - This file
