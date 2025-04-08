#!/bin/bash

echo "🚀 Pushing Modular Research Suite to GitHub..."

# Set working directory to script location
cd "$(dirname "$0")"

# Initialize if not already a git repo
if [ ! -d .git ]; then
  git init
fi

# Set remote (only if not already configured)
if ! git remote get-url origin > /dev/null 2>&1; then
  read -p "Enter your GitHub repo URL (e.g. https://github.com/yourname/repo.git): " repo
  git remote add origin "$repo"
fi

git add .
git commit -m "Initial commit: Modular Research Suite Phase 4"
git branch -M main
git push -u origin main

echo "✅ Push complete. Your research suite is now live on GitHub."
