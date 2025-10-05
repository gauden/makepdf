
# Implementation Plan: Use Current Working Directory

**Branch**: `002-i-would-like` | **Date**: 2025-10-05 | **Spec**: [./spec.md](./spec.md)
**Input**: Feature specification from `/Users/gauden/dev/makepdf/specs/002-i-would-like/spec.md`

## Execution Flow (/plan command scope)
```
1. Load feature spec from Input path
   → If not found: ERROR "No feature spec at {path}"
2. Fill Technical Context (scan for NEEDS CLARIFICATION)
   → Detect Project Type from context (web=frontend+backend, mobile=app+api)
   → Set Structure Decision based on project type
3. Fill the Constitution Check section based on the content of the constitution document.
4. Evaluate Constitution Check section below
   → If violations exist: Document in Complexity Tracking
   → If no justification possible: ERROR "Simplify approach first"
   → Update Progress Tracking: Initial Constitution Check
5. Execute Phase 0 → research.md
   → If NEEDS CLARIFICATION remain: ERROR "Resolve unknowns"
6. Execute Phase 1 → contracts, data-model.md, quickstart.md, agent-specific template file (e.g., `CLAUDE.md` for Claude Code, `.github/copilot-instructions.md` for GitHub Copilot, `GEMINI.md` for Gemini CLI, `QWEN.md` for Qwen Code or `AGENTS.md` for opencode).
7. Re-evaluate Constitution Check section
   → If new violations: Refactor design, return to Phase 1
   → Update Progress Tracking: Post-Design Constitution Check
8. Plan Phase 2 → Describe task generation approach (DO NOT create tasks.md)
9. STOP - Ready for /tasks command
```

**IMPORTANT**: The /plan command STOPS at step 7. Phases 2-4 are executed by other commands:
- Phase 2: /tasks command creates tasks.md
- Phase 3-4: Implementation execution (manual or via tools)

## Summary
This feature will modify the `makepdf` tool to use the user's current working directory as the default location for finding input files. The core logic in `src/makepdf/main.py` will be updated to use `os.getcwd()` when no input paths are provided, ensuring the tool operates in the directory from which it is called.

## Technical Context
**Language/Version**: Python >=3.12
**Primary Dependencies**: pypdf, Pillow
**Storage**: Filesystem
**Testing**: pytest
**Target Platform**: OS Independent (CLI)
**Project Type**: single
**Performance Goals**: Handle as many files as system memory allows.
**Constraints**: N/A
**Scale/Scope**: Small, single-purpose command-line tool.

## Constitution Check
*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

- **I. Code Quality**: Yes, the changes will be made in a clear and maintainable way, following existing code style.
- **II. Testing Standards**: Yes, new unit tests will be added to cover the new behavior, maintaining coverage.
- **III. User Experience Consistency**: Yes, this change improves the expected CLI behavior to be more intuitive.
- **IV. Performance Requirements**: Yes, the change is not expected to impact performance negatively.

## Project Structure

### Documentation (this feature)
```
specs/002-i-would-like/
├── plan.md              # This file (/plan command output)
├── research.md          # Phase 0 output (/plan command)
├── data-model.md        # Phase 1 output (/plan command)
├── quickstart.md        # Phase 1 output (/plan command)
├── contracts/           # Phase 1 output (/plan command)
└── tasks.md             # Phase 2 output (/tasks command - NOT created by /plan)
```

### Source Code (repository root)
```
# Option 1: Single project (DEFAULT)
src/
└── makepdf/
    ├── __init__.py
    ├── lib.py
    └── main.py

tests/
├── test_lib.py
└── test_main.py
```

**Structure Decision**: Option 1: Single project

## Phase 0: Outline & Research
1. **Extract unknowns from Technical Context** above:
   - All items in technical context are resolved. No research needed.

2. **Generate and dispatch research agents**:
   - N/A

3. **Consolidate findings** in `research.md`:
   - No research was required.

**Output**: research.md with all NEEDS CLARIFICATION resolved

## Phase 1: Design & Contracts
*Prerequisites: research.md complete*

1. **Extract entities from feature spec** → `data-model.md`:
   - No new data models are required. The change is behavioral.

2. **Generate API contracts** from functional requirements:
   - N/A. This is a CLI tool, not an API.

3. **Generate contract tests** from contracts:
   - N/A.

4. **Extract test scenarios** from user stories:
   - The quickstart will be updated to reflect the new default behavior.

5. **Update agent file incrementally** (O(1) operation):
   - Run `.specify/scripts/bash/update-agent-context.sh gemini`

**Output**: data-model.md, /contracts/*, failing tests, quickstart.md, agent-specific file

## Phase 2: Task Planning Approach
*This section describes what the /tasks command will do - DO NOT execute during /plan*

**Task Generation Strategy**:
- Load `.specify/templates/tasks-template.md` as base
- Generate tasks from the feature spec and this plan.
- A task will be created to modify `src/makepdf/main.py` to change the default file collection behavior.
- A task will be created to add new tests to `tests/test_main.py` to verify the new behavior.

**Ordering Strategy**:
- TDD order: Tests before implementation.

**Estimated Output**: 2-3 numbered, ordered tasks in tasks.md

**IMPORTANT**: This phase is executed by the /tasks command, NOT by /plan

## Phase 3+: Future Implementation
*These phases are beyond the scope of the /plan command*

**Phase 3**: Task execution (/tasks command creates tasks.md)
**Phase 4**: Implementation (execute tasks.md following constitutional principles)
**Phase 5**: Validation (run tests, execute quickstart.md, performance validation)

## Complexity Tracking
*Fill ONLY if Constitution Check has violations that must be justified*

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| N/A       | N/A        | N/A                                 |


## Progress Tracking
*This checklist is updated during execution flow*

**Phase Status**:
- [x] Phase 0: Research complete (/plan command)
- [x] Phase 1: Design complete (/plan command)
- [x] Phase 2: Task planning complete (/plan command - describe approach only)
- [ ] Phase 3: Tasks generated (/tasks command)
- [ ] Phase 4: Implementation complete
- [ ] Phase 5: Validation passed

**Gate Status**:
- [x] Initial Constitution Check: PASS
- [x] Post-Design Constitution Check: PASS
- [x] All NEEDS CLARIFICATION resolved
- [ ] Complexity deviations documented

---
*Based on Constitution v1.0.0 - See /.specify/memory/constitution.md*
