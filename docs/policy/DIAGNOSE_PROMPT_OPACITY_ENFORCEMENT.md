# Diagnose Prompt Opacity Enforcement

> Locked under `locks/sentinel/DIAGNOSE_PROMPT_OPACITY_ENFORCEMENT_LOCK_001.json`.

Remediates **CLAUDE-AUTH-007**: previously
`real_model_diagnose_with_build_verifier._build_prompt` embedded the
caller-supplied `workspace_identity` verbatim. The "opaque" property
was a caller convention, not a function-boundary enforcement.

The fix adds `_opacify_workspace_identity(raw)`:

- sha256-hashes the raw value
- truncates to 16 hex chars
- returns `ws-<16hex>`

`_build_prompt` always opacifies before embedding. Regardless of
what the caller supplied (a real path, a code-like fragment, a
secret, multi-line content), only the opaque tag appears in the
model prompt.

Regression tests cover secrets, code fragments, and newlines.
