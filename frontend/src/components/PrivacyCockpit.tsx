"use client";
import { useState } from "react";
import { ShieldCheck, Cloud, HardDrive, EyeOff, Eye, Search } from "lucide-react";
import { isTauri } from "@/lib/api";
import { useSettings } from "@/contexts/SettingsContext";
import { NETWORK_POLICY_COPY } from "@/lib/networkPolicy";

type CloakEntry = {
  real: string;
  token: string;
  kind: "function" | "class" | "variable" | "module";
  sentToCloud: boolean;
  occurrences: number;
};

const CLOAK_MAP: CloakEntry[] = [];

const KIND_COLORS: Record<CloakEntry["kind"], string> = {
  function: "#60a5fa",
  class: "#a78bfa",
  variable: "#34d399",
  module: "#f59e0b",
};

export function PrivacyCockpit() {
  const [reveal, setReveal] = useState<Set<string>>(new Set());
  const [filter, setFilter] = useState<"all" | "cloud" | "local">("all");
  const [search, setSearch] = useState("");
  const { networkPolicy, setSettingsTab, setShowSettings } = useSettings();
  const networkCopy = NETWORK_POLICY_COPY[networkPolicy];

  const cloudCount = CLOAK_MAP.filter((e) => e.sentToCloud).length;
  const localCount = CLOAK_MAP.filter((e) => !e.sentToCloud).length;
  const totalOccurrences = CLOAK_MAP.reduce((s, e) => s + e.occurrences, 0);

  const filtered = CLOAK_MAP
    .filter((e) => filter === "all" || (filter === "cloud" ? e.sentToCloud : !e.sentToCloud))
    .filter((e) => !search || e.real.includes(search) || e.token.includes(search));

  const toggleReveal = (token: string) => {
    setReveal((prev) => {
      const next = new Set(prev);
      if (next.has(token)) next.delete(token);
      else next.add(token);
      return next;
    });
  };

  return (
    <div className="relative flex h-full min-h-0 flex-col overflow-hidden p-5">
      <div className="pointer-events-none absolute inset-0 opacity-8">
        <div className="absolute inset-0"
          style={{ background: "repeating-linear-gradient(0deg, transparent, transparent 30px, rgba(52,211,153,0.02) 30px, rgba(52,211,153,0.02) 31px)" }} />
      </div>

      <div className="relative z-10 flex min-h-0 flex-1 flex-col gap-4">
        {/* Header */}
        <div className="border-b border-white/10 pb-4">
          <div className="flex items-center gap-2 text-[10px] font-black uppercase tracking-widest text-emerald-400 mb-2">
            <ShieldCheck size={13} /> Project Cloak
          </div>
          <h2 className="text-[26px] font-black leading-tight text-[var(--determinex-text)]"
            style={{ fontFamily: "var(--determinex-font-display)" }}>
            Privacy Cockpit
          </h2>
          <p className="text-[10px] text-gray-600 mt-1 font-mono">
            Cloak map appears after a Cloak-enabled run writes audit evidence.
          </p>
        </div>

        <button
          type="button"
          onClick={() => {
            setSettingsTab("network");
            setShowSettings(true);
          }}
          className="rounded-full border border-white/10 bg-black/30 px-3 py-1.5 text-left text-[9px] font-black uppercase tracking-widest text-gray-500 transition hover:border-emerald-500/40 hover:text-emerald-400"
          title="Open Network Policy settings"
        >
          Network: {networkCopy.shortLabel}
        </button>

        {/* Stats */}
        <div className="grid grid-cols-3 gap-2 shrink-0">
          <div className="rounded-xl border border-white/8 bg-black/30 p-3 text-center">
            <div className="font-mono text-[22px] font-black text-emerald-400">{CLOAK_MAP.length}</div>
            <div className="text-[8px] uppercase tracking-widest text-gray-600 mt-0.5">Identifiers</div>
          </div>
          <div className="rounded-xl border border-white/8 bg-black/30 p-3 text-center">
            <div className="font-mono text-[22px] font-black text-violet-400">{cloudCount}</div>
            <div className="text-[8px] uppercase tracking-widest text-gray-600 mt-0.5">Sent to Cloud</div>
          </div>
          <div className="rounded-xl border border-white/8 bg-black/30 p-3 text-center">
            <div className="font-mono text-[22px] font-black text-cyan-400">{totalOccurrences}</div>
            <div className="text-[8px] uppercase tracking-widest text-gray-600 mt-0.5">Occurrences</div>
          </div>
        </div>

        {/* Filter + Search */}
        <div className="flex flex-col gap-2 shrink-0">
          <div className="grid grid-cols-3 gap-1.5">
            {(["all", "cloud", "local"] as const).map((f) => (
              <button
                key={f}
                onClick={() => setFilter(f)}
                className="flex items-center justify-center gap-1.5 rounded-lg border py-1.5 text-[9px] font-bold uppercase tracking-wider transition-all"
                style={{
                  borderColor: filter === f ? (f === "cloud" ? "#a78bfa60" : f === "local" ? "#34d39960" : "rgba(255,255,255,0.2)") : "rgba(255,255,255,0.07)",
                  background: filter === f ? "rgba(255,255,255,0.05)" : "transparent",
                  color: filter === f ? "#fff" : "#6b7280",
                }}
              >
                {f === "cloud" && <Cloud size={10} />}
                {f === "local" && <HardDrive size={10} />}
                {f === "all" && <EyeOff size={10} />}
                {f}
              </button>
            ))}
          </div>
          <div className="relative">
            <Search size={11} className="absolute left-3 top-1/2 -translate-y-1/2 text-gray-600" />
            <input
              value={search}
              onChange={(e) => setSearch(e.target.value)}
              placeholder="Filter identifiers…"
              className="w-full rounded-xl border border-white/8 bg-black/30 py-2 pl-8 pr-3 text-[11px] text-white/70 placeholder:text-gray-700 outline-none focus:border-[var(--determinex-accent)]/40"
            />
          </div>
        </div>

        {/* Map table */}
        <div className="flex-1 overflow-y-auto no-scrollbar space-y-1">
          {filtered.map((entry) => {
            const shown = reveal.has(entry.token);
            return (
              <div
                key={entry.token}
                className="flex items-center gap-3 rounded-xl border border-white/5 bg-white/[0.01] px-3 py-2.5 hover:border-white/10 transition-colors"
              >
                {/* Kind badge */}
                <span
                  className="text-[7px] font-black uppercase tracking-wider rounded px-1.5 py-0.5 shrink-0 font-mono"
                  style={{ color: KIND_COLORS[entry.kind], background: KIND_COLORS[entry.kind] + "20" }}
                >
                  {entry.kind.slice(0, 2).toUpperCase()}
                </span>

                {/* Cloaked name */}
                <span className="font-mono text-[11px] text-emerald-400/80 shrink-0 w-14">{entry.token}</span>

                {/* Arrow */}
                <span className="text-gray-700 text-[10px] shrink-0">→</span>

                {/* Real name (togglable) */}
                <span className={`font-mono text-[11px] flex-1 min-w-0 truncate transition-all ${shown ? "text-white/70" : "blur-[3px] select-none text-white/40"}`}>
                  {entry.real}
                </span>

                {/* Cloud/local badge */}
                <span className={`flex items-center gap-1 text-[8px] shrink-0 ${entry.sentToCloud ? "text-violet-400" : "text-emerald-600"}`}>
                  {entry.sentToCloud ? <Cloud size={9} /> : <HardDrive size={9} />}
                  <span className="font-mono">{entry.sentToCloud ? "cloud" : "local"}</span>
                </span>

                {/* Occurrences */}
                <span className="text-[8px] font-mono text-gray-700 shrink-0 w-6 text-right">{entry.occurrences}×</span>

                {/* Reveal toggle */}
                <button onClick={() => toggleReveal(entry.token)} className="shrink-0 text-gray-700 hover:text-gray-400 transition-colors">
                  {shown ? <EyeOff size={12} /> : <Eye size={12} />}
                </button>
              </div>
            );
          })}
          {filtered.length === 0 && (
            <div className="flex h-full min-h-[150px] flex-col items-center justify-center gap-1 opacity-40">
              <p className="text-[11px] text-gray-500">No Cloak audit loaded</p>
              <p className="max-w-[300px] text-center text-[9px] text-gray-700">
                Run with Cloak audit enabled before this panel reports identifiers or leakage proof.
              </p>
            </div>
          )}
        </div>

        {/* Proof banner */}
        <div className="rounded-xl border border-white/10 bg-black/30 px-4 py-3 flex items-center gap-3 shrink-0">
          <ShieldCheck size={16} className="text-gray-500 shrink-0" />
          <div>
            <div className="text-[10px] font-black text-gray-400">No Cloak proof loaded</div>
            <div className="text-[9px] text-gray-700 mt-0.5 font-mono">
              Loaded audit: {cloudCount} cloud tokens / {localCount} local-only identifiers
            </div>
          </div>
        </div>

        {!isTauri() && (
          <div className="rounded-xl border border-white/5 bg-white/[0.02] px-3 py-2 text-[9px] text-gray-700 font-mono text-center shrink-0">
            Browser mode cannot read native Cloak audit evidence.
          </div>
        )}
      </div>
    </div>
  );
}
