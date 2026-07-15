"use client";
import { useState } from "react";
import { RefreshCcw, CheckCircle2, XCircle, Zap, TrendingUp } from "lucide-react";
import { isTauri } from "@/lib/api";

type TrainingPair = {
  id: string;
  tool: string;
  lang: string;
  error: string;
  fix: string;
  verdict: "PASS" | "FAIL";
  age: string;
  attempt: number;
};

const INITIAL_PAIRS: TrainingPair[] = [];

export function FlywheelFeed() {
  const [pairs] = useState<TrainingPair[]>(INITIAL_PAIRS);
  const corpusSize = pairs.length;
  const todayAdded = 0;
  const running = false;

  return (
    <div className="relative flex h-full min-h-0 flex-col overflow-hidden p-5">
      <div className="pointer-events-none absolute inset-0 opacity-10">
        <div className="absolute left-1/2 top-1/2 -translate-x-1/2 -translate-y-1/2 h-[600px] w-[600px] rounded-full"
          style={{ background: "#f59e0b", filter: "blur(140px)" }} />
      </div>

      <div className="relative z-10 flex min-h-0 flex-1 flex-col gap-4">
        <div className="flex items-start justify-between gap-4 border-b border-white/10 pb-4">
          <div>
            <div className="flex items-center gap-2 text-[10px] font-black uppercase tracking-widest text-amber-400 mb-2">
              <RefreshCcw size={13} /> Flywheel
            </div>
            <h2 className="text-[26px] font-black leading-tight text-[var(--determinex-text)]"
              style={{ fontFamily: "var(--determinex-font-display)" }}>
              Training Feed
            </h2>
          </div>
          <button
            disabled
            className="flex items-center gap-1.5 rounded-xl border border-white/10 bg-white/[0.02] px-3 py-1.5 text-[10px] font-bold uppercase tracking-widest text-gray-700 transition-all disabled:cursor-not-allowed"
          >
            Awaiting feed
          </button>
        </div>

        <div className="grid grid-cols-3 gap-2 shrink-0">
          <div className="rounded-xl border border-white/8 bg-black/30 p-3 text-center">
            <div className="font-mono text-[20px] font-black text-amber-400">{corpusSize.toLocaleString()}</div>
            <div className="text-[8px] uppercase tracking-widest text-gray-600 mt-0.5">Total Pairs</div>
          </div>
          <div className="rounded-xl border border-white/8 bg-black/30 p-3 text-center">
            <div className="flex items-center justify-center gap-1">
              <TrendingUp size={12} className="text-emerald-400" />
              <span className="font-mono text-[20px] font-black text-emerald-400">+{todayAdded}</span>
            </div>
            <div className="text-[8px] uppercase tracking-widest text-gray-600 mt-0.5">Today</div>
          </div>
          <div className="rounded-xl border border-white/8 bg-black/30 p-3 text-center">
            <div className="flex items-center justify-center">
              <Zap size={14} className={running ? "text-amber-400 animate-pulse" : "text-gray-700"} />
            </div>
            <div className={`text-[8px] uppercase tracking-widest mt-0.5 ${running ? "text-amber-400" : "text-gray-700"}`}>
              {running ? "LIVE" : "IDLE"}
            </div>
          </div>
        </div>

        <div className="flex-1 overflow-y-auto no-scrollbar space-y-2">
          {pairs.map((pair, i) => (
            <div
              key={pair.id}
              className="rounded-xl border border-white/8 overflow-hidden transition-all"
              style={{ opacity: i === 0 ? 1 : Math.max(0.3, 1 - i * 0.04) }}
            >
              <div className="flex items-center gap-2 px-3 py-2 bg-black/20 border-b border-white/5">
                <span className={`h-1.5 w-1.5 rounded-full ${pair.verdict === "PASS" ? "bg-emerald-400" : "bg-red-400"}`} />
                <span className="text-[10px] font-black text-white/70">{pair.tool}</span>
                <span className="text-[8px] font-mono text-gray-600">{pair.lang}</span>
                <span className="text-[8px] font-mono text-gray-700">attempt {pair.attempt}</span>
                <div className="flex-1" />
                <span className={`flex items-center gap-1 text-[8px] font-bold ${pair.verdict === "PASS" ? "text-emerald-400" : "text-red-400"}`}>
                  {pair.verdict === "PASS" ? <CheckCircle2 size={9} /> : <XCircle size={9} />}
                  {pair.verdict}
                </span>
                <span className="text-[8px] font-mono text-gray-700">{pair.age}</span>
              </div>
              <div className="grid grid-cols-2 gap-0 divide-x divide-white/5">
                <div className="px-3 py-2">
                  <div className="text-[7px] uppercase font-bold tracking-widest text-red-400/60 mb-1">Error</div>
                  <div className="text-[9px] font-mono text-red-300/70 leading-relaxed">{pair.error}</div>
                </div>
                <div className="px-3 py-2">
                  <div className="text-[7px] uppercase font-bold tracking-widest text-emerald-400/60 mb-1">Fix</div>
                  <div className="text-[9px] font-mono text-emerald-300/70 leading-relaxed">{pair.fix}</div>
                </div>
              </div>
            </div>
          ))}
          {pairs.length === 0 && (
            <div className="flex h-full min-h-[180px] flex-col items-center justify-center gap-1 opacity-40">
              <p className="text-[11px] text-gray-500">No training pairs loaded</p>
              <p className="max-w-[320px] text-center text-[9px] text-gray-700">
                Live corpus growth requires real Hive build sessions and an ingested training feed.
              </p>
            </div>
          )}
        </div>

        {!isTauri() && (
          <div className="rounded-xl border border-white/5 bg-white/[0.02] px-3 py-2 text-[9px] text-gray-700 font-mono text-center shrink-0">
            Browser mode cannot read native training feed evidence.
          </div>
        )}
      </div>
    </div>
  );
}
