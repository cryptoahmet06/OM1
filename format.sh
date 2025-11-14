#!/bin/bash
files=$(git diff --name-only origin/main...HEAD | grep '\.py$')
if [ -z "$files" ]; then
    echo "No Python files changed."
    exit 0
fi
echo "$files" | xargs ruff check --fix
echo "$files" | xargs isort
echo "$files" | xargs black
echo "Done!"
