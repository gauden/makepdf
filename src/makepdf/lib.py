from pypdf import PdfWriter, PdfReader
from PIL import Image
import os
import shutil
import subprocess

def command_exists(cmd):
    return shutil.which(cmd) is not None

def make_pdf(input_files, output_file):
    merger = PdfWriter()
    temp_files = []

    for input_file in input_files:
        if input_file.lower().endswith('.pdf'):
            reader = PdfReader(input_file, strict=False)
            merger.append(reader)
        elif input_file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.webp')):
            image = Image.open(input_file)
            if image.mode == 'RGBA':
                image = image.convert('RGB')
            temp_pdf_path = input_file + '.pdf'
            image.save(temp_pdf_path)
            merger.append(temp_pdf_path)
            temp_files.append(temp_pdf_path)
        # FFmpeg conversion block removed as per feature specification
        # elif command_exists('ffmpeg'):
        #     if not input_file.lower().endswith('.txt'):
        #         temp_pdf_path = input_file + '.pdf'
        #         try:
        #             subprocess.run(['ffmpeg', '-i', input_file, temp_pdf_path], check=True, capture_output=True)
        #             merger.append(temp_pdf_path)
        #             temp_files.append(temp_pdf_path)
        #         except subprocess.CalledProcessError as e:
        #             print(f"Could not convert {input_file} to PDF. ffmpeg error: {e.stderr.decode()}")

    merger.write(output_file)
    merger.close()

    for temp_file in temp_files:
        os.remove(temp_file)