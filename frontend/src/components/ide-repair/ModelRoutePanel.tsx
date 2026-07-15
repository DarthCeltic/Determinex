// CLAUDE LANE — Model route panel.
// Locked under: locks/sentinel/FRONTEND_MODEL_ROUTE_PANEL_LOCK_001.json

"use client";
import * as React from "react";

import { IdeRepairResponse, invokeIdeCommand } from "@/lib/ide-repair-api";

export const FRONTEND_MODEL_ROUTE_PANEL_STATUS_TOKENS = [
  "MODEL_ROUTE_PANEL_READY",
  "MODEL_ROUTE_DRY_RUN_VISIBLE",
  "MODEL_ROUTE_LIVE_OPT_IN_VISIBLE",
  "MODEL_ROUTE_BLOCKED_NO_MODEL_VISIBLE",
  "MODEL_ROUTE_NETWORK_BLOCKED_VISIBLE",
] as const;

interface Props {
  taskClass?: string;
  initial?: IdeRepairResponse | null;
}

export function ModelRoutePanel({ taskClass = "BUILD_DIAGNOSIS", initial = null }: Props) {
  const [resp, setResp] = React.useState<IdeRepairResponse | null>(initial);

  const refresh = React.useCallback(async () => {
    const r = await invokeIdeCommand("get_model_route_status", { task_class: taskClass });
    setResp(r);
  }, [taskClass]);

  React.useEffect(() => { void refresh(); }, [refresh]);

  const payload = (resp?.payload ?? {}) as Record<string, unknown>;
  const decision = String(payload.decision ?? "");
  const selectedRoute = String(payload.selected_route ?? "");
  const selectedModelId = String(payload.selected_model_id ?? "");

  const dryRunDefault = decision === "" || decision === "ROUTE_DRY_RUN_SELECTED";
  const liveOptInAvailable = decision === "ROUTE_SELECTED" || decision === "ROUTE_FALLBACK_SELECTED";
  const noModel = decision.startsWith("ROUTE_BLOCKED_") || decision === "ROUTE_NO_MODEL_REQUIRED";

  const status = noModel
    ? "MODEL_ROUTE_BLOCKED_NO_MODEL_VISIBLE"
    : liveOptInAvailable
      ? "MODEL_ROUTE_LIVE_OPT_IN_VISIBLE"
      : "MODEL_ROUTE_DRY_RUN_VISIBLE";

  return (
    <section
      data-testid="model-route-panel"
      data-status={status}
      className="rounded border p-3 text-sm"
    >
      <header className="flex items-center justify-between">
        <h3 className="font-medium">Model Route</h3>
        <span className="text-xs uppercase opacity-70" data-testid="model-route-mode">
          Dry-run default
        </span>
      </header>

      <dl className="mt-2 grid grid-cols-2 gap-1">
        <dt className="opacity-70">Task class</dt>
        <dd data-testid="model-route-task-class">{taskClass}</dd>

        <dt className="opacity-70">Decision</dt>
        <dd data-testid="model-route-decision">{decision || "loading…"}</dd>

        <dt className="opacity-70">Route</dt>
        <dd data-testid="model-route-selected">{selectedRoute || "—"}</dd>

        <dt className="opacity-70">Model id</dt>
        <dd className="font-mono text-xs" data-testid="model-route-model-id">
          {selectedModelId || "—"}
        </dd>
      </dl>

      <ul className="mt-3 space-y-1 text-xs">
        {dryRunDefault && (
          <li className="opacity-80" data-testid="model-route-dry-run-note">
            Dry-run is the default. No live model call is made unless you opt in explicitly.
          </li>
        )}
        {liveOptInAvailable && (
          <li className="text-emerald-700" data-testid="model-route-live-opt-in-note">
            Live opt-in is available for this task class. The model output remains advisory.
          </li>
        )}
        {noModel && (
          <li className="text-amber-700" data-testid="model-route-blocked-note">
            Live diagnose is blocked: no admitted local model.
          </li>
        )}
        <li className="opacity-80" data-testid="model-route-network-blocked-note">
          Network/cloud providers are blocked by default.
        </li>
      </ul>
    </section>
  );
}

export default ModelRoutePanel;
