import subprocess
import os
import tempfile
import shutil
from pathlib import Path
import pytest

# Path to the executable
EXECUTABLE = "./executable"

def run(*args, stdin=None, env=None, cwd=None, timeout=5.0, check=False):
    """Run the executable with given arguments and optional stdin."""
    full_env = os.environ.copy()
    if env:
        full_env.update(env)
    
    result = subprocess.run(
        [EXECUTABLE, *args],
        input=stdin.encode() if isinstance(stdin, str) else stdin,
        capture_output=True,
        timeout=timeout,
        env=full_env,
        cwd=cwd,
    )
    
    if check and result.returncode != 0:
        print(f"Command failed: {EXECUTABLE} {' '.join(args)}")
        print(f"stdout: {result.stdout.decode()}")
        print(f"stderr: {result.stderr.decode()}")
    
    return result

@pytest.fixture
def temp_dir(tmp_path):
    """Provide a temporary directory for tests."""
    return tmp_path

@pytest.fixture
def sample_file(temp_dir):
    """Create a sample file with known content."""
    file_path = temp_dir / "sample.txt"
    content = b"This is a test file with some content.\n"
    file_path.write_bytes(content)
    return file_path

@pytest.fixture
def sample_dir(temp_dir):
    """Create a sample directory structure."""
    dir_path = temp_dir / "sample_dir"
    dir_path.mkdir()
    (dir_path / "file1.txt").write_text("Content of file 1")
    (dir_path / "file2.txt").write_text("Content of file 2")
    subdir = dir_path / "subdir"
    subdir.mkdir()
    (subdir / "file3.txt").write_text("Content of file 3")
    return dir_path
