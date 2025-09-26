#!/bin/bash

# The absolute path to your project directory
PROJECT_DIR="/path/to/your/makepdf/project"

# Change to the project directory and run the command
(cd "$PROJECT_DIR" && uv run makepdf "$@")
