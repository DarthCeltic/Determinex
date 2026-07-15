"use client";
import { useState } from "react";
import { Eye, EyeOff, Plus, Trash2, AlertTriangle, Copy, Check } from "lucide-react";

type EnvVar = { key: string; value: string; masked: boolean; sensitive: boolean; profile: string };

const PROFILES = ["dev", "staging", "prod"] as const;
type Profile = typeof PROFILES[number];

const INITIAL_VARS: EnvVar[] = [];

export function EnvManager() {
  const [profile, setProfile] = useState<Profile>("dev");
  const [revealed, setRevealed] = useState<Set<string>>(new Set());
  const [copied, setCopied] = useState<string | null>(null);
  const [showAdd, setShowAdd] = useState(false);
  const [newKey, setNewKey] = useState("");
  const [newVal, setNewVal] = useState("");
  const [vars, setVars] = useState<EnvVar[]>(INITIAL_VARS);

  const profileVars = vars.filter((v) => v.profile === profile);
  const sensitiveCount = profileVars.filter((v) => v.sensitive).length;

  const toggleReveal = (key: string) => setRevealed((s) => { const n = new Set(s); n.has(key) ? n.delete(key) : n.add(key); return n; });

  const copy = (val: string, key: string) => {
    navigator.clipboard.writeText(val).catch(() => {});
    setCopied(key);
    setTimeout(() => setCopied(null), 1500);
  };

  const remove = (key: string) => setVars((v) => v.filter((e) => !(e.key === key && e.profile === profile)));

  const add = () => {
    if (!newKey.trim()) return;
    const sensitive = newKey.toLowerCase().includes("key") || newKey.toLowerCase().includes("secret") || newKey.toLowerCase().includes("token");
    setVars((v) => [...v, { key: newKey.trim(), value: newVal, masked: sensitive, sensitive, profile }]);
    setNewKey(""); setNewVal(""); setShowAdd(false);
  };

  return (
    <div className="flex h-full flex-col overflow-hidden">
      {/* Profile selector */}
      <div className="shrink-0 flex items-center gap-2 border-b px-4 py-2.5" style={{ borderColor: "var(--determinex-border)", background: "rgba(0,0,0,0.2)" }}>
        <span className="text-[9px] uppercase font-black tracking-widest text-gray-600 mr-1">Profile</span>
        {PROFILES.map((p) => (
          <button key={p} onClick={() => setProfile(p)}
            className={`rounded-lg px-3 py-1 text-[9px] font-bold uppercase tracking-widest transition-all ${profile === p ? "bg-[var(--determinex-accent)] text-black" : "border border-white/8 text-gray-600 hover:text-gray-300"}`}>
            {p}
          </button>
        ))}
        <button onClick={() => setShowAdd((v) => !v)} className="ml-auto flex items-center gap-1 text-gray-600 hover:text-gray-300 transition-colors text-[9px]">
          <Plus size={11} /> Add
        </button>
      </div>

      {sensitiveCount > 0 && (
        <div className="shrink-0 flex items-center gap-2 px-4 py-2 border-b border-amber-500/15 bg-amber-950/10">
          <AlertTriangle size={11} className="text-amber-400 shrink-0" />
          <p className="text-[9px] text-amber-400/80">{sensitiveCount} sensitive variables -- values masked. Secret hygiene enforced by pre-commit hook.</p>
        </div>
      )}

      {showAdd && (
        <div className="shrink-0 flex flex-col gap-2 border-b px-4 py-3" style={{ borderColor: "var(--determinex-border)", background: "rgba(0,0,0,0.3)" }}>
          <div className="flex gap-2">
            <input value={newKey} onChange={(e) => setNewKey(e.target.value)} placeholder="KEY_NAME"
              className="flex-1 rounded-lg border border-white/8 bg-black/30 px-3 py-1.5 text-[10px] font-mono uppercase placeholder:text-gray-700 text-white/70 outline-none focus:border-[var(--determinex-accent)]/30" />
            <input value={newVal} onChange={(e) => setNewVal(e.target.value)} placeholder="value"
              onKeyDown={(e) => e.key === "Enter" && add()}
              className="flex-1 rounded-lg border border-white/8 bg-black/30 px-3 py-1.5 text-[10px] font-mono placeholder:text-gray-700 text-white/70 outline-none focus:border-[var(--determinex-accent)]/30" />
          </div>
          <div className="flex gap-2">
            <button onClick={add} className="flex-1 rounded-lg py-1.5 text-[10px] font-bold text-black" style={{ background: "var(--determinex-accent)" }}>Save</button>
            <button onClick={() => setShowAdd(false)} className="rounded-lg border border-white/8 px-3 text-[10px] text-gray-500 hover:text-gray-300">Cancel</button>
          </div>
        </div>
      )}

      <div className="flex-1 overflow-y-auto no-scrollbar divide-y divide-white/[0.03]">
        {profileVars.map((v) => {
          const isRevealed = revealed.has(v.key);
          const display = v.sensitive && !isRevealed ? "****" + v.value.slice(-4) : v.value;
          return (
            <div key={v.key} className="group flex items-center gap-3 px-4 py-2.5 hover:bg-white/[0.02] transition-colors">
              <div className="flex-1 min-w-0">
                <div className="text-[10px] font-mono font-bold text-white/70">{v.key}</div>
                <div className={`text-[9px] font-mono mt-0.5 ${v.sensitive && !isRevealed ? "text-gray-700 tracking-widest" : "text-gray-500"} truncate`}>{display}</div>
              </div>
              <div className="flex items-center gap-1 shrink-0 opacity-0 group-hover:opacity-100 transition-opacity">
                {v.sensitive && (
                  <button onClick={() => toggleReveal(v.key)} className="p-1.5 text-gray-600 hover:text-gray-300 rounded transition-colors">
                    {isRevealed ? <EyeOff size={11} /> : <Eye size={11} />}
                  </button>
                )}
                <button onClick={() => copy(v.value, v.key)} className="p-1.5 text-gray-600 hover:text-gray-300 rounded transition-colors">
                  {copied === v.key ? <Check size={11} className="text-emerald-400" /> : <Copy size={11} />}
                </button>
                <button onClick={() => remove(v.key)} className="p-1.5 text-gray-600 hover:text-red-400 rounded transition-colors">
                  <Trash2 size={11} />
                </button>
              </div>
            </div>
          );
        })}
        {profileVars.length === 0 && (
          <div className="flex flex-col items-center justify-center gap-1 py-16 opacity-40">
            <p className="text-[11px] text-gray-500">No live variables loaded for {profile}</p>
            <p className="max-w-[260px] text-center text-[9px] text-gray-700">
              Added values stay in this session until a secure environment collector is wired.
            </p>
          </div>
        )}
      </div>
    </div>
  );
}
