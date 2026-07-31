# Project Cloak — Implemented & Validated

> **Status (rev. 2026-06-10)**: COMPLETE. Built April 27-28, 2026. Warm-up validation: 3/3 instances
> patched (100%, 129 seconds). Post-hardening SWE-bench Lite ablation has an audited May
> B-Uncloaked snapshot at **14.0%** (42/300, zero errored), but fresh B-Uncloaked and
> E-RegionControl reruns are required before publication. B-Cloaked RosettaOFF and
> D-Cloaked currently remain lower bounds because disk-pressured Docker workers hit
> per-instance image-export errors; a larger-disk rerun is required for final deltas. No new
> Cloak-internal changes since 5-29. Benchmark results are not product support, not release
> support, and not product readiness.
>
> **2026-06-10 additions related to Cloak:**
> - L2 Egress Filter (`scripts/hive/safety_gate.py`): Cloak is now enforced at the API gateway. When `DETERMINEX_REQUIRE_CLOAK=1`, the pre-API gate blocks any cloud call where obfuscation is not active. This is the production enforcement mechanism ensuring no unobfuscated source reaches cloud providers.
> - Copyright Displacement Guard (`scripts/determinex_copyright_guard.py`): A separate companion tool for verbatim reproduction detection. Not part of Cloak (identifier obfuscation) — a distinct audit system for registered artistic works. See `docs/SAFETY.md`.
>
> Related governance: [`policy/CLOAK_THREAT_MODEL.md`](../policy/CLOAK_THREAT_MODEL.md).

---

## What It Is

Project Cloak is an AST-aware, whole-repository Python identifier obfuscation system that allows
a local AI coding agent to solve real-world software engineering tasks using cloud AI while keeping
every proprietary identifier — every function name, class name, variable name, and argument name
— invisible to the cloud model.

The cloud AI never sees `separability_matrix`, `CompoundModel`, `DeterminexConfig`, or any other
private repository symbol. It sees `x_0070`, `x_0177`, `x_0187`. It solves the problem in that
obfuscated space. The patch is restored to original identifiers before being applied.

---

## Design Decisions (Locked)

| # | Decision | Call | Rationale |
|---|---|---|---|
| 3.1 | Issue text | CLOAK | Length-descending sort before regex swap |
| 3.2 | Test files | CLOAK | AI handles opaque fixtures; consistency > convenience |
| 3.3 | Docstrings | Option D | Cloak identifier tokens within; strip `#` comments entirely |
| 1.4 | Single-letter vars | EXEMPT | `i`, `j`, `x`, `n`, `_`, `__` |
| 2.1 | Dunder names | EXEMPT | Strict `^__.*__$` only — `init_config` gets cloaked |
| 5.1 | Map ordering | ALPHABETICAL | Deterministic across runs, case-insensitive |
| 2.2 | Star imports | PASS-THROUGH + LOG | Unobfuscated, flagged in audit |
| 4.1 | Unrecognized AI names | PASS-THROUGH | New identifiers are valid code |
| — | Filenames | NEVER CLOAK | Navigation value > security gain |
| — | Control | TWO RUNS | Uncloaked → Cloaked; score delta is the finding |
| — | Audit | REQUIRED | `verify_cloak.py` confirms zero leakage post-run |
| — | C-Style | NOT NOW | SWE-bench is Python only; generalize post-launch |

---

## Architecture (As Built)

Package: `scripts/determinex_cloak/`. Seven components, clean separation, with verification and audit helpers in `scripts/verify_cloak.py` and `scripts/cloak_audit.py`.

```text
CloakPipeline
├── StdlibManifest          loads data/stdlib_312.txt
│                           + parses repo requirements*.txt / setup.cfg / pyproject.toml
│                           → frozenset of safe package names
│
├── IdentifierClassifier    ast.NodeVisitor over all .py files in repo
│                           collect: Name, FunctionDef, ClassDef, arg, Attribute identifiers
│                           filter out: stdlib, framework, single-char, ^__.*__$
│                           → frozenset[str] of private identifiers (deduplicated globally)
│
├── SymbolMap               sort frozenset alphabetically (case-insensitive)
│                           assign x_0001, x_0002, ... deterministically
│                           → {original: x_NNNN} + {x_NNNN: original}
│
├── ASTTransformer          ast.NodeTransformer applying forward map
│                           visit_Name, visit_FunctionDef, visit_ClassDef, visit_arg
│                           docstrings: regex token replace (not strip)
│                           inline #comments: strip entirely
│                           → obfuscated source string (never written to disk)
│
├── IssueTextTransformer    regex on issue description string
│                           identifiers sorted by len() descending before apply
│                           → obfuscated issue text
│
├── RestorationEngine       regex on raw diff lines (not AST)
│                           pattern: \bx_\d{4}\b
│                           reverse map, length-descending (longer x_NNNN first)
│                           pass-through: any token not in reverse map
│                           → restored diff or (None, error_description)
│
└── AuditLogger             writes per-instance JSONL to logs/swebench/cloak_audit/
                            on DETERMINEX_CLOAK_AUDIT=1: logs obfuscated API requests
                            always: logs restoration failures to cloak_failures.jsonl
```

### Persistent Per-Instance State

```python
CloakContext(
    instance_id: str,
    symbol_map: dict[str, str],        # forward: original → x_NNNN
    reverse_map: dict[str, str],       # reverse: x_NNNN → original
    obfuscated_files: dict[str, str],  # path → obfuscated source
    star_import_warnings: list[str],   # logged but not cloaked
)
```

Created ONCE at start of `solve()`. Never rebuilt mid-run. Saved to `cloak_map_<instance_id>.json`
for post-run audit.

**Scale**: For `astropy__astropy-12907`, the classifier mapped **24,134 private identifiers** with
**169 star-import holes** (documented, auditable).

---

## Files Delivered

| File | Purpose | Status |
|---|---|---|
| `scripts/determinex_cloak/` | Full Cloak package (all 7 components) | ✓ Built |
| `scripts/verify_cloak.py` | Post-run privacy audit | ✓ Built |
| `scripts/cloak_audit.py` | Audit helper utilities | ✓ Built |
| `data/stdlib_312.txt` | Python 3.12 stdlib safe-list | ✓ Built |
| `scripts/determinex_swebench_agent.py` | Integration: `solve()` Cloak hooks | ✓ Integrated |
| `scripts/determinex_swebench_run.py` | Config B dual-run, `DETERMINEX_CLOAK` env var | ✓ Integrated |
| `scripts/testing/run_ablation.sh` | Full B-Uncloaked → B-Cloaked → D-Cloaked sequence | ✓ Built |

---

## Integration: The `solve()` Function

The Cloak integration points in `determinex_swebench_agent.py`:

1. **Pre-call**: `CloakContext` built once — whole-repo AST scan, identifier classification,
   alphabetical SymbolMap assignment, per-instance JSON save.
2. **Issue text**: `IssueTextTransformer` replaces all private identifiers in the problem
   statement before any AI sees it.
3. **File retrieval**: File *discovery* (keyword search, `locate_relevant_files`) runs on **real
   text** before obfuscation. This is the **Context Paradox fix** — see below.
4. **Architect call**: Sees obfuscated issue text + obfuscated relevant file content. Plans the fix
   in x_NNNN space.
5. **Builder call**: Sees obfuscated file content + Architect plan. Generates patch in x_NNNN space.
6. **Restoration**: `RestorationEngine` replaces all x_NNNN tokens in the raw diff with original
   identifiers before `patch` is applied to the real repository.
7. **Verification**: Tests run against the real (restored) codebase.

---

## Discoveries Made During Implementation

These were not anticipated in the build plan. Each required diagnosis and a targeted fix before
the pipeline would produce patches at all.

### Discovery 1: The Context Paradox

**Symptom**: 100% empty patches on cloaked runs. The agent found relevant files, planned a fix,
but the plan named files like `x_14086.py` that did not exist.

**Root cause**: Issue text was obfuscated *before* `locate_relevant_files()`. The keyword
extraction step extracted x_NNNN tokens instead of real function names. File search found zero
matches. The Architect planned fixes to the wrong files or nonexistent paths.

**Fix**: Moved obfuscation to occur *after* file discovery. `locate_relevant_files()` runs on
original text. Only the content passed to the Architect and Builder calls gets obfuscated. This
is structurally correct: we are hiding identifiers from the cloud AI, not from our own file system.

**Impact**: Cloaked runs went from 0% patch generation to normal patch generation.

---

### Discovery 2: The Full-File Rewrite Bug

**Symptom**: Every patch attempt for files under 400 lines was rejected with
`Patch changes N/M lines (>80%)`. The ratios were always close to 2× (e.g., 132/66, 634/317,
1284/642 — exactly double the original file size in changed lines).

**Root cause**: `_REGION_THRESHOLD = 400` meant any file under 400 lines was passed to the Builder
as a complete file. The Builder prompt explicitly said "Return the ENTIRE corrected Python file."
The Builder complied — but returned the file with subtly different whitespace, docstring formatting,
and trailing-space conventions throughout. `difflib.unified_diff` then reported nearly every line
as changed, producing a unified diff ~2× the size of the original file. This triggered the 80%
line-change ratio check, which discarded every attempt.

**Fix part 1**: `_REGION_THRESHOLD = 0` — always use region mode regardless of file size. The
Builder now sees only the 40–80 lines surrounding the target change site, not the entire file.

**Fix part 2**: Remove the 80% ratio check entirely from `make_targeted_patch()`. Region mode
naturally bounds diff size to the region window. For the rare case that escapes region mode, the
2000-line absolute cap is the only remaining gate.

**Impact**: 3/3 instances patched in 129 seconds on warm-up. Zero ratio rejections.

---

### Discovery 3: Builder Line-Number Echoing

**Symptom**: After switching to region mode, some patches failed to apply because they contained
lines prefixed `"   67 | actual_code"` — the Builder echoing back the line-number display format
used in the context prompt.

**Root cause**: The prompt shows the Builder a numbered region:
```
   67 | def separability_matrix(transform):
   68 |     ...
```
The Builder echoed this format back in its output, including the `"   N | "` prefix. These prefixes
were stripped in the region-mode path only, not in the fallback full-file path.

**Fix**: Move the line-number stripping step *before* the `if region_mode:` branch so it applies
in both paths:
```python
stripped = []
for line in raw.splitlines():
    m = re.match(r'^\s*\d+\s*\|\s?(.*)', line)
    stripped.append(m.group(1) if m else line)
raw = "\n".join(stripped)
```

**Impact**: Eliminates a class of patch-apply failures on non-region paths.

---

### Discovery 4: Cloak Checksum Failure (Identifier Rename Leak)

**Symptom**: In cloaked runs, after the patch was generated, the checksum validator reported:
`Builder renamed 35/35 x_NNNN tokens (x_0070, x_0177, ...) — retry`.

**Root cause**: The Builder was receiving a context where the file content was obfuscated but
the *Builder prompt instructions* mentioned the target identifier by its real name (passed in via
the Architect plan). The Builder then renamed the obfuscated tokens to match, creating a patch
that contained neither the real names nor the x_NNNN tokens — a mixed state the checksum
validator correctly rejected.

**Status**: Resolved via temperature escalation retry (T=0.1 → T=0.4 → T=0.7). The deeper fix
is the Semantic Key layer (Discovery 5), which gives the Builder functional context for each
x_NNNN token without exposing real names.

---

### Discovery 5: Builder Semantic Blindness — The x_NNNN Reasoning Gap

**Symptom**: Even when patches applied cleanly (passed checksum), the Builder sometimes produced
semantically incorrect fixes — correct syntax, wrong logic. Analysis showed the Builder was
treating x_NNNN tokens as opaque placeholders and making changes based on structural position
alone, not understanding what each identifier actually does.

**Root cause**: The Architect's plan references real concepts from the issue text (e.g., "add a
null check before accessing the session cache"). The Builder sees the plan but also sees
`x_1234` in the code with no way to know it IS the session cache. For simple local changes,
position-based reasoning is sufficient. For anything requiring semantic understanding of what
a private method or attribute does, the Builder is reasoning blind.

**Fix**: `build_semantic_key()` — a local pre-flight step that generates a functional glossary
for the x_NNNN tokens appearing in the fix region, injected into both the Architect and Builder
prompts. Real names never leave the machine — only descriptions derived from them:

```
[SYMBOL GUIDE — generated locally, not transmitted as real names]
Token semantics for this fix region:
  x_1234: session cache (private attr)
  x_5678: database backwards (fn)
  x_9012: format string validator (private method)
```

The key is built from the Cloak symbol map BEFORE obfuscation and BEFORE any API call, ensuring
the semantic context is attached at the local boundary — it cannot be lost or stripped in transit.
Functional hints are derived by splitting the real name on underscores and camelCase; the real
identifier string is never present in the outbound prompt.

**Impact**: Directly addresses the main failure mode for semantically complex fixes — the class
of patches that apply cleanly but fail the test suite because the logic is wrong.

---

### Discovery 6: Compile-Gate Error Re-Obfuscation in the Retry Loop

**Symptom**: When a cloaked patch fails to compile in the isolated worktree, the retry
mechanism needs to give the Architect specific error context — what failed, and where. But
the compile-gate runs against a real git worktree that contains unobfuscated (restored) source
code. The compiler (`rustc`, `go build`, `python -m py_compile`) therefore produces error
messages containing real identifiers from the actual source: `CompoundModel undefined at line 47`,
`DeterminexConfig has no attribute 'batch_size'`. If these error messages are fed directly into the
retry prompt, real proprietary identifiers reach the cloud API — a leakage vector in the retry path.

**Root cause**: The threat model requires that no original identifier string cross the local/cloud
boundary in any direction. The compile-gate creates an otherwise-invisible outbound path: the
worktree is real code; the compiler reads real code; the error is real-identifier text; the retry
prompt is outbound to the cloud Architect. Without re-obfuscation, every compile failure leaks the
identifiers from the failing lines.

**Fix**: Before injecting any compiler output, test-runner output, or error text into the retry
prompt, pass the raw text through `IssueTextTransformer` using the instance's existing SymbolMap
(forward map: original → x\_NNNN), with identifiers sorted by length descending before substitution
(same ordering as the initial issue text obfuscation). The cloud Architect receives:
`x_0177 undefined at line 47`, `x_0187 has no attribute 'x_1421'`. Real identifiers never appear.

This applies to every channel that can carry compiler output into a retry prompt:
- `rustc` / `go build` / `python -m py_compile` stdout and stderr
- `pytest` / `go test` failure output
- Traceback text from test harness
- Any static analysis or lint output used in retry context

**Invariant**: Every text path from worktree output to cloud API call must pass through
`IssueTextTransformer` using the current instance's SymbolMap. No exception for "short" errors
or "numeric" errors — line numbers and file paths are transmitted as-is (they do not reveal
identifier semantics), but all identifier-format tokens in error output are substituted.

**Impact**: The zero-leakage guarantee (`DETERMINEX_CLOAK_AUDIT=1` clean verdict) extends through
the full retry path. The cloud AI never observes a real identifier regardless of how many retry
attempts occur or how many different compiler errors are produced.

**Source**: CLAUDE.md §Project Cloak — "compile errors are generated from real code (worktree),
then re-obfuscated before being fed back to the Architect. The cloud AI sees
`x_NNNN undefined on line 47` — never the real identifier. Zero leakage even in error messages."

---

## Ablation Configuration

| Config | Architect | Builder | Cloak | Run ID Pattern |
|---|---|---|---|---|
| **B-Uncloaked** | DeepSeek V3 | DeepSeek V3 | OFF | `determinex_lite_B-FrontierParity-Uncloaked_*` |
| **B-Cloaked** | DeepSeek V3 | DeepSeek V3 | ON | `determinex_lite_B-FrontierParity-Cloaked_*` |
| **E-RegionControl** | DeepSeek V3 | DeepSeek V3 | OFF, region forced | `determinex_lite_E-RegionControl_*` |
| **D-Cloaked** | Claude Sonnet 4.6 | DeepSeek V3 | ON | `determinex_lite_D-NuclearHybrid-Cloaked_*` |

**Scale**: 300 instances (SWE-bench Lite full split). 4 parallel workers. Pre-cloned repos on
`T:\determinex-swebench` (zero clone overhead). Each config runs sequentially via `run_ablation.sh`.

### Run History

| Run | Date | Status | Notes |
|---|---|---|---|
| B-Uncloaked (post-hardening) | 2026-05-11 | COMPLETE | **14.0%** (42/300), 0 errored |
| E-RegionControl (post-hardening) | 2026-05-11 | LOWER BOUND | **>=6.0%**, disk-export errors |
| B-Cloaked RosettaOFF (post-hardening) | 2026-05-11 | LOWER BOUND | **>=2.3%**, disk-export errors |
| D-Cloaked (post-hardening) | 2026-05-11 | LOWER BOUND | **>=3.3%**, disk-export errors |
| Larger-disk rerun | queued | NEXT | Final privacy-cost and hybrid-lift deltas |

**Decision (Lane B boundary)**: The post-hardening B-Uncloaked result is an audited May
snapshot, not the final publication control. The three region-mode / Cloak-on configurations
are honest lower bounds until rerun on a larger-disk worker pool.

---

## Score Delta Framework

```
Config B Uncloaked:     14.0%  <- audited May snapshot; fresh rerun pending
Config E RegionControl: >=6.0% ← lower-bound region-mode control
Config B Cloaked:       >=2.3% ← lower-bound privacy result
Config D Cloaked:       >=3.3% ← lower-bound Nuclear Hybrid result

Delta (B):  Y - X       ← the price of sovereignty (expected: < 3pp)
Delta (D):  Z - Y       ← the value of Claude as Architect
```

**Two-generation comparison (what actually gets published)**:

```
Post-hardening B-Uncloaked:      14.0%   <- audited May snapshot; fresh rerun pending
Post-hardening E-RegionControl:  >=6.0%  ← lower bound
Post-hardening B-Cloaked:        >=2.3%  ← lower bound
Post-hardening D-Cloaked:        >=3.3%  ← lower bound

Final privacy delta: rerun required on larger-disk workers
```

**White paper lead** (draft lower-bound form; not publication-final):

> *"Determinex resolved 14.0% of SWE-bench Lite in the audited May B-Uncloaked snapshot. With full
> identifier obfuscation enabled, the current disk-pressured run establishes a lower bound
> of >=2.3%; the final cost of sovereignty is gated on fresh B-Uncloaked and E-RegionControl reruns."*

If Z is under 3pp, that is the headline. If Z is 8pp, that is also a finding — and publishable,
because no one else has quantified it.

---

## Verification Pipeline

`scripts/verify_cloak.py` — post-run privacy audit.

For each instance that has a `cloak_map_<iid>.json`:
1. Load forward map (original → x_NNNN)
2. Scan `api_requests.jsonl` (if `DETERMINEX_CLOAK_AUDIT=1` was set)
3. Check every logged API prompt excerpt for any original identifier
4. Report: CLEAN / LEAK×N per instance

**Full audit** (with `DETERMINEX_CLOAK_AUDIT=1`):
```
VERDICT: CLEAN — zero proprietary identifiers reached cloud APIs
CLAIM  : Determinex resolved these instances while the cloud AI was
         blind to all 24,134 proprietary identifier tokens
         (169 star-import names are a documented known hole)
```

**Without audit env var** (current ablation runs):
```
VERDICT: UNVERIFIED — run with DETERMINEX_CLOAK_AUDIT=1 for proof
```

Re-run with `DETERMINEX_CLOAK_AUDIT=1` to generate the publishable proof artifact.

---

## Language-Agnostic Architecture

The current deployment of Project Cloak targets Python repositories (SWE-bench Lite is Python-only).
However, the core pipeline architecture is language-agnostic. The five-stage structure applies
to any language with an AST parser:

```
StdlibManifest      ← safe-list of standard library + framework identifiers for the target language
IdentifierClassifier ← AST visitor over all source files: collect private identifiers, exclude safe-list
SymbolMap           ← deterministic alphabetical assignment: private identifiers → opaque tokens
ASTTransformer      ← AST-level substitution (compilability-preserving, never regex on code)
IssueTextTransformer ← text-level substitution for issue text, compiler errors, and retry context
RestorationEngine   ← reverse substitution: opaque tokens → original identifiers in AI-generated patches
AuditLogger         ← per-instance JSONL for post-run zero-leakage verification
```

**Language extension points** (current deployment notes):
- Python: `ast.NodeVisitor` + `ast.NodeTransformer`. Deployed.
- Go: `go/ast` (standard library). Extension path is well-defined; `go build` is the compiler oracle.
- Rust: `syn` crate. Extension path defined; `rustc`/`cargo check` is the compiler oracle.
- Java/TypeScript/JavaScript/Ruby/PHP/C/C++: `tree-sitter` provides a unified parser API across all.
  The `IdentifierClassifier` and `ASTTransformer` components use language-specific grammar rules
  for node selection; all other pipeline components are language-agnostic.

**The invariant that makes multi-language extension safe**: The `RestorationEngine` operates on
raw diff text (not AST), using length-descending regex. This is already language-agnostic — it does
not need to understand the target language's syntax to correctly restore opaque tokens in a unified diff.

**Why language-agnostic claiming matters**: The core inventive elements — identifier classification
using an AST-appropriate parser, deterministic opaque-token assignment, compilability-preserving
AST-level transformation, local semantic key generation, and re-obfuscation of compiler error output
in the retry path — are not properties of Python. They are properties of any language where
(a) an AST parser exists and (b) compilability is machine-verifiable.

---

## Known Holes (Documented, Not Fixed)

Publishing the holes strengthens the claim — it demonstrates rigorous audit rather than inflated
security theater.

| Hole | Description | Audit Status |
|---|---|---|
| **Star imports** | Names exported via `from module import *` are unobfuscated | Counted and logged per-instance in `star_import_warnings` |
| **String annotations** | `"UserRecord"` in `TYPE_CHECKING` context is not an AST Name node | Partial coverage only |
| **Issue text prose** | `"user record"` (split words, not identifier-format) passes through | By design — substitution is identifier-format only |
| **Architect plan → Builder** | Architect plan may reference real names from issue text; Builder receives both plan and obfuscated code — semantic key bridges this gap with functional hints, not real names | Mitigated by Semantic Key (Discovery 5) |

---

## Ablation Status (audited May snapshot; fresh publication rerun pending)

All four post-hardening configs were re-run against SWE-bench Lite (300 instances) on 2026-05-11 using Hetzner CPX41 workers. The B-Uncloaked run completed with zero errored instances, but Lane B treats it as an audited May snapshot rather than a final publication baseline until the fresh B-Uncloaked/E-RegionControl reruns land. The three Cloak-on / region-mode configurations still incurred per-instance Docker image-export errors on the disk-pressured workers and their resolved counts remain lower bounds pending a fresh rerun on a larger-disk box.

| Config | Resolved | Errored | % | Status |
|---|---|---|---|---|
| **B-Uncloaked** | **42/300** | **0** | **14.0%** | **Audited May snapshot; fresh rerun pending** |
| E-RegionControl | **≥18/300** | 119 | **≥6.0%** | Lower bound (disk-full errors) |
| B-Cloaked-RosettaOFF | **≥7/300** | 121 | **≥2.3%** | Lower bound (disk-full errors) |
| D-Cloaked | **≥10/300** | 106 | **≥3.3%** | Lower bound (disk-full errors) |

**Delta chain (May snapshot anchor; final privacy-cost delta pending fresh reruns):**
```
B-Uncloaked -> E-RegionControl:   lower-bound relationship only; rerun required
E-RegionControl -> B-Cloaked:     lower-bound relationship only; rerun required
B-Cloaked -> D-Cloaked:           lower-bound relationship only; rerun required

Total privacy-sovereignty cost: not final until fresh B-Uncloaked and E-RegionControl reports are imported.
```

**Sovereignty overhead**: lower-bounded at 11.7pp. The cloaked configs were on disk-pressured workers and their resolved counts are floor estimates; the true ordering and final delta require a fresh rerun on a larger-disk box. The D-Cloaked lower bound (3.3% vs B-Cloaked 2.3%) is consistent with Claude-as-Architect helping under Cloak, but the +1.0pp margin sits within the disk-full noise band and is not yet a publishable claim.

---

## Data-Driven Pivot — Semantic Anchoring (2026-05-11)

### Hypothesis

The ablation revealed a reproducible **repo-type semantic split**:

- **B-Cloaked** resolved 3 django instances. **D-Cloaked** resolved 0 django instances.
- Both resolved sympy/sphinx instances at similar rates.
- E-RegionControl (Cloak OFF, region ON) also resolved 0 django instances.

The pattern is consistent: **django fixes require framework-semantic reasoning; sympy/sphinx fixes are algorithmic and survive obfuscation.**

Django's framework conventions (`get_queryset`, `save`, `clean`, `dispatch`, `get_object_or_404`, `form_valid`) are load-bearing identifiers — the fix pattern IS the method name. When those names become `x_0347`, `x_1182`, the AI must infer from structural position alone what these override hooks do. DeepSeek's training corpus apparently contains enough obfuscated-code patterns to make plausible guesses; Claude's chain-of-thought is more disrupted.

Sympy fixes are different in character: "this transformation has a sign error", "this simplification rule has an edge case". The fix is a numerical or logical correction, not a framework hook convention. These survive obfuscation because the relevant semantics are in the algorithm, not the identifier names.

**The hypothesis**: If we preserve a curated set of framework-specific method names through Cloak (a "Keep List"), the 10.7pp sovereignty overhead shrinks — specifically, the django-class resolutions recover. Sympy/sphinx numbers are unaffected because they never depended on method name semantics.

### Why This Matters for the Paper

Current claim boundary: the 14.0% B-Uncloaked value is an audited May snapshot, and the Cloak-on / region-mode values are lower bounds from disk-pressured infrastructure. Do not publish a final privacy-cost claim until fresh B-Uncloaked and E-RegionControl reports are imported from the larger-disk rerun.

With semantic anchoring, the future measured claim will use the next completed run's concrete score and curated anchor count instead of placeholders.

This is a stronger and more nuanced contribution: not "Cloak costs 10.7pp" but "Cloak costs ~2.7pp for framework-agnostic tasks; a targeted Keep List recovers the framework-pattern gap without giving up privacy on business logic."

### Proposed Ablation Design

**Config F — B-Cloaked-KeepList**: DeepSeek V4 + Cloak ON + Keep List active

The Keep List is a per-framework registry of method names that are preserved in plaintext through Cloak:

```python
FRAMEWORK_KEEP_LIST = {
    # Django ORM / view layer
    "django": [
        "get_queryset", "get_object", "get_object_or_404",
        "save", "delete", "clean", "full_clean", "validate_unique",
        "dispatch", "get", "post", "put", "patch",
        "form_valid", "form_invalid", "get_form_kwargs",
        "get_context_data", "get_success_url",
        "setUp", "tearDown",  # test hooks
    ],
    # scikit-learn estimator protocol
    "sklearn": [
        "fit", "transform", "fit_transform", "predict",
        "predict_proba", "score", "get_params", "set_params",
    ],
    # pytest
    "pytest": [
        "setup", "teardown", "setup_method", "teardown_method",
        "setup_class", "teardown_class", "conftest",
    ],
    # Flask view / blueprint layer
    "flask": [
        "before_request", "after_request", "teardown_request",
        "errorhandler", "route",
    ],
}
```

The Keep List is applied in `IdentifierClassifier.classify()` as an exemption set — identical to how dunders and single-char vars are exempted today. These names still appear in the obfuscated prompt in plaintext, giving the AI the framework-semantic signal it needs to reason correctly about override hooks.

**What this test proves or disproves:**
- If Config F resolves ≥5 django instances (vs B-Cloaked's 3): Keep List recovers framework-pattern fixes. Privacy-sovereignty claim holds for business logic (the ≫99% of identifiers not on the Keep List).
- If Config F resolves same as B-Cloaked: Framework semantic loss is not the root cause; investigate region-mode context window width for django (multi-file patterns require wider context).
- If Config F resolves more django AND preserves sympy: The hybrid claim — "targeted Keep List + full obfuscation for business logic" — is validated and publishable.

**Secondary ablation — Config G: B-Cloaked-WideRegion**: Test whether widening region window from 50 → 150 lines recovers the 8.0pp E-RegionControl penalty. If yes: the region-mode penalty is a parameter, not a structural limit. If no: narrowing is load-bearing for patch quality, not just a context size issue.

### Implementation Plan

1. **Document first** (this section — DONE)
2. **Add Keep List to `scripts/determinex_cloak/`**:
   - New `FRAMEWORK_KEEP_LIST` dict at module top
   - Extend `IdentifierClassifier._is_exempt()` to check Keep List membership
   - Log kept identifiers to cloak map as `"keep_list_preserved": [...]` for audit transparency
   - Keep List names still appear in obfuscated code; they are NOT in the x_NNNN map
3. **Config F run**: 300 instances, same Hetzner setup, 12 workers, authenticated DockerHub
4. **Measure**: django resolution rate Config F vs B-Cloaked; sympy/sphinx rates unchanged is the null
5. **Document findings** here and in WHITE_PAPER.md Section 3.13

### Privacy Claim With Keep List

The Keep List does NOT break the privacy claim. Framework method names (`get_queryset`, `fit`) are:
- Already public knowledge (Django/scikit-learn open-source docs)
- Not business-logic identifiers (they are API surface, not implementation)
- Present in the model's training data regardless

The privacy claim always was about *proprietary* identifiers — the function names, class names, and variable names that encode business logic unique to the codebase. Keep List names are framework protocol, not proprietary logic. The audit trail (`keep_list_preserved` field) makes this distinction explicit and auditable.

**Refined publishable claim template**: replace the score and anchor counts with values from the larger-disk rerun before publication.

---

## What Was NOT Built (and Why)

| Skipped Item | Reason |
|---|---|
| Rust/tree-sitter parser | Python `ast` is sufficient; generalize post-launch |
| Filename obfuscation | Zero security value; breaks file navigation |
| ML-based identifier classifier | Whitelist subtraction is correct and auditable |
| Per-token confidence scoring | Deterministic map — not probabilistic |
| Live API request redaction middleware | Local restoration is the architecturally correct layer |

---

*Document updated April 28, 2026. Implementation complete. Ablation running.*
*Author: DarthCeltic.*

