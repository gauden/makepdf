# Quickstart

This guide demonstrates the new default behavior of the `makepdf` tool.

## Setup

1.  Create a directory and navigate into it:
    ```bash
    mkdir test_makepdf
    cd test_makepdf
    ```

2.  Create some dummy image files:
    ```bash
    touch image1.jpg
    touch image2.png
    ```

## Execution

1.  Run `makepdf` without any arguments:
    ```bash
    makepdf
    ```

2.  Verify the output:
    - An `output.pdf` file should be created in the `test_makepdf` directory.

This demonstrates that `makepdf` now uses the current working directory by default.
