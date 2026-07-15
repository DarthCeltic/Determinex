// CLAUDE LANE - IDE repair panel shell.
// Locked under: locks/sentinel/FRONTEND_REPAIR_PANEL_SHELL_LOCK_001.json
//
// Lays out the 9 visible sections and mounts the shipped read-only/gated
// sub-panels. The shell renders no source mutation controls and surfaces every
// blocked state explicitly.

"use client";
import * as React from "react";

import { tauriRuntimePresent } from "@/lib/ide-repair-api";
import { DiagnoseAndPatchPlanPanel } from "./DiagnoseAndPatchPlanPanel";
import { EvidenceViewerPanel } from "./EvidenceViewerPanel";
import { HumanApprovalPanel } from "./HumanApprovalPanel";
import { LocalModelSettingsPanel } from "./LocalModelSettingsPanel";
import { ModelRoutePanel } from "./ModelRoutePanel";
import { RealDiagnosisPanel } from "./RealDiagnosisPanel";
import { SourceApplyDryRunPanel } from "./SourceApplyDryRunPanel";
import { TempVerifyPanel } from "./TempVerifyPanel";
import { WorkspaceStatusPanel } from "./WorkspaceStatusPanel";

export const REPAIR_PANEL_SECTIONS = [
  "Workspace",
  "Verifier",
  "Model Route",
  "Diagnosis",
  "Patch Plan",
  "Temp Verification",
  "Human Approval",
  "Evidence",
  "Risk Warnings",
] as const;

export const REPAIR_PANEL_STATUS_TOKENS = [
  "REPAIR_PANEL_SHELL_READY",
  "REPAIR_PANEL_BLOCKED_FRONTEND_MISSING",
  "REPAIR_PANEL_SOURCE_MUTATION_BLOCKED_VISIBLE",
  "REPAIR_PANEL_RISK_WARNINGS_VISIBLE",
] as const;

interface RepairPanelShellProps {
  children?: React.ReactNode;
  workspacePath?: string;
}

function renderRepairSection(name: (typeof REPAIR_PANEL_SECTIONS)[number], workspacePath: string) {
  if (name === "Risk Warnings") {
    return (
      <ul className="list-disc pl-5 space-y-1">
        <li>The diagnosis is advisory. The model can be wrong.</li>
        <li>The patch plan is untrusted until the verifier passes.</li>
        <li>Source mutation requires explicit human approval.</li>
        <li>Nothing here becomes training data.</li>
      </ul>
    );
  }
  if (name === "Workspace") return <WorkspaceStatusPanel workspacePath={workspacePath} />;
  if (name === "Verifier") return <SourceApplyDryRunPanel workspacePath={workspacePath} />;
  if (name === "Model Route") {
    return (
      <div className="space-y-3">
        <ModelRoutePanel />
        <LocalModelSettingsPanel />
      </div>
    );
  }
  if (name === "Diagnosis") {
    return (
      <div>
        <DiagnoseAndPatchPlanPanel workspacePath={workspacePath} />
        <RealDiagnosisPanel workspacePath={workspacePath} />
      </div>
    );
  }
  if (name === "Patch Plan") {
    return <DiagnoseAndPatchPlanPanel workspacePath={workspacePath} />;
  }
  if (name === "Temp Verification") return <TempVerifyPanel workspacePath={workspacePath} />;
  if (name === "Human Approval") return <HumanApprovalPanel workspacePath={workspacePath} />;
  if (name === "Evidence") return <EvidenceViewerPanel workspacePath={workspacePath} />;
  return <span>Unavailable</span>;
}

export function RepairPanelShell({ children, workspacePath = "" }: RepairPanelShellProps) {
  const runtimePresent = tauriRuntimePresent();
  const resolvedWorkspacePath =
    workspacePath ||
    (typeof window !== "undefined" ? window.location.pathname : "");
  const status = runtimePresent
    ? "REPAIR_PANEL_SHELL_READY"
    : "REPAIR_PANEL_BLOCKED_FRONTEND_MISSING";

  return (
    <div
      data-testid="ide-repair-panel-shell"
      data-status={status}
      className="flex flex-col gap-3 p-4 max-w-5xl mx-auto"
    >
      <header className="flex items-center justify-between border-b pb-2">
        <h1 className="text-lg font-semibold">Determinex - Repair Panel</h1>
        <span
          className="text-xs uppercase tracking-wide opacity-70"
          data-testid="repair-shell-status"
        >
          {status}
        </span>
      </header>

      <aside
        role="note"
        className="rounded border border-amber-500/40 bg-amber-500/5 px-3 py-2 text-sm"
        data-testid="repair-shell-safety-banner"
      >
        <div data-testid="repair-shell-source-mutation-blocked">
          Source mutation is BLOCKED until a human approves a verified diff.
        </div>
        <div data-testid="repair-shell-training-eligibility">
          Training eligibility: <strong>False</strong> for everything you do here.
        </div>
        <div data-testid="repair-shell-approval-required">
          Approval is required before any change leaves the temp workspace.
        </div>
      </aside>

      <section className="grid grid-cols-1 md:grid-cols-2 gap-3">
        {REPAIR_PANEL_SECTIONS.map((name) => (
          <article
            key={name}
            className="rounded border bg-background/40 p-3"
            data-testid={`repair-section-${name.toLowerCase().replace(/ /g, "-")}`}
          >
            <h2 className="text-sm font-medium uppercase tracking-wide opacity-80">
              {name}
            </h2>
            <div className="mt-2 text-xs" data-testid="repair-section-content">
              {renderRepairSection(name, resolvedWorkspacePath)}
            </div>
          </article>
        ))}
      </section>

      {children}
    </div>
  );
}

export default RepairPanelShell;
