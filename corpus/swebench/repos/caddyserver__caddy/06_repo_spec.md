---
name: swebench-caddyserver__caddy
description: SWE-bench repo behavioral spec for caddyserver/caddy. Aggregated from 14 bug-fix instances across 1 dataset(s). Inject into builder prompt for SWE-bench tasks targeting this repo.
type: swebench-repo-spec
---

# caddyserver/caddy — SWE-bench Repo Spec

> **14 bug-fix instances** across 1 dataset(s); language(s): python.

## Section 1 — Dataset coverage

| Dataset | Instances |
|---------|-----------|
| swe-bench-multilingual-test | 14 |

## Section 2 — Where bugs typically live (top files touched in fixes)

| File | Times touched |
|------|---------------|
| `caddyconfig/caddyfile/lexer.go` | 5 |
| `replacer.go` | 2 |
| `caddyconfig/httpcaddyfile/addresses.go` | 1 |
| `caddyconfig/httpcaddyfile/options.go` | 1 |
| `modules/logging/filters.go` | 1 |
| `caddyconfig/caddyfile/dispenser.go` | 1 |
| `caddyconfig/caddyfile/parse.go` | 1 |
| `admin.go` | 1 |
| `modules/caddyhttp/reverseproxy/selectionpolicies.go` | 1 |
| `caddyconfig/httpcaddyfile/httptype.go` | 1 |
| `modules/caddypki/acmeserver/caddyfile.go` | 1 |
| `modules/caddyhttp/ip_matchers.go` | 1 |
| `cmd/main.go` | 1 |

## Section 3 — Test framework signal

Detected: **unknown — sample names: TestCaddyfileAdaptToJSON, TestCookieFilter, TestLexer, TestNestedImport, TestLexer**

Sample FAIL_TO_PASS test names (first 10):
```
  TestCaddyfileAdaptToJSON
  TestCookieFilter
  TestLexer
  TestNestedImport
  TestLexer
  TestUnsyncedConfigAccess
  TestUriReplace
  TestLexer
  TestCookieHashPolicyWithSecureRequest
  TestCaddyfileAdaptToJSON
```

## Section 4 — Problem-theme distribution

Top themes across 14 issue statements (auto-clustered):

| Theme | Count | % |
|-------|-------|---|
| config_environment | 4 | 28.6% |
| wrong_output | 3 | 21.4% |
| other | 2 | 14.3% |
| documentation | 2 | 14.3% |
| crash_or_traceback | 1 | 7.1% |
| regression | 1 | 7.1% |
| encoding_unicode | 1 | 7.1% |

## Section 5 — Sample issues (no patches — those are the answer)

### Sample 1 — `caddyserver__caddy-4774`

**Files likely affected**: `caddyconfig/httpcaddyfile/addresses.go`, `caddyconfig/httpcaddyfile/options.go`
**FAIL_TO_PASS** (1 tests, first 3): `['TestCaddyfileAdaptToJSON']`

**Problem statement (excerpt):**
> default_bind global option cannot accept multiple IP addresses I'm running Caddy 2.5.1 in a dual-stack server.
 I'd like to make Caddy bind by default to the IPv4 address and one main IPv6 address, and then customize certain sites to bind on other IPv6 addresses.
 
 '''text
 {
   default_bind [2001:db8:11:ad::80] 198.51.100.184
 }
 :33441 {
   respond "site 33441"
 }
 :33442 {
   bind [2001:db8:11

### Sample 2 — `caddyserver__caddy-4943`

**Files likely affected**: `modules/logging/filters.go`
**FAIL_TO_PASS** (1 tests, first 3): `['TestCookieFilter']`

**Problem statement (excerpt):**
> Unable to edit 'Cookie' in logs I have a fairly simple config:
 '''
 {
 	servers {
 		log_credentials
 	}
 }
 
 http://:8000 {
 	encode gzip
 
 	log {
 		format filter {
 			wrap json
 			fields {
 				request>headers>Cookie cookie {
 					replace sessionid REDACTED
 				}
 			}
 		}
 	}
 
 	route {
 		reverse_proxy /api/* web:8000
 		reverse_proxy /admin* web:8000
 	}
 }
 '''
 
 It is setup this 

### Sample 3 — `caddyserver__caddy-5404`

**Files likely affected**: `caddyconfig/caddyfile/lexer.go`
**FAIL_TO_PASS** (1 tests, first 3): `['TestLexer']`

**Problem statement (excerpt):**
> fuzz-tokenizer: Slice bounds out of range · caddyfile.(*lexer).next  Detailed Report: https://oss-fuzz.com/testcase?key=5119873601896448
 
 Project: caddy
 Fuzzing Engine: libFuzzer
 Fuzz Target: fuzz-tokenize
 Job Type: libfuzzer_asan_caddy
 Platform Id: linux
 
 Crash Type: Slice bounds out of range
 Crash Address: 
 Crash State:
   caddyfile.(*lexer).next
   caddyfile.Tokenize
   caddyfile.Fuzz

### Sample 4 — `caddyserver__caddy-5626`

**Files likely affected**: `caddyconfig/caddyfile/dispenser.go`, `caddyconfig/caddyfile/parse.go`, `caddyconfig/caddyfile/lexer.go`
**FAIL_TO_PASS** (1 tests, first 3): `['TestNestedImport']`

**Problem statement (excerpt):**
> Caddy 2.7.0-beta.2: nested imports in handler broken (again) I think the same problem problem existed before (#4914) but was supposed to be fixed. It actually worked in beta.1 but is now broken again. The following example fails:
 
 '''caddyfile
 (responderWithStatus) {
 	respond {args[0]} {args[1]}
 }
 
 (responder) {
 	import responderWithStatus {args[0]} 202
 }
 
 http://127.0.0.1:8080 {
 	hand

### Sample 5 — `caddyserver__caddy-5761`

**Files likely affected**: `caddyconfig/caddyfile/lexer.go`
**FAIL_TO_PASS** (1 tests, first 3): `['TestLexer']`

**Problem statement (excerpt):**
> caddy template cannot use << >>? Caddyfile
 '''
 localhost {
   templates {
     between <<  >>
   }
 }
 '''
 
 error:
 
 '''
 Error: adapting config using caddyfile: heredoc marker on line #3 must contain only alpha-numeric characters, dashes and underscores; got '  >>'
 ''' 

### Sample 6 — `caddyserver__caddy-5870`

**Files likely affected**: `admin.go`
**FAIL_TO_PASS** (1 tests, first 3): `['TestUnsyncedConfigAccess']`

**Problem statement (excerpt):**
> API, UX: return 4xx on invalid input for delete method Caddy : v2.7.4 + (master)
 OS: Ubuntu 22.04
 Module: API
 
 **Issue**:
 When I delete a non-existing listener, Caddy returns '200' instead of '4xx'.
 
 **Reproduce**:
 
 1. caddy run (no config)
 2. Add a route:
 
 'hello.json'
 
 '''json
 {
   "apps": {
     "http": {
       "servers": {
         "example": {
           "listen": [":2015"],
 

### Sample 7 — `caddyserver__caddy-5995`

**Files likely affected**: `replacer.go`
**FAIL_TO_PASS** (1 tests, first 3): `['TestUriReplace']`

**Problem statement (excerpt):**
> Caddy 2.7: uri replace does not work with closing brackets ( '}' ) Hi,
 
 I'm using caddy to sanitize URIs. 
 
 I created a rule in Caddyfile to replace bad encoded brackets with the correct encoding, but it's not working with closing brackets.
 
 I think this is a bug because I tried to escape the brackets in Caddyfile following the rules in https://caddyserver.com/docs/caddyfile/concepts#tokens-

### Sample 8 — `caddyserver__caddy-6051`

**Files likely affected**: `caddyconfig/caddyfile/lexer.go`
**FAIL_TO_PASS** (1 tests, first 3): `['TestLexer']`

**Problem statement (excerpt):**
> Allow blank lines in Heredoc I want to send some blank lines in the respond.
 
 '''caddyfile
 example.com {
 	handle {
 		respond <<EOF
 			The next line is a blank line
 
 			The previous line is a blank line
 			EOF 200
 	}
 }
 '''
 
 But I got Error: adapting config using caddyfile: mismatched leading whitespace in heredoc <<EOF on line #5 [], expected whitespace [			] to match the closing mark

## Section 6 — Builder guidance

When building a fix for an instance in caddyserver/caddy:

1. **Read the problem statement carefully** — the issue text describes the bug and often hints at root cause.
2. **Likely files**: see §2 above. caddyconfig/caddyfile/lexer.go appears in most fixes.
3. **Run the FAIL_TO_PASS tests** to see the failure first (`pytest <test_name> -v`).
4. **Inspect surrounding code** at the file paths from §2 — common bug locations.
5. **Match the theme** (§4) to known repo patterns: regression vs edge case vs API change.
6. **Generate minimal patch** — SWE-bench scoring rewards smallest viable fix.
7. **Verify PASS_TO_PASS still pass** — don't break existing functionality.

## Section 7 — Index of all instances in this repo

All 14 instance_ids live in `c:/tmp/swebench_instance_index.jsonl` (filterable by `repo == "caddyserver/caddy"`).

First 20 instance_ids:

- `caddyserver__caddy-4774` (dataset: `swe-bench-multilingual-test`)
- `caddyserver__caddy-4943` (dataset: `swe-bench-multilingual-test`)
- `caddyserver__caddy-5404` (dataset: `swe-bench-multilingual-test`)
- `caddyserver__caddy-5626` (dataset: `swe-bench-multilingual-test`)
- `caddyserver__caddy-5761` (dataset: `swe-bench-multilingual-test`)
- `caddyserver__caddy-5870` (dataset: `swe-bench-multilingual-test`)
- `caddyserver__caddy-5995` (dataset: `swe-bench-multilingual-test`)
- `caddyserver__caddy-6051` (dataset: `swe-bench-multilingual-test`)
- `caddyserver__caddy-6115` (dataset: `swe-bench-multilingual-test`)
- `caddyserver__caddy-6288` (dataset: `swe-bench-multilingual-test`)
- `caddyserver__caddy-6345` (dataset: `swe-bench-multilingual-test`)
- `caddyserver__caddy-6350` (dataset: `swe-bench-multilingual-test`)
- `caddyserver__caddy-6370` (dataset: `swe-bench-multilingual-test`)
- `caddyserver__caddy-6411` (dataset: `swe-bench-multilingual-test`)

---

*Determinex · Lunarian Data Systems · auto-generated from SWE-bench-family datasets*
