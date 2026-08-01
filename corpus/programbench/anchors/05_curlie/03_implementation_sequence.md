---
name: curlie-impl-sequence
description: curlie build order. URL normalization first; argument discriminator second; body construction third; the rest is plumbing. Easiest anchor to lock — projected 4-6 attempts.
type: implementation-sequence
---

# curlie — Implementation Sequence

> **Smallest anchor by test count (741) and rated easy.** Lock target: 4-6 attempts. Use `--offline` mode for offline test-driving the parser before connecting curl exec.

## Phase A — Argument scaffolding (target: 30-45%)

1. **Argv parsing**: separate flags from positionals. First positional may be METHOD, second is URL. Gate: `curlie x.com` parses as method=GET, url=x.com.
2. **URL normalization**: add `http://` if no scheme. Gate: `x.com` → `http://x.com`; `:8080` → `http://localhost:8080`.
3. **Method inference**: explicit METHOD overrides; body items promote to POST. Gate: matrix from fuzzing-surface.
4. **`--offline` mode**: print the would-be curl invocation, exit 0. Gate: every later test can be driven from `--offline` output without network.

## Phase B — Request item discriminator (target: 60-75%)

5. **Header `key:value`**: trim leading space in value; trailing space preserved.
6. **URL param `key==value`**: append to query string, URL-encoded.
7. **String field `key=value`**: stage for body.
8. **Raw JSON field `key:=value`**: parse value as JSON; error if invalid JSON.
9. **File upload `key@/path`**: stage for multipart.
10. **String-from-file `key=@/path`**: read file, treat as string field.
11. **Raw-JSON-from-file `key:=@/path.json`**: read file, parse as JSON, treat as raw value.

Gate: every row of the discriminator matrix produces the right Spec internal structure.

## Phase C — Body construction (target: 78-87%)

12. **JSON mode** (default when any non-header item, no `--form`): build `{"k1":"v1","k2":42}` body. Set `Content-Type: application/json`.
13. **Form mode** (`-f`/`--form`): URL-encode `k1=v1&k2=v2` body. `Content-Type: application/x-www-form-urlencoded`.
14. **Multipart mode** (any `@` item OR `--multipart`): build multipart body with random boundary. Set `Content-Type: multipart/form-data; boundary=...`.
15. **Raw stdin body**: when no body items present and stdin is not TTY, read stdin as body. JSON mode applies if Content-Type already implied.

Gate: each mode produces correct curl invocation in `--offline`.

## Phase D — Auth + output flags (target: 88-93%)

16. **`-a USER:PASS` / `--auth`**: pass `-u USER:PASS` to curl.
17. **`--bearer TOKEN`**: add `Authorization: Bearer TOKEN` header.
18. **`-o FILE` / `--output`**: pass through to curl.
19. **`-d` / `--download`**: pass `-O` (use server filename) to curl.
20. **`-v` / `--verbose`**: pass `-v` to curl, also include curlie's own request trace if reference has one.
21. **`--check-status`**: post-process curl's exit code (any HTTP 4xx/5xx → exit 1).

## Phase E — Network execution (target: 94-97%)

22. **Spawn curl with built args**. Forward stdout/stderr/stdin.
23. **Pretty-print response if JSON + TTY**. Skip in PB tests (always pipes).
24. **Exit code passthrough**: curl's exit becomes curlie's exit.

## Phase F — Edge sweep (target: 98-100%)

25. **Empty values** in form/JSON: `k=` → `{"k":""}`.
26. **Repeated keys** in form mode: `tag=a tag=b` → `tag=a&tag=b` (both).
27. **Repeated keys** in JSON mode: last-wins (HTTPie convention).
28. **Quoted shell args** in `--offline` output: shell-safe single-quote with `'\''` for embedded quotes.
29. **`--default-scheme https`** alters the URL normalizer.
30. **`--http1.1`, `--http2`** pass through to curl.
31. **`--insecure` / `-k`** passes to curl.
32. **`--proxy URL`** passes to curl.
33. **`--timeout N`** passes as `--max-time N` to curl.
34. **Stdin body with `@-`**: `key=@-` reads stdin as the value of `key`.
35. **Empty stdin**: don't include body if stdin is empty AND no positional body items.

## The 90→100% gap

Where curlie's tail typically lives:

1. **`--offline` curl invocation byte-perfect format.** Quote rules, flag order, body indentation. Tests likely string-compare; one extra space breaks 30+ tests.
2. **Header ordering in the printed invocation.** HTTPie convention: `Host` first, then user-supplied headers in insertion order, then implicit ones (Content-Type, Authorization).
3. **Multipart boundary**: tests likely accept any boundary but must produce a syntactically correct multipart body. Verify the Content-Type's `boundary=` parameter quoting.
4. **JSON body whitespace**: compact `{"k":"v"}` vs pretty `{"k": "v"}` — verify which the reference emits.
5. **`:=` parsing edge**: `k:=foo` (unquoted bareword) → error (not valid JSON). `k:=null`, `k:=true`, `k:=false` work; `k:=undefined` errors.
6. **URL-encoding charset**: `k==hello world` → `k=hello%20world`. RFC 3986 percent-encoding.
7. **`Content-Length` header** auto-injection when sending body via stdin pipe.
8. **Exit code 0 on a 404** WITHOUT `--check-status`. Tests may verify this.
9. **`--auth user:`** (empty pass): curl handles as empty-pass; verify.
10. **`--print` flag combinations**: `--print=Hh` (uppercase H = response headers, lowercase h = request headers) order matters for output.

## Failure-category triage

```
Group A — Argument discriminator (parser) bugs
Group B — URL normalization
Group C — Body construction (JSON / form / multipart)
Group D — Auth / output flag plumbing
Group E — `--offline` output format
Group F — Exit code mapping
```

Group A and E together account for ~70% of expected failures (~520 tests). Lock those before touching anything else.

## Why this anchor locks fast

1. No novel data structures.
2. No novel algorithms.
3. The reference is well-documented (HTTPie's docs apply nearly verbatim).
4. The implementation is largely a `match` statement over argv and a curl-args builder.
5. Network tests can be driven via `--offline` mode entirely — fast feedback loops.

**Expected lock**: 4-6 attempts, 30-50 minutes wall clock, ~40 training rows emitted.
