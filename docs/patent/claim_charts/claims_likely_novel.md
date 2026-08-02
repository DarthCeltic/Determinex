---
title: "Claim Triage — LIKELY NOVEL (no clear prior art in the 7-reference set)"
status: DRAFT — for attorney/inventor review only. Not a legal opinion.
date: 2026-06-10
source_sections: WHITE_PAPER.md §3.4, §9.1–9.9, §10, §13; PROJECT_CLOAK.md
note: >
  "Likely novel" means not anticipated by the 7 identified references. It does NOT mean
  patentable. Additional prior art search required before filing. These are high-priority
  candidates for independent claim drafting.
---

# Claims Likely Novel

These claim concepts appear to survive the 7-reference prior art set with no narrowing needed.
They should be prioritized for independent claim slots. Attorney to conduct full search before
treating any of these as confirmed novel.

---

## NOVEL-01: Context Paradox Pattern (Discovery vs. Transmission Separation)

**Concept:**
> The method of performing file and symbol discovery against **unobfuscated** source text to identify relevant code regions, then applying identifier obfuscation **exclusively** to content transmitted to external AI systems, such that the semantic search uses real identifiers while the AI call receives only opaque tokens.

**Why likely novel:**
- Not disclosed in any of the 7 references
- US 12,566,889 (Acronis) obfuscates before transmission but does not address or distinguish the discovery phase
- CodeCipher has no file-discovery phase (embedding-level, not file-selection problem)
- None of the privacy-related references (Acronis, IBM, CodeCipher) address the functional decomposition of "discovery uses original identifiers / AI transmission uses obfuscated identifiers"
- This is a structurally essential method step — without it, the agent cannot locate relevant files (the failure mode that produced 100% empty patches in early Cloak runs)

**Source text:** WHITE_PAPER.md §9.3 ("The Context Paradox — A Discovery"); PROJECT_CLOAK.md §Discovery 1

**Inventorship documentation:** PROJECT_CLOAK.md Discovery 1 records the complete diagnosis chain:
symptom (100% empty patches on cloaked runs), root cause identification (file keyword extraction
on obfuscated text returned x_NNNN tokens, file search found zero matches), architectural decision
("we are hiding identifiers from the cloud AI, not from our own file system"), and fix (move
obfuscation after `locate_relevant_files()`). This sequence — observing the failure, diagnosing
the structural cause, formulating the architectural rule, directing the implementation fix — is the
record of Ryan Gurganious's conception of this invention. The AI tools implemented the fix under
that direction. Sole human inventorship is unambiguously documented here.

**Claim language candidate:**
> "executing file and symbol discovery against unobfuscated source text; identifying relevant code regions based on unobfuscated identifiers; applying identifier-level obfuscation to content of the identified regions only for the purpose of transmission to an external language model API; wherein the obfuscation is not applied during the discovery phase."

---

## NOVEL-02: Semantic Key — Local Word-Splitting + Syntactic Category Annotation

**Concept:**
> A method for providing functional semantic context to a cloud AI without exposing original identifier names, comprising: for each opaque token in the transmission region, generating a description by word-boundary-splitting the original identifier string (underscore and camelCase boundaries) and annotating the description with the identifier's syntactic category (function, class, variable, argument, attribute); assembling these descriptions into a functional glossary attached to the AI prompt; wherein the glossary is computed locally from an identifier map that never leaves the local device.

**Why likely novel:**
- Not disclosed in any of the 7 references
- Acronis and IBM obfuscate but provide no semantic context to the LLM about what the obfuscated tokens mean
- CodeCipher has no reverse-semantic mechanism (34% recovery rate demonstrates semantic blindness)
- The specific mechanism — word-split + syntactic category + local computation from the SymbolMap — is Determinex's invention (identified as the fix for "Semantic Blindness" failure mode in §9.5)
- The privacy guarantee is specific: real identifier names never appear in the transmitted key (only split word segments, which may appear in any English-language training corpus)

**Source text:** WHITE_PAPER.md §9.5 ("Semantic Key: Local Context Bridge"), PROJECT_CLOAK.md

---

## NOVEL-03: Compile-Gate Error Re-Obfuscation in Retry Loop

**Concept:**
> A method wherein, after an obfuscated code patch fails compilation in an isolated worktree: the compiler error messages (which contain real identifier names from the actual compiled code) are processed through the same AST obfuscation pipeline to replace any private identifiers with their x\_NNNN tokens before the error messages are injected into the retry prompt for the external AI.

**Why likely novel:**
- Not disclosed in any of the 7 references
- This is the specific mechanism preventing leakage in the retry path: the real code compiles in the worktree (so the compiler error contains real identifiers), but those errors must be re-obfuscated before being sent back to the cloud AI
- Described in CLAUDE.md: "compile errors are generated from real code (worktree), then re-obfuscated before being fed back to the Architect. The cloud AI sees `x_NNNN undefined on line 47` — never the real identifier. Zero leakage even in error messages."
- The insight that the retry-error path is a leakage vector (compiler errors contain real identifiers) and the specific solution (run the same obfuscation pipeline on the error text) is novel to this work

**Source text:** CLAUDE.md §Project Cloak, WHITE_PAPER.md §3.13, PROJECT_CLOAK.md §Discovery 6

**Spec gap resolved 2026-06-11:** PROJECT_CLOAK.md Discovery 6 now contains the full enabling
disclosure for this claim: threat model, root cause, fix procedure (IssueTextTransformer applied
to all compiler/test output before retry injection), scope (all error channels), and the
invariant statement. This is no longer an under-disclosed claim element.

---

## NOVEL-04: L2 Egress Filter — API Gateway Blocking Unobfuscated Cloud Calls

**Concept:**
> An API gateway component that, when a flag DETERMINEX\_REQUIRE\_CLOAK is set, intercepts outbound requests to external language model APIs and blocks any request where the source code content has not been processed through the obfuscation pipeline, ensuring that unobfuscated source code cannot reach cloud providers even if the orchestration layer fails to invoke obfuscation.

**Why likely novel:**
- Not disclosed in any of the 7 references
- The specific "enforce obfuscation at the API gateway layer, not only at the pipeline layer" is a defense-in-depth mechanism
- Analogous to HTTPS enforcement at the proxy layer — a well-known pattern in network security — but the application to LLM API calls with code-content obfuscation verification is novel in this context
- Implementation: `scripts/hive/safety_gate.py`

**Source text:** PROJECT_CLOAK.md (2026-06-10 additions section)

**Note for attorney:** This may be weaker as an independent claim but is strong as a dependent claim on NARROW-03. As a system claim element ("wherein the system further comprises an API gateway that blocks transmission when obfuscation is not active"), it adds practical value to the claim set.

---

## NOVEL-05: Zero-Leakage Audit Trail via Per-Instance JSONL + Full API Request Log

**Concept:**
> A verification method for AST-aware code obfuscation comprising: logging all outbound API requests and responses to per-instance JSONL audit files; after a run completes, scanning all logged API request payloads for the presence of any string from the original identifier set (using the same SymbolMap generated during obfuscation); and producing a cryptographic attestation that zero original identifiers appeared in any transmitted API request.

**Why likely novel:**
- Not disclosed in any of the 7 references
- Acronis and IBM obfuscate but provide no post-hoc audit mechanism
- The ability to produce a verifiable "zero-leakage" attestation from a full API request log (enabled by `DETERMINEX_CLOAK_AUDIT=1`) is a novel claim element with enterprise/compliance value
- The audit artifact (cloak\_map + full API logs + scan result) constitutes a reproducible privacy proof

**Source text:** WHITE_PAPER.md §9.7, PROJECT_CLOAK.md (AuditLogger component)

---

## NOVEL-06: Atomic Workspace Write with fsync Before Compiler Invocation

**Concept:**
> A method for eliminating OS write-cache race conditions in AI-generated code validation comprising: after writing an AI-generated code modification to disk, calling `os.fsync()` to block until the OS confirms physical write completion before invoking the compiler, eliminating the failure mode where the compiler reads a partially-written or empty file from the page cache.

**Why likely novel:**
- Not disclosed in any of the 7 references
- This is a specific operating-system-level reliability mechanism for the Compiler Oracle
- The failure mode (Python `file.write()` returns before data is durable; compiler reads empty file; `py_compile` accepts empty file → false positive) is a production-discovered invariant
- The fix (`os.fsync()` before compiler invocation in all training-eligible paths) is a specific, non-obvious engineering solution

**Source text:** WHITE_PAPER.md §3.9 ("OS Write-Cache Race Conditions (Issue #20)")

**Note for attorney:** This is likely best as a dependent claim or implementation detail in the specification rather than an independent claim. The underlying concept of fsync-before-read exists in database literature. But the specific application to LLM-generated code compilation as a correctness invariant in training data generation may be novel.

---

## NOVEL-07: Three-Layer Secure Deployment of Trained Latent Bridge Artifact

**Concept (corrected 2026-06-11 from artifact inspection):**
> A method for secure deployment of a trained inter-model latent bridge comprising three independent
> security layers applied in sequence: (1) enforcing read-only filesystem permissions on the
> serialized artifact before loading; (2) invoking `torch.load(..., weights_only=True)` to
> prevent execution of arbitrary Python code embedded in pickle-format serialization; (3)
> computing a SHA256 digest over all weight tensors in deterministic sorted-key order —
> excluding the embedded hash field itself to avoid the self-referential bootstrap problem —
> and comparing against the reference hash embedded in the artifact; raising a fatal error and
> refusing use of the artifact on any mismatch.

**Correction from prior description:**
The WHITE_PAPER.md §3.4 states "SHA256 verified against raw file bytes before `torch.load()`."
This is inaccurate. The actual implementation (`scripts/determinex_rosetta.py` — inspected 2026-06-11):
- `_enforce_readonly()` runs first (chmod before any load operation)
- `torch.load(..., weights_only=True)` runs SECOND — the `weights_only=True` flag is the
  pickle RCE protection (PyTorch blocks arbitrary code execution when this flag is set)
- SHA256 via `_compute_weights_sha256()` runs THIRD — over tensor values, not raw bytes,
  which correctly excludes the self-referential `sha256` key
- Integrity verified on rosetta_v1.pt: SHA256 PASS `7589dd...` (2026-06-11)

**Verification files (can be pulled and verified immediately):**
- `T:/determinex-models/rosetta_v1.pt` — the sealed production artifact
- `scripts/determinex_rosetta.py` lines 486–629 — `_compute_weights_sha256()`, `_verify_sha256()`, `seal_rosetta()`, `RosettaStone.load()`
- Run: `python3 -c "import sys; sys.path.insert(0,'scripts'); from determinex_rosetta import _compute_weights_sha256, _verify_sha256; import torch; ckpt=torch.load('T:/determinex-models/rosetta_v1.pt',map_location='cpu',weights_only=False); print(_compute_weights_sha256(ckpt))"`
- Expected: `7589dd55512c9333f370a483ff8fcb60297ca50a44be1fb7057a3d54805a1eab`

**Why likely novel:**
- Not disclosed in any of the 7 references
- The specific combination: read-only enforcement + `weights_only=True` for RCE protection +
  tensor-value SHA256 with self-referential key exclusion is a non-obvious three-layer defense
- The self-referential key exclusion (`if key == "sha256": continue` in the hash computation)
  is a specific engineering solution to the bootstrap problem: a hash stored IN the file being
  hashed would always produce a different result unless excluded
- Motivated by the known pickle RCE attack vector and by production deployment on consumer hardware
  where artifact integrity cannot be assumed

**Source text:** `scripts/determinex_rosetta.py` §_compute_weights_sha256, §_verify_sha256, §RosettaStone.load (lines 486–629)

**Note for attorney:** Likely best as a dependent security claim or system claim element.
The general concept of "hash before use" exists in software security. The specific three-layer
combination applied to ML model artifacts with self-referential hash exclusion may be novel
in the ML deployment context. The previous NOVEL-07 description (raw-file-bytes hash before load)
was inaccurate — the correct description above reflects the actual implementation.

---

## NOVEL-08: DAG-Driven LoRA Routing with Per-Task-Vector Compile-Pass-Rate Registry

**Concept (Phase 3 — not yet built):**
> A system for dynamic language model adapter selection comprising: a task-type vocabulary declared in a DAG (directed acyclic graph) step manifest; a registry storing, per adapter, per task-type, the compile-pass rate measured on micro-evaluation probes for that task type; and a routing component that selects, for each DAG step, the adapter with the highest compile-pass rate for the declared task type of that step.

**Why likely novel:**
- Not disclosed in any of the 7 references
- Dynamic LoRA selection exists (vLLM multi-LoRA feature); the specific mechanism of compile-pass-rate as the routing signal is novel
- The DAG task\_vector field as the routing key is specific to this architecture
- Published in WHITE_PAPER.md §13.3 as a design record: "published here as a formal design record predating any subsequent independent implementation"

**Source text:** WHITE_PAPER.md §13.3

**Note for attorney:** This is a Phase 3 feature (not yet implemented). The WHITE_PAPER.md establishes prior disclosure. Attorney should evaluate whether publishing the design in the white paper protects against third-party patents or whether a provisional is needed to establish a priority date before a third party independently implements and files.

---

---

## NOVEL-09: Bidirectional IP Sovereignty Architecture (Cloak Out + Provenance In)

**Concept:**
> A combined system for IP sovereignty in AI-assisted software development comprising: (a) an outbound obfuscation component that replaces private identifier tokens with opaque surrogates before transmission to external AI systems; and (b) an inbound attribution component that detects when AI-generated output substantially reproduces registered source material and generates attribution records — wherein both components operate on the same generation pipeline, such that the system simultaneously prevents proprietary information from leaving and documents provenance of incoming influence.

**Why likely novel:**
- The combination of outbound obfuscation (Cloak) + inbound attribution tracking (provenance sidecar) operating on the same pipeline is not disclosed in any of the 7 references
- US 12,566,889 (Acronis) and US 20250086310 (IBM) address only outbound obfuscation — no inbound provenance tracking
- The specific license-tier-aware policy (permissive OSS → attribution tag only; non-permissive → alert) implemented in the inbound component is novel
- Append-only dual audit trail (copyright audit log + attribution log) enables simultaneous verification of both "nothing leaked out" and "all influences documented in"
- The filtered-bigram Jaccard comparison for code (stopword removal of programming keywords) is an engineering choice distinguishing from naive document-similarity approaches applied to prose

**Implementation date:** 2026-06-10
**Implementation files:**
- `scripts/determinex_copyright_guard.py` — combined guard (outbound: `CopyrightGuard._works`; inbound: `CopyrightGuard._references`)
- `scripts/hive/executor.py` — fire-and-forget sidecar wiring (observe mode)
- `scripts/determinex_programbench_agent.py` — fire-and-forget sidecar wiring (observe mode)
- `corpus/references/` — seed reference corpus (8 sources: 2 OSS, 4 academic, 2 patent)

**Source text:** CLAUDE.md §Project Cloak; `scripts/determinex_copyright_guard.py` module docstring; `docs/SAFETY.md` §Copyright Displacement Guard + Provenance Sidecar

**Note for attorney:** The individual components (outbound obfuscation, inbound similarity detection) exist separately in prior art. The novel element is the bidirectional integration on the same pipeline with a unified IP sovereignty policy. Attorney should evaluate whether the combination claim is patentable as a system or method claim given the individual components exist.

---

## NOVEL-10: Replay-Verification Ingestion Gate (Never-Trust-Submitted-Verdicts)

**Concept:** `[NEW — DETERMINEX_NODE.md §5 / §9; updated owner verdict 2026-06-11]`
> A method for anti-poisoning ingestion of externally submitted compiler-verified training
> pairs comprising: (a) receiving a submission asserting a before/after code pair and a
> claimed compiler verdict (passed/total/exit codes); (b) executing the `before` artifact
> in a sealed, network-isolated container — if it COMPILES when it was claimed to fail,
> the pair is rejected as unverifiable; (c) applying the submitted fix, compiling and running
> the `after` artifact against the submitted test corpus — either the inline `test_surface`
> content or, where the submission includes a `test_ref` (public harness identifier and
> version hash), the node's own pinned mirror of that harness at the specified version
> (submitted test content ignored for execution) — exit codes and pass/total counts must
> match the submitted verdict exactly; (d) rejecting and reason-code-logging any pair whose
> recomputed verdict diverges from the submitted verdict; (e) flagging the submitting client
> identifier in the provenance record on any mismatch.

**Why likely novel:**
- No reference in the 7-reference prior art set addresses ingestion of externally submitted
  training pairs at all (all 7 references are local-training or obfuscation systems)
- The specific bidirectional compile check (before must FAIL as claimed; after must PASS as
  claimed) is a structural novelty: it makes a false-verdict injection attack require
  submitting actually-working code, which is definitionally lower-toxicity signal
- The result is a mathematical property, not just a heuristic: a pair that passes replay
  verification is a genuine compiler-validated (error → fix) pair regardless of submitter
  intent; a pair that fails is either genuinely wrong or deliberately fabricated, and both
  are rejected without requiring semantic analysis of intent
- The "replay converts poisoning attacks into working-code submission" inversion is the core
  claim: it does not detect bad actors, it removes the incentive structure for bad actors

**Prior art differentiation:**
- Federated learning literature: aggregation of gradients or model updates, not verified
  (error → fix) pairs; no replay execution step
- RLHF and human-feedback pipelines: human rater trust model, not compiler verification
- SWE-bench / ProgramBench: evaluation harnesses, not ingestion gates for external
  submissions into a training corpus
- Determinex local compile-gate (CLAUDE.md): same mechanism applied to LOCAL generation;
  the novel element here is applying it to EXTERNAL submissions from untrusted clients

**Source text:** `docs/papers/DETERMINEX_NODE.md` §3 (schema), §5 §(3) (replay detail),
§6 §3 (test-surface gaming defense), §9 N-10

**Note for attorney:** This is likely the strongest novel claim in the Node family. It is
entirely design-only as of 2026-06-11 (v0 build is post-announce). Include in provisional
as written-description material to establish priority date. Closely related to NOVEL-06
(local compile-gate) — attorney should evaluate whether a single method claim can cover
both local and remote-submission applications or whether separate independent claims
are preferable.

---

## NOVEL-11: Corpus-Release Gating by Frozen-Benchmark Regression Test

**Concept:** `[NEW — DETERMINEX_NODE.md §6 §2 / §9]`
> A method for corpus quality assurance comprising: maintaining a frozen internal benchmark
> set that is never updated during an active training campaign; before publishing any corpus
> release to training, evaluating the candidate corpus against the frozen benchmark;
> blocking any corpus release that produces a measurable regression against the frozen
> benchmark baseline (defined as a reduction in pass rate on the frozen benchmark suite);
> and recording the before/after frozen-benchmark scores in the publicly rendered corpus
> release notes as a machine-verifiable quality attestation.

**Why likely novel:**
- Applying compiler-oracle discipline to corpus releases (not just individual pairs) is
  novel: the frozen benchmark acts as an oracle that can detect corpus drift, style
  degeneration, or subtle poisoning even when individual pairs each pass replay verification
- The "never update the frozen benchmark during an active campaign" invariant is a
  structural guarantee preventing the benchmark from being gamed by corpus composition
- No reference in the 7-reference set addresses corpus-level quality gating
- The public before/after score in corpus release notes extends the transparency ledger
  concept (NOVEL-05 audit trail) to corpus releases, not just individual pairs

**Source text:** `docs/papers/DETERMINEX_NODE.md` §6 §2 ("slow corpus skew" defense), §8
(transparency ledger), §9 N-11

**Note for attorney:** Design-only as of 2026-06-11. Closely related to the Eval-in-Loop
architecture (NOVEL-06) — this extends the verified_locked gating concept from individual
generation steps to corpus releases. May be claimed as a dependent claim on the Eval-in-Loop
family or as an independent system claim covering the corpus-release quality gate.

---

## NOVEL-12: Per-Submission Cloak-Namespace Re-Mapping at Intake

**Concept:** `[NEW — DETERMINEX_NODE.md §6 §4 / §9]`
> A method for preventing adversarial token-space collision in federated Cloaked-pair
> ingestion comprising: at intake, generating a fresh, submission-specific opaque-token
> namespace for each submitted pair (re-assigning all x_NNNN tokens in the submitted
> `before`/`after`/`test_surface` fields to a new, non-overlapping namespace); wherein
> the client's original x_NNNN assignments are never preserved into the shared corpus,
> preventing any adversarial relationship between token identities across clients; and
> wherein the re-mapping is applied before deduplication, replay verification, and
> corpus ingestion.

**Why likely novel:**
- The attack vector being addressed — adversarial x_NNNN patterns designed to collide
  with other clients' obfuscated vocabularies in a shared corpus — is specific to the
  Cloaked-pair format and has no analog in federated learning literature (which transmits
  gradients, not symbolic code representations)
- The fix (per-submission namespace regeneration at intake) is a specific structural
  mechanism not disclosed in any of the 7 references
- The property it establishes — token identities in the shared corpus have no semantic
  relationship to any individual client's local token assignments — is a privacy-amplifying
  guarantee on top of the existing Cloak privacy properties

**Source text:** `docs/papers/DETERMINEX_NODE.md` §6 §4, §9 N-12

**Note for attorney:** Design-only as of 2026-06-11. Closely related to the Project Cloak
family (NOVEL-01 through NOVEL-05). May be strongest as a dependent claim on a Cloak
system claim, or as an independent claim specifically addressing federated ingestion of
obfuscated training data.

---

## NOVEL-13: Client-Side Verified-Locked Gating of OTA Weight Deltas (Symmetric Trust Boundary)

**Concept:** `[PRIOR mechanism, NEW framing — DETERMINEX_NODE.md §7 / §9]`
> A method for secure receipt of over-the-air model weight updates in an AI development
> system comprising: (a) verifying the cryptographic signature of an inbound weight delta
> against a trusted organization key before any installation; (b) applying the weight
> delta to a staging environment; (c) executing a `verified_locked` evaluation gate on
> the updated model — identical to the gate applied to locally trained models — before
> allowing the updated weights to go live; (d) blocking installation and surfacing an
> error if the evaluation gate fails; wherein the client-side gate applies the same
> compiler-oracle quality standard to both locally trained weights and remotely delivered
> weights, creating a symmetric trust boundary in both directions of the fleet signal loop.

**Why likely novel:**
- The symmetric trust boundary framing is the novel element: the node applies replay
  verification to INBOUND pairs (§5 §(3)); the client applies verified_locked gating to
  INBOUND weight deltas (§7). The same structural principle (never trust a stated verdict,
  verify with the compiler oracle) applies in both directions.
- No reference in the 7-reference set addresses client-side gating of OTA weight updates
- The "treat OTA delta exactly like a local retrain product" equivalence principle means
  the fleet does not distinguish between "I trained this locally" and "the Node sent this"
  at the quality verification layer — only the signature verification differs

**Prior art differentiation:**
- Standard OTA update mechanisms (mobile, IoT): signature verification + install; no
  behavioral quality gate before installation
- Model serving updates (vLLM, Ollama hot-swap): atomic swap, no compiler-oracle validation
- The novel element is the GATE, not the signature or the hot-swap mechanism

**Source text:** `docs/papers/DETERMINEX_NODE.md` §7, §9 N-13

**Note for attorney:** The underlying verified_locked gating mechanism already exists in
Determinex (NOVEL-06, Eval-in-Loop architecture). The novel claim here is its application to
INBOUND OTA deltas as a symmetric guarantee. May be best as a dependent claim on the
Eval-in-Loop family, extended to cover OTA receipt. If claimed independently, draft at the
level of "applying the same compiler-oracle quality gate to both locally generated and
remotely delivered model updates."

---

## NOVEL-14: Tier-Gated Corpus Promotion (NEEDS TRIAGE)

**Concept:** `[NEW — DETERMINEX_NODE.md §4; owner verdict 2026-06-11]`
> A method for regulated cross-tier migration of training signal in a tiered corpus
> management system comprising: (a) storing submitted training pairs in sealed, tier-specific
> corpus cartridges (school, enterprise, community) with no automatic cross-tier migration;
> (b) requiring a multi-condition gate for any promotion of sealed-tier pairs into a shared
> corpus — including applicable regulatory compliance review (e.g., COPPA/FERPA for
> school-tier), data-use agreement amendment, data-specific scrubbing layer verification,
> differential privacy aggregation confirmation, and a logged authorization record in an
> append-only transparency ledger; (c) blocking any cross-tier migration absent all gate
> conditions being positively satisfied and recorded; wherein no corpus release may include
> promoted sealed-tier pairs unless all gate conditions are verified and the transparency
> ledger reflects the sign-off.

**Why likely novel (needs triage):**
- The multi-condition gate (regulatory + agreement + scrub + DP + ledger) as a required
  pipeline stage before cross-tier corpus promotion is not disclosed in any of the
  7-reference prior art set
- Standard federated learning literature does not address consent-tier migration; DP papers
  address anonymization but not cross-tier authorization gates
- This is a compliance automation claim: the structural novelty is the gate as a required
  pipeline element, not the regulatory requirements themselves
- The transparency ledger sign-off as a hard gate condition (not a post-hoc audit) is the
  distinguishing implementation detail
- Needs further triage: individual requirements (COPPA/FERPA, DP aggregation) are
  well-known; novelty argument must rest on the automated structural gate combination

**Prior art differentiation:**
- Federated learning literature: deals with gradient aggregation, not consent-tier corpus
  management
- GDPR/FERPA compliance tools: administrative processes, not automated software pipeline gates
- The combination — tiered sealed storage + multi-condition promotion gate + ledger sign-off
  as a required software pipeline element — has no prior art anticipation as a combined system

**Source text:** `docs/papers/DETERMINEX_NODE.md` §4 (school cartridge, gated promotion
pathway), §8 (transparency ledger sign-off)

**Note for attorney:** NEEDS TRIAGE — flag as candidate claim for evaluation. May be
strongest as a dependent claim on NOVEL-10 / NOVEL-11 (extending the verified-gate concept
to corpus promotion decisions), or as a separate system claim covering the tier-management
architecture. Regulatory requirements (COPPA/FERPA) should appear as embodiment details, not
as required claim elements, to keep claim scope broad. Design-only as of 2026-06-11; same
treatment as NOVEL-10–13 (include in provisional as written-description material).

---

*All items in this file are risk assessments for attorney/inventor review. Not legal opinions. Attorney must conduct full prior art search before relying on these assessments.*
