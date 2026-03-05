#!/bin/bash
# Fix Script for Task 1 - Swagger UI not accessible

echo "=== Step 1: Navigate to repo ==="
cd ~/se-toolkit-lab-4 || { echo "Repo not found!"; exit 1; }

echo "=== Step 2: Stop and clean old containers ==="
docker compose --env-file .env.docker.secret down -v

echo "=== Step 3: Check .env.docker.secret exists ==="
if [ ! -f .env.docker.secret ]; then
    echo "Creating .env.docker.secret from template..."
    cp .env.docker.example .env.docker.secret
fi

echo "=== Step 4: Start all services ==="
docker compose --env-file .env.docker.secret up --build -d

echo "=== Step 5: Wait for services to start (30 seconds) ==="
sleep 30

echo "=== Step 6: Check service status ==="
docker compose --env-file .env.docker.secret ps

echo "=== Step 7: Check Caddy logs ==="
docker compose --env-file .env.docker.secret logs caddy --tail 20

echo "=== Step 8: Check App logs ==="
docker compose --env-file .env.docker.secret logs app --tail 20

echo "=== Done! ==="
echo "Now open in browser: http://10.93.25.246:42002/docs"
