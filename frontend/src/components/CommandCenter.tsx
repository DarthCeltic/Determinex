import React, { useState, useEffect } from "react";
import { getGitStatus, GitStatusResult } from "../lib/gitService";
import { invokeSafe } from "../lib/api";
import { useAiRouter } from "../contexts/AiRouterContext";
import { Activity, ShieldCheck, FileCode, CheckCircle, XCircle, AlertTriangle, PlayCircle } from "lucide-react";

type Props = {
  workspacePath: string;
};

export function CommandCenter({ workspacePath }: Props) {
  const [gitStatus, setGitStatus] = useState<GitStatusResult | null>(null);
  const [auditScore, setAuditScore] = useState<number | null>(null);
  const { activeRoute } = useAiRouter();

  useEffect(() => {
    if (!workspacePath) return;
    const fetchStatus = async () => {
      try {
        const gs = await getGitStatus(workspacePath);
        setGitStatus(gs);
      } catch (e) {
        console.error("Failed to load git status", e);
      }
      try {
        const auditData = await invokeSafe<any>("run_project_audit", {});
        if (auditData) {
          setAuditScore(auditData.score);
        }
      } catch (e) {
        console.error("Failed to run project audit", e);
      }
    };
    fetchStatus();
    const int = setInterval(fetchStatus, 30000);
    return () => clearInterval(int);
  }, [workspacePath]);

  const hasDirtyFiles = gitStatus && gitStatus.files.length > 0;
  const isReleaseReady = auditScore && auditScore >= 90;

  return (
    <div className="flex flex-col h-full bg-[#0d1117] text-[#c9d1d9] p-6 space-y-6 overflow-y-auto">
      <div className="flex items-center space-x-3 border-b border-[#30363d] pb-4">
        <Activity className="w-6 h-6 text-blue-400" />
        <h2 className="text-xl font-semibold text-[#f0f6fc]">Command Center</h2>
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
        <div className="bg-[#161b22] border border-[#30363d] rounded-lg p-5">
          <h3 className="text-sm font-semibold text-[#8b949e] mb-4 uppercase tracking-wider">Active Context</h3>
          <div className="space-y-4">
            <div className="flex justify-between items-center">
              <span className="text-sm">Model Route</span>
              <span className="px-2 py-1 bg-[#238636] text-white text-xs rounded-md font-mono">
                {activeRoute?.provider || "Default"} ({activeRoute?.kind || "None"})
              </span>
            </div>
            <div className="flex justify-between items-center">
              <span className="text-sm">Current Branch</span>
              <span className="text-sm font-mono text-[#58a6ff]">{gitStatus?.branch || "unknown"}</span>
            </div>
          </div>
        </div>

        <div className="bg-[#161b22] border border-[#30363d] rounded-lg p-5">
          <h3 className="text-sm font-semibold text-[#8b949e] mb-4 uppercase tracking-wider">Release Readiness</h3>
          <div className="space-y-4">
            <div className="flex items-center space-x-3">
              {auditScore === null ? (
                <div className="animate-pulse h-4 w-24 bg-[#30363d] rounded"></div>
              ) : (
                <>
                  {isReleaseReady ? <ShieldCheck className="w-5 h-5 text-green-400" /> : <AlertTriangle className="w-5 h-5 text-yellow-400" />}
                  <span className="text-sm">
                    Audit Score: <strong className={isReleaseReady ? "text-green-400" : "text-yellow-400"}>{auditScore}/100</strong>
                  </span>
                </>
              )}
            </div>
            <div className="flex items-center space-x-3">
              {hasDirtyFiles ? <XCircle className="w-5 h-5 text-red-400" /> : <CheckCircle className="w-5 h-5 text-green-400" />}
              <span className="text-sm">
                {hasDirtyFiles ? <span className="text-red-400">{gitStatus?.files.length} uncommitted changes</span> : "Working tree clean"}
              </span>
            </div>
          </div>
        </div>
      </div>

      <div className="bg-[#161b22] border border-[#30363d] rounded-lg p-5 flex-1">
        <h3 className="text-sm font-semibold text-[#8b949e] mb-4 uppercase tracking-wider">Next Recommended Action</h3>
        {hasDirtyFiles ? (
          <div className="flex flex-col items-center justify-center h-40 space-y-3">
            <FileCode className="w-10 h-10 text-yellow-400" />
            <p className="text-sm text-[#8b949e]">You have uncommitted work. Review and commit your changes.</p>
            <button className="px-4 py-2 bg-[#21262d] hover:bg-[#30363d] border border-[#30363d] rounded-md text-sm transition-colors">
              Open Source Control
            </button>
          </div>
        ) : isReleaseReady ? (
          <div className="flex flex-col items-center justify-center h-40 space-y-3">
            <PlayCircle className="w-10 h-10 text-green-400" />
            <p className="text-sm text-[#8b949e]">Project is healthy and ready for release.</p>
            <button className="px-4 py-2 bg-[#238636] hover:bg-[#2ea043] rounded-md text-sm text-white font-medium transition-colors">
              Launch Release Process
            </button>
          </div>
        ) : (
          <div className="flex flex-col items-center justify-center h-40 space-y-3">
            <AlertTriangle className="w-10 h-10 text-orange-400" />
            <p className="text-sm text-[#8b949e]">Project audit is below 90. Review the Problems panel for blockers.</p>
            <button className="px-4 py-2 bg-[#21262d] hover:bg-[#30363d] border border-[#30363d] rounded-md text-sm transition-colors">
              View Problems
            </button>
          </div>
        )}
      </div>
    </div>
  );
}
