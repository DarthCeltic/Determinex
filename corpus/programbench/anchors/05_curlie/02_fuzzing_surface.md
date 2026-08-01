---
name: curlie-fuzzing-surface
description: Specific testable behaviors in curlie. Argument-discriminator matrix, URL normalization rules, body-mode inference, exit-code passthrough.
type: fuzzing-surface
---

# curlie — Fuzzing Attack Surface

741 tests across 10 branches. The 286-test branch likely covers argument discrimination + body mode. The 159-test and 124-test branches likely cover URL normalization + exit-code passthrough.

## Argument-discriminator matrix (the core surface)

| Syntax | Item type | JSON mode produces | Form mode produces |
|--------|-----------|--------------------|--------------------|
| `key:value` | header | `Header: key: value` | same |
| `key:` | header (empty) | `Header: key:` | same |
| `key:` (no value, ends with semicolon: `key;`) | header (literal empty) | tested separately |
| `key==value` | URL query | `?key=value` (URL-encoded) | same |
| `key=value` | string field | `{"key":"value"}` | `key=value` |
| `key:=42` | raw JSON int | `{"key":42}` | error or `key=42` |
| `key:=true` | raw JSON bool | `{"key":true}` | |
| `key:=null` | raw JSON null | `{"key":null}` | |
| `key:=[1,2]` | raw JSON array | `{"key":[1,2]}` | |
| `key:={"a":1}` | raw JSON obj | `{"key":{"a":1}}` | |
| `key@/path/file` | file upload (multipart) | n/a | (forces multipart) |
| `key=@/path/file` | string-from-file | `{"key":"<contents>"}` | `key=<contents>` |
| `key:=@/path.json` | raw-JSON-from-file | `{"key":<parsed>}` | n/a |

## URL normalization rules

| Input | Normalized |
|-------|-----------|
| `https://x.com/p` | unchanged |
| `http://x.com/p`  | unchanged |
| `x.com`           | `http://x.com` |
| `x.com/p`         | `http://x.com/p` |
| `:8080`           | `http://localhost:8080` |
| `/path`           | `http://localhost/path` |
| `localhost:8080`  | `http://localhost:8080` |
| `127.0.0.1`       | `http://127.0.0.1` |
| `[::1]:80`        | `http://[::1]:80` |
| `::1` (no brackets) | error or `http://::1` (verify against reference) |

If a `--default-scheme=https` flag exists, swap the default. Verify.

## Method inference rules

| Args | Inferred method |
|------|-----------------|
| `curlie example.com` | GET |
| `curlie example.com k=v` | POST |
| `curlie GET example.com` | GET |
| `curlie POST example.com` | POST |
| `curlie post example.com` | POST (case-insensitive) |
| `curlie example.com Header:value` | GET (headers don't trigger POST) |
| `curlie example.com k==v` | GET (query params don't trigger POST) |
| `curlie --json example.com k=v` | POST (`--json` forces JSON mode) |
| `curlie --form example.com k=v` | POST (`--form` body) |

## CLI flag matrix

### Mode flags
- `-j` / `--json` (default mode)
- `-f` / `--form` (URL-encoded body)
- `--multipart` (force multipart)
- `--raw STRING` / stdin body

### Auth
- `-a USER:PASS` / `--auth USER:PASS`
- `-A TYPE` / `--auth-type basic|digest|bearer`
- `--bearer TOKEN`

### Output
- `-d` / `--download` save to file
- `-o FILE` / `--output FILE`
- `-c` / `--continue` resume
- `--pretty all|format|none|colors`
- `-S` / `--style PYG_STYLE` syntax theme
- `-v` / `--verbose`
- `-q` / `--quiet`
- `--print STRING` (which parts to print: `H` headers, `B` body, `r` request, `R` response)
- `-h` / `--headers` (alias for `--print=h`)
- `-b` / `--body` (alias for `--print=b`)

### HTTP protocol
- `--http1.0`, `--http1.1`, `--http2`, `--http3`
- `-k` / `--insecure`
- `--cert FILE`, `--key FILE`
- `--proxy URL`
- `--timeout SECONDS`
- `--follow` / `-F` redirect-following (not the same as `-f` for form!)
- `--max-redirects N`

### Special
- `--offline` / `--print-curl` print equivalent curl command, don't run
- `--curl` print the underlying curl args
- `--default-scheme http|https`
- `--check-status` (raise on >=400)

## Body-construction edges

### JSON mode
- Top-level body is always an object: `{"k1":"v1","k2":42}`
- Numbers via `:=`: `count:=10` → `{"count":10}` (NOT `"10"`)
- Booleans via `:=`: `flag:=true`
- Nested objects: `meta:={"a":1}`
- Repeated keys → last-wins

### Form mode
- URL-encoded: `key%201=val%26ue`
- Repeated keys → both included: `tag=a&tag=b`

### Multipart mode
- Any `@` triggers it
- Boundary: random; tests probably check Content-Type header presence + filename header

## Output format edges (where 90→100% lives)

1. **`--offline` output exactly matches `curl ARGS` invocation.** This is heavily tested. Quoting in the printed command must be shell-safe.
2. **Header order in output.** HTTPie/curlie sort headers in a specific way (Host first, then alphabetic? verify reference). Tests likely compare exact ordering.
3. **JSON body indentation in `--offline`.** Compact vs pretty.
4. **Auth header injection** — `--auth u:p` becomes `Authorization: Basic <base64>` OR remains as curl flag `-u u:p`. curlie does the latter; verify.
5. **`--bearer TOKEN`** becomes `Authorization: Bearer TOKEN`.
6. **Stdin body**: `echo '{"x":1}' | curlie post example.com` reads stdin when no positional body items. JSON mode by default.
7. **`@-` placeholder** — file path `-` means stdin. `key=@-` reads stdin into `key`.

## Exit codes

- 0: success (HTTP 2xx, or 3xx without `--check-status`, or any if `--check-status` not set)
- 1: HTTP-level failure with `--check-status` (any 4xx/5xx)
- 2: usage error
- 3: bad URL
- 4: connection error (passes through curl's exit 7)
- 5: redirect limit
- Otherwise curl's exit code passed through directly

## Stderr

- Errors prefixed `curlie: ` (verify reference).
- Pass through curl's stderr unchanged on network errors.
- `-v` adds verbose request/response trace.

## Testable surprise behaviors

1. **`curlie x.com k=v`** — implicit POST, JSON body `{"k":"v"}`.
2. **`curlie x.com k:=null`** — JSON body `{"k":null}`, NOT empty.
3. **`curlie x.com k==`** — empty query value: `?k=`.
4. **`curlie -f x.com k=v k=w`** — form body `k=v&k=w`.
5. **`curlie -f x.com k:=42`** — `k=42` (stringified).
6. **`curlie x.com User-Agent:`** — empty value sends `User-Agent:` header (different from suppressing it).
7. **`curlie --offline x.com k=v`** — print `curl -X POST -H 'Content-Type: application/json' -d '{"k":"v"}' http://x.com` (or similar).
8. **`curlie -a u:p x.com`** — basic auth.
9. **`curlie x.com k:='[1,2,3]'`** — JSON array as value.
10. **`curlie x.com k:='{"nested":"obj"}'`** — JSON object as value.

## Likely test name structure

- `test_url_normalization_*` (scheme, port, path)
- `test_method_inference_*` (implicit GET vs POST)
- `test_request_item_string`, `test_request_item_raw_json`, `test_request_item_header`, `test_request_item_query`
- `test_request_item_file_upload`, `test_request_item_string_from_file`, `test_request_item_json_from_file`
- `test_form_mode`, `test_json_mode_default`, `test_multipart_mode`
- `test_auth_basic`, `test_bearer_token`
- `test_offline_mode_output`
- `test_exit_code_passthrough`, `test_check_status`
- `test_stdin_body`, `test_pretty_print`
