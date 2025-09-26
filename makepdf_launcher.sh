#!/bin/bash

# The absolute path to your project directory
PROJECT_DIR="/Users/gauden/dev/makepdf"

# Change to the project directory and run the command
(cd "$PROJECT_DIR" && uv run makepdf "$@")
