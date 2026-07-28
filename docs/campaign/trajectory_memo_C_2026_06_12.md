# Trajectory Memo C — 2026-06-12 (post-conversion shard)

> Generated after Addendum C dispatch. Count: **52/200 = 26.0%**.
> Protocol: realistic and optimistic ranges with named assumptions. No hero numbers.

---

## Conversion Shard Results

The F1 skip-conversion shard (dsq taxi.csv) returned a confirmed **strict lock** at 1532/1532.

Key finding: The apt-get-without-update antipattern silently breaks package installs inside
Docker task images. Root cause documented; future compile.sh changes that install packages
must run `apt-get update` (now done via Python subprocess).

---

## N-Series Current Scores

| Tool | Pass | Total | Fail | Skip | Assessment |
|------|------|-------|------|------|-----------|
| **N1 figlet** | 2084 | 2088 | 4 | 0 | 2 unique fails (bidir'd). HIGH confidence lock. |
| **N5 bartib** | 1856 | 1858 | 0 | 2 | 1 unique skip: `help --help` behavioral. HIGH confidence. |
| **N2 handlr** | 1800 | 1812 | 12 | 0 | 6 unique fails. Medium — depends on failure class. |
| **N3 crowbook** | 1760 | 1774 | 14 | 0 | 7 unique fails. Medium — structural check pending. |
| **N4 xh** | 2302 | 2532 | 228 | 2 | Large delta (completion class). Low near-term probability. |

---

## Named Assumptions

**A1 — figlet 2 unique failures are behavioral (Codex-fixable)**
Confidence: HIGH (very small delta, bidir'd to 4)

**A2 — bartib `help --help` is a small Rust flag addition**
Confidence: HIGH (skip reason is explicit; standard clap pattern)

**A3 — handlr 6 unique failures include fixable behavioral cases**
Confidence: MEDIUM (no failure class diagnosis yet; could be structural)

**A4 — crowbook 7 unique failures are not all structural**
Confidence: MEDIUM-LOW (crowbook is a book compiler, environment dependencies likely)

**A5 — no cap-removal batch in this wave**
Confidence: ASSUMED (60 partial_eval_100 tools exist but not in this dispatch)

---

## Ranges

### Realistic branch (Addendum C wave, A1+A2 hold, A3 50%, A4 miss)
- 52 base
- +1 figlet (A1)
- +1 bartib (A2)
- +0.5 handlr expectation
- +0 crowbook (structural assumed)
- +0 xh (large delta, not near-term)

**Realistic: 54–55 by end of Addendum C wave**

### Optimistic branch (A1+A2+A3+A4 all hold, some near-locks resolve)
- 52 base
- +1 figlet, +1 bartib, +1 handlr, +1 crowbook
- +1 from near-lock pipeline (gping ceiling resolution, pingu 416/419 near-miss, sd near-lock)

**Optimistic: 57–58 by end of Addendum C wave**

### Extended optimistic (if cap-removal batch fires within 2 sessions)
- Partial_eval_100 → full eval on 60 tools
- Expected yield: ~15–25% convert to genuine locks (cap was a performance choice, many should pass)
- Adds 9–15 locks

**Extended optimistic: 66–73 by end of cap-removal batch**

---

## Critical Path

1. **figlet (N1)**: Codex executes — fastest possible new lock. Unblocked.
2. **bartib (N5)**: Small Rust change. Codex executes. High value.
3. **handlr (N2)**: Diagnosis first. May be structural or behavioral.
4. **Cap-removal batch**: 60 tools, mechanical (remove `del items[400:]`). Not yet dispatched.
   This is the highest-volume vein — triggers the extended optimistic branch.

---

## Conversion Shard Lesson (pattern update)

**APT-GET-WITHOUT-UPDATE antipattern**: Any `apt-get install` in compile.sh run inside a
Docker task image requires `apt-get update` first. Task images have stale package lists.
The install fails silently if `|| true` is appended. Future compile.sh additions that
install packages MUST use the Python subprocess pattern (which runs update internally)
or explicitly add `apt-get update -qq 2>/dev/null || true` before any install.

*Driver: Claude Sonnet 4.6 | 2026-06-12*
