import argparse
import os
from .lib import make_pdf

def main():
    parser = argparse.ArgumentParser(description="Concatenate images and PDFs into a single PDF.")
    parser.add_argument("inputs", nargs="*", help="Input files or directories.")
    parser.add_argument("--output", help="Output PDF file.", default="output.pdf")
    parser.add_argument("--start", help="An existing PDF file to append to.")
    parser.add_argument("--version", action="version", version="%(prog)s 0.1.0")
    args = parser.parse_args()

    files = []
    for item in args.inputs:
        if os.path.isdir(item):
            for filename in os.listdir(item):
                files.append(os.path.join(item, filename))
        else:
            files.append(item)

    if args.start:
        files = [args.start] + files

    make_pdf(files, args.output)

if __name__ == "__main__":
    main()
