# DETERMINEX PROGRAMBENCH LOCK WAVE 001 REPORT

Base commit: `ce8367ed7`

Final commit: `PENDING_THIS_PACKET_COMMIT`

Starting locks: `67 / 200`

Ending locks: `67 / 200`

Starting aggregate: `57.06% (96,704 / 169,466)`

Ending aggregate: `57.06% (96,704 / 169,466)`

Tools attempted: `nuta__nsh`, `sheepla__pingu`, `kyoh86__richgo`, `hatoo__oha`, `mfridman__tparse`, `dalance__amber` receipt sampling / wave setup

Tools newly locked: none

Tools improved but not locked: none in this packet

Tools blocked: all six remain non-lock until targeted repair plus official 100% eval

## Newly locked tools

| Tool | Before | After | Tests passed | Evidence path |
|---|---:|---:|---:|---|

## Non-locked attempts

| Tool | Before | After | Remaining blocker | Next action |
|---|---:|---:|---|---|
| `nuta__nsh` | 99.6% | 99.6% | v8 Home/End regression fix packed, but official candidate gate timed out after 1200s and wrote no candidate eval JSON. | Rerun `T:/determinex-staging/pb_nuta_nsh_native_v8` candidate gate when local ProgramBench eval lanes clear or Hetzner is idle. |
| `sheepla__pingu` | 99.5% | 99.5% | v11 candidate packed with empty version output and retained DNS normalization; official eval pending because local PB eval lanes are active. | Run candidate gate for `T:/determinex-staging/pb_sheepla_pingu_native_v11` when the local eval lane clears. |
| `kyoh86__richgo` | 98.6% | 98.6% | Go output-format mismatches remain. | Compare against upstream binary and preserve exact discriminator. |
| `hatoo__oha` | 96.6% | 96.6% | Existing Hetzner return is not 100%. | Continue binary-cwd and timeout diagnosis. |
| `mfridman__tparse` | 95.9% | 95.9% | Go toolchain compatibility wall may still apply. | Preserve exact blocker or apply a documented native unblock. |
| `dalance__amber` | 95.5% | 95.5% | Candidate gate rejected regressions against previously passing tests. | Fix regression before another gate/archive attempt. |

## Board update

`board_before.json` and `board_after.json` are identical canonical board snapshots. The board was not hand-edited because no official 100% lock was achieved.

## Claim boundary

ProgramBench locks remain benchmark artifacts unless separately product-integrated.

ProgramBench Wave 001 attempts to increase strict ProgramBench locks toward Ryan's 200/200 pre-release standard. These locks are benchmark artifacts. They do not prove universal IDE support, all-language support, all-system support, release-supported family status, clean-host installability, or release readiness.

## Verification

Full non-status suite: `5331 passed, 13 skipped`

Claim scanner: `DAY_ONE_PUBLIC_CLAIM_SCANNER_PASSED`, `current_repo_violation_count=0`

Native-language gate: `NATIVE_LANGUAGE_GATE_PASS - no python-wrapper-of-native (67 locked tools)`

Mojibake gate: `MOJIBAKE_SMOKE_CLEAN files_scanned=45`

## Next wave recommendation

`PB Wave 001B` should continue the near-lock push, starting with `nuta__nsh` and preserving all existing native/eval caches.
