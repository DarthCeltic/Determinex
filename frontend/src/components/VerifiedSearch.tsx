"use client";
import { useState, useRef } from "react";
import { Search, CheckCircle2, XCircle, Zap, Clock, ArrowRight } from "lucide-react";
import { isTauri, invokeSafe } from "@/lib/api";

type SampleResult = {
  attempt: number;
  verdict: "PASS" | "FAIL";
  code: string;
  duration: number;
};
type SearchResult = {
  query: string;
  candidates: SampleResult[];
  winner: SampleResult | null;
  totalMs: number;
};

const DEMO_QUERIES = [
  "find all files that match a shell glob pattern",
  "count lines in a file, skipping blank lines",
  "parse a JSON array and sum a numeric field",
];

function CandidateCard({ r, isWinner }: { r: SampleResult; isWinner: boolean }) {
  const [expanded, setExpanded] = useState(isWinner);
  return (
    <div
      className="rounded-xl border overflow-hidden transition-all"
      style={{
        borderColor: isWinner ? "#34d39960" : r.verdict === "FAIL" ? "rgba(248,113,113,0.2)" : "rgba(255,255,255,0.08)",
        background: isWinner ? "rgba(52,211,153,0.06)" : "rgba(0,0,0,0.3)",
      }}
    >
      <button onClick={() => setExpanded((e) => !e)} className="w-full flex items-center gap-3 px-3 py-2.5 text-left">
        <div className="flex h-5 w-5 shrink-0 items-center justify-center rounded text-[9px] font-black"
          style={{
            background: r.verdict === "PASS" ? "rgba(52,211,153,0.15)" : "rgba(248,113,113,0.15)",
            color: r.verdict === "PASS" ? "#34d399" : "#f87171",
          }}>
          {r.attempt}
        </div>
        <span className={`flex items-center gap-1 text-[9px] font-bold ${r.verdict === "PASS" ? "text-emerald-400" : "text-red-400"}`}>
          {r.verdict === "PASS" ? <CheckCircle2 size={10} /> : <XCircle size={10} />}
          {r.verdict}
        </span>
        <span className="text-[8px] font-mono text-gray-700">{r.duration}ms</span>
        {isWinner && (
          <span className="ml-auto text-[8px] font-black text-emerald-400 uppercase tracking-widest">Winner</span>
        )}
      </button>
      {expanded && (
        <div className="border-t border-white/5 bg-black/40 p-3">
          <pre className="text-[10px] font-mono text-emerald-300/80 leading-relaxed overflow-x-auto no-scrollbar whitespace-pre-wrap">{r.code}</pre>
        </div>
      )}
    </div>
  );
}

export function VerifiedSearch() {
  const [query, setQuery] = useState("");
  const [searching, setSearching] = useState(false);
  const [result, setResult] = useState<SearchResult | null>(null);
  const [error, setError] = useState<string | null>(null);
  const [elapsedMs, setElapsedMs] = useState(0);
  const intervalRef = useRef<ReturnType<typeof setInterval> | null>(null);
  const tauriMode = isTauri();

  const runSearch = async () => {
    if (!query.trim() || searching) return;
    setSearching(true);
    setResult(null);
    setError(null);
    setElapsedMs(0);

    const start = Date.now();
    intervalRef.current = setInterval(() => setElapsedMs(Date.now() - start), 100);

    try {
      const res = await invokeSafe<SearchResult>("verified_search", { query });
      if (!res) {
        setError(
          tauriMode
            ? "Verified Search backend is not registered in the desktop runtime."
            : "Verified Search requires the Tauri desktop runtime or the local IDE HTTP bridge."
        );
      } else {
        setResult(res);
      }
    } catch (e) {
      setError(e instanceof Error ? e.message : "Verified Search backend call failed.");
    } finally {
      if (intervalRef.current) clearInterval(intervalRef.current);
      setSearching(false);
    }
  };

  return (
    <div className="relative flex h-full min-h-0 flex-col overflow-hidden p-5">
      <div className="pointer-events-none absolute inset-0 opacity-8">
        <div className="absolute right-0 bottom-0 h-[400px] w-[400px] translate-x-1/3 translate-y-1/3 rounded-full"
          style={{ background: "#60a5fa", filter: "blur(100px)" }} />
      </div>

      <div className="relative z-10 flex min-h-0 flex-1 flex-col gap-4">
        {/* Header */}
        <div className="border-b border-white/10 pb-4">
          <div className="flex items-center gap-2 text-[10px] font-black uppercase tracking-widest text-blue-400 mb-2">
            <Search size={13} /> Verified Search
          </div>
          <h2 className="text-[26px] font-black leading-tight text-[var(--determinex-text)]"
            style={{ fontFamily: "var(--determinex-font-display)" }}>
            Oracle Search
          </h2>
          <p className="text-[10px] text-gray-600 font-mono mt-1">
            Describe what you want. K candidates sampled, then oracle-verified before you see it.
          </p>
        </div>

        {/* Search input */}
        <div className="flex gap-2 shrink-0">
          <div className="relative flex-1">
            <Search size={13} className="absolute left-3.5 top-1/2 -translate-y-1/2 text-gray-600" />
            <input
              value={query}
              onChange={(e) => setQuery(e.target.value)}
              onKeyDown={(e) => e.key === "Enter" && runSearch()}
              placeholder="Describe code you need..."
              className="w-full rounded-xl border border-white/10 bg-black/40 py-3 pl-10 pr-4 text-[12px] text-white/80 placeholder:text-gray-700 outline-none focus:border-[var(--determinex-accent)]/40 transition-colors"
            />
          </div>
          <button
            onClick={runSearch}
            disabled={searching || !query.trim()}
            className="flex items-center gap-2 rounded-xl border border-[var(--determinex-accent)]/40 bg-[var(--determinex-accent)]/10 px-4 py-3 text-[11px] font-black uppercase tracking-widest text-[var(--determinex-accent)] transition-all hover:bg-[var(--determinex-accent)]/20 disabled:opacity-40"
          >
            {searching ? <Clock size={14} className="animate-spin" /> : <Zap size={14} />}
            {searching ? `${(elapsedMs / 1000).toFixed(1)}s` : "Search"}
          </button>
        </div>

        {/* Demo queries */}
        {!result && !searching && !error && (
          <div className="space-y-1.5 shrink-0">
            <div className="text-[8px] uppercase font-bold tracking-widest text-gray-700 mb-2">Try a query</div>
            {DEMO_QUERIES.map((q) => (
              <button
                key={q}
                onClick={() => { setQuery(q); }}
                className="group w-full flex items-center gap-2 rounded-xl border border-white/5 bg-white/[0.02] px-3 py-2.5 text-left transition-all hover:border-white/10 hover:bg-white/[0.04]"
              >
                <ArrowRight size={11} className="text-gray-700 group-hover:text-[var(--determinex-accent)] transition-colors shrink-0" />
                <span className="text-[10px] font-mono text-gray-500 group-hover:text-gray-300 transition-colors">{q}</span>
              </button>
            ))}
          </div>
        )}

        {error && !searching && (
          <div className="rounded-xl border border-amber-500/20 bg-amber-950/10 px-4 py-3 text-[10px] text-amber-200/80 font-mono shrink-0">
            <div className="mb-1 flex items-center gap-2 text-[9px] font-black uppercase tracking-widest text-amber-300">
              <XCircle size={11} /> Backend unavailable
            </div>
            {error}
          </div>
        )}

        {/* Searching state */}
        {searching && (
          <div className="flex-1 flex flex-col items-center justify-center gap-4">
            <div className="relative h-20 w-20">
              {[0, 1, 2, 3, 4, 5].map((i) => (
                <div
                  key={i}
                  className="absolute inset-0 rounded-full border border-[var(--determinex-accent)]/30 animate-ping"
                  style={{ animationDelay: `${i * 0.2}s`, animationDuration: "1.5s" }}
                />
              ))}
              <div className="absolute inset-0 flex items-center justify-center">
                <Zap size={24} className="text-[var(--determinex-accent)] animate-pulse" />
              </div>
            </div>
            <div className="text-center">
              <div className="text-[12px] font-bold text-white/60">Waiting for verifier backend...</div>
              <div className="text-[10px] text-gray-700 font-mono mt-1">Oracle verifying each before showing you</div>
            </div>
          </div>
        )}

        {/* Results */}
        {result && !searching && (
          <div className="flex-1 min-h-0 overflow-y-auto no-scrollbar space-y-3">
            {/* Summary */}
            <div className="flex items-center justify-between rounded-xl border border-white/8 bg-black/30 px-4 py-3 shrink-0">
              <div className="text-[10px] font-bold text-white/60">
                {result.candidates.filter((c) => c.verdict === "PASS").length}/{result.candidates.length} candidates passed
              </div>
              <div className="text-[10px] font-mono text-gray-700">{(result.totalMs / 1000).toFixed(2)}s total</div>
            </div>

            {/* Winner first */}
            {result.winner && (
              <div>
                <div className="text-[8px] uppercase font-bold tracking-widest text-emerald-400 mb-1.5 flex items-center gap-1.5">
                  <CheckCircle2 size={9} /> Verified solution
                </div>
                <CandidateCard r={result.winner} isWinner />
              </div>
            )}

            {/* All attempts */}
            <div>
              <div className="text-[8px] uppercase font-bold tracking-widest text-gray-600 mb-1.5">All attempts</div>
              <div className="space-y-1.5">
                {result.candidates.filter((c) => c !== result.winner).map((c) => (
                  <CandidateCard key={c.attempt} r={c} isWinner={false} />
                ))}
              </div>
            </div>
          </div>
        )}

        {!tauriMode && (
          <div className="rounded-xl border border-white/5 bg-white/[0.02] px-3 py-2 text-[9px] text-gray-700 font-mono text-center shrink-0">
            Browser mode: results appear only when the local IDE HTTP bridge returns a real verifier response.
          </div>
        )}
      </div>
    </div>
  );
}
