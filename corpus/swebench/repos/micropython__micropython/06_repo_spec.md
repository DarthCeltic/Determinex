---
name: swebench-micropython__micropython
description: SWE-bench repo behavioral spec for micropython/micropython. Aggregated from 5 bug-fix instances across 1 dataset(s). Inject into builder prompt for SWE-bench tasks targeting this repo.
type: swebench-repo-spec
---

# micropython/micropython — SWE-bench Repo Spec

> **5 bug-fix instances** across 1 dataset(s); language(s): python.

## Section 1 — Dataset coverage

| Dataset | Instances |
|---------|-----------|
| swe-bench-multilingual-test | 5 |

## Section 2 — Where bugs typically live (top files touched in fixes)

| File | Times touched |
|------|---------------|
| `py/bc.c` | 1 |
| `py/modthread.c` | 1 |
| `ports/stm32/mpthreadport.c` | 1 |
| `py/mpthread.h` | 1 |
| `ports/esp32/mpthreadport.c` | 1 |
| `ports/unix/mpthreadport.c` | 1 |
| `ports/cc3200/mpthreadport.c` | 1 |
| `ports/rp2/mpthreadport.c` | 1 |
| `ports/renesas-ra/mpthreadport.c` | 1 |
| `py/objslice.c` | 1 |
| `py/compile.c` | 1 |
| `py/mpz.c` | 1 |

## Section 3 — Test framework signal

Detected: **unknown — sample names: basics/fun_calldblstar.py, thread/thread_ident1.py, basics/slice_indices.py, basics/try_finally_return.py, basics/string_format_intbig.py**

Sample FAIL_TO_PASS test names (first 10):
```
  basics/fun_calldblstar.py
  thread/thread_ident1.py
  basics/slice_indices.py
  basics/try_finally_return.py
  basics/string_format_intbig.py
```

## Section 4 — Problem-theme distribution

Top themes across 5 issue statements (auto-clustered):

| Theme | Count | % |
|-------|-------|---|
| crash_or_traceback | 2 | 40.0% |
| wrong_output | 2 | 40.0% |
| concurrency | 1 | 20.0% |

## Section 5 — Sample issues (no patches — those are the answer)

### Sample 1 — `micropython__micropython-10095`

**Files likely affected**: `py/bc.c`
**FAIL_TO_PASS** (1 tests, first 3): `['basics/fun_calldblstar.py']`

**Problem statement (excerpt):**
> CPython difference when unpacking kwargs  The following shows a difference with CPython. It works fine if the dicts have no common keys: '''python def foo(**x):     print(x) foo(**a, **b)  # a and b are dicts ''' With these dicts, behaviour differs: '''python a = {'one': 1, 'two': 2} z = {'one': 1, 'five': 5} ''' MP: '''python >>> foo(**a, **z) {'two': 2, 'one': 1, 'five': 5} ''' CPython: '''pytho

### Sample 2 — `micropython__micropython-12158`

**Files likely affected**: `py/modthread.c`, `ports/stm32/mpthreadport.c`, `py/mpthread.h`, `ports/esp32/mpthreadport.c`, `ports/unix/mpthreadport.c`
**FAIL_TO_PASS** (1 tests, first 3): `['thread/thread_ident1.py']`

**Problem statement (excerpt):**
> Add Thread ID return to _thread.start_new_thread function Description:
 Currently, in MicroPython, the '_thread.start_new_thread' function allows starting a new thread but does not provide a direct way to obtain the ID of the newly created thread. This feature request aims to add Thread ID return to the 'start_new_thread' function, similar to CPython, to facilitate tracking and managing the create

### Sample 3 — `micropython__micropython-13039`

**Files likely affected**: `py/objslice.c`
**FAIL_TO_PASS** (1 tests, first 3): `['basics/slice_indices.py']`

**Problem statement (excerpt):**
> heap-buffer-overflow: mis-interpretation of float as int at slice_indices # Summary
 
 - **OS**: Ubuntu 22.04
 - **version**: micropython@a00c9d56db775ee5fc14c2db60eb07bab8e872dd
 - **port**: unix
 - **contribution**: Junwha Hong and Wonil Jang @S2-Lab, UNIST
 - **description**: 'slice_indices' misinterpret float value as integer value, and leads to buffer overflow.
 
 # PoC
 
 '''c
 # A claan ite

### Sample 4 — `micropython__micropython-13569`

**Files likely affected**: `py/compile.c`
**FAIL_TO_PASS** (1 tests, first 3): `['basics/try_finally_return.py']`

**Problem statement (excerpt):**
> Strange bug in try - finally block This snippet is not working properly on Micropython compared to CPython:
 
 '''python
 class IDGenerator:
     def __init__(self, max_id: int):
         self._i = 0
         self._mi = max_id
 
     def get(self):
         try:
             return self._i
         finally:
             self._i += 1
             if self._i > self._mi:
                 self._i = 0

### Sample 5 — `micropython__micropython-15898`

**Files likely affected**: `py/mpz.c`
**FAIL_TO_PASS** (1 tests, first 3): `['basics/string_format_intbig.py']`

**Problem statement (excerpt):**
> Incorrect thousands separator formatting with mpz When formatting a mpz number with the built-in thousands separator format specifier '{:,}', _and_ the first group of digits is 3 long, there is a leading ',' in the result.
 
 Reproducer says it all:
 '''
 >>> number = 123_456_789_123_456_789_123_456_789
 >>> "{:,}".format(number)
 ',123,456,789,123,456,789,123,456,789'
 '''
 
 Non-mpz numbers do n

## Section 6 — Builder guidance

When building a fix for an instance in micropython/micropython:

1. **Read the problem statement carefully** — the issue text describes the bug and often hints at root cause.
2. **Likely files**: see §2 above. py/bc.c appears in most fixes.
3. **Run the FAIL_TO_PASS tests** to see the failure first (`pytest <test_name> -v`).
4. **Inspect surrounding code** at the file paths from §2 — common bug locations.
5. **Match the theme** (§4) to known repo patterns: regression vs edge case vs API change.
6. **Generate minimal patch** — SWE-bench scoring rewards smallest viable fix.
7. **Verify PASS_TO_PASS still pass** — don't break existing functionality.

## Section 7 — Index of all instances in this repo

All 5 instance_ids live in `c:/tmp/swebench_instance_index.jsonl` (filterable by `repo == "micropython/micropython"`).

First 20 instance_ids:

- `micropython__micropython-10095` (dataset: `swe-bench-multilingual-test`)
- `micropython__micropython-12158` (dataset: `swe-bench-multilingual-test`)
- `micropython__micropython-13039` (dataset: `swe-bench-multilingual-test`)
- `micropython__micropython-13569` (dataset: `swe-bench-multilingual-test`)
- `micropython__micropython-15898` (dataset: `swe-bench-multilingual-test`)

---

*Determinex · Lunarian Data Systems · auto-generated from SWE-bench-family datasets*
