import React, { useEffect, useState } from "react";
import { invokeSafe } from "../lib/api";
import { ShieldCheck, ArrowRight, Server, Terminal, Settings, Loader2 } from "lucide-react";

type Props = {
  workspacePath: string;
  onClose: () => void;
};

export function WorkspaceOnboarding({ workspacePath, onClose }: Props) {
  const [analysis, setAnalysis] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [executing, setExecuting] = useState(false);
  const [executionResult, setExecutionResult] = useState<string | null>(null);

  useEffect(() => {
    async function analyze() {
      try {
        const result = await invokeSafe<any>("analyze_workspace", { workspace: workspacePath });
        setAnalysis(result);
      } catch (e) {
        console.error("Failed to analyze workspace", e);
      } finally {
        setLoading(false);
      }
    }
    analyze();
  }, [workspacePath]);

  const executeAction = async () => {
    if (!analysis?.actionCommand) {
      onClose();
      return;
    }
    setExecuting(true);
    setExecutionResult(null);
    try {
      const result = await invokeSafe<{ stdout: string; stderr: string; exit_code: number | null }>(
        "run_terminal_command",
        { command: analysis.actionCommand, cwd: workspacePath }
      );
      setExecutionResult(
        result && result.exit_code === 0
          ? `Done: ${analysis.actionCommand}`
          : `Failed (exit ${result?.exit_code}): ${result?.stderr || result?.stdout || "unknown error"}`
      );
    } catch (e) {
      setExecutionResult(`Failed to run: ${e}`);
    } finally {
      setExecuting(false);
    }
  };

  if (loading) {
    return (
      <div className="fixed inset-0 z-50 flex items-center justify-center bg-black/60 backdrop-blur-sm">
        <div className="bg-[#161b22] border border-[#30363d] rounded-xl p-8 w-full max-w-lg shadow-2xl flex flex-col items-center justify-center space-y-4">
          <div className="animate-spin rounded-full h-12 w-12 border-t-2 border-b-2 border-blue-500"></div>
          <p className="text-[#8b949e] animate-pulse">Scanning workspace stack...</p>
        </div>
      </div>
    );
  }

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center bg-black/60 backdrop-blur-sm">
      <div className="bg-[#161b22] border border-[#30363d] rounded-xl w-full max-w-xl shadow-2xl overflow-hidden">
        <div className="bg-[#21262d] border-b border-[#30363d] px-6 py-4 flex items-center justify-between">
          <h2 className="text-lg font-bold text-white flex items-center gap-2">
            <Server className="w-5 h-5 text-blue-400" /> Workspace Detected
          </h2>
        </div>
        
        <div className="p-6 space-y-6">
          <div className="bg-[#0d1117] border border-[#30363d] rounded-lg p-4 space-y-4">
            <div className="flex justify-between items-center">
              <span className="text-sm text-[#8b949e]">Inferred Stack</span>
              <div className="flex gap-2">
                {analysis?.inferredStack?.map((stack: string) => (
                  <span key={stack} className="px-2 py-1 bg-[#238636]/20 text-[#3fb950] border border-[#238636]/50 rounded text-xs font-mono">
                    {stack}
                  </span>
                ))}
              </div>
            </div>
            
            {analysis?.buildCommand && (
              <div className="flex justify-between items-center">
                <span className="text-sm text-[#8b949e]">Build Command</span>
                <span className="px-2 py-1 bg-gray-800 text-gray-300 rounded text-xs font-mono flex items-center gap-2">
                  <Terminal className="w-3 h-3" /> {analysis.buildCommand}
                </span>
              </div>
            )}
          </div>

          <div className="space-y-2">
            <h3 className="text-sm font-semibold text-white">Recommended Next Action</h3>
            <div className="p-4 border border-blue-500/30 bg-blue-500/10 rounded-lg flex items-start gap-4">
              <div className="mt-1 bg-blue-500/20 p-2 rounded-md">
                <ShieldCheck className="w-5 h-5 text-blue-400" />
              </div>
              <div className="flex-1">
                <h4 className="text-sm font-bold text-blue-300">{analysis?.recommendedAction}</h4>
                <p className="text-xs text-[#8b949e] mt-1">
                  Based on the detected stack, this is the safest first step to ensure your workspace is ready for AI ideation.
                </p>
              </div>
            </div>
          </div>

          {executionResult && (
            <div className="text-xs font-mono text-[#8b949e] bg-[#0d1117] border border-[#30363d] rounded p-2 whitespace-pre-wrap">
              {executionResult}
            </div>
          )}
        </div>

        <div className="bg-[#0d1117] border-t border-[#30363d] px-6 py-4 flex justify-end gap-3">
          <button onClick={onClose} className="px-4 py-2 text-sm text-[#8b949e] hover:text-white transition-colors">
            Dismiss
          </button>
          <button
            onClick={executeAction}
            disabled={executing}
            className="px-4 py-2 bg-[#238636] hover:bg-[#2ea043] disabled:opacity-60 text-white text-sm font-medium rounded-md shadow-sm flex items-center gap-2 transition-colors"
          >
            {executing ? (
              <>
                Running <Loader2 className="w-4 h-4 animate-spin" />
              </>
            ) : (
              <>
                Execute Action <ArrowRight className="w-4 h-4" />
              </>
            )}
          </button>
        </div>
      </div>
    </div>
  );
}
