"use client";
import { useState } from "react";
import { Save, RotateCcw } from "lucide-react";

type Lang = "rust" | "go" | "python" | "typescript";

type Config = {
  rust:       { profile: string; features: string[]; toolchain: string; target: string; extraArgs: string };
  go:         { ldflags: string; cgoEnabled: boolean; goVersion: string; buildTags: string };
  python:     { pythonVersion: string; venv: string; extraPyArgs: string };
  typescript: { tsconfig: string; strict: boolean; noEmit: boolean; target: string };
};

const DEFAULT: Config = {
  rust:       { profile:"debug", features:["async","tokio"], toolchain:"stable", target:"x86_64-pc-windows-msvc", extraArgs:"" },
  go:         { ldflags:"-s -w", cgoEnabled:false, goVersion:"1.22", buildTags:"" },
  python:     { pythonVersion:"3.11", venv:".venv", extraPyArgs:"" },
  typescript: { tsconfig:"tsconfig.json", strict:true, noEmit:false, target:"ES2022" },
};

const RUST_FEATURES = ["async","tokio","serde","clap","tracing","mimalloc","jemalloc","rayon"];
const TS_TARGETS = ["ES2015","ES2017","ES2020","ES2022","ESNext"];

export function BuildConfig() {
  const [lang, setLang] = useState<Lang>("rust");
  const [cfg, setCfg] = useState<Config>(DEFAULT);
  const [saved, setSaved] = useState(false);

  const save = () => { setSaved(true); setTimeout(() => setSaved(false), 1500); };
  const reset = () => setCfg(DEFAULT);

  const setRust  = (k: keyof Config["rust"], v: any)       => setCfg((c) => ({ ...c, rust:       { ...c.rust,       [k]: v } }));
  const setGo    = (k: keyof Config["go"], v: any)         => setCfg((c) => ({ ...c, go:         { ...c.go,         [k]: v } }));
  const setTs    = (k: keyof Config["typescript"], v: any) => setCfg((c) => ({ ...c, typescript: { ...c.typescript, [k]: v } }));
  const setPy    = (k: keyof Config["python"], v: any)     => setCfg((c) => ({ ...c, python:     { ...c.python,     [k]: v } }));

  const toggleFeature = (f: string) => setRust("features", cfg.rust.features.includes(f) ? cfg.rust.features.filter((x) => x !== f) : [...cfg.rust.features, f]);

  const LANGS: { id: Lang; label: string }[] = [
    { id:"rust", label:"Rust" }, { id:"go", label:"Go" }, { id:"python", label:"Python" }, { id:"typescript", label:"TypeScript" },
  ];

  const Field = ({ label, children }: { label: string; children: React.ReactNode }) => (
    <div className="flex flex-col gap-1.5">
      <label className="text-[9px] uppercase font-black tracking-widest text-gray-600">{label}</label>
      {children}
    </div>
  );

  const Input = ({ value, onChange, ...rest }: { value: string; onChange: (v: string) => void; placeholder?: string }) => (
    <input value={value} onChange={(e) => onChange(e.target.value)} {...rest}
      className="rounded-lg border border-white/8 bg-black/30 px-3 py-2 text-[10px] font-mono text-white/70 placeholder:text-gray-700 outline-none focus:border-[var(--determinex-accent)]/30 transition-colors" />
  );

  const Select = ({ value, onChange, options }: { value: string; onChange: (v: string) => void; options: string[] }) => (
    <select value={value} onChange={(e) => onChange(e.target.value)}
      className="rounded-lg border border-white/8 bg-black/30 px-3 py-2 text-[10px] font-mono text-white/70 outline-none focus:border-[var(--determinex-accent)]/30 transition-colors">
      {options.map((o) => <option key={o} value={o}>{o}</option>)}
    </select>
  );

  const Toggle = ({ checked, onChange, label }: { checked: boolean; onChange: (v: boolean) => void; label: string }) => (
    <label className="flex items-center gap-2.5 cursor-pointer">
      <div onClick={() => onChange(!checked)}
        className={`relative h-4 w-7 rounded-full transition-colors ${checked ? "bg-[var(--determinex-accent)]" : "bg-white/10"}`}>
        <div className={`absolute top-0.5 h-3 w-3 rounded-full bg-white transition-all ${checked ? "left-3.5" : "left-0.5"}`} />
      </div>
      <span className="text-[10px] text-gray-400">{label}</span>
    </label>
  );

  return (
    <div className="flex h-full flex-col overflow-hidden">
      <div className="shrink-0 flex items-center gap-1 border-b px-4 pt-2" style={{ borderColor: "var(--determinex-border)", background: "rgba(0,0,0,0.2)" }}>
        {LANGS.map(({ id, label }) => (
          <button key={id} onClick={() => setLang(id)}
            className={`border-b-2 px-4 py-2 text-[9px] font-black uppercase tracking-widest transition-all ${lang === id ? "border-[var(--determinex-accent)] text-[var(--determinex-accent)]" : "border-transparent text-gray-600 hover:text-gray-400"}`}>
            {label}
          </button>
        ))}
        <div className="ml-auto flex gap-2 mb-1">
          <button onClick={reset} className="flex items-center gap-1 text-[9px] text-gray-600 hover:text-gray-400 transition-colors"><RotateCcw size={10} /> Reset</button>
          <button onClick={save} className={`flex items-center gap-1.5 rounded-lg px-3 py-1 text-[9px] font-bold transition-all ${saved ? "bg-emerald-500/20 text-emerald-400 border border-emerald-500/30" : "border border-white/8 text-gray-500 hover:text-gray-300"}`}>
            <Save size={10} /> {saved ? "Saved" : "Save"}
          </button>
        </div>
      </div>

      <div className="flex-1 overflow-y-auto no-scrollbar p-6 space-y-5">
        {lang === "rust" && (<>
          <Field label="Build Profile"><Select value={cfg.rust.profile} onChange={(v) => setRust("profile", v)} options={["debug","release","bench","test"]} /></Field>
          <Field label="Toolchain"><Select value={cfg.rust.toolchain} onChange={(v) => setRust("toolchain", v)} options={["stable","nightly","beta"]} /></Field>
          <Field label="Target"><Input value={cfg.rust.target} onChange={(v) => setRust("target", v)} placeholder="x86_64-pc-windows-msvc" /></Field>
          <Field label="Feature Flags">
            <div className="flex flex-wrap gap-2">
              {RUST_FEATURES.map((f) => (
                <button key={f} onClick={() => toggleFeature(f)}
                  className={`rounded-lg border px-2.5 py-1 text-[9px] font-mono transition-all ${cfg.rust.features.includes(f) ? "border-[var(--determinex-accent)]/40 bg-[var(--determinex-accent)]/10 text-[var(--determinex-accent)]" : "border-white/8 text-gray-600 hover:text-gray-400"}`}>
                  {f}
                </button>
              ))}
            </div>
          </Field>
          <Field label="Extra Args"><Input value={cfg.rust.extraArgs} onChange={(v) => setRust("extraArgs", v)} placeholder="-- --nocapture" /></Field>
        </>)}

        {lang === "go" && (<>
          <Field label="Go Version"><Input value={cfg.go.goVersion} onChange={(v) => setGo("goVersion", v)} placeholder="1.22" /></Field>
          <Field label="LD Flags"><Input value={cfg.go.ldflags} onChange={(v) => setGo("ldflags", v)} placeholder="-s -w" /></Field>
          <Field label="Build Tags"><Input value={cfg.go.buildTags} onChange={(v) => setGo("buildTags", v)} placeholder="integration" /></Field>
          <Toggle checked={cfg.go.cgoEnabled} onChange={(v) => setGo("cgoEnabled", v)} label="CGO Enabled" />
        </>)}

        {lang === "python" && (<>
          <Field label="Python Version"><Select value={cfg.python.pythonVersion} onChange={(v) => setPy("pythonVersion", v)} options={["3.11","3.12","3.13"]} /></Field>
          <Field label="Virtual Env Path"><Input value={cfg.python.venv} onChange={(v) => setPy("venv", v)} placeholder=".venv" /></Field>
          <Field label="Extra pytest Args"><Input value={cfg.python.extraPyArgs} onChange={(v) => setPy("extraPyArgs", v)} placeholder="-x -v --tb=short" /></Field>
        </>)}

        {lang === "typescript" && (<>
          <Field label="tsconfig"><Input value={cfg.typescript.tsconfig} onChange={(v) => setTs("tsconfig", v)} placeholder="tsconfig.json" /></Field>
          <Field label="Target"><Select value={cfg.typescript.target} onChange={(v) => setTs("target", v)} options={TS_TARGETS} /></Field>
          <Toggle checked={cfg.typescript.strict} onChange={(v) => setTs("strict", v)} label="Strict mode" />
          <Toggle checked={cfg.typescript.noEmit} onChange={(v) => setTs("noEmit", v)} label="noEmit (type-check only)" />
        </>)}
      </div>
    </div>
  );
}
