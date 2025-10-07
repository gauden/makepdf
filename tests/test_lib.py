import os
import unittest
from unittest.mock import patch
from pypdf import PdfReader, PdfWriter
from PIL import Image
import shutil
from makepdf.lib import make_pdf

TEST_DATA_DIR = "tests/data"

def create_dummy_pdf(name):
    writer = PdfWriter()
    writer.add_blank_page(width=100, height=100)
    with open(name, "wb") as f:
        writer.write(f)

class TestLib(unittest.TestCase):

    def setUp(self):
        os.makedirs(TEST_DATA_DIR, exist_ok=True)
        self.test_files = []

    def tearDown(self):
        for f in self.test_files:
            if os.path.exists(f):
                os.remove(f)
        if os.path.exists(TEST_DATA_DIR):
            shutil.rmtree(TEST_DATA_DIR)

    def create_dummy_file(self, name, content=''):
        with open(os.path.join(TEST_DATA_DIR, name), 'w') as f:
            f.write(content)
        self.test_files.append(os.path.join(TEST_DATA_DIR, name))

    def create_dummy_image(self, name):
        img = Image.new('RGB', (100, 100), color = 'red')
        img.save(os.path.join(TEST_DATA_DIR, name))
        self.test_files.append(os.path.join(TEST_DATA_DIR, name))

    def test_make_pdf_with_pdfs(self):
        create_dummy_pdf(os.path.join(TEST_DATA_DIR, 'test1.pdf'))
        create_dummy_pdf(os.path.join(TEST_DATA_DIR, 'test2.pdf'))
        output_pdf = 'output.pdf'
        self.test_files.append(output_pdf)

        make_pdf([os.path.join(TEST_DATA_DIR, 'test1.pdf'), os.path.join(TEST_DATA_DIR, 'test2.pdf')], output_pdf)

        self.assertTrue(os.path.exists(output_pdf))
        reader = PdfReader(output_pdf)
        self.assertEqual(len(reader.pages), 2)

    def test_make_pdf_with_images(self):
        self.create_dummy_image('test1.jpg')
        self.create_dummy_image('test2.png')
        output_pdf = 'output.pdf'
        self.test_files.append(output_pdf)

        make_pdf([os.path.join(TEST_DATA_DIR, 'test1.jpg'), os.path.join(TEST_DATA_DIR, 'test2.png')], output_pdf)

        self.assertTrue(os.path.exists(output_pdf))
        reader = PdfReader(output_pdf)
        self.assertEqual(len(reader.pages), 2)

if __name__ == '__main__':
    unittest.main()