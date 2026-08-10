"""The other side of the mojibake pipe.

`determinex_pb_mojibake_guard` answers "is any FILE corrupt". That was being read as "no
mojibake", which is a different claim, and the gap between them is exactly one degree sign: a
source file holding a perfectly valid UTF-8 character, printed to a Windows cp1252 console, is
mangled ON THE WAY OUT. Clean file, clean check, garbage on screen.

Vesuvius hit this on a live run. This guard was inspected at the time and found to have the
identical blind spot, and nothing was done about it here for a day.

THE RULE IS DETERMINEX-SPECIFIC. Forbidding non-ASCII in printed strings -- Vesuvius's answer --
would flag 189 files and 86 distinct characters here, including box-drawing that several report
renderers use on purpose. So the rule is not "do not print this character", it is "if you print
it, guarantee the stream that carries it": 53 files already do, 96 entrypoints do not.
"""

from __future__ import annotations

import sys
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(_ROOT / "scripts"))

from determinex_pb_mojibake_guard import check_console_encoding  # noqa: E402

_DEG = "°"
_ARROW = "→"


def _check(tmp_path: Path, body: str, name: str = "m.py") -> list[str]:
    p = tmp_path / name
    p.write_text(body, encoding="utf-8")
    return check_console_encoding(p)


def test_an_entrypoint_printing_non_ascii_is_flagged(tmp_path):
    out = _check(
        tmp_path, f'def m():\n    print("GPU 51{_DEG}C")\nif __name__ == "__main__":\n    m()\n'
    )
    assert out, "the exact defect that started this went unreported"
    assert "U+00B0" in out[0]


def test_the_report_names_codepoints_and_never_echoes_the_character(tmp_path):
    """Echoing it makes the guard's own output render as mojibake on the console it is warning
    about -- and this module is excluded from its own scan, so nothing would ever flag that."""
    out = _check(tmp_path, f'print("x{_DEG}")\nif __name__ == "__main__":\n    pass\n')
    assert out
    assert _DEG not in out[0], "the mojibake report contains the character it is reporting"
    assert "DEGREE SIGN" in out[0]


def test_securing_stdout_clears_it(tmp_path):
    """The fix keeps the character AND the reports that use box-drawing on purpose. Stripping
    text to appease a terminal would make the output worse to fix the wrong layer."""
    body = (
        "import sys\n"
        'sys.stdout.reconfigure(encoding="utf-8")\n'
        f'def m():\n    print("GPU 51{_DEG}C")\n'
        'if __name__ == "__main__":\n    m()\n'
    )
    assert not _check(tmp_path, body)


def test_a_library_is_not_flagged(tmp_path):
    """A library does not own the process's stdout. The entrypoint that runs it does, and that
    is where the fix goes -- reporting the library moves the finding away from the fix."""
    assert not _check(tmp_path, f'def helper():\n    print("GPU 51{_DEG}C")\n')


def test_a_clean_entrypoint_is_silent(tmp_path):
    """Specificity. A guard that fires on everything gets removed."""
    assert not _check(
        tmp_path, 'def m():\n    print("GPU 51 deg C")\nif __name__ == "__main__":\n    m()\n'
    )


def test_an_f_string_built_in_one_place_and_printed_in_another_is_caught(tmp_path):
    """THE defect. `parts.append(f"GPU={x}<deg>C")` is unreachable from an AST walk rooted at
    `print`, so the guard written to catch this exact bug did not catch this exact bug. Every
    f-string is checked, not only printed arguments."""
    body = (
        "def build():\n"
        "    parts = []\n"
        f'    parts.append(f"GPU={{1}}{_DEG}C")\n'
        "    return parts\n"
        'if __name__ == "__main__":\n    print(build())\n'
    )
    out = _check(tmp_path, body)
    assert out, "an indirectly-printed f-string was missed"
    assert out[0].startswith("line 3")


def test_a_multiline_f_string_reports_the_line_the_character_is_on(tmp_path):
    """Two traps, both of which make the count go down while the defect stays. A multi-line
    f-string reports ONE lineno for the whole part, so a fixer trusting it edits the wrong line.
    And the line cannot be recovered by splitting the literal's VALUE on newlines, because an
    escaped `\n` is one character of value and ZERO source lines. Only the node's span works."""
    body = (
        "def m():\n"
        "    x = 1\n"
        '    s = f"""line one\n'
        "line two\n"
        f"line three {{x}} {_ARROW} done\n"
        '"""\n'
        "    print(s)\n"
        'if __name__ == "__main__":\n    m()\n'
    )
    out = _check(tmp_path, body)
    assert out
    assert out[0].startswith("line 5"), f"reported the wrong line: {out[0][:40]}"
