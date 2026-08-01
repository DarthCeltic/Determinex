---
name: swebench-tokio-rs__tokio
description: SWE-bench repo behavioral spec for tokio-rs/tokio. Aggregated from 34 bug-fix instances across 2 dataset(s). Inject into builder prompt for SWE-bench tasks targeting this repo.
type: swebench-repo-spec
---

# tokio-rs/tokio — SWE-bench Repo Spec

> **34 bug-fix instances** across 2 dataset(s); language(s): python, rust.

## Section 1 — Dataset coverage

| Dataset | Instances |
|---------|-----------|
| multi-swe-bench | 25 |
| swe-bench-multilingual-test | 9 |

## Section 2 — Where bugs typically live (top files touched in fixes)

| File | Times touched |
|------|---------------|
| `tokio/src/macros/select.rs` | 4 |
| `tokio/Cargo.toml` | 3 |
| `tokio/src/io/async_fd.rs` | 3 |
| `tokio-macros/src/entry.rs` | 3 |
| `tokio/src/io/poll_evented.rs` | 2 |
| `tokio/src/sync/broadcast.rs` | 2 |
| `tokio/src/net/unix/stream.rs` | 2 |
| `tokio/src/net/unix/listener.rs` | 2 |
| `tokio-stream/src/lib.rs` | 2 |
| `tokio-macros/src/lib.rs` | 2 |
| `tokio/src/runtime/builder.rs` | 2 |
| `tokio/src/task/local.rs` | 2 |
| `tokio/src/net/unix/datagram/socket.rs` | 2 |
| `tokio/src/sync/semaphore.rs` | 2 |
| `tokio/src/io/interest.rs` | 2 |
| `tokio/src/io/ready.rs` | 2 |
| `tokio/src/net/udp.rs` | 2 |
| `tokio/src/signal/unix/driver.rs` | 1 |
| `tokio/src/runtime/scheduler/multi_thread/handle/metrics.rs` | 1 |
| `tokio/src/runtime/scheduler/multi_thread_alt/handle/metrics.rs` | 1 |
| `tokio/src/sync/mpsc/block.rs` | 1 |
| `tokio/src/io/util/write_all_buf.rs` | 1 |
| `tokio-util/src/time/delay_queue.rs` | 1 |
| `tokio/src/fs/file.rs` | 1 |
| `.github/workflows/ci.yml` | 1 |
| `tokio-stream/Cargo.toml` | 1 |
| `tokio/src/runtime/blocking/pool.rs` | 1 |
| `benches/Cargo.toml` | 1 |
| `examples/dump.rs` | 1 |
| `tokio-util/Cargo.toml` | 1 |

## Section 3 — Test framework signal

Detected: **unknown — sample names: net_types_are_unwind_safe, unix_net_types_are_unwind_safe, resubscribe_to_closed_channel, io_driver_ready_count, num_blocking_threads**

Sample FAIL_TO_PASS test names (first 10):
```
  net_types_are_unwind_safe
  unix_net_types_are_unwind_safe
  resubscribe_to_closed_channel
  io_driver_ready_count
  num_blocking_threads
  test_is_empty_32_msgs
  write_all_buf_vectored
  wake_after_remove_last
  abstract_socket_name
  empty_read
```

## Section 4 — Problem-theme distribution

Top themes across 34 issue statements (auto-clustered):

| Theme | Count | % |
|-------|-------|---|
| concurrency | 2 | 22.2% |
| other | 2 | 22.2% |
| crash_or_traceback | 1 | 11.1% |
| documentation | 1 | 11.1% |
| edge_case | 1 | 11.1% |
| performance | 1 | 11.1% |
| wrong_output | 1 | 11.1% |

## Section 5 — Sample issues (no patches — those are the answer)

### Sample 1 — `tokio-rs__tokio-4384`

**Files likely affected**: `tokio/src/io/poll_evented.rs`
**FAIL_TO_PASS** (2 tests, first 3): `['net_types_are_unwind_safe', 'unix_net_types_are_unwind_safe']`

**Problem statement (excerpt):**
> 'tokio::net::UdpSocket' is not marked as UnwindSafe **Version**
 '''
 ├── tokio v1.6.0
 │   └── tokio-macros v1.2.0 (proc-macro)
     │   │   ├── tokio v1.6.0 (*)
     │   │   ├── tokio-util v0.6.7
     │   │   │   └── tokio v1.6.0 (*)
     │   ├── tokio v1.6.0 (*)
     ├── tokio v1.6.0 (*)
     ├── tokio-stream v0.1.6
     │   └── tokio v1.6.0 (*)
     ├── tokio-tungstenite v0.13.0
     │   ├── t

### Sample 2 — `tokio-rs__tokio-4867`

**Files likely affected**: `tokio/src/sync/broadcast.rs`
**FAIL_TO_PASS** (1 tests, first 3): `['resubscribe_to_closed_channel']`

**Problem statement (excerpt):**
> Resubscribing to a closed broadcast receiver will hang on a call to 'recv' **Version**
 tokio v1.19.2, tokio master (4daeea8cad1ce8e67946bc0e17d499ab304b5ca2)
 
 **Platform**
 Windows 10 64 bit
 
 **Description**
 Attempting to resubscribe to a closed broadcast receiver will hang on calls to 'recv'.
 
 I tried this code:
 'Cargo.toml':
 '''toml
 [package]
 name = "tokio-broadcast-bug"
 version = "

### Sample 3 — `tokio-rs__tokio-4898`

**Files likely affected**: `tokio/src/signal/unix/driver.rs`
**FAIL_TO_PASS** (1 tests, first 3): `['io_driver_ready_count']`

**Problem statement (excerpt):**
> Unix signal driver signals writable interest without ever writing **Version**
 tokio: 1.20.1
 
 **Platform**
 (any Unix with signal feature enabled)
 
 **Description**
 https://github.com/tokio-rs/tokio/blob/2099d0bd87fe53aa98a7c02334852d279baeb779/tokio/src/signal/unix/driver.rs#L79
 
 Here the 'WRITABLE' interest is set, but the driver never writes this descriptor.
 
 **Why this is a problem**
 

### Sample 4 — `tokio-rs__tokio-6551`

**Files likely affected**: `tokio/src/runtime/scheduler/multi_thread/handle/metrics.rs`, `tokio/src/runtime/scheduler/multi_thread_alt/handle/metrics.rs`
**FAIL_TO_PASS** (1 tests, first 3): `['num_blocking_threads']`

**Problem statement (excerpt):**
> runtime metrics blocking threads miscount **Version**
 
 'cargo tree | grep tokio'
 '''
 measured-tokio v0.0.21 (/Users/conrad/Documents/code/better-metrics/tokio)
 └── tokio v1.37.0
 └── tokio v1.37.0 (*)
 '''
 
 **Platform**
 '''
 Darwin Conrads-MacBook-Pro.local 23.4.0 Darwin Kernel Version 23.4.0: Fri Mar 15 00:12:49 PDT 2024; root:xnu-10063.101.17~1/RELEASE_ARM64_T6020 arm64
 '''
 
 **Descrip

### Sample 5 — `tokio-rs__tokio-6603`

**Files likely affected**: `tokio/src/sync/mpsc/block.rs`
**FAIL_TO_PASS** (1 tests, first 3): `['test_is_empty_32_msgs']`

**Problem statement (excerpt):**
> Every 32 messages 'is_empty()' on 'Receiver' and 'UnboundedReceiver' returns 'false' even though len == 0 **Version**
 tokio v1.37.0
 
 **Platform**
 Windows 10, 64 bits
 
 **Description**
 
 This issue was first mentionned in a [stackoverflow question](https://stackoverflow.com/questions/78552088/rust-tokiosyncmpscchannel-is-empty-returning-false-when-len-returns-0)
 Every 32 messages, after read

### Sample 6 — `tokio-rs__tokio-6724`

**Files likely affected**: `tokio/src/io/util/write_all_buf.rs`
**FAIL_TO_PASS** (1 tests, first 3): `['write_all_buf_vectored']`

**Problem statement (excerpt):**
> Vectored IO for 'write_all_buf' **Is your feature request related to a problem? Please describe.**
 
 The 'AsyncWriteExt' trait provides the 'write_all_buf' function to write the entire contents of a 'Buf' type to the underlying writer. However, if the buf is fragmented (eg a VecDeque<u8> or Chain), then it can have potentially bad performance with the current implementation, writing many small bu

### Sample 7 — `tokio-rs__tokio-6752`

**Files likely affected**: `tokio-util/src/time/delay_queue.rs`
**FAIL_TO_PASS** (1 tests, first 3): `['wake_after_remove_last']`

**Problem statement (excerpt):**
> DelayQueue not woken when last item removed **Version**
 
 ' tokio-util v0.7.11'
 
 **Platform**
 'Linux 5.15.0-117-generic #127-Ubuntu SMP Fri Jul 5 20:13:28 UTC 2024 x86_64'
 
 **Description**
 When 'DelayQueue::poll_expired' returns 'Pending' it grabs a 'Waker' and stores it in [self.waker](https://github.com/tokio-rs/tokio/blob/master/tokio-util/src/time/delay_queue.rs#L155). However, this wak

### Sample 8 — `tokio-rs__tokio-6838`

**Files likely affected**: `tokio/src/net/unix/stream.rs`, `tokio/src/net/unix/listener.rs`
**FAIL_TO_PASS** (1 tests, first 3): `['abstract_socket_name']`

**Problem statement (excerpt):**
> UnixListener::bind with abstract unix socket path has an extra \0 prefix **Version**
 
 v1.40.0
 
 **Platform**
 Linux VM-66-53-centos 5.4.241-1-tlinux4-0017.12 #1 SMP Fri Aug 2 14:51:21 CST 2024 x86_64 x86_64 x86_64 GNU/Linux
 
 **Description**
 
 Example code:
 
 '''rust
 let abstract_path = "\0/tmp/mesh/business/mmmeshexample";
 let listener = UnixListener::bind(abstract_path).unwrap();
 '''
 

## Section 6 — Builder guidance

When building a fix for an instance in tokio-rs/tokio:

1. **Read the problem statement carefully** — the issue text describes the bug and often hints at root cause.
2. **Likely files**: see §2 above. tokio/src/macros/select.rs appears in most fixes.
3. **Run the FAIL_TO_PASS tests** to see the failure first (`pytest <test_name> -v`).
4. **Inspect surrounding code** at the file paths from §2 — common bug locations.
5. **Match the theme** (§4) to known repo patterns: regression vs edge case vs API change.
6. **Generate minimal patch** — SWE-bench scoring rewards smallest viable fix.
7. **Verify PASS_TO_PASS still pass** — don't break existing functionality.

## Section 7 — Index of all instances in this repo

All 34 instance_ids live in `c:/tmp/swebench_instance_index.jsonl` (filterable by `repo == "tokio-rs/tokio"`).

First 20 instance_ids:

- `tokio-rs__tokio-4384` (dataset: `swe-bench-multilingual-test`)
- `tokio-rs__tokio-4867` (dataset: `swe-bench-multilingual-test`)
- `tokio-rs__tokio-4898` (dataset: `swe-bench-multilingual-test`)
- `tokio-rs__tokio-6551` (dataset: `swe-bench-multilingual-test`)
- `tokio-rs__tokio-6603` (dataset: `swe-bench-multilingual-test`)
- `tokio-rs__tokio-6724` (dataset: `swe-bench-multilingual-test`)
- `tokio-rs__tokio-6752` (dataset: `swe-bench-multilingual-test`)
- `tokio-rs__tokio-6838` (dataset: `swe-bench-multilingual-test`)
- `tokio-rs__tokio-7139` (dataset: `swe-bench-multilingual-test`)
- `tokio-rs__tokio-7124` (dataset: `multi-swe-bench`)
- `tokio-rs__tokio-7111` (dataset: `multi-swe-bench`)
- `tokio-rs__tokio-6967` (dataset: `multi-swe-bench`)
- `tokio-rs__tokio-6742` (dataset: `multi-swe-bench`)
- `tokio-rs__tokio-6618` (dataset: `multi-swe-bench`)
- `tokio-rs__tokio-6462` (dataset: `multi-swe-bench`)
- `tokio-rs__tokio-6409` (dataset: `multi-swe-bench`)
- `tokio-rs__tokio-6345` (dataset: `multi-swe-bench`)
- `tokio-rs__tokio-6339` (dataset: `multi-swe-bench`)
- `tokio-rs__tokio-6290` (dataset: `multi-swe-bench`)
- `tokio-rs__tokio-6280` (dataset: `multi-swe-bench`)
- ... (14 more)

---

*Determinex · Lunarian Data Systems · auto-generated from SWE-bench-family datasets*
