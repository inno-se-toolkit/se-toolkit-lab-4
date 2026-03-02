-- Task 1: pgAdmin Queries for Verifying Interactions
-- Run these queries in pgAdmin Query Tool

-- =====================================================
-- Query 1: View latest 5 interactions (main verification)
-- =====================================================
SELECT * FROM interacts ORDER BY id DESC LIMIT 5;

-- =====================================================
-- Query 2: View all interactions with details
-- =====================================================
SELECT 
    i.id,
    i.learner_id,
    l.name AS learner_name,
    l.email AS learner_email,
    i.item_id,
    it.title AS item_title,
    it.type AS item_type,
    i.kind,
    i.created_at
FROM interacts i
JOIN learner l ON i.learner_id = l.id
JOIN item it ON i.item_id = it.id
ORDER BY i.id DESC;

-- =====================================================
-- Query 3: Count interactions by kind
-- =====================================================
SELECT kind, COUNT(*) as count 
FROM interacts 
GROUP BY kind 
ORDER BY count DESC;

-- =====================================================
-- Query 4: Find interactions for specific learner
-- =====================================================
-- Change learner_id to filter by different learner
SELECT * FROM interacts WHERE learner_id = 1 ORDER BY id DESC;

-- =====================================================
-- Query 5: Find interactions for specific item
-- =====================================================
-- Change item_id to filter by different item
SELECT * FROM interacts WHERE item_id = 1 ORDER BY id DESC;
