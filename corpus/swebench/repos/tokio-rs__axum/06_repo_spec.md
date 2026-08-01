---
name: swebench-tokio-rs__axum
description: SWE-bench repo behavioral spec for tokio-rs/axum. Aggregated from 7 bug-fix instances across 1 dataset(s). Inject into builder prompt for SWE-bench tasks targeting this repo.
type: swebench-repo-spec
---

# tokio-rs/axum — SWE-bench Repo Spec

> **7 bug-fix instances** across 1 dataset(s); language(s): python.

## Section 1 — Dataset coverage

| Dataset | Instances |
|---------|-----------|
| swe-bench-multilingual-test | 7 |

## Section 2 — Where bugs typically live (top files touched in fixes)

| File | Times touched |
|------|---------------|
| `axum/CHANGELOG.md` | 7 |
| `axum/src/routing/mod.rs` | 6 |
| `axum/src/routing/route.rs` | 3 |
| `axum-extra/src/routing/mod.rs` | 2 |
| `axum/src/routing/method_routing.rs` | 2 |
| `axum/src/routing/future.rs` | 2 |
| `axum/src/routing/path_router.rs` | 2 |
| `axum-extra/CHANGELOG.md` | 1 |
| `axum/src/extract/matched_path.rs` | 1 |
| `axum/src/response/redirect.rs` | 1 |
| `examples/oauth/Cargo.toml` | 1 |
| `examples/oauth/src/main.rs` | 1 |
| `axum-extra/src/routing/resource.rs` | 1 |

## Section 3 — Test framework signal

Detected: **unknown — sample names: routing::tests::wildcard_with_trailing_slash, routing::tests::not_found_for_extra_trailing_slash, routing::tests::not_found_for_missing_trailing_slash, routing::tests::fallback::doesnt_panic_if_used_with_nested_router, routing::tests::fallback::issue_2072**

Sample FAIL_TO_PASS test names (first 10):
```
  routing::tests::wildcard_with_trailing_slash
  routing::tests::not_found_for_extra_trailing_slash
  routing::tests::not_found_for_missing_trailing_slash
  routing::tests::fallback::doesnt_panic_if_used_with_nested_router
  routing::tests::fallback::issue_2072
  routing::tests::fallback::issue_2072_outer_fallback_after_merge
  routing::tests::fallback::merge_router_with_fallback_into_nested_router_with_fallback
  routing::tests::fallback::merging_nested_router_with_fallback_into_router_with_fallback
  routing::tests::wildcard_with_trailing_slash
  routing::tests::with_trailing_slash_post
```

## Section 4 — Problem-theme distribution

Top themes across 7 issue statements (auto-clustered):

| Theme | Count | % |
|-------|-------|---|
| other | 3 | 42.9% |
| wrong_output | 2 | 28.6% |
| regression | 1 | 14.3% |
| documentation | 1 | 14.3% |

## Section 5 — Sample issues (no patches — those are the answer)

### Sample 1 — `tokio-rs__axum-1119`

**Files likely affected**: `axum/src/routing/route.rs`, `axum/CHANGELOG.md`, `axum/src/routing/mod.rs`, `axum-extra/CHANGELOG.md`, `axum-extra/src/routing/mod.rs`
**FAIL_TO_PASS** (3 tests, first 3): `['routing::tests::wildcard_with_trailing_slash', 'routing::tests::not_found_for_extra_trailing_slash', 'routing::tests::not_found_for_missing_trailing_slash']`

**Problem statement (excerpt):**
> Consider removing support for trailing slash redirects If you define a route like '.route("/foo", _)' and someone calls '/foo/' axum will issue a redirect response to '/foo'. Same goes if you define '/foo/' and someone calls '/foo'. If both routes are defined (i.e. '/foo/' and '/foo') axum will not redirect between them.
 
 We've had this feature since 0.3.0 (since moving to 'matchit') but I've st

### Sample 2 — `tokio-rs__axum-1730`

**Files likely affected**: `axum/src/routing/route.rs`, `axum/CHANGELOG.md`, `axum/src/routing/method_routing.rs`, `axum/src/routing/future.rs`
**FAIL_TO_PASS** (0 tests, first 3): `[]`

**Problem statement (excerpt):**
> 'MethodRouter' fallbacks that require 'State' are inconvenient If you want a fallback that only accepts 'GET' and responds with '404 Not Found' for everything else you can do this
 
 '''rust
 router
     .fallback_service(get(fallback).fallback(not_found))
 '''
 
 but if 'fallback' requires state you end up doing something like this
 
 '''rust
 router
     .fallback_service(
         get(fallback)

### Sample 3 — `tokio-rs__axum-1934`

**Files likely affected**: `axum/CHANGELOG.md`, `axum/src/routing/path_router.rs`, `axum/src/routing/mod.rs`, `axum/src/extract/matched_path.rs`
**FAIL_TO_PASS** (1 tests, first 3): `['routing::tests::fallback::doesnt_panic_if_used_with_nested_router']`

**Problem statement (excerpt):**
> Axum 0.6.15 seems to break ServeDir completely - [x] I have looked for existing issues (including closed) about this
 
 ## Bug Report
 
 ### Version
 
 'cargo tree | grep axum'
 '''
 axum v0.6.15
 │   ├── axum-core v0.3.4
 │   ├── axum-core v0.3.4
 '''
 'cargo tree | grep tower-http'
 '''
 tower-http
 ├── tower-http v0.4.0
 '''
 
 > Note: With axum 'v0.6.12' the exact same code works as epxected
 

### Sample 4 — `tokio-rs__axum-2096`

**Files likely affected**: `axum/CHANGELOG.md`, `axum/src/routing/path_router.rs`, `axum/src/routing/mod.rs`
**FAIL_TO_PASS** (4 tests, first 3): `['routing::tests::fallback::issue_2072', 'routing::tests::fallback::issue_2072_outer_fallback_after_merge', 'routing::tests::fallback::merge_router_with_fallback_into_nested_router_with_fallback']`

**Problem statement (excerpt):**
> Nested 'fallback()' routes regression with 'merge()' <!--
 Thank you for reporting an issue.
 
 Please fill in as much of the template below as you're able.
 -->
 
 - [x] I have looked for existing issues (including closed) about this
 
 ## Bug Report
 
 ### Version
 
 The error is observed in all versions between '0.6.13' - '0.6.18'.
 
 '''
 ├── axum v0.6.13
 │   ├── axum-core v0.3.4
 '''
 
 ### 

### Sample 5 — `tokio-rs__axum-682`

**Files likely affected**: `axum/CHANGELOG.md`, `axum/src/routing/mod.rs`, `axum/src/response/redirect.rs`, `examples/oauth/Cargo.toml`, `examples/oauth/src/main.rs`
**FAIL_TO_PASS** (3 tests, first 3): `['routing::tests::wildcard_with_trailing_slash', 'routing::tests::with_trailing_slash_post', 'routing::tests::without_trailing_slash_post']`

**Problem statement (excerpt):**
> Use HTTP 308 instead of 301 for trailing slash redirects ## Feature Request
 
 ### Motivation
 
 Performing a POST to '/some/url/' (with the trailing slash) does an HTTP 301 (introduced in #410) to '/some/url'. However, HTTP 301 transforms a POST to a GET, which is undesired.
 
 ### Proposal
 
 Use [HTTP 308](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/308) instead, as suggested by @j

### Sample 6 — `tokio-rs__axum-691`

**Files likely affected**: `axum/CHANGELOG.md`, `axum/src/routing/mod.rs`
**FAIL_TO_PASS** (1 tests, first 3): `['routing::tests::nest::nesting_router_at_root']`

**Problem statement (excerpt):**
> Odd behavior when nesting root '/' path ## Bug Report
 
 <!--
 Thank you for reporting an issue.
 
 Please fill in as much of the template below as you're able.
 -->
 
 ### Version
 
 'v0.4.3'
 
 ### Platform
 
 'Linux 5.15.7-arch1-1 #1 SMP PREEMPT Wed, 08 Dec 2021 14:33:16 +0000 x86_64 GNU/Linux'
 
 ### Crates
 
 'axum', I believe
 
 ### Description
 
 While working on routes for an app, I wanted

### Sample 7 — `tokio-rs__axum-734`

**Files likely affected**: `axum/src/routing/route.rs`, `axum/CHANGELOG.md`, `axum/src/routing/future.rs`, `axum/src/routing/mod.rs`, `axum-extra/src/routing/resource.rs`
**FAIL_TO_PASS** (1 tests, first 3): `['routing::tests::head_content_length_through_hyper_server']`

**Problem statement (excerpt):**
> Incorrect content-length header in reply to HEAD request ## Bug Report
 
 ### Version
 
 axum v0.4.4
 axum-core v0.1.1
 
 ### Platform
 
 Debian Linux 12 ("bookworm")
 Linux feynman 5.15.0-3-amd64 <span>#</span>1 SMP Debian 5.15.15-1 (2022-01-18) x86_64 GNU/Linux
 rustc 1.58.1 (db9d1b20b 2022-01-20)
 
 ### Description
 
 The 'content-length' header in the reply to a simple 'HEAD' request is set to

## Section 6 — Builder guidance

When building a fix for an instance in tokio-rs/axum:

1. **Read the problem statement carefully** — the issue text describes the bug and often hints at root cause.
2. **Likely files**: see §2 above. axum/CHANGELOG.md appears in most fixes.
3. **Run the FAIL_TO_PASS tests** to see the failure first (`pytest <test_name> -v`).
4. **Inspect surrounding code** at the file paths from §2 — common bug locations.
5. **Match the theme** (§4) to known repo patterns: regression vs edge case vs API change.
6. **Generate minimal patch** — SWE-bench scoring rewards smallest viable fix.
7. **Verify PASS_TO_PASS still pass** — don't break existing functionality.

## Section 7 — Index of all instances in this repo

All 7 instance_ids live in `c:/tmp/swebench_instance_index.jsonl` (filterable by `repo == "tokio-rs/axum"`).

First 20 instance_ids:

- `tokio-rs__axum-1119` (dataset: `swe-bench-multilingual-test`)
- `tokio-rs__axum-1730` (dataset: `swe-bench-multilingual-test`)
- `tokio-rs__axum-1934` (dataset: `swe-bench-multilingual-test`)
- `tokio-rs__axum-2096` (dataset: `swe-bench-multilingual-test`)
- `tokio-rs__axum-682` (dataset: `swe-bench-multilingual-test`)
- `tokio-rs__axum-691` (dataset: `swe-bench-multilingual-test`)
- `tokio-rs__axum-734` (dataset: `swe-bench-multilingual-test`)

---

*Determinex · Lunarian Data Systems · auto-generated from SWE-bench-family datasets*
