"use client";
import { useState } from "react";
import { Check, X, ChevronDown, GitBranch, FileCode } from "lucide-react";

type DiffLine = { type: "add" | "remove" | "context" | "header"; content: string; lineOld?: number; lineNew?: number };
type Patch = { id: string; title: string; file: string; summary: string; lines: DiffLine[] };

const PATCHES: Patch[] = [
  {
    id:"p1",
    title:"Oracle fix: mismatched types in lib.rs",
    file:"src/lib.rs",
    summary:"Attempt 2/5 -- converts &str to String to satisfy function signature",
    lines:[
      { type:"header",  content:"@@ -24,8 +24,8 @@ pub fn process(input: &str) -> Result<String>" },
      { type:"context", content:"    let config = Config::default();",         lineOld:24, lineNew:24 },
      { type:"context", content:"    let parser = Parser::new(&config);",      lineOld:25, lineNew:25 },
      { type:"context", content:"    ",                                         lineOld:26, lineNew:26 },
      { type:"remove",  content:"-   let result = parser.parse(input);",       lineOld:27             },
      { type:"add",     content:"+   let result = parser.parse(input.to_owned());", lineNew:27         },
      { type:"context", content:"    ",                                         lineOld:28, lineNew:28 },
      { type:"context", content:"    Ok(result)",                               lineOld:29, lineNew:29 },
      { type:"context", content:"}",                                            lineOld:30, lineNew:30 },
    ],
  },
  {
    id:"p2",
    title:"keifu: remove TUI collection filter",
    file:"compile.sh",
    summary:"Remove collect_ignore_glob blocking TUI tests -- keifu v3 fix",
    lines:[
      { type:"header",  content:"@@ -18,12 +18,6 @@ def pytest_configure(config):" },
      { type:"context", content:"    config.addinivalue_line('markers', 'slow: slow tests')", lineOld:18, lineNew:18 },
      { type:"context", content:"",                                                             lineOld:19, lineNew:19 },
      { type:"remove",  content:"-collect_ignore_glob = [",                                    lineOld:20 },
      { type:"remove",  content:'-    "test_tui*.py",',                                        lineOld:21 },
      { type:"remove",  content:'-    "test_tmux*.py",',                                       lineOld:22 },
      { type:"remove",  content:"-]",                                                          lineOld:23 },
      { type:"remove",  content:"",                                                             lineOld:24 },
      { type:"context", content:"def pytest_runtest_setup(item):",                             lineOld:25, lineNew:20 },
      { type:"context", content:"    pass",                                                    lineOld:26, lineNew:21 },
    ],
  },
  {
    id:"p3",
    title:"Cloak: fix paren-stripped anchor matching",
    file:"scripts/privacy_cloak/patcher.py",
    summary:"Strip everything after '(' before comparing anchors -- fixes fastlane-19207",
    lines:[
      { type:"header",  content:"@@ -301,6 +301,9 @@ def _find_anchor(source_lines, anchor):" },
      { type:"context", content:"    for i, line in enumerate(source_lines):",  lineOld:301, lineNew:301 },
      { type:"context", content:"        stripped = line.strip()",             lineOld:302, lineNew:302 },
      { type:"add",     content:"+       # strip params before comparing -- model may write def foo(a,b) but source has def foo", lineNew:303 },
      { type:"add",     content:"+       anchor_base = anchor.split('(')[0].rstrip()",  lineNew:304 },
      { type:"add",     content:"+       stripped_base = stripped.split('(')[0].rstrip()", lineNew:305 },
      { type:"remove",  content:"-       if anchor in stripped:",               lineOld:303 },
      { type:"add",     content:"+       if anchor_base in stripped_base:",     lineNew:306 },
      { type:"context", content:"            return i",                         lineOld:304, lineNew:307 },
      { type:"context", content:"    return -1",                                lineOld:305, lineNew:308 },
    ],
  },
];

const LINE_STYLES: Record<DiffLine["type"], string> = {
  add:     "bg-emerald-950/25 text-emerald-300 border-l-2 border-emerald-500/40",
  remove:  "bg-red-950/25 text-red-300 border-l-2 border-red-500/40",
  context: "text-gray-500",
  header:  "text-cyan-600/70 bg-black/20",
};

export function DiffViewer() {
  const [selected, setSelected] = useState("p1");
  const [approved, setApproved] = useState<Set<string>>(new Set());
  const [rejected, setRejected] = useState<Set<string>>(new Set());

  const patch = PATCHES.find((p) => p.id === selected)!;
  const isApproved = approved.has(selected);
  const isRejected = rejected.has(selected);

  const approve = () => { setApproved((s) => new Set([...s, selected])); setRejected((s) => { const n = new Set(s); n.delete(selected); return n; }); };
  const reject  = () => { setRejected((s) => new Set([...s, selected])); setApproved((s) => { const n = new Set(s); n.delete(selected); return n; }); };

  const adds    = patch.lines.filter((l) => l.type === "add").length;
  const removes = patch.lines.filter((l) => l.type === "remove").length;

  return (
    <div className="flex h-full flex-col overflow-hidden">
      {/* Patch selector */}
      <div className="shrink-0 border-b px-4 py-2" style={{ borderColor: "var(--determinex-border)", background: "rgba(0,0,0,0.2)" }}>
        <div className="flex items-center gap-2 text-[9px] uppercase font-black tracking-widest text-gray-600 mb-2">
          <GitBranch size={10} /> Oracle Patches
        </div>
        <div className="flex flex-col gap-1">
          {PATCHES.map((p) => (
            <button key={p.id} onClick={() => setSelected(p.id)}
              className={`flex items-center gap-2.5 rounded-xl border px-3 py-2 text-left transition-all ${selected === p.id ? "border-[var(--determinex-accent)]/30 bg-[var(--determinex-accent)]/5" : "border-white/5 hover:bg-white/[0.02]"}`}>
              <FileCode size={11} className="text-gray-600 shrink-0" />
              <span className="text-[10px] font-semibold text-white/70 flex-1 truncate">{p.title}</span>
              {approved.has(p.id) && <Check size={11} className="text-emerald-400 shrink-0" />}
              {rejected.has(p.id) && <X size={11} className="text-red-400 shrink-0" />}
            </button>
          ))}
        </div>
      </div>

      {/* Diff header */}
      <div className="shrink-0 flex items-center gap-3 border-b px-4 py-2.5" style={{ borderColor: "var(--determinex-border)" }}>
        <span className="text-[10px] font-mono text-gray-500 flex-1 truncate">{patch.file}</span>
        <span className="text-[9px] text-emerald-400 font-mono">+{adds}</span>
        <span className="text-[9px] text-red-400 font-mono">-{removes}</span>
        <div className="flex gap-2 ml-2">
          <button onClick={reject}
            className={`flex items-center gap-1 rounded-lg border px-2.5 py-1 text-[9px] font-bold transition-all ${isRejected ? "border-red-500/50 bg-red-950/30 text-red-300" : "border-white/8 text-gray-600 hover:border-red-500/30 hover:text-red-400"}`}>
            <X size={10} /> Reject
          </button>
          <button onClick={approve}
            className={`flex items-center gap-1 rounded-lg border px-2.5 py-1 text-[9px] font-bold transition-all ${isApproved ? "border-emerald-500/50 bg-emerald-950/30 text-emerald-300" : "border-white/8 text-gray-600 hover:border-emerald-500/30 hover:text-emerald-400"}`}>
            <Check size={10} /> Approve
          </button>
        </div>
      </div>

      {/* Diff body */}
      <div className="flex-1 overflow-y-auto no-scrollbar">
        <div className="text-[9px] text-gray-600 italic px-4 py-2 border-b border-white/[0.03] bg-black/10">{patch.summary}</div>
        <div className="divide-y divide-white/[0.02]">
          {patch.lines.map((line, i) => (
            <div key={i} className={`flex gap-0 ${LINE_STYLES[line.type]}`}>
              <div className="w-8 shrink-0 text-[8px] font-mono text-gray-800 text-right pr-2 py-1 select-none">
                {line.lineOld ?? ""}
              </div>
              <div className="w-8 shrink-0 text-[8px] font-mono text-gray-800 text-right pr-2 py-1 select-none">
                {line.lineNew ?? ""}
              </div>
              <pre className="flex-1 min-w-0 py-1 px-2 text-[10px] font-mono overflow-x-auto whitespace-pre">{line.content}</pre>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}
