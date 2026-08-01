---
name: curlie-transfer-map
description: Per-cluster-tool, what specifically transfers from curlie. The HTTPie-syntax parser is the most direct transfer (xh is a near-clone). The HTTP CLI scaffold is the universal piece.
type: transfer-map
---

# curlie → Cluster Transfer Map

| Tool | Bench # | Transfer | Specific knowledge that transfers | Additional work |
|------|---------|----------|------------------------------------|-----------------|
| **xh** | #55 | **Direct** | xh is a Rust-rewritten HTTPie — **near-identical surface to curlie**. Reuse the entire `parse.go` discriminator (port to Rust). URL normalization, method inference, body modes, auth — all transfer. xh's only material difference from curlie: it does the HTTP itself (using `reqwest` crate) instead of shelling out to curl. | Replace `os/exec curl` with `reqwest::Client`. ~300 LOC. The 50.0% ceiling suggests the test surface already overlaps heavily with curlie's. **xh is the cluster's biggest direct lift from curlie's lock.** |
| **oha** | #43 | Partial | HTTP request building (URL, headers, method, body) transfers from curlie's `Spec` model. oha is a load tester — wraps a single request in a benchmark loop. | Concurrency model (goroutines firing N parallel requests). Stats aggregation: latency distribution, RPS, error rate. Real-time TUI for progress. **TUI overlaps with fzf cluster.** ~600 LOC over curlie's request model. |
| **muffet** | #94 | Partial | HTTP client semantics (URL parsing, follow-redirects, timeout) transfer. muffet is a link checker: fetch HTML, extract links, recurse. | HTML parser (Go stdlib has `golang.org/x/net/html`). URL deduplication. Concurrency control. Output formats. ~400 LOC over curlie's HTTP scaffold. |
| **miniserve** | #56 | Partial | HTTP **protocol semantics** (request parsing, response building, status codes). miniserve is a SERVER — opposite end of the wire. The protocol-level mental model from curlie helps but the implementation is mirror-image. | HTTP server implementation (`net/http` is stdlib). Directory listing UI. Auth (basic auth check). File upload handling. ~700 LOC. **Genuinely partial** — server-side mostly novel. |
| **dog** | #61 | Partial | DNS-over-HTTPS / DoT — the HTTPS transport layer transfers from curlie's HTTP knowledge. The DNS protocol itself is novel. | DNS message encoding/decoding (RFC 1035). DoT (port 853) and DoH transport. Output formats (table, JSON). ~900 LOC. Largest test count in cluster (1,300) — non-trivial cost. |
| **gping** | #35 | Minimal | Almost nothing transfers. gping is ICMP ping with a graphical TUI — different protocol layer (raw sockets), TUI overlaps fzf cluster. | ICMP packet construction (requires root or capabilities). TUI rendering (fzf cluster). RTT statistics. ~500 LOC. |
| **pingu** | #101 | Minimal | Same as gping. pingu is similar but smaller surface (ceiling 96.6% suggests it's nearly trivial). | Similar shape; ~300 LOC. |

## Compounding with already-locked / in-progress

- **zoxide / yj / ripsecrets / htmlq / shellharden / csview / dutree** — none in this cluster's domain. curlie's transfer is forward-only.

## The HTTPie family within the cluster

curlie and xh are **the same tool** in different languages. Locking curlie creates a parser/discriminator fixture that, ported to Rust, lifts xh from 50.0% to 90%+ in a single port — **xh is the highest-leverage cluster sibling of any anchor**.

Strategy after curlie locks:
1. Extract `_lib/go/httpie_parse.go` and `_lib/rs/httpie_parse.rs` (twin ports).
2. Build xh as a thin `reqwest`-based shell around the Rust port.
3. Expected xh time-to-100%: 1-2 hours.

## Reusable fixtures to extract after curlie locks

- `_lib/go/httpie_parse.go` — argument discriminator + Spec builder
- `_lib/go/url_normalize.go` — URL-with-defaults normalizer
- `_lib/go/curl_invoke.go` — Spec → curl-args + exec
- `_lib/rs/httpie_parse.rs` — Rust port of the discriminator (xh prep)

## Anti-transfer notes

1. **The curl-shelling pattern doesn't help for xh, oha, muffet** — they all need a real HTTP client. The Spec model transfers; the execution does not.
2. **TUI tools in this cluster (oha, gping, pingu)** need fzf's TTY layer, not curlie's argument parser.
3. **Server tools (miniserve)** are mostly novel.
4. **DNS tools (dog)** share only the URL/transport semantics.

## Honest cluster lift expectation

- curlie: anchor at 100%
- xh: 95%+ (fastest sibling lift in any cluster — bullet)
- muffet: 80% reachable with HTTP scaffold + HTML parsing (~3-4 attempts)
- oha: 70% reachable; load-testing engine and TUI are real new work
- miniserve: 65% reachable; server is mostly new
- dog: 60% reachable; DNS protocol is mostly new
- gping/pingu: low transfer; build separately under fzf cluster

**Realistic locks from this anchor**: curlie + xh + muffet = **3 tools at 100%**. Stretch: oha, miniserve at 100% adds 2 more.

## Why curlie still earns the anchor slot despite low transfer

The cluster's TOTAL test count (~4,689) is high. Even at 3-of-7 lock rate, that's ~2,800-3,000 resolved tests for the smallest test-count investment of any anchor. Strategically: **curlie is the cheapest anchor by far**, and xh-from-curlie is the single biggest sibling lift in the entire bench.
