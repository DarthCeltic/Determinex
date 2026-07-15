"use client";
import { useState } from "react";
import { Check, X, RefreshCw, ChevronDown, ChevronRight, Clock, Play, GitBranch } from "lucide-react";

type RunStatus = "success" | "failure" | "running" | "queued";
type Job = { name: string; status: RunStatus; duration?: string };
type Run = { id: string; workflow: string; branch: string; commit: string; status: RunStatus; duration?: string; ago: string; jobs: Job[]; expanded?: boolean };

const INITIAL_RUNS: Run[] = [];

const STATUS_CONFIG: Record<RunStatus, { icon: typeof Check; color: string; bg: string; border: string }> = {
  success: { icon: Check,      color:"text-emerald-400", bg:"bg-emerald-950/10", border:"border-emerald-500/20" },
  failure: { icon: X,          color:"text-red-400",     bg:"bg-red-950/10",     border:"border-red-500/20"     },
  running: { icon: RefreshCw,  color:"text-cyan-400",    bg:"bg-cyan-950/10",    border:"border-cyan-500/20"    },
  queued:  { icon: Clock,      color:"text-gray-500",    bg:"",                  border:"border-white/8"        },
};

export function CICDPanel() {
  const [runs, setRuns] = useState(INITIAL_RUNS);
  const [branch, setBranch] = useState("all");
  const branches = ["all", ...Array.from(new Set(runs.map((r) => r.branch)))];

  const toggle = (id: string) => setRuns((prev) => prev.map((r) => r.id === id ? { ...r, expanded: !r.expanded } : r));
  const filtered = branch === "all" ? runs : runs.filter((r) => r.branch === branch);

  return (
    <div className="flex h-full flex-col overflow-hidden">
      {/* Filter bar */}
      <div className="shrink-0 flex items-center gap-2 border-b px-4 py-2.5" style={{ borderColor: "var(--determinex-border)", background: "rgba(0,0,0,0.2)" }}>
        <GitBranch size={11} className="text-gray-600" />
        <select value={branch} onChange={(e) => setBranch(e.target.value)}
          className="rounded-lg border border-white/8 bg-black/30 px-2 py-1 text-[9px] font-mono text-gray-500 outline-none focus:border-[var(--determinex-accent)]/30">
          {branches.map((b) => <option key={b} value={b}>{b}</option>)}
        </select>
        <span className="ml-auto text-[8px] text-gray-700 font-mono">{filtered.length} runs</span>
        <button
          disabled
          title="CI trigger requires a repository CI integration"
          className="flex items-center gap-1 rounded-lg border border-white/8 bg-white/[0.02] px-2.5 py-1 text-[9px] font-bold text-gray-700 transition-all disabled:cursor-not-allowed"
        >
          <Play size={9} /> Trigger
        </button>
      </div>

      {/* Run list */}
      <div className="flex-1 overflow-y-auto no-scrollbar divide-y divide-white/[0.03]">
        {filtered.map((run) => {
          const { icon: Icon, color, bg, border } = STATUS_CONFIG[run.status];
          return (
            <div key={run.id}>
              <button onClick={() => toggle(run.id)}
                className="w-full flex items-center gap-3 px-4 py-3 hover:bg-white/[0.02] transition-colors text-left">
                <Icon size={13} className={`${color} shrink-0 ${run.status === "running" ? "animate-spin" : ""}`} />
                <div className="flex-1 min-w-0">
                  <div className="text-[10px] font-semibold text-white/75">{run.workflow}</div>
                  <div className="flex items-center gap-2 mt-0.5">
                    <span className="text-[8px] font-mono text-gray-700">{run.branch}</span>
                    <span className="text-[8px] font-mono text-gray-700">{run.commit}</span>
                  </div>
                </div>
                <div className="text-right shrink-0">
                  <div className="text-[9px] font-mono text-gray-600">{run.duration ?? "..."}</div>
                  <div className="text-[8px] text-gray-700">{run.ago}</div>
                </div>
                {run.expanded ? <ChevronDown size={11} className="text-gray-600 shrink-0" /> : <ChevronRight size={11} className="text-gray-600 shrink-0" />}
              </button>
              {run.expanded && (
                <div className="px-4 pb-3 space-y-1.5 bg-black/10">
                  {run.jobs.map((job, i) => {
                    const { icon: JIcon, color: jc } = STATUS_CONFIG[job.status];
                    return (
                      <div key={i} className="flex items-center gap-2.5 pl-6">
                        <JIcon size={10} className={`${jc} shrink-0 ${job.status === "running" ? "animate-spin" : ""}`} />
                        <span className="text-[9px] text-gray-500 flex-1">{job.name}</span>
                        <span className="text-[8px] font-mono text-gray-700">{job.duration ?? ""}</span>
                      </div>
                    );
                  })}
                </div>
              )}
            </div>
          );
        })}
        {filtered.length === 0 && (
          <div className="flex flex-col items-center justify-center gap-1 py-16 opacity-40">
            <p className="text-[11px] text-gray-500">No CI runs loaded</p>
            <p className="max-w-[260px] text-center text-[9px] text-gray-700">
              Connect a CI provider or ingest local run evidence before this panel reports status.
            </p>
          </div>
        )}
      </div>
    </div>
  );
}
