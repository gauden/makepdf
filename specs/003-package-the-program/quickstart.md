# Quickstart

This guide explains how to build and install the `makepdf` package.

## Prerequisites

- Python 3.9 or higher
- `build` package (`pip install build`)
- `uv` package (`pip install uv`)

## Build

1.  Navigate to the root of the project.
2.  Run the following command to build the package:

    ```bash
    python -m build
    ```

    This will create a `dist/` directory containing the built package.

## Installation

1.  Once the package is built, you can install it using `uv`:

    ```bash
    uv tool install --from dist/makepdf-0.1.0-py3-none-any.whl
    ```

2.  Verify the installation by running:

    ```bash
    makepdf --version
    ```
