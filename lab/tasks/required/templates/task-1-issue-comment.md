## Task Completion Evidence

### Screenshot 1: Browser Developer Tools (Network Tab)

<!-- Replace this line with your actual screenshot -->
<!-- Drag and drop your screenshot into GitHub to upload it -->

The HTTP request shows:
- **Method**: POST
- **URL**: `http://<VM_IP>:42002/interactions/`
- **Status Code**: 201 Created
- **Request Body**: `{"learner_id": 1, "item_id": 1, "kind": "attempt"}`

### Screenshot 2: pgAdmin Database Verification

<!-- Replace this line with your actual screenshot -->
<!-- Drag and drop your screenshot into GitHub to upload it -->

The database query shows the interaction was stored:
- **Table**: `interacts`
- **Query**: `SELECT * FROM interacts ORDER BY id DESC LIMIT 5;`
- **Result**: New row with `learner_id=1`, `item_id=1`, `kind=attempt`

### Summary

Data flow confirmed: **Browser** → **API (FastAPI)** → **Database (PostgreSQL)**

---

**Acceptance Criteria Checklist:**
- [x] Issue has the correct title: `[Task] Observe System Component Interaction`
- [x] Issue comment includes screenshot of browser DevTools showing HTTP request/response
- [x] Issue comment includes screenshot of pgAdmin showing database row
- [x] Issue is closed
