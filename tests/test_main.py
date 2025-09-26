import os
import shutil
import sys
from unittest import TestCase
from unittest.mock import patch
from pypdf import PdfWriter
from makepdf.main import main

TEST_DATA_DIR = "tests/data"

def create_dummy_pdf(name):
    writer = PdfWriter()
    writer.add_blank_page(width=100, height=100)
    with open(name, "wb") as f:
        writer.write(f)

class TestMain(TestCase):
    @classmethod
    def setUpClass(cls):
        os.makedirs(TEST_DATA_DIR, exist_ok=True)
        create_dummy_pdf(os.path.join(TEST_DATA_DIR, "file1.pdf"))
        create_dummy_pdf(os.path.join(TEST_DATA_DIR, "file2.pdf"))
        create_dummy_pdf(os.path.join(TEST_DATA_DIR, "existing.pdf"))
        with open(os.path.join(TEST_DATA_DIR, "file1.txt"), "w") as f:
            f.write("dummy text")
        with open(os.path.join(TEST_DATA_DIR, "file2.txt"), "w") as f:
            f.write("more dummy text")

    @classmethod
    def tearDownClass(cls):
        if os.path.exists("output.pdf"):
            os.remove("output.pdf")
        if os.path.exists("my-document.pdf"):
            os.remove("my-document.pdf")
        if os.path.exists(TEST_DATA_DIR):
            shutil.rmtree(TEST_DATA_DIR)

    def test_directory_concatenation(self):
        with patch.object(sys, 'argv', ['makepdf', TEST_DATA_DIR]):
            main()
        self.assertTrue(os.path.exists("output.pdf"))

    def test_file_list_concatenation(self):
        with patch.object(sys, 'argv', ['makepdf', os.path.join(TEST_DATA_DIR, "file1.pdf"), os.path.join(TEST_DATA_DIR, "file2.pdf")]):
            main()
        self.assertTrue(os.path.exists("output.pdf"))

    def test_output_filename(self):
        with patch.object(sys, 'argv', ['makepdf', os.path.join(TEST_DATA_DIR, "file1.pdf"), '--output', 'my-document.pdf']):
            main()
        self.assertTrue(os.path.exists("my-document.pdf"))

    def test_append_to_existing_pdf(self):
        with patch.object(sys, 'argv', ['makepdf', os.path.join(TEST_DATA_DIR, "file1.pdf"), '--start', os.path.join(TEST_DATA_DIR, "existing.pdf")]):
            main()
        self.assertTrue(os.path.exists("output.pdf"))