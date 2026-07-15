import React, { useEffect, useState } from "react";
import { invokeSafe } from "../lib/api";
import { AlertCircle, FileWarning, ShieldAlert, XCircle, Code, Shield } from "lucide-react";

export function ProblemsPanel() {
  const [diagnostics, setDiagnostics] = useState<any[]>([]);
  const [auditBlockers, setAuditBlockers] = useState<any[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    async function fetchProblems() {
      setLoading(true);
      try {
        const diag = await invokeSafe<any[]>("get_lsp_diagnostics", { filePath: "" });
        if (diag) setDiagnostics(diag);
      } catch (e) {
        console.error("Failed to load LSP diagnostics", e);
      }

      try {
        const audit = await invokeSafe<any>("run_project_audit", {});
        if (audit && audit.blockers) {
          setAuditBlockers(audit.blockers);
        }
      } catch (e) {
        console.error("Failed to load project audit", e);
      }
      setLoading(false);
    }
    fetchProblems();
    const int = setInterval(fetchProblems, 60000);
    return () => clearInterval(int);
  }, []);

  const totalProblems = diagnostics.length + auditBlockers.length;

  return (
    <div className="flex flex-col h-full bg-[#0d1117] text-[#c9d1d9] border-t border-[#30363d] font-sans">
      <div className="flex items-center px-4 py-2 border-b border-[#30363d] bg-[#161b22]">
        <div className="flex items-center gap-2 text-sm font-medium">
          <AlertCircle className="w-4 h-4 text-red-400" />
          <span>Problems</span>
          <span className="ml-2 bg-[#30363d] text-xs px-2 py-0.5 rounded-full">{totalProblems}</span>
        </div>
      </div>

      <div className="flex-1 overflow-y-auto p-2">
        {loading && totalProblems === 0 ? (
          <div className="p-4 text-sm text-[#8b949e] animate-pulse">Scanning workspace...</div>
        ) : totalProblems === 0 ? (
          <div className="p-4 flex flex-col items-center justify-center text-center h-full space-y-3 opacity-60">
            <CheckCircle className="w-12 h-12 text-green-500" />
            <p className="text-sm">No problems have been detected in the workspace.</p>
          </div>
        ) : (
          <div className="space-y-1">
            {auditBlockers.map((blocker, idx) => (
              <div key={"audit-" + idx} className="group flex items-start gap-3 p-2 hover:bg-[#161b22] rounded cursor-pointer transition-colors">
                <ShieldAlert className="w-4 h-4 text-red-400 mt-0.5 shrink-0" />
                <div className="flex flex-col">
                  <span className="text-sm text-[#f0f6fc]">{blocker}</span>
                  <span className="text-xs text-[#8b949e] flex items-center gap-1"><Shield className="w-3 h-3" /> Project Audit Blocker</span>
                </div>
              </div>
            ))}

            {diagnostics.map((diag, idx) => (
              <div key={"diag-" + idx} className="group flex items-start gap-3 p-2 hover:bg-[#161b22] rounded cursor-pointer transition-colors">
                {diag.severity === "error" ? <XCircle className="w-4 h-4 text-red-400 mt-0.5 shrink-0" /> : <FileWarning className="w-4 h-4 text-yellow-400 mt-0.5 shrink-0" />}
                <div className="flex flex-col">
                  <span className="text-sm text-[#f0f6fc]">{diag.message}</span>
                  <span className="text-xs text-[#8b949e] flex items-center gap-1">
                    <Code className="w-3 h-3" /> {diag.file || "unknown file"}{diag.line ? ":" + diag.line : ""}
                  </span>
                </div>
              </div>
            ))}
          </div>
        )}
      </div>
    </div>
  );
}

function CheckCircle(props: any) {
  return <svg {...props} xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/><polyline points="22 4 12 14.01 9 11.01"/></svg>
}
