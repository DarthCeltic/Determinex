# Native-rebuild vs ProgramBench solve (honest bookkeeping)

(historical) The prior "65-82 locks" are **native rebuilds**: Determinex shipped each tool's real upstream
source and rebuilt it. That is a genuine capability (build any tool from source) but it is
**NOT a ProgramBench solve** — PB requires a from-scratch *reimplementation* from the
binary's observable behavior (no source, no wrapper). Shipping source bypasses the
benchmark exactly like the cargo-clone shortcut the PB authors forbid.

**Status:** the lock counts in CLAUDE.md / the board are native-rebuild counts, not PB
solves. Until each is replaced by a reimplementation scored on the official v1.2.2 harness,
they must NOT be claimed as ProgramBench results. The legitimate engine
(determinex_pb_reimpl + determinex_observe + determinex_pb_official_eval + corpus coach) produces
real PB solves; gron is the first proven path (official eval working; capable model climbing).

This file is the canonical correction; CLAUDE.md's ProgramBench section + the board still
need their headline numbers relabeled accordingly.
