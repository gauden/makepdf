import os
import subprocess
import shutil
from unittest import TestCase
from PyPDF2 import PdfWriter

def create_dummy_pdf(name):
    writer = PdfWriter()
    writer.add_blank_page(width=100, height=100)
    with open(name, "wb") as f:
        writer.write(f)

class TestMain(TestCase):
    @classmethod
    def setUpClass(cls):
        os.makedirs("test_dir", exist_ok=True)
        create_dummy_pdf("test_dir/file1.pdf")
        create_dummy_pdf("test_dir/file2.pdf")
        create_dummy_pdf("file1.pdf")
        create_dummy_pdf("file2.pdf")
        create_dummy_pdf("existing.pdf")

    @classmethod
    def tearDownClass(cls):
        if os.path.exists("output.pdf"):
            os.remove("output.pdf")
        if os.path.exists("my-document.pdf"):
            os.remove("my-document.pdf")
        if os.path.exists("test_dir"):
            shutil.rmtree("test_dir")
        os.remove("file1.pdf")
        os.remove("file2.pdf")
        os.remove("existing.pdf")

    def test_directory_concatenation(self):
        subprocess.run(["uv", "run", "python", "-m", "makepdf.main", "test_dir"], check=True)
        self.assertTrue(os.path.exists("output.pdf"))

    def test_file_list_concatenation(self):
        subprocess.run(["uv", "run", "python", "-m", "makepdf.main", "file1.pdf", "file2.pdf"], check=True)
        self.assertTrue(os.path.exists("output.pdf"))

    def test_output_filename(self):
        subprocess.run(["uv", "run", "python", "-m", "makepdf.main", "file1.pdf", "--output", "my-document.pdf"], check=True)
        self.assertTrue(os.path.exists("my-document.pdf"))

    def test_append_to_existing_pdf(self):
        subprocess.run(["uv", "run", "python", "-m", "makepdf.main", "file1.pdf", "--start", "existing.pdf"], check=True)
        self.assertTrue(os.path.exists("existing.pdf"))