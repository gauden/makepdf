# makepdf

A simple tool to concatenate images and PDFs into a single PDF file.

## Installation

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/gauden/makepdf.git
    cd makepdf
    ```

2.  **Run the setup script:**

    This will create a `makepdf` command in the project directory.

    ```bash
    ./makepdf_launcher.sh
    ```

3.  **Move the command to your PATH:**

    This will make the `makepdf` command available globally.

    ```bash
    sudo mv ./makepdf_launcher.sh /usr/local/bin/makepdf
    ```

4.  **Verify the installation:**

    ```bash
    makepdf --version
    ```

## Uninstallation

To uninstall the `makepdf` command, simply remove the file from `/usr/local/bin`:

```bash
sudo rm /usr/local/bin/makepdf
```

You can also delete the project directory.

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
