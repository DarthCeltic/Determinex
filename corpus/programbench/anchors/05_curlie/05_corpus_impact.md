---
name: curlie-corpus-impact
description: What curlie adds to the Determinex Oracle. The corpus's first HTTP-protocol fixture and HTTPie-syntax parser. Delegating-to-external-binary CLI training pairs.
type: corpus-impact
---

# curlie — Corpus Impact

## What this teaches the Oracle

curlie's lock adds four distinct training-pair categories — the corpus's first material exposure to networking and external-binary delegation:

1. **HTTPie-syntax parser failure pairs**
   - Item-discriminator confusion (`==` vs `=` vs `:=` vs `:`)
   - JSON-value coercion at parse time (`:=null` → `null`, not `"null"`)
   - File-from-stream `@-` placeholder handling
   This DSL is small but its rules are **highly specific**; precision pairs are valuable.

2. **HTTP-CLI argument-translation failure pairs**
   - Method inference from body presence
   - URL normalization: scheme, port, IPv6
   - Body-mode inference: JSON default, form override, multipart-via-`@`-trigger
   Generalizable to any HTTP-shaped CLI tool.

3. **External-process-invocation failure pairs**
   - argv quoting and shell-safety in printed commands
   - exit-code passthrough discipline
   - stdin/stdout/stderr forwarding semantics
   Generalizable to **any wrapper-tool pattern** — and Determinex uses external binaries (curl, git, docker, ollama) constantly. This fixture pays off everywhere.

4. **`--offline` / dry-run failure pairs**
   - Print-but-don't-execute mode
   - Format-stable command-line output
   This pattern recurs (`fd --print-cmd`, etc.).

## What this makes faster beyond the immediate cluster

- **Every CLI-wrapper tool** Determinex ever writes. The Oracle gains a known-good template for "translate user-friendly args into a wire-format protocol or another binary's args."
- **Every HTTP-using script in the broader Determinex codebase**. The agent's own DeepSeek/Anthropic API calls follow this shape. The Oracle becomes more confident at scaffolding new HTTP integrations.
- **The `_lib/go/httpie_parse.go` artifact** is reusable for any future HTTPie-compatible tool (which is a recurring pattern in dev tooling).

## Compounding with already-locked tools

| Locked tool | Compounding effect |
|-------------|--------------------|
| zoxide      | None. |
| yj          | None. |
| ripsecrets  | None. |

## Compounding with currently-in-progress tools

| In-progress tool | Lift from curlie lock |
|------------------|------------------------|
| htmlq | None. |
| shellharden | None. |
| csview | None. |
| dutree | None. |

(curlie's compounding is purely forward.)

## Training data emitted

For a 741-test target with ~5 attempts: **~20-30 high-quality training rows**. Lower than other anchors but reflects curlie's smaller test surface AND faster expected lock.

## Strategic value

**curlie is the bench's fastest entry into the network/HTTP family.** Justification:
1. Smallest test count of any anchor (741 — half of the next-smallest).
2. Easy difficulty rating — only "easy" in the anchor set.
3. The xh sibling is a near-clone — single biggest cluster-sibling lift available.
4. The corpus gains its first HTTP/networking fixture, opening downstream tools (oha, muffet, miniserve, dog) for partial-transfer work.
5. The argument-translation pattern (HTTPie → curl) is itself a category of CLI tool worth understanding.

## When to schedule curlie

The strategy doc orders the anchors 1→5 by compounding return. **curlie is intentionally last** because its compounding is the lowest. But:
- If jq is dragging at >95% for >5 attempts, **insert curlie** as a quick win to refill momentum.
- If fzf or fd is blocking on a Rust/Go cold-build cycle, **curlie is the right interleave** — it iterates fast.

Treat curlie as the **strategic palate-cleanser** of the anchor set.

## Action when locked

1. Move artifact from `T:/determinex-programbench/<run>/rs__curlie.5dfcbb1/source/` into `corpus/programbench/locked/curlie/`.
2. Extract:
   - `corpus/programbench/_lib/go/httpie_parse.go`
   - `corpus/programbench/_lib/go/url_normalize.go`
   - `corpus/programbench/_lib/go/curl_invoke.go`
3. Append WAL training pairs to `data/programbench_corpus.jsonl`.
4. Update `corpus/programbench/README.md` status board.
5. **Build xh next** — the curlie-to-xh port is the cheapest cluster lock in the entire bench.
6. Commit with tag `programbench-anchor-5-locked`.
