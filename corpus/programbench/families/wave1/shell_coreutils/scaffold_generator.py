#!/usr/bin/env python3
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from generator_lib import run_cli

if __name__ == "__main__":
    raise SystemExit(run_cli("shell_coreutils"))
