import subprocess
import sys
from pathlib import Path

def test_installation():
    """
    Tests that the package can be built and installed, and that the installed
    command runs correctly.
    """
    # Create a virtual environment using uv
    venv_dir = Path("test_venv")
    subprocess.run(["uv", "venv", str(venv_dir)], check=True)

    # Activate the virtual environment
    if sys.platform == "win32":
        python_path = venv_dir / "Scripts" / "python.exe"
    else:
        python_path = venv_dir / "bin" / "python"

    # Install build in the virtual environment
    subprocess.run(["uv", "pip", "install", "--python", str(python_path), "build"], check=True)

    # Build the package
    subprocess.run([str(python_path), "-m", "build"], check=True)

    # Find the built wheel
    dist_dir = Path("dist")
    wheel = list(dist_dir.glob("*.whl"))[0]

    # Install the package using uv
    subprocess.run(["uv", "pip", "install", "--python", str(python_path), str(wheel)], check=True)

    # Run the installed command
    if sys.platform == "win32":
        makepdf_path = venv_dir / "Scripts" / "makepdf.exe"
    else:
        makepdf_path = venv_dir / "bin" / "makepdf"
        
    result = subprocess.run([str(makepdf_path), "--version"], capture_output=True, text=True)

    # Check the output
    assert "makepdf" in result.stdout
    assert "0.1.0" in result.stdout
