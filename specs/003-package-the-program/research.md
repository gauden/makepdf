# Research: Packaging with hatchling and uv

**Date**: 2025-10-06

## Decisions

### Packaging Tool: Hatchling

- **Decision**: Use `hatchling` as the build backend for the Python project.
- **Rationale**: The user explicitly requested `hatchling`. It is a modern, extensible build backend that is fully compliant with PEP 621.
- **Alternatives considered**: `setuptools`, `flit`. `setuptools` is the most common, but can be complex. `flit` is simpler, but less extensible than `hatchling`.

### Installation Tool: uv

- **Decision**: The primary installation method will be via `uv tool install`.
- **Rationale**: The user explicitly requested `uv`. `uv` is a fast, modern Python package installer that is gaining popularity.
- **Alternatives considered**: `pip`. `pip` is the standard Python package installer, but `uv` is significantly faster.

## Implementation Details

### `pyproject.toml` Configuration

To use `hatchling`, the `pyproject.toml` file must be configured as follows:

```toml
[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[project]
name = "makepdf"
version = "0.1.0"
requires-python = ">=3.9"
classifiers = [
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
]

[project.scripts]
makepdf = "makepdf.main:main"
```

### Building the Package

The package can be built using the following command:

```bash
python -m build
```

This will create a source distribution (`.tar.gz`) and a built distribution (`.whl`) in the `dist/` directory.

### Installation with `uv`

The package can be installed from the built distribution using `uv`:

```bash
uv tool install --from dist/makepdf-0.1.0-py3-none-any.whl
```

Or, if published to a registry:

```bash
uv tool install makepdf
```
