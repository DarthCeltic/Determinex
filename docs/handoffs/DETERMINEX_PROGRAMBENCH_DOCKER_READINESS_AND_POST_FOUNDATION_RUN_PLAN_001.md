# DETERMINEX_PROGRAMBENCH_DOCKER_READINESS_AND_POST_FOUNDATION_RUN_PLAN_001

- Status: `PROGRAMBENCH_DOCKER_READINESS_PASSED`.
- Docker available: `True`.
- Factory readiness: `True`.
- Strict locks: `56`; score=100 not archived: `0`.
- Aggregate runnable score: `84957 / 161099 = 52.74%`.
- Bounded candidate count: `25`.

## Candidate Set

- `doxygen__doxygen` score `99.6` gap `1` language `cpp` packet `False`.
- `facebookresearch__fasttext` score `99.14772727272727` gap `3` language `cpp` packet `False`.
- `kyoh86__richgo` score `98.60050890585242` gap `11` language `go` packet `False`.
- `jqlang__jq` score `91.65023011176858` gap `127` language `c` packet `False`.
- `altdesktop__i3-style` score `88.13333333333334` gap `89` language `rust` packet `False`.
- `mfridman__tparse` score `85.43165467625899` gap `81` language `go` packet `False`.
- `konradsz__igrep` score `81.65007112375534` gap `129` language `rust` packet `False`.
- `mookid__diffr` score `78.51662404092072` gap `168` language `rust` packet `False`.
- `johanneskaufmann__html-to-markdown` score `76.18069815195072` gap `232` language `go` packet `False`.
- `nuta__nsh` score `74.92690058479532` gap `343` language `rust` packet `False`.
- `tinycc__tinycc` score `71.88478396994364` gap `449` language `c` packet `False`.
- `oppiliappan__eva` score `70.92419522326064` gap `280` language `unknown` packet `False`.
- `dalance__amber` score `70.76923076923077` gap `228` language `unknown` packet `False`.
- `skeema__skeema` score `66.96832579185521` gap `511` language `go` packet `False`.
- `sitkevij__hex` score `66.02052451539339` gap `298` language `rust` packet `False`.
- `junegunn__fzf` score `61.22112211221122` gap `470` language `go` packet `False`.
- `sheepla__pingu` score `61.016949152542374` gap `161` language `go` packet `False`.
- `clog-tool__clog-cli` score `60.53984575835476` gap `307` language `rust` packet `False`.
- `antonmedv__walk` score `60.076530612244895` gap `313` language `go` packet `False`.
- `nachoparker__dutree` score `58.92291446673706` gap `389` language `rust` packet `False`.
- `foriequal0__git-trim` score `58.87323943661972` gap `292` language `rust` packet `False`.
- `bensadeh__tailspin` score `58.72611464968153` gap `324` language `rust` packet `False`.
- `eradman__entr` score `58.68852459016394` gap `252` language `c` packet `False`.
- `nikoladucak__caps-log` score `58.18847209515096` gap `457` language `cpp` packet `False`.
- `tarka__xcp` score `57.78834720570749` gap `355` language `rust` packet `False`.

## Safe Run Command

`cd T:/Dev/ProgramBench && PYTHONUTF8=1 uv run programbench eval "T:/determinex-programbench/<candidate_run_root>" --filter "<base_slug>" --force`

## Stop Conditions

- stop after the explicit candidate set completes or after 50 candidates, whichever comes first.
- stop immediately on DockerHub/network rate limit and record RATE_LIMIT_BLOCKED.
- stop on any stale board count mismatch before archiving.
- stop on any candidate that requires secrets, paid tools, unknown binaries, or unclear license/security risk.
- stop before claiming any new strict lock unless passed == runnable and locked archive is written.

No broad ProgramBench run, total-100 claim, support-from-tool-presence claim, or public-go claim is made.
