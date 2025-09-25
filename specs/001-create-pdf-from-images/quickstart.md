# Quickstart

This guide will walk you through the process of using the `makepdf` tool.

## Installation

```bash
# Install the package
uv pip install makepdf

# Verify the installation
makepdf --version
```

## Usage

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
