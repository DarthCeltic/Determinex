"use client";
import { useEffect, useRef, useState } from "react";
import { GitBranch, AlertCircle, CheckCircle2, Zap, Cpu, Circle, PanelBottom } from "lucide-react";
import { AiRouteSummary } from "@/components/AiRouteSelect";
import { routeKeyReady, type ApiKeyStatus } from "@/lib/aiRouting";
import { useAiRouter } from "@/contexts/AiRouterContext";

type Props = {
  activeSidebar: string;
  selectedModel: string;
  gitBranch: string;
  oracleAccepted: boolean | null;
  oracleVerdict: string | null;
  errorCount: number;
  warningCount?: number;
  keyStatus?: ApiKeyStatus;
  onChangeModel?: (value: string) => void;
  onClickErrors?: () => void;
  onClickModel?: () => void;
  onTogglePanel?: () => void;
};

const PANEL_LABELS: Record<string, string> = {
  none:        "Home",
  ideation:    "Concept Lab",
  pipeline:    "Build Pipeline",
  explorer:    "Workspace",
  git:         "Source Control",
  hive:        "Work",
  benchmark:   "Brain",
  tools:       "Tools",
  proof:       "Proof",
  health:      "Health Map",
  trace:       "Agent Trace",
  cloak:       "Privacy Cockpit",
  flywheel:    "Flywheel Feed",
  terminal:    "Terminal",
  editor:      "Editor",
  search:      "Verified Search",
};

function ModelChip({ model, ready }: { model: string; ready: boolean }) {
  const short = model
    .replace(/determinex/gi, "determinex")
    .replace("claude-", "")
    .replace("sonnet-", "Sonnet ")
    .replace("opus-", "Opus ")
    .replace("haiku-", "Haiku ")
    .replace("gemini-", "Gemini ")
    .replace("gpt-", "GPT-")
    .slice(0, 20);
  return (
    <span className="flex items-center gap-1 text-[9px] text-gray-500 font-mono border-l border-white/8 pl-2.5 ml-0.5">
      <Circle size={6} className={`fill-current ${ready ? "text-emerald-400" : "text-amber-400"}`} />
      <Cpu size={9} className="text-violet-500/60" />
      {model === "auto" ? "Auto" : short}
    </span>
  );
}

export function StatusBar({
  activeSidebar,
  selectedModel,
  gitBranch,
  oracleAccepted,
  oracleVerdict,
  errorCount,
  warningCount = 0,
  keyStatus = {},
  onChangeModel,
  onClickErrors,
  onClickModel,
  onTogglePanel,
}: Props) {
  const panelLabel = PANEL_LABELS[activeSidebar] ?? activeSidebar;
  const router = useAiRouter();
  const [routePopoverOpen, setRoutePopoverOpen] = useState(false);
  const popoverRef = useRef<HTMLDivElement>(null);
  const modelReady = routeKeyReady(selectedModel, keyStatus) && router.routeWarnings.length === 0;

  useEffect(() => {
    if (!routePopoverOpen) return;
    const onOutside = (e: MouseEvent) => {
      if (popoverRef.current && !popoverRef.current.contains(e.target as Node)) {
        setRoutePopoverOpen(false);
      }
    };
    const onEscape = (e: KeyboardEvent) => {
      if (e.key === "Escape") setRoutePopoverOpen(false);
    };
    document.addEventListener("mousedown", onOutside);
    document.addEventListener("keydown", onEscape);
    return () => {
      document.removeEventListener("mousedown", onOutside);
      document.removeEventListener("keydown", onEscape);
    };
  }, [routePopoverOpen]);

  const oracleColor =
    oracleAccepted === true
      ? "text-emerald-400"
      : oracleAccepted === false
      ? "text-red-400"
      : "text-gray-700";

  return (
    <div
      className="fixed bottom-0 left-0 right-0 z-50 flex h-5 items-center justify-between select-none"
      style={{
        background: "rgba(4,6,10,0.96)",
        borderTop: "1px solid rgba(255,255,255,0.05)",
        backdropFilter: "blur(8px)",
      }}
    >
      {/* Left section */}
      <div className="flex items-center h-full">
        {/* Brand pill */}
        <div
          className="flex h-full items-center px-3 text-[9px] font-black uppercase tracking-widest"
          style={{ background: "var(--determinex-accent)", color: "#000" }}
        >
          Determinex
        </div>

        {/* Git branch */}
        <div className="flex items-center gap-1 px-2.5 text-[9px] text-gray-600 border-r border-white/8 h-full">
          <GitBranch size={10} />
          <span className="font-mono">{gitBranch || "no repo"}</span>
        </div>

        {/* Errors */}
        <button
          onClick={onClickErrors}
          className="flex items-center gap-1 px-2.5 text-[9px] h-full border-r border-white/8 transition-colors hover:bg-white/[0.04]"
        >
          {errorCount > 0 ? (
            <>
              <AlertCircle size={10} className="text-red-400" />
              <span className="text-red-400 font-mono">{errorCount}</span>
            </>
          ) : (
            <>
              <CheckCircle2 size={10} className="text-gray-700" />
              <span className="text-gray-700">0</span>
            </>
          )}
          {warningCount > 0 && (
            <>
              <AlertCircle size={10} className="text-amber-400 ml-1.5" />
              <span className="text-amber-400 font-mono">{warningCount}</span>
            </>
          )}
        </button>

        {/* Panel toggle */}
        {onTogglePanel && (
          <button
            onClick={onTogglePanel}
            title="Toggle bottom/side panel"
            className="flex items-center gap-1 px-2.5 text-[9px] h-full border-r border-white/8 text-gray-600 transition-colors hover:bg-white/[0.04] hover:text-gray-300"
          >
            <PanelBottom size={10} />
          </button>
        )}
      </div>

      {/* Center: active panel */}
      <div className="absolute left-1/2 -translate-x-1/2 text-[9px] font-mono text-gray-600 pointer-events-none">
        {panelLabel}
      </div>

      {/* Right section */}
      <div className="flex items-center gap-0 h-full pr-1">
        {/* Oracle status */}
        <div className="flex items-center gap-1.5 px-2.5 text-[9px] border-l border-white/8 h-full">
          <Circle
            size={7}
            className={`${oracleColor} fill-current`}
          />
          <span className={`font-mono ${oracleColor}`}>
            {oracleVerdict
              ? oracleVerdict.slice(0, 12)
              : "Oracle Ready"}
          </span>
        </div>

        {/* Flywheel pulse */}
        <div className="flex items-center gap-1 px-2.5 text-[9px] text-gray-700 border-l border-white/8 h-full">
          <Zap size={9} className="text-orange-500/50" />
          <span className="font-mono">Flywheel</span>
        </div>

        {/* Model — click opens a quick-switch popover */}
        <div className="relative h-full" ref={popoverRef}>
          <button
            onClick={() => setRoutePopoverOpen((v) => !v)}
            className="flex items-center h-full px-2.5 border-l border-white/8 hover:bg-white/[0.04] transition-colors"
          >
            <ModelChip model={selectedModel} ready={modelReady} />
          </button>

          {routePopoverOpen && (
            <div className="absolute bottom-6 right-0 z-[200] w-[310px] animate-fade-in">
              <AiRouteSummary
                value={selectedModel}
                keyStatus={keyStatus}
                onChange={onChangeModel}
                onOpenSettings={() => {
                  setRoutePopoverOpen(false);
                  onClickModel?.();
                }}
              />
            </div>
          )}
        </div>

        {/* Shortcut hint */}
        <div className="pl-2 pr-2.5 text-[8px] font-mono text-gray-800 border-l border-white/5 h-full flex items-center">
          ^P
        </div>
      </div>
    </div>
  );
}
