// CLAUDE LANE — Source apply dry-run panel.
// Locked under: locks/sentinel/FRONTEND_SOURCE_APPLY_DRY_RUN_PANEL_LOCK_001.json
//
// Read-only panel for the source apply gate. NO real apply button is
// rendered here. The panel surfaces whether the gate would allow a
// write IF a real approval were present, but explicitly disables the
// notion of writing.

"use client";
import * as React from "react";

import { IdeRepairResponse, invokeIdeCommand } from "@/lib/ide-repair-api";

export const SOURCE_APPLY_DRY_RUN_PANEL_STATUS_TOKENS = [
  "SOURCE_APPLY_DRY_RUN_PANEL_READY",
  "SOURCE_APPLY_BLOCKED_VISIBLE",
  "SOURCE_APPLY_SOURCE_UNCHANGED_VISIBLE",
  "SOURCE_APPLY_REAL_WRITE_DISABLED",
] as const;

interface Props {
  workspacePath: string;
}

export function SourceApplyDryRunPanel({ workspacePath }: Props) {
  const [resp, setResp] = React.useState<IdeRepairResponse | null>(null);

  const refresh = React.useCallback(async () => {
    const r = await invokeIdeCommand("source_apply_dry_run", { workspace: workspacePath });
    setResp(r);
  }, [workspacePath]);

  React.useEffect(() => { void refresh(); }, [refresh]);

  const payload = (resp?.payload ?? {}) as Record<string, unknown>;
  const sourceMutationStatus = String(payload.source_mutation ?? "BLOCKED_PENDING_HUMAN_APPROVAL");
  const blocked = !sourceMutationStatus.includes("READY");

  return (
    <section
      data-testid="source-apply-dry-run-panel"
      className="rounded border p-3 text-sm space-y-2"
    >
      <header>
        <h3 className="font-medium">Source Apply (dry-run only)</h3>
      </header>

      <div className="rounded border border-amber-500/30 bg-amber-500/5 px-3 py-2 text-xs"
           data-testid="source-apply-real-write-disabled-note">
        Real source mutation is disabled in this build. This panel shows what
        the gate WOULD decide if a real approval were submitted. No file is
        written here.
      </div>

      <dl className="grid grid-cols-2 gap-1 text-xs">
        <dt className="opacity-70">Source mutation</dt>
        <dd className="font-mono" data-testid="source-apply-gate-status">
          {sourceMutationStatus}
        </dd>
      </dl>

      {blocked && (
        <div className="rounded border border-red-500/30 bg-red-500/5 p-2 text-xs"
             data-testid="source-apply-blocked-note">
          Apply is blocked. Possible reasons: no signed approval, stale source,
          diff mismatch, verifier not passed. See evidence viewer for the full
          gate decision record.
        </div>
      )}

      <div className="text-xs opacity-80" data-testid="source-apply-source-unchanged-note">
        Your original files are unchanged. Rollback note: any temp workspace
        produced by an earlier verify step is automatically discarded on
        verifier failure.
      </div>
    </section>
  );
}

export default SourceApplyDryRunPanel;
