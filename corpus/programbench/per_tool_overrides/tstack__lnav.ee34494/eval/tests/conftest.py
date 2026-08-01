"""Shared test fixtures for lnav testing."""

import subprocess
import tempfile
import shutil
from pathlib import Path
import pytest

# Path to the executable
EXECUTABLE = Path(__file__).parent.parent.parent / "executable"


@pytest.fixture
def run_lnav():
    """
    Fixture providing a helper function to run lnav.
    
    Returns a function that executes lnav with given arguments and returns
    a CompletedProcess with stdout, stderr, and returncode.
    """
    def _run(args=None, stdin=None, timeout=30, check=False, env=None):
        """
        Run lnav with the given arguments.
        
        Args:
            args: List of command-line arguments (without the executable name)
            stdin: Input to pass to stdin (string or bytes)
            timeout: Timeout in seconds
            check: If True, raise CalledProcessError on non-zero exit
            env: Environment variables dict
            
        Returns:
            subprocess.CompletedProcess with stdout, stderr, returncode
        """
        cmd = [str(EXECUTABLE)]
        if args:
            cmd.extend(args)
        
        stdin_bytes = None
        if stdin is not None:
            stdin_bytes = stdin.encode() if isinstance(stdin, str) else stdin
        
        result = subprocess.run(
            cmd,
            input=stdin_bytes,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            timeout=timeout,
            check=check,
            env=env
        )
        
        # Decode output
        result.stdout = result.stdout.decode('utf-8', errors='replace')
        result.stderr = result.stderr.decode('utf-8', errors='replace')
        
        return result
    
    return _run


@pytest.fixture
def temp_dir():
    """Fixture providing a temporary directory that is cleaned up after the test."""
    tmpdir = tempfile.mkdtemp()
    yield Path(tmpdir)
    shutil.rmtree(tmpdir, ignore_errors=True)


@pytest.fixture
def sample_log(temp_dir):
    """Fixture providing a sample log file."""
    log_file = temp_dir / "sample.log"
    log_file.write_text(
        "2021-07-03T21:49:29.123 INFO Starting application\n"
        "2021-07-03T21:49:30.456 DEBUG Initialization complete\n"
        "2021-07-03T21:49:31.789 ERROR Connection failed\n"
    )
    return log_file
