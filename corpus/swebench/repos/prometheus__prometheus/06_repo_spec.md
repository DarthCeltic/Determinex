---
name: swebench-prometheus__prometheus
description: SWE-bench repo behavioral spec for prometheus/prometheus. Aggregated from 8 bug-fix instances across 1 dataset(s). Inject into builder prompt for SWE-bench tasks targeting this repo.
type: swebench-repo-spec
---

# prometheus/prometheus — SWE-bench Repo Spec

> **8 bug-fix instances** across 1 dataset(s); language(s): python.

## Section 1 — Dataset coverage

| Dataset | Instances |
|---------|-----------|
| swe-bench-multilingual-test | 8 |

## Section 2 — Where bugs typically live (top files touched in fixes)

| File | Times touched |
|------|---------------|
| `web/ui/module/codemirror-promql/src/complete/promql.terms.ts` | 2 |
| `web/ui/module/codemirror-promql/src/promql.ts` | 2 |
| `tsdb/head_append.go` | 2 |
| `promql/engine.go` | 2 |
| `discovery/puppetdb/resources.go` | 1 |
| `discovery/puppetdb/fixtures/vhosts.json` | 1 |
| `promql/functions.go` | 1 |
| `web/ui/module/lezer-promql/src/promql.grammar` | 1 |
| `docs/querying/functions.md` | 1 |
| `web/ui/module/codemirror-promql/src/types/function.ts` | 1 |
| `promql/parser/functions.go` | 1 |
| `tsdb/head.go` | 1 |
| `model/labels/labels.go` | 1 |
| `promql/parser/lex.go` | 1 |
| `web/ui/module/codemirror-promql/src/grammar/tokens.js` | 1 |
| `web/ui/module/codemirror-promql/src/grammar/promql.grammar` | 1 |
| `docs/querying/operators.md` | 1 |
| `promql/parser/generated_parser.y` | 1 |
| `promql/parser/generated_parser.y.go` | 1 |

## Section 3 — Test framework signal

Detected: **unknown — sample names: TestPuppetDBRefreshWithParameters, TestEvaluations, TestEvaluations/testdata/functions.test, TestSnapshotAheadOfWALError, TestHeadDetectsDuplicateSampleAtSizeLimit**

Sample FAIL_TO_PASS test names (first 10):
```
  TestPuppetDBRefreshWithParameters
  TestEvaluations
  TestEvaluations/testdata/functions.test
  TestSnapshotAheadOfWALError
  TestHeadDetectsDuplicateSampleAtSizeLimit
  TestRangeQuery
  TestRangeQuery/drop-metric-name
  TestLabels_DropMetricName
  TestEngine_Close
  TestEngine_Close/nil_engine
```

## Section 4 — Problem-theme distribution

Top themes across 8 issue statements (auto-clustered):

| Theme | Count | % |
|-------|-------|---|
| other | 3 | 37.5% |
| import_module | 1 | 12.5% |
| documentation | 1 | 12.5% |
| wrong_output | 1 | 12.5% |
| crash_or_traceback | 1 | 12.5% |
| concurrency | 1 | 12.5% |

## Section 5 — Sample issues (no patches — those are the answer)

### Sample 1 — `prometheus__prometheus-10633`

**Files likely affected**: `discovery/puppetdb/resources.go`, `discovery/puppetdb/fixtures/vhosts.json`
**FAIL_TO_PASS** (1 tests, first 3): `['TestPuppetDBRefreshWithParameters']`

**Problem statement (excerpt):**
> PuppetDB Service Discovery - Numerical parameters not converted to __meta_puppetdb_parameter labels ### What did you do?
 
 Hi,
 
 We use puppetdb_sd to populate targets for scraping, with parameters enabled to be used with relabeling. 
 
 We've noticed some of the parameters were missing, based on their type.
 
 It doesn't look like there is a case for 'int' or 'float' values in discovery/puppetd

### Sample 2 — `prometheus__prometheus-10720`

**Files likely affected**: `promql/functions.go`, `web/ui/module/codemirror-promql/src/complete/promql.terms.ts`, `web/ui/module/codemirror-promql/src/promql.ts`, `web/ui/module/lezer-promql/src/promql.grammar`, `docs/querying/functions.md`
**FAIL_TO_PASS** (2 tests, first 3): `['TestEvaluations', 'TestEvaluations/testdata/functions.test']`

**Problem statement (excerpt):**
> PromQL function day_of_year <!--
 
     Please do *NOT* ask support questions in Github issues.
 
     If your issue is not a feature request or bug report use our
     community support.
 
     https://prometheus.io/community/
 
     There is also commercial support available.
 
     https://prometheus.io/support-training/
 
 -->
 ## Proposal
 **Use case. Why is this important?**
 
 We have day o

### Sample 3 — `prometheus__prometheus-11859`

**Files likely affected**: `tsdb/head.go`
**FAIL_TO_PASS** (1 tests, first 3): `['TestSnapshotAheadOfWALError']`

**Problem statement (excerpt):**
> Prometheus loading old memory snapshots instead of newer one during startup ### What did you do?  - Enabled 'memory-snapshot-on-shutdown' a few months ago
 - Multiple restart of Prometheus since the feature was enabled
 - Noticed recently that restarting prometheus cause us to lose the last ~2h of data
 - After investigation, I found that Prometheus keeps reloading an old snapshot from Aug 19 ('ch

### Sample 4 — `prometheus__prometheus-12874`

**Files likely affected**: `tsdb/head_append.go`
**FAIL_TO_PASS** (1 tests, first 3): `['TestHeadDetectsDuplicateSampleAtSizeLimit']`

**Problem statement (excerpt):**
> Duplicate sample not discarded when chunk is created due to reaching chunk size limit ### What did you do?  Ingesting about 1.7M series.
   ### What did you expect to see?  The resulting chunks in the written block after compaction are not overlapping.
   ### What did you see instead? Under which circumstances?  We are using Mimir [compactor](https://grafana.com/docs/mimir/v2.9.x/references/archit

### Sample 5 — `prometheus__prometheus-13845`

**Files likely affected**: `model/labels/labels.go`
**FAIL_TO_PASS** (3 tests, first 3): `['TestRangeQuery', 'TestRangeQuery/drop-metric-name', 'TestLabels_DropMetricName']`

**Problem statement (excerpt):**
> Queries return same series twice with non-stringlabels build ### What did you do?
 
 In some cases range queries return multiple separate series with identical label sets where only one series is expected.
 
 The conditions seem to be:
 * metric needs to have at least one label lexicographically smaller than '__name__', for example '__address__'
 * metric needs to have at least one label lexicogra

### Sample 6 — `prometheus__prometheus-14861`

**Files likely affected**: `promql/engine.go`
**FAIL_TO_PASS** (2 tests, first 3): `['TestEngine_Close', 'TestEngine_Close/nil_engine']`

**Problem statement (excerpt):**
> Agent mode PromQL engine shutdown ends in crash due to nil pointer dereference ### What did you do?
 
 Ran Prometheus (built from 'main') in agent mode and then shut it down.
 
 ### What did you expect to see?
 
 An orderly shutdown.
 
 ### What did you see instead? Under which circumstances?
 
 A crash:
 
 '''
 ts=2024-09-07T19:41:50.112Z caller=main.go:1041 level=warn msg="Received an OS signal,

### Sample 7 — `prometheus__prometheus-15142`

**Files likely affected**: `tsdb/head_append.go`
**FAIL_TO_PASS** (3 tests, first 3): `['TestHeadAppendHistogramAndCommitConcurrency', 'TestHeadAppendHistogramAndCommitConcurrency/float_histogram', 'TestHeadAppendHistogramAndCommitConcurrency/integer_histogram']`

**Problem statement (excerpt):**
> race in tsdb.headAppender.AppendHistogram ### What did you do?
 
 Run Mimir with race detection enabled.
 
 ### What did you expect to see?
 
 No race condition.
 
 ### What did you see instead? Under which circumstances?
 
 WARNING: DATA RACE
 Write at 0x00c08329f350 by goroutine 148443:
   github.com/prometheus/prometheus/tsdb.(*headAppender).AppendHistogram()
      .../vendor/github.com/prometh

### Sample 8 — `prometheus__prometheus-9248`

**Files likely affected**: `promql/parser/lex.go`, `web/ui/module/codemirror-promql/src/grammar/tokens.js`, `web/ui/module/codemirror-promql/src/grammar/promql.grammar`, `web/ui/module/codemirror-promql/src/complete/promql.terms.ts`, `docs/querying/operators.md`
**FAIL_TO_PASS** (2 tests, first 3): `['TestEvaluations', 'TestEvaluations/testdata/operators.test']`

**Problem statement (excerpt):**
> 'atan2' is currently not allowed between scalar values In PromQL testing I noticed that 'atan2' is currently not allowed between scalar values like '1 atan2 2' ('operator "atan2" not allowed for Scalar operations'). Is there a good reason for this? I would just treat it like any of the other arithmetic operators, which also work between scalars.
 
 _Originally posted by @juliusv in https://github.

## Section 6 — Builder guidance

When building a fix for an instance in prometheus/prometheus:

1. **Read the problem statement carefully** — the issue text describes the bug and often hints at root cause.
2. **Likely files**: see §2 above. web/ui/module/codemirror-promql/src/complete/promql.terms.ts appears in most fixes.
3. **Run the FAIL_TO_PASS tests** to see the failure first (`pytest <test_name> -v`).
4. **Inspect surrounding code** at the file paths from §2 — common bug locations.
5. **Match the theme** (§4) to known repo patterns: regression vs edge case vs API change.
6. **Generate minimal patch** — SWE-bench scoring rewards smallest viable fix.
7. **Verify PASS_TO_PASS still pass** — don't break existing functionality.

## Section 7 — Index of all instances in this repo

All 8 instance_ids live in `c:/tmp/swebench_instance_index.jsonl` (filterable by `repo == "prometheus/prometheus"`).

First 20 instance_ids:

- `prometheus__prometheus-10633` (dataset: `swe-bench-multilingual-test`)
- `prometheus__prometheus-10720` (dataset: `swe-bench-multilingual-test`)
- `prometheus__prometheus-11859` (dataset: `swe-bench-multilingual-test`)
- `prometheus__prometheus-12874` (dataset: `swe-bench-multilingual-test`)
- `prometheus__prometheus-13845` (dataset: `swe-bench-multilingual-test`)
- `prometheus__prometheus-14861` (dataset: `swe-bench-multilingual-test`)
- `prometheus__prometheus-15142` (dataset: `swe-bench-multilingual-test`)
- `prometheus__prometheus-9248` (dataset: `swe-bench-multilingual-test`)

---

*Determinex · Lunarian Data Systems · auto-generated from SWE-bench-family datasets*
