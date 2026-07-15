# AI Fairness Audit

**Status:** Implemented for binary decision measurement. Not a debiasing system.

## What Is Supported

Determinex provides a deterministic fairness-audit utility for tabular binary
decision outputs:

```powershell
.\.venv\Scripts\python.exe -m scripts.fairness.audit `
  --input decisions.csv `
  --group-field group `
  --truth-field y_true `
  --prediction-field y_pred
```

Input rows must contain:

- a group field, such as `group`, `segment`, or another audited cohort label
- a binary ground-truth field with values `0` or `1`
- a binary prediction or decision field with values `0` or `1`

The report includes per-group counts and rates:

- selection rate
- true positive rate
- false positive rate

It also computes:

- demographic parity difference
- equal opportunity difference
- equalized odds difference

If a group has no positive or negative ground-truth examples, the affected rate is
reported as `null` and the report emits a warning instead of inventing a value.

## Claim Boundary

This feature supports the narrow claim:

> Determinex can compute deterministic group fairness metrics for supplied binary
> decision datasets and emit an auditable JSON report.

It does not support these claims:

- Determinex debiases models.
- Determinex certifies that a dataset is diverse or representative.
- Determinex has a user-facing bias-report feedback workflow.
- Determinex proves a model is fair for deployment.

The safety layer separately blocks requests to build proxy-discrimination systems.
That refusal gate is misuse prevention, not statistical fairness certification.

## Implementation

- Code: `scripts/fairness/audit.py`
- Tests: `tests/fairness/test_fairness_audit.py`

The implementation has no external runtime dependencies. It is intended to run in
offline/local Determinex environments and produce deterministic JSON suitable for
evidence packets or manual review.
