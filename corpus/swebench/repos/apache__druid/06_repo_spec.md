---
name: swebench-apache__druid
description: SWE-bench repo behavioral spec for apache/druid. Aggregated from 5 bug-fix instances across 1 dataset(s). Inject into builder prompt for SWE-bench tasks targeting this repo.
type: swebench-repo-spec
---

# apache/druid — SWE-bench Repo Spec

> **5 bug-fix instances** across 1 dataset(s); language(s): python.

## Section 1 — Dataset coverage

| Dataset | Instances |
|---------|-----------|
| swe-bench-multilingual-test | 5 |

## Section 2 — Where bugs typically live (top files touched in fixes)

| File | Times touched |
|------|---------------|
| `processing/src/main/java/org/apache/druid/query/aggregation/post/ArithmeticPostAggregator.java` | 1 |
| `docs/querying/post-aggregations.md` | 1 |
| `server/src/main/java/org/apache/druid/discovery/DruidLeaderClient.java` | 1 |
| `processing/src/main/java/org/apache/druid/java/util/common/JodaUtils.java` | 1 |
| `processing/src/main/java/org/apache/druid/query/spec/MultipleIntervalSegmentSpec.java` | 1 |
| `processing/src/main/java/org/apache/druid/timeline/VersionedIntervalTimeline.java` | 1 |
| `processing/src/main/java/org/apache/druid/query/groupby/GroupByQueryQueryToolChest.java` | 1 |
| `server/src/main/java/org/apache/druid/server/metrics/WorkerTaskCountStatsMonitor.java` | 1 |

## Section 3 — Test framework signal

Detected: **unknown — sample names: org.apache.druid.query.aggregation.post.ArithmeticPostAggregatorTest#testPow, org.apache.druid.discovery.DruidLeaderClientTest#test503ResponseFromServerAndCacheRefresh, org.apache.druid.timeline.VersionedIntervalTimelineTest#testOverlapSecondContainsFirstZeroLengthInterval, org.apache.druid.timeline.VersionedIntervalTimelineTest#testOverlapSecondContainsFirstZeroLengthInterval2, org.apache.druid.timeline.VersionedIntervalTimelineTest#testOverlapSecondContainsFirstZeroLengthInterval3**

Sample FAIL_TO_PASS test names (first 10):
```
  org.apache.druid.query.aggregation.post.ArithmeticPostAggregatorTest#testPow
  org.apache.druid.discovery.DruidLeaderClientTest#test503ResponseFromServerAndCacheRefresh
  org.apache.druid.timeline.VersionedIntervalTimelineTest#testOverlapSecondContainsFirstZeroLengthInterval
  org.apache.druid.timeline.VersionedIntervalTimelineTest#testOverlapSecondContainsFirstZeroLengthInterval2
  org.apache.druid.timeline.VersionedIntervalTimelineTest#testOverlapSecondContainsFirstZeroLengthInterval3
  org.apache.druid.query.groupby.GroupByQueryQueryToolChestTest#testCacheStrategy
  org.apache.druid.server.metrics.WorkerTaskCountStatsMonitorTest#testMonitorWithPeon
```

## Section 4 — Problem-theme distribution

Top themes across 5 issue statements (auto-clustered):

| Theme | Count | % |
|-------|-------|---|
| documentation | 1 | 20.0% |
| crash_or_traceback | 1 | 20.0% |
| edge_case | 1 | 20.0% |
| regression | 1 | 20.0% |
| config_environment | 1 | 20.0% |

## Section 5 — Sample issues (no patches — those are the answer)

### Sample 1 — `apache__druid-13704`

**Files likely affected**: `processing/src/main/java/org/apache/druid/query/aggregation/post/ArithmeticPostAggregator.java`, `docs/querying/post-aggregations.md`
**FAIL_TO_PASS** (1 tests, first 3): `['org.apache.druid.query.aggregation.post.ArithmeticPostAggregatorTest#testPow']`

**Problem statement (excerpt):**
> Support Post aggregation function pow(f1,f2) to cater for square, cube , square root. ### Description
 
 Please describe the feature or change with as much detail as possible. 
 
 As of now the only supported arithmetic functions are +, -, *, /, and quotient.
 https://druid.apache.org/docs/latest/querying/post-aggregations.html#arithmetic-post-aggregator.
 The request is to add an additional funct

### Sample 2 — `apache__druid-14092`

**Files likely affected**: `server/src/main/java/org/apache/druid/discovery/DruidLeaderClient.java`
**FAIL_TO_PASS** (1 tests, first 3): `['org.apache.druid.discovery.DruidLeaderClientTest#test503ResponseFromServerAndCacheRefresh']`

**Problem statement (excerpt):**
> DruidLeaderClient should refresh cache for non-200 responses Currently DruidLeaderClient invalidates the cache when it encounters an IOException or a ChannelException ([here](https://github.com/apache/druid/blob/master/server/src/main/java/org/apache/druid/discovery/DruidLeaderClient.java#L160)). In environments where proxies/sidecars are involved in communication between Druid components, there i

### Sample 3 — `apache__druid-14136`

**Files likely affected**: `processing/src/main/java/org/apache/druid/java/util/common/JodaUtils.java`, `processing/src/main/java/org/apache/druid/query/spec/MultipleIntervalSegmentSpec.java`, `processing/src/main/java/org/apache/druid/timeline/VersionedIntervalTimeline.java`
**FAIL_TO_PASS** (3 tests, first 3): `['org.apache.druid.timeline.VersionedIntervalTimelineTest#testOverlapSecondContainsFirstZeroLengthInterval', 'org.apache.druid.timeline.VersionedIntervalTimelineTest#testOverlapSecondContainsFirstZeroLengthInterval2', 'org.apache.druid.timeline.VersionedIntervalTimelineTest#testOverlapSecondContainsFirstZeroLengthInterval3']`

**Problem statement (excerpt):**
> Zero-length interval matches too much data On the example wikipedia dataset, this query matches all data after '2016-06-27T00:00:11.080Z', but should really match nothing. The problem is in 'VersionedIntervalTimeline.lookup' and stems from the fact that 'interval1.overlaps(interval2)' does *not* consider the intervals to be overlapping if 'interval1' is zero-length and has the same start instant a

### Sample 4 — `apache__druid-15402`

**Files likely affected**: `processing/src/main/java/org/apache/druid/query/groupby/GroupByQueryQueryToolChest.java`
**FAIL_TO_PASS** (1 tests, first 3): `['org.apache.druid.query.groupby.GroupByQueryQueryToolChestTest#testCacheStrategy']`

**Problem statement (excerpt):**
> Druid 28.0.0 breaks the whole-query cache for groupBy queries with multiple post-aggregate metrics. I have been using Druid 28.0.0 and found a new bug.
 The whole-query cache for groupBy queries with multiple post-aggregation metrics is broken.
 However, if there are no post-aggregation metrics or a single post-aggregation metric, this bug does not seem to occur.
 
 This bug is probably caused by 

### Sample 5 — `apache__druid-16875`

**Files likely affected**: `server/src/main/java/org/apache/druid/server/metrics/WorkerTaskCountStatsMonitor.java`
**FAIL_TO_PASS** (1 tests, first 3): `['org.apache.druid.server.metrics.WorkerTaskCountStatsMonitorTest#testMonitorWithPeon']`

**Problem statement (excerpt):**
> WorkerTaskCountStatsMonitor doesn't work in Druid 30.0.0 ### Affected Version
 
 30.0.0
 
 ### Description
 
 I'm using a Middlemanager+Peons and I used to have following monitors enabled in MM config:
 '''
 druid.monitoring.monitors=["org.apache.druid.java.util.metrics.JvmMonitor", "org.apache.druid.server.metrics.EventReceiverFirehoseMonitor", "org.apache.druid.server.metrics.WorkerTaskCountStat

## Section 6 — Builder guidance

When building a fix for an instance in apache/druid:

1. **Read the problem statement carefully** — the issue text describes the bug and often hints at root cause.
2. **Likely files**: see §2 above. processing/src/main/java/org/apache/druid/query/aggregation/post/ArithmeticPostAggregator.java appears in most fixes.
3. **Run the FAIL_TO_PASS tests** to see the failure first (`pytest <test_name> -v`).
4. **Inspect surrounding code** at the file paths from §2 — common bug locations.
5. **Match the theme** (§4) to known repo patterns: regression vs edge case vs API change.
6. **Generate minimal patch** — SWE-bench scoring rewards smallest viable fix.
7. **Verify PASS_TO_PASS still pass** — don't break existing functionality.

## Section 7 — Index of all instances in this repo

All 5 instance_ids live in `c:/tmp/swebench_instance_index.jsonl` (filterable by `repo == "apache/druid"`).

First 20 instance_ids:

- `apache__druid-13704` (dataset: `swe-bench-multilingual-test`)
- `apache__druid-14092` (dataset: `swe-bench-multilingual-test`)
- `apache__druid-14136` (dataset: `swe-bench-multilingual-test`)
- `apache__druid-15402` (dataset: `swe-bench-multilingual-test`)
- `apache__druid-16875` (dataset: `swe-bench-multilingual-test`)

---

*Determinex · Lunarian Data Systems · auto-generated from SWE-bench-family datasets*
