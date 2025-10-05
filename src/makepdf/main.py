import argparse
import os
import sys
from .lib import make_pdf

def main():
    parser = argparse.ArgumentParser(description="Concatenate images and PDFs into a single PDF.")
    parser.add_argument("inputs", nargs="*", help="Input files or directories.")
    parser.add_argument("--output", help="Output PDF file.", default="output.pdf")
    parser.add_argument("--start", help="An existing PDF file to append to.")
    parser.add_argument("--version", action="version", version="%(prog)s 0.1.0")
    args = parser.parse_args()

    inputs = args.inputs
    if not inputs:
        inputs = ['.']

    files = []
    for item in inputs:
        if os.path.isdir(item):
            for filename in os.listdir(item):
                files.append(os.path.join(item, filename))
        else:
            files.append(item)

    if args.start:
        files = [args.start] + files

    if not files:
        print("No valid files found. Supported file types are: .pdf, .png, .jpg, .jpeg, .gif, .webp", file=sys.stderr)
        return

    output_file = args.output
    if output_file == "output.pdf" and len(inputs) == 1 and os.path.isdir(inputs[0]):
        output_file = os.path.join(inputs[0], "output.pdf")

    make_pdf(files, output_file)

if __name__ == "__main__":
    main()
