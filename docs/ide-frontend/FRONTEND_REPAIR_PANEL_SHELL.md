# Frontend Repair Panel Shell

> Locked under `locks/sentinel/FRONTEND_REPAIR_PANEL_SHELL_LOCK_001.json`.

Minimal Next.js shell at `/ide-repair` rendering the 9 visible sections
(Workspace, Verifier, Model Route, Diagnosis, Patch Plan, Temp
Verification, Human Approval, Evidence, Risk Warnings) with
always-visible source-mutation-blocked, training-eligibility-false,
and approval-required banners.

The TypeScript API wrapper (`src/lib/ide-repair-api.ts`) refuses to
honor `source_mutation_authorized=true` or `training_eligible=true`
from any backend response — defense-in-depth across the seam.
