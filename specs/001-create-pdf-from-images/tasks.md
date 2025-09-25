# Tasks: PDF Concatenation Tool

**Input**: Design documents from `/Users/gauden/dev/makepdf/specs/001-create-pdf-from-images/`

## Phase 3.1: Setup
- [ ] T001 Create project structure in `src/makepdf` and `tests`
- [ ] T002 Initialize Python project with `pyproject.toml`
- [ ] T003 [P] Configure linting with `ruff`

## Phase 3.2: Tests First (TDD) ⚠️ MUST COMPLETE BEFORE 3.3
**CRITICAL: These tests MUST be written and MUST FAIL before ANY implementation**
- [ ] T004 [P] Write failing integration test for directory concatenation in `tests/test_main.py`
- [ ] T005 [P] Write failing integration test for file list concatenation in `tests/test_main.py`
- [ ] T006 [P] Write failing integration test for output filename in `tests/test_main.py`
- [ ] T007 [P] Write failing integration test for appending to existing PDF in `tests/test_main.py`

## Phase 3.3: Core Implementation (ONLY after tests are failing)
- [ ] T008 Implement `makepdf` CLI with `argparse` in `src/makepdf/main.py`
- [ ] T009 Implement PDF concatenation logic in `src/makepdf/lib.py`
- [ ] T010 Implement image conversion logic in `src/makepdf/lib.py`

## Phase 3.4: Integration
- [ ] T011 Add optional `ffmpeg` integration for file conversion in `src/makepdf/lib.py`

## Phase 3.5: Polish
- [ ] T012 [P] Write unit tests for `lib.py` in `tests/test_lib.py`
- [ ] T013 [P] Update `README.md` with usage instructions
- [ ] T014 Run manual tests from `quickstart.md`

## Dependencies
- Tests (T004-T007) before implementation (T008-T010)
- T009 and T010 block T008
- Core implementation before integration (T011)
- Everything before polish (T012-T014)

## Parallel Example
```
# Launch T004-T007 together:
Task: "Write failing integration test for directory concatenation in tests/test_main.py"
Task: "Write failing integration test for file list concatenation in tests/test_main.py"
Task: "Write failing integration test for output filename in tests/test_main.py"
Task: "Write failing integration test for appending to existing PDF in tests/test_main.py"
```
