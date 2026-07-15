"use client";
import { useState } from "react";
import { AlertCircle, AlertTriangle, Info, FileCode, ChevronRight, X } from "lucide-react";

type Severity = "error" | "warning" | "info";
type Problem = { id: string; severity: Severity; file: string; line: number; col: number; message: string; source: string };

const PROBLEMS: Problem[] = [];

const SEV_CONFIG = {
  error:   { icon: AlertCircle,   color: "text-red-400",   bg: "bg-red-950/20",   border: "border-red-500/20",   label: "error"   },
  warning: { icon: AlertTriangle, color: "text-amber-400", bg: "bg-amber-950/10", border: "border-amber-500/15", label: "warning" },
  info:    { icon: Info,          color: "text-blue-400",  bg: "bg-blue-950/10",  border: "border-blue-500/15",  label: "info"    },
};

export function ProblemsPanel() {
  const [filter, setFilter] = useState<Severity | "all">("all");
  const [dismissed, setDismissed] = useState<Set<string>>(new Set());

  const visible = PROBLEMS.filter((p) => !dismissed.has(p.id) && (filter === "all" || p.severity === filter));
  const byFile = visible.reduce<Record<string, Problem[]>>((acc, p) => {
    (acc[p.file] = acc[p.file] ?? []).push(p);
    return acc;
  }, {});

  const counts = { error: PROBLEMS.filter((p) => p.severity === "error" && !dismissed.has(p.id)).length,
                   warning: PROBLEMS.filter((p) => p.severity === "warning" && !dismissed.has(p.id)).length,
                   info: PROBLEMS.filter((p) => p.severity === "info" && !dismissed.has(p.id)).length };

  return (
    <div className="flex h-full flex-col overflow-hidden">
      {/* Filter bar */}
      <div className="shrink-0 flex items-center gap-1 border-b px-4 py-2" style={{ borderColor: "var(--determinex-border)", background: "rgba(0,0,0,0.2)" }}>
        {(["all", "error", "warning", "info"] as const).map((f) => {
          const count = f === "all" ? counts.error + counts.warning + counts.info : counts[f];
          return (
            <button key={f} onClick={() => setFilter(f)}
              className={`flex items-center gap-1.5 rounded-lg px-2.5 py-1 text-[9px] font-black uppercase tracking-widest transition-all ${filter === f ? "bg-white/[0.08] text-white" : "text-gray-600 hover:text-gray-400"}`}>
              {f !== "all" && (() => { const { icon: Icon, color } = SEV_CONFIG[f]; return <Icon size={10} className={color} />; })()}
              {f === "all" ? "All" : f} <span className="font-mono text-gray-700">{count}</span>
            </button>
          );
        })}
        <span className="ml-auto text-[8px] text-gray-700 font-mono">{visible.length} problems</span>
      </div>

      {/* Problem list */}
      <div className="flex-1 overflow-y-auto no-scrollbar">
        {Object.keys(byFile).length === 0 ? (
          <div className="flex flex-col items-center justify-center h-full gap-2 opacity-30">
            <AlertCircle size={24} className="text-gray-600" />
            <p className="text-[11px] text-gray-600">No live diagnostics loaded</p>
            <p className="max-w-xs text-center text-[9px] text-gray-700 font-mono">
              This panel no longer renders sample compiler errors. Diagnostics will appear here after a real collector is wired.
            </p>
          </div>
        ) : (
          Object.entries(byFile).map(([file, problems]) => (
            <div key={file} className="border-b border-white/[0.03]">
              <div className="flex items-center gap-2 px-4 py-2 bg-white/[0.02]">
                <FileCode size={11} className="text-gray-600 shrink-0" />
                <span className="text-[10px] font-mono text-gray-500 truncate">{file}</span>
                <span className="ml-auto text-[8px] font-mono text-gray-700">{problems.length}</span>
              </div>
              {problems.map((p) => {
                const { icon: Icon, color, bg, border } = SEV_CONFIG[p.severity];
                return (
                  <div key={p.id} className={`group flex items-start gap-3 px-4 py-2.5 border-l-2 ${border} ${bg} hover:brightness-110 transition-all`}>
                    <Icon size={12} className={`${color} shrink-0 mt-0.5`} />
                    <div className="flex-1 min-w-0">
                      <p className="text-[10px] text-gray-300 leading-relaxed">{p.message}</p>
                      <div className="flex items-center gap-2 mt-0.5">
                        <span className="text-[8px] font-mono text-gray-700">{p.file}:{p.line}:{p.col}</span>
                        <span className="text-[8px] text-gray-700 border border-white/8 rounded px-1">{p.source}</span>
                      </div>
                    </div>
                    <button onClick={() => setDismissed((s) => new Set([...s, p.id]))}
                      className="opacity-0 group-hover:opacity-100 transition-opacity text-gray-700 hover:text-gray-400">
                      <X size={11} />
                    </button>
                  </div>
                );
              })}
            </div>
          ))
        )}
      </div>
    </div>
  );
}
