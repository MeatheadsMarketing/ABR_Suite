#!/bin/bash

# Navigate to the script's directory
cd "$(dirname "$0")"

# Optional: initialize README if missing
[ ! -f README.md ] && echo "# Deep Research Workflow" > README.md

# Git branch setup
git checkout -b main 2>/dev/null || git checkout main

# Add, commit, and push
git add .
git commit -m "Auto-push on $(date '+%Y-%m-%d %H:%M:%S')"
git push -u origin main
