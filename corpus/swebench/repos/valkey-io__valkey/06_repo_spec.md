---
name: swebench-valkey-io__valkey
description: SWE-bench repo behavioral spec for valkey-io/valkey. Aggregated from 4 bug-fix instances across 1 dataset(s). Inject into builder prompt for SWE-bench tasks targeting this repo.
type: swebench-repo-spec
---

# valkey-io/valkey — SWE-bench Repo Spec

> **4 bug-fix instances** across 1 dataset(s); language(s): python.

## Section 1 — Dataset coverage

| Dataset | Instances |
|---------|-----------|
| swe-bench-multilingual-test | 4 |

## Section 2 — Where bugs typically live (top files touched in fixes)

| File | Times touched |
|------|---------------|
| `src/db.c` | 1 |
| `src/acl.c` | 1 |
| `src/cluster_legacy.c` | 1 |
| `src/valkey-cli.c` | 1 |

## Section 3 — Test framework signal

Detected: **Java/JUnit (TestClass.testMethod)**

Sample FAIL_TO_PASS test names (first 10):
```
  TOUCH alters the last access time of a key in no-touch mode
  Test ACL LOAD works on replica
  CLUSTER SHARDS slot response is non-empty when primary node fails
  valkey-cli make source node ignores NOREPLICAS error when doing the last CLUSTER SETSLOT
```

## Section 4 — Problem-theme distribution

Top themes across 4 issue statements (auto-clustered):

| Theme | Count | % |
|-------|-------|---|
| other | 1 | 25.0% |
| crash_or_traceback | 1 | 25.0% |
| edge_case | 1 | 25.0% |
| config_environment | 1 | 25.0% |

## Section 5 — Sample issues (no patches — those are the answer)

### Sample 1 — `valkey-io__valkey-1499`

**Files likely affected**: `src/db.c`
**FAIL_TO_PASS** (1 tests, first 3): `['TOUCH alters the last access time of a key in no-touch mode']`

**Problem statement (excerpt):**
> [BUG] TOUCH has no effect in scripts when client is in no-touch mode **Describe the bug**
 
 When a client is in "no-touch" mode, the "TOUCH" command must update the last access time of a key (see https://valkey.io/commands/client-no-touch/).
 
 This does not work when the "TOUCH" command is called from a script.
 
 **To reproduce**
 
 The problem is present in all released versions (Valkey 7.2.7,

### Sample 2 — `valkey-io__valkey-1842`

**Files likely affected**: `src/acl.c`
**FAIL_TO_PASS** (1 tests, first 3): `['Test ACL LOAD works on replica']`

**Problem statement (excerpt):**
> [BUG] Valkey replica crashes on 'ACL LOAD' **Describe the bug**  In a primary-replica setup, running 'ACL LOAD' on the replica crashes Valkey. It works correctly on the primary.  **To reproduce**  1. Create a sample valkey.acl file e.g. with the line:  ''' user foo on #551a821992d8592d71c26a4989e26ce1d39e90ba3c20e3eaf99eed4a2e64251f +@all ~* resetchannels &* ''' 2. Run a valkey server from the '/s

### Sample 3 — `valkey-io__valkey-790`

**Files likely affected**: `src/cluster_legacy.c`
**FAIL_TO_PASS** (1 tests, first 3): `['CLUSTER SHARDS slot response is non-empty when primary node fails']`

**Problem statement (excerpt):**
> [BUG] CLUSTER SHARDS command returns "empty array" in slots section We are running a 6-node Valkey cluster (version 7.2.5) in a docker environment with 1 replica. When we stop one of the master nodes in the cluster, the CLUSTER SHARDS command returns empty slots for that specific shard. 
 
 Output with an empty array.
 
 
 '''
 1) 1) "slots"
    2) 1) (integer) 5461
       2) (integer) 10922
    3

### Sample 4 — `valkey-io__valkey-928`

**Files likely affected**: `src/valkey-cli.c`
**FAIL_TO_PASS** (1 tests, first 3): `['valkey-cli make source node ignores NOREPLICAS error when doing the last CLUSTER SETSLOT']`

**Problem statement (excerpt):**
> [BUG] cluster rebalance --cluster-weight <node>=0 fails with clusterManagerMoveSlot: NOREPLICAS error **Describe the bug**
 
 Testing with the 8.0.0-rc1 load, during a rebalance launched from valkey-cli to remove all the shards from a master, an error is seen if the master is configured with 'cluster-allow-replica-migration no'.
 
 If 'cluster-allow-replica-migration yes', then the command succeed

## Section 6 — Builder guidance

When building a fix for an instance in valkey-io/valkey:

1. **Read the problem statement carefully** — the issue text describes the bug and often hints at root cause.
2. **Likely files**: see §2 above. src/db.c appears in most fixes.
3. **Run the FAIL_TO_PASS tests** to see the failure first (`pytest <test_name> -v`).
4. **Inspect surrounding code** at the file paths from §2 — common bug locations.
5. **Match the theme** (§4) to known repo patterns: regression vs edge case vs API change.
6. **Generate minimal patch** — SWE-bench scoring rewards smallest viable fix.
7. **Verify PASS_TO_PASS still pass** — don't break existing functionality.

## Section 7 — Index of all instances in this repo

All 4 instance_ids live in `c:/tmp/swebench_instance_index.jsonl` (filterable by `repo == "valkey-io/valkey"`).

First 20 instance_ids:

- `valkey-io__valkey-1499` (dataset: `swe-bench-multilingual-test`)
- `valkey-io__valkey-1842` (dataset: `swe-bench-multilingual-test`)
- `valkey-io__valkey-790` (dataset: `swe-bench-multilingual-test`)
- `valkey-io__valkey-928` (dataset: `swe-bench-multilingual-test`)

---

*Determinex · Lunarian Data Systems · auto-generated from SWE-bench-family datasets*
