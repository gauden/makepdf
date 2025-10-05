import os
import subprocess
import pytest
from unittest.mock import patch
from PIL import Image

@pytest.fixture
def setup_test_directory(tmp_path):
    original_cwd = os.getcwd()
    test_dir = tmp_path / "test_dir"
    os.mkdir(test_dir)
    os.chdir(test_dir)
    yield test_dir
    os.chdir(original_cwd)

def create_dummy_image(filename):
    img = Image.new('RGB', (1, 1), color = 'red')
    img.save(filename)

def test_makepdf_cwd_with_images(setup_test_directory):
    # Create dummy image files
    create_dummy_image("image1.jpg")
    create_dummy_image("image2.png")

    # Run makepdf without arguments
    with patch('sys.argv', ['makepdf']):
        from makepdf.main import main
        main()

    # Check if output.pdf was created
    assert os.path.exists("output.pdf")

def test_makepdf_cwd_empty_directory(setup_test_directory, capsys):
    # Run makepdf without arguments in an empty directory
    with patch('sys.argv', ['makepdf']):
        from makepdf.main import main
        main()

    # Check for the appropriate message
    captured = capsys.readouterr()
    assert "No valid files found" in captured.err

def test_makepdf_with_absolute_path_overrides_cwd(setup_test_directory, tmp_path):
    # Create a subdirectory with an image
    sub_dir = setup_test_directory / "sub"
    os.mkdir(sub_dir)
    create_dummy_image(sub_dir / "image3.jpg")

    # Run makepdf with an absolute path to the subdirectory
    with patch('sys.argv', ['makepdf', str(sub_dir)]):
        from makepdf.main import main
        main()

    # Check that output.pdf is created inside the subdirectory
    assert os.path.exists(sub_dir / "output.pdf")
