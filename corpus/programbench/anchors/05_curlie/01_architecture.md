---
name: curlie-architecture
description: Architecture for curlie. Translate HTTPie-style positional args into curl flags; exec curl. Two-step pipeline; minimal state.
type: architecture
---

# curlie — Architecture Blueprint

## Language choice

**Go.** Justification:
1. Reference is Go; matches PB image and cargo-free build.
2. `os/exec` provides clean curl invocation; stdout/stderr forwarding is straightforward.
3. PB containers ship `curl` (universal in Linux base images). curlie's whole purpose is to be a thin wrapper, not a new HTTP client.
4. Static binary builds in seconds.

Alternative: Python with `subprocess.run`. Equally viable; slightly slower iteration since shebang+chmod is less natural than `go build`.

## Core data structures

### `Spec` — the translated invocation
```go
type Spec struct {
    Method      string         // GET, POST, PUT, DELETE, etc.
    URL         string         // normalized (scheme added if missing)
    Headers     []Header       // [{Key, Value}, ...]
    QueryParams []KV           // ?k=v
    FormFields  []KV           // -d k=v (URL-encoded)
    JSONFields  []JSONField    // JSON body construction (key=v as string, key:=v as raw JSON)
    Files       []FileField    // multipart upload (key@path)
    BodyRaw     []byte         // when --raw or stdin body
    Auth        *Auth          // basic / bearer
    Curlflags   []string       // pass-through curl flags
    Mode        Mode           // JSON, Form, Multipart, Raw
}

type Auth struct { User, Pass string; Bearer string }
type KV struct { Key, Value string }
type Header struct { Key, Value string }
type JSONField struct { Key string; Value any /* parsed JSON or string */ }
type FileField struct { Key, Path string }
```

### `Args` — input parsing
HTTPie-style:
```
[METHOD] URL [REQUEST_ITEM ...]
```

`REQUEST_ITEM` discriminator (the heart of the tool):
| Suffix | Type | Example | Effect |
|--------|------|---------|--------|
| `:`    | header | `User-Agent:foo` | sets header |
| `==`   | URL param | `q==hello` | adds `?q=hello` |
| `=`    | form/json field (string) | `name=alice` | becomes `{"name":"alice"}` in JSON mode |
| `:=`   | json field (raw JSON) | `count:=42` | becomes `{"count":42}` (number) |
| `@`    | file upload (multipart) | `file@/path/x.txt` | multipart with file |
| `=@`   | string-from-file | `bio=@bio.txt` | reads file as string into JSON/form value |
| `:=@`  | raw-json-from-file | `meta:=@meta.json` | reads file as JSON value |

Mode is inferred from item types:
- Any `@` (multipart file) → Multipart mode
- Any `:=` or `=` AND no `@` → JSON mode (default)
- `--form` flag → Form mode (URL-encoded body, not JSON)
- `--raw` or stdin body → Raw mode

## Module breakdown (Go)

```
cmd/curlie/main.go     entrypoint
parse.go               argv → Spec; HTTPie-syntax discrimination
url.go                 URL normalization (add scheme, host validation)
body.go                JSON/form/multipart body construction
curl.go                Spec → curl-flag list; exec curl
auth.go                --auth user:pass or user-only (then prompts? skip in batch)
output.go              passthrough; --pretty; --offline
errors.go              messages + exit codes
```

## Build script

`compile.sh`:
```bash
#!/bin/bash
set -e
go mod init curlie >/dev/null 2>&1 || true
go build -o executable .
chmod +x executable
```

No external deps strictly required (stdlib `os/exec`, `flag`, `encoding/json`, `net/url`, `strings`). If using `cobra` for CLI, `go mod tidy` will pull it.

## Critical implementation decisions

### Decision 1: Shell out to `curl`, don't reimplement HTTP
curlie's whole *purpose* is to be a curl wrapper. PB tests likely verify the translated curl invocation OR the response body. Either way, delegating to real curl is the correct architecture.

```go
func runCurl(spec Spec) (int, error) {
    args := spec.toCurlArgs()
    cmd := exec.Command("curl", args...)
    cmd.Stdout = os.Stdout
    cmd.Stderr = os.Stderr
    if err := cmd.Run(); err != nil {
        if ee, ok := err.(*exec.ExitError); ok {
            return ee.ExitCode(), nil
        }
        return 1, err
    }
    return 0, nil
}
```

### Decision 2: --offline mode prints the curl invocation, doesn't run it
Tests may verify the translation logic via `--offline` (HTTPie has this; verify curlie has equivalent — likely `--print-curl` or similar). Implement this *first* — it makes test-driving the parser without network calls trivial.

### Decision 3: URL normalization
- Bare host `example.com` → `http://example.com` (default scheme)
- `:8080` (just port) → `http://localhost:8080`
- `/path` → `http://localhost/path`
- Already-schemed URL → unchanged

This is testable independently of network.

### Decision 4: Method inference
- If first positional is one of `GET POST PUT DELETE HEAD OPTIONS PATCH TRACE CONNECT`, treat as method.
- Else: implicit `GET` if no body items, implicit `POST` if any body items.
- `-j`/`--json` and `-f`/`--form` toggle body modes but don't change implicit method.

### Decision 5: Header parsing edge
`User-Agent:foo bar` is `User-Agent: foo bar` (leading space trimmed but trailing kept).
`X-Empty;` (semicolon trick) sends empty header. Verify curlie supports this.

### Decision 6: Body construction
**JSON mode** (default with `=` or `:=` items):
```json
{"key1": "value1", "key2": 42}
```
- `=` produces string value
- `:=` parses value as JSON (number, bool, null, array, object)

**Form mode** (`--form` flag):
```
key1=value1&key2=42
```
- All values URL-encoded
- `:=` items still parse as JSON but stringified

**Multipart mode** (any `@` item):
- `Content-Type: multipart/form-data; boundary=...`
- Each `=` is a form field; `@` is a file upload

### Decision 7: Authentication
- `--auth user:pass` → `-u user:pass` to curl
- `--auth user` → curl prompts on TTY (PB pipes always — likely error or skip)
- `--auth-type basic|digest|bearer` → maps to curl auth flag

### Decision 8: Pretty output
curlie/HTTPie pretty-print response by default if it's JSON and output is TTY. **PB pipes always** — pretty-print is auto-disabled. Honor `--pretty=all|format|none|colors` flags if tested.

### Decision 9: Exit code passthrough
curlie's exit code = curl's exit code. curl exit codes are documented (0=success, 6=could not resolve, 7=could not connect, 22=HTTP error with `-f`, etc.).

## Edge cases to bake in early

1. **No URL** → error `usage: curlie [METHOD] URL [REQUEST_ITEMS]`
2. **METHOD with lowercase** — `get example.com` should still work as `GET`.
3. **Body items with implicit GET** — should auto-promote to POST.
4. **Empty value** — `key=` is `{"key": ""}` (empty string, not null).
5. **Repeated keys** — `tag=a tag=b` either becomes `{"tag":"b"}` (last-wins) or `{"tag":["a","b"]}` (array). HTTPie default: last-wins. Verify in curlie.
6. **Special chars in keys** — `User-Agent:foo` (header), `Mr.X=alice` (form field with dot in key — quoting matters).

## What NOT to implement (defer)

- Cookie jar persistence — verify in eval before building.
- Sessions / named profiles — almost certainly out of test scope.
- Plugin system — out of scope.
- Stream printing — pass through curl's `-N`.
- HTTP/2 / HTTP/3 specific flags — pass through to curl unchanged.
