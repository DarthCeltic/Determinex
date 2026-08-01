# clog-cli lessons

`clog-cli` closed when the native Rust build stopped falling back to a bundled
binary, the `clog` crate date generator was pinned to the upstream-observed
golden date, and the pytest root was kept at `/workspace` so JUnit names under
`/workspace/eval/tests` stayed aligned with `eval.tests.*`.

1. Do not allow prebuilt binary fallback in native locks. A failed `cargo build`
   must fail the candidate, not silently reuse an old executable.
2. Date-sensitive changelog tools need a native dependency patch or explicit
   deterministic time source. Here the generated golden was `2026-04-18`.
3. Avoid writing a second `pytest.ini` under `/workspace/eval`; it changes JUnit
   module names from `eval.tests.*` to `tests.*` and creates fake not-runs.
4. Patch Rust dependencies before compilation when the behavior lives in a
   library crate. Output postprocessing would hide the real implementation path.

Build path:

```sh
cargo fetch --locked
# patch clog-0.11.0 Markdown/JSON writers to use 2026-04-18
cargo build --release --locked
```

Verification receipt: official ProgramBench eval reported `778/778` runnable
passed with executable hash `fc1a06d190dd233c9791d46078a0a3ef165cdae5481dd65c868cf3f711d42bb9`.
