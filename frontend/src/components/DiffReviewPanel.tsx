import React, { useEffect, useState } from "react";
import { invokeSafe } from "../lib/api";
import { DiffEditor } from "@monaco-editor/react";
import { Check, X, GitCompare, Save, Trash2, Loader2 } from "lucide-react";

export function DiffReviewPanel() {
  const [stagedDiffs, setStagedDiffs] = useState<any[]>([]);
  const [selectedDiffId, setSelectedDiffId] = useState<string | null>(null);
  const [loading, setLoading] = useState(true);
  const [actionInProgress, setActionInProgress] = useState(false);

  const fetchDiffs = async () => {
    try {
      const diffs = await invokeSafe<any[]>("get_staged_diffs", {});
      setStagedDiffs(diffs || []);
      if (diffs && diffs.length > 0 && !selectedDiffId) {
        setSelectedDiffId(diffs[0].id);
      } else if (!diffs || diffs.length === 0) {
        setSelectedDiffId(null);
      }
    } catch (e) {
      console.error("Failed to load staged diffs", e);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchDiffs();
    const int = setInterval(fetchDiffs, 10000);
    return () => clearInterval(int);
  }, []);

  const handleApply = async (id: string) => {
    setActionInProgress(true);
    try {
      await invokeSafe("apply_staged_diff", { id });
      await fetchDiffs();
    } catch (e) {
      console.error("Failed to apply diff", e);
    } finally {
      setActionInProgress(false);
    }
  };

  const handleReject = async (id: string) => {
    setActionInProgress(true);
    try {
      await invokeSafe("reject_staged_diff", { id });
      await fetchDiffs();
    } catch (e) {
      console.error("Failed to reject diff", e);
    } finally {
      setActionInProgress(false);
    }
  };

  const selectedDiff = stagedDiffs.find(d => d.id === selectedDiffId);

  if (loading && stagedDiffs.length === 0) {
    return <div className="flex-1 bg-[#0d1117] flex items-center justify-center"><Loader2 className="w-8 h-8 text-blue-500 animate-spin" /></div>;
  }

  return (
    <div className="flex h-full bg-[#0d1117] text-[#c9d1d9]">
      <div className="w-64 border-r border-[#30363d] bg-[#161b22] flex flex-col">
        <div className="p-4 border-b border-[#30363d] flex items-center gap-2">
          <GitCompare className="w-4 h-4 text-purple-400" />
          <h2 className="text-sm font-bold text-white">AI Proposed Changes</h2>
        </div>
        <div className="flex-1 overflow-y-auto">
          {stagedDiffs.length === 0 ? (
            <div className="p-4 text-xs text-[#8b949e] italic">No pending changes to review.</div>
          ) : (
            stagedDiffs.map(diff => (
              <div 
                key={diff.id} 
                onClick={() => setSelectedDiffId(diff.id)}
                className={"p-3 border-b border-[#30363d] cursor-pointer hover:bg-[#21262d] transition-colors " + (selectedDiffId === diff.id ? "bg-[#21262d] border-l-2 border-l-purple-500" : "")}
              >
                <div className="text-sm font-mono truncate text-blue-400">{diff.path.split(/[/\\]/).pop()}</div>
                <div className="text-xs text-[#8b949e] truncate">{diff.path}</div>
              </div>
            ))
          )}
        </div>
      </div>

      <div className="flex-1 flex flex-col">
        {selectedDiff ? (
          <>
            <div className="h-14 border-b border-[#30363d] bg-[#0d1117] px-4 flex items-center justify-between shrink-0">
              <div className="flex items-center gap-2">
                <span className="text-sm font-mono text-[#8b949e]">{selectedDiff.path}</span>
              </div>
              <div className="flex items-center gap-2">
                <button 
                  onClick={() => handleReject(selectedDiff.id)}
                  disabled={actionInProgress}
                  className="px-3 py-1.5 flex items-center gap-1.5 text-sm font-medium text-red-400 hover:bg-red-500/10 border border-red-500/20 rounded transition-colors disabled:opacity-50"
                >
                  <Trash2 className="w-4 h-4" /> Reject
                </button>
                <button 
                  onClick={() => handleApply(selectedDiff.id)}
                  disabled={actionInProgress}
                  className="px-3 py-1.5 flex items-center gap-1.5 text-sm font-medium text-green-400 bg-green-500/10 hover:bg-green-500/20 border border-green-500/20 rounded transition-colors disabled:opacity-50"
                >
                  <Save className="w-4 h-4" /> Apply Change
                </button>
              </div>
            </div>
            <div className="flex-1 min-h-0">
              <DiffEditor
                theme="vs-dark"
                original={selectedDiff.originalContent}
                modified={selectedDiff.proposedContent}
                options={{
                  readOnly: true,
                  renderSideBySide: true,
                  minimap: { enabled: false },
                  scrollBeyondLastLine: false,
                }}
              />
            </div>
          </>
        ) : (
          <div className="flex-1 flex flex-col items-center justify-center opacity-50">
            <Check className="w-16 h-16 text-green-500 mb-4" />
            <p className="text-lg">All caught up!</p>
            <p className="text-sm text-[#8b949e]">No AI changes pending your review.</p>
          </div>
        )}
      </div>
    </div>
  );
}
