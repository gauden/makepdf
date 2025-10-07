# Tasks

This file outlines the tasks required to remove FFmpeg conversion functionality.

## Task List

1.  **[X] Remove FFmpeg Code**: 
    - Refactor `src/makepdf/lib.py` to remove all code related to FFmpeg conversion.
    - Ensure that if a user attempts to use a feature that previously relied on FFmpeg, the application silently ignores the request and proceeds without the FFmpeg-dependent functionality.

2.  **[X] Remove FFmpeg Test**: 
    - Delete the `test_make_pdf_with_ffmpeg` function from `tests/test_lib.py`.

3.  **[X] Update Documentation**: 
    - Update `specs/001-create-pdf-from-images/tasks.md` to remove any FFmpeg references.
    - Update `specs/001-create-pdf-from-images/plan.md` to remove any FFmpeg references.
    - Review `README.md` and remove any mentions of FFmpeg conversion.
    - Review `GEMINI.md` and remove any mentions of FFmpeg conversion.

4.  **[X] Verify No FFmpeg Dependency**: 
    - Ensure that FFmpeg is no longer listed as a dependency in `pyproject.toml` or any other configuration files.
