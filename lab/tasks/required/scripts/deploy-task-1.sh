#!/bin/bash
# Task 1: VM Deployment Script
# Run this script ONCE you are SSH connected to your VM

set -e

echo "========================================"
echo "Task 1: Deploying Backend to VM"
echo "========================================"

# Navigate to project
echo "[1/5] Navigating to se-toolkit-lab-4..."
cd ~/se-toolkit-lab-4 || {
    echo "Error: se-toolkit-lab-4 directory not found!"
    echo "Please clone the repository first:"
    echo "  git clone <your-fork-url> se-toolkit-lab-4"
    exit 1
}

# Pull latest changes
echo "[2/5] Pulling latest changes..."
git pull

# Create environment file if not exists
echo "[3/5] Setting up environment file..."
if [ ! -f .env.docker.secret ]; then
    cp .env.docker.example .env.docker.secret
    echo "Created .env.docker.secret from example"
else
    echo ".env.docker.secret already exists"
fi

# Update CADDY_HOST_ADDRESS
echo "[4/5] Configuring CADDY_HOST_ADDRESS..."
sed -i 's/CADDY_HOST_ADDRESS=127.0.0.1/CADDY_HOST_ADDRESS=0.0.0.0/' .env.docker.secret
echo "Set CADDY_HOST_ADDRESS=0.0.0.0"

# Start containers
echo "[5/5] Starting Docker containers..."
docker compose --env-file .env.docker.secret up --build -d

echo ""
echo "========================================"
echo "Deployment Complete!"
echo "========================================"
echo ""
echo "Verifying containers..."
docker compose --env-file .env.docker.secret ps

echo ""
echo "Next steps:"
echo "1. Open Swagger UI: http://<YOUR_VM_IP>:42002/docs"
echo "2. Open pgAdmin: http://<YOUR_VM_IP>:42003"
echo ""
echo "API Key: my-secret-api-key"
echo "pgAdmin: admin@example.com / admin"
