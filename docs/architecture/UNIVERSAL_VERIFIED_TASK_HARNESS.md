# Universal Verified Task Harness

Determinex now has a benchmark-neutral verifier loop under `scripts/verified_task/`.

The contract is `TaskSpec`:

- workspace or repo
- instruction/prompt
- setup commands
- validation commands
- resource limits
- scoring rule
- privacy/Cloak policy

Adapters convert benchmark formats into this contract. The same runner then executes validators, records verdict-rich traces, and writes corpus JSONL on the configured staging root. By default, bulky state goes to `T:/determinex-staging/verified_tasks` or `DETERMINEX_VERIFIED_TASK_ROOT`.

## Current Language Profiles

Profiles exist for:

- Python
- Bash
- Go
- Rust
- TypeScript
- JavaScript
- Java
- C
- C++
- SQL
- Ruby
- PHP

Profiles are command defaults, not hard policy. Adapters should override them when a benchmark gives exact commands.

## CLI

```bash
python scripts/verified_task_cli.py terminal \
  --id demo \
  --instruction "run tests" \
  --workspace path/to/workspace \
  --validate "python -m pytest -q"

python scripts/verified_task_cli.py run-spec task_spec.json

python scripts/verified_task_cli.py inventory
python scripts/verified_task_cli.py compress T:/determinex-staging/verified_tasks/<run>
```

## Corpus Shape

Each attempt records:

- benchmark
- task id
- language
- prompt/instruction
- validator commands
- stdout/stderr
- verdict
- failure class
- repair prompt or patch summary when available

This is the shared bridge for ProgramBench, Terminal-Bench, SWE-style repair, DebugBench, Aider Polyglot, BigCodeBench, SQL/BIRD, and security scanner loops.

## Language Factory Doctrine

Every language/domain backend must implement the same factory sequence:

```text
Indexer
-> Task extractor
-> Safe source gate
-> Baseline verifier
-> Controlled failure generator
-> Repair pipeline
-> Oracle verifier
-> Signed corpus writer
-> Lock manifest
-> Compression candidate
```

The product is not "ask a model to fix code." The product is a verifier-backed
factory:

```text
find project
understand project
prove project works
break it in a controlled way
repair it
verify the repair
sign the trace
train, compress, and reroute from the trace
```

Language locks must preserve one contract across ecosystems: same backend
shape, same gate sequence, same signing, same manifest format. No language gets
a shortcut around license/provenance, source safety, native validators, or HMAC
corpus records.

Current lock sequence:

| Lock | Purpose |
|---|---|
| `JAVA_REPAIR_LOCK_001` | Enterprise/backend/build-system repair |
| `RUST_REPAIR_LOCK_001` | ProgramBench native CLI/tool repair |
| `PYTHON_REPAIR_LOCK_001` | SWE-bench and Python repo repair capture |
| `GO_REPAIR_LOCK_001` | Go modules, ProgramBench Go tools, multilingual routing |
| `NATIVE_C_CPP_REPAIR_LOCK_001` | DebugBench/systems repair and ProgramBench native source flips |
| `TYPESCRIPT_REPAIR_LOCK_001` | Frontend/UI repair, browser-adjacent tasks, SWE-bench Pro |
| `SQL_ORACLE_LOCK_001` | Database oracle for BIRD, BIRD-Critic, LiveSQLBench, analytics repair |
| `BROWSER_AGENT_LOCK_001` | Browser policy/oracle/replay/corpus trace contract |
| `CORPUS_COVERAGE_LOCK_001` | Corpus dashboard, benchmark-to-corpus adapter contract, durable HMAC integrity |
| `CORPUS_SCHEMA_MATURITY_LOCK_001` | Schema completeness, training eligibility, verifier/source/status backfill |
| `BENCH_TO_CORPUS_ELIGIBILITY_LOCK_001` | New benchmark rows are training-eligible only when schema-complete and signed |
| `TRAINING_CORPUS_DASHBOARD_LOCK_001` | Tracks training-eligible growth separately from signed eval evidence |
| `NO_LOOSE_BENCH_ARTIFACTS_LOCK_001` | Ensures every benchmark artifact resolves to a corpus-visible terminal status |
| `AIDER_POLYGLOT_TRACE_HARNESS_LOCK_001` | Converts Aider Polyglot-style attempts into signed schema-complete traces |
| `LOCAL_LEGACY_CORPUS_QUARANTINE_LOCK_001` | Excludes unsigned/malformed local ProgramBench legacy rows from training |
| `LEGACY_CORPUS_RECOVERY_LOCK_001` | Mines quarantined legacy rows for taxonomy, priority, replay candidates, and guarded promotion |
| `LEGACY_REPLAY_PROMOTION_LOCK_001` | Proves fresh verifier replay can write a new recovered training row without mutating legacy rows |
| `PROGRAMBENCH_REPLAY_VERIFIER_LOCK_001` | Resolves each selected replay candidate to exactly one signed training/eval/reject/infra outcome |
| `PROGRAMBENCH_REPLAY_HYDRATION_LOCK_001` | Preflights replay candidates into explicit hydration statuses before verifier execution |
| `PROGRAMBENCH_TASK_ROOT_RESOLUTION_LOCK_001` | Maps legacy candidate identities to concrete ProgramBench task/source roots before hydration |
| `PROGRAMBENCH_ROOT_DISAMBIGUATION_LOCK_001` | Selects canonical runnable roots from multiple local ProgramBench matches |
| `PROGRAMBENCH_REPLAY_IMAGE_HYDRATION_LOCK_001` | Resolves task images or explicit local no-image verifier mode before replay execution |
| `PROGRAMBENCH_REPLAY_METADATA_RECOVERY_LOCK_001` | Recovers task image/local verifier/provenance metadata without executing guessed metadata |
| `PROGRAMBENCH_ONLINE_ARTIFACT_DISCOVERY_LOCK_001` | Discovery-only artifact lane: online sources can suggest, but only pinned/scanned/provenance-recorded artifacts can hydrate |
| `PROGRAMBENCH_ONLINE_PROVIDER_REGISTRY_LOCK_001` | Restricts online discovery to exact-reference allowlisted providers before any provider calls are wired |
| `PROGRAMBENCH_ROOT_CAUSE_PACKET_LOCK_001` | Requires signed, evidence-backed root-cause packets before fresh ProgramBench reruns |
| `PROGRAMBENCH_BOUNDED_RERUN_EXECUTION_LOCK_001` | Enforces exact root-cause packet rerun scope and attempt limits before execution |
| `PROGRAMBENCH_REAL_BOUNDED_RERUN_LOCK_001` | Runs one authorized live ProgramBench attempt and records one signed outcome |
| `PROGRAMBENCH_INFRA_FAILURE_TRIAGE_LOCK_001` | Converts real bounded rerun infrastructure failures into signed recovery records |
| `PROGRAMBENCH_OPERATOR_ARTIFACT_ADMISSION_LOCK_001` | Validates operator-supplied cleanroom image provenance without hydrating or executing it |
| `PROGRAMBENCH_ARTIFACT_SOURCE_ESCALATION_LOCK_001` | Generates the exact operator provenance checklist when real image provenance is absent |
| `PROGRAMBENCH_DOCKERHUB_MANIFEST_PROVENANCE_LOCK_001` | Converts exact Docker Hub manifest metadata into a signed provenance candidate without pulling or executing |
| `PROGRAMBENCH_CLEANROOM_IMAGE_IMPORT_LOCK_001` | Imports exact digest-pinned cleanroom image bytes into quarantine, then blocks policy admission without scan evidence |
| `PROGRAMBENCH_CLEANROOM_IMAGE_SCAN_LOCK_001` | Produces signed scanner evidence or signed scanner-unavailable blockers for quarantined cleanroom images |
| `PROGRAMBENCH_CLEANROOM_IMAGE_SCANNER_ADMISSION_LOCK_001` | Admits approved scanner paths only after identity, version, and non-executing archive capability checks |
| `PROGRAMBENCH_APPROVED_SCANNER_SETUP_LOCK_001` | Produces setup/admission evidence for Trivy or Grype before scan retry |
| `PROGRAMBENCH_CLEANROOM_IMAGE_SCAN_TRIAGE_LOCK_001` | Classifies failed scan findings before remediation, alternate-source, or exception decisions |
| `PROGRAMBENCH_CLEANROOM_IMAGE_REMEDIATION_PLAN_LOCK_001` | Plans reproducible cleanroom remediation or safer-equivalent image recovery without rebuilding or executing |
| `PROGRAMBENCH_CLEANROOM_BUILD_RECIPE_RECOVERY_LOCK_001` | Recovers exact, partial, or quarantine-only cleanroom build recipe evidence without rebuilding |
| `PROGRAMBENCH_CLEANROOM_BUILD_RECIPE_PROVENANCE_GAP_LOCK_001` | Converts quarantine-only recipe reconstruction into signed missing-provenance blockers before rebuild |
| `PROGRAMBENCH_CLEANROOM_RECIPE_PROVENANCE_RECOVERY_LOCK_001` | Attempts to close recipe/base-image provenance gaps from local and already-admitted sources only |
| `PROGRAMBENCH_REBUILD_PROVENANCE_QUARANTINE_DECISION_LOCK_001` | Decides whether partial cleanroom rebuild provenance is blocked, quarantine-only, or ready without rebuilding |
| `PROGRAMBENCH_OPERATOR_PROVENANCE_REQUEST_PACKET_LOCK_001` | Generates the exact operator-facing provenance request needed to close rebuild authority gaps |
| `PROGRAMBENCH_ALTERNATE_CLEANROOM_IMAGE_PROVENANCE_LOCK_001` | Searches local/admitted evidence for explicit alternate cleanroom image provenance candidates without pulling or executing |
| `PROGRAMBENCH_UPSTREAM_ARTIFACT_AUTHORITY_RECHECK_LOCK_001` | Reconciles official ProgramBench task_cleanroom artifact authority with local rebuild/remediation/security policy gates |
| `PROGRAMBENCH_OFFICIAL_ARTIFACT_SECURITY_DECISION_LOCK_001` | Decides whether an official upstream artifact can execute, remains metadata-only, or needs later exception/sandbox gates |
| `PROGRAMBENCH_OFFICIAL_ARTIFACT_SANDBOX_REQUIREMENTS_LOCK_001` | Defines the exact stronger sandbox requirements needed before scan-failed official artifact execution can be considered |
| `PROGRAMBENCH_SECURITY_POLICY_EXCEPTION_REQUEST_LOCK_001` | Writes the operator policy-exception request packet without granting an exception |
| `PROGRAMBENCH_SECURITY_POLICY_ADMISSION_GATE_LOCK_001` | Gates real operator policy admission and records live admission as required when no real approval exists |
| `PROGRAMBENCH_OFFICIAL_ARTIFACT_EXECUTION_PREFLIGHT_LOCK_001` | Preflights all official-artifact execution prerequisites without running Docker or ProgramBench |
| `PROGRAMBENCH_TASK_SKIP_WITH_PROVENANCE_REASON_LOCK_001` | Skips Doxygen with a precise provenance/security reason instead of model-failure or benchmark-failure classification |
| `PROGRAMBENCH_DOXYGEN_LANE_FINAL_STATE_LOCK_001` | Writes the final machine-checkable Doxygen lane state |
| `PROGRAMBENCH_CAMPAIGN_STATUS_BOARD_LOCK_001` | Aggregates ProgramBench campaign status without executing anything |
| `PROGRAMBENCH_TRAINING_ELIGIBILITY_NEGATIVE_GUARD_LOCK_001` | Blocks metadata-only, scan-failed, policy-required, skipped, and partial-provenance records from training eligibility |
| `PROGRAMBENCH_RERUN_READINESS_MATRIX_LOCK_001` | Writes the operator-facing rerun readiness matrix |
| `PROGRAMBENCH_CLEANROOM_IMAGE_HYDRATION_LOCK_001` | Hydrates only admitted digest-verified, scan-passing artifacts into quarantine/cache while still refusing execution |
| `PROGRAMBENCH_INSTANCE_STATE_SCHEMA_LOCK_001` | Defines a reusable machine-readable ProgramBench instance state schema |
| `PROGRAMBENCH_BATCH001_STATE_AGGREGATOR_LOCK_001` | Aggregates Doxygen and Batch 001 replay evidence into generic instance states |
| `PROGRAMBENCH_GENERIC_OPERATOR_POLICY_ADMISSION_LOCK_001` | Generalizes operator policy admission without treating fixtures as live approvals |
| `PROGRAMBENCH_GENERIC_EXECUTION_PREFLIGHT_LOCK_001` | Generalizes non-executing ProgramBench rerun preflight across instances |
| `PROGRAMBENCH_SKIP_REASON_TAXONOMY_LOCK_001` | Separates security/provenance/infrastructure skips from model and benchmark failures |
| `PROGRAMBENCH_BATCH_SKIP_DECISION_LOCK_001` | Applies skip decisions to all known Batch 001 rows without creating training data |
| `PROGRAMBENCH_OPERATOR_ACTION_QUEUE_LOCK_001` | Produces operator evidence requests for blocked ProgramBench instances |
| `PROGRAMBENCH_CAMPAIGN_REPORTING_API_LOCK_001` | Provides a read-only deterministic JSON status API for the campaign |
| `PROGRAMBENCH_EVIDENCE_GRAPH_LOCK_001` | Links ProgramBench evidence nodes and blocker edges without authorization shortcuts |
| `PROGRAMBENCH_CODEX_LANE_FINAL_STATE_LOCK_001` | Summarizes the reusable Codex ProgramBench apparatus state |
| `PROGRAMBENCH_OPERATOR_PACKET_TEMPLATES_LOCK_001` | Generates non-approval operator packet templates for required evidence |
| `PROGRAMBENCH_OPERATOR_PACKET_VALIDATOR_LOCK_001` | Validates operator packets without granting execution |
| `PROGRAMBENCH_BATCH001_METADATA_RECOVERY_QUEUE_LOCK_001` | Queues Batch 001 metadata/provenance recovery actions |
| `PROGRAMBENCH_EXACT_PROVIDER_PROBE_PLAN_LOCK_001` | Plans exact-provider metadata probes without network, pull, or run |
| `PROGRAMBENCH_BATCH001_OPERATOR_PACKET_BUNDLE_LOCK_001` | Bundles operator packet templates for current Batch 001 actions |
| `PROGRAMBENCH_OPERATOR_INBOX_SCANNER_LOCK_001` | Scans local operator inbox packets without mutation or approval |
| `PROGRAMBENCH_OPERATOR_PACKET_ADMISSION_ROUTER_LOCK_001` | Routes validated packets to non-executing admission gates |
| `PROGRAMBENCH_BATCH001_UNBLOCK_SIMULATION_LOCK_001` | Simulates which blockers would clear if operator packets arrived |
| `PROGRAMBENCH_EVIDENCE_GRAPH_INTEGRITY_GUARD_LOCK_001` | Guards against invalid execution or training paths in ProgramBench evidence |
| `PROGRAMBENCH_OPERATOR_CLI_LOCK_001` | Provides operator-facing status/action/packet/simulation CLI commands |
| `PROGRAMBENCH_OPERATOR_OUTBOX_LOCK_001` | Writes fillable operator packet templates and a hashed outbox manifest |
| `PROGRAMBENCH_PLATFORM_COMPLETION_SCORECARD_LOCK_001` | Scores ProgramBench platform readiness without inflating blocked dimensions |
| `PROGRAMBENCH_CODEX_OPERATOR_READY_FINAL_STATE_LOCK_001` | Records the operator-ready non-executing Codex lane final state |
| `PROGRAMBENCH_OPERATOR_PACKET_ADMISSION_PROCESSING_LOCK_001` | Processes live operator inbox packets into non-executing gate-review routes |
| `PROGRAMBENCH_OPERATOR_PACKET_ADMISSION_LIVE_PACKET_REVIEW_LOCK_001` | Reviews live operator inbox packets after operator-ready prerequisites without approving execution |
| `PROGRAMBENCH_OPERATOR_READY_AUDIT_LOCK_001` | Audits the operator-ready ProgramBench lane for stale references and authority escalation |
| `DISTILLATION_LOCK_001` | Specialist-unit deployment and compression evidence gate |

Next lock:

1. `PROGRAMBENCH_OPERATOR_PACKET_ADMISSION_LIVE_GATE_REVIEW_LOCK_001`
2. `PROGRAMBENCH_OFFICIAL_ARTIFACT_SECURITY_DECISION_LOCK_001`
3. `AIDER_POLYGLOT_SAMPLE_RUN_LOCK_001`
4. `CORPUS_TRAINING_ELIGIBILITY_LOCK_001`

## Corpus Coverage Gate

The current language locks prove factory shape, not corpus maturity. Benchmark
campaigns are allowed to start, but they must act as trace harvesters:

```text
No benchmark without corpus.
No corpus without provenance.
No repair without verifier.
No trace without signature.
No claim without lock.
```

`scripts/corpus/corpus_coverage_report.py` is the corpus dashboard. It counts
rows by language, framework, build system, failure type, validator, source kind,
license bucket, benchmark source, repair outcome, safety outcome, and router or
model used. It also reports unsigned rows, missing provenance, missing verifier
fields, duplicate trace hashes, and unsafe rejection traces.

Durable corpus signatures require `DETERMINEX_CORPUS_HMAC_KEY` in `.env` or the
process environment. Rows written without a durable key are test-only and must
not be treated as train/eval material until migrated or regenerated. The
coverage report surfaces `current_signature_key_scope`,
`by_signature_key_scope`, `ephemeral_signature_count`, and
`invalid_signature_count` so memory and capability claims cannot silently depend
on non-verifiable rows.

`scripts/corpus/corpus_schema_maturity.py` is the schema maturity gate. It
separates cryptographic integrity from training readiness:

```text
Integrity green: signed, durable key, valid signature, no duplicate trace hash.
Maturity green: schema-complete, verifier-backed, source-kind labeled, status classified.
Training-eligible: schema-complete plus explicit active_training_eligible status.
```

The operating rule is:

```text
Signed is not enough.
Training-eligible requires schema-complete.
```

Legacy rows are allowed to become `active_eval_evidence`; they are not upgraded
to training fuel by migration alone. Rows must be classified as one of:

```text
active_training_eligible
active_eval_evidence
legacy_backfill_needed
quarantined
rejected
```

The local legacy ProgramBench training corpus is excluded from training by
default through `corpus/programbench/training_corpus/TRAINING_EXCLUSION.json`.
The active schema-mature corpus root is `T:/determinex_corpus`.

Legacy recovery now treats local ProgramBench rows as raw ore:

```text
legacy corpus -> parse recovery -> classification -> dedupe/provenance inference
  -> replay planning -> fresh verifier run -> new signed recovered row
```

`LEGACY_CORPUS_RECOVERY_LOCK_001` explicitly forbids in-place promotion.
Quarantined rows may feed taxonomy, priority, router risk, and replay
candidate generation. Training rows must be newly written after fresh verifier
evidence and linked with `recovered_from.legacy_row_hash`.

`LEGACY_REPLAY_PROMOTION_LOCK_001` adds the bridge from recovery planning to
clean corpus growth. It requires a fresh verifier artifact or verifier run id,
assigns failure and repair outcome labels, writes a separate
`legacy_replay_recovered` row, and applies a promotion budget:

```text
max 10 promotion attempts per scan
max 3 per tool
max 1 per duplicate cluster
```

`PROGRAMBENCH_REPLAY_VERIFIER_LOCK_001` adds the batch execution contract for
selected replay candidates. Every candidate must resolve into exactly one of:

```text
active_training_eligible
active_eval_evidence
signed_reject
signed_infra_failure
```

Replay alone cannot create training rows. Training eligibility requires a
verified failure-to-repair transition. The first Batch 001 run used the
injectable verifier without workspace roots and correctly resolved missing
hydration as signed infrastructure failures instead of loose artifacts.

`PROGRAMBENCH_REPLAY_HYDRATION_LOCK_001` splits those infrastructure failures
into actionable preflight states:

```text
HYDRATED_READY
MISSING_TASK_ROOT
MISSING_CANDIDATE_ROOT
MISSING_DOCKER_IMAGE
MISSING_EVAL_HARNESS
MISSING_BASELINE
AMBIGUOUS_TOOL_MATCH
CHECKSUM_MISMATCH
UNSUPPORTED_LEGACY_FORMAT
```

`PROGRAMBENCH_TASK_ROOT_RESOLUTION_LOCK_001` adds the identity resolver before
hydration. It indexes local ProgramBench roots, applies exact/alias/binary
passes, blocks paths outside allowed roots, and writes:

```text
assurance/evidence/programbench_task_root_resolution_batch_001.json
```

Batch 001 no longer fails as unknown. It now maps to local identity evidence but
is blocked by duplicate root ambiguity:

```text
Batch 001 task-root resolution: 0 resolved, 10 MULTIPLE_MATCHES, 0 missing
```

`PROGRAMBENCH_ROOT_DISAMBIGUATION_LOCK_001` selects canonical roots from those
multiple matches using deterministic precedence and evidence-backed overrides.
For Batch 001, all ten tools selected `per_tool_overrides` roots:

```text
Batch 001 root disambiguation: 10 CANONICAL_ROOT_SELECTED
```

After feeding those selected roots back into hydration, the blocker moved again:

```text
Batch 001 hydration after disambiguation: 0 HYDRATED_READY, 10 MISSING_DOCKER_IMAGE
```

`PROGRAMBENCH_REPLAY_IMAGE_HYDRATION_LOCK_001` splits that blocker into
image/local-verifier specific states:

```text
IMAGE_LOCAL_READY
IMAGE_HYDRATED_FROM_CACHE
IMAGE_PULL_READY
IMAGE_MISSING
IMAGE_PULL_FAILED
IMAGE_METADATA_MISSING
IMAGE_NAME_AMBIGUOUS
LOCAL_NO_IMAGE_VERIFIER_READY
LOCAL_NO_IMAGE_VERIFIER_UNSUPPORTED
ONLINE_DISCOVERY_CANDIDATE_FOUND
ONLINE_ARTIFACT_PINNED
ONLINE_ARTIFACT_REJECTED
ONLINE_ARTIFACT_AMBIGUOUS
```

Batch 001 currently resolves to:

```text
Batch 001 image hydration: 0 ready, 10 IMAGE_METADATA_MISSING
```

That means canonical roots exist, but no explicit `task_image` metadata and no
explicit local replay verifier metadata are present. The next rung is metadata
recovery or online artifact discovery, not blind execution.

`PROGRAMBENCH_REPLAY_METADATA_RECOVERY_LOCK_001` adds that rung:

```text
canonical root
  -> task_image metadata search
  -> local verifier metadata search
  -> benchmark/task provenance recovery
  -> artifact source candidate extraction
  -> replay manifest
```

Doctrine:

```text
Canonical root tells us where.
Metadata tells us how.
Verifier tells us whether.
Corpus tells us what it means.
```

Only exact metadata unlocks hydration:

```text
METADATA_EXACT_MATCH
LOCAL_VERIFIER_METADATA_FOUND
TASK_IMAGE_FOUND
```

Reconstructed metadata is quarantine-only until pinned/scanned/provenance-signed
or replaced by explicit verifier metadata. Batch 001 currently recovered:

```text
10 METADATA_RECONSTRUCTED_HIGH_CONFIDENCE
0 hydration_unlocked
10 quarantine_only
```

`PROGRAMBENCH_ONLINE_ARTIFACT_DISCOVERY_LOCK_001` adds the third lane:

```text
missing local image
  -> online artifact discovery
  -> digest/revision pin
  -> quarantine/scanner metadata
  -> signed provenance record
  -> hydration only if policy passes
```

Determinex is not limited to local artifacts, but it never trusts online artifacts
by default. Online sources may provide candidates. Only pinned, scanned,
provenance-recorded artifacts can enter the verifier path.

`PROGRAMBENCH_ONLINE_PROVIDER_REGISTRY_LOCK_001` keeps that third lane narrow.
Allowed providers are exact-reference only:

```text
docker_hub_official
ghcr_exact
github_release_metadata
huggingface_explicit
```

Broad search, unknown providers, inferred officialness, floating `latest`, and
unpinned execution remain blocked.

`PROGRAMBENCH_ROOT_CAUSE_PACKET_LOCK_001` gates fresh drain work. No close
candidate rerun is authorized without:

```text
baseline/candidate comparison
failing tests
regression diff summary
suspected patch location
suspected failure class
repair hypothesis
bounded rerun_scope
signed packet
```

The gate emits `RERUN_AUTHORIZED` only from `ROOT_CAUSE_PACKET_READY`, and only
for the packet's bounded `rerun_scope`. Stale packets, conflicting evidence,
missing critical fields, invalid signatures, and quarantine-only replay manifests
fail closed.

`PROGRAMBENCH_BOUNDED_RERUN_EXECUTION_LOCK_001` consumes that authorization and
enforces the exact target:

```text
packet authorizes scope
verifier authorizes outcome
corpus policy authorizes training
```

The bounded execution gate blocks scope mismatches, stale packets, missing
packets, attempt counts above `max_attempts`, and quarantine-only inputs. Mock
outcomes are recorded as signed `active_eval_evidence` by default; improvements
are not training rows unless a later corpus policy lock says so.

`PROGRAMBENCH_REAL_BOUNDED_RERUN_LOCK_001` applied the chain to one real
Doxygen attempt:

```text
packet: doxygen_real_bounded_rerun_20260527
scope: doxygen__doxygen.966d98e / close_lock_v7_doxygen_richgo_20260527
max_attempts: 1
outcome: REAL_BOUNDED_RERUN_INFRA_FAILURE
reason: missing cleanroom Docker image programbench/doxygen_1776_doxygen.966d98e:task_cleanroom
training_eligible: false
```

`PROGRAMBENCH_ALTERNATE_CLEANROOM_IMAGE_PROVENANCE_LOCK_001` then checks
whether an explicit alternate cleanroom image candidate already exists in
local/admitted evidence. The live Doxygen result is:

```text
status: ALTERNATE_CLEANROOM_PROVENANCE_NOT_FOUND
decision: NO_ALTERNATE_IMAGE_CANDIDATE_FOUND
exact_candidates: 0
partial_candidates: 0
blocked_candidates: 0
```

The searched sources were local evidence roots, signed ProgramBench provenance
records, admitted metadata records, internal config/cache manifests, and lock
records. No broad web search, latest tag inference, Docker pull, Docker run,
hydration, rebuild, ProgramBench rerun, policy exception, cache readiness,
execution, or training eligibility was authorized.

`PROGRAMBENCH_UPSTREAM_ARTIFACT_AUTHORITY_RECHECK_LOCK_001` prevents the
alternate-not-found result from being mistaken for an upstream artifact dead
end. It rechecks local ProgramBench docs/code, the exact Docker Hub manifest
record, the provider registry lock, and the signed Doxygen security/provenance
records:

```text
upstream_benchmark_artifact_authority: PRESENT
rebuild_provenance_authority: ABSENT
remediation_authority: ABSENT
execution_security_policy: BLOCKED_SCAN_FAILED
decision: OFFICIAL_ARTIFACT_METADATA_ONLY_ADMITTED_EXECUTION_BLOCKED_SCAN_FAILED
cache_ready: false
executable: false
training_eligible: false
```

This admits the Doxygen image only as an official upstream benchmark artifact
metadata fact. It does not authorize rebuild, remediation, hydration, Docker
execution, ProgramBench rerun, policy exception, cache readiness, or training
eligibility.

`PROGRAMBENCH_OFFICIAL_ARTIFACT_SECURITY_DECISION_LOCK_001` then keeps the
official artifact on the metadata-only path because the signed scan failed:

```text
decision: OFFICIAL_ARTIFACT_EXECUTION_BLOCKED_SCAN_FAILED
metadata_only_admitted: true
security_policy_exception_granted: false
stronger_sandbox_approved: false
docker_execution_authorized: false
programbench_rerun_authorized: false
cache_ready: false
executable: false
training_eligible: false
```

The Codex completion campaign then writes the remaining non-executing truth
chain:

```text
PROGRAMBENCH_OFFICIAL_ARTIFACT_SANDBOX_REQUIREMENTS_LOCK_001:
  status: SANDBOX_REQUIREMENTS_WRITTEN
  execution_authorized: false

PROGRAMBENCH_SECURITY_POLICY_EXCEPTION_REQUEST_LOCK_001:
  status: SECURITY_POLICY_EXCEPTION_REQUEST_WRITTEN
  human_operator_approval_required: true

PROGRAMBENCH_SECURITY_POLICY_ADMISSION_GATE_LOCK_001:
  status: SECURITY_POLICY_ADMISSION_REQUIRED
  live_policy_admission_accepted: false

PROGRAMBENCH_OFFICIAL_ARTIFACT_EXECUTION_PREFLIGHT_LOCK_001:
  status: OFFICIAL_ARTIFACT_PREFLIGHT_BLOCKED_POLICY_ADMISSION_REQUIRED

PROGRAMBENCH_TASK_SKIP_WITH_PROVENANCE_REASON_LOCK_001:
  reason: POLICY_ADMISSION_REQUIRED_FOR_SCAN_FAILED_OFFICIAL_ARTIFACT

PROGRAMBENCH_DOXYGEN_LANE_FINAL_STATE_LOCK_001:
  artifact_authority: PRESENT
  rebuild_authority: ABSENT
  remediation_authority: ABSENT
  security_execution_authority: ABSENT_PENDING_OPERATOR_POLICY_ADMISSION
  bounded_rerun_authority: BLOCKED_BY_SECURITY_PREFLIGHT
  official_score_available: false
  cache_ready: false
  executable: false
  training_eligible: false
  next_unblocker: OPERATOR_SECURITY_POLICY_ADMISSION
```

The campaign status board and rerun readiness matrix both classify Doxygen as
blocked by operator security policy admission, not as an artifact dead end, not
as a model failure, and not as training data.

`PROGRAMBENCH_OPERATOR_PROVENANCE_REQUEST_PACKET_LOCK_001` converts that
decision into an operator-facing evidence request, not an admission:

```text
status: OPERATOR_PROVENANCE_REQUEST_PACKET_WRITTEN
current_decision: REBUILD_QUARANTINE_DECISION_PARTIAL_ONLY
missing_evidence:
  - original_cleanroom_build_recipe
  - original_build_context
  - pinned_base_image_digest
  - toolchain_version_provenance
  - operator_signed_source_base_recipe_binding
original_go_runtime_expected: 1.21.0
remediation_target_go_runtime: 1.24.13
fidelity_risk: material
```

The packet explicitly accepts only digest/source-linked provenance, such as an
original build recipe, pinned base-image digest, signed internal build record,
reproducible official build recipe, or operator-signed packet binding source,
base digest, recipe, toolchain, and target image. It rejects latest tags,
name-only base images, inferred official images, OCI history alone,
reconstructed Dockerfile-style steps alone, broad search results, fixture
admissions, and screenshots or prose claims without digest/source linkage.

The request packet still authorizes nothing executable:

```text
image_rebuild_authorized: false
docker_pull_authorized: false
docker_execution_authorized: false
hydration_authorized: false
programbench_rerun_authorized: false
cache_ready: false
executable: false
training_eligible: false
```

The run did not retry and did not touch Richgo or any other close candidate.

`PROGRAMBENCH_INFRA_FAILURE_TRIAGE_LOCK_001` converts that failed-closed
attempt into a deterministic recovery object:

```text
source_record: assurance/evidence/programbench_real_bounded_reruns/doxygen_real_bounded_rerun_20260527.REAL_BOUNDED_RERUN_INFRA_FAILURE.json
triage_record: assurance/evidence/programbench_infra_failure_triage/doxygen_real_bounded_rerun_20260527.MISSING_CLEANROOM_IMAGE.triage.json
failure_type: MISSING_CLEANROOM_IMAGE
missing_image: programbench/doxygen_1776_doxygen.966d98e:task_cleanroom
local_image_status: IMAGE_MISSING_LOCAL
source_status: IMAGE_RECOVERY_REQUIRES_OPERATOR
provenance_status: IMAGE_HYDRATION_BLOCKED_NO_PROVENANCE
training_eligible: false
```

Allowed next actions are local inventory check, exact provider lookup if
configured, and operator-supplied digest/provenance. Blocked actions remain
blind Docker pulls, broad web search, inferred official images, execution from
quarantine, and direct public-untrusted hydration.

`PROGRAMBENCH_OPERATOR_ARTIFACT_ADMISSION_LOCK_001` adds the next gate:

```text
operator claim
  -> exact triage match
  -> exact image match
  -> exact Doxygen scope match
  -> digest or immutable revision required
  -> provenance notes required
  -> public-untrusted direct hydration blocked
  -> signed hydration_candidate only
  -> executable: false
  -> training_eligible: false
```

This is admission only. It does not pull, hydrate, scan, cache, execute, rerun
Doxygen, or promote anything to training. A fixture acceptance record exists
under `assurance/evidence/programbench_operator_artifact_admissions/fixtures/`
to prove the gate accepts well-formed provenance without becoming execution
permission.

`PROGRAMBENCH_DOCKERHUB_MANIFEST_PROVENANCE_LOCK_001` records the next
discovery: local Docker inspection still reports no such image, but exact
Docker Hub manifest metadata exists for the Doxygen cleanroom image. The
lookup was metadata-only:

```text
image: programbench/doxygen_1776_doxygen.966d98e:task_cleanroom
registry: docker.io
tag: task_cleanroom
manifest_digest: sha256:cc50d0f7e9a1f3f90512e3d4c34781f4686a8fa3774fbff489947ef41bde2e72
pulled_layers: false
executed: false
hydration_authorized: false
execution_authorized: false
training_eligible: false
```

That turns the trail from missing real provenance into a signed remote-manifest
provenance candidate and a real operator admission claim. It still does not
pull layers, scan, cache, execute, rerun Doxygen, or mark anything training
eligible.

`PROGRAMBENCH_CLEANROOM_IMAGE_HYDRATION_LOCK_001` is the next gate after
admission. It requires a real admitted artifact import path, the admitted
digest, a passing scan result, and policy admission before anything can become
cache-ready. Running it against the real Doxygen admission without an imported
artifact writes a signed fail-closed record:

```text
admission_record: assurance/evidence/programbench_operator_artifact_admissions/programbench_doxygen_1776_doxygen.966d98e_task_cleanroom.OPERATOR_ARTIFACT_ADMISSION_ACCEPTED.json
status: CLEANROOM_IMAGE_BLOCKED_NO_ARTIFACT
expected_digest: sha256:cc50d0f7e9a1f3f90512e3d4c34781f4686a8fa3774fbff489947ef41bde2e72
reason: artifact_import_path_required_for_hydration
cache_ready: false
executable: false
training_eligible: false
```

The hydration lock can copy a digest-verified, scan-passing artifact into
quarantine/cache, but it still does not execute Docker, rerun ProgramBench, or
promote anything to training.

`PROGRAMBENCH_CLEANROOM_IMAGE_IMPORT_LOCK_001` then performed the live import
step by exact digest. It pulled/saved the image bytes into quarantine, verified
the observed digest against the admitted manifest digest, and stopped because
no scanner evidence was available:

```text
image: programbench/doxygen_1776_doxygen.966d98e:task_cleanroom
source: docker.io/programbench/doxygen_1776_doxygen.966d98e@sha256:cc50d0f7e9a1f3f90512e3d4c34781f4686a8fa3774fbff489947ef41bde2e72
artifact_import_path: T:/determinex_artifacts/quarantine/programbench/sha256_cc50d0f7e9a1f3f90512e3d4c34781f4686a8fa3774fbff489947ef41bde2e72.tar
status: CLEANROOM_IMAGE_IMPORT_SCAN_UNAVAILABLE
observed_digest: sha256:cc50d0f7e9a1f3f90512e3d4c34781f4686a8fa3774fbff489947ef41bde2e72
docker_executed: false
cache_ready: false
training_eligible: false
```

That moves the blocker from missing bytes to missing scan evidence. The image
still cannot hydrate to cache or execute until scan/policy evidence exists.

`PROGRAMBENCH_CLEANROOM_IMAGE_SCAN_LOCK_001` formalizes that blocker. It loads
the signed import record, verifies the artifact exists, confirms the import
record digest, detects approved scanners, and writes signed scan evidence. On
the current machine no approved scanner is available, so the Doxygen tar remains
blocked:

```text
artifact_path: T:/determinex_artifacts/quarantine/programbench/sha256_cc50d0f7e9a1f3f90512e3d4c34781f4686a8fa3774fbff489947ef41bde2e72.tar
status: CLEANROOM_IMAGE_SCAN_UNAVAILABLE
expected_digest: sha256:cc50d0f7e9a1f3f90512e3d4c34781f4686a8fa3774fbff489947ef41bde2e72
observed_digest: sha256:cc50d0f7e9a1f3f90512e3d4c34781f4686a8fa3774fbff489947ef41bde2e72
file_sha256: sha256:7eba6daa485e518cea068e847ead2236a633d6f50c1606896dd0eb4cfe12534b
file_size: 703348224
reason: no_approved_scanner_available
cache_ready: false
executable: false
training_eligible: false
```

Approved scanner evidence can come from Trivy, Grype, or Docker Scout only when
usable without executing the image.

`PROGRAMBENCH_CLEANROOM_IMAGE_SCANNER_ADMISSION_LOCK_001` separates scanner
configuration from scanning. It verifies scanner identity, version, and
non-executing archive-scan capability before the scan gate may consume a
scanner. On the current machine, Trivy and Grype were not found. Docker was
found as a Docker Scout candidate, but admission failed closed:

```text
scanner_name: docker_scout
scanner_path: C:/Program Files/Docker/Docker/resources/bin/docker.EXE
status: CLEANROOM_SCANNER_VERSION_FAILED
reason: Docker config access denied and docker scout command unavailable
cache_ready: false
executable: false
training_eligible: false
```

The Doxygen artifact remains blocked at scanner admission. No scan, hydration,
Docker execution, ProgramBench rerun, cache readiness, or training eligibility
is authorized by this lock.

`PROGRAMBENCH_APPROVED_SCANNER_SETUP_LOCK_001` adds the operator/tooling setup
rung. It prefers Trivy, falls back to Grype, accepts an explicit operator path,
then reruns scanner admission for the candidate path. It does not install
arbitrary binaries, scan the Doxygen artifact, hydrate, execute Docker, rerun
ProgramBench, or mark anything cache-ready/training-eligible. On the current
machine Trivy was installed through the operator-visible package manager flow
and admitted:

```text
status: APPROVED_SCANNER_ADMISSION_PASSED
scanner: trivy
scanner_version: Version: 0.70.0
capability: trivy image --input <archive.tar> --format json
cache_ready: false
executable: false
training_eligible: false
```

The scan gate was then rerun against the quarantined Doxygen tar. It completed
without Docker container execution or ProgramBench execution, but failed policy:

```text
status: CLEANROOM_IMAGE_SCAN_FAILED
scanner: trivy
critical: 38
high: 617
medium: 2729
low: 154
total: 3538
cache_ready: false
executable: false
training_eligible: false
```

Hydration consumed that signed scan record and remained blocked:

```text
status: CLEANROOM_IMAGE_SCAN_FAILED
policy_result: CLEANROOM_IMAGE_POLICY_BLOCKED
reason: security_scan_policy_failed
cache_ready: false
executable: false
training_eligible: false
```

`PROGRAMBENCH_CLEANROOM_IMAGE_SCAN_TRIAGE_LOCK_001` classifies that failed scan
before any remediation, alternate-source, or exception decision. The Doxygen
image triage says:

```text
status: CLEANROOM_IMAGE_SCAN_TRIAGED
recommendation: REMEDIATE_IMAGE_REQUIRED
critical: 38
high: 617
medium: 2729
low: 154
critical_high_with_fix: 650
critical_high_without_fix: 5
dominant critical/high category: language_runtime
top critical packages: Go stdlib v1.21.0
policy_blocked: true
cache_ready: false
executable: false
training_eligible: false
```

The next Codex decision is no longer scanner setup or scan execution. It is
cleanroom image remediation planning, with alternate-source provenance as the
fallback. A policy exception is not the default path for this finding volume.
No bounded Doxygen rerun is allowed from this image while scan policy is
blocked.

`PROGRAMBENCH_CLEANROOM_IMAGE_REMEDIATION_PLAN_LOCK_001` converts that triage
into a signed plan, not a rebuild. The plan keeps the image blocked and names
the missing proof inputs:

```text
status: CLEANROOM_IMAGE_REMEDIATION_PLAN_WRITTEN
recommendation: REMEDIATE_IMAGE_REQUIRED
dominant risk category: language_runtime
primary strategy: update_go_runtime_toolchain
Go target: 1.24.13
requires build recipe: true
requires base image provenance: true
fidelity risk: material
cache_ready: false
executable: false
training_eligible: false
```

The next Codex rung is build-recipe/base-provenance recovery, not policy
exception and not Doxygen execution. Any rebuilt or alternate image must enter
through a later provenance/import/scan/hydration sequence and then revalidate
the bounded Doxygen rerun before execution.

`PROGRAMBENCH_CLEANROOM_BUILD_RECIPE_RECOVERY_LOCK_001` performs that local
recovery search. For Doxygen, it finds ProgramBench task metadata and OCI image
config history in the quarantined tar. The image history reconstructs the
Dockerfile-style steps and identifies Go `1.21.0`, but it is not the original
recipe file and it lacks a pinned base image digest:

```text
status: BUILD_RECIPE_RECONSTRUCTED_QUARANTINE_ONLY
task_metadata_present: true
image_config_history_present: true
original_recipe_file_recovered: false
base_image_digest_present: false
go_runtime_version_detected: 1.21.0
go_target: 1.24.13
go_update_compatible: true
fidelity class: material_fidelity_change
cache_ready: false
executable: false
training_eligible: false
```

Credential-like material in image history is redacted before evidence is
written. The next rung is a provenance-gap lock or exact build-recipe/base
provenance recovery; this quarantine-only reconstruction is not allowed to
build, hydrate, execute, or authorize a Doxygen rerun.

`PROGRAMBENCH_CLEANROOM_BUILD_RECIPE_PROVENANCE_GAP_LOCK_001` turns that
quarantine-only reconstruction into a signed blocker packet. It verifies the
remediation plan and recipe recovery records agree on the Doxygen image and
digest, then records the proof gaps:

```text
status: BUILD_RECIPE_PROVENANCE_GAP_WRITTEN
ORIGINAL_RECIPE_MISSING
BASE_IMAGE_DIGEST_MISSING
RECONSTRUCTED_FROM_IMAGE_HISTORY_ONLY
MATERIAL_FIDELITY_RISK
REBUILD_NOT_AUTHORIZED
```

The packet states that OCI image history can explain probable build steps, but
it is not equivalent to the original Dockerfile or benchmark-faithful build
recipe. The missing closure evidence is:

```text
original cleanroom build recipe
pinned base image digest
independent non-history recipe source
Go runtime update plan
```

Until those gaps close, the Doxygen cleanroom artifact remains:

```text
rebuild_authorized: false
docker_execution_authorized: false
hydration_authorized: false
programbench_rerun_authorized: false
cache_ready: false
executable: false
training_eligible: false
```

`PROGRAMBENCH_CLEANROOM_RECIPE_PROVENANCE_RECOVERY_LOCK_001` attempts to close
those gaps using only local evidence roots and already-admitted provenance
records. It searches ProgramBench task metadata, signed cleanroom evidence,
operator admission records, Docker Hub manifest provenance, and local lock
records. It does not perform broad web search, Docker pulls, hydration, image
rebuilds, ProgramBench reruns, or policy exceptions.

For Doxygen, the recovery is partial and quarantine-only:

```text
status: RECIPE_PROVENANCE_RECOVERED_PARTIAL
decision: REBUILD_PROVENANCE_PARTIAL_QUARANTINE_ONLY
original_cleanroom_build_recipe_closed: false
pinned_base_image_digest_closed: false
go_runtime_update_plan_available: true
fidelity_risk: material
cache_ready: false
executable: false
training_eligible: false
```

The lock confirms the existing clues are useful, but they still do not authorize
a benchmark-faithful rebuild. The original cleanroom recipe and pinned base
image digest remain the hard missing proof objects.

`PROGRAMBENCH_REBUILD_PROVENANCE_QUARANTINE_DECISION_LOCK_001` turns that
partial recovery into the machine-checkable rebuild boundary:

```text
decision: REBUILD_QUARANTINE_DECISION_PARTIAL_ONLY
remediation_technically_possible: true
go_runtime_current: 1.21.0
go_runtime_target: 1.24.13
original_recipe_gap_open: true
pinned_base_image_digest_gap_open: true
rebuild_provenance_authorized: false
```

This is the explicit distinction:

```text
Go remediation is technically imaginable.
Benchmark-faithful rebuild authority is not present.
```

The decision keeps every execution boundary closed:

```text
image_rebuild_authorized: false
docker_pull_authorized: false
docker_execution_authorized: false
hydration_authorized: false
programbench_rerun_authorized: false
cache_ready: false
executable: false
training_eligible: false
```

`PROGRAMBENCH_ARTIFACT_SOURCE_ESCALATION_LOCK_001` now handles both cases. The
accepted fixture is explicitly ignored for real hydration, while the admitted
Docker Hub manifest claim marks escalation not required and points to the
hydration gate. The signed escalation record says:

```text
missing_image: programbench/doxygen_1776_doxygen.966d98e:task_cleanroom
status: ARTIFACT_SOURCE_ESCALATION_WRITTEN
ARTIFACT_SOURCE_ESCALATION_NOT_REQUIRED_REAL_ADMISSION_EXISTS
FIXTURE_ADMISSION_IGNORED
NO_HYDRATION_AUTHORIZED
NO_EXECUTION_AUTHORIZED
training_eligible: false
```

Accepted operator inputs are a local image tar with sha256 digest and source
notes, a registry reference pinned by digest, an official ProgramBench build
recipe with reproducible hash, or a signed internal cache record. Rejected
inputs include `latest`, name-only images, unverified public images, fixture
admissions, and quarantine-only artifacts.

Current legacy mining ladder:

```text
005k scan: complete
025k scan: complete
100k scan: complete
100k replay candidates: 99909
100k unrecoverable rows: 91
Batch 001 selected: 10 candidates, 10 tools, 3 failure classes
Batch 001 replay attempted: 10
Batch 001 signed infra failures: 10
Batch 001 loose artifacts: 0
Batch 001 active_training_eligible: 0
Batch 001 hydration: 0 HYDRATED_READY, 10 MISSING_DOCKER_IMAGE
Batch 001 task-root resolution: 0 resolved, 10 MULTIPLE_MATCHES
Batch 001 root disambiguation: 10 CANONICAL_ROOT_SELECTED
Batch 001 image hydration: 0 ready, 10 IMAGE_METADATA_MISSING
Batch 001 metadata recovery: 0 hydration_unlocked, 10 METADATA_RECONSTRUCTED_HIGH_CONFIDENCE
Batch 001 online discovery: 0 pinned, 10 IMAGE_MISSING (searcher not configured)
```

Current corpus posture after the 2026-05-27 close-lock and 7zip reruns:

```text
T:/determinex_corpus:
  active_eval_evidence: 13478
  active_training_eligible: 0
  unsigned: 0
  invalid signatures: 0
  duplicate trace hashes: 0
  parse errors: 0

corpus/programbench/training_corpus:
  excluded_from_training_by_default
  reason: unsigned/malformed legacy ProgramBench rows
  required promotion path: parse repair -> schema backfill -> provenance recovery
    -> verifier labeling -> dedupe -> durable re-signing
```

Minimum external-claim threshold is intentionally higher than the starting lock:

```text
>= 100 verified signed traces per major language
>= 25 traces per major failure class
>= 3 source types per language
>= 1 real benchmark integration per priority language
0 unsigned corpus rows
0 unlicensed corpus rows
0 unsafe source-gate bypasses
dedupe report generated
corpus card written
```

Until those thresholds are met, benchmark work is a campaign generator rather
than a public domination claim.

Memory-derived status is never enough for a benchmark or capability claim. Any
claim that touches score, corpus size, lock status, or model capability must be
backed by current eval JSON, lock manifest, coverage report, or live process
state before it is repeated in docs or launch material.

## Benchmark Trace Contract

Every benchmark adapter must preserve four conversions:

```text
attempt_to_trace()
reject_to_trace()
accept_to_trace()
failure_to_repair_task()
```

The default contract lives in `scripts/verified_task/benchmark_trace_contract.py`.
Adapters can specialize it, but they cannot skip signed success, reject, infra
failure, or repair-task traces.

`scripts/verified_task/bench_to_corpus_eligibility.py` is the write-time
training eligibility gate for new benchmark traces. It stamps complete rows as
`active_training_eligible` and marks incomplete rows non-training-eligible
instead of letting them silently enter the training pool. The first covered
surfaces are:

- ProgramBench accept and reject traces
- Aider Polyglot traces
- Terminal-Bench traces
- SWE-bench Pro traces
- SQL/BIRD traces
- Browser traces

Required new-row fields:

```text
schema_version
record_status
corpus_type
language or environment_type
source_kind
source_benchmark
license_provenance or license_bucket
verifier_command
verifier_result
failure_class
failure_type
repair_outcome
trace_hash_schema_version
trace_hash
signature_key_scope
_sig
```

## Compression Runtime Gate

Specialist units are not deployed directly from a training run. They must pass:

```text
signed corpus
-> no unsigned rows
-> license policy enforced
-> train/eval split deduped
-> held-out specialist beats baseline
-> safety regression suite passes
-> model card written
-> data card written
-> unit registry status safety_checked
-> deploy
```

The unit registry lives under `scripts/units/` and gives each specialist an
explicit lifecycle, allowed task list, blocked task list, eval lock, safety
lock, and license clearance lock.
