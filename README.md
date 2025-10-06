# makepdf

A simple tool to concatenate images and PDFs into a single PDF file.

Fully created with Github Spec-kit and Google Gemini-CLI

## Installation

It is recommended to install `makepdf` using `uv`.

```bash
uv tool install makepdf
```

Alternatively, you can build and install it from source.

### Build from Source

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/gauden/makepdf.git
    cd makepdf
    ```

2.  **Build the package:**

    ```bash
    python -m build
    ```

3.  **Install using `uv`:**

    ```bash
    uv tool install --from dist/makepdf-0.1.0-py3-none-any.whl
    ```

4.  **Verify the installation:**

    ```bash
    makepdf --version
    ```

## Uninstallation

To uninstall the `makepdf` command, run:

```bash
uv tool uninstall makepdf
```

## Usage

If no input files or directories are specified, `makepdf` will automatically process all supported files in the current working directory.

### Concatenate all images and PDFs in a directory

```bash
makepdf /path/to/your/directory
```

This will create a file named `output.pdf` in your current directory.

### Specify an output filename

```bash
makepdf /path/to/your/directory --output my-document.pdf
```

### Concatenate specific files

```bash
makepdf file1.jpg file2.pdf file3.png
```

### Append to an existing PDF

```bash
makepdf file1.jpg file2.png --start existing.pdf
```