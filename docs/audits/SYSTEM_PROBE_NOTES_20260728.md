# System probe notes — 2026-07-28

Notes from a long probing session. Recorded because the *pattern* is more reusable than
any individual fix: nearly every defect found had the same shape, and the techniques
that found them are repeatable.

## The recurring failure mode

**A check that passes when the thing it checks is broken.** Every item below is an
instance. None was found by reading code; all were found by running something and
comparing the result against what it claimed.

| # | The check | What it actually did |
|---|---|---|
| 1 | `validate_project` for Python | `compileall` — syntax only. A module-level `NameError` produced "Compiler Oracle: PASS". |
| 2 | `validate_project` for anything else | `return (True, "")`. TypeScript/Java/C/C++ steps recorded as compiler-verified, checked by nothing. |
| 3 | Execution-layer audit lock | Pointed at a duplicate doc, so it stayed green while the doc humans read drifted. Three sources disagreed on the count of unclassified execution sites. |
| 4 | `dependency_scan` with no scanner | Overwrote 383 packages / 5 HIGH CVEs with zeros. `blocked: true` was honest; the evidence was gone. |
| 5 | `verify_lockfiles` | Checked the requirement *files*, never the environment. 42 HIGH CVEs whose fixes were all already declared and none installed — including pip-audit itself. |
| 6 | Cloak audit (`verify_cloak.py`) | Defines a leak as an identifier *from the forward map*. An identifier the extractor never captured cannot be reported. Auditor blind exactly where the extractor is blind. |
| 7 | Session cost accounting | Recorded the single original builder call. Router and amplifier calls uncounted — `AMPLIFY_K=6` meant six paid calls, one billed. Budget guard under-counting ~6×. |
| 8 | Immutability guard | Counted `__pycache__` regeneration as a corpus mutation: green in isolation, red in the full suite. |
| 9 | A/B tier histogram (mine) | Both local rungs are tier 1, so 2 real escalations displayed as "tier 1=3". |
| 10 | Corpus API docstring | Claimed learned_classes "grows ONLY from verified=True" — superseded by a salvage two days after it was written. 5 verified of 272. |

## What found them

Ranked by yield:

1. **Running the thing against a deliberately broken input.** Highest yield by far. The
   Python oracle, the agent CLIs, the Cloak leaks, and the cost hole all surfaced this
   way. A planted `zzq`-prefixed identifier or an `add()` that returns `a - b` is worth
   more than any amount of reading.
2. **Generalising a found bug to its siblings.** One JavaScript field leak became five
   across JS/TS/PHP/Ruby/C++ by asking "what else has this shape?". One duplicate audit
   doc became four. Two of four oracle branches, not one.
3. **Canarying every new guard before trusting it.** Several of my own guards were
   wrong on first write. A guard that has never been observed to fail is not yet a
   guard.
4. **The project's own `--guard` gates.** All 8 pass (`corpus_wiring_census`,
   `pb_tier_classify`, `pb_override_scan`, `pb_board_guard`, `pb_senses_guard`,
   `determinex_pb_provenance_guard`, `day_one_public_claim_scanner`,
   `overclaim_guard`). Useful as a *floor* — they are not where bugs currently hide.
5. **The corpus API's own `maturity` report.** Found the flywheel's 5-of-272 verified
   ratio, and then two calibration errors in the API itself.

## Measurement mistakes I made

Worth recording separately, because in three cases my *measurement* was the bug and I
briefly believed a wrong conclusion:

* Read `$?` through a pipe and saw `head`'s exit status, concluding `--strict` did not
  work when it did.
* `tail -18` after a grep matching "complete" cut the `[ROUTE]` line, concluding routing
  had not fired when it probably had. Still unverified either way — no stdout was
  captured, so I stopped claiming it.
* `tail -3` on a directory listing led me to state a checkout had "only a db and specs"
  when it had 40 session dirs.

Lesson: when a measurement contradicts an expectation, suspect the measurement first.

## Still unprobed

* **Latency has no instrumentation anywhere.** The ledger records tokens and dollars,
  never milliseconds, so every "responds in milliseconds locally" claim is unmeasured.
  Routing cost 27% and 31% more wall clock in the two A/B runs — that is a real cost
  with no home in the accounting.
* **Per-call token capture.** `route_decisions.jsonl` records samples, not tokens, so
  cost cannot be attributed per rung. This is why the A/B has an unexplained
  discrepancy (2 paid calls vs 3 predicted ~33% saving; 1.6% observed).
* **`_ORACLE_IMAGES` has three entries.** Rust, Go, Python. Every other language now
  fails closed, which is honest but not capable. A TypeScript image with `tsc`
  preinstalled would make the `tsc` claim real; it cannot use `npx` because the sandbox
  runs `--network=none`.
* **The hive path never writes to `providers.jsonl`.** Two cost ledgers exist and only
  the session manifest sees hive spend. Worth unifying, or at least documenting which
  is authoritative for what.
* **`C:\Dev\Citadel` still exists**, 9.7 GB. Two `.env` pointers aimed at it this
  session; one silently sent two days of sessions to the wrong tree with fallback
  models. The guard now catches that class, but the trap is still there.

## Numbers, for the record

* Full suite: **5,006 passed, 0 failed, 0 skipped**.
* Security gate: **6/6 PASS** (was 3 PASS / 2 BLOCKED at session start).
* CVEs: **42 HIGH → 0**.
* Cloak: 9 of 9 languages obfuscate their fixture; **5 plaintext leaks closed**.
* knip: 35 findings + 13 hints → **1 inherent hint**.
* Router A/B: mechanism proven, saving **1.6%** — and n=3 cannot support a rate.


---

# Continuation — 2026-07-29

Same theme as 2026-07-28, and it kept holding: **the checks that pass when the thing
is broken.** Four more, all in code that had tests and all green.

## The cost-accounting split brain

Three modules each owned a rule for "what does this call cost", and each was wrong in a
different direction. Nothing compared them, so nothing failed.

| module | unknown model | locality test | consequence |
|---|---|---|---|
| `budget_guard` (the cloud spend cap) | exact-key `.get()` → **$0.00** | none | **cap silently disabled** for any prefixed model |
| `hive/budget` (session pricing) | substring → blended rate | needed a slash | local models billed as paid |
| `determinex_providers` (the usage ledger / "gas gauge") | one-entry dict → flat **$1/$1** | own list, missing `local/` + `determinex/` | free calls billed; claude-sonnet under-reported ~10× |

Two findings inside that are worth stating separately, because they point opposite ways:

* **The cap could not engage.** `PRICING.get(model, (0.0, 0.0))` — exact key, defaulting
  to free. `PRICING`'s keys are bare (`deepseek-chat`); the strings litellm needs are
  prefixed (`openrouter/deepseek/deepseek-v4-flash`). Every prefixed cloud call cost $0,
  so `spend_usd` never moved. This is the dangerous direction: **real money, hidden.**
  It survived because the PB driver's defaults are bare names and priced fine. Setting
  `DETERMINEX_DEEPSEEK_MODEL` to the OpenRouter form — which is what CLAUDE.md's `.env`
  implies for DeepSeek — disables the cap without a word.

* **Local models were billed.** `hive/ctx_config.py` assigns the roles BARE Ollama tags
  by default (`determinex-engineer-v11-dsl`), and every locality test required a slash.
  $0.012 per builder step against a $2.00 default budget: a fully local session accrued
  fictional spend, showed it, and after ~167 steps logged *"API BUDGET EXHAUSTED —
  switching to local-only mode"* while it had never left local.

`hive/budget` already carried a comment explaining precisely why substring matching is
required — it fixed its own copy and the original stayed broken. That is the shape to
watch for: **a fix applied to a copy is a fix that will be un-applied by the next
caller.** `api_client._resolve_model` likewise carries a comment about bare tags having
no slash; it resolves via the alias map, and the three bare tags are not in it.

Fixed by making `budget_guard` the one canonical home and converging all three, with a
test that asserts they agree. Writing that test found the fourth divergence
(providers' list missing `local/`), which also meant `DETERMINEX_NETWORK_POLICY=offline`
had been **refusing genuinely-local models** as if they were about to leave the machine.

## The oracle that verified nothing

Asked why the new TypeScript branch needed a has-sources guard, then asked whether the
others did:

```
python      PASSED an empty workspace     <-- compileall over zero files exits 0
rust        refused
go          refused
typescript  refused
```

So a builder step whose patch was malformed, or that wrote outside the path the step
declared, was recorded **VERIFIED** in the WAL and was eligible for the training corpus
— in the language this project uses most. The import and `unittest` stages exit 0 on
nothing too, so all three stages agreed on a workspace with no code in it.

## TypeScript, and two bugs that passed their own tests

`tsc` had been listed in CLAUDE.md as part of the oracle for months while TypeScript
actually fell through the lenient pass. Building the image surfaced two defects that a
naive test would have called green:

* `tsc --project /determinex-tsconfig.json` type-checked **correctly** and reported every
  error as `../proc/1/cwd/bad.ts`. tsconfig `include` globs resolve against the *config's*
  directory, so a config at `/` walked the container root and reached the mounted sources
  sideways through `/proc`. Right errors, useless paths — and the retry loop's feedback
  injection has to open the file an error names.
* `lang="ts"` missed the `_ORACLE_IMAGES` lookup, fell through to the default image, and
  reported `tsc: not found` as a compile failure. **A missing oracle impersonating a
  broken program** is the one mistake an oracle must never make.

The pinned-language-set test earned its keep here: adding the image failed it *and* the
three tests that had been using `typescript` as their example of an unconfigured
language, which forced them to be repointed rather than left quietly wrong.

## Two things I checked and did NOT change

Worth recording, because "investigated and sound" is a result:

* **`_preprocess_spec_to_dsl` makes an unbilled litellm call.** It returns early unless
  the model resolves to `ollama/`, so it only ever calls a local model. Not billing it
  is correct.
* **`corpus_tree_index._is_local_navigator` accepts any bare name**, so `gpt-4o` reads as
  "local". That looked like a privacy hole in a Cloak-sensitive path — the navigator sees
  corpus prose on every query. It is not: the transport is
  `swe_agent.inference._ollama`, a hardcoded local `/api/generate` over urllib with no
  cloud path anywhere in the module. In that context a bare name genuinely *is* an Ollama
  tag, so the slash test is right and the docstring matches.

## Measurement mistakes, continued

The 2026-07-28 list said to suspect the measurement first. Three more:

* Read a background task's status as "exit code 0" when it was the **pipeline's** status;
  pytest had reported `2 failed`. Same `$?`-through-a-pipe error as yesterday, in a new
  costume.
* Claimed `golang:1.23-alpine` was absent from the local images and that Go's oracle had
  therefore never run here. It was present; Go verifies correctly. I had read a
  previously-truncated listing as complete.
* A heredoc ate `\n` escapes for the third time and the `.replace()` calls in that same
  script **silently no-op'd** — `str.replace` does not error on no match, so three test
  repoints reported success and changed nothing. Caught only by grepping for the result.
  Stop using heredocs for content containing backslashes; `Write` does not mangle them.

## Still open

* **`UNKNOWN_CLOUD_RATE` is a behaviour change.** An unknown cloud model now costs
  $8/1M instead of $0, so a long drive on a model with no `PRICING` row can hit a cap it
  previously ignored. That is the intended direction — under-reporting spends real money,
  over-reporting just falls back to local — but the fix is to add a `PRICING` row, not to
  restore the zero.
* **`determinex/` as a locality signal** rests on a naming convention. A `determinex/*`
  alias pointed at a cloud model would read as local. Not reachable in the providers
  lane (those aliases are hive-only and not valid litellm model strings), and the hive
  lane's cloud guard catches it, but it is convention rather than proof.
* **Per-call token capture** still missing from `route_decisions.jsonl`, so the router
  A/B still cannot attribute cost per rung.
* **`C:\Dev\Citadel`**, 9.7 GB, still there.
