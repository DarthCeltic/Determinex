# Claude ProgramBench Handoff

This is the quick launch rail for the next five-hour ProgramBench sprint.

## Current Checkpoint

- jq anchor is at **87/100**, **5973/6872 passing**, latest official run:
  `work/programbench/jq_eval_run_small_clusters/jqlang__jq.b33a763/submission.tar.gz`
- Every official jq run in this sequence used clean image/archive preflight.
- Locked display-100 tools remain: zoxide, yj, ripsecrets, htmlq, ripgrep.
- In-progress high-value tools: jq, shellharden, csview, dutree.

## Read First

1. `docs/PROGRAMBENCH.md`
2. `corpus/programbench/README.md`
3. `corpus/programbench/_strategy/language_family_sprint_matrix.md`
4. `corpus/programbench/_strategy/per_language_scaffolds.md`
5. Relevant anchor pack under `corpus/programbench/anchors/`

## Operating Rules

- One tool at a time.
- One failure family per eval cycle.
- Preserve passing tests.
- Build a real root-level `./executable`; never symlink it.
- Run `scripts/programbench_image_preflight.py` before the first official eval and before trusting any score.
- Do not edit eval fixtures unless the upstream binary proves the fixture is wrong.
- Keep `compile.sh` language-specific and boring.

## Suggested Claude Work Queue

1. Continue jq from the latest 87/100 checkpoint:
   - runtime error normalization: slice indices, mktime bad elements, object-key array messages
   - regex/oniguruma parse gaps: octal escapes, `\Q...\E`, recursion/lookahead compile rejection
   - util time parsing: `%k`, `%G`, `%n`, `%T`, `%F`
   - path/update semantics: `pick/1`, `getpath(...) |=`, `.[] = 1`
   - module imports: JSON data imports and optional imports
   - exact stderr: invalid escape capitalization/locations, `$bar`/break label top-level text
2. If jq stalls, switch to mechanical grunt work:
   - create source skeletons for the next family using `language_family_sprint_matrix.md`
   - harvest probes with `scripts/determinex_programbench_probe.py`
   - add `README_DETERMINEX.md` to each work dir with score/fail-family notes
3. Hand refined patches back to Codex for integration and official scoring.

## Canonical Commands

Preflight:

```bash
python scripts/programbench_image_preflight.py <instance_id> --source-dir <source_dir> --submission-tar <submission.tar.gz>
```

Official eval wrapper:

```bash
python scripts/programbench_eval_runner.py <instance_id> C:\Dev\Determinex\work\programbench\<run_dir> --force
```

Direct ProgramBench eval:

```bash
cd T:/Dev/ProgramBench && PYTHONUTF8=1 uv run programbench eval "T:/determinex-programbench/<pilot_dir>" --filter "<author>" --force
```
