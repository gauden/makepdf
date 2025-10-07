# Research: Removal of FFmpeg Conversion

**Date**: 2025-10-06

## Decisions

### Scope of Removal

- **Decision**: All FFmpeg-related functionality, code, tests, and documentation will be removed.
- **Rationale**: User clarification explicitly stated "All ffmpeg functionality is to be removed."

### Handling of Removed Functionality

- **Decision**: If a user attempts to use a feature that previously relied on FFmpeg, the application will silently ignore the request and proceed without the FFmpeg-dependent functionality.
- **Rationale**: User clarification.

### Handling of Existing Configurations

- **Decision**: The system will log a warning and continue, assuming the user will manually update any existing configurations or scripts that might still reference FFmpeg or its conversion capabilities.
- **Rationale**: User clarification.

## Identified FFmpeg Occurrences

### Code
- `src/makepdf/lib.py`: Contains the core FFmpeg conversion logic (`command_exists('ffmpeg')`, `subprocess.run(['ffmpeg', ...])`).

### Tests
- `tests/test_lib.py`: Contains `test_make_pdf_with_ffmpeg` which specifically tests the FFmpeg integration.

### Documentation/Specifications
- `specs/001-create-pdf-from-images/tasks.md`: Mentions `ffmpeg` integration.
- `specs/001-create-pdf-from-images/plan.md`: Lists `ffmpeg` as an optional dependency.
- `specs/004-remove-ffmpeg-conversion/spec.md`: This specification document itself.

### Other
- `.pytest_cache/v/cache/nodeids`: Cache file, can be ignored.

## Plan for Removal

1.  **Code Removal**: Delete or refactor code in `src/makepdf/lib.py` related to FFmpeg.
2.  **Test Removal**: Delete `test_make_pdf_with_ffmpeg` from `tests/test_lib.py`.
3.  **Documentation Updates**: 
    - Update `specs/001-create-pdf-from-images/tasks.md` to remove FFmpeg references.
    - Update `specs/001-create-pdf-from-images/plan.md` to remove FFmpeg references.
    - Ensure `README.md` does not mention FFmpeg (will be checked during implementation).
    - Update `GEMINI.md` to remove FFmpeg references.
