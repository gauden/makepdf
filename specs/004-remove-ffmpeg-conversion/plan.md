# Implementation Plan: Remove FFmpeg Conversion

**Branch**: `004-remove-ffmpeg-conversion` | **Date**: 2025-10-06 | **Spec**: [link](./spec.md)
**Input**: Feature specification from `/specs/004-remove-ffmpeg-conversion/spec.md`

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
This plan outlines the steps to completely remove FFmpeg conversion functionality, code, tests, and documentation from the `makepdf` application.

## Technical Context
**Language/Version**: Python 3.9+
**Primary Dependencies**: None (FFmpeg will be removed)
**Storage**: N/A
**Testing**: `pytest`
**Target Platform**: OS Independent
**Project Type**: single
**Performance Goals**: Application should be lighter due to dependency removal.
**Constraints**: Complete removal of FFmpeg.
**Scale/Scope**: Small CLI tool.

## Constitution Check
*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

- **I. Code Quality**: The proposed changes will improve code clarity by removing dead code.
- **II. Testing Standards**: Existing tests for FFmpeg will be removed, and core functionality tests will be maintained.
- **III. User Experience Consistency**: N/A for this feature.
- **IV. Performance Requirements**: Removal of FFmpeg is expected to improve performance by reducing overhead.

## Project Structure

### Documentation (this feature)
```
specs/004-remove-ffmpeg-conversion/
├── plan.md              # This file (/plan command output)
├── research.md          # Phase 0 output (/plan command)
├── data-model.md        # Phase 1 output (/plan command)
├── quickstart.md        # Phase 1 output (/plan command)
└── tasks.md             # Phase 2 output (/tasks command - NOT created by /plan)
```

### Source Code (repository root)
```
# Option 1: Single project (DEFAULT)
src/
└── makepdf/

tests/
```

**Structure Decision**: Option 1: Single project

## Phase 0: Outline & Research
Completed. See `research.md`.

## Phase 1: Design & Contracts
Completed. See `data-model.md` and `quickstart.md`.

## Phase 2: Task Planning Approach
Completed. See `tasks.md`.

## Phase 3+: Future Implementation
*These phases are beyond the scope of the /plan command*

**Phase 3**: Task execution (/tasks command creates tasks.md)  
**Phase 4**: Implementation (execute tasks.md following constitutional principles)  
**Phase 5**: Validation (run tests, execute quickstart.md, performance validation)

## Complexity Tracking
No violations to the constitution.

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
- [x] Complexity deviations documented

---
*Based on Constitution v1.0.0 - See /.specify/memory/constitution.md*