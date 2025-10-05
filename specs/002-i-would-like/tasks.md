# Tasks: Use Current Working Directory

**Input**: Design documents from `/specs/002-i-would-like/`
**Prerequisites**: plan.md, research.md, data-model.md, quickstart.md

## Phase 3.1: Setup
- No setup tasks required.

## Phase 3.2: Tests First (TDD)
- [x] T001 [P] Create a new test file `tests/test_main_cwd.py` to test the current working directory logic. This file should contain placeholder tests for running `makepdf` with no arguments in a directory with and without image files.

## Phase 3.3: Core Implementation
- [x] T002 Modify `src/makepdf/main.py` to use the files in the current working directory if no input files or directories are provided as arguments.

## Phase 3.4: Integration
- [x] T003 Implement the tests in `tests/test_main_cwd.py` to verify the new default behavior. The tests should check that `output.pdf` is created correctly when run in a directory with images and that an appropriate message is shown for an empty directory.

## Phase 3.5: Polish
- [x] T004 [P] Update the `README.md` file to document the new default behavior where `makepdf` uses the current working directory if no input paths are given.

## Dependencies
- T001 must be completed before T003.
- T002 must be completed before T003.

## Parallel Example
```
# T001 and T004 can be run in parallel:
Task: "Create a new test file tests/test_main_cwd.py..."
Task: "Update the README.md file..."
```
