---
name: swebench-fluent__fluentd
description: SWE-bench repo behavioral spec for fluent/fluentd. Aggregated from 12 bug-fix instances across 1 dataset(s). Inject into builder prompt for SWE-bench tasks targeting this repo.
type: swebench-repo-spec
---

# fluent/fluentd — SWE-bench Repo Spec

> **12 bug-fix instances** across 1 dataset(s); language(s): python.

## Section 1 — Dataset coverage

| Dataset | Instances |
|---------|-----------|
| swe-bench-multilingual-test | 12 |

## Section 2 — Where bugs typically live (top files touched in fixes)

| File | Times touched |
|------|---------------|
| `lib/fluent/plugin/in_tail.rb` | 2 |
| `lib/fluent/plugin/in_http.rb` | 2 |
| `lib/fluent/plugin/output.rb` | 1 |
| `lib/fluent/event_router.rb` | 1 |
| `lib/fluent/plugin_helper/retry_state.rb` | 1 |
| `lib/fluent/rpc.rb` | 1 |
| `lib/fluent/config/yaml_parser/loader.rb` | 1 |
| `lib/fluent/plugin/out_forward.rb` | 1 |
| `lib/fluent/plugin/out_forward/ack_handler.rb` | 1 |
| `lib/fluent/system_config.rb` | 1 |
| `lib/fluent/plugin_helper/http_server/server.rb` | 1 |

## Section 3 — Test framework signal

Detected: **unknown — sample names: test_ENOENT_error_after_setup_watcher, test_should_replace_target_info, Do not retry when retry_max_times is 0, test_application_ndjson, can pass records modified by filters to handle_emits_error**

Sample FAIL_TO_PASS test names (first 10):
```
  test_ENOENT_error_after_setup_watcher
  test_should_replace_target_info
  Do not retry when retry_max_times is 0
  test_application_ndjson
  can pass records modified by filters to handle_emits_error
  exponential backoff retries with secondary and max_steps
  test_invalid_rpc_endpoint[no_port]
  test_invalid_rpc_endpoint[invalid_addr]
  test_rpc_server[ipv4]
  test_rpc_server[ipv6]
```

## Section 4 — Problem-theme distribution

Top themes across 12 issue statements (auto-clustered):

| Theme | Count | % |
|-------|-------|---|
| documentation | 4 | 33.3% |
| crash_or_traceback | 2 | 16.7% |
| config_environment | 2 | 16.7% |
| wrong_output | 2 | 16.7% |
| performance | 1 | 8.3% |
| other | 1 | 8.3% |

## Section 5 — Sample issues (no patches — those are the answer)

### Sample 1 — `fluent__fluentd-3328`

**Files likely affected**: `lib/fluent/plugin/in_tail.rb`
**FAIL_TO_PASS** (1 tests, first 3): `['test_ENOENT_error_after_setup_watcher']`

**Problem statement (excerpt):**
> in_tail throws error and crashes process Check [CONTRIBUTING guideline](https://github.com/fluent/fluentd/blob/master/CONTRIBUTING.md) first and here is the list to help us investigate the problem.
 
 **Describe the bug**
 We are seeing an exception being thrown while Fluentd is starting up, which is causing Fluentd process to crash.  We suspect these are caused by short-lived, often run, K8s Cron

### Sample 2 — `fluent__fluentd-3466`

**Files likely affected**: `lib/fluent/plugin/in_tail.rb`
**FAIL_TO_PASS** (1 tests, first 3): `['test_should_replace_target_info']`

**Problem statement (excerpt):**
> Kubernetes container logs - duplicate logs found when using read_bytes_limit_per_second parameter ### Describe the bug  Continue on https://github.com/fluent/fluentd/issues/3434. I followed @ashie suggestion and did the stress test again on our EFK stack with [read_bytes_limit_per_second](https://docs.fluentd.org/input/tail#read_bytes_limit_per_second) parameter and Fluentd version 'v1.13.2'. Howe

### Sample 3 — `fluent__fluentd-3608`

**Files likely affected**: `lib/fluent/plugin/output.rb`
**FAIL_TO_PASS** (1 tests, first 3): `['Do not retry when retry_max_times is 0']`

**Problem statement (excerpt):**
> Plugin retries even when 'retry_max_times 0' **Describe the bug**
 Fluentd will retry chunks even when configured with 'retry_max_times 0'
 
 The buffer config below will cause retries, as per logs pasted below
 '''          
           retry_max_times 0
           retry_wait 3s
           retry_timeout 100s
           retry_max_interval 30s
           retry_forever false
 '''
 See below that cert

### Sample 4 — `fluent__fluentd-3616`

**Files likely affected**: `lib/fluent/plugin/in_http.rb`
**FAIL_TO_PASS** (1 tests, first 3): `['test_application_ndjson']`

**Problem statement (excerpt):**
> in_http: Support for Content-Type application/x-ndjson ### Is your feature request related to a problem? Please describe.
 
 Moving away from a legacy application in which logs were sent over HTTP as newline delimited JSON objects. With the added support for newline delimited JSON added to the in_http plugin Fluentd would be a drop-in replacement.
 
 I see that the out_http plugin supports applica

### Sample 5 — `fluent__fluentd-3631`

**Files likely affected**: `lib/fluent/event_router.rb`
**FAIL_TO_PASS** (1 tests, first 3): `['can pass records modified by filters to handle_emits_error']`

**Problem statement (excerpt):**
> Records passed  to @ERROR label do not contain modifications made in the pipeline/config ### Describe the bug  In a pipeline where the log records are mutated, when errors occur the log records passed to the @ERROR label do not contain modifications made further up in the pipeline before the error ocurred.  ### To Reproduce  **Steps**
 
 1) Run the config below, which adds a field
 2) Use fluent c

### Sample 6 — `fluent__fluentd-3640`

**Files likely affected**: `lib/fluent/plugin_helper/retry_state.rb`
**FAIL_TO_PASS** (1 tests, first 3): `['exponential backoff retries with secondary and max_steps']`

**Problem statement (excerpt):**
> Exponential backoff is not calculated right ### Describe the bug
 
 In documentation is written:
 
 _With exponential_backoff, retry_wait interval will be calculated as below:
 c: constant factor, @retry_wait
 b: base factor, @retry_exponential_backoff_base
 k: number of retry times
 total retry time: c + c * b^1 + (...) + c*b^k = c*b^(k+1) - 1_
 
 I was not sure, if alone c element counts as firs

### Sample 7 — `fluent__fluentd-3641`

**Files likely affected**: `lib/fluent/rpc.rb`
**FAIL_TO_PASS** (5 tests, first 3): `['test_invalid_rpc_endpoint[no_port]', 'test_invalid_rpc_endpoint[invalid_addr]', 'test_rpc_server[ipv4]']`

**Problem statement (excerpt):**
> IPV6 rpc_endpoint is not working for fluentd v1.13. ### Describe the bug  I am trying to add IPv6 environment rpc configuration to fluentd. However, it does not seem to be working and throwing continuous errors while starting up.
   ### To Reproduce  Please refer below configuration to reproduce the issue:
 configuration:
 <system>
      rpc_endpoint [::]:24444
      workers 4
 </system>  ### Expe

### Sample 8 — `fluent__fluentd-3917`

**Files likely affected**: `lib/fluent/config/yaml_parser/loader.rb`
**FAIL_TO_PASS** (1 tests, first 3): `['test_included_glob']`

**Problem statement (excerpt):**
> Glob pattern isn't resolved for !include directive in YAML format ### Describe the bug  No matter how I've tried I can't make paths with '*' in them work in !include directive.  ### To Reproduce  Here is simple Docker file that demonstrates the problem:
 '''
 FROM fluent/fluentd:v1.15-1
 
 SHELL ["/bin/ash", "-c"]
 
 RUN mkdir -p /fluentd/etc/more \
   && echo $'\
 - match:\n\
     $tag: "morematc

## Section 6 — Builder guidance

When building a fix for an instance in fluent/fluentd:

1. **Read the problem statement carefully** — the issue text describes the bug and often hints at root cause.
2. **Likely files**: see §2 above. lib/fluent/plugin/in_tail.rb appears in most fixes.
3. **Run the FAIL_TO_PASS tests** to see the failure first (`pytest <test_name> -v`).
4. **Inspect surrounding code** at the file paths from §2 — common bug locations.
5. **Match the theme** (§4) to known repo patterns: regression vs edge case vs API change.
6. **Generate minimal patch** — SWE-bench scoring rewards smallest viable fix.
7. **Verify PASS_TO_PASS still pass** — don't break existing functionality.

## Section 7 — Index of all instances in this repo

All 12 instance_ids live in `c:/tmp/swebench_instance_index.jsonl` (filterable by `repo == "fluent/fluentd"`).

First 20 instance_ids:

- `fluent__fluentd-3328` (dataset: `swe-bench-multilingual-test`)
- `fluent__fluentd-3466` (dataset: `swe-bench-multilingual-test`)
- `fluent__fluentd-3608` (dataset: `swe-bench-multilingual-test`)
- `fluent__fluentd-3616` (dataset: `swe-bench-multilingual-test`)
- `fluent__fluentd-3631` (dataset: `swe-bench-multilingual-test`)
- `fluent__fluentd-3640` (dataset: `swe-bench-multilingual-test`)
- `fluent__fluentd-3641` (dataset: `swe-bench-multilingual-test`)
- `fluent__fluentd-3917` (dataset: `swe-bench-multilingual-test`)
- `fluent__fluentd-4030` (dataset: `swe-bench-multilingual-test`)
- `fluent__fluentd-4311` (dataset: `swe-bench-multilingual-test`)
- `fluent__fluentd-4598` (dataset: `swe-bench-multilingual-test`)
- `fluent__fluentd-4655` (dataset: `swe-bench-multilingual-test`)

---

*Determinex · Lunarian Data Systems · auto-generated from SWE-bench-family datasets*
