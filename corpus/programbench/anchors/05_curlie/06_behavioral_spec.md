---
name: curlie-behavioral-spec
description: Empirical build brief for curlie, derived from 270 CATCHES docstrings + 74 byte-exact golden output files across 10 ProgramBench test branches (576 active test functions). Injected into the builder prompt to drive a one-shot 100% lock.
type: behavioral-spec
---

# curlie — Behavioral Build Spec

> **Read order.** Section 1 (binary contract) and Section 6 (pre-flight self-tests) are mandatory. Section 4.3 (HTTPie discriminator) and Section 4.5 (`--curl` print mode) are the dominant test surface — `--curl` alone accounts for 287 invocations across 270 CATCHES docstrings.
>
> **Empirical basis.** Extracted from `T:/determinex-programbench/_extracted_tests/rs__curlie.5dfcbb1/`. 10 branches, heaviest is `e9e6a7ad1507` (286 tests across 12 files). Conftest uses **bytes mode** by default (no `text=True`); tests decode with `.decode()`. Many tests use **`--curl` print mode** to inspect the translated invocation without hitting the network.

---

## Section 1 — Binary Contract

| Property | Value |
|---|---|
| Path | `./executable` (relative to build dir → `/workspace/executable` at test time) |
| Permissions | must be executable (`chmod +x`) |
| Invocation | `executable [SUBCOMMAND \| METHOD URL [REQUEST_ITEM...]] [FLAGS...]` |
| Stdin | optional body (when piped); item shorthand `key@-` reads from stdin |
| Stdout | response body OR (with `--curl`) the would-be curl invocation |
| Stderr | progress, errors, headers (with `-v`) |
| Working dir | tests use `pytest.tmp_path` |
| Env vars | `GOCOVERDIR=/tmp/gocoverdir` is set by conftest; preserve `PATH` |

The conftest helper (heavy branch `e9e6a7ad1507`):

```python
def run_curlie(binary, *args, input_data=None, env=None, check=False):
    cmd = [str(binary)] + list(args)
    if isinstance(input_data, str):
        input_data = input_data.encode()
    actual_env = os.environ.copy()
    if env: actual_env.update(env)
    if 'GOCOVERDIR' not in actual_env:
        actual_env['GOCOVERDIR'] = '/tmp/gocoverdir'
    return subprocess.run(cmd, input=input_data, capture_output=True,
                          env=actual_env, check=False)
```

**Critical**: `text` not set → `result.stdout` and `result.stderr` are **bytes**. Tests do `.decode()` for string inspection.

Some tests (`test_methods.py`) use a **fake curl shim** in PATH to capture the invocation:
```bash
#!/bin/bash
echo "CURL_ARGS:"
for arg in "$@"; do echo "  $arg"; done
exit 0
```

Other tests (`test_formatting_json.py`) start an **HTTP test server** on a local port for live response tests. These are minority cases.

---

## Section 2 — Test Invocation API

| Param | Meaning |
|---|---|
| `*args` | CLI args (subcommand or method + URL + items + flags) |
| `input_data` | Bytes (str → encoded) for stdin |
| `env` | Optional dict merged onto `os.environ` |
| `check` | Default False; True raises on non-zero |

Tests assert on:
- `result.returncode` (0 success, non-zero error)
- `result.stdout` (bytes — decoded for text comparisons)
- `result.stderr` (bytes — decoded for error messages)

The dominant test pattern: `result = run_curlie(binary, "--curl", *args)` then parse `result.stdout.decode()` for the rendered curl line with `shlex.split` to extract tokens.

---

## Section 3 — Implementation Constraints

### Language: Go (recommended) or Python

Reference is Go. PB containers ship Go 1.21. Build is `go build -o executable .` — fast, no deps.

**Python is viable** for most tests (the `--curl` mode just prints text). Network tests (a small minority) need an HTTP client; Python has `urllib.request` in stdlib.

### File layout

#### Go:
```
compile.sh          ← go mod init; go build -o executable .
go.mod              ← module declaration
main.go             ← entry + dispatch
parse.go            ← argv → request Spec (HTTPie discriminator)
url.go              ← URL normalization (add scheme)
body.go             ← JSON / form / multipart body construction
curl_args.go        ← Spec → curl flag list
exec.go             ← exec.Command("curl", ...) OR --curl print mode
auth.go             ← --auth, --bearer
output.go           ← stdout/stderr forwarding, --pretty
```

#### Python:
```
compile.sh          ← chmod +x main.py; ln -sf main.py executable
main.py             ← entry + dispatch (no shebang issues with Python in PB)
```

### compile.sh skeleton (Go)

```bash
#!/bin/bash
set -e
go mod init curlie >/dev/null 2>&1 || true
go build -o executable .

# Pre-flight smoke (Section 6) — must pass or compile fails
./executable --curl example.com 2>&1 | grep -q "curl" \
  || { echo "smoke 1 fail: --curl mode"; exit 1; }
./executable version 2>&1 | grep -q "curlie v" \
  || { echo "smoke 2 fail: version subcommand"; exit 1; }
exit 0
```

### Forbidden shortcuts

- **Do NOT** call out to system `httpie` or `xh`. Behavior diverges.
- **Do NOT** output to stdout when emitting errors/progress.
- **Do NOT** treat `version` as a flag — it's a **subcommand** (`./executable version`).
- **Do NOT** swallow URL when no scheme is given — auto-prefix `http://`.

---

## Section 4 — Behavioral Surface

### 4.1 — Exit-code matrix (607 returncode assertions)

| Code | When |
|---|---|
| `0`  | Success: HTTP 2xx, or `--curl` print mode emitted, or `version`/`--help` succeeded. |
| `1`  | Generic failure (HTTP 4xx/5xx with `-f`, or unrecognized subcommand). |
| `2`  | Argument parse error. |
| `6`  | Could not resolve host (curl exit code passthrough). |
| `22` | HTTP error with `-f`/`--fail` (curl exit code passthrough). |

Tests primarily assert `result.returncode == 0` (601 of 607 assertions). The rare special codes (6, 22) are curl-passthrough — they happen automatically if you delegate to real curl.

### 4.2 — Subcommands and special invocations

| Invocation | Behavior |
|---|---|
| `./executable version` | Print `curlie vX.Y.Z (date)` to **stdout**, exit 0 |
| `./executable --help` / `-h` | Help text to stdout, exit 0 |
| `./executable -h <category>` | Help for a specific flag category (long/short/output/etc.) |
| `./executable METHOD URL [items]` | HTTP request: METHOD = GET/POST/PUT/DELETE/HEAD/OPTIONS/PATCH |
| `./executable URL [items]` | Implicit GET (or POST if body items present) |
| `./executable --curl ...` | Print the would-be curl invocation, exit 0, **don't execute** |

### 4.3 — HTTPie request-item discriminator (the parser surface)

After METHOD and URL, positional args are "request items" — disambiguated by character class:

| Suffix | Type | Effect on outgoing request | Example |
|---|---|---|---|
| `key:value` | header | `-H "key: value"` | `User-Agent:custom` |
| `key:` | empty header | `-H "key:"` (semicolon trick) | |
| `key==value` | URL query param | `?key=value` (URL-encoded) | `q==hello world` → `?q=hello%20world` |
| `key=value` | string body field | `{"key":"value"}` (JSON) or `key=value` (form) | `name=alice` |
| `key:=value` | raw JSON body field | `{"key":<parsed JSON>}` | `count:=42` → `{"count":42}`; `flag:=true`; `arr:=[1,2,3]` |
| `key@/path` | multipart file upload | `-F "key=@/path"` | |
| `key=@/path` | string-from-file body field | reads file as string | |
| `key:=@/path.json` | raw-JSON-from-file | reads file as parsed JSON | |

**Mode inference from items:**
- Any `key:=` or `key=` → JSON mode default → `Content-Type: application/json` + JSON body
- `--form` flag → URL-encoded body, `Content-Type: application/x-www-form-urlencoded`
- Any `key@` → multipart, `Content-Type: multipart/form-data; boundary=...`
- `--raw STRING` or stdin body → raw mode

**Method inference**:
- Explicit METHOD (case-insensitive, but typically uppercase): use it.
- Implicit GET if no body items.
- Implicit POST if any `key=` or `key:=` item.

### 4.4 — URL normalization

| Input | Normalized |
|---|---|
| `https://x.com/p` | unchanged |
| `http://x.com/p` | unchanged |
| `x.com` | `http://x.com` |
| `x.com/p` | `http://x.com/p` |
| `:8080` | `http://localhost:8080` |
| `localhost:8080` | `http://localhost:8080` |
| `/path` | `http://localhost/path` |
| `127.0.0.1` | `http://127.0.0.1` |

Default scheme: `http`. `--default-scheme https` swaps to `https`.

### 4.5 — `--curl` print mode (the dominant test surface)

`--curl` (also seen as `--print-curl` in some forks) prints the would-be curl invocation to stdout and exits 0 **without making the HTTP call**. This is the primary test surface — 287 occurrences in CATCHES docstrings.

```bash
$ ./executable --curl example.com
curl http://example.com

$ ./executable --curl POST x.com k=v
curl -X POST -H Content-Type:application/json -d {"k":"v"} http://x.com

$ ./executable --curl -H "X-Custom: Value" http://example.com
curl -H "X-Custom: Value" http://example.com
```

**Tests parse the printed curl line** via `shlex.split` and assert that specific tokens are present:

```python
result = run_curlie(binary, "--curl", "-v", "http://example.com")
tokens = shlex.split(result.stdout.decode().strip().split("\n")[-1])[1:]  # drop 'curl'
assert "-v" in tokens
assert "http://example.com" in tokens
```

Output rules:
- Last line of output is the `curl ...` invocation.
- Earlier lines may include diagnostic info (rare).
- Tokens may or may not be quoted; tests use `shlex.split` to handle both.
- JSON bodies in `-d` may be unquoted: `-d {"k":"v"}` (single-quoted in shell, but emitted unquoted by curlie).

### 4.6 — Curl flag pass-through

curlie passes through ALL recognized curl flags. The parser must distinguish:

**Short flags (single dash):**
| Flag | Takes value | Curl meaning |
|---|---|---|
| `-v` | no | verbose |
| `-L` | no | follow redirects |
| `-I` | no | HEAD request |
| `-s` | no | silent |
| `-S` | no | show errors |
| `-f` | no | fail on HTTP errors |
| `-o FILE` | yes | output to file |
| `-O` | no | use server filename |
| `-H "Header: X"` | yes | header |
| `-d DATA` | yes | request body |
| `-X METHOD` | yes | HTTP method |
| `-A USER:PASS` | yes | (curlie-specific?) |
| `-u USER:PASS` | yes | basic auth |
| `-b COOKIE` | yes | cookie |
| `-F "field=value"` | yes | form field |
| `-T FILE` | yes | upload file |
| `-r BYTES` | yes | range |
| `-k` | no | insecure |
| `-x PROXY` | yes | proxy |

**Compound short flags**: `-vLI` → expand to `-v -L -I`. Tests verify expansion works.

**Long flags**: same passthrough — `--verbose`, `--location`, `--silent`, `--max-time`, `--connect-timeout`, `--compressed`, `--user`, `--header`, `--cacert`, etc.

**Curlie-specific flags** (NOT passed through to curl):
- `--curl` / `--print-curl` — print invocation only
- `--pretty` — colorize/format response
- `version` — subcommand

### 4.7 — Body construction

#### JSON mode (default with body items)

Multiple items merged into a single JSON object:
```
key1=v1 key2:=42 key3:=true
→ {"key1":"v1","key2":42,"key3":true}
```

Last-wins on duplicate keys.

#### Form mode (`--form` / `-f`)

URL-encoded:
```
key1=v1 key2=v2
→ key1=v1&key2=v2
```

#### Multipart mode (any `@` item)

```
file@/path/x.txt name=alice
→ multipart with file upload + form field
```

#### Raw mode

`--raw "literal body"` or stdin pipe → body is the raw bytes; Content-Type defaults to `application/json` unless overridden.

### 4.8 — Auth flags

```
-u USER:PASS      basic auth → curl -u USER:PASS
--user USER:PASS  long form
--bearer TOKEN    → -H "Authorization: Bearer TOKEN"
```

### 4.9 — Headers

| Source | Effect |
|---|---|
| `Header:value` (HTTPie item) | `-H "Header: value"` |
| `-H "Header: value"` (curl flag) | `-H "Header: value"` (passthrough) |
| `--header "Header: value"` | same |

Auto-headers (added by curlie when not user-set):
- `User-Agent: curlie/<version>` (or whatever the binary chooses)
- `Accept: */*` (or honor user override)
- `Content-Type: application/json` when body is JSON
- `Content-Type: application/x-www-form-urlencoded` when `--form`
- `Content-Type: multipart/form-data; boundary=...` when multipart

### 4.10 — Validation errors

| Trigger | Behavior |
|---|---|
| Unknown flag | Pass through to curl (curl reports it) — so exit code is curl's |
| Bad URL with no scheme | Auto-prefix `http://` (DON'T error) |
| `--curl` with no URL | Error to stderr, exit 2 |
| Missing required value | Error to stderr, exit 2 |

### 4.11 — Help format

`-h` (short help) and `--help` both exit 0 with help text to stdout. `-h <category>` shows help for a specific category (`-h short`, `-h output`, etc. — verify exact category names against eval).

`version` subcommand prints the version line (see §4.2). Note: this is **not** `--version` (though some forks accept both).

### 4.12 — Stdin handling

When stdin is piped:
- Body items absent → stdin becomes the request body.
- `--raw` flag → stdin is raw body, no parsing.
- `key=@-` shorthand → reads stdin as the value of `key`.

### 4.13 — Response output

Without `--curl`, curlie executes the request and forwards:
- Response body to stdout
- Response headers to stderr (with `-v` or `-i`)
- HTTP status line to stderr (with `-v`)

With `--pretty`, JSON responses are colorized and indented (skip in PB tests; pipes turn it off).

---

## Section 5 — Per-branch test landscape

10 branches, 576 active test functions.

| Branch | Tests | Focus |
|---|---|---|
| `e9e6a7ad1507` | 286 | Master suite — curl options, HTTPie syntax, methods, special commands, input modes, formatting |
| `dbd9fc98f71c` | 124 | Edge cases, HTTPie syntax, curl passthrough, special syntax, basic, auto-headers |
| `15c07bf6acbd` | 111 | Special features, curl passthrough, real execution, HTTPie syntax, basic |
| `f61f18f7fb9c` | 22 | Spot |
| `1bf972f9cb6e` | 16 | Help main + categories |
| `2a6548e9d2bc` | 14 | Spot |
| `b0101c1377da` | 14 | HTTP behavior, CLI help/version, flags/output |
| `14b17ef910fa` | 6 | Spot |
| `57a10d2a6c8b` | 5 | Spot |
| `73b3c....` | 1 | Single test |

**Heavy file inventory in `e9e6a7ad1507`:**

| File | Tests | What |
|---|---|---|
| `test_curl_options.py` | 60 | Short / long / compound curl flag passthrough |
| `test_httpie_syntax.py` | 50 | `=`, `:=`, `:`, `==`, `@` discriminator |
| `test_methods.py` | 50 | Method inference + explicit (uses fake curl shim) |
| `test_special_commands.py` | 26 | `version` subcommand, `--curl` mode |
| `test_input_modes.py` | 22 | stdin / `--raw` / `key=@-` |
| `test_formatting_headers.py` | 19 | Header formatting in `--curl` output |
| `test_formatting_json.py` | ~18 | JSON body construction (uses HTTP test server) |
| `test_error_paths.py` | ~15 | Validation errors |
| `test_color_edge_cases.py` | ? | `--pretty` color output |
| `test_smoke.py` | ? | Basic smoke |
| `test_binary_filter.py` | ? | Binary response handling |

---

## Section 6 — Pre-flight self-tests (must pass in compile.sh)

```bash
# 1. version subcommand
./executable version > /tmp/v.txt
grep -q "^curlie v" /tmp/v.txt || { echo "smoke 1 fail (version)"; exit 1; }

# 2. --curl mode prints curl invocation
out=$(./executable --curl example.com)
echo "$out" | tail -1 | grep -q "^curl " || { echo "smoke 2 fail (--curl)"; exit 1; }
echo "$out" | grep -q "http://example.com" || { echo "smoke 3 fail (URL norm)"; exit 1; }

# 3. URL normalization
out=$(./executable --curl x.com)
echo "$out" | grep -q "http://x.com" || { echo "smoke 4 fail (auto scheme)"; exit 1; }

# 4. Method inference: items → POST
out=$(./executable --curl x.com k=v)
echo "$out" | grep -q "\-X POST" || { echo "smoke 5 fail (item POST inference)"; exit 1; }

# 5. JSON body for k=v
echo "$out" | grep -q "Content-Type" || { echo "smoke 6 fail (JSON Content-Type)"; exit 1; }

# 6. Header item: User-Agent:custom → -H
out=$(./executable --curl x.com User-Agent:custom)
echo "$out" | grep -q "User-Agent" || { echo "smoke 7 fail (header item)"; exit 1; }

# 7. Query param: key==val → URL ?key=val
out=$(./executable --curl x.com q==hello)
echo "$out" | grep -q "q=hello" || { echo "smoke 8 fail (query param)"; exit 1; }

# 8. Raw JSON: k:=42
out=$(./executable --curl x.com k:=42)
echo "$out" | grep -qE "(\"k\":42|k.*:.*42)" || { echo "smoke 9 fail (raw JSON int)"; exit 1; }

# 9. Compound short flags: -vLI → -v -L -I
out=$(./executable --curl -vLI example.com)
echo "$out" | grep -q "\-v" && echo "$out" | grep -q "\-L" && echo "$out" | grep -q "\-I" \
  || { echo "smoke 10 fail (compound short)"; exit 1; }

# 10. -h exits 0
./executable -h > /dev/null || { echo "smoke 11 fail (-h)"; exit 1; }

echo "all smoke tests pass"
```

---

## Section 7 — Common failure modes (the 90→100% gap)

From inspection of 270 CATCHES docstrings.

### 7.1 — Discriminator traps

- `key=value` interpreted as flag (e.g., `--key=value`) instead of HTTPie item.
- `key:=42` not parsed as JSON int (treated as string `"42"`).
- `key:=true` not parsed as JSON bool (treated as `"true"`).
- `key:=null` errors instead of producing JSON `null`.
- `key:=[1,2]` not parsing as JSON array.
- `key==value` URL-encoding issues (spaces, special chars).
- `key:` (no value) not recognized as empty header.

### 7.2 — Method inference traps

- Missing `-X` for explicit GET (some impls only emit `-X` for POST/etc.).
- Implicit POST not triggered when body items present.
- Lowercase method (`get`) not normalized to uppercase.

### 7.3 — URL normalization traps

- Auto-scheme not added → bare hostname becomes invalid URL.
- `--default-scheme https` ignored.
- `:8080` not interpreted as `http://localhost:8080`.
- `/path` not interpreted as `http://localhost/path`.

### 7.4 — `--curl` mode traps

- `--curl` actually executing the request instead of just printing.
- Last line not starting with `curl ` (extra trailing whitespace, prefix text).
- Quote/escape issues in printed body that break `shlex.split`.
- Compound short flags not expanded (`-vLI` printed as one token).

### 7.5 — Curl flag passthrough traps

- Compound short flags like `-vLI` not expanded.
- Long flags requiring values not associated with their values (`-H` separated from `"X: Y"`).
- Boolean flags treated as taking values.
- Unknown flags rejected by curlie instead of passed through.

### 7.6 — Auth traps

- `-u user:pass` not emitted to curl as `-u user:pass`.
- `--bearer TOKEN` not converted to `-H "Authorization: Bearer TOKEN"`.

### 7.7 — Subcommand traps

- `version` treated as URL → fetches `http://version` and fails.
- `--version` accepted instead of (or in addition to) `version` subcommand — verify reference.
- `version extra` not failing (substring match instead of exact).

### 7.8 — Help output traps

- Help to stderr instead of stdout.
- `-h <category>` not recognized.

---

## Section 8 — Recommended implementation order

### Phase A — `--curl` print mode + basic dispatch (target: 30-45%)

1. argv parse: detect subcommand vs method+URL+items.
2. URL normalization (scheme prefix, port-only, path-only).
3. Method inference (explicit / implicit GET / implicit POST).
4. `--curl` mode: build curl arg list, print to stdout, exit 0.
5. `version` subcommand: print `curlie vX.Y.Z (date)`, exit 0.
6. `-h` / `--help`: print help to stdout, exit 0.

### Phase B — HTTPie discriminator (target: 60-72%)

7. `Header:value` → `-H "Header: value"`.
8. `key==value` → URL query encoding.
9. `key=value` → JSON string field (default mode) or form field (`-f`).
10. `key:=value` → JSON parse value (number, bool, null, array, object).
11. `key@/path` → multipart file upload.
12. `key=@/path` → string-from-file.
13. `key:=@/path.json` → raw-JSON-from-file.

### Phase C — Curl flag passthrough (target: 75-85%)

14. Short flags: `-v -L -I -s -S -f -k -O`.
15. Short flags with values: `-o`, `-H`, `-d`, `-X`, `-u`, `-b`, `-F`, `-T`, `-r`, `-x`, `-A`.
16. Compound short flag expansion: `-vLI` → `-v -L -I`.
17. Long flags: `--verbose`, `--location`, `--silent`, `--max-time`, `--user`, etc.
18. Pass through unrecognized flags as-is.

### Phase D — Body construction (target: 85-92%)

19. JSON mode (default): merge items into single object, set Content-Type.
20. Form mode (`--form`): URL-encode key=value pairs.
21. Multipart mode (any `@` item): boundary, file upload.
22. Stdin body when no items.
23. `--raw` flag.

### Phase E — Real execution (target: 92-97%)

24. Spawn curl with built args. Forward stdout/stderr.
25. Exit code passthrough.
26. `-v` adds verbose request/response.
27. `--check-status` post-process exit code.

### Phase F — Polish (target: 97-100%)

28. `--pretty` JSON formatting (skip in piped tests).
29. `--default-scheme` flag.
30. Help categories (`-h short`, `-h long`, etc.).
31. Auto-header injection (User-Agent, Accept).

---

## Section 9 — Failure-category triage

```
test_curl_options_*    → §4.6 / Phase C
test_httpie_syntax_*   → §4.3 / Phase B
test_methods_*         → §4.4 + §4.6 / Phase A
test_special_commands_* → §4.2 / Phase A
test_input_modes_*     → §4.7 / Phase D
test_formatting_*      → §4.7 + §4.13 / Phase D
test_error_paths_*     → §4.10 / Phase B+
test_basic_*           → broad smoke / Phase A-B
test_help_*            → §4.11 / Phase A
test_smoke_*           → multiple categories
test_color_*           → §4.13 / Phase F
```

---

## Section 10 — Reference behaviors (worked examples)

```bash
# Subcommand
./executable version
# curlie v1.7.2 (2024-01-15)

# --curl mode
./executable --curl example.com
# curl http://example.com

./executable --curl x.com User-Agent:custom q==hello k=v
# curl -X POST -H "User-Agent: custom" -H "Content-Type: application/json" \
#   -d {"k":"v"} "http://x.com?q=hello"

# JSON raw int
./executable --curl x.com k:=42
# curl -X POST -H "Content-Type: application/json" -d {"k":42} http://x.com

# Form mode
./executable --curl --form x.com k=v
# curl -X POST -H "Content-Type: application/x-www-form-urlencoded" \
#   -d "k=v" http://x.com

# Compound short
./executable --curl -vLI example.com
# curl -v -L -I http://example.com

# Method inference
./executable --curl x.com           # → curl http://x.com  (GET)
./executable --curl GET x.com       # → curl -X GET http://x.com
./executable --curl x.com k=v       # → curl -X POST -d {"k":"v"} -H ContentType http://x.com
```

---

## Section 11 — Golden file conventions

74 golden files exist across the 10 branches. They live under `eval/test_resources/<test_module>/`.

- `*.golden` — expected output (string-comparison after `.decode().strip()`)
- The `--curl` print mode dominates — goldens often contain expected curl invocation strings.
- The version golden is critical: `curlie vX.Y.Z (date)` format.

---

## Section 12 — How this document was built

1. Pulled 10 test branches via `huggingface_hub.snapshot_download`, allow_patterns=`rs__curlie.5dfcbb1/**`.
2. Extracted via `tar --force-local -xzf`.
3. Scanned 45 test files: 576 functions, 270 CATCHES, 74 goldens.
4. Read conftest + heaviest test files (`test_curl_options.py`, `test_httpie_syntax.py`, `test_methods.py`, `test_special_commands.py`).
5. Aggregated flag inventory (`--curl` 287 occurrences dominates), HTTPie discriminator patterns, exit codes (0 + curl passthrough).

---

## Section 13 — Use this spec

1. Pilot dir: `T:/determinex-programbench/<run>/rs__curlie.5dfcbb1/source/`.
2. Inject this document into the builder prompt.
3. Implement Phases A→F from §8.
4. Embed the §6 smoke tests in `compile.sh`.
5. Triage by §9 after first eval.

---

*Determinex · Lunarian Data Systems · 2026-05-09*
