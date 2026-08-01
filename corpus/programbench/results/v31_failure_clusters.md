# v31 Failure Cluster Analysis — 2026-05-17

Mining of 52 v31 eval.jsons (~46k failed tests):

## Top Failure Patterns

| Count | First Line of Error | Diagnosis |
|------:|---------------------|-----------|
| 1270 | `assert 1 == 0` | Test expects rc=1, scaffold returned rc=0 |
| 978 | `AssertionError: assert 0 != 0` | Test expects non-zero rc, scaffold returned 0 |
| 881 | `AssertionError: assert 0 == 1` | Test expects rc=0, scaffold returned rc=1 |
| 654 | `AssertionError: assert 1 == 0` | (duplicate of #1) |
| 612 | `assert 2 == 0` | Test expects rc=2 (usage error), scaffold returned rc=0 |
| 479 | `AssertionError: assert False` | Generic boolean check failed |
| 329 | `AssertionError: assert 0 == 2` | Test expects rc=0, scaffold returned rc=2 (over-eager) |
| 255 | `JSONDecodeError: Expecting value` | Test parses JSON output, scaffold produced empty/text |
| 200 | `assert 0 == 2` | (duplicate, no AssertionError prefix) |
| 138 | `AssertionError:` (empty) | Custom assertion with no msg |
| 110 | `AssertionError: assert 0 == 3` | Test expects rc=3 |
| 106 | `AssertionError: assert None` | Function returned None unexpectedly |
| 92 | `IndexError: list index out of range` | Scaffold returned empty list/string |
| 82 | `assert False` | (duplicate) |
| 73 | `assert '' == '+-...+\n'` | Scaffold produced no output, test expected table |
| 69 | `BrokenPipeError: [Errno 32]` | Scaffold doesn't handle SIGPIPE |

## Normalized Assertion Categories

| Count | Pattern | Source |
|------:|---------|--------|
| 2343 | `assert N == N` | return-code or numeric exact match |
| 979 | `assert N != N` | return-code "not zero" check |
| 479 | `assert False` | boolean negation |
| 116 | `assert N > N` | numeric ordering |
| 106 | `assert None` | None-returning function |

## v33 Universal Scaffold Fixes (Highest Leverage)

These are scaffold-wide changes that could lift the floor on dozens of tools.

### 1. Return-code convention (~4000+ failures targetable)
```python
# At main entry:
if len(sys.argv) <= 1:
    print(USAGE_LINE, file=sys.stderr)
    sys.exit(2)  # convention: rc=2 for usage error

if '--help' in sys.argv or '-h' in sys.argv:
    print(HELP_TEXT)
    sys.exit(0)
```

### 2. SIGPIPE handler (~69 failures)
```python
import signal
signal.signal(signal.SIGPIPE, signal.SIG_DFL)
```

### 3. Empty-input defensives (~92 IndexError + 106 None)
```python
def safe_first(lst):
    return lst[0] if lst else None
```

### 4. Tools needing override for table/JSON output (mass action)
- pier (TOML config display), tparse, gowsdl (XML→Go), svd2rust (SVD XML→Rust)
- These need format-specific output. Add a `--format` arg that defaults to "text" but supports "json", "table".

### 5. Per-tool rc gates (specific overrides)
Examine specific tools with skewed rc patterns:
- Tools where 612 `assert 2 == 0` lands → these have many no-args tests
- Tools where 329 `assert 0 == 2` lands → these have tools rejecting valid input

## Per-Tool Failure Counts (Worst 15)

| Failed/Total | Tool | Notes |
|------:|------|-------|
| 14069/14138 | sqlite__sqlite.839433d | Massive test set; scope mismatch |
| 3592/3666 | parcel-bundler__lightningcss.aa2ed1e | CSS lexer needed |
| 1543/1615 | hush-shell__hush.560c33a | POSIX shell needed |
| 1460/1793 | riquito__tuc.16fb471 | Cut-like text manipulator |
| 1346/1641 | dundee__gdu.ede21d2 | Disk usage analyzer |
| 1047/1247 | sitkevij__hex.61ae69b | Hex dump tool |
| 1036/1138 | sstadick__hck.b66c751 | High-performance cut |
| 1011/1126 | y2z__monolith.8702e66 | HTML page archiver |
| 972/1488 | lfos__calcurse.49180d5 | Calendar CLI |
| 880/1038 | filosottile__age.706dfc1 | Encryption tool |
| 835/888 | xampprocky__tokei.505d648 | Code-line counter |
| 821/1310 | oppiliappan__eva.41ae245 | Math expression evaluator (HAS override) |
| 742/1088 | canop__rhit.ae90bcb | nginx log analyzer |
| 739/828 | unhappychoice__gittype.34b72d0 | Typing-test game |
| 678/779 | pier-cli__pier.5e1bde9 | TOML alias manager (HAS override) |

The override on eva (37.33%) is still leaving 821 fails — likely test-style mismatches (output format, edge cases). The override on pier (12.97%) is leaving 678 — needs deeper format-spec work.
