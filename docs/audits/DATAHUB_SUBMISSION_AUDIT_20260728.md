# DataHub Hackathon Submission — Audit

**Date:** 2026-07-28
**Scope:** the DataHub Agent Hackathon (Challenge #2, Metadata-Aware Code Generation) entry —
`scripts/determinex_datahub.py`, `scripts/determinex_data_engineer.py`,
`tests/test_determinex_datahub.py`, `examples/datahub/*`, `docs/hackathon/DATAHUB_HACKATHON_2026.md`.
**Trigger:** a completion report claimed the integration was done, with "a 100% passing test suite
(4 passed in 0.52s)" and "Apache 2.0 license is already included."

Both of those statements were the problem. The suite was green *because* it only tested fixtures,
and there is no Apache license in this repository. What follows is what was actually wrong, what
was changed, and what is still not true.

---

## Verdict

The submission as handed over would have failed on contact with a live DataHub instance, and the
failure would have looked like success. Five defects, all in the same shape: **a broken path that
returns confident, plausible output.**

That shape is disqualifying here specifically, because the entry's entire thesis is *"AI agents
break pipelines because they guess schemas; this one doesn't."* An integration that invents schema
when the catalog is unreachable is not a weaker version of that claim — it is a counterexample to it.

---

## Defects found and fixed

### 1. Unreachable DataHub silently produced invented schema (critical)

`_execute_gql` caught `URLError`/`OSError` and returned built-in fixture data. `get_dataset_schema`
also fell back to fixtures on an empty response. So with no DataHub running, the tool printed
`[OK] Fetched 5 fields` for `analytics.orders` and generated SQL against a five-column table that
existed nowhere — byte-identical in appearance to a real run.

**Fixed:** the client raises `DataHubUnavailable`. Fixtures are reachable only via explicit
`mock_mode`. Transport failure never becomes data.

**Guard:** `test_unreachable_datahub_raises_and_never_fabricates_schema`. Proven failable — the old
fallback was reintroduced as a canary and this test went red; canary reverted.

### 2. The lineage GraphQL query was invalid and could never have worked

The query passed positional `urn:` / `direction:` arguments. DataHub's `searchAcrossLineage` takes a
single `input: SearchAcrossLineageInput!` (verified against docs.datahub.com). The query would have
been rejected by every real instance — and defect #1 hid that completely, because the rejection path
returned fixtures. A passing test asserted the fixture's contents.

**Fixed:** correct single-`input` query with `start`/`count`. **Guard:**
`test_lineage_query_sends_a_single_input_object` asserts the query text and variables, not the result.

### 3. `emit_lineage` was `return True` — a hard-coded constant behind a passing test

Body was `return True` with the comment `# Simulated lineage emission`, while the submission's video
script promised "show lineage emitted back to DataHub," and a test asserted `is True`.

**Fixed:** real `updateLineage(input: UpdateLineageInput!)` mutation with `edgesToAdd`. Returns
`False` in mock mode — there is nothing to write to, and reporting success for a write that did not
happen is the same lie in a smaller box. **Guards:**
`test_emit_lineage_actually_calls_updateLineage` (asserts the mutation was sent and the edge shape),
`test_emit_lineage_reports_false_in_mock_mode`.

### 4. The generator emitted a column it had never seen

`generate_dbt_model` unconditionally appended `where o.status != 'CANCELLED'`. `status` exists only
in the fixture. Against any real `analytics.orders` without it, the "schema-verified" output was
invalid SQL — the exact failure mode the entry claims to eliminate, produced by the entry itself.

**Fixed:** the predicate is emitted only when the catalog reports the column. Join keys are
validated on both sides and generation aborts with the actual column lists when absent.
**Guards:** `test_generator_omits_the_status_filter_when_the_column_does_not_exist`,
`..._includes_..._when_the_column_exists`, `test_generator_refuses_when_the_join_key_is_absent`.

### 5. Artifacts did not say where their schema came from

A fixture-derived `sample_dbt_model.sql` was indistinguishable from a catalog-derived one, so a
judge could not tell whether the demo proved anything.

**Fixed:** every `DatasetSchema`/`Lineage` carries `provenance` (`live` | `fixture`); generated dbt
and Airflow files are stamped, fixture output reading
`-- Schema source: OFFLINE FIXTURES -- not verified against a live catalog`. CLI prints
`[LIVE]`/`[FIXTURE]` per dataset and exits **2** with *"Refusing to generate code against an
unverified schema"* when the catalog is unreachable. **Guard:**
`test_generated_sql_states_which_source_it_came_from`.

---

## Test suite

| | Before | After |
|---|---|---|
| Tests | 4 | 12 |
| Constructed with `mock_mode=True` | 4 of 4 | 2 of 12 |
| Exercise the GraphQL transport | 0 | 6 (real threaded `HTTPServer` stub) |
| Would fail if the silent fallback returned | no | yes (verified by canary) |

The old suite asserted that fixtures contained their own contents (`len(fields) == 5`) and that a
hard-coded `True` was `True`. It was green and the integration was substantially broken. **A green
suite was weak evidence** — the same lesson this project has now learned in three separate
subsystems.

One incidental bug in the new tests: the stub handler's response dict was first named `responses`,
which shadows `BaseHTTPRequestHandler.responses` (used internally by `send_response`). Renamed
`scripted`.

---

## Claims corrected in the submission document

| Claim as written | Status | Now reads |
|---|---|---|
| "DataHub Context Platform / **MCP Server**" (overview, architecture diagram, tech list, video script — 4 places) | **False.** No MCP code exists anywhere in the repo. | GraphQL API only, with an explicit "there is no MCP server integration in this entry" scope note |
| Determinex **Observer** performs a "Schema Contract Audit" | **False.** The Observer model is not wired into this path at all. | verification is deterministic (column presence, join-key checks), not model-judged |
| "Apache 2.0 license is already included" | **False.** No Apache license exists in this repository. | AGPL-3.0-or-later, matching `LICENSE`, `pyproject.toml`, `frontend/package.json`, `Cargo.toml` |
| Video script closes on lineage emission | Was scripted against the `return True` stub. | now scripts the **refusal demo** — kill the container, show exit 2 — which is the claim worth proving |

---

## Still not true / open

1. **Never run against a real DataHub instance.** Every live-path test runs against a local stub
   whose responses I wrote. The query shapes were verified against DataHub's published GraphQL
   schema docs, not against a running deployment. Standing up the DataHub quickstart and re-running
   is the single highest-value remaining step, and it is the one thing that would convert "should
   work" into "works."
2. **`updateLineage` write is unverified end-to-end.** The mutation is correct per docs and the
   test asserts the exact document and variables sent, but no edge has ever landed in a real
   catalog.
3. **AGPL-3.0-or-later may not satisfy the hackathon's licensing requirement.** The repo is
   copyleft. If the rules require a permissive license, this entry is ineligible as-is, and that is
   an owner decision — not something to quietly relicense. (Separately: repo metadata says
   `or-later` while a project note recorded `AGPL-3.0-only` as final. The repo, including the
   LICENSE text's own "or any later version" grant, says `or-later` in all four places; the note is
   the stale one, but the discrepancy should be settled deliberately.)
4. **No video recorded**, and the refusal demo in the script has not been rehearsed against a real
   container stop.
5. **Deadline:** August 10, 2026, 5:00 PM EDT.

---

## Files changed

- `scripts/determinex_datahub.py` — rewritten: `DataHubUnavailable`, provenance on every result,
  corrected `searchAcrossLineage`, real `updateLineage`, no silent fallback
- `scripts/determinex_data_engineer.py` — rewritten: conditional predicates, join-key validation,
  provenance stamps, exit 2 on unavailability
- `tests/test_determinex_datahub.py` — rewritten: 4 → 12 tests, real HTTP stub
- `docs/hackathon/DATAHUB_HACKATHON_2026.md` — 7 claim corrections
- `examples/datahub/sample_dbt_model.sql`, `sample_airflow_dag.py` — regenerated with provenance
  stamps
