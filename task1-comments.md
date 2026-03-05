## Comment 1: Request as fetch code

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

---

## Comment 2: Response as JSON

```json
{
  "email": "john-doe@email.com",
  "name": "John Doe",
  "id": 6,
  "enrolled_at": "2026-03-05T17:28:37.214333"
}
```

---

## Comment 3: Data output from pgAdmin (CSV)

```csv
id,name,email,enrolled_at
6,John Doe,john-doe@email.com,2026-03-05 17:28:37.214333
5,Eve Adams,eve@example.com,2025-10-15 11:00:00
4,Diana Prince,diana@example.com,2025-10-01 08:30:00
3,Charlie Brown,charlie@example.com,2025-09-15 10:00:00
2,Bob Smith,bob@example.com,2025-09-01 09:15:00
```

---

## Comment 4: ERD from pgAdmin

Database: lab-4

Tables:
- **learner** (id, name, email, enrolled_at)
- **item** (id, type, name, description)
- **interacts** (id, learner_id, item_id, kind, created_at)

Relationships:
- learner 1--* interacts
- item 1--* interacts

> Note: Please see the attached screenshot from pgAdmin showing the ERD diagram in Chen notation with all three tables and their relationships.

---

## Task Completion

All acceptance criteria met:
- ✅ Deployed back-end to VM
- ✅ Swagger UI accessible at http://10.93.25.246:42002/docs
- ✅ Sent POST /learners/ request successfully (201 Created)
- ✅ Verified data in pgAdmin (learner table)
- ✅ Added all 4 required comments with artifacts
