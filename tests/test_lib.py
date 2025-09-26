import os
import unittest
from unittest.mock import patch, call
from pypdf import PdfReader, PdfWriter
from PIL import Image
from makepdf.lib import make_pdf, command_exists

def create_dummy_pdf(name):
    writer = PdfWriter()
    writer.add_blank_page(width=100, height=100)
    with open(name, "wb") as f:
        writer.write(f)

class TestLib(unittest.TestCase):

    def setUp(self):
        self.test_files = []

    def tearDown(self):
        for f in self.test_files:
            if os.path.exists(f):
                os.remove(f)

    def create_dummy_file(self, name, content=''):
        with open(name, 'w') as f:
            f.write(content)
        self.test_files.append(name)

    def create_dummy_image(self, name):
        img = Image.new('RGB', (100, 100), color = 'red')
        img.save(name)
        self.test_files.append(name)

    def test_make_pdf_with_pdfs(self):
        create_dummy_pdf('test1.pdf')
        create_dummy_pdf('test2.pdf')
        output_pdf = 'output.pdf'
        self.test_files.append(output_pdf)

        make_pdf(['test1.pdf', 'test2.pdf'], output_pdf)

        self.assertTrue(os.path.exists(output_pdf))
        reader = PdfReader(output_pdf)
        self.assertEqual(len(reader.pages), 2)

    def test_make_pdf_with_images(self):
        self.create_dummy_image('test1.jpg')
        self.create_dummy_image('test2.png')
        output_pdf = 'output.pdf'
        self.test_files.append(output_pdf)

        make_pdf(['test1.jpg', 'test2.png'], output_pdf)

        self.assertTrue(os.path.exists(output_pdf))
        reader = PdfReader(output_pdf)
        self.assertEqual(len(reader.pages), 2)

    @patch('makepdf.lib.subprocess.run')
    @patch('makepdf.lib.command_exists', return_value=True)
    def test_make_pdf_with_ffmpeg(self, mock_command_exists, mock_subprocess_run):
        self.create_dummy_file('test.mov')
        # Create a dummy pdf file that ffmpeg would create
        create_dummy_pdf('test.mov.pdf')
        output_pdf = 'output.pdf'
        self.test_files.append(output_pdf)

        make_pdf(['test.mov'], output_pdf)

        self.assertTrue(os.path.exists(output_pdf))
        mock_command_exists.assert_called_once_with('ffmpeg')
        mock_subprocess_run.assert_called_once_with(['ffmpeg', '-i', 'test.mov', 'test.mov.pdf'], check=True, capture_output=True)

if __name__ == '__main__':
    unittest.main()
