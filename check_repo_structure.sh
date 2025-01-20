#!/bin/bash
if [ ! -f "README.md" ]; then
    echo "ERROR: README.md is missing"
    exit 1
fi
if [ ! -d "src" ]; then
    echo "ERROR: src directory is missing"
    exit 1
fi
if [ ! -f "src/main.py" ]; then
    echo "ERROR: src/main.py is missing"
    exit 1
fi
echo "Repository structure is correct"
