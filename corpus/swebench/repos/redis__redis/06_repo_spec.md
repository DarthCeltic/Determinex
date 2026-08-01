---
name: swebench-redis__redis
description: SWE-bench repo behavioral spec for redis/redis. Aggregated from 12 bug-fix instances across 1 dataset(s). Inject into builder prompt for SWE-bench tasks targeting this repo.
type: swebench-repo-spec
---

# redis/redis — SWE-bench Repo Spec

> **12 bug-fix instances** across 1 dataset(s); language(s): python.

## Section 1 — Dataset coverage

| Dataset | Instances |
|---------|-----------|
| swe-bench-multilingual-test | 12 |

## Section 2 — Where bugs typically live (top files touched in fixes)

| File | Times touched |
|------|---------------|
| `src/t_stream.c` | 2 |
| `src/acl.c` | 2 |
| `src/t_list.c` | 1 |
| `src/t_zset.c` | 1 |
| `redis.conf` | 1 |
| `src/functions.c` | 1 |
| `src/util.c` | 1 |
| `src/bitops.c` | 1 |
| `src/t_string.c` | 1 |
| `src/script_lua.c` | 1 |
| `src/server.h` | 1 |
| `src/server.c` | 1 |
| `src/module.c` | 1 |

## Section 3 — Test framework signal

Detected: **unknown — sample names: XTRIM with MINID option, big delta from master record, LPOP/RPOP with <count> against non existing key in RESP2, BZMPOP should not blocks on non key arguments - #10762, Validate subset of channels is prefixed with resetchannels flag, ACL SETUSER RESET reverting to default newly created user**

Sample FAIL_TO_PASS test names (first 10):
```
  XTRIM with MINID option, big delta from master record
  LPOP/RPOP with <count> against non existing key in RESP2
  BZMPOP should not blocks on non key arguments - #10762
  Validate subset of channels is prefixed with resetchannels flag
  ACL SETUSER RESET reverting to default newly created user
  MONITOR can log commands issued by functions
  GEOSEARCH with small distance
  BITPOS will illegal arguments
  BITPOS against non-integer value
  GETRANGE against string value
```

## Section 4 — Problem-theme distribution

Top themes across 12 issue statements (auto-clustered):

| Theme | Count | % |
|-------|-------|---|
| wrong_output | 5 | 41.7% |
| other | 2 | 16.7% |
| documentation | 2 | 16.7% |
| performance | 2 | 16.7% |
| config_environment | 1 | 8.3% |

## Section 5 — Sample issues (no patches — those are the answer)

### Sample 1 — `redis__redis-10068`

**Files likely affected**: `src/t_stream.c`
**FAIL_TO_PASS** (1 tests, first 3): `['XTRIM with MINID option, big delta from master record']`

**Problem statement (excerpt):**
> [BUG] XTRIM MINID may delete messages whose IDs are higher than threshold **Describe the bug**
 In a certain scenario, the XTRIM command will delete messages with IDs higher than the threshold provided by the MINID option. In fact, all messages in the stream get deleted in this specific scenario.
 
 **To reproduce**
 One must add a message to the stream providing an ID, say "10-1". Then other mess

### Sample 2 — `redis__redis-10095`

**Files likely affected**: `src/t_list.c`
**FAIL_TO_PASS** (1 tests, first 3): `['LPOP/RPOP with <count> against non existing key in RESP2']`

**Problem statement (excerpt):**
> [BUG] LPOP key [count] returns Null Bulk reply instead of Null array reply. **Describe the bug**
 
 LPOP with count argument returns Null bulk reply instead of array null reply. As per [documentation](https://redis.io/commands/lpop) 
 
     When called with the count argument:
 
     Array reply: list of popped elements, or nil when key does not exist.
 
 When running against Redis 6.2.6, we get
 

### Sample 3 — `redis__redis-10764`

**Files likely affected**: `src/t_zset.c`
**FAIL_TO_PASS** (1 tests, first 3): `['BZMPOP should not blocks on non key arguments - #10762']`

**Problem statement (excerpt):**
> [BUG] BZMPOP blocks on non key arguments In Redis 7.0 BZMPOP was introduced allowing to block for any of the provided sets to have at least one element.
 However this command introduced a change in command arguments for which the current generic blocking [code ](https://github.com/redis/redis/blob/unstable/src/t_zset.c#L4044) for zset commands is not considering.
 
 When issuing a bzmpop with time

### Sample 4 — `redis__redis-11279`

**Files likely affected**: `redis.conf`, `src/acl.c`
**FAIL_TO_PASS** (2 tests, first 3): `['Validate subset of channels is prefixed with resetchannels flag', 'ACL SETUSER RESET reverting to default newly created user']`

**Problem statement (excerpt):**
> [BUG] 'ACL SETUSER ... reset' doesn't revert to true defaults **Describe the bug**
 
 'ACL SETUSER' with the 'reset' argument doesn't return to the _exact_ defaults as those of a newly-created user.
 Specifically, the 'sanitize-payload' that is implicitly added by 'sanitize-dump' configuration directive (default: clients) is added.
 I'm not entirely clear about all the implications, but this irks 

### Sample 5 — `redis__redis-11510`

**Files likely affected**: `src/functions.c`
**FAIL_TO_PASS** (1 tests, first 3): `['MONITOR can log commands issued by functions']`

**Problem statement (excerpt):**
> [BUG] Monitor command doesn't show fcall I got the redis server from a snap package:
 '''
 redis_version:7.0.5
 redis_git_sha1:1571907e
 redis_git_dirty:0
 redis_build_id:360fc1435f116c6e
 redis_mode:standalone
 os:Linux 5.17.5-300.fc36.x86_64 x86_64
 '''
 
 So if i do this:
 '''
 127.0.0.1:6379> function load replace "#!lua name=TEST\nredis.register_function('TEST123', function(keys, args) return

### Sample 6 — `redis__redis-11631`

**Files likely affected**: `src/util.c`
**FAIL_TO_PASS** (1 tests, first 3): `['GEOSEARCH with small distance']`

**Problem statement (excerpt):**
> [BUG] Distance value is mangled in GEORADIUS after 7.0.6 upgrade **Describe the bug**
 
 This issue began immediately after the 7.0.6 release. Our docker container that runs unit tests as part of the CI/CD pipeline is set to use the latest version and we noticed test failure immediately after the release. We are using the python redis library (version 3.5.3) to call the redis functions.
 
 The iss

### Sample 7 — `redis__redis-11734`

**Files likely affected**: `src/bitops.c`
**FAIL_TO_PASS** (2 tests, first 3): `['BITPOS will illegal arguments', 'BITPOS against non-integer value']`

**Problem statement (excerpt):**
> [BUG] Bitcount doesn't return error for missing end parameter if key is missing **Describe the bug**
 
 BITCOUNT is documented as
 
 '''
 BITCOUNT key [start end [BYTE | BIT]]
 '''
 
 When 'start' is specified but 'end' is missing (a syntax error), the command returns 'ERR syntax error' when the key exists, but returns '0' if the key is missing.
 
 **To reproduce**
 
 '''
 $ redis-server --version

### Sample 8 — `redis__redis-12272`

**Files likely affected**: `src/t_string.c`
**FAIL_TO_PASS** (2 tests, first 3): `['GETRANGE against string value', 'GETRANGE against integer-encoded value']`

**Problem statement (excerpt):**
> [BUG] SUBSTR returns wrong result with start 0 and end less than start **Describe the bug**
 
 'SUBSTR' returns an empty string when end is less than start. However, if start is 0, the first character is returned.
 
 **To reproduce**
 
 '''
 > set test cat
 OK
 > substr test 1 -500
 ""
 > substr test 0 -500
 "c"
 '''
 
 **Expected behavior**
 
 If end < start, 'SUBSTR' should return an empty strin

## Section 6 — Builder guidance

When building a fix for an instance in redis/redis:

1. **Read the problem statement carefully** — the issue text describes the bug and often hints at root cause.
2. **Likely files**: see §2 above. src/t_stream.c appears in most fixes.
3. **Run the FAIL_TO_PASS tests** to see the failure first (`pytest <test_name> -v`).
4. **Inspect surrounding code** at the file paths from §2 — common bug locations.
5. **Match the theme** (§4) to known repo patterns: regression vs edge case vs API change.
6. **Generate minimal patch** — SWE-bench scoring rewards smallest viable fix.
7. **Verify PASS_TO_PASS still pass** — don't break existing functionality.

## Section 7 — Index of all instances in this repo

All 12 instance_ids live in `c:/tmp/swebench_instance_index.jsonl` (filterable by `repo == "redis/redis"`).

First 20 instance_ids:

- `redis__redis-10068` (dataset: `swe-bench-multilingual-test`)
- `redis__redis-10095` (dataset: `swe-bench-multilingual-test`)
- `redis__redis-10764` (dataset: `swe-bench-multilingual-test`)
- `redis__redis-11279` (dataset: `swe-bench-multilingual-test`)
- `redis__redis-11510` (dataset: `swe-bench-multilingual-test`)
- `redis__redis-11631` (dataset: `swe-bench-multilingual-test`)
- `redis__redis-11734` (dataset: `swe-bench-multilingual-test`)
- `redis__redis-12272` (dataset: `swe-bench-multilingual-test`)
- `redis__redis-12472` (dataset: `swe-bench-multilingual-test`)
- `redis__redis-13115` (dataset: `swe-bench-multilingual-test`)
- `redis__redis-13338` (dataset: `swe-bench-multilingual-test`)
- `redis__redis-9733` (dataset: `swe-bench-multilingual-test`)

---

*Determinex · Lunarian Data Systems · auto-generated from SWE-bench-family datasets*
