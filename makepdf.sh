#!/bin/bash

# Get the directory of the script
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Run the command in the project directory
(cd "$SCRIPT_DIR" && uv run makepdf "$@")
