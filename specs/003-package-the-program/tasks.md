# Tasks

This file outlines the tasks required to implement the packaging feature.

## Task List

1.  **[X] Update `pyproject.toml`**: 
    - Set `build-backend` to `hatchling.build`.
    - Define project metadata such as `name`, `version`, `requires-python`, etc.
    - Define the `makepdf` script entry point.

2.  **[X] Create `MANIFEST.in`**: 
    - Create a `MANIFEST.in` file to ensure all necessary files (e.g., `README.md`, `LICENSE`) are included in the source distribution.

3.  **[X] Update `README.md`**:
    - Add a section with instructions on how to install the package using `uv`.

4.  **[X] Create Installation Test**:
    - Create a new test file `tests/test_installation.py`.
    - This test should:
        - Build the package.
        - Install the package using `uv` in a virtual environment.
        - Run `makepdf --version` to verify the installation.

5.  **[X] Build the Package**:
    - Run `python -m build` to create the source and wheel distributions.

6.  **[X] Test Installation with `uv`**:
    - Manually test the installation process using `uv` as described in the `quickstart.md`.