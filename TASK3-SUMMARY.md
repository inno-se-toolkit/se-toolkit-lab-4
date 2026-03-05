# Task 3: Add Front-end - Summary

## Completed Steps

### Part A: Dev version
- ✅ Set up frontend environment (`.env` file)
- ✅ Installed dependencies with `npm install`
- ✅ Ran dev server with `npm run dev`
- ✅ Frontend accessible at `http://localhost:5173/`

### Part B: Production version
- ✅ Deployed frontend to VM
- ✅ Rebuilt caddy service: `docker compose --env-file .env.docker.secret up --build caddy -d`
- ✅ Frontend served at `http://10.93.25.246:42002/`

### Part C: Type Filter Feature
- ✅ Added type filter dropdown with "All" option
- ✅ Filter derives unique types from loaded items dynamically
- ✅ Table rows filtered by selected type
- ✅ Committed with message: `feat: add type filter to the front-end table`

## Changes Made

### frontend/src/App.tsx
- Added `selectedType` state to track filter selection
- Added `uniqueTypes` derived from items array
- Added `filteredItems` that filters based on selected type
- Added filter dropdown UI with "All" option

## Acceptance Criteria

- [x] Issue has correct title: `[Task] Add Front-end`
- [x] Type filter control added to frontend/src/App.tsx
- [x] "All" option exists in type filter
- [x] Rows filtered by selected type
- [x] Commit message: `feat: add type filter to the front-end table`
- [x] Frontend runs locally with npm run dev
- [x] Production build deployed on VM and served by Caddy
- [ ] PR created and approved
- [ ] Issue closed by PR

## PR

PR: https://github.com/vanya630/se-toolkit-lab-4/pull/X (to be created)

---

**Closes #3**
