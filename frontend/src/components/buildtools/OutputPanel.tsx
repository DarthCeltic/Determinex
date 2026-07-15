"use client";
import { useState, useRef, useEffect } from "react";
import { Trash2 } from "lucide-react";

type Channel = "compiler" | "tests" | "oracle" | "linter" | "system";
type LogLine = { ts: string; level: "info" | "warn" | "error" | "success" | "muted"; text: string };

const INITIAL_LOGS: Record<Channel, LogLine[]> = {
  compiler: [],
  tests: [],
  oracle: [],
  linter: [],
  system: [],
};

const LINE_COLORS: Record<LogLine["level"], string> = {
  info:    "text-cyan-400",
  warn:    "text-amber-400",
  error:   "text-red-400",
  success: "text-emerald-400",
  muted:   "text-gray-600",
};

const CHANNELS: { id: Channel; label: string }[] = [
  { id:"compiler", label:"Compiler" },
  { id:"tests",    label:"Tests"    },
  { id:"oracle",   label:"Oracle"   },
  { id:"linter",   label:"Linter"   },
  { id:"system",   label:"System"   },
];

export function OutputPanel() {
  const [channel, setChannel] = useState<Channel>("compiler");
  const [logs, setLogs] = useState(INITIAL_LOGS);
  const bottomRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    bottomRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [channel, logs]);

  const clear = () => setLogs((prev) => ({ ...prev, [channel]: [] }));

  return (
    <div className="flex h-full flex-col overflow-hidden" style={{ fontFamily: "var(--determinex-font-mono, monospace)" }}>
      {/* Channel tabs */}
      <div className="shrink-0 flex items-center gap-0 border-b" style={{ borderColor: "var(--determinex-border)", background: "rgba(0,0,0,0.3)" }}>
        {CHANNELS.map(({ id, label }) => {
          const count = logs[id].filter((l) => l.level === "error").length;
          return (
            <button key={id} onClick={() => setChannel(id)}
              className={`flex items-center gap-1.5 border-b-2 px-4 py-2.5 text-[9px] font-black uppercase tracking-widest transition-all ${channel === id ? "border-[var(--determinex-accent)] text-[var(--determinex-accent)]" : "border-transparent text-gray-600 hover:text-gray-400"}`}>
              {label}
              {count > 0 && <span className="rounded-full bg-red-500 text-white text-[7px] font-black w-3.5 h-3.5 flex items-center justify-center">{count}</span>}
            </button>
          );
        })}
        <button onClick={clear} className="ml-auto mr-3 text-gray-700 hover:text-gray-400 transition-colors p-1">
          <Trash2 size={12} />
        </button>
      </div>

      {/* Log output */}
      <div className="flex-1 overflow-y-auto no-scrollbar p-4 space-y-0.5">
        {logs[channel].length === 0 ? (
          <div className="space-y-1">
            <p className="text-[10px] text-gray-700 font-mono">No live output loaded.</p>
            <p className="max-w-xl text-[9px] text-gray-800 font-mono">
              This panel no longer renders sample compiler/test/oracle logs. Wire this channel to a real command or session stream before showing output.
            </p>
          </div>
        ) : (
          logs[channel].map((line, i) => (
            <div key={i} className="flex gap-3 text-[10px] leading-relaxed">
              <span className="text-gray-800 shrink-0 select-none">{line.ts}</span>
              <span className={LINE_COLORS[line.level]}>{line.text}</span>
            </div>
          ))
        )}
        <div ref={bottomRef} />
      </div>
    </div>
  );
}
