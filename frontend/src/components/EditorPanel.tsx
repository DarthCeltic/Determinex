"use client";
import { useState, useCallback, useEffect } from "react";
import { FileCode, FolderOpen, Check, X, ChevronRight, Plus, Save, Columns, Trash, AlertTriangle, List } from "lucide-react";
import { isTauri, readFileContent, invokeSafe } from "@/lib/api";
import { getLspDiagnostics, getLspSymbols, LspDiagnostic, LspSymbol } from "@/lib/lspService";
import dynamic from "next/dynamic";

const MonacoEditor = dynamic(() => import("@monaco-editor/react").then((m) => m.default), {
  ssr: false,
  loading: () => (
    <div className="flex-1 flex items-center justify-center bg-[#0d1117]">
      <span className="text-[11px] font-mono text-gray-700">Loading editor…</span>
    </div>
  ),
});

type OpenFile = { name: string; path: string; content: string; dirty: boolean; lang: string };

const LANG_MAP: Record<string, string> = {
  py: "python", rs: "rust", ts: "typescript", tsx: "typescript",
  js: "javascript", jsx: "javascript", go: "go", toml: "toml",
  json: "json", md: "markdown", sh: "shell", css: "css",
};

const DEFAULT_DEMO_FILES: OpenFile[] = [
  {
    name: "hive.py", path: "scripts/hive.py", dirty: false, lang: "python",
    content: `# Determinex Hive Mind Orchestrator
# Core pipeline: new-session → generate-dag → run-session

from typing import Optional
from oracle import CompilerOracle
from rosetta import RosettaProjector

class HiveMindOrchestrator:
    """Main orchestrator — DAG planning + Builder execution + Oracle gate."""

    def __init__(self, model_config: dict, oracle: CompilerOracle):
        self.oracle = oracle
        self.rosetta = RosettaProjector()
        self.model_config = model_config

    def new_session(self, spec: str, lang: str) -> str:
        """Create a new build session from a spec file."""
        session_id = self._generate_session_id()
        self._write_wal_record(session_id, {"spec": spec, "lang": lang})
        return session_id

    def generate_dag(self, session_id: str) -> list[dict]:
        """Architect produces a DAG of ordered build steps."""
        spec = self._load_session_spec(session_id)
        dag = self._architect_call(spec)
        return dag

    def run_session(self, session_id: str) -> dict:
        """Execute DAG — Builder → Oracle → retry loop (max 5×)."""
        dag = self.generate_dag(session_id)
        results = []
        for step in dag:
            result = self._execute_step(session_id, step)
            results.append(result)
            if result["verdict"] == "PASS":
                self._write_wal_record(session_id, result)
        return {"session_id": session_id, "steps": results}
`,
  },
  {
    name: "HealthMap.tsx", path: "frontend/src/components/HealthMap.tsx", dirty: false, lang: "typescript",
    content: `// Project Health Map — real-time oracle status per file
// Shows compile errors, warnings, and passing state across the whole project
"use client";
import { useState } from "react";

type FileHealth = {
  path: string;
  status: "pass" | "warn" | "error";
  errors: number;
  warnings: number;
};
`,
  },
];

function FileBadge({ name, dirty, active, onClose, onClick }: {
  name: string; dirty: boolean; active: boolean;
  onClose: (e: React.MouseEvent) => void; onClick: () => void;
}) {
  return (
    <button
      onClick={onClick}
      className="group flex items-center gap-2 px-3 py-1.5 border-r border-white/5 transition-all text-left shrink-0"
      style={{ background: active ? "rgba(255,255,255,0.06)" : "transparent" }}
    >
      <span className={`text-[10px] font-mono ${active ? "text-white/80" : "text-gray-500 group-hover:text-gray-300"}`}>
        {name}
      </span>
      {dirty && <span className="h-1.5 w-1.5 rounded-full bg-amber-400 shrink-0" />}
      <span
        onClick={onClose}
        className="text-gray-700 hover:text-white transition-colors shrink-0 hidden group-hover:block"
      >
        <X size={10} />
      </span>
    </button>
  );
}

export function EditorPanel() {
  const [openFiles, setOpenFiles] = useState<OpenFile[]>(() => {
    if (typeof window !== "undefined") {
      const saved = localStorage.getItem("determinex_editor_tabs");
      if (saved) {
        try { return JSON.parse(saved); } catch (e) {}
      }
    }
    return DEFAULT_DEMO_FILES;
  });
  const [activeIdx, setActiveIdx] = useState(0);
  const [rightActiveIdx, setRightActiveIdx] = useState(1);
  const [saving, setSaving] = useState(false);
  const [isSplit, setIsSplit] = useState(false);
  const [closedTabs, setClosedTabs] = useState<OpenFile[]>([]);
  const [diagnostics, setDiagnostics] = useState<LspDiagnostic[]>([]);
  const [symbols, setSymbols] = useState<LspSymbol[]>([]);
  const [showOutline, setShowOutline] = useState(false);
  const [editorRef, setEditorRef] = useState<any>(null);
  const tauriMode = isTauri();

  const activeFile = openFiles[activeIdx];
  const rightActiveFile = openFiles[rightActiveIdx] || openFiles[0];

  // Load diagnostics and symbols
  useEffect(() => {
    if (!activeFile) return;
    getLspDiagnostics(activeFile.name).then(setDiagnostics);
    getLspSymbols(activeFile.name).then(setSymbols);
  }, [activeFile?.name]);

  // Set editor markers when diagnostics or editorRef changes
  useEffect(() => {
    if (!editorRef || !activeFile) return;
    const monaco = (window as any).monaco;
    if (monaco) {
      const markers = diagnostics.map(d => ({
        startLineNumber: d.line,
        startColumn: d.column,
        endLineNumber: d.line,
        endColumn: d.column + 10,
        message: d.message,
        severity: d.severity === "error" ? monaco.MarkerSeverity.Error : monaco.MarkerSeverity.Warning
      }));
      monaco.editor.setModelMarkers(editorRef.getModel(), "owner", markers);
    }
  }, [diagnostics, editorRef, activeFile]);

  // Tab Persistence
  useEffect(() => {
    localStorage.setItem("determinex_editor_tabs", JSON.stringify(openFiles));
  }, [openFiles]);

  // Handle Ctrl+Shift+T tab restoration
  useEffect(() => {
    const handleKeyDown = (e: KeyboardEvent) => {
      if (e.ctrlKey && e.shiftKey && e.key.toLowerCase() === "t") {
        e.preventDefault();
        if (closedTabs.length > 0) {
          const restored = closedTabs[closedTabs.length - 1];
          setOpenFiles((prev) => {
            if (prev.some((f) => f.path === restored.path)) return prev;
            return [...prev, restored];
          });
          setClosedTabs((prev) => prev.slice(0, -1));
          setActiveIdx(openFiles.length);
        }
      }
    };
    window.addEventListener("keydown", handleKeyDown);
    return () => window.removeEventListener("keydown", handleKeyDown);
  }, [closedTabs, openFiles]);

  const handleChange = useCallback((value: string | undefined) => {
    if (value === undefined) return;
    setOpenFiles((prev) =>
      prev.map((f, i) => (i === activeIdx ? { ...f, content: value, dirty: true } : f))
    );
  }, [activeIdx]);

  const handleRightChange = useCallback((value: string | undefined) => {
    if (value === undefined) return;
    setOpenFiles((prev) =>
      prev.map((f, i) => (i === rightActiveIdx ? { ...f, content: value, dirty: true } : f))
    );
  }, [rightActiveIdx]);

  const handleSave = async () => {
    if (!activeFile) return;
    setSaving(true);
    try {
      if (tauriMode) {
        await invokeSafe("write_file_content", { path: activeFile.path, content: activeFile.content });
      }
      setOpenFiles((prev) =>
        prev.map((f, i) => (i === activeIdx ? { ...f, dirty: false } : f))
      );
    } catch (e) {
      console.error("Save failed:", e);
    } finally {
      setSaving(false);
    }
  };

  const handleClose = (e: React.MouseEvent, idx: number) => {
    e.stopPropagation();
    const tabToClose = openFiles[idx];
    setClosedTabs((prev) => [...prev, tabToClose]);
    const next = openFiles.filter((_, i) => i !== idx);
    setOpenFiles(next);
    setActiveIdx(Math.max(0, Math.min(activeIdx, next.length - 1)));
    setRightActiveIdx(Math.max(0, Math.min(rightActiveIdx, next.length - 1)));
  };

  const handleCreateFile = () => {
    const name = `untitled-${openFiles.length + 1}.py`;
    const path = `scripts/${name}`;
    const newF: OpenFile = {
      name,
      path,
      content: "# New python script\n",
      dirty: true,
      lang: "python",
    };
    setOpenFiles((prev) => [...prev, newF]);
    setActiveIdx(openFiles.length);
  };

  const handleDeleteFile = () => {
    if (!activeFile) return;
    if (confirm(`Are you sure you want to delete ${activeFile.name}?`)) {
      const next = openFiles.filter((_, i) => i !== activeIdx);
      setOpenFiles(next);
      setActiveIdx(Math.max(0, Math.min(activeIdx, next.length - 1)));
    }
  };

  const ext = activeFile?.name.split(".").pop() ?? "";
  const lang = LANG_MAP[ext] ?? "plaintext";

  const rightExt = rightActiveFile?.name.split(".").pop() ?? "";
  const rightLang = LANG_MAP[rightExt] ?? "plaintext";

  return (
    <div className="flex h-full min-h-0 flex-col overflow-hidden" style={{ background: "#0d1117" }}>
      {/* Tab bar */}
      <div className="flex items-center border-b border-white/8 bg-black/40 overflow-x-auto no-scrollbar shrink-0">
        {openFiles.map((f, i) => (
          <FileBadge
            key={f.path}
            name={f.name}
            dirty={f.dirty}
            active={i === activeIdx}
            onClick={() => setActiveIdx(i)}
            onClose={(e) => handleClose(e, i)}
          />
        ))}
        <button
          onClick={handleCreateFile}
          className="p-2 text-gray-500 hover:text-white transition-colors"
          title="New File"
        >
          <Plus size={12} />
        </button>
        <div className="flex-1" />
        <div className="flex items-center gap-2 px-3">
          <button
            onClick={() => setIsSplit(!isSplit)}
            className={`p-1.5 rounded hover:bg-white/5 transition-all ${isSplit ? "text-blue-400" : "text-gray-500"}`}
            title="Split Editor"
          >
            <Columns size={12} />
          </button>
          <button
            onClick={() => setShowOutline(!showOutline)}
            className={`p-1.5 rounded hover:bg-white/5 transition-all ${showOutline ? "text-cyan-400" : "text-gray-500"}`}
            title="Toggle Outline"
          >
            <List size={12} />
          </button>
          {activeFile && (
            <button
              onClick={handleDeleteFile}
              className="p-1.5 text-gray-500 hover:text-red-400 transition-colors"
              title="Delete Active File"
            >
              <Trash size={12} />
            </button>
          )}
          {activeFile?.dirty && (
            <button
              onClick={handleSave}
              disabled={saving}
              className="flex items-center gap-1.5 rounded-lg border border-[var(--determinex-accent)]/30 bg-[var(--determinex-accent)]/10 px-2.5 py-1 text-[9px] font-bold uppercase tracking-widest text-[var(--determinex-accent)] transition-all hover:bg-[var(--determinex-accent)]/20 disabled:opacity-40"
            >
              <Save size={10} />
              {saving ? "Saving…" : "Save"}
            </button>
          )}
        </div>
      </div>

      {/* File path breadcrumb */}
      {activeFile && (
        <div className="flex items-center gap-1.5 border-b border-white/5 bg-black/20 px-4 py-1.5 shrink-0 justify-between">
          <div className="flex items-center gap-1.5">
            {activeFile.path.split("/").map((part, i, arr) => (
              <span key={i} className="flex items-center gap-1">
                <span className={`text-[9px] font-mono ${i === arr.length - 1 ? "text-white/60" : "text-gray-700"}`}>{part}</span>
                {i < arr.length - 1 && <ChevronRight size={9} className="text-gray-700" />}
              </span>
            ))}
          </div>
          {isSplit && rightActiveFile && (
            <div className="flex items-center gap-1.5 border-l border-white/10 pl-4">
              <span className="text-[9px] font-mono text-blue-400">Right: {rightActiveFile.name}</span>
            </div>
          )}
        </div>
      )}

      {/* Monaco Editor splits rendering */}
      {activeFile ? (
        <div className="flex-1 min-h-0 flex overflow-hidden">
          {/* Left editor */}
          <div className="flex-1 min-h-0 overflow-hidden flex flex-col">
            <MonacoEditor
              value={activeFile.content}
              language={lang}
              onChange={handleChange}
              theme="vs-dark"
              onMount={(editor) => {
                setEditorRef(editor);
                const monaco = (window as any).monaco;
                if (monaco) {
                  editor.addCommand(monaco.KeyMod.CtrlCmd | monaco.KeyCode.KeyS, () => {
                    handleSave();
                  });
                }
              }}
              options={{
                fontSize: 13,
                fontFamily: '"JetBrains Mono", monospace',
                fontLigatures: true,
                minimap: { enabled: false },
                lineNumbers: "on",
                scrollBeyondLastLine: false,
                renderLineHighlight: "gutter",
                wordWrap: "on",
                padding: { top: 16, bottom: 16 },
                tabSize: 2,
                insertSpaces: true,
                smoothScrolling: true,
                cursorBlinking: "phase",
                bracketPairColorization: { enabled: true },
              }}
            />
          </div>

          {/* Split Right editor */}
          {isSplit && rightActiveFile && (
            <div className="flex-1 min-h-0 overflow-hidden flex flex-col border-l border-white/10">
              <div className="p-1 bg-[#161b22]/50 border-b border-white/5 flex items-center gap-2">
                <select
                  value={rightActiveIdx}
                  onChange={(e) => setRightActiveIdx(Number(e.target.value))}
                  className="bg-[#0d1117] border border-white/10 rounded px-1 text-white text-[9px]"
                >
                  {openFiles.map((f, i) => (
                    <option key={f.path} value={i}>{f.name}</option>
                  ))}
                </select>
              </div>
              <MonacoEditor
                value={rightActiveFile.content}
                language={rightLang}
                onChange={handleRightChange}
                theme="vs-dark"
                options={{
                  fontSize: 12,
                  fontFamily: '"JetBrains Mono", monospace',
                  minimap: { enabled: false },
                  lineNumbers: "on",
                  scrollBeyondLastLine: false,
                  wordWrap: "on",
                  tabSize: 2,
                }}
              />
            </div>
          )}

          {/* Outline Sidebar */}
          {showOutline && (
            <div className="w-64 border-l border-white/10 bg-[#161b22]/90 flex flex-col font-mono text-[10px] text-gray-300">
              <div className="p-3 border-b border-white/5 flex items-center justify-between text-white font-bold bg-black/20">
                <span>OUTLINE & DIAGNOSTICS</span>
              </div>
              <div className="flex-1 overflow-y-auto p-3 space-y-4">
                {/* Diagnostics List */}
                <div>
                  <div className="text-gray-500 font-bold uppercase tracking-wider mb-1">Diagnostics ({diagnostics.length})</div>
                  {diagnostics.length === 0 ? (
                    <div className="text-gray-600 italic text-[9px]">No diagnostics found.</div>
                  ) : (
                    diagnostics.map((d, i) => (
                      <div key={i} className="flex gap-1.5 p-1 bg-black/10 rounded mb-1 text-gray-400">
                        <AlertTriangle className={`h-3 w-3 shrink-0 mt-0.5 ${d.severity === "error" ? "text-red-400" : "text-yellow-400"}`} />
                        <div>
                          <div className="text-white font-semibold">[Line {d.line}]</div>
                          <div>{d.message}</div>
                        </div>
                      </div>
                    ))
                  )}
                </div>
                {/* Outline Symbols */}
                <div>
                  <div className="text-gray-500 font-bold uppercase tracking-wider mb-1">Symbols ({symbols.length})</div>
                  {symbols.length === 0 ? (
                    <div className="text-gray-600 italic text-[9px]">No symbols defined.</div>
                  ) : (
                    symbols.map((s, i) => (
                      <div
                        key={i}
                        onClick={() => {
                          if (editorRef) {
                            editorRef.revealLineInCenter(s.line);
                            editorRef.setPosition({ lineNumber: s.line, column: 1 });
                            editorRef.focus();
                          }
                        }}
                        className="p-1 hover:bg-white/5 rounded cursor-pointer flex items-center justify-between text-gray-400 hover:text-white"
                      >
                        <span>{s.name}</span>
                        <span className="text-[8px] px-1 bg-cyan-900/30 text-cyan-400 rounded uppercase">{s.kind}</span>
                      </div>
                    ))
                  )}
                </div>
              </div>
            </div>
          )}
        </div>
      ) : (
        <div className="flex-1 flex flex-col items-center justify-center gap-4 text-center">
          <div className="h-16 w-16 rounded-2xl border border-white/8 bg-white/[0.03] flex items-center justify-center">
            <FileCode size={28} className="text-gray-700" />
          </div>
          <p className="text-[13px] font-bold text-gray-600">No files open</p>
          <p className="text-[11px] text-gray-700 font-mono">
            {tauriMode ? "Open a file from the Space panel" : "Open a file to start editing"}
          </p>
        </div>
      )}

      {/* Status bar */}
      <div className="flex items-center gap-4 border-t border-white/5 bg-black/50 px-4 py-1.5 shrink-0">
        {activeFile && (
          <>
            <span className="text-[9px] font-mono text-gray-700">{lang}</span>
            <span className="text-[9px] font-mono text-gray-700">UTF-8</span>
            <span className="text-[9px] font-mono text-gray-700">LF</span>
            {activeFile.dirty && (
              <span className="text-[9px] font-mono text-amber-500">● unsaved</span>
            )}
          </>
        )}
        <div className="flex-1" />
        {!tauriMode && (
          <span className="text-[8px] font-mono text-gray-500">
            Sandbox/Web Mock Save mode active
          </span>
        )}
      </div>
    </div>
  );
}
