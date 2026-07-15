// CLAUDE LANE — Diagnose + patch plan flow panel.
// Locked under: locks/sentinel/FRONTEND_DIAGNOSE_AND_PATCH_PLAN_FLOW_LOCK_001.json

"use client";
import * as React from "react";

import { IdeRepairResponse, invokeIdeCommand } from "@/lib/ide-repair-api";

export const DIAGNOSE_PATCH_PLAN_STATUS_TOKENS = [
  "FRONTEND_DIAGNOSE_DRY_RUN_READY",
  "FRONTEND_LIVE_DIAGNOSE_OPT_IN_REQUIRED",
  "FRONTEND_PATCH_PLAN_QUARANTINED",
  "FRONTEND_PATCH_PLAN_SOURCE_UNCHANGED",
] as const;

interface Props {
  workspacePath: string;
  taskClass?: string;
}

export function DiagnoseAndPatchPlanPanel({
  workspacePath,
  taskClass = "BUILD_DIAGNOSIS",
}: Props) {
  const [diagnoseResp, setDiagnoseResp] = React.useState<IdeRepairResponse | null>(null);
  const [planResp, setPlanResp] = React.useState<IdeRepairResponse | null>(null);
  const [liveOptIn, setLiveOptIn] = React.useState<boolean>(false);
  const [planOptIn, setPlanOptIn] = React.useState<boolean>(false);

  const runDryRun = React.useCallback(async () => {
    const r = await invokeIdeCommand("diagnose_dry_run", {
      workspace: workspacePath, task_class: taskClass,
    });
    setDiagnoseResp(r);
  }, [workspacePath, taskClass]);

  const runLive = React.useCallback(async () => {
    if (!liveOptIn) return;
    const r = await invokeIdeCommand("diagnose_live_opt_in", {
      workspace: workspacePath, task_class: taskClass, opt_in: true,
    });
    setDiagnoseResp(r);
  }, [workspacePath, taskClass, liveOptIn]);

  const runPlan = React.useCallback(async () => {
    if (!planOptIn) return;
    const r = await invokeIdeCommand("generate_patch_plan", {
      workspace: workspacePath, opt_in: true,
    });
    setPlanResp(r);
  }, [workspacePath, planOptIn]);

  return (
    <section
      data-testid="diagnose-and-patch-plan-panel"
      className="rounded border p-3 text-sm space-y-3"
    >
      <header>
        <h3 className="font-medium">Diagnosis &amp; Patch Plan</h3>
        <p className="text-xs opacity-70" data-testid="diagnose-advisory-note">
          The model output is advisory. The verifier is the source of truth.
        </p>
      </header>

      <div className="space-y-2">
        <div className="flex items-center gap-2">
          <button
            type="button"
            onClick={() => void runDryRun()}
            className="rounded border px-2 py-1 text-xs"
            data-testid="diagnose-dry-run-button"
          >
            Diagnose (dry-run)
          </button>
          <span className="text-xs opacity-70">no model call</span>
        </div>

        <div className="flex items-center gap-2">
          <label className="flex items-center gap-1 text-xs">
            <input
              type="checkbox"
              checked={liveOptIn}
              onChange={(e) => setLiveOptIn(e.target.checked)}
              data-testid="diagnose-live-opt-in-checkbox"
            />
            I understand the model output is advisory and untrusted.
          </label>
          <button
            type="button"
            onClick={() => void runLive()}
            disabled={!liveOptIn}
            className="rounded border px-2 py-1 text-xs disabled:opacity-50"
            data-testid="diagnose-live-button"
          >
            Diagnose (live, opt-in)
          </button>
        </div>

        {diagnoseResp && (
          <pre
            className="overflow-auto rounded bg-muted/50 p-2 text-xs"
            data-testid="diagnose-result"
          >
            {JSON.stringify(diagnoseResp, null, 2)}
          </pre>
        )}
      </div>

      <hr className="opacity-40" />

      <div className="space-y-2">
        <div className="flex items-center gap-2">
          <label className="flex items-center gap-1 text-xs">
            <input
              type="checkbox"
              checked={planOptIn}
              onChange={(e) => setPlanOptIn(e.target.checked)}
              data-testid="patch-plan-opt-in-checkbox"
            />
            I understand the plan is quarantined and will not be applied.
          </label>
          <button
            type="button"
            onClick={() => void runPlan()}
            disabled={!planOptIn}
            className="rounded border px-2 py-1 text-xs disabled:opacity-50"
            data-testid="patch-plan-button"
          >
            Generate patch plan (quarantine only)
          </button>
        </div>

        {planResp && (
          <pre
            className="overflow-auto rounded bg-muted/50 p-2 text-xs"
            data-testid="patch-plan-result"
          >
            {JSON.stringify(planResp, null, 2)}
          </pre>
        )}

        <div className="text-xs opacity-80" data-testid="patch-plan-quarantined-note">
          Patch plans are quarantined. No diff is applied here. Your files were not modified.
        </div>
      </div>
    </section>
  );
}

export default DiagnoseAndPatchPlanPanel;
