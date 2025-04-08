#!/bin/bash

# This script sets macOS Keychain to store your GitHub token securely
echo "🔐 Configuring Git to store credentials in macOS Keychain..."
git config --global credential.helper osxkeychain

echo "✅ Done! Next time you push to GitHub:"
echo "1. Enter your GitHub username."
echo "2. Paste your Personal Access Token instead of password."
echo "🔁 It will be saved securely in your macOS Keychain."

echo "🔍 To verify:"
echo "git config --global credential.helper"
